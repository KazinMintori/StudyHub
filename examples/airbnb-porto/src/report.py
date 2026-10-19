"""Tạo báo cáo HTML/PDF từ cùng các bảng và hình của một lượt chạy."""
import html
import os
import shutil
import subprocess
import sys
from pathlib import Path


def export_report(reports, figures, summary, values):
    reports, figures = Path(reports), Path(figures)
    escape = lambda value: html.escape(str(value))
    selected = [k for k in values if k['aggregation_level'] == 'city_sample' and k['value'] != '' and k['kpi_id'] != 'negative_review_share']
    names = {'listing_count': 'Số listing', 'entire_home_share': 'Cả chỗ ở (%)', 'median_minimum_nights': 'Số đêm tối thiểu (trung vị)', 'no_review_share': 'Chưa có review (%)', 'mean_available_next30': 'Lịch sẵn có (%)', 'median_advertised_price_latest': 'Giá chào (EUR/đêm)'}
    table = ''.join(f'<tr><td>{escape(k["snapshot_date"])}</td><td>{escape(names[k["kpi_id"]])}</td><td>{float(k["value"]):.2f}</td><td>{k["eligible_count"]}</td></tr>' for k in selected)
    sheets = [f'''<article><p class="eyebrow">StudyHub · Dự án thực hành độc lập</p><h1>Phân tích Porto</h1><p>Mẫu {summary['cohort_size']} listing thuộc giao {summary['cohort_intersection']} ID qua bốn snapshot. Dữ liệu xử lý gồm {summary['listing_rows']} hàng listing và {summary['calendar_rows']} hàng lịch trong các cửa sổ đã chọn.</p><h2>Kết quả tổng hợp</h2><table><thead><tr><th>Snapshot</th><th>Chỉ số</th><th>Giá trị</th><th>N hợp lệ</th></tr></thead><tbody>{table}</tbody></table><h2>Cách đọc</h2><p>Giá chỉ dùng mốc cuối. Lịch sẵn có không xác nhận giao dịch đặt phòng. Mẫu theo giao ID không đo listing mới xuất hiện hoặc biến mất.</p><p>Baseline đã chạy trên {summary['sampled_reviews']} review duy nhất. Lượt này không công bố chất lượng LLM hoặc nhãn người chưa đo.</p><p class="source">Lượt chạy: {escape(summary['run_id'])}<br>Nguồn: Inside Airbnb, CC BY 4.0. URL và checksum nằm trong source-manifest.json.</p></article>''']
    captions = ['Phân bố listing trong mẫu theo khu vực, không phải mật độ toàn thành phố.', 'Các cửa sổ tương lai cùng dài30ngày, thuộc các snapshot khác nhau. Độ phủ ghi trong CSV.', 'Loại phòng được tổng hợp từ mẫu mốc cuối.', 'Giá chào nguồn, không phải doanh thu hoặc ADR thực thu.', 'Tỷ lệ listing chưa có review không trực tiếp đo mức hài lòng.']
    for i, image in enumerate(sorted(figures.glob('*.svg'))):
        caption = captions[i] if i < len(captions) else 'Kết quả LLM, đối chiếu độ phủ và evaluation.json.'
        area_table = ''
        if i == 0:
            areas = sorted([k for k in values if k['aggregation_level']=='neighbourhood' and k['snapshot_date']==summary['snapshots'][-1] and k['kpi_id']=='listing_count'], key=lambda k:float(k['value']), reverse=True)[:6]
            area_table = '<h3>Sáu khu có nhiều listing mẫu nhất</h3><table>'+''.join(f'<tr><td>{escape(k["neighbourhood"])}</td><td>{int(float(k["value"]))}</td></tr>' for k in areas)+'</table>'
        sheets.append(f'<article class="figure-page {"map-page" if i==0 else ""}"><h2>Hình {i+1}</h2><img src="{image.resolve().as_uri()}" alt="{escape(caption)}">{area_table}<p>{escape(caption)}</p></article>')
    style = '''@page{size:A4;margin:14mm}*{box-sizing:border-box}body{font:10pt/1.45 Arial,sans-serif;color:#262139;margin:0}article{break-after:page}article:last-child{break-after:auto}h1{font-size:25pt;margin:7pt 0 12pt}h2{font-size:14pt;margin:12pt 0 7pt;break-after:avoid}.eyebrow,.source{color:#625a75;font-size:8pt}table{border-collapse:collapse;width:100%;font-size:8.5pt}td,th{padding:3.5pt 6pt;border-bottom:1px solid #ded8e8;text-align:left}th{background:#efebf7}tr{break-inside:avoid}.figure-page img{display:block;max-width:100%;max-height:224mm;width:auto;margin:0 auto}.figure-page p{font-size:10pt}'''
    style += '.map-page img{width:100%;height:148mm;object-fit:contain}.map-page h3{font-size:11pt;margin:8pt 0 4pt}.map-page td{font-size:9pt;padding:3pt 5pt}'
    document = '<!doctype html><html lang="vi"><meta charset="utf-8"><title>Phân tích Porto</title><style>'+style+'</style><body>'+''.join(sheets)+'</body></html>'
    source = reports/'report.html'
    source.write_text(document, encoding='utf-8')
    candidates = [os.environ.get('CHROME_PATH'), 'C:/Program Files/Google/Chrome/Application/chrome.exe', 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe', shutil.which('google-chrome'), shutil.which('chromium'), '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome']
    browser = next((p for p in candidates if p and Path(p).is_file()), None)
    if not browser:
        return {'pdf': 'not_exported', 'reason': 'Set CHROME_PATH or print report.html to PDF'}
    target = reports/'report.pdf'
    profile = reports/'browser-profile'
    result = subprocess.run([browser, '--headless', '--disable-gpu', '--no-pdf-header-footer', '--no-first-run', '--user-data-dir='+str(profile.resolve()), '--print-to-pdf='+str(target.resolve()), source.resolve().as_uri()], capture_output=True, timeout=90)
    if result.returncode or not target.exists() or target.stat().st_size < 1000:
        raise RuntimeError('PDF export failed; HTML report retained')
    return {'pdf': 'exported', 'bytes': target.stat().st_size}
