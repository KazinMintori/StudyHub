## Thực hành lịch quan sát và kỳ so sánh

### Ngày sai định dạng khác ngày thiếu

::: exercise Theo dõi lỗi chuyển đổi ngày
Ngày được ghi theo DD/MM/YYYY. Ngày vào là `28/02/2026`, `03/07/2026`, `31/06/2026`, `None`. Ngày ra tương ứng là `03/03/2026`, `06/07/2026`, `05/07/2026`, `12/07/2026`. Tính số đêm và đánh dấu riêng ngày vào có dữ liệu nhưng không đọc được.
:::

::: solution
```python
import pandas as pd
import numpy as np
dat_thu = pd.DataFrame({"vao":["28/02/2026","03/07/2026","31/06/2026",None],
    "ra":["03/03/2026","06/07/2026","05/07/2026","12/07/2026"]}, index=["D1","D2","D3","D4"])
vao = pd.to_datetime(dat_thu["vao"], format="%d/%m/%Y", errors="coerce")
ra = pd.to_datetime(dat_thu["ra"], format="%d/%m/%Y", errors="coerce")
so_dem = (ra - vao).dt.days
loi_vao = dat_thu["vao"].notna() & vao.isna()
assert so_dem.loc[["D1","D2"]].tolist() == [3,3]
assert so_dem.loc[["D3","D4"]].isna().all()
assert loi_vao.loc[loi_vao].index.tolist() == ["D3"]
```

Sau chuyển đổi, D3 và D4 đều có NaT. Chỉ đối chiếu với cột gốc mới phân biệt được ngày không tồn tại và ô đã thiếu từ nguồn.
:::

### Quý đã kết thúc và bảy ngày gần nhất

::: exercise Không dùng kỳ chưa trọn để kết luận giảm
Với review Santiago ngày 29/06/2026, tách các hàng sau mốc chụp để đối chiếu, giữ cả hàng cùng ngày. Đếm theo quý, chỉ giữ các quý đã kết thúc. So cách chọn ở mốc 29/06 và 30/06.

Trong riêng năm 2025, tạo đủ 365 ngày và tính trung bình bảy ngày kết thúc tại mỗi ngày, `min_periods=7`. Tìm ngày có trung bình lớn nhất, in bảy số gốc để đối chiếu và vẽ số hàng ngày cùng trung bình trong tháng 11. Không dùng thông tin sau ngày đang xét.
:::

::: solution
```python
def chon_den_moc(rv, moc):
    data = rv.copy()
    data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d", errors="coerce")
    loi = data.loc[data["date"].isna()].copy()
    ngoai_moc = data.loc[data["date"].gt(moc)].copy()
    r = data.loc[data["date"].notna() & data["date"].le(moc)].set_index("date").sort_index()
    return r, ngoai_moc, loi

def dem_va_truot(r, moc):
    quy = r.resample("QE").size()
    quy_day_du = quy.loc[quy.index <= moc]
    lich_2025 = pd.date_range("2025-01-01","2025-12-31",freq="D")
    ngay = r.loc["2025"].resample("D").size().reindex(lich_2025,fill_value=0)
    tb7 = ngay.rolling(7,min_periods=7).mean()
    ngay_cao_nhat = tb7.idxmax()
    cua_so = ngay.loc[ngay_cao_nhat-pd.Timedelta(days=6):ngay_cao_nhat]
    assert len(cua_so) == 7 and np.isclose(cua_so.mean(),tb7.loc[ngay_cao_nhat])
    return quy, quy_day_du, ngay, tb7, ngay_cao_nhat, cua_so

dem_quy_thu = pd.Series([100,120], index=pd.to_datetime(["2026-03-31","2026-06-30"]))
assert len(dem_quy_thu.loc[dem_quy_thu.index <= pd.Timestamp("2026-06-29")]) == 1
assert len(dem_quy_thu.loc[dem_quy_thu.index <= pd.Timestamp("2026-06-30")]) == 2

def ve_cua_so(ngay, tb7):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(figsize=(8,4))
    ngay.loc["2025-11"].plot(ax=ax,color="0.6",label="Mỗi ngày")
    tb7.loc["2025-11"].plot(ax=ax,label="Trung bình 7 ngày gần nhất")
    ax.set(xlabel="Ngày",ylabel="Số đánh giá",title="Số đánh giá và trung bình bảy ngày trong tháng 11/2025")
    ax.legend()
    return fig, ax
```

Sáu giá trị đầu thiếu vì chưa đủ bảy ngày trong phạm vi năm đã chọn. Điền 0 vào lịch chỉ hợp lệ khi khoảng ấy đã được thu thập đầy đủ. Đỉnh trung bình có thể xuất hiện sau một ngày có số đếm cao vì cửa sổ còn giữ ngày đó trong những bước tiếp theo.

Nhãn 30/06 không bảo đảm quý II đã trọn nếu mốc chụp là 29/06. Quý I/2026 có 90 ngày, còn quý II mới quan sát 90 trong 91 ngày tại mốc ấy. Cần tách vấn đề độ dài kỳ khỏi biến động số lượng, thay vì luôn xóa hàng cuối bất kể mốc chụp.
:::

### So cùng quý và chuẩn hóa theo số ngày

::: exercise Chọn đúng kỳ gốc
1. Tính mức thay đổi quý I/2026 so với quý I/2025. Vì sao `shift(12)` sai khi mỗi hàng là một quý? Đếm lại quý I/2025 bằng mask từ 01/01 đến trước 01/04.
2. Trong bốn năm 2022–2025, gộp số đánh giá của cùng tháng. So tháng 2 với tháng 1 theo tổng số và theo số đánh giá mỗi ngày. Tính cả số ngày của năm nhuận.
:::

::: solution
```python
def so_cung_quy(r, quy_day_du):
    q = quy_day_du.reindex(pd.date_range(quy_day_du.index.min(),quy_day_du.index.max(),freq="QE"))
    goc = q.shift(4)
    ty_le = q / goc.where(goc.ne(0)) - 1
    mask = (r.index >= pd.Timestamp("2025-01-01")) & (r.index < pd.Timestamp("2025-04-01"))
    assert mask.sum() == q.loc[pd.Timestamp("2025-03-31")]
    return ty_le

def so_thang_theo_ngay(r):
    lich = pd.date_range("2022-01-31","2025-12-31",freq="ME")
    thang = r.resample("ME").size().reindex(lich,fill_value=0)
    so_ngay = pd.Series(lich.days_in_month,index=lich)
    tong = thang.groupby(thang.index.month).sum()
    ngay = so_ngay.groupby(so_ngay.index.month).sum()
    tb_ngay = tong / ngay
    chenh_tong = tong.loc[2] / tong.loc[1] - 1 if tong.loc[1] else np.nan
    chenh_ngay = tb_ngay.loc[2] / tb_ngay.loc[1] - 1 if tb_ngay.loc[1] else np.nan
    assert ngay.loc[1] == 124 and ngay.loc[2] == 113
    return tong, tb_ngay, chenh_tong, chenh_ngay
```

`shift(4)` lùi bốn quý, còn `shift(12)` lùi ba năm khi lịch quý liên tiếp. Tháng 1 có tổng 124 ngày qua bốn năm, tháng 2 có 113 ngày. Mức thay đổi theo ngày loại ảnh hưởng của số ngày trong phép chia này, nhưng chưa tách xu hướng, mùa vụ hoặc thay đổi phạm vi thu thập.
:::
