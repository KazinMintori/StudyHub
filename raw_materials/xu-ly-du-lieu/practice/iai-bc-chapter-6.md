## Thực hành phối hợp tệp, API và SQL

### Chọn cột, giữ kiểu và đọc lại Parquet

::: exercise So sánh hai cách lưu bảng
Đọc bản `data/listings.csv.gz` của Santiago ngày 29/06/2026 theo hai cách: Toàn bộ cột và chỉ năm cột `id`, `room_type`, `number_of_reviews`, `first_review`, `last_review`. Giữ mã dạng chuỗi và hai cột ngày dạng datetime. Lưu bảng nhỏ thành CSV và Parquet, đọc lại rồi so sánh kiểu và giá trị. Không kết luận loại tệp nào luôn nhỏ hay nhanh hơn nếu chưa đo cùng dữ liệu.
:::

::: solution
```python
from pathlib import Path
import pandas as pd
import json
import requests
import duckdb

COT_5 = ["id","room_type","number_of_reviews","first_review","last_review"]
def doc_nam_cot(path):
    return pd.read_csv(path, usecols=COT_5, dtype={"id":"string"},
                       parse_dates=["first_review","last_review"])

def luu_hai_dang(bang, folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    csv_path, parquet_path = folder / "listings_5cot.csv", folder / "listings_5cot.parquet"
    bang.to_csv(csv_path, index=False)
    bang.to_parquet(parquet_path, index=False)
    csv_doc = doc_nam_cot(csv_path)
    parquet_doc = pd.read_parquet(parquet_path)
    pd.testing.assert_frame_equal(parquet_doc, bang, check_dtype=True)
    return csv_doc, parquet_doc, {"csv_bytes":csv_path.stat().st_size,
                                 "parquet_bytes":parquet_path.stat().st_size}
```

CSV không mang đầy đủ schema của DataFrame, nên khi đọc lại cần nêu cách diễn giải mã và ngày. Parquet giữ thông tin kiểu cho những cột được hỗ trợ. Kích thước tệp trong lần chạy này là một phép đo cụ thể, không phải tỷ lệ tiết kiệm áp dụng cho mọi bảng.
:::

### Ghép thời tiết theo ngày với số đánh giá

::: exercise Giữ phản hồi API và kiểm tra đơn vị
Lấy nhiệt độ tối đa theo ngày của Santiago trong tháng 01/2025 từ API lịch sử Open-Meteo, múi giờ `America/Santiago`, đơn vị °C. Lưu nguyên phản hồi và thông tin thời điểm tải. Tạo bảng ngày, đếm đánh giá cùng tháng, ghép hai nguồn và tính tương quan. Lặp lại cho tháng 07/2025 rồi so sánh hai kết quả trong phạm vi dữ liệu đã lấy.
:::

::: solution
```python
def lay_thoi_tiet(start, end, folder, session=requests):
    params = {"latitude":-33.4489, "longitude":-70.6693,
              "start_date":start, "end_date":end,
              "daily":"temperature_2m_max", "timezone":"America/Santiago"}
    response = session.get("https://archive-api.open-meteo.com/v1/archive",
                           params=params, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if payload["daily_units"]["temperature_2m_max"] != "°C":
        raise ValueError("Đơn vị nhiệt độ không đúng yêu cầu")
    if payload["timezone"] != "America/Santiago":
        raise ValueError("Múi giờ không đúng yêu cầu")
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"weather-{start}-{end}.json"
    path.write_bytes(response.content)
    path.with_suffix(".meta.json").write_text(json.dumps({
        "url":response.url, "tai_luc_utc":pd.Timestamp.now(tz="UTC").isoformat()},
        ensure_ascii=False, indent=2), encoding="utf-8")
    bang = pd.DataFrame(payload["daily"])
    bang["time"] = pd.to_datetime(bang["time"], format="%Y-%m-%d")
    return bang

def ghep_theo_ngay(thoi_tiet, rv, start, end):
    start, end = pd.Timestamp(start), pd.Timestamp(end)
    ngay = pd.to_datetime(rv["date"], format="%Y-%m-%d")
    chon = ngay.between(start, end)
    dem = ngay.loc[chon].value_counts().sort_index()
    lich = pd.date_range(start, end, freq="D")
    theo_ngay = dem.reindex(lich, fill_value=0).rename_axis("time").reset_index(name="so_review")
    gop = thoi_tiet.merge(theo_ngay, on="time", how="left", validate="1:1")
    assert gop["time"].is_unique
    assert gop["so_review"].notna().all() and len(gop) == len(lich)
    return gop, gop["temperature_2m_max"].corr(gop["so_review"])
```

Việc điền 0 cho ngày không có đánh giá đòi hỏi tệp review đã thu đủ khoảng ngày đang xét. `response.content` giữ byte gốc, khác với việc tự viết lại một dict thành JSON. Hệ số tương quan chỉ mô tả liên hệ tuyến tính của hai chuỗi trong khoảng chọn. Nó chưa chứng minh nhiệt độ gây ra thay đổi lượng đánh giá.
:::

### COUNT, JOIN và HAVING trên cùng dữ liệu

::: exercise Kiểm chứng SQL bằng pandas
1. Đếm đánh giá theo năm bằng DuckDB và đối chiếu với Python hoặc pandas.
2. Theo loại chỗ ở, tính số listing bằng `COUNT(*)` và số có `first_review` bằng `COUNT(first_review)`.
3. Ghép trái các đánh giá năm 2025 với loại chỗ ở, giữ cả đánh giá chưa tìm được mã và giải thích giá trị thiếu sau ghép.
4. Tìm những chỗ ở có ít nhất 100 đánh giá năm 2025 bằng `HAVING`.
5. Tìm năm chỗ ở có nhiều đánh giá nhất năm 2025, kèm tên, rồi kiểm lại bằng `value_counts`.
:::

::: solution
```python
def truy_van_review(listings, reviews):
    l = listings.copy()
    r = reviews.copy()
    l["id"] = l["id"].astype("string")
    r["listing_id"] = r["listing_id"].astype("string")
    r["date"] = pd.to_datetime(r["date"], format="%Y-%m-%d")
    if l["id"].isna().any() or l["id"].duplicated().any():
        raise ValueError("Bảng listing cần mã đầy đủ và duy nhất")
    con = duckdb.connect()
    try:
        con.register("listings", l)
        con.register("reviews", r)
        nam = con.sql("SELECT year(date) AS nam, COUNT(*) AS n FROM reviews GROUP BY nam ORDER BY nam").df()
        loai = con.sql("SELECT room_type, COUNT(*) AS so_cho_o, COUNT(first_review) AS so_co_danh_gia FROM listings GROUP BY room_type").df()
        dem = con.sql("SELECT listing_id, COUNT(*) AS n FROM reviews WHERE year(date)=2025 GROUP BY listing_id").df()
        nhieu = con.sql("SELECT listing_id, COUNT(*) AS n FROM reviews WHERE year(date)=2025 GROUP BY listing_id HAVING COUNT(*)>=100").df()
        theo_loai = con.sql("SELECT l.room_type, COUNT(*) AS n FROM reviews r LEFT JOIN listings l ON r.listing_id=l.id WHERE year(r.date)=2025 GROUP BY l.room_type").df()
        top5 = con.sql("SELECT d.listing_id, l.name, d.n FROM (SELECT listing_id, COUNT(*) AS n FROM reviews WHERE year(date)=2025 GROUP BY listing_id) d LEFT JOIN listings l ON d.listing_id=l.id ORDER BY d.n DESC,d.listing_id LIMIT 5").df()
    finally:
        con.close()
    dem_pd = r.loc[r["date"].dt.year.eq(2025), "listing_id"].value_counts()
    dem_sql = dem.set_index("listing_id")["n"].sort_index()
    pd.testing.assert_series_equal(dem_sql, dem_pd.sort_index(), check_names=False, check_dtype=False, check_index_type=False)
    assert theo_loai["n"].sum() == dem_pd.sum()
    assert len(nhieu) == dem_pd.ge(100).sum()
    return {"theo_nam":nam, "listing_theo_loai":loai,
            "review_theo_loai":theo_loai, "tu_100":nhieu, "top5":top5}
```

`COUNT(*)` đếm hàng, còn `COUNT(first_review)` không đếm ô NULL. Bộ lọc năm thuộc `WHERE`, điều kiện về số lượng đã tổng hợp thuộc `HAVING`. Hàm kiểm mã listing duy nhất để phép ghép không nhân dòng review. Khi đọc trực tiếp Parquet bằng DuckDB, có thể dùng `read_parquet(?)` với đường dẫn là tham số, thay cho bảng đã đăng ký.
:::
