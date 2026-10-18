## Thực hành quy tắc xử lý chuỗi và chất lượng dữ liệu

### Chuẩn hóa trong đúng phạm vi

::: exercise Kiểm tra cả chuỗi giá
1. Với `["  Wifi ", "wifi", "WIFI!", "wi-fi"]`, chỉ bỏ khoảng trắng hai đầu và đổi chữ thường. Có được tự gộp cả bốn thành `wifi` không?
2. Với `["a.b", "axb", None]`, tìm đúng dấu chấm và không chọn hàng thiếu.
3. Đọc giá USD có dấu `$`, dấu phẩy hàng nghìn và dấu chấm thập phân. Phần thập phân nếu có phải có đúng hai chữ số. Kiểm tra toàn chuỗi trước khi chuyển, giữ cột gốc và phân biệt nguồn thiếu với dữ liệu có nhưng sai định dạng. Thử `$1,200.00`, ` $850.00 `, `None`, `liên hệ`, `từ $500`, `$24,50.00`, `$95.5`.
:::

::: solution
```python
import re
import json
import numpy as np
import pandas as pd
s = pd.Series(["  Wifi ", "wifi", "WIFI!", "wi-fi"])
assert s.str.strip().str.lower().tolist() == ["wifi", "wifi", "wifi!", "wi-fi"]
assert pd.Series(["a.b", "axb", None]).str.contains(".", regex=False, na=False).tolist() == [True,False,False]
PAT_GIA = r"\$(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]{2})?"

def doc_gia_chuoi(gia):
    chuan = gia.astype("string").str.strip()
    hop_le = chuan.str.fullmatch(PAT_GIA, na=False)
    chu_so = chuan.where(hop_le).str.removeprefix("$").str.replace(",", "", regex=False)
    gia_so = pd.to_numeric(chu_so, errors="coerce")
    loi_doc = gia.notna() & ~hop_le
    return gia_so, loi_doc, hop_le
```

`strip` và `lower` không xóa dấu câu hay dấu nối. Muốn gộp các cách viết ấy phải bổ sung một quy tắc riêng. Với giá, `fullmatch` xác nhận toàn bộ chuỗi theo quy ước đã biết. Trích được một số từ `từ $500` chưa làm cả chuỗi trở thành giá hợp lệ.
:::

### Làm sạch đúng một đoạn HTML và đọc kết quả trích xuất

::: exercise Khảo sát cột đánh giá trước khi suy luận
Với `comments` trong bảng đánh giá Santiago ngày 29/06/2026, đếm giá trị thiếu, lấy các đoạn có nội dung và độ dài của chúng. Đếm đoạn ngắn hơn 20 ký tự. Chỉ thay đúng `<br/>` bằng một dấu cách, giữ chỉ mục và bản gốc.

Trích từ đầu tiên sau `cerca de`, `cerca de la`, `cerca del`, `near`, `near the`, không phân biệt hoa thường. Xem các từ hay xuất hiện và chọn ít nhất hai từ không phải tên địa điểm để đọc lại nguyên văn. Sau đó kiểm tra phát biểu “Đếm đoạn có wifi hoặc internet là đếm khách hài lòng về mạng” bằng một mẫu tối đa 20 đoạn khớp.
:::

::: solution
```python
PAT_GAN = r"\b(?:cerca de(?: la|l)?|near(?: the)?)\s+(\w+)"
def khao_sat_comments(rv):
    goc = rv["comments"]
    c = goc.dropna().astype("string")
    sach = c.str.replace("<br/>", " ", regex=False)
    tu_sau_gan = sach.str.extract(PAT_GAN, flags=re.I, expand=False)
    mask_mang = sach.str.contains(r"wifi|internet", case=False, regex=True, na=False)
    khop = sach.loc[mask_mang]
    return {
        "so_thieu":int(goc.isna().sum()), "do_dai":c.str.len(),
        "so_ngan":int(c.str.len().lt(20).sum()),
        "so_br":int(c.str.contains("<br/>", regex=False).sum()),
        "sach":sach, "tu_sau_gan":tu_sau_gan,
        "dem_tu":tu_sau_gan.str.lower().value_counts(),
        "mau_tu_khoa":khop.sample(min(20, len(khop)), random_state=7),
    }

def xem_tu_nghi_van(result, danh_sach_tu):
    tu = result["tu_sau_gan"].str.lower()
    return {name:result["sach"].loc[tu.eq(name).fillna(False)].head(3)
            for name in danh_sach_tu}
```

`todo` trong `cerca de todo` là “mọi thứ”, không phải tên địa điểm. Cụm `cerca del Movistar Arena` cũng chỉ cho từ `Movistar`, chưa trả được toàn bộ tên. Vì vậy đầu ra được gọi là `tu_sau_gan`.

Một đoạn chứa từ `wifi` có thể khen, chê, phủ định hoặc chỉ liệt kê tiện nghi. Kết luận đúng phạm vi là số đoạn có nhắc từ khóa theo mẫu đang dùng. Muốn đếm mức hài lòng phải có quy tắc hiểu nội dung và bộ dữ liệu kiểm tra phù hợp.
:::

### Danh sách JSON, mục lặp và mẫu số

::: exercise Tỷ lệ chỗ ở liệt kê Wifi
Đọc `amenities` bằng `json.loads`, rồi tách từng mục bằng `explode` nhưng giữ mã chỗ ở. Không chia chuỗi bằng dấu phẩy vì tên một mục có thể chứa dấu phẩy.

Tính tỷ lệ chỗ ở liệt kê đúng mục `Wifi`. Kiểm riêng bảng có các danh sách `["Wifi", "Wifi", "Kitchen"]`, `["Kitchen"]`, `[]`, `None`, `["Wifi"]`. Khi tính trên các chỗ ở đã có thông tin, mẫu số là bao nhiêu? Vì sao danh sách rỗng khác dữ liệu thiếu?
:::

::: solution
```python
def doc_danh_sach(value):
    if pd.isna(value):
        return None
    result = json.loads(value)
    if not isinstance(result, list) or not all(isinstance(x, str) for x in result):
        raise ValueError("Tiện nghi phải là danh sách các chuỗi")
    return result

def thong_ke_wifi(ds):
    da_biet = ds.map(lambda x:isinstance(x, list))
    co_wifi = ds.map(lambda x:"Wifi" in x if isinstance(x, list) else pd.NA).astype("boolean")
    muc = ds.loc[da_biet].explode().dropna()
    ty_le = co_wifi.loc[da_biet].mean() if da_biet.any() else pd.NA
    return co_wifi, muc, int(da_biet.sum()), ty_le

ds_nho = pd.Series([["Wifi","Wifi","Kitchen"], ["Kitchen"], [], None, ["Wifi"]],
                   index=["P1","P2","P3","P4","P5"])
co_wifi, muc, so_da_biet, ty_le_nho = thong_ke_wifi(ds_nho)
assert so_da_biet == 4 and ty_le_nho == 0.5
```

Mỗi chỗ ở chỉ đóng góp một giá trị True hoặc False. Lặp `Wifi` hai lần trong một ô không làm chỗ ở đó được đếm hai lần. Danh sách rỗng xác nhận không có mục được liệt kê, còn `None` để ngỏ thông tin. Tỷ lệ trên không chứng minh mạng hoạt động tốt.
:::

### Diện tích với dấu phẩy thập phân

::: exercise Mở rộng quy tắc trích diện tích
Nhận `45 m2`, `30m²`, `45.5 m2`, `45,5 m²`, nhưng không nhận `30m2x`. Trả diện tích dạng số và giữ cột tên gốc. Bổ sung trường hợp mã có chữ dính trước số và số âm viết liền để kiểm tra ranh giới.
:::

::: solution
```python
PAT_DT = r"(?:^|[^\w.,-])([0-9]+(?:[.,][0-9]+)?)\s*m(?:2|²)\b"
def trich_dien_tich(ten):
    chuoi = ten.astype("string").str.extract(PAT_DT, flags=re.I, expand=False)
    return pd.to_numeric(chuoi.str.replace(",", ".", regex=False), errors="coerce")
```

Nhóm bắt giữ phần số. Phần trước nhóm số yêu cầu đầu chuỗi hoặc một ký tự phân cách phù hợp, còn ranh giới sau đơn vị loại hậu tố `x`. Mẫu này dùng miền cách viết đã nêu, chưa xử lý mọi cách ghi diện tích hoặc mọi dạng số âm có khoảng trắng.
:::

### Điền giá trị có lý do và giữ cờ ước lượng

::: exercise Tách giá quan sát khỏi giá được điền
Theo quy ước của bài, `reviews_per_month` được điền 0 ở chỗ ở có `number_of_reviews == 0`. Giữ các giá trị khác. Không áp dụng suy luận đó cho điểm đánh giá.

Với giá thiếu, tạo một Series điền bằng trung vị của cùng `room_type` và một Series boolean đánh dấu giá đã điền. Không sửa bảng gốc. So sánh trung bình trước và sau, ghi rõ thống kê nào dùng cả giá ước lượng.
:::

::: solution
```python
def dien_theo_y_nghia(ds):
    rpm = ds["reviews_per_month"].copy()
    rpm.loc[ds["number_of_reviews"].eq(0)] = 0
    trung_vi_nhom = ds.groupby("room_type", dropna=False)["price"].transform("median")
    gia_uoc_luong = ds["price"].fillna(trung_vi_nhom)
    gia_da_dien = ds["price"].isna() & gia_uoc_luong.notna()
    return rpm, gia_uoc_luong, gia_da_dien
```

Nếu một nhóm không có giá nào đã biết thì trung vị nhóm vẫn thiếu, nên hàm không tự tạo giá để điền. Điền trung vị có thể làm thay đổi trung bình và độ phân tán. Cần giữ cờ để phân biệt kết quả ước lượng với quan sát ban đầu.
:::

### Cờ giá và tác động của các cách xử lý

::: exercise Thử cả float64 và Float64
Viết hàm trả ba cờ `thieu`, `khong_duong`, `cao` cho cột số `price`. Cờ cuối dùng điều kiện giá lớn hơn ngưỡng, không lấy bằng ngưỡng. Các cờ phải có kiểu boolean, không chứa NA và giữ chỉ mục.

Trên các giá dương đã biết, tính ngưỡng IQR và P99. So số lượng, trung bình, trung vị của ba cách: Giữ nguyên giá, bỏ giá trên P99, chặn giá tại P99. Không sửa dữ liệu nguồn hay tự kết luận giá bị cờ là sai.
:::

::: solution
```python
def kiem_gia(d, nguong):
    p = d["price"]
    return pd.DataFrame({"thieu":p.isna(),
        "khong_duong":p.le(0).fillna(False),
        "cao":p.gt(nguong).fillna(False)}, index=d.index).astype(bool)

def so_sanh_cach_xu_ly(ds):
    gia = ds.loc[ds["price"].gt(0).fillna(False), "price"].dropna()
    if gia.empty:
        raise ValueError("Không có giá dương để tính ngưỡng")
    q1, q3 = gia.quantile([.25, .75])
    nguong_iqr, p99 = q3 + 1.5 * (q3 - q1), gia.quantile(.99)
    cac_cach = {"co_gia_duong":gia, "bo_tren_p99":gia.loc[gia.le(p99)],
                "chan_p99":gia.clip(upper=p99)}
    bang = pd.DataFrame({name:{"so_cho_o":len(s), "trung_binh":s.mean(),
                               "trung_vi":s.median()} for name,s in cac_cach.items()}).T
    return nguong_iqr, int(gia.gt(nguong_iqr).sum()), p99, kiem_gia(ds,p99), bang
```

Bỏ hàng làm đổi tập quan sát, còn chặn giá thay đổi giá trị của các hàng vẫn được giữ. Không thể dùng hai kết quả như thể chúng cùng mô tả nguyên vẹn dữ liệu nguồn. IQR và P99 là hai quy tắc sàng lọc khác nhau, cần lựa chọn theo mục tiêu kiểm tra.
:::

### Trùng cặp thuộc tính chưa chắc trùng sự kiện

::: exercise Giữ hai đánh giá khác nhau trong cùng ngày
Bảng có `review_id = ["R1", "R2", "R1", "R3"]`. Hai hàng R1 giống hệt là một bản nhập lặp. R1 và R2 cùng `listing_id`, cùng ngày nhưng khác nội dung. Loại bản nhập lặp và giải thích vì sao không được làm tương tự trên bản rút gọn chỉ có `listing_id`, `date`.
:::

::: solution
```python
def bo_ban_nhap_lap(mau_rv):
    thuoc_tinh = [cot for cot in mau_rv.columns if cot != "review_id"]
    mau_thuan = mau_rv.groupby("review_id", dropna=False)[thuoc_tinh].nunique(dropna=False).gt(1).any(axis=1)
    if mau_thuan.any():
        raise ValueError("Cùng review_id nhưng thuộc tính mâu thuẫn, cần kiểm tra")
    return mau_rv.drop_duplicates().copy()
```

Trong miền của đề, R1 có đủ mã sự kiện và thông tin trùng nhau, nên chỉ giữ một bản. Hai hàng R1 và R2 là hai sự kiện riêng dù trùng chỗ ở và ngày. Bản rút gọn mất `review_id` nên việc đếm cặp trùng chỉ phát hiện các cặp thuộc tính giống nhau, chưa xác nhận bản nhập lặp.
:::

### Bộ cờ ngày, khóa và báo cáo kiểm tra

::: exercise Giữ cả hàng bị cờ và mẫu số của từng bảng
Viết `kiem_reviews(r, ids, moc)` trả ba cờ `ngay_thieu`, `sau_moc`, `id_khong_khop`. Ngày bằng mốc vẫn hợp lệ. Ngày thiếu không bật cờ sau mốc. Mã thiếu hoặc không có trong bảng chỗ ở phải bị cờ.

Thử mốc 29/06/2026 và 30/06/2026, thay danh sách mã và đảo thứ tự hàng. Xuất báo cáo có tên bảng, quy tắc, số hàng và tỷ lệ. Giữ riêng những hàng có ít nhất một cờ cùng chỉ mục gốc.
:::

::: solution
```python
def kiem_reviews(r, ids, moc):
    return pd.DataFrame({"ngay_thieu":r["date"].isna(),
        "sau_moc":r["date"].gt(moc).fillna(False),
        "id_khong_khop":r["listing_id"].isna() | ~r["listing_id"].isin(ids)},
        index=r.index).astype(bool)

def tom_tat_co(co, ten_bang):
    return pd.DataFrame({"bang":ten_bang, "so_hang":co.sum(),
        "tong_hang":len(co), "ty_le_pct":co.mean() * 100}).rename_axis("quy_tac").reset_index()

def luu_kiem_tra(ds, rv, nguong, moc, path):
    co_gia = kiem_gia(ds, nguong)
    co_rv = kiem_reviews(rv, ds["id"], moc)
    report = pd.concat([tom_tat_co(co_gia,"listings"), tom_tat_co(co_rv,"reviews")], ignore_index=True)
    report.to_csv(path, index=False)
    can_xem = co_rv.any(axis=1)
    chi_tiet = rv.loc[can_xem, ["listing_id","date"]].join(co_rv.add_prefix("co_"))
    return report, chi_tiet
```

Một hàng có thể bật nhiều cờ, nên tổng lượt gắn cờ có thể lớn hơn số hàng cần kiểm tra. Hai bảng cũng có đơn vị quan sát khác nhau. Không cộng số hàng bị cờ của bảng listing và bảng review thành một tỷ lệ chung.
:::

### Tách giá mâu thuẫn trước khi gộp

::: exercise Một giá cho mỗi cặp mã và kỳ
Với mã và kỳ đã chuẩn hóa, tách mọi hàng của khóa có nhiều giá đã biết khác nhau vào `gia_can_xem`. Gộp các khóa còn lại thành một hàng, ưu tiên giá đã biết nếu có. Nhóm toàn NA vẫn giữ NA. Thử bảng:

```python
gia_nhap = pd.DataFrame({"id":["P1","P2","P3","P4","P1","P2","P3","P4","P1"],
    "ky":["T6","T6","T6","T6","T6","T6","T6","T6","T5"],
    "gia":[120,90,np.nan,np.nan,120,95,110,np.nan,100]})
```
:::

::: solution
```python
def gop_gia_khong_mau_thuan(df):
    khoa = ["id","ky"]
    if df[khoa].isna().any().any():
        raise ValueError("Khóa của bài không được thiếu")
    so_gia = df.groupby(khoa)["gia"].transform("nunique")
    can_xem = df.loc[so_gia.gt(1), khoa+["gia"]].copy()
    gop = df.loc[so_gia.le(1)].groupby(khoa, as_index=False)["gia"].first()
    return gop, can_xem
```

P2/T6 có hai giá 90 và 95 nên cần thông tin về thời điểm cập nhật hoặc nguồn đo trước khi chọn. P3/T6 có một giá 110 và một ô thiếu nên chưa mâu thuẫn. P4/T6 không có giá đã biết, vì vậy kết quả vẫn thiếu.
:::

### Đối chiếu tổng và khoảng 12 tháng

::: exercise Giữ các mã có số đếm bằng 0
Đọc `id`, `listing_id` cùng kiểu chuỗi. Theo từng chỗ ở, đối chiếu số nguồn `number_of_reviews` với số đếm toàn tệp và số đếm đến hết 29/06/2026. Giữ các chỗ ở chưa có đánh giá với số đếm 0.

Đếm riêng khoảng 30/06/2025 đến hết 29/06/2026, rồi lấy số tự đếm trừ `number_of_reviews_ltm`. Không bỏ hàng chỉ vì cùng mã và ngày.
:::

::: solution
```python
def doi_chieu_review(ds, rv, moc=pd.Timestamp("2026-06-29")):
    listing = ds.set_index("id", verify_integrity=True)
    ca_file = rv.groupby("listing_id").size()
    den_moc = rv.loc[rv["date"].le(moc)].groupby("listing_id").size()
    dau = pd.Timestamp("2025-06-30")
    trong_12 = rv.loc[rv["date"].between(dau, moc)].groupby("listing_id").size()
    result = listing[["number_of_reviews","number_of_reviews_ltm"]].rename(
        columns={"number_of_reviews":"nguon", "number_of_reviews_ltm":"nguon_12_thang"})
    result["dem_ca_file"] = ca_file.reindex(listing.index, fill_value=0)
    result["den_moc"] = den_moc.reindex(listing.index, fill_value=0)
    result["dem_12_thang"] = trong_12.reindex(listing.index, fill_value=0)
    result["lech_12_thang"] = result["dem_12_thang"] - result["nguon_12_thang"]
    return result
```

Nếu tổng nguồn khớp toàn tệp nhưng số đến mốc thấp hơn, cần xem những ngày sau mốc, không tự cho rằng phép đếm sai. Bước đối chiếu này phải đi cùng các cờ khóa không khớp, vì việc reindex về bảng chỗ ở không giữ riêng các review có mã ngoài bảng cha.
:::

### Mốt, điền tiến theo nhóm và nội suy theo thời gian

::: exercise Ba quy tắc điền khác nhau
1. Điền loại chỗ ở thiếu bằng mốt của các giá trị đã biết.
2. Sắp lịch giá theo `id`, `ky`, lấy giá phía trước của cùng id và chỉ điền tối đa một ô trong mỗi đoạn thiếu.
3. Nội suy nhiệt độ theo khoảng cách thời gian, chỉ điền giữa hai quan sát đã biết. Thử `[18, NA, NA, 24, NA]` tại các ngày 01, 02, 05, 07, 08/06/2026. Vì sao nội suy theo vị trí hàng cho kết quả khác?
:::

::: solution
```python
def ba_cach_dien(loai, lich_gia, nhiet_do):
    mot = loai.mode()
    loai_dien = loai.fillna(mot.iloc[0]) if not mot.empty else loai.copy()
    lich_dien = lich_gia.sort_values(["id","ky"]).copy()
    lich_dien["dien"] = lich_dien.groupby("id")["gia"].ffill(limit=1)
    noi_suy = nhiet_do.sort_index().interpolate(method="time", limit_area="inside")
    return loai_dien, lich_dien, noi_suy
```

Nếu có nhiều mốt, chương trình đang chọn giá trị đầu trong thứ tự pandas trả về. Báo cáo cần nêu quy tắc này hoặc giữ riêng trường hợp hòa. Điền tiến không được chạy xuyên qua các id. Với chuỗi nhiệt độ, khoảng từ ngày 01 đến ngày 07 dài sáu ngày nên ngày 02 nhận 19 và ngày 05 nhận 22. Ngày 08 vẫn thiếu vì không có quan sát phía sau.
:::
