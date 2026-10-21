# Bài 2 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai2_60_cau_hoi.md). Đủ 60 câu: 40 trắc nghiệm, 20 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B2-001 | B |
| B2-002 | A |
| B2-003 | C |
| B2-004 | A |
| B2-005 | B |
| B2-006 | D |
| B2-007 | B |
| B2-011 | A |
| B2-012 | C |
| B2-013 | B |
| B2-014 | C |
| B2-015 | C |
| B2-016 | C |
| B2-017 | B |
| B2-021 | C |
| B2-022 | A |
| B2-023 | C |
| B2-024 | B |
| B2-025 | B |
| B2-026 | C |
| B2-027 | A |
| B2-031 | D |
| B2-032 | A |
| B2-033 | D |
| B2-034 | D |
| B2-035 | A |
| B2-036 | B |
| B2-037 | D |
| B2-041 | B |
| B2-042 | A |
| B2-043 | D |
| B2-044 | C |
| B2-045 | A |
| B2-046 | D |
| B2-051 | D |
| B2-052 | D |
| B2-053 | B |
| B2-054 | C |
| B2-055 | D |
| B2-056 | A |

## Tự luận

### B2-008

`[None, 0, 5]`; get chỉ dùng mặc định khi thiếu khóa, không thay None hay 0.
`c["phi"]` gây KeyError, còn `c.get("phi", 5)` trả 5.

### B2-009

`float(None)` gây TypeError; sửa `except (ValueError, TypeError):`.
Lọc `[x for x in v if x is not None and x > 0]` được `[8.0]`; "0", "-2" đổi được số nhưng không hợp lệ.

### B2-010

In 30.0 vì chia cả 4 phòng thay vì 3 giá đã biết; giữ 0 hợp lệ.
Sửa `tb = sum(co_gia)/len(co_gia) if co_gia else None`, được 40.0; rỗng trả None.

### B2-018

`|An   | 1,200|`
`n = 1200`.

### B2-019

In `4 0 5`: list ngoài riêng, dict còn chung; sửa giá ảnh hưởng a, append chỉ ảnh hưởng b.
Trước khi sửa, tạo `b = [r.copy() for r in a]` để tách các dict phẳng.

### B2-020

Code chọn A/B vì đếm mọi phòng; chỉ B có đủ 2 giá hợp lệ, `[40, 80]`.
Sửa bằng hàm lọc giá rồi đếm độ dài:

```python
def gia_khu(ten):
    return [r["gia"] for r in rows if r["khu"] == ten and r["gia"] is not None and r["gia"] > 0]
chon = sorted(k for k in dem if len(gia_khu(k)) >= 2)
```

### B2-028

In `[15,16]`, là mã mới; sửa `bien_mat = cu - moi` được `[11,12]` sau sắp xếp.
Biểu thức cuối: `[11,12,15,16]`, gồm các mã chỉ có ở một đợt.

### B2-029

In `[30.0,-3.0] 13.5`; truthiness bỏ 0 hợp lệ và giữ giá âm.
Lọc `[x for x in v if x is not None and x >= 0]` được `[30.0,0.0]`, mean 15.0; thử "$0", "$-3".

### B2-030

NameError vì chưa nhập tên cleaning; sửa lời gọi thành `clean_price("$80")`, được 80.0.
Module giúp dùng chung hàm; replace là phương thức của chuỗi s.

### B2-038

(i) list; (ii) dict; (iii) set; (iv) tuple.
`lat, lon = (10, 106)` → lat = 10, lon = 106.

### B2-039

In 30.0, đúng phải 60.0; trả None khi chuyển giá lỗi và chạy lại bước chuyển.
Lọc `[x for x in v if x is not None]`; dùng `sum(g)/len(g) if g else None` với g là list đã lọc.

### B2-040

In 9 do so chuỗi; sửa `gia = [float(r["gia"]) for r in rows if r["gia"] != ""]`.
Max đúng 100.0, vẫn giữ "0"; dùng `max(gia) if gia else None` để xử lý toàn ô trống.

### B2-047

In `[-4,8] 2.0`; lọc `[x for x in nhiet if x is not None]` được `[-4,0,8]`, mean 4/3 °C.
`x > 0` loại cả âm và 0 hợp lệ, còn so None với 0 gây TypeError.

### B2-048

`ids = ["P2","P4"]`; `bang = {"P2":0,"P4":50}`.

```python
ids = [r["id"] for r in rows if r["gia"] is not None and r["gia"] >= 0]
bang = {r["id"]: r["gia"] for r in rows if r["gia"] is not None and r["gia"] >= 0}
```

### B2-049

TypeError khi lọc None > 0; sửa `pos = [x for x in v if x is not None and x > 0]`, được `[10.0]`.
`tb = sum(pos)/len(pos) if pos else None` → 10.0, list rỗng trả None.

### B2-050

In True nhưng so_phong vẫn là chuỗi; trước ghi, sửa `obj["so_phong"] = int(obj["so_phong"])`.
Kiểm `isinstance(doc["so_phong"], int)` và số đếm nguồn; equality chỉ kiểm ghi/đọc khớp.

### B2-057

`('P3',90)`, kiểu tuple; `[m for m,g in sorted(phong,key=lambda p:p[1])[:2]]` → `["P2","P4"]`.
`phong[0]` vẫn là `("P1",40)` vì sorted tạo list mới.

### B2-058

AttributeError tại None.replace; sửa `except (ValueError, AttributeError):`, v = `[10.0,None,0.0,-2.0]`.
Lọc `[x for x in v if x is not None and x > 0]` → `[10.0]`; thử 0/âm để kiểm quy tắc giá dương.

### B2-059

Đọc lại: nhan = "Nam, Bắc", gia = "0"; DictWriter giữ dấu phẩy trong một trường.
`newline=""` để csv quản lý xuống dòng; chế độ w ghi đè:

```python
import csv
with open("phong.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["ma", "nhan", "gia"])
    w.writeheader()
    w.writerow(row)
```

### B2-060

Hiện in `[('2025',1),('2026',2)]`, đếm phòng theo review gần nhất; sửa được 2025:4, 2026:2.
2026 mới nửa năm, chưa đủ suy giảm cả năm hay nguyên nhân:

```python
dem = {}
for r in reviews:
    nam = r["date"][:4]
    dem[nam] = dem.get(nam, 0) + 1
```
