"""Sinh hình SVG vừa màn hình nhỏ từ bảng đã tính, không có dữ liệu thay thế."""
import html
import json
import math
import textwrap
from collections import Counter
from pathlib import Path

INK = '#262139'
MUTED = '#625a75'
PURPLE = '#6948af'
TEAL = '#267d70'
PALE = '#efebf7'


class SVG:
    def __init__(self, title, subtitle, height=500):
        self.height = height
        self.parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 {height}" width="360" height="{height}" role="img"><title>{html.escape(title)}</title><rect width="360" height="{height}" fill="#fffdf9" rx="12"/>']
        self.text(20, 30, title, 18, weight='700')
        self.wrap(20, 57, subtitle, 38, 14, MUTED)

    def text(self, x, y, text, size=16, color=INK, anchor='start', weight='400'):
        self.parts.append(f'<text x="{x:.2f}" y="{y:.2f}" font-family="Arial, sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{html.escape(str(text))}</text>')

    def wrap(self, x, y, text, width=35, size=15, color=INK):
        lines = textwrap.wrap(text, width=width, break_long_words=False)
        for i, line in enumerate(lines):
            self.text(x, y+i*(size+5), line, size, color)
        return y+len(lines)*(size+5)

    def rect(self, x, y, w, h, color, stroke='none'):
        self.parts.append(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{color}" stroke="{stroke}" rx="3"/>')

    def line(self, x1, y1, x2, y2, color=MUTED):
        self.parts.append(f'<path d="M{x1:.2f} {y1:.2f}L{x2:.2f} {y2:.2f}" stroke="{color}" stroke-width="1.5" fill="none"/>')

    def save(self, path):
        self.parts.append('</svg>')
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        Path(path).write_text('\n'.join(self.parts), encoding='utf-8')


def render_all(listings, kpis, config, geojson, output):
    output = Path(output)
    latest = [r for r in listings if r['snapshot_date'] == config['latest_snapshot']]
    count = len(latest)
    city = [k for k in kpis if k['aggregation_level'] == 'city_sample']
    counts = Counter(r['neighbourhood_cleansed'] for r in latest)
    geo = json.loads(Path(geojson).read_text(encoding='utf-8'))
    if geo.get('type') != 'FeatureCollection' or not geo.get('features'):
        raise ValueError('GeoJSON must contain actual features')
    features = geo['features']
    def polygons(feature):
        geometry = feature['geometry']
        if geometry['type'] == 'Polygon':
            return [geometry['coordinates']]
        if geometry['type'] == 'MultiPolygon':
            return geometry['coordinates']
        raise ValueError('Unsupported geographic geometry')
    points = [p for f in features for poly in polygons(f) for ring in poly for p in ring]
    x0, x1 = min(p[0] for p in points), max(p[0] for p in points)
    y0, y1 = min(p[1] for p in points), max(p[1] for p in points)
    cos = math.cos(math.radians((y0+y1)/2))
    scale = min(310/((x1-x0)*cos), 240/(y1-y0))
    project = lambda p: (25+(p[0]-x0)*cos*scale, 100+(y1-p[1])*scale)
    svg = SVG('Listing mẫu theo khu vực', f'Bộ Porto · {config["latest_snapshot"]} · N = {count}', 450)
    maximum = max(counts.values(), default=1)
    for feature in features:
        name = feature['properties'].get('neighbourhood', '')
        n = counts.get(name, 0)
        color = '#e7e2ef' if not n else '#c8badf' if n < maximum/3 else '#9d83c5' if n < 2*maximum/3 else PURPLE
        for poly in polygons(feature):
            path = ''
            for ring in poly:
                # Reduce display points only. Original geometry remains in raw.
                step = max(1, len(ring)//250)
                path += ' '.join(('M' if i == 0 else 'L')+f'{project(p)[0]:.2f},{project(p)[1]:.2f}' for i, p in enumerate(ring[::step]))+' Z '
            svg.parts.append(f'<path d="{path}" fill="{color}" fill-rule="evenodd" stroke="#fff" stroke-width=".7"><title>{html.escape(name)}: {n} listing mẫu</title></path>')
    svg.text(20, 375, 'Số listing trong mẫu', 16, weight='700')
    first, second = math.ceil(maximum/3)-1, math.ceil(2*maximum/3)-1
    ranges = [('#e7e2ef', '0'), ('#c8badf', f'1–{first}'), ('#9d83c5', f'{first+1}–{second}'), (PURPLE, f'{second+1}–{maximum}')]
    for i, (color, label) in enumerate(ranges):
        svg.rect(20+i*80, 390, 28, 18, color)
        svg.text(54+i*80, 405, label, 12)
    svg.text(20, 435, 'Ranh giới giản lược từ GeoJSON nguồn.', 14, MUTED)
    svg.save(output/'01-ban-do.svg')

    svg = SVG('Lịch sẵn có 30 ngày tới', 'Trung bình tỷ lệ ngày hợp lệ theo listing. Không phải tỷ lệ đặt phòng.', 430)
    svg.line(48, 130, 48, 330)
    svg.line(48, 330, 335, 330)
    for value in [0, 25, 50, 75, 100]:
        y = 330-value*2
        svg.line(48, y, 335, y, '#ded8e8')
        svg.text(39, y+5, str(value), 14, anchor='end')
    observations = [k for k in city if k['kpi_id'] == 'mean_available_next30']
    prior = None
    for i, kpi in enumerate(observations):
        x = 65+i*82
        if kpi['value'] == '':
            prior = None
            continue
        y = 330-float(kpi['value'])*2
        if prior:
            svg.line(*prior, x, y, TEAL)
        svg.parts.append(f'<circle cx="{x}" cy="{y}" r="5" fill="{TEAL}"/>')
        svg.text(x, y-14, f'{float(kpi["value"]):.1f}%', 15, anchor='middle', weight='700')
        svg.text(x, 360, kpi['snapshot_date'][5:7]+'/'+kpi['snapshot_date'][:4], 14, anchor='middle')
        prior = x, y
    svg.wrap(20, 395, 'Bốn cửa sổ tương lai ở bốn snapshot, không phải lịch sử doanh thu tháng.', 41, 14, MUTED)
    svg.save(output/'02-lich-san-co.svg')

    room_counts = Counter(r['room_type'] for r in latest)
    svg = SVG('Loại chỗ ở trong mẫu', f'Mốc {config["latest_snapshot"]} · N = {count}', 180+len(room_counts)*85)
    names = {'Entire home/apt': 'Cả chỗ ở', 'Private room': 'Phòng riêng', 'Shared room': 'Phòng chung', 'Hotel room': 'Phòng khách sạn'}
    for i, (name, n) in enumerate(sorted(room_counts.items())):
        y = 110+i*85
        svg.text(20, y, names.get(name, name), 16)
        svg.rect(20, y+12, 220*n/count, 22, PURPLE)
        svg.text(250, y+30, f'{n} ({100*n/count:.1f}%)', 14)
    svg.save(output/'03-loai-cho-o.svg')

    prices = [r['price_advertised_eur'] for r in latest if r['price_advertised_eur'] is not None and r['price_advertised_eur'] > 0]
    bounds = [0, 50, 100, 150, 200, 300, math.inf]
    bins = [sum(lo <= p < hi for p in prices) for lo, hi in zip(bounds, bounds[1:])]
    svg = SVG('Số listing theo khoảng giá', f'EUR/đêm · {config["latest_snapshot"]} · N giá hợp lệ = {len(prices)}', 540)
    maximum = max(bins, default=1) or 1
    for i, (lo, hi, n) in enumerate(zip(bounds, bounds[1:], bins)):
        y = 130+i*53
        svg.text(20, y+17, f'{lo}–<{hi}' if math.isfinite(hi) else f'≥{lo}', 15)
        svg.rect(110, y, 165*n/maximum, 25, TEAL)
        svg.text(292, y+18, n, 16)
    svg.wrap(20, 495, 'Mỗi cột là một khoảng giá, không phải các khoảng có độ rộng bằng nhau.', 40, 14, MUTED)
    svg.save(output/'04-phan-bo-gia.svg')

    areas = [area for area, _ in counts.most_common(6)]
    if len(counts)>6:
        areas.append('Các khu còn lại')
    heat_height = 150+sum(20*len(textwrap.wrap(area, 38))+83 for area in areas)
    svg = SVG('Listing chưa có review', 'Tỷ lệ % theo khu vực và snapshot. Mỗi hàng có mẫu số riêng.', heat_height)
    values = {(k['neighbourhood'], k['snapshot_date']): k for k in kpis if k['aggregation_level'] == 'neighbourhood' and k['kpi_id'] == 'no_review_share'}
    if 'Các khu còn lại' in areas:
        for date in config['snapshots']:
            others = [r for r in listings if r['snapshot_date']==date and r['neighbourhood_cleansed'] not in areas and r['number_of_reviews'] is not None and r['number_of_reviews']>=0]
            values[('Các khu còn lại', date)]={'value':100*sum(r['number_of_reviews']==0 for r in others)/len(others) if others else ''}
    y = 110
    for area in areas:
        y = svg.wrap(20, y, area, 38, 15)+3
        for i, date in enumerate(config['snapshots']):
            k = values.get((area, date))
            value = None if not k or k['value'] == '' else float(k['value'])
            x = 20+i*80
            color = PALE if value is None or value == 0 else '#ded1ef' if value < 10 else '#c3a7e1' if value < 25 else '#9471bd'
            svg.rect(x, y, 72, 30, color)
            svg.text(x+36, y+21, 'n/a' if value is None else f'{value:.1f}%', 14, anchor='middle')
            svg.text(x+36, y+51, date[5:7]+'/'+date[2:4], 14, anchor='middle')
        y += 80
    svg.save(output/'05-review-theo-khu.svg')
