"""Dữ liệu thật, khóa rõ ràng và các phép tính có mẫu số tường minh."""
from __future__ import annotations

import csv
import datetime as dt
import gzip
import hashlib
import json
import math
import random
import re
import statistics
from collections import defaultdict
from pathlib import Path

ROOM_TYPES = {'Entire home/apt', 'Private room', 'Shared room', 'Hotel room'}


def write_csv(path, records, fields=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    records = list(records)
    fields = fields or (list(records[0]) if records else ['status'])
    tmp = path.with_suffix(path.suffix + '.tmp')
    with tmp.open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    tmp.replace(path)


def rows(path, required):
    """Giữ nguyên chuỗi mã. Thiếu nguồn/cột bắt buộc thì báo lỗi."""
    path = Path(path)
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        missing = set(required) - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f'{path.name}: Missing columns {sorted(missing)}')
        yield from reader


def number(value, integer=False):
    try:
        result = float(value)
        if not math.isfinite(result) or (integer and not result.is_integer()):
            return None
        return int(result) if integer else result
    except (TypeError, ValueError):
        return None


def price(value, decimal='.', thousands=','):
    """Dấu phân cách lấy từ cấu hình, không đoán '1.234' là 1234 hay 1,234."""
    if value is None:
        return None
    text = re.sub(r'[$€£\s]|EUR|USD|GBP', '', str(value).strip(), flags=re.I)
    if not text:
        return None
    if decimal == thousands:
        raise ValueError('Decimal and thousands separators must differ')
    sign = r'[+-]?'
    sep = re.escape(thousands)
    dec = re.escape(decimal)
    pattern = sign + rf'(?:\d+|\d{{1,3}}(?:{sep}\d{{3}})+)(?:{dec}\d+)?'
    if not re.fullmatch(pattern, text):
        return None
    return number(text.replace(thousands, '').replace(decimal, '.'))


def choose_cohort(raw, snapshots, size, seed):
    sets = [{row['id'] for row in rows(raw/date/'listings.csv.gz', ['id']) if row['id']} for date in snapshots]
    common = sorted(set.intersection(*sets))
    if len(common) < size:
        raise ValueError(f'Only {len(common)} common listing IDs; requested {size}')
    return sorted(random.Random(seed).sample(common, size)), len(common)


def read_selected(raw, config, ids, processed):
    snapshots = config['snapshots']
    listings, calendar, reviews, appearances, exceptions = [], [], {}, [], []
    counts = []
    for date in snapshots:
        seen = {}
        source_count = 0
        for row in rows(raw/date/'listings.csv.gz', ['id', 'room_type', 'minimum_nights', 'number_of_reviews', 'neighbourhood_cleansed']):
            source_count += 1
            lid = row['id']
            if lid not in ids:
                continue
            if lid in seen:
                raise ValueError(f'Duplicate listing key in snapshot {date}')
            parsed_price = price(row.get('price'), config.get('price_decimal', '.'), config.get('price_thousands', ','))
            item = {'snapshot_date': date, 'id': lid, 'neighbourhood_cleansed': row['neighbourhood_cleansed'].strip() or 'unmapped', 'room_type': row['room_type'], 'price_raw': row.get('price', ''), 'price_advertised_eur': parsed_price, 'minimum_nights': number(row['minimum_nights'], True), 'number_of_reviews': number(row['number_of_reviews'], True)}
            flags = []
            if date == config['latest_snapshot'] and parsed_price is None:
                flags.append('PRICE_MISSING_OR_UNREADABLE')
            elif date == config['latest_snapshot'] and parsed_price <= 0:
                flags.append('PRICE_NON_POSITIVE')
            if item['room_type'] not in ROOM_TYPES:
                flags.append('ROOM_TYPE_UNKNOWN')
            if item['minimum_nights'] is None or item['minimum_nights'] < 1:
                flags.append('MINIMUM_NIGHTS_INVALID')
            if item['number_of_reviews'] is None or item['number_of_reviews'] < 0:
                flags.append('REVIEW_COUNT_INVALID')
            if item['neighbourhood_cleansed'] == 'unmapped':
                flags.append('NEIGHBOURHOOD_MISSING')
            item['qa_flags'] = '|'.join(flags)
            for flag in flags:
                exceptions.append({'table': 'listings', 'snapshot_date': date, 'record_id': lid, 'rule': flag, 'action': 'RETAIN_AND_LIMIT_AFFECTED_KPI'})
            seen[lid] = item
        if set(seen) != set(ids):
            raise ValueError(f'Cohort mismatch in {date}')
        listings.extend(seen.values())
        start = dt.date.fromisoformat(date)
        end = start + dt.timedelta(days=config['calendar_window_days'])
        calendar_seen = {}
        calendar_source_count = 0
        for row in rows(raw/date/'calendar.csv.gz', ['listing_id', 'date', 'available']):
            calendar_source_count += 1
            if row['listing_id'] not in ids:
                continue
            try:
                day = dt.date.fromisoformat(row['date'])
            except ValueError:
                exceptions.append({'table': 'calendar', 'snapshot_date': date, 'record_id': row['listing_id'], 'rule': 'DATE_INVALID', 'action': 'EXCLUDE_CALENDAR_METRIC'})
                continue
            if not start <= day < end:
                continue
            key = (row['listing_id'], row['date'])
            if key in calendar_seen:
                raise ValueError(f'Duplicate calendar key in {date}')
            available = row['available'].strip().lower()
            if available not in {'t', 'f'}:
                exceptions.append({'table': 'calendar', 'snapshot_date': date, 'record_id': row['listing_id'], 'rule': 'AVAILABLE_INVALID', 'action': 'EXCLUDE_CALENDAR_METRIC'})
            calendar_seen[key] = {'snapshot_date': date, 'listing_id': row['listing_id'], 'date': row['date'], 'available': available, 'valid': available in {'t', 'f'}}
        calendar.extend(calendar_seen.values())
        review_source_count = 0
        for row in rows(raw/date/'reviews.csv.gz', ['id', 'listing_id', 'date', 'comments']):
            review_source_count += 1
            if row['listing_id'] not in ids or not row['id']:
                continue
            rid = row['id']
            item = {'review_id': rid, 'listing_id': row['listing_id'], 'date': row['date'], 'comments': row['comments'], 'snapshot_date': date}
            appearances.append({'snapshot_date': date, 'review_id': rid})
            if rid in reviews and any(reviews[rid][key] != item[key] for key in ['comments', 'listing_id', 'date']):
                exceptions.append({'table': 'reviews', 'snapshot_date': date, 'record_id': rid, 'rule': 'REVIEW_VERSION_CONFLICT', 'action': 'KEEP_FIRST_AND_REPORT_CONFLICT'})
            else:
                reviews.setdefault(rid, item)
        counts.append({'snapshot_date': date, 'source_listings': source_count, 'source_calendar': calendar_source_count, 'source_reviews': review_source_count, 'selected_listings': len(seen), 'selected_calendar': len(calendar_seen)})
    conflicts = {row['record_id'] for row in exceptions if row['rule'] == 'REVIEW_VERSION_CONFLICT'}
    candidates = [r for r in reviews.values() if r['review_id'] not in conflicts and r['comments'].strip()]
    candidates.sort(key=lambda r: hashlib.sha256(f"{config['cohort_seed']}:{r['review_id']}".encode()).hexdigest())
    sample = candidates[:config['review_sample_size']]
    write_csv(processed/'selected_listings.csv', listings)
    write_csv(processed/'selected_calendar.csv', calendar)
    write_csv(processed/'selected_reviews.csv', sample)
    write_csv(processed/'review_appearances.csv', appearances)
    write_csv(processed/'exceptions.csv', exceptions, ['table', 'snapshot_date', 'record_id', 'rule', 'action'])
    return listings, calendar, sample, counts, exceptions, len(reviews)


def kpis(listings, calendar, config):
    """Tính lại từ hàng hợp lệ, không lấy trung bình các trung vị khu vực."""
    by_day = defaultdict(list)
    for row in calendar:
        if row['valid']:
            by_day[(row['snapshot_date'], row['listing_id'])].append(row)
    result = []
    for date in config['snapshots']:
        group = [r for r in listings if r['snapshot_date'] == date]
        groups = [('all', group)] + [(area, [r for r in group if r['neighbourhood_cleansed'] == area]) for area in sorted({r['neighbourhood_cleansed'] for r in group})]
        for area, data in groups:
            def add(name, values, value, unit, numerator='', status='completed', notes=''):
                result.append({'kpi_id': name, 'snapshot_date': date, 'aggregation_level': 'city_sample' if area == 'all' else 'neighbourhood', 'neighbourhood': area, 'value': '' if value is None else round(value, 8), 'unit': unit, 'numerator': numerator, 'denominator': len(values), 'eligible_count': len(values), 'population_count': len(data), 'currency': 'EUR' if unit == 'EUR/night' else '', 'status': status if value is not None else 'unavailable' if status == 'completed' else status, 'notes': notes})
            add('listing_count', data, len({r['id'] for r in data}), 'listings')
            rooms = [r for r in data if r['room_type'] in ROOM_TYPES]
            n = sum(r['room_type'] == 'Entire home/apt' for r in rooms)
            add('entire_home_share', rooms, 100*n/len(rooms) if rooms else None, 'percent', n)
            nights = [r['minimum_nights'] for r in data if r['minimum_nights'] is not None and r['minimum_nights'] >= 1]
            add('median_minimum_nights', nights, statistics.median(nights) if nights else None, 'nights')
            prices = [r['price_advertised_eur'] for r in data if r['price_advertised_eur'] is not None and r['price_advertised_eur'] > 0]
            if date == config['latest_snapshot']:
                add('median_advertised_price_latest', prices, statistics.median(prices) if prices else None, 'EUR/night')
            else:
                add('median_advertised_price_latest', [], None, 'EUR/night', status='not_applicable_latest_only')
            review_counts = [r['number_of_reviews'] for r in data if r['number_of_reviews'] is not None and r['number_of_reviews'] >= 0]
            n = sum(count == 0 for count in review_counts)
            add('no_review_share', review_counts, 100*n/len(review_counts) if review_counts else None, 'percent', n)
            rates, observed = [], 0
            for row in data:
                days = by_day.get((date, row['id']), [])
                if days:
                    rates.append(sum(x['available'] == 't' for x in days)/len(days))
                    observed += len(days)
            coverage = observed/(len(data)*config['calendar_window_days']) if data else 0
            add('mean_available_next30', rates, 100*statistics.mean(rates) if rates else None, 'percent', notes=f'Calendar coverage={coverage:.8f}; observed valid days={observed}; expected days={len(data)*config["calendar_window_days"]}; not occupancy')
            # Review aggregate belongs to one deduplicated sample, not four repeated snapshots.
    return result


def blank_manual_template(sample, path, config):
    """Không ghi đè tệp người đã gán nhãn."""
    fields = ['review_id', 'listing_id', 'comments', 'split', 'sentiment', 'aspects_json', 'language', 'annotator']
    template = []
    count = config['dev_sample_size'] + config['test_sample_size']
    for i, row in enumerate(sample[:count]):
        template.append({'review_id': row['review_id'], 'listing_id': row['listing_id'], 'comments': row['comments'], 'split': 'dev' if i < config['dev_sample_size'] else 'test', 'sentiment': '', 'aspects_json': '', 'language': '', 'annotator': ''})
    if not Path(path).exists():
        write_csv(path, template, fields)
    else:
        existing = list(rows(path, fields))
        if [(r['review_id'], r['comments'], r['split']) for r in existing] != [(r['review_id'], r['comments'], r['split']) for r in template]:
            raise ValueError('Manual label file belongs to different sample/content/split; preserve it and choose a new path')
    return template
