## Thực hành đọc số đánh giá theo năm

::: exercise Tổng hợp một bản chụp có năm chưa trọn
Đọc `visualisations/reviews.csv` của Santiago ngày 29/06/2026 bằng `csv.DictReader`. Tệp có `listing_id` và `date`. Đếm đánh giá theo năm, in theo thứ tự năm và tìm năm có nhiều đánh giá nhất. So sánh 2020–2021 và 2025–2026. Nêu điều gì có thể đọc từ số đếm và điều gì cần thêm bằng chứng.
:::

::: solution
```python
import csv
from collections import Counter
from datetime import date

def dem_review_nam(rows):
    result = Counter()
    for row in rows:
        ngay = date.fromisoformat(row["date"])
        result[str(ngay.year)] += 1
    return dict(sorted(result.items()))

def bao_cao_review_nam(path):
    with open(path, encoding="utf-8-sig", newline="") as file:
        counts = dem_review_nam(csv.DictReader(file))
    for nam, so_luong in counts.items():
        print(nam, so_luong)
    lon_nhat = max(counts.values(), default=None)
    nam_nhieu_nhat = [nam for nam, n in counts.items() if n == lon_nhat]
    return counts, nam_nhieu_nhat
```

Phép đếm mô tả những đánh giá có trong tệp, không trực tiếp đo số lượt khách hay quy mô thị trường. Biến động 2020–2021 có thể dẫn tới giả thuyết về các thay đổi xã hội trong giai đoạn đó, nhưng chỉ riêng bảng này không xác định được nguyên nhân. Cần đối chiếu thêm nguồn và phạm vi thu thập.

Bản chụp ngày 29/06/2026 chưa chứa trọn năm 2026. Vì vậy số của năm này thấp hơn cả năm 2025 chưa đủ để kết luận thị trường co lại. Muốn so sánh, hãy chọn cùng khoảng lịch đã quan sát ở cả hai năm và kiểm tra mức đầy đủ của dữ liệu.
:::
