## Thực hành đọc và tổng hợp dữ liệu bằng Python

### Định dạng số, lọc giá thiếu và so sánh hai tập mã

::: exercise Ba phép kiểm tra trước khi đọc tệp
1. Định dạng `118199.6` thành `Giá TB: 118,200 CLP` và `0.178` thành `17.8%`.
2. Tính trung bình các giá đã biết trong `[52000, None, 78000, None, 61000]`. Giải thích vì sao phải kiểm tra `is not None`.
3. Với hai tập `{101, 102, 103, 104}` và `{102, 104, 105}`, tìm mã chỉ có ở lần trước và mã mới ở lần sau.
:::

::: solution
```python
gia_tb, ty_le = 118199.6, 0.178
ket_qua = f"Giá TB: {gia_tb:,.0f} CLP"
ty_le_chu = f"{ty_le:.1%}"
gia = [52000, None, 78000, None, 61000]
gia_co = [x for x in gia if x is not None]
tb = sum(gia_co) / len(gia_co)
thang_3, thang_6 = {101, 102, 103, 104}, {102, 104, 105}
bien_mat, moi_them = thang_3 - thang_6, thang_6 - thang_3
assert ket_qua == "Giá TB: 118,200 CLP" and ty_le_chu == "17.8%"
assert round(tb) == 63667
assert bien_mat == {101, 103} and moi_them == {105}
```

Điều kiện `if x` còn loại số 0, trong khi số 0 có thể là một giá trị đã được ghi nhận. Phép hiệu tập hợp chỉ mô tả mã xuất hiện hay vắng trong hai bản dữ liệu. Nó chưa cho biết nguyên nhân một mã biến mất.
:::

### Từ CSV đến báo cáo có thể đọc lại

::: exercise Khảo sát bảng chỗ ở mà chưa dùng pandas
Dùng bảng `visualisations/listings.csv` của Santiago, bản chụp ngày 29/06/2026. Giá tính theo CLP cho mỗi đêm. Tệp được tải từ [Inside Airbnb](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv).

1. Đọc bằng `csv.DictReader`, giữ nguyên mã và các cột dạng chuỗi.
2. Viết hàm chuyển giá sang số, trả `None` cho dữ liệu rỗng, sai định dạng hoặc không hữu hạn. Áp dụng lên toàn bộ cột, đếm giá thiếu, tính trung bình và trung vị.
3. Tìm chỗ ở có giá cao nhất để kiểm tra, không tự xóa chỉ vì giá lớn.
4. Đếm số chỗ ở theo khu, lấy năm khu có nhiều chỗ ở nhất và tính trung vị giá đã biết của từng khu.
5. Lọc các hàng có `number_of_reviews == "0"`, đối chiếu với `last_review`.
6. Ghi báo cáo JSON và đọc lại để kiểm tra.
:::

::: solution
Các kết quả về số dòng hay trung vị phải được tính từ đúng tệp đang đọc. Không thay kết quả tính bằng các hằng số được chép từ một lần chạy khác.

```python
import csv
import json
import math
from collections import Counter, defaultdict
from statistics import median

def doc_bang(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))

def to_float(value):
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None

def tong_hop_python(rows):
    gia = [to_float(r["price"]) for r in rows]
    hop_le = [x for x in gia if x is not None]
    dem_khu = Counter(r["neighbourhood"] for r in rows)
    top5 = sorted(dem_khu.items(), key=lambda kv: (-kv[1], kv[0]))[:5]
    gia_theo_khu = defaultdict(list)
    co_gia = []
    for r, value in zip(rows, gia):
        if value is not None:
            gia_theo_khu[r["neighbourhood"]].append(value)
            co_gia.append((r, value))
    dat_nhat = max(co_gia, key=lambda pair: pair[1])[0] if co_gia else None
    chua_review = [r for r in rows if r["number_of_reviews"] == "0"]
    mau_thuan_review = [r for r in chua_review if r["last_review"] != ""]
    bao_cao = {
        "thanh_pho": "Santiago", "snapshot": "2026-06-29",
        "so_phong": len(rows), "so_phong_co_gia": len(hop_le),
        "so_thieu_gia": len(rows) - len(hop_le),
        "gia_trung_binh_clp": sum(hop_le) / len(hop_le) if hop_le else None,
        "gia_trung_vi_clp": median(hop_le) if hop_le else None,
        "ty_le_chua_review": len(chua_review) / len(rows) if rows else None,
        "gia_trung_vi_theo_khu": {
            khu: median(gia_theo_khu[khu]) if gia_theo_khu[khu] else None
            for khu, _ in top5
        },
    }
    return bao_cao, top5, dat_nhat, mau_thuan_review

def ghi_doc_bao_cao(bao_cao, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(bao_cao, f, ensure_ascii=False, indent=2, allow_nan=False)
    with open(path, encoding="utf-8") as f:
        doc_lai = json.load(f)
    assert doc_lai == bao_cao
    return doc_lai
```

Trung vị ít nhạy với một giá cực lớn hơn trung bình, nhưng vẫn phải kiểm tra đơn vị, thời điểm và tập hàng được giữ. Danh sách `mau_thuan_review` giúp tìm những hàng cần đối chiếu. Nếu danh sách rỗng, ta chỉ biết quy tắc này không phát hiện mâu thuẫn trong bảng đang xét.

Tệp CSV không buộc mọi trường đọc được phải đầy đủ. Trong bài này, cần kiểm tra hàng tiêu đề và sự hiện diện của các cột đã nêu trước khi gọi hàm.
:::

### Xếp hạng khu theo đủ số giá quan sát được

::: exercise Mở rộng từ năm khu sang toàn bộ khu đủ dữ liệu
Lập bảng gồm mọi khu có ít nhất 100 chỗ ở có giá hợp lệ. Mỗi dòng có tên khu, số giá hợp lệ và trung vị, xếp giảm dần theo trung vị. Dùng f-string để căn cột. Không dùng tổng số chỗ ở của khu thay cho số giá hợp lệ.
:::

::: solution
```python
def xep_hang_khu(rows, toi_thieu=100):
    nhom = defaultdict(list)
    for row in rows:
        value = to_float(row["price"])
        if value is not None:
            nhom[row["neighbourhood"]].append(value)
    result = [(khu, len(values), median(values))
              for khu, values in nhom.items() if len(values) >= toi_thieu]
    return sorted(result, key=lambda row: (-row[2], row[0]))

def in_xep_hang(rows, toi_thieu=100):
    for khu, n, trung_vi in xep_hang_khu(rows, toi_thieu):
        print(f"{khu:<20}{n:>10,}{trung_vi:>14,.0f}")
```

Ngưỡng 100 áp dụng sau khi lọc giá thiếu. Một khu có nhiều hàng nhưng phần lớn chưa có giá vẫn có thể bị loại. Thứ tự xếp hạng mô tả các giá đã ghi nhận trong bản chụp, không tự chứng minh chênh lệch do vị trí địa lý gây ra.
:::
