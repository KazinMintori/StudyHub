## Thực hành lập hồ sơ một quận

Các bài thực hành dùng bảng chỗ ở Santiago ngày 29/06/2026, với giá theo CLP/đêm. Các cột cần dùng gồm `id`, `name`, `neighbourhood`, `room_type`, `price`. Hãy tính các kết quả từ đúng bản dữ liệu đang sử dụng.

### Chọn dữ liệu và khớp nhãn

::: exercise Kiểm tra các kiểu kết quả và phép khớp nhãn
1. Lấy `price` thành Series và hai cột `name`, `price` thành DataFrame. Tính tỷ lệ phòng riêng, lấy các hàng nguyên căn và lấy riêng giá của các hàng đó bằng `.loc`.
2. Cho `s = pd.Series([100, 200, 300], index=[5, 0, 2])`. Tính `s.loc[2]`, `s.iloc[2]`, `s.loc[0]`, `s.iloc[0]`.
3. Giá cũ có nhãn A, B, C với giá 100, 200, 50. Giá mới có nhãn B, A, D với giá 220, 90, 70. Tính chênh lệch theo nhãn và đếm kết quả thiếu.
:::

::: solution
```python
import pandas as pd
import numpy as np

def chon_bang(df):
    cot_gia = df["price"]
    bang_con = df[["name", "price"]]
    ty_le_private = df["room_type"].eq("Private room").fillna(False).mean()
    mask_nc = df["room_type"].eq("Entire home/apt").fillna(False)
    return cot_gia, bang_con, ty_le_private, df[mask_nc], df.loc[mask_nc, "price"]

s = pd.Series([100, 200, 300], index=[5, 0, 2])
assert (s.loc[2], s.iloc[2], s.loc[0], s.iloc[0]) == (300, 300, 200, 100)
gia_cu = pd.Series({"A":100, "B":200, "C":50})
gia_moi = pd.Series({"B":220, "A":90, "D":70})
thay_doi = gia_moi - gia_cu
assert thay_doi.loc["A"] == -10 and thay_doi.loc["B"] == 20
assert thay_doi.isna().sum() == 2
```

Hai cách lấy phần tử ở chỉ số 2 tình cờ cùng trả 300, nhưng chỉ số 0 cho hai kết quả khác nhau. Vì vậy không nên dùng một trường hợp trùng kết quả để kết luận nhãn và vị trí là một. Phép trừ Series ghép A với A, B với B. C và D thiếu đối tác nên kết quả tại đó bị thiếu.
:::

### Khảo sát, lọc và lập báo giá

::: exercise Hồ sơ Ñuñoa và một quận tự chọn
1. Khảo sát toàn bảng bằng `shape`, `sample`, `info`, `describe`, `value_counts`. Ghi số hàng, số cột, số giá thiếu và số loại phòng.
2. Lọc Ñuñoa, tính tỷ trọng của quận trong toàn bảng. Đếm nguyên căn có giá không quá 60.000 CLP và xem năm chỗ ở giá thấp nhất với hai cột `name`, `price`.
3. Trên bản sao, giảm 10% giá nguyên căn rồi tính lại tiền ba đêm. Giữ nguyên dữ liệu gốc.
4. So sánh tỷ lệ giá thấp hơn trung vị thành phố theo hai mẫu số: Toàn bộ hàng của quận và các hàng có giá. Tính cơ cấu loại phòng cùng tỷ lệ thiếu giá.
5. Xuất hồ sơ CSV, đọc lại và kiểm tra số chỗ ở, trung vị. Lặp lại cho một quận khác bằng cách đổi một tham số, viết ba câu so sánh về quy mô, giá và mức thiếu dữ liệu.
:::

::: solution
Phần khảo sát giúp kiểm tra kiểu cột trước khi tính. Mã dưới giả sử `price` đã là cột số và mỗi hàng là một chỗ ở trong cùng bản chụp.

```python
def khao_sat(df):
    return {
        "shape": df.shape,
        "mau": df.sample(min(3, len(df)), random_state=1),
        "so_thieu_price": int(df["price"].isna().sum()),
        "mo_ta_gia": df["price"].describe(),
        "loai_phong": df["room_type"].value_counts(dropna=False),
    }

def ho_so_quan(df, ten_quan="Ñuñoa"):
    nu = df.loc[df["neighbourhood"].eq(ten_quan).fillna(False)].copy()
    if nu.empty or df.empty:
        raise ValueError("Không có dữ liệu cho quận được chọn")
    med_tp = df["price"].median()
    gia_co = nu["price"].dropna()
    duoi_med = nu["price"].lt(med_tp).fillna(False)
    bao_gia = nu[["id", "room_type", "price"]].copy()
    mask = bao_gia["room_type"].eq("Entire home/apt").fillna(False)
    bao_gia.loc[mask, "price"] = bao_gia.loc[mask, "price"] * 0.9
    bao_gia["tien_3_dem"] = bao_gia["price"] * 3
    re_nhat = nu.loc[nu["price"].notna()].nsmallest(5, "price")[["name", "price"]]
    ho_so = {
        "quan": ten_quan, "so_cho_o": len(nu),
        "ty_trong_thi_truong": len(nu) / len(df),
        "gia_trung_vi": nu["price"].median(),
        "so_nguyen_can_duoi_60000": int((nu["room_type"].eq("Entire home/apt") & nu["price"].le(60000)).fillna(False).sum()),
        "ty_le_duoi_tv_moi_hang": float(duoi_med.sum() / len(nu)) if pd.notna(med_tp) else np.nan,
        "ty_le_duoi_tv_thanh_pho": float(gia_co.lt(med_tp).mean()) if len(gia_co) and pd.notna(med_tp) else np.nan,
        "ty_le_thieu_gia_pct": float(nu["price"].isna().mean() * 100),
        "co_cau": nu["room_type"].value_counts(normalize=True, dropna=False).to_dict(),
    }
    return nu, ho_so, bao_gia, re_nhat

def luu_ho_so_quan(ho_so, path):
    bang = pd.DataFrame([{k:v for k,v in ho_so.items() if k != "co_cau"}])
    bang.to_csv(path, index=False)
    doc_lai = pd.read_csv(path)
    assert doc_lai.shape == bang.shape
    assert doc_lai.loc[0, "so_cho_o"] == ho_so["so_cho_o"]
    np.testing.assert_allclose(doc_lai["gia_trung_vi"], bang["gia_trung_vi"], equal_nan=True)
    return doc_lai
```

Có thể gọi `df.info()` bên cạnh kết quả `khao_sat(df)` để xem kiểu và số giá trị không thiếu. Hai tỷ lệ dưới trung vị chỉ khác mẫu số khi thành phố có trung vị xác định. Tỷ lệ dùng mọi hàng xem giá chưa biết là chưa xác nhận được điều kiện. Tỷ lệ dùng giá đã biết chỉ mô tả nhóm đã có giá. Cần ghi rõ lựa chọn này trong nhận xét.

Để so quận khác, gọi cùng hàm với tên quận mới. Nhận xét cần dẫn số tính được từ hai hồ sơ, không đoán trước quận nào đắt hơn.
:::

### Sửa phép gán qua hai lần chọn

::: exercise Vì sao bảng không đổi trong pandas 3?
Xét `bao_gia["price"][bao_gia["room_type"] == "Entire home/apt"] *= 0.9`. Giải thích đối tượng nào được lấy ra ở mỗi bước, rồi sửa bằng `.loc`. Cột tiền ba đêm đã tính trước phép giảm giá có tự đổi không?
:::

::: solution
Lần ngoặc đầu lấy một Series. Phép gán tiếp theo tác động lên đối tượng trung gian, không phải một phép cập nhật DataFrame đích theo cơ chế Copy-on-Write của pandas 3. Cần gán rõ cả hàng và cột trên bảng:

```python
def bao_gia_dung(nu):
    result = nu[["id", "room_type", "price"]].copy()
    mask = result["room_type"].eq("Entire home/apt").fillna(False)
    result.loc[mask, "price"] = result.loc[mask, "price"] * 0.9
    result["tien_3_dem"] = result["price"] * 3
    return result
```

Cột tính sẵn chứa giá trị, không giữ một công thức phụ thuộc như ô bảng tính. Vì vậy phải tính lại sau khi cập nhật giá.
:::
