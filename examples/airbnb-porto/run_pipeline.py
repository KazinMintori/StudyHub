#!/usr/bin/env python3
"""Chạy dữ liệu thật. Không tự sinh dữ liệu thay thế khi đầu vào lỗi."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import sys
import time
import urllib.request
from collections import Counter
from pathlib import Path

from src.baseline_classifier import classify_review_baseline
from src.charts import render_all
from src.core import blank_manual_template, choose_cohort, kpis, read_selected, write_csv
from src.review_analysis import call_gemini, evaluate
from src.report import export_report


def digest(path):
    sha = hashlib.sha256()
    with Path(path).open('rb') as stream:
        while chunk := stream.read(1024*1024):
            sha.update(chunk)
    return sha.hexdigest()


def get_sources(root, config):
    raw = root/'data/raw'
    manifest_path = raw/'source-manifest.json'
    old = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else []
    previous = {r['url']: r for r in old}
    previous_locations = {(r['snapshot_date'], r['file']): r for r in old}
    tasks = [(date, 'data/'+name+'.csv.gz', name+'.csv.gz') for date in config['snapshots'] for name in ['listings', 'calendar', 'reviews']]
    tasks.append((config['latest_snapshot'], 'visualisations/neighbourhoods.geojson', 'neighbourhoods.geojson'))
    manifest = []
    for date, relative, filename in tasks:
        url = 'https://data.insideairbnb.com/'+config['public_root'].strip('/')+'/'+date+'/'+relative
        path = raw/date/filename
        path.parent.mkdir(parents=True, exist_ok=True)
        recorded = previous_locations.get((date, filename))
        if path.exists() and (not recorded or recorded['url'] != url):
            raise ValueError('Cached source is not associated with the requested URL: '+filename+' '+date)
        if not path.exists():
            temporary = path.with_suffix(path.suffix+'.part')
            for attempt in range(3):
                try:
                    size = 0
                    with urllib.request.urlopen(url, timeout=60) as response, temporary.open('wb') as output:
                        expected = response.headers.get('Content-Length')
                        while chunk := response.read(1024*1024):
                            size += len(chunk)
                            if size > config.get('max_download_bytes', 400*1024*1024):
                                raise ValueError('Download exceeds configured bound')
                            output.write(chunk)
                        if expected and size != int(expected):
                            raise ValueError('Incomplete download')
                    temporary.replace(path)
                    break
                except Exception:
                    if attempt == 2:
                        raise
                    time.sleep(2 ** attempt)
        checksum = digest(path)
        if url in previous and previous[url]['sha256'] != checksum:
            raise ValueError('Cached source checksum changed: '+filename+' '+date)
        manifest.append({'snapshot_date': date, 'file': filename, 'url': url, 'bytes': path.stat().st_size, 'sha256': checksum})
    raw.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    return raw, manifest


def qa_summary(listings, exceptions, values, config):
    output = []
    rules = [('PRICE_MISSING_OR_UNREADABLE', 'EXCLUDE_PRICE_KPI_ONLY'), ('PRICE_NON_POSITIVE', 'EXCLUDE_PRICE_KPI_ONLY'), ('ROOM_TYPE_UNKNOWN', 'EXCLUDE_ROOM_SHARE_ONLY'), ('MINIMUM_NIGHTS_INVALID', 'EXCLUDE_MINIMUM_NIGHTS_ONLY'), ('REVIEW_COUNT_INVALID', 'EXCLUDE_NO_REVIEW_SHARE_ONLY'), ('NEIGHBOURHOOD_MISSING', 'KEEP_AS_UNMAPPED')]
    for date in config['snapshots']:
        group = [r for r in listings if r['snapshot_date'] == date]
        for rule, action in rules:
            if rule.startswith('PRICE_') and date != config['latest_snapshot']:
                continue
            affected = sum(e['rule'] == rule and e['snapshot_date'] == date and e['table'] == 'listings' for e in exceptions)
            if not affected:
                continue
            count = next(k for k in values if k['snapshot_date'] == date and k['neighbourhood'] == 'all' and k['kpi_id'] == 'listing_count')['value']
            output.append({'snapshot_date': date, 'rule_id': rule, 'severity': 'WARN' if affected else 'INFO', 'action': action, 'records_before': len(group), 'records_after': len(group), 'affected': affected, 'kpi': 'listing_count', 'kpi_before': count, 'kpi_after': count, 'notes': 'No row deletion. Price-specific eligibility is shown in kpi_city.csv; missing price has no numeric pre-cleaning price value.'})
    for rule in sorted({e['rule'] for e in exceptions if e['table'] != 'listings'}):
        affected = sum(e['rule'] == rule for e in exceptions)
        output.append({'snapshot_date': 'all', 'rule_id': rule, 'severity': 'WARN', 'action': 'LOG_AND_EXCLUDE_AFFECTED_METRIC', 'records_before': '', 'records_after': '', 'affected': affected, 'kpi': '', 'kpi_before': '', 'kpi_after': '', 'notes': 'See exceptions.csv; no synthetic replacement.'})
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', default='configs/porto.json')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--skip-llm', action='store_true')
    mode.add_argument('--run-llm', action='store_true')
    parser.add_argument('--llm-limit', type=int, default=300)
    parser.add_argument('--model', default='')
    args = parser.parse_args()
    csv.field_size_limit(10*1024*1024)
    config_path = Path(args.config).resolve()
    config = json.loads(config_path.read_text(encoding='utf-8'))
    if len(config['snapshots']) != len(set(config['snapshots'])) or not config['snapshots']:
        raise ValueError('Snapshots must be nonempty and distinct')
    if config['currency'] != 'EUR':
        raise ValueError('This example explicitly supports EUR; adapt price logic before another currency')
    root = config_path.parent.parent
    model = args.model or config.get('llm_config', {}).get('model', '')
    if args.run_llm and (not model or not os.environ.get('GEMINI_API_KEY')):
        raise ValueError('--run-llm needs a selected model and GEMINI_API_KEY')
    if args.llm_limit < 1:
        raise ValueError('--llm-limit must be positive')
    run_id = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())+'-'+hashlib.sha256(config_path.read_bytes()).hexdigest()[:8]+'-'+str(time.time_ns())[-6:]
    run = root/'runs'/run_id
    processed = run/'processed'
    reports = run/'reports'
    figures = run/'figures'
    reports.mkdir(parents=True, exist_ok=True)
    def save(name, data):
        (reports/name).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    save('run-status.json', {'run_id': run_id, 'status': 'running', 'configuration': config})
    print('[1/6] Verify public source files', flush=True)
    raw, manifest = get_sources(root, config)
    save('source-manifest.json', manifest)
    print('[2/6] Select reproducible cohort', flush=True)
    cohort, intersection = choose_cohort(raw, config['snapshots'], config['cohort_size'], config['cohort_seed'])
    write_csv(processed/'cohort.csv', [{'listing_id': i} for i in cohort])
    print('[3/6] Stream listings, calendar and reviews for four snapshots', flush=True)
    listings, calendar, sample, counts, exceptions, unique_reviews = read_selected(raw, config, set(cohort), processed)
    print('[4/6] Compute verified aggregates and baseline', flush=True)
    values = kpis(listings, calendar, config)
    manual = root/'data/samples/manual_labels.csv'
    blank_manual_template(sample, manual, config)
    baseline = []
    for row in sample:
        pred = classify_review_baseline(row['review_id'], row['comments'])
        prediction = {k: pred[k] for k in ['sentiment', 'aspects', 'language']}
        if prediction['language'] == 'other':
            prediction['language'] = 'und'
        baseline.append({'review_id': row['review_id'], 'status': 'success', 'prediction': prediction})
    llm = []
    if args.run_llm:
        print('[5/6] Call selected Gemini model with content-keyed cache', flush=True)
        for row in sample[:args.llm_limit]:
            llm.append(call_gemini(row, model, root/'data/llm_cache'))
    else:
        print('[5/6] Skip API calls; preserve blank human labels', flush=True)
    save('baseline-predictions.json', baseline)
    save('llm-predictions.json', llm)
    evaluation = evaluate(manual, baseline, llm, sample)
    save('evaluation.json', evaluation)
    valid = [r for r in llm if r.get('status') == 'success']
    negative = sum(r['prediction']['sentiment'] == 'negative' for r in valid)
    # Deduplicated review sample has one aggregation scope; never repeat its result across snapshots.
    values.append({'kpi_id': 'negative_review_share', 'snapshot_date': 'review_sample', 'aggregation_level': 'city_sample', 'neighbourhood': 'all', 'value': 100*negative/len(valid) if valid else '', 'unit': 'percent', 'numerator': negative if valid else '', 'denominator': len(valid), 'eligible_count': len(valid), 'population_count': len(sample), 'currency': '', 'status': 'computed_unvalidated' if valid and evaluation['status'] != 'completed' else 'completed' if valid else 'no_valid_predictions' if llm else 'not_run', 'notes': 'LLM predictions only; coverage='+str(len(valid)/len(sample) if sample else 0)})
    write_csv(processed/'kpi_city.csv', [k for k in values if k['aggregation_level'] == 'city_sample'])
    write_csv(processed/'kpi_neighbourhood.csv', [k for k in values if k['aggregation_level'] == 'neighbourhood'])
    write_csv(reports/'qa_report.csv', qa_summary(listings, exceptions, values, config))
    write_csv(reports/'source-counts.csv', counts)
    print('[6/6] Render actual results and publish this run pointer', flush=True)
    render_all(listings, values, config, raw/config['latest_snapshot']/'neighbourhoods.geojson', figures)
    if valid:
        from src.charts import SVG
        chart = SVG('Cảm xúc trong mẫu LLM', f'N hợp lệ = {len(valid)}/{len(sample)} · Chất lượng xem evaluation.json', 360)
        for i, sentiment in enumerate(['positive', 'mixed', 'negative']):
            n = sum(r['prediction']['sentiment'] == sentiment for r in valid)
            chart.text(20, 120+i*70, sentiment, 16)
            chart.rect(115, 101+i*70, 150*n/len(valid), 25, '#6948af')
            chart.text(290, 120+i*70, n, 16)
        chart.save(figures/'06-cam-xuc-llm.svg')
    summary = {'city': config['city'], 'snapshots': config['snapshots'], 'cohort_size': len(cohort), 'cohort_intersection': intersection, 'listing_rows': len(listings), 'calendar_rows': len(calendar), 'unique_cohort_reviews': unique_reviews, 'sampled_reviews': len(sample), 'source_bytes': sum(x['bytes'] for x in manifest), 'source_files': len(manifest), 'baseline_predictions': len(baseline), 'llm_success': len(valid), 'manual_evaluation': evaluation['status'], 'run_id': run_id, 'figures': len(list(figures.glob('*.svg'))), 'config_sha256': hashlib.sha256(config_path.read_bytes()).hexdigest()}
    save('summary.json', summary)
    report = ['# Báo cáo thực hành Porto', '', '## Phạm vi', f'Mẫu {len(cohort)} listing thuộc giao {intersection} ID qua bốn snapshot. Kết quả không đại diện toàn thành phố.', '', '## KPI đã chạy', '| Snapshot | Chỉ số | Giá trị | Đơn vị | N hợp lệ |', '| --- | --- | --- | --- | --- |']
    for k in values:
        if k['aggregation_level'] == 'city_sample' and k['value'] != '':
            report.append(f'| {k["snapshot_date"]} | {k["kpi_id"]} | {k["value"]:.4f} | {k["unit"]} | {k["eligible_count"]} |')
    report += ['', '## Hình', *[f'![{p.stem}](../figures/{p.name})' for p in sorted(figures.glob('*.svg'))], '', '## Diễn giải và giới hạn', 'Chỉ dùng giá mốc cuối. Lịch sẵn có không xác nhận đặt phòng hoặc doanh thu. Các review lặp giữa snapshot chỉ được chọn một lần.', 'Bộ nhãn tay không được điền bằng mô hình. Kết quả nhãn người và API được theo dõi riêng trong evaluation.json.', '', '## Nguồn', 'Inside Airbnb, https://insideairbnb.com/get-the-data/, CC BY 4.0. URL và checksum từng tệp nằm trong source-manifest.json.']
    (reports/'report.md').write_text('\n'.join(report)+'\n', encoding='utf-8')
    summary['report_export'] = export_report(reports, figures, summary, values)
    save('summary.json', summary)
    save('run-status.json', {'run_id': run_id, 'status': 'data_complete', 'llm': 'executed' if args.run_llm else 'not_run', 'evaluation': evaluation['status']})
    pointer = root/'latest-run.json'
    temp = pointer.with_suffix('.tmp')
    temp.write_text(json.dumps({'run_id': run_id, 'path': str(run.relative_to(root)), 'status': 'data_complete'}, indent=2)+'\n', encoding='utf-8')
    temp.replace(pointer)
    print(json.dumps(summary, indent=2), flush=True)
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f'Pipeline failed: {type(error).__name__}: {error}', file=sys.stderr)
        raise SystemExit(1)
