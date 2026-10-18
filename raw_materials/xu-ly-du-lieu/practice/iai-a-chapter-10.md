## Thực hành tổng hợp thị trường theo nhiều tiêu chí

### Phân khúc giá và quy mô quản lý

::: exercise Từ từng hàng đến bảng so sánh nhóm
Dùng bảng Santiago ngày 29/06/2026. Giá theo CLP/đêm. Cần các cột `id`, `name`, `price`, `neighbourhood`, `number_of_reviews_ltm`, `calculated_host_listings_count`.

1. Dùng hàm và `map` để phân giá thành `re` khi dưới 30.000, `trung` khi từ 30.000 đến dưới 100.000, `cao` khi từ 100.000 trở lên. Giữ giá thiếu ngoài ba nhóm.
2. Theo phân khúc, tính số chỗ ở, trung vị giá và trung bình số đánh giá trong 12 tháng.
3. Theo quy ước của bài, đặt `chuyen=True` khi chủ nhà quản lý ít nhất năm listing. Tính tỷ trọng listing của nhóm này và bảng so sánh giá, số đánh giá giữa hai nhóm.
4. Dùng `transform("size")` gắn quy mô quận vào từng hàng, giữ các quận có ít nhất 300 chỗ ở.
5. Lập bảng hai chiều phân khúc × kiểu chủ nhà với giá trị là số đánh giá trung bình. So sánh kết quả tổng thể với kết quả trong từng phân khúc.
6. Tìm mọi chỗ ở đồng hạng giá cao nhất của mỗi quận đủ quy mô. Tính cơ cấu ba phân khúc trong từng quận đó và tìm quận có tỷ trọng phân khúc cao lớn nhất.
:::

::: solution
```python
import pandas as pd
def phan_khuc(gia):
    if pd.isna(gia):
        return None
    if gia < 30000:
        return "re"
    if gia < 100000:
        return "trung"
    return "cao"

def phan_tich_nhom(df, toi_thieu=300):
    data = df.copy()
    data["phan_khuc"] = data["price"].map(phan_khuc)
    if data["calculated_host_listings_count"].isna().any():
        raise ValueError("Cần xác định cách xử lý quy mô chủ nhà bị thiếu")
    data["chuyen"] = data["calculated_host_listings_count"].ge(5)
    tong_hop = data.groupby("phan_khuc", dropna=False).agg(
        so_phong=("id", "size"), gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"))
    so_sanh = data.groupby("chuyen").agg(
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"))
    data["n_quan"] = data.groupby("neighbourhood", dropna=False)["id"].transform("size")
    dong = data.loc[data["n_quan"].ge(toi_thieu)].copy()
    pv = data.pivot_table(index="phan_khuc", columns="chuyen",
                          values="number_of_reviews_ltm", aggfunc="mean")
    dem = pd.crosstab(dong["neighbourhood"], dong["phan_khuc"])
    ty_trong = dem.div(dem.sum(axis=1), axis=0)
    return {"du_lieu":data, "tong_hop":tong_hop, "so_sanh":so_sanh,
            "ty_le_listing_chuyen":data["chuyen"].mean(), "du_quy_mo":dong,
            "pivot_review":pv, "ty_trong_phan_khuc":ty_trong,
            "ty_le_thieu_gia_theo_quan":dong.groupby("neighbourhood")["price"].apply(lambda s:s.isna().mean())}

def dat_nhat_tung_quan(df):
    lon_nhat = df.groupby("neighbourhood")["price"].transform("max")
    return df.loc[df["price"].eq(lon_nhat).fillna(False),
                  ["id", "name", "neighbourhood", "price"]]
```

`transform` giữ một giá trị quy mô nhóm cho mỗi hàng. So sánh với cực đại nhóm giữ cả các hàng đồng hạng, trong khi chỉ lấy một `idxmax` có thể bỏ hàng đồng hạng. Bảng tỷ trọng phân khúc ở đây dùng các listing có phân khúc xác định làm mẫu số. Tỷ lệ giá thiếu được trả riêng để người đọc thấy phần dữ liệu chưa được phân loại.

Tên `chuyen` chỉ là một phân nhóm theo ngưỡng năm listing. Nó không xác minh nghề nghiệp của chủ nhà. Số đánh giá trong 12 tháng cũng không đồng nhất với số lượt đặt hay doanh thu. Nếu một nhóm có trung bình cao hơn trong mọi phân khúc, ta vẫn chưa loại được ảnh hưởng của vị trí, chất lượng và thời điểm hoạt động.
:::

### Chọn quận nhiều lựa chọn và trung vị thấp

::: exercise Kiểm tra lại một kết quả từ groupby
Trong các quận có ít nhất 300 chỗ ở, tìm quận có trung vị giá thấp nhất. Ngưỡng quy mô tính trên toàn bộ listing của quận. Đối chiếu kết quả bằng cách lọc riêng quận được chọn và tính lại trung vị.
:::

::: solution
```python
def quan_gia_thap(df, toi_thieu=300):
    tk = df.groupby("neighbourhood", as_index=False).agg(
        so_cho_o=("id", "size"), gia_trung_vi=("price", "median"))
    tk = tk.loc[tk["so_cho_o"].ge(toi_thieu) & tk["gia_trung_vi"].notna()]
    result = tk.sort_values(["gia_trung_vi", "neighbourhood"]).head(1)
    if not result.empty:
        ten = result["neighbourhood"].iloc[0]
        doc_lap = df.loc[df["neighbourhood"].eq(ten), "price"].median()
        assert doc_lap == result["gia_trung_vi"].iloc[0]
    return result
```

Điều kiện số lượng và phép tính trung vị có mẫu số khác nhau. `size` đếm hàng để kiểm tra quy mô, còn `median` bỏ các giá thiếu. Một bảng báo cáo đầy đủ nên nêu thêm số giá quan sát được của quận được chọn.
:::
