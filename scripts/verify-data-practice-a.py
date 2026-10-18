"""Run the authored IAI 02-05 practice, then check independent small fixtures."""
import csv
import json
import math
import re
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'raw_materials/xu-ly-du-lieu/practice'


def execute(file):
    namespace = {}
    blocks = re.findall(r'^```python\n(.*?)^```', file.read_text(encoding='utf-8'), re.M | re.S)
    with redirect_stdout(StringIO()):
        for number, code in enumerate(blocks, 1):
            exec(compile(code, f'{file.name}:block{number}', 'exec'), namespace)
    return namespace, len(blocks)


def main():
    total = 0
    namespaces = {}
    for file in sorted(FOLDER.glob('iai-a-chapter-*.md')):
        namespace, count = execute(file)
        namespaces[file.stem.rsplit('-', 1)[1]] = namespace
        total += count
    n3 = namespaces['3']
    rows = [
        {'id':'1','neighbourhood':'A','price':'10','number_of_reviews':'0','last_review':''},
        {'id':'2','neighbourhood':'A','price':'','number_of_reviews':'1','last_review':'2025-01-01'},
        {'id':'3','neighbourhood':'B','price':'30','number_of_reviews':'0','last_review':'2025-02-01'},
        {'id':'4','neighbourhood':'A','price':'0','number_of_reviews':'2','last_review':'2025-03-01'},
    ]
    f = n3['to_float']
    assert [f(x) for x in ['45647', '59000.5', '', 'N/A', None, 'NaN', 'inf']] == [45647.0, 59000.5, None, None, None, None, None]
    report, top5, maximum, conflicts = n3['tong_hop_python'](rows)
    assert report['so_phong_co_gia'] == 3 and report['so_thieu_gia'] == 1
    assert math.isclose(report['gia_trung_binh_clp'], 40 / 3)
    assert report['gia_trung_vi_clp'] == 10
    assert report['gia_trung_vi_theo_khu'] == {'A':5, 'B':30}
    assert report['ty_le_chua_review'] == .5 and top5 == [('A',3), ('B',1)]
    assert maximum['id'] == '3' and [r['id'] for r in conflicts] == ['3']
    assert n3['xep_hang_khu'](rows, 1) == [('B',1,30), ('A',2,5)]
    assert n3['xep_hang_khu'](rows) == []
    empty = n3['tong_hop_python']([])[0]
    assert empty['gia_trung_vi_clp'] is None and empty['ty_le_chua_review'] is None
    with tempfile.TemporaryDirectory(prefix='studyhub-practice-a-') as directory:
        path = Path(directory)
        with (path / 'rows.csv').open('w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        assert n3['doc_bang'](path / 'rows.csv') == rows
        assert n3['ghi_doc_bao_cao'](report, path / 'report.json') == report
        verify_additional(namespaces, path)
    print(json.dumps({'practiceGroup':'IAI02-05', 'pythonBlocks':total, 'numericAndBoundaryFixtures':'passed'}, ensure_ascii=False))


def verify_additional(namespaces, path):
    # Each additional chapter's fixture is added alongside that practice file.
    if '5' in namespaces:
        df = pd.DataFrame({
            'id':['1','2','3','4'], 'name':['a','b','c','d'],
            'neighbourhood':['Ñuñoa','Ñuñoa','Ñuñoa','B'],
            'room_type':['Entire home/apt','Private room','Entire home/apt','Private room'],
            'price':[100.,50.,np.nan,200.], 'number_of_reviews_ltm':[2,0,1,4],
            'calculated_host_listings_count':[5,1,7,1],
        })
        n = namespaces['5']
        original = df.copy(deep=True)
        nu, report, quote, cheap = n['ho_so_quan'](df, 'Ñuñoa')
        assert report['so_cho_o'] == 3 and report['gia_trung_vi'] == 75
        assert report['ty_trong_thi_truong'] == .75
        assert report['ty_le_duoi_tv_thanh_pho'] == .5
        assert report['ty_le_duoi_tv_moi_hang'] == 1 / 3
        np.testing.assert_allclose(quote['price'], [90,50,np.nan], equal_nan=True)
        np.testing.assert_allclose(quote['tien_3_dem'], [270,150,np.nan], equal_nan=True)
        pd.testing.assert_frame_equal(df, original)
        assert n['luu_ho_so_quan'](report, path / 'district.csv')['so_cho_o'].iloc[0] == 3
    if '8' in namespaces:
        n = namespaces['8']
        prices = pd.DataFrame({'id':[1,2,3], 'price':[10000.,50000.,np.nan], 'phan_khuc':['re','trung',None]})
        joined = n['ghep_phi'](prices)
        np.testing.assert_allclose(joined['gia_tong'], [11000,56500,np.nan], equal_nan=True)
        assert len(joined) == len(prices) and joined['phi_dich_vu'].isna().sum() == 1
    if '10' in namespaces:
        n = namespaces['10']
        data = pd.DataFrame({'id':[1,2,3,4], 'name':['a','b','c','d'], 'neighbourhood':['A','A','B','B'],
            'price':[10000.,100000.,50000.,np.nan], 'number_of_reviews_ltm':[1,2,3,4],
            'calculated_host_listings_count':[1,5,2,7]})
        result = n['phan_tich_nhom'](data, toi_thieu=2)
        assert len(result['du_quy_mo']) == 4
        assert result['tong_hop'].loc['cao', 'so_phong'] == 1
        assert result['du_lieu']['chuyen'].tolist() == [False,True,False,True]
        maxima = n['dat_nhat_tung_quan'](result['du_quy_mo'])
        assert maxima['id'].tolist() == [2,3]
        shares = result['ty_trong_phan_khuc']
        np.testing.assert_allclose(shares.sum(axis=1), [1,1])
        assert n['quan_gia_thap'](data, toi_thieu=2)['neighbourhood'].iloc[0] == 'B'
    if '11' in namespaces:
        counts = namespaces['11']['dem_review_nam']([{'date':'2025-01-01'}, {'date':'2025-12-01'}, {'date':'2026-06-01'}])
        assert counts == {'2025':2, '2026':1}


if __name__ == '__main__':
    main()
