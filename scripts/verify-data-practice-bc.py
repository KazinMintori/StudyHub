"""Execute IAI06-14 practice and test independent offline fixtures, including plots."""
import json
import math
import re
import tempfile
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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


def verify_io(n, folder):
    l = pd.DataFrame({'id':pd.Series(['P1','P2','P3'],dtype='string'), 'name':['a','b','c'],
        'room_type':['Entire home/apt','Private room','Private room'],
        'number_of_reviews':[2,1,0], 'first_review':pd.to_datetime(['2025-01-01','2025-01-02',None]),
        'last_review':pd.to_datetime(['2025-01-03','2025-01-02',None])})
    c,p,sizes = n['luu_hai_dang'](l[n['COT_5']],folder/'formats')
    assert c['id'].tolist() == l['id'].tolist() and sizes['csv_bytes'] > 0 and sizes['parquet_bytes'] > 0
    payload = {'timezone':'America/Santiago','daily_units':{'temperature_2m_max':'°C'},
               'daily':{'time':['2025-01-01','2025-01-02'],'temperature_2m_max':[20.,30.]}}
    class Response:
        url = 'https://example.invalid/weather?fixture=1'
        content = json.dumps(payload,ensure_ascii=False).encode('utf-8')
        status_checked = False
        def json(self):
            return payload
        def raise_for_status(self):
            self.status_checked = True
    response = Response()
    class Session:
        def get(self,url,params,timeout):
            assert url.startswith('https://archive-api.open-meteo.com/')
            assert params['timezone'] == 'America/Santiago' and params['start_date'] == '2025-01-01'
            assert timeout == 30
            return response
    weather = n['lay_thoi_tiet']('2025-01-01','2025-01-02',folder/'weather',Session())
    assert response.status_checked
    assert (folder/'weather/weather-2025-01-01-2025-01-02.json').read_bytes() == response.content
    rv = pd.DataFrame({'listing_id':['P1','P1','P2','X','P3'],
                       'date':['2025-01-01','2025-01-01','2025-01-02','2025-02-01','2026-01-01']})
    joined,corr = n['ghep_theo_ngay'](weather,rv,'2025-01-01','2025-01-02')
    assert joined['so_review'].tolist() == [2,1] and math.isclose(corr,-1)
    sql = n['truy_van_review'](l,rv)
    assert sql['theo_nam']['n'].sum() == 5
    assert sql['review_theo_loai']['n'].sum() == 4
    assert sql['listing_theo_loai']['so_co_danh_gia'].sum() == 2
    assert len(sql['tu_100']) == 0


def verify_cleaning(n, folder):
    prices = pd.Series(['$1,200.00',' $850.00 ',None,'liên hệ','từ $500','$24,50.00','$95.5'])
    values,errors,valid = n['doc_gia_chuoi'](prices)
    assert values.iloc[:2].tolist() == [1200,850] and values.iloc[2:].isna().all()
    assert errors.tolist() == [False,False,False,True,True,True,True]
    rv = pd.DataFrame({'comments':['Near the metro<br/>Wifi is poor','cerca de todo','cerca del parque',None]})
    result = n['khao_sat_comments'](rv)
    assert result['so_thieu'] == 1 and result['so_br'] == 1
    assert result['tu_sau_gan'].tolist() == ['metro','todo','parque']
    assert '<br/>' in rv.loc[0,'comments'] and '<br/>' not in result['sach'].iloc[0]
    assert len(n['xem_tu_nghi_van'](result,['todo'])['todo']) == 1
    assert n['doc_danh_sach']('["Wifi", "Washer, dryer"]') == ['Wifi','Washer, dryer']
    assert n['doc_danh_sach'](None) is None
    area = n['trich_dien_tich'](pd.Series(['45 m2','30m²','45.5 m2','45,5 m²','30m2x','x30m2','-30m2',None]))
    np.testing.assert_allclose(area.to_numpy(dtype=float,na_value=np.nan), [45,30,45.5,45.5,np.nan,np.nan,np.nan,np.nan],equal_nan=True)
    ds = pd.DataFrame({'id':['P1','P2','P3'], 'room_type':['A','A','B'],
        'price':[100.,np.nan,200.], 'number_of_reviews':[1,0,0],
        'reviews_per_month':[1.,np.nan,np.nan], 'number_of_reviews_ltm':[1,0,0]})
    original = ds.copy(deep=True)
    rpm,imputed,flag = n['dien_theo_y_nghia'](ds)
    assert rpm.tolist() == [1,0,0] and imputed.tolist() == [100,100,200]
    assert flag.tolist() == [False,True,False]
    pd.testing.assert_frame_equal(ds,original)
    expected = pd.DataFrame({'thieu':[True,False,False,False,False,False],
        'khong_duong':[False,True,True,False,False,False], 'cao':[False,False,False,False,True,True]},
        index=['P6','P2','P9','P1','P5','P3'])
    sample = pd.DataFrame({'price':[np.nan,0,-5,100,101,200]},index=expected.index)
    for dtype in ['float64','Float64']:
        flags = n['kiem_gia'](sample.astype(dtype),100)
        pd.testing.assert_frame_equal(flags,expected)
    _,_,p99,_,comparison = n['so_sanh_cach_xu_ly'](pd.DataFrame({'price':[10.,12.,14.,16.,100.,np.nan]}))
    assert comparison.loc['co_gia_duong','so_cho_o'] == 5
    assert comparison.loc['bo_tren_p99','so_cho_o'] == 4
    assert comparison.loc['chan_p99','so_cho_o'] == 5 and p99 < 100
    reviews = pd.DataFrame({'review_id':['R1','R2','R1','R3'], 'listing_id':['P1','P1','P1','P2'],
        'date':pd.to_datetime(['2026-06-28']*4), 'noi_dung':['Yên tĩnh','Sạch sẽ','Yên tĩnh','Thuận tiện']})
    assert n['bo_ban_nhap_lap'](reviews)['review_id'].tolist() == ['R1','R2','R3']
    r = pd.DataFrame({'listing_id':['P1','P9','P1',None,'P2'],
        'date':pd.to_datetime(['2026-06-29','2026-06-30',None,'2026-06-28','2026-06-27'])}, index=[9,3,7,1,5])
    flags = n['kiem_reviews'](r,['P1','P2'],pd.Timestamp('2026-06-29'))
    assert flags['sau_moc'].tolist() == [False,True,False,False,False]
    assert flags['id_khong_khop'].tolist() == [False,True,False,True,False]
    assert flags.sum().sum() == 4 and flags.any(axis=1).sum() == 3
    report,detail = n['luu_kiem_tra'](ds,r,150,pd.Timestamp('2026-06-29'),folder/'qa.csv')
    assert len(report) == 6 and len(detail) == 3
    assert (report.loc[report['bang'].eq('listings'),'tong_hang'] == 3).all()
    grouped,conflicts = n['gop_gia_khong_mau_thuan'](n['gia_nhap'])
    assert len(conflicts) == 2 and conflicts['id'].eq('P2').all()
    values = grouped.set_index(['id','ky'])['gia']
    assert values.loc[('P3','T6')] == 110 and pd.isna(values.loc[('P4','T6')])
    aligned = n['doi_chieu_review'](ds,r)
    assert aligned.loc['P1','dem_ca_file'] == 2 and aligned.loc['P1','den_moc'] == 1
    assert aligned.loc['P3','dem_ca_file'] == 0
    types = pd.Series(['Nguyên căn','Phòng riêng','Nguyên căn',None,'Nguyên căn'])
    history = pd.DataFrame({'id':['P2','P1','P1','P2','P1','P2','P1','P2'],
        'ky':[3,1,4,1,2,2,3,4], 'gia':[np.nan,100,130,np.nan,np.nan,200,np.nan,np.nan]})
    temperatures = pd.Series([18,np.nan,np.nan,24,np.nan],index=pd.to_datetime(
        ['2026-06-01','2026-06-02','2026-06-05','2026-06-07','2026-06-08']))
    filled,h,interpolated = n['ba_cach_dien'](types,history,temperatures)
    assert filled.iloc[3] == 'Nguyên căn'
    np.testing.assert_allclose(h['dien'],[100,100,np.nan,130,np.nan,200,200,np.nan],equal_nan=True)
    np.testing.assert_allclose(interpolated,[18,19,22,24,np.nan],equal_nan=True)


def verify_time(n):
    dates = pd.to_datetime(['2022-01-01','2023-02-01','2024-02-29','2025-01-01','2025-01-02','2025-03-31',
        '2025-11-20','2025-11-21','2025-11-22','2025-11-23','2025-11-24','2025-11-25','2025-11-26','2026-03-01','2026-06-29','2026-06-30'])
    rv = pd.DataFrame({'listing_id':['P1']*len(dates),'date':dates})
    r,outside,errors = n['chon_den_moc'](rv,pd.Timestamp('2026-06-29'))
    assert len(outside) == 1 and errors.empty
    q,complete,daily,rolling,maximum,window = n['dem_va_truot'](r,pd.Timestamp('2026-06-29'))
    assert complete.index[-1] == pd.Timestamp('2026-03-31')
    assert len(daily) == 365 and rolling.iloc[:6].isna().all()
    assert len(window) == 7
    rates = n['so_cung_quy'](r,complete)
    assert np.isclose(rates.loc['2026-03-31'],1/3-1)
    n['so_thang_theo_ngay'](r)
    assert (pd.Timestamp('2026-03-31')-pd.Timestamp('2026-01-01')).days+1 == 90
    assert (pd.Timestamp('2026-06-29')-pd.Timestamp('2026-04-01')).days+1 == 90
    fig,_ = n['ve_cua_so'](daily,rolling)
    plt.close(fig)


def verify_plots(n,folder):
    import geopandas as gpd
    from shapely.geometry import box
    ds = pd.DataFrame({'id':['P1','P2','P3','P4'], 'name':['a','b','c','d'],
        'neighbourhood':['Providencia','Providencia','Ñuñoa','Ñuñoa'],
        'room_type':['Entire home/apt','Private room','Entire home/apt','Private room'],
        'price':[100.,50.,80.,40.], 'calculated_host_listings_count':[5,1,5,1],
        'availability_365':[0,365,100,360], 'longitude':[-70.6,-70.7,-70.65,-70.66],
        'latitude':[-33.4,-33.5,-33.45,-33.46]})
    rv = pd.DataFrame({'listing_id':['P1','P1','P2','P3'], 'date':['2025-01-01','2025-02-01','2026-05-01','2026-06-30']})
    figs,counts,stats,ends = n['tao_ba_hinh'](ds,rv,folder/'plots',toi_thieu=1)
    assert counts.index.max() <= pd.Timestamp('2026-05-31') and ends == (1,2)
    assert len(list((folder/'plots').glob('*.png'))) == 3
    n['sua_truc_cot'](ds,['Providencia','Ñuñoa'])
    n['boxplot_quy_mo'](ds)
    geo = gpd.GeoDataFrame({'neighbourhood':['Providencia','Ñuñoa','Không có listing']},
        geometry=[box(0,0,1,1),box(1,0,2,1),box(2,0,3,1)],crs='EPSG:4326')
    mapped,_,axes = n['cap_ban_do'](geo,ds)
    assert mapped['n'].tolist() == [2,2,0] and pd.isna(mapped['gia_tv'].iloc[-1])
    assert all(not ax.axison for ax in axes)
    _,_,ratios = n['sua_ky_goc'](rv)
    assert set(ratios) == {2019,2020}
    interactive,top = n['diem_tuong_tac'](ds)
    assert len(interactive.data[0].x) == 4 and len(top) == 4
    plt.close('all')


def main():
    namespaces,total = {},0
    for file in sorted(FOLDER.glob('iai-bc*chapter-*.md')):
        n,count = execute(file)
        key = 'schema' if 'schema' in file.stem else file.stem.rsplit('-',1)[1]
        namespaces[key] = n
        total += count
    with tempfile.TemporaryDirectory(prefix='studyhub-practice-bc-') as directory:
        path = Path(directory)
        verify_io(namespaces['6'],path)
        verify_cleaning(namespaces['7'],path)
        verify_time(namespaces['11'])
        verify_plots(namespaces['9'],path)
    assert namespaces['schema']['accuracy'] == .625
    assert sorted(namespaces['schema']['loi_schema']) == [2,5]
    assert namespaces['13']['gop'].to_dict() == {'T6':41.8,'T9':45.0}
    print(json.dumps({'practiceGroup':'IAI06-14','pythonBlocks':total,
        'offlineFixtures':'passed','http':'injected response, no network','plots':'matplotlib, seaborn, geopandas, plotly verified'},ensure_ascii=False))


if __name__ == '__main__':
    main()
