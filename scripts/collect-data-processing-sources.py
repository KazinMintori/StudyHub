"""Inventory public course sources; keep full reference text outside published docs."""
import concurrent.futures
import hashlib
import json
import re
import tempfile
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
CACHE = Path(tempfile.gettempdir()) / 'studyhub-data-sources'
CACHE.mkdir(exist_ok=True)
WES = 'https://wesmckinney.com/book/'
IAI = 'https://courses.iaidev.com/programming-for-data-processing/2627-1/'


def get(url):
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    response.encoding = 'utf-8'
    return response


def collect(item):
    response = get(item['url'])
    soup = BeautifulSoup(response.text, 'html.parser')
    main = soup.select_one('main') or soup.body
    for node in main.select('script,style,nav'):
        node.decompose()
    headings = [n.get_text(' ', strip=True) for n in main.select('h1,h2,h3,h4')]
    text = main.get_text('\n', strip=True)
    (CACHE / (item['id'] + '.txt')).write_text(text, encoding='utf-8')
    (CACHE / (item['id'] + '.html')).write_text(response.text, encoding='utf-8')
    return {**item, 'resolvedUrl': response.url, 'status': response.status_code,
            'sha256': hashlib.sha256(response.content).hexdigest(), 'headings': headings}


def main():
    wes = BeautifulSoup(get(WES).text, 'html.parser')
    iai = BeautifulSoup(get(IAI).text, 'html.parser')
    items = []
    seen = set()
    for a in wes.select('a[href]'):
        label = a.get_text(' ', strip=True)
        match = re.match(r'^(\d+|[AB])\s+', label)
        if not match:
            continue
        key = match[1]
        if key in seen:
            continue
        seen.add(key)
        items.append({'id': 'wes-' + key.zfill(2), 'source': 'wes', 'chapter': key,
                      'title': label, 'url': urljoin(WES, a['href'])})
    seen = set()
    for a in iai.select('a[href]'):
        url = urljoin(IAI, a['href'])
        match = re.search(r'/lecture-(\d+)[^/]*\.html', url)
        if not match or match[1] in seen or int(match[1]) > 14:
            continue
        key = match[1]
        seen.add(key)
        items.append({'id': 'iai-' + key, 'source': 'iai', 'lecture': int(key),
                      'title': a.get_text(' ', strip=True), 'url': url})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(collect, items))
    inventory = {'checkedOn': '2026-10-18', 'records': records,
                 'unlistedIaiLectures': sorted(set(range(1, 15)) - {r['lecture'] for r in records if r['source'] == 'iai'}),
                 'excludedNotebook': 'https://colab.research.google.com/github/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lecture-01.ipynb',
                 'handling': 'Topic inventory only. Protected prose and figures are not published. Draft original teaching material.'}
    target = ROOT / 'raw_materials/xu-ly-du-lieu/source-inventory.json'
    target.write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'wes': sum(r['source'] == 'wes' for r in records),
                      'iai': sum(r['source'] == 'iai' for r in records),
                      'unlisted': inventory['unlistedIaiLectures'], 'cache': str(CACHE)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
