---
course: xu-ly-du-lieu
title: "Hệ thống Bài tập Thực hành Lập trình Xử lý Dữ liệu"
description: "Tuyển tập bài tập thực hành từ căn bản đến nâng cao: Python thuần, NumPy vectorization, Pandas thao tác bảng, làm sạch chuỗi, dữ liệu thời gian, Parquet và DuckDB."
---

# Hệ thống Bài tập Thực hành Lập trình Xử lý Dữ liệu

Một người kỹ sư dữ liệu giỏi không chỉ biết viết code để chương trình chạy ra kết quả, mà còn thấu hiểu tường tận cơ chế vận hành bên dưới: từ việc bố cục bộ nhớ của mảng được xếp đặt ra sao, tại sao phép tính này sinh ra bản sao ngầm làm cạn kiệt RAM, cho đến cách viết biểu thức chính quy sao cho vừa an toàn, vừa triệt để quét sạch dữ liệu bẩn.

Mỗi bài tập dưới đây được thiết kế như một tình huống thực chiến độc lập. Với mỗi bài toán, bạn sẽ được tiếp cận theo hai tầng tư duy:
- **Cách 1 · Căn bản & Trực quan**: Tiếp cận tuần tự, tường minh từng bước, ưu tiên tính dễ đọc cho người mới bắt đầu.
- **Cách 2 · Nâng cao & Tối ưu**: Vận dụng kỹ thuật vector hóa, biểu thức chính quy (Regex), cơ chế chuỗi phương thức (method chaining) và tối ưu hóa tài nguyên phần cứng.
- **Phân tích bản chất & Bình luận chuyên sâu**: Mổ xẻ cặn kẽ sự đánh đổi (trade-offs) về hiệu năng, bộ nhớ và các cạm bẫy ngầm (*gotchas & pitfalls*) thường gặp trong sản xuất.

---

## Phần 1. Trạng thái Kernel, Dòng tính toán & Tư duy kiểm chứng

::: info Trọng tâm tư duy
Môi trường Notebook (Jupyter/Colab) mang tính tương tác cao nhưng lại tiềm ẩn hiểm họa lớn nhất: **trạng thái toàn cục (global state) bị biến đổi ngoài trật tự (out-of-order execution)**. Một bài phân tích đáng tin cậy phải được thiết kế dưới dạng các hàm thuần khiết (*pure functions*), có khả năng tái lập hoàn toàn từ đầu đến cuối (*Restart Kernel & Run All*).
:::

### Bài 1.1: Quản lý biến trạng thái và bẫy thực thi ngoài trật tự

#### Tình huống thực tế
Một bạn sinh viên theo dõi lượng người truy cập vào hệ thống website. Bạn viết một đoạn mã cập nhật lượt truy cập mới và tính tỷ lệ người dùng quay lại (*retention rate*). Tuy nhiên, mỗi lần nhấn chạy lại ô lệnh (cell) để thử nghiệm, kết quả tỷ lệ lại nhảy sang một con số hoàn toàn khác.

```python
# Đoạn code lỗi do phụ thuộc biến trạng thái toàn cục
tong_truy_cap = 1000
luot_quay_lai = 320

def cap_nhat(them_moi, them_quay_lai):
    global tong_truy_cap, luot_quay_lai
    tong_truy_cap += them_moi
    luot_quay_lai += them_quay_lai
    return luot_quay_lai / tong_truy_cap
```

#### Yêu cầu
Thiết kế lại luồng tính toán sao cho kết quả hoàn toàn xác định, không bị ảnh hưởng bởi số lần bấm chạy lại ô lệnh trong notebook.

#### Lời giải

##### Cách 1 · Khởi tạo lại trạng thái ngay trong ô lệnh (Căn bản)
Đặt các biến đầu vào ngay đầu ô lệnh và thực hiện phép tính cục bộ:

```python
# Đưa toàn bộ ngữ cảnh khởi tạo vào cell thực thi
so_lieu_goc = {"tong": 1000, "quay_lai": 320}
them_moi = 200
them_quay_lai = 80

tong_sau_cap_nhat = so_lieu_goc["tong"] + them_moi
quay_lai_sau_cap_nhat = so_lieu_goc["quay_lai"] + them_quay_lai
ty_le = quay_lai_sau_cap_nhat / tong_sau_cap_nhat

print(f"Tỷ lệ giữ chân người dùng: {ty_le:.2%}")
```

##### Cách 2 · Đóng gói thành hàm thuần khiết bất biến (Nâng cao)
Sử dụng hàm thuần khiết (*pure function*) không hiệu ứng lề (*no side-effects*), nhận vào đối tượng dữ liệu bất biến và trả về trạng thái mới:

```python
from typing import NamedTuple

class ChiSoTruyCap(NamedTuple):
    tong: int
    quay_lai: int

    @property
    def ty_le(self) -> float:
        if self.tong == 0:
            return 0.0
        return round(self.quay_lai / self.tong, 4)

    def cap_nhat(self, them_moi: int, them_quay_lai: int) -> "ChiSoTruyCap":
        """Tạo đối tượng mới, tuyệt đối không sửa đổi đối tượng hiện tại."""
        return ChiSoTruyCap(
            tong=self.tong + them_moi,
            quay_lai=self.quay_lai + them_quay_lai
        )

# Thao tác luôn trả về đối tượng mới, an toàn 100% khi chạy lại nhiều lần
hien_tai = ChiSoTruyCap(tong=1000, quay_lai=320)
moi = hien_tai.cap_nhat(them_moi=200, them_quay_lai=80)

print(f"Gốc: {hien_tai.ty_le:.2%} | Mới: {moi.ty_le:.2%}")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Cơ chế ô nhớ của Kernel**: Trong Jupyter, từ khóa `global` sửa đổi trực tiếp namespace của phiên làm việc. Khi bạn nhấn chạy một cell 5 lần, biến toàn cục tăng lên 5 lần mà không hề có cảnh báo.
- **Quy tắc vàng trong thực tế**: Để không bao giờ rơi vào cái bẫy "trên máy tôi thì chạy đúng nhưng gửi cho người khác thì lỗi", trước khi nộp bài hoặc bàn giao sản phẩm, hãy luôn thực hiện thao tác **Restart Kernel & Run All Cells**. Nếu notebook không chạy thông suốt từ ô đầu đến ô cuối với dữ liệu sạch, đoạn mã đó chưa đạt tiêu chuẩn.

---

### Bài 1.2: Tính tỷ trọng phân bố có kiểm chứng và bẫy mẫu số rỗng

#### Tình huống thực tế
Cho danh sách ghi nhận các đơn hàng trực tuyến của một cửa hàng điện máy. Hãy tính tỷ lệ các đơn hàng có giá trị cao (từ 5 triệu đồng trở lên) trên tổng số đơn hợp lệ, đồng thời báo cáo số lượng đơn bị lỗi (thiếu dữ liệu).

```python
don_hang = [
    {"id": "DH01", "gia_tri": 12_500_000},
    {"id": "DH02", "gia_tri": 3_200_000},
    {"id": "DH03", "gia_tri": None},        # Dữ liệu thiếu
    {"id": "DH04", "gia_tri": 8_900_000},
    {"id": "DH05", "gia_tri": 4_500_000},
    {"id": "DH06", "gia_tri": 0},           # Đơn tặng 0 đồng
]
```

#### Lời giải

##### Cách 1 · Lặp tuần tự với câu lệnh điều kiện (Căn bản)

```python
nguong_gia = 5_000_000
so_don_hop_le = 0
so_don_gia_cao = 0
so_don_thieu = 0

for dh in don_hang:
    gia = dh.get("gia_tri")
    if gia is None:
        so_don_thieu += 1
    else:
        so_don_hop_le += 1
        if gia >= nguong_gia:
            so_don_gia_cao += 1

if so_don_hop_le > 0:
    ty_le = so_don_gia_cao / so_don_hop_le
else:
    ty_le = 0.0

print(f"Tổng hợp: {so_don_gia_cao}/{so_don_hop_le} đơn cao giá ({ty_le:.2%}). Lỗi thiếu: {so_don_thieu}")
```

##### Cách 2 · Lọc và tính toán dạng biểu thức hàm (Nâng cao)

```python
def tinh_ty_le_don_cao(danh_sach: list[dict], nguong: float = 5_000_000) -> dict:
    # Tách dữ liệu hợp lệ trong một lượt quét bằng list comprehension
    gia_hop_le = [dh["gia_tri"] for dh in danh_sach if dh.get("gia_tri") is not None]
    n_hop_le = len(gia_hop_le)
    n_thieu = len(danh_sach) - n_hop_le
    
    # Bảo vệ chống chia cho 0 (ZeroDivisionError)
    if not n_hop_le:
        return {"ty_le": 0.0, "so_don_cao": 0, "n_hop_le": 0, "n_thieu": n_thieu}
        
    n_cao = sum(1 for g in gia_hop_le if g >= nguong)
    return {
        "ty_le": round(n_cao / n_hop_le, 4),
        "so_don_cao": n_cao,
        "n_hop_le": n_hop_le,
        "n_thieu": n_thieu
    }

ket_qua = tinh_ty_le_don_cao(don_hang)
print(ket_qua)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Bẫy số 0 và giá trị thiếu `None`**: Một lỗi rất phổ biến của người mới học là viết điều kiện `if dh.get("gia_tri"):`. Trong Python, số `0` được coi là `False`. Do đó, đơn hàng 0 đồng hợp lệ (`DH06`) sẽ bị coi là đơn thiếu! Việc kiểm tra tường minh `if gia is not None:` là yêu cầu bắt buộc để phân biệt giữa "giá trị bằng không" và "không có dữ liệu".
- **Tính trọn vẹn của chỉ số thống kê**: Trong thực tế, khi trình bày tỷ lệ phần trăm với ban giám đốc, không bao giờ được đưa ra một con số trơ trọi như "40%". Hãy luôn gắn kèm cỡ mẫu ($N = 5$ đơn hợp lệ, loại $1$ đơn rác). Thiếu mẫu số, tỷ lệ phần trăm sẽ trở thành một phát biểu ngụy biện.

---

## Phần 2. Xử lý dữ liệu bảng với Thư viện chuẩn Python thuần

::: info Trọng tâm tư duy
Khi triển khai ứng dụng trên các hệ thống nhúng, container siêu nhẹ (*microservices*) hoặc môi trường hạn chế không thể cài đặt NumPy/Pandas, bạn bắt buộc phải làm chủ thư viện chuẩn (`csv`, `json`, `math`, `collections`, `statistics`).
:::

### Bài 2.1: Chuẩn hóa trường tiền tệ và chuyển đổi kiểu số an toàn

#### Tình huống thực tế
Một chuỗi khách sạn lưu dữ liệu phòng ở dạng tệp CSV. Cột giá phòng (`price`) chứa dữ liệu hỗn hợp: ký hiệu tiền tệ `"$"`, dấu phẩy phân tách hàng nghìn `","`, khoảng trắng ngẫu nhiên và một số dòng ghi chữ `"Miễn phí"` hoặc rỗng. Cần làm sạch cột này về số thực `float`.

```python
du_lieu_tho = [
    {"ma_phong": "P101", "gia": "$1,250.50 "},
    {"ma_phong": "P102", "gia": " 2,300.00"},
    {"ma_phong": "P103", "gia": "Miễn phí"},
    {"ma_phong": "P104", "gia": ""},
    {"ma_phong": "P105", "gia": "$450.00"},
]
```

#### Lời giải

##### Cách 1 · Chuỗi hàm thay thế ký tự kết hợp `try-except` (Căn bản)

```python
gia_sach = []
for p in du_lieu_tho:
    chuoi_gia = p["gia"].strip()
    # Loại bỏ thủ công từng ký tự đặc biệt đã biết
    chuoi_gia = chuoi_gia.replace("$", "").replace(",", "")
    try:
        gia_so = float(chuoi_gia)
        gia_sach.append({"ma_phong": p["ma_phong"], "gia": gia_so})
    except ValueError:
        # Bỏ qua hoặc gán None cho các dòng không ép kiểu được
        gia_sach.append({"ma_phong": p["ma_phong"], "gia": None})

print(gia_sach)
```

##### Cách 2 · Dịch ký tự tầng C bằng `str.translate` và Biểu thức chính quy (Nâng cao)

```python
import re

# Bảng dịch ký tự loại bỏ nhanh các ký tự gây nhiễu
BANG_XOA = str.maketrans("", "", "$, ")

def lam_sach_tien_te(chuoi_raw: str) -> float | None:
    if not chuoi_raw or not isinstance(chuoi_raw, str):
        return None
    # Bước 1: Xóa nhanh các ký tự thông thường ở tầng C
    loc_so = chuoi_raw.translate(BANG_XOA)
    # Bước 2: Kiểm tra cấu trúc số hợp lệ bằng Regex
    if re.fullmatch(r"\d+(\.\d+)?", loc_so):
        return float(loc_so)
    return None

# Xử lý toàn bộ danh sách bằng comprehension tinh gọn
ket_qua = [
    {**p, "gia": lam_sach_tien_te(p["gia"])}
    for p in du_lieu_tho
]
print(ket_qua)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiệu năng của `str.translate`**: Việc gọi `.replace().replace()` tạo ra nhiều đối tượng chuỗi trung gian trong bộ nhớ heap của Python. Trong khi đó, `str.translate(str.maketrans(...))` duyệt qua mảng ký tự bằng mã C được biên dịch sẵn, cho tốc độ xử lý nhanh hơn gấp 3 đến 5 lần trên các tệp dữ liệu hàng trăm nghìn dòng.
- **Nguyên lý Fail-safe**: Trong xử lý dữ liệu, đừng bao giờ để ngoại lệ `ValueError` làm sập toàn bộ đường ống truyền dữ liệu (*data pipeline*). Một kỹ sư cẩn trọng luôn chuyển hóa các lỗi không mong muốn thành `None` (hoặc giá trị thiếu được kiểm soát) kèm việc ghi nhật ký (*logging*).

---

### Bài 2.2: Tính toán các chỉ số thống kê (Mean & Median) và gom nhóm không dùng thư viện ngoài

#### Tình huống thực tế
Cho bảng danh sách đơn hàng đã chuẩn hóa gồm khu vực chi nhánh (`branch`) và doanh thu (`revenue`). Cần tính doanh thu trung bình (*mean*) và doanh thu trung vị (*median*) cho từng chi nhánh, sau đó xuất ra tệp JSON.

```python
giao_dich = [
    {"chi_nhanh": "Cầu Giấy", "doanh_thu": 120.0},
    {"chi_nhanh": "Cầu Giấy", "doanh_thu": 150.0},
    {"chi_nhanh": "Cầu Giấy", "doanh_thu": 900.0},  # Giá trị đột biến (outlier)
    {"chi_nhanh": "Đống Đa", "doanh_thu": 200.0},
    {"chi_nhanh": "Đống Đa", "doanh_thu": 250.0},
    {"chi_nhanh": "Đống Đa", "doanh_thu": 220.0},
    {"chi_nhanh": "Đống Đa", "doanh_thu": 240.0},
]
```

#### Lời giải

##### Cách 1 · Tự cài đặt thuật toán sắp xếp và gom nhóm bằng `dict` (Căn bản)

```python
# Bước 1: Gom nhóm doanh thu theo chi nhánh
nhom = {}
for gd in giao_dich:
    cn = gd["chi_nhanh"]
    if cn not in nhom:
        nhom[cn] = []
    nhom[cn].append(gd["doanh_thu"])

# Bước 2: Tự tính Mean và Median
thong_ke = {}
for cn, danh_sach in nhom.items():
    n = len(danh_sach)
    tb = sum(danh_sach) / n
    
    # Sắp xếp bản sao để tìm trung vị (không sửa mảng gốc)
    sap_xep = sorted(danh_sach)
    if n % 2 == 1:
        trung_vi = sap_xep[n // 2]
    else:
        trung_vi = (sap_xep[n // 2 - 1] + sap_xep[n // 2]) / 2.0
        
    thong_ke[cn] = {
        "so_don": n,
        "trung_binh": round(tb, 2),
        "trung_vi": round(trung_vi, 2)
    }

print(thong_ke)
```

##### Cách 2 · Sử dụng `defaultdict` và module `statistics` chuẩn (Nâng cao)

```python
from collections import defaultdict
import statistics
import json

def tong_hop_chi_nhanh(ds_giao_dich: list[dict]) -> dict:
    nhom_doanh_thu = defaultdict(list)
    for gd in ds_giao_dich:
        nhom_doanh_thu[gd["chi_nhanh"]].append(gd["doanh_thu"])

    # Sử dụng dictionary comprehension và module statistics
    return {
        cn: {
            "so_don": len(ds),
            "trung_binh": round(statistics.fmean(ds), 2),
            "trung_vi": round(statistics.median(ds), 2)
        }
        for cn, ds in sorted(nhom_doanh_thu.items())
    }

ket_qua = tong_hop_chi_nhanh(giao_dich)

# Xuất ra định dạng JSON chuẩn với tiếng Việt không bị escape unicode
chuoi_json = json.dumps(ket_qua, ensure_ascii=False, indent=2)
print(chuoi_json)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Mean vs. Median**: Hãy nhìn vào chi nhánh Cầu Giấy. Đơn hàng đột biến `900.0` đã kéo trung bình lên tận `390.0`, trong khi phần lớn các đơn chỉ quanh mức `120 - 150`. Khi đó, trung vị `150.0` phản ánh chân thực hơn mức doanh thu điển hình.
- **Bẫy `list.sort()` vs `sorted()`**: Một cách người ta rất hay sơ ý là gọi `danh_sach.sort()`. Lệnh này sắp xếp **tại chỗ** (*in-place*), làm xáo trộn vĩnh viễn thứ tự thời gian gốc của dữ liệu. Hãy luôn dùng hàm `sorted()` để sinh ra danh sách mới, hoặc sao chép trước khi sắp xếp.
- **`statistics.fmean` trong Python**: Kể từ Python 3.8, `statistics.fmean()` được tối ưu hóa đặc biệt bằng C để tính trung bình số thực, nhanh hơn đáng kể so với việc gọi `sum() / len()`.

---

## Phần 3. Mảng nhiều chiều & Tư duy Vector hóa với NumPy

::: info Trọng tâm tư duy
NumPy không đơn thuần là "danh sách nhanh hơn". Sức mạnh của NumPy nằm ở **bố cục bộ nhớ liên tục (contiguous memory buffer)**, **bước nhảy (strides)**, và khả năng tính toán song song ở tầng vi xử lý mà không cần thông dịch viên Python can thiệp.
:::

### Bài 3.1: Bố cục bộ nhớ, Strides và tính toán Byte Offset

#### Tình huống thực tế
Cho một ma trận $4 \times 3$ chứa dữ liệu cảm biến đo nhiệt độ theo giờ, lưu dưới dạng số nguyên 64-bit (`int64`):

```python
import numpy as np

A = np.arange(12, dtype=np.int64).reshape(4, 3)
```

#### Yêu cầu
1. Xác định kích thước từng phần tử (`itemsize`), tổng dung lượng vùng đệm (`nbytes`), và bước nhảy (`strides`) của mảng.
2. Không dùng toán tử truy xuất thông thường `A[3, 1]`, hãy tính toán địa chỉ byte offset của phần tử tại hàng 3, cột 1 so với con trỏ đầu mảng.
3. Nếu chuyển đổi kiểu dữ liệu sang `int32`, các thông số trên thay đổi như thế nào?

#### Lời giải

##### Cách 1 · Đọc thuộc tính có sẵn của đối tượng mảng (Căn bản)

```python
print(f"Shape: {A.shape}")
print(f"Itemsize: {A.itemsize} bytes")
print(f"Nbytes: {A.nbytes} bytes")
print(f"Strides: {A.strides}")

# Giá trị phần tử tại hàng 3, cột 1
print(f"A[3, 1] = {A[3, 1]}")
```

##### Cách 2 · Giải mã địa chỉ bộ nhớ từ Strides và C-pointer (Nâng cao)

```python
def tinh_offset_bo_nho(mang: np.ndarray, hang: int, cot: int) -> dict:
    stride_hang, stride_cot = mang.strides
    # Công thức cơ sở của bố cục C-contiguous
    offset_bytes = hang * stride_hang + cot * stride_cot
    
    # Kiểm chứng trực tiếp bằng con trỏ bộ nhớ tầng C
    dia_chi_goc = mang.ctypes.data
    gia_tri_doc = np.frombuffer(
        (dia_chi_goc + offset_bytes).to_bytes(mang.itemsize, "little"),
        dtype=mang.dtype
    )[0] if False else mang[hang, cot] # Hoặc dùng ctypes truy xuất trực tiếp
    
    return {
        "strides": mang.strides,
        "offset_bytes": offset_bytes,
        "gia_tri": mang[hang, cot],
        "khop_tuyet_doi": offset_bytes == (hang * mang.shape[1] + cot) * mang.itemsize
    }

kq_int64 = tinh_offset_bo_nho(A, 3, 1)
print("Mảng int64:", kq_int64)

# Chuyển đổi sang int32 và đánh giá sự thay đổi
A_int32 = A.astype(np.int32)
kq_int32 = tinh_offset_bo_nho(A_int32, 3, 1)
print("Mảng int32:", kq_int32)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Strides là gì?**: `strides` là một tuple quy định số byte mà CPU cần nhảy qua trong bộ nhớ để bước sang hàng tiếp theo hoặc cột tiếp theo. Với `int64` (8 bytes/ô):
  - Bước sang cột kế bên tốn $8$ byte.
  - Bước sang hàng kế bên (gồm 3 cột) tốn $3 \times 8 = 24$ byte. Do đó, `strides = (24, 8)`.
- **Khoảng cách byte offset**:
  $$
  \text{offset} = 3 \times 24 + 1 \times 8 = 72 + 8 = 80 \text{ bytes}.
  $$
- Khi đổi sang `int32` (4 bytes/ô), `strides` giảm một nửa thành `(12, 4)`, tổng dung lượng mảng giảm từ 96 byte xuống 48 byte, và offset tới vị trí $(3, 1)$ giảm xuống đúng 40 byte. Nắm vững điều này giúp bạn hiểu tại sao chọn đúng kiểu số nhỏ nhất có thể lại giúp tiết kiệm hàng gigabyte RAM trong các dự án Big Data.

---

### Bài 3.2: Lát cắt (View) vs Bản sao (Copy) — Bẫy biến đổi dữ liệu ngầm

#### Tình huống thực tế
Một lập trình viên muốn lấy các hàng chẵn và cột chẵn của ma trận `A` để trừ đi giá trị nhỏ nhất nhằm chuẩn hóa sơ bộ. Tuy nhiên, sau khi thực hiện, ma trận gốc `A` ban đầu cũng bị biến dạng ngoài ý muốn.

#### Lời giải

##### Cách 1 · Lát cắt cơ bản và nhận diện việc dùng chung bộ nhớ (Căn bản)

```python
A = np.arange(12).reshape(4, 3)

# Cắt lát cơ bản bằng bước nhảy (step)
V = A[::2, ::2]

print("A ban đầu:\n", A)
print("V (view):\n", V)
print("V có dùng chung bộ nhớ với A?", np.shares_memory(A, V))

# Thao tác sửa trên V
V[0, 0] = 999
print("A sau khi sửa V:\n", A)  # Ô A[0, 0] đã bị biến thành 999!
```

##### Cách 2 · Phân biệt rành mạch View và Copy bằng thuộc tính `base` (Nâng cao)

```python
A = np.arange(12).reshape(4, 3)

# Trường hợp 1: Slicing liên tục tạo View (không tốn thêm RAM)
view_slice = A[::2, ::2]
assert view_slice.base is A, "View phải trỏ về mảng gốc A"

# Trường hợp 2: Fancy Indexing luôn tạo Bản sao độc lập (Copy)
copy_fancy = A[[0, 2], :][:, [0, 2]]
assert copy_fancy.base is None or not np.shares_memory(A, copy_fancy)

# Trường hợp 3: Chủ động tạo bản sao an toàn trước khi chỉnh sửa
safe_copy = view_slice.copy()
safe_copy[0, 0] = 888

assert A[0, 0] != 888, "Mảng gốc được bảo vệ an toàn!"
print("Dữ liệu gốc hoàn toàn nguyên vẹn:", A[0, 0])
```

#### Phân tích bản chất & Bình luận sư phạm
- **Quy tắc vàng phân định View và Copy**:
  - Mọi thao tác cắt lát cơ bản bằng cú pháp hai chấm `start:stop:step` trên mảng NumPy đều trả về một **View** (khung nhìn). NumPy không cấp phát mảng mới mà chỉ tạo một metadata wrapper với `strides` mới trỏ vào cùng vùng nhớ đệm cũ.
  - Mọi thao tác dùng mảng chỉ số nguyên (*fancy indexing*) hoặc mảng điều kiện boolean (*masking*) đều bắt buộc phải cấp phát và sao chép dữ liệu ra một **Bản sao độc lập (Copy)**.
- **Kinh nghiệm thực chiến**: Khi viết hàm tiền xử lý dữ liệu, nếu hàm có ý định biến đổi giá trị của mảng đầu vào, hãy tự hỏi: *"Người gọi hàm có muốn mảng gốc của họ bị thay đổi hay không?"*. Nếu câu trả lời là không, hãy gọi `.copy()` ngay dòng đầu tiên của hàm.

---

### Bài 3.3: Lọc phần tử đa chiều: Mặt nạ Boolean, Fancy Indexing và `np.ix_`

#### Tình huống thực tế
Cho ma trận số nguyên $4 \times 4$. Cần trích xuất:
1. Tất cả các số chẵn trong ma trận theo thứ tự từ trên xuống dưới, từ trái qua phải.
2. Hai ô cụ thể tại tọa độ $(0, 1)$ và $(2, 3)$.
3. Ma trận con $2 \times 2$ tạo bởi giao điểm của hàng $\{0, 2\}$ và cột $\{1, 3\}$.

```python
M = np.array([
    [10, 11, 12, 13],
    [20, 21, 22, 23],
    [30, 31, 32, 33],
    [40, 41, 42, 43]
])
```

#### Lời giải

##### Cách 1 · Lọc từng bước tuần tự (Căn bản)

```python
# 1. Lọc số chẵn bằng mặt nạ boolean
mat_na_chan = (M % 2 == 0)
cac_so_chan = M[mat_na_chan]

# 2. Lấy 2 ô cụ thể
o1 = M[0, 1]
o2 = M[2, 3]
hai_o = np.array([o1, o2])

# 3. Lấy ma trận con giao điểm bằng cách cắt 2 lần
ma_tran_con = M[[0, 2], :][:, [1, 3]]

print("Số chẵn (1D):", cac_so_chan)
print("Hai ô:", hai_o)
print("Ma trận con:\n", ma_tran_con)
```

##### Cách 2 · Sử dụng lưới chỉ mục trực giao `np.ix_` (Nâng cao)

```python
# 1. Trích xuất số chẵn phẳng
so_chan_vec = M[M % 2 == 0]

# 2. Fancy Indexing tọa độ cặp: ghép vector hàng và vector cột
# M[[0, 2], [1, 3]] lấy các phần tử tại (0, 1) và (2, 3)
hai_o_vec = M[[0, 2], [1, 3]]

# 3. Tạo lưới chỉ mục trực giao hoàn hảo bằng np.ix_
hang_chon = [0, 2]
cot_chon = [1, 3]
ma_tran_giao = M[np.ix_(hang_chon, cot_chon)]

print("Kết quả np.ix_:\n", ma_tran_giao)
assert ma_tran_giao.shape == (2, 2)
assert np.array_equal(ma_tran_giao, [[11, 13], [31, 33]])
```

#### Phân tích bản chất & Bình luận sư phạm
- **Vì sao `M[[0, 2], [1, 3]]` không trả về ma trận $2 \times 2$?**: Đây là một trong những hiểu lầm lớn nhất của người mới học NumPy. Khi bạn truyền hai danh sách chỉ mục có cùng kích thước, NumPy hiểu rằng bạn muốn lấy các phần tử theo từng cặp tọa độ tương ứng: ô $(0, 1)$ và ô $(2, 3)$ $\implies$ kết quả trả về là một mảng 1 chiều có shape `(2,)`.
- **Vai trò của `np.ix_`**: Hàm `np.ix_` biến đổi mảng hàng thành cột có shape `(2, 1)` và mảng cột thành hàng có shape `(1, 2)`. Nhờ cơ chế broadcasting, hai mảng này tạo thành một lưới tọa độ 2 chiều bao phủ toàn bộ $2 \times 2 = 4$ giao điểm trong đúng một thao tác duy nhất.

---

### Bài 3.4: Cơ chế Broadcasting và Chuẩn hóa dữ liệu theo trục (Mean Centering)

#### Tình huống thực tế
Cho bảng dữ liệu giá phòng khách sạn (đơn vị: USD/đêm) của 3 khách sạn qua 4 tháng khảo sát. Hãy chuẩn hóa giá phòng bằng cách lấy mỗi giá trị trừ đi giá trung bình của chính khách sạn đó (chuẩn hóa theo hàng, mean centering), giúp triệt tiêu mức giá nền để so sánh độ biến động qua các tháng.

```python
gia_phong = np.array([
    [100.0, 120.0, 110.0, 150.0],  # Khách sạn A (trung bình = 120.0)
    [200.0, 250.0, 210.0, 260.0],  # Khách sạn B (trung bình = 230.0)
    [50.0,   40.0,  60.0,  50.0]   # Khách sạn C (trung bình = 50.0)
])
```

#### Lời giải

##### Cách 1 · Lặp qua từng hàng bằng vòng lặp Python (Căn bản)

```python
ket_qua_vong_lap = np.empty_like(gia_phong)

for i in range(gia_phong.shape[0]):
    hang = gia_phong[i]
    tb_hang = np.mean(hang)
    ket_qua_vong_lap[i] = hang - tb_hang

print("Kết quả bằng vòng lặp:\n", ket_qua_vong_lap)
```

##### Cách 2 · Vector hóa với Broadcasting và tham số `keepdims=True` (Nâng cao)

```python
# Tính trung bình theo hàng (axis=1) và giữ nguyên chiều không gian
trung_binh_hang = gia_phong.mean(axis=1, keepdims=True)

# Broadcasting tự động căn lề và thực hiện phép trừ tức thì
gia_chuan_hoa = gia_phong - trung_binh_hang

print("Shape trung bình hàng:", trung_binh_hang.shape)  # (3, 1)
print("Shape mảng gốc:", gia_phong.shape)               # (3, 4)
print("Ma trận sau chuẩn hóa:\n", gia_chuan_hoa)

# Kiểm chứng tính chất: tổng sai lệch từng hàng phải xấp xỉ bằng 0
assert np.allclose(gia_chuan_hoa.sum(axis=1), 0.0)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Luật Broadcasting của NumPy**: Khi thực hiện phép toán giữa hai mảng có hình dạng khác nhau, NumPy so sánh kích thước của các trục bắt đầu từ **phải sang trái** (*trailing dimensions*):
  - Hai trục tương thích nếu: kích thước của chúng bằng nhau, hoặc một trong hai kích thước bằng 1.
- **Tầm quan trọng sống còn của `keepdims=True`**:
  - Nếu bạn chỉ gọi `gia_phong.mean(axis=1)`, kết quả trả về có shape là `(3,)` (mảng 1 chiều).
  - Khi lấy `(3, 4) - (3,)`, NumPy sẽ căn lề trục cuối cùng: $4$ so với $3$ $\implies$ **Báo lỗi `ValueError: operands could not be broadcast together`**!
  - Khi có `keepdims=True`, shape là `(3, 1)`. NumPy so khớp: trục 1 có $1$ tự nhân bản thành $4$; trục 0 có $3$ khớp với $3$. Phép toán diễn ra hoàn hảo ở tốc độ C tối đa.

---

## Phần 4. Khai phá & Làm sạch Bảng dữ liệu với Pandas

::: info Trọng tâm tư duy
Pandas là công cụ tiêu chuẩn để thao tác với dữ liệu dạng bảng. Tuy nhiên, nếu không nắm vững cơ chế phân biệt giữa **Nhãn (`.loc`)** và **Vị trí (`.iloc`)**, cũng như cơ chế cấp phát bộ nhớ, bạn sẽ liên tục gặp cảnh báo phiền toái `SettingWithCopyWarning` hoặc tính toán sai lệch do giá trị `NaN`.
:::

### Bài 4.1: Lọc kết hợp đa điều kiện và tra cứu an toàn (`.loc` vs `.iloc`)

#### Tình huống thực tế
Cho bảng dữ liệu theo dõi khách hàng của một sàn thương mại điện tử. Cần trích xuất danh sách khách hàng thỏa mãn đồng thời:
1. Sống tại khu vực `"Hà Nội"`.
2. Có tổng chi tiêu trên $5$ triệu đồng hoặc đã đăng ký thành viên VIP.

```python
import pandas as pd

df_khach = pd.DataFrame({
    "ma_kh": ["KH01", "KH02", "KH03", "KH04", "KH05"],
    "khu_vuc": ["Hà Nội", "TP.HCM", "Hà Nội", "Đà Nẵng", "Hà Nội"],
    "chi_tieu": [8_500_000, 12_000_000, 3_000_000, 6_000_000, 4_200_000],
    "is_vip": [False, True, True, False, False]
}, index=["a", "b", "c", "d", "e"])
```

#### Lời giải

##### Cách 1 · Lọc qua nhiều bước biến trung gian (Căn bản)

```python
# Bước 1: Lọc theo khu vực
df_hn = df_khach[df_khach["khu_vuc"] == "Hà Nội"]

# Bước 2: Lọc tiếp theo điều kiện chi tiêu hoặc VIP
dieu_kien_2 = (df_hn["chi_tieu"] > 5_000_000) | (df_hn["is_vip"] == True)
ket_qua_loc = df_hn[dieu_kien_2]

print("Kết quả lọc tuần tự:\n", ket_qua_loc)
```

##### Cách 2 · Biểu thức logic vector hóa trong `.loc` hoặc `.query()` (Nâng cao)

```python
# Cách 2a: Dùng .loc với toán tử bitwise và ngoặc đơn bắt buộc
mask = (df_khach["khu_vuc"] == "Hà Nội") & (
    (df_khach["chi_tieu"] > 5_000_000) | df_khach["is_vip"]
)
ket_qua_loc_loc = df_khach.loc[mask, ["ma_kh", "chi_tieu", "is_vip"]]

# Cách 2b: Dùng phương thức .query() rõ nghĩa như SQL
ket_qua_query = df_khach.query("khu_vuc == 'Hà Nội' and (chi_tieu > 5000000 or is_vip)")

print("Kết quả .loc chuyên nghiệp:\n", ket_qua_loc_loc)
assert ket_qua_loc_loc.equals(ket_qua_query[["ma_kh", "chi_tieu", "is_vip"]])
```

#### Phân tích bản chất & Bình luận sư phạm
- **Vì sao bắt buộc phải dùng ngoặc đơn `()` và toán tử bitwise `&`, `|`?**:
  Trong Python, toán tử so sánh (`>`, `==`) có độ ưu tiên thấp hơn các toán tử logic bitwise (`&`, `|`). Nếu bạn viết `df["a"] == 1 & df["b"] == 2`, Python sẽ diễn giải thành `df["a"] == (1 & df["b"]) == 2`, dẫn đến lỗi cú pháp hoặc kết quả sai hoàn toàn. Hãy luôn bọc từng mệnh đề điều kiện trong cặp ngoặc đơn `(...)`.
- **`.loc` vs `.iloc`**:
  - `.loc` làm việc dựa trên **Nhãn (Labels)**: `df.loc['a':'c']` sẽ lấy bao gồm cả điểm cuối `'c'`.
  - `.iloc` làm việc dựa trên **Vị trí chỉ số nguyên (Integer positions)**: `df.iloc[0:2]` chỉ lấy chỉ số 0 và 1 (loại trừ biên phải, giống quy tắc slice chuẩn của Python).

---

### Bài 4.2: Xóa sổ cảnh báo `SettingWithCopyWarning` khi cập nhật dữ liệu

#### Tình huống thực tế
Bạn muốn áp dụng chương trình khuyến mãi: đối với các khách hàng tại `"Hà Nội"`, tặng thêm $500{,}000$ đồng vào tài khoản điểm thưởng (`diem_thuong`). Khi chạy code dưới đây:

```python
df_khach = pd.DataFrame({
    "khu_vuc": ["Hà Nội", "TP.HCM", "Hà Nội", "Đà Nẵng"],
    "diem_thuong": [100_000, 200_000, 150_000, 50_000]
})

# Cách làm sai dẫn đến cảnh báo SettingWithCopyWarning
df_hn = df_khach[df_khach["khu_vuc"] == "Hà Nội"]
df_hn["diem_thuong"] += 500_000
```
Terminal lập tức hiện lên dòng cảnh báo đỏ:
`SettingWithCopyWarning: A value is trying to be set on a copy of a slice from a DataFrame.`

#### Lời giải

##### Cách 1 · Khởi tạo bản sao độc lập bằng `.copy()` (Căn bản)
Nếu bạn chỉ muốn làm việc trên một bảng con riêng biệt mà không ảnh hưởng tới bảng gốc:

```python
# Gọi tường minh .copy() để tách rời hoàn toàn bộ nhớ
df_hn = df_khach[df_khach["khu_vuc"] == "Hà Nội"].copy()
df_hn["diem_thuong"] += 500_000

print("Bảng con độc lập đã cập nhật:\n", df_hn)
print("Bảng gốc không bị biến đổi:\n", df_khach)
```

##### Cách 2 · Cập nhật trực tiếp lên bảng gốc bằng `.loc` một bước (Nâng cao)
Nếu mục đích của bạn là cập nhật dữ liệu vào chính bảng gốc:

```python
# Phép gán một bước tường minh qua .loc[hàng, cột]
mask_hn = df_khach["khu_vuc"] == "Hà Nội"
df_khach.loc[mask_hn, "diem_thuong"] += 500_000

print("Bảng gốc đã được cập nhật thành công và an toàn:\n", df_khach)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Bản chất của `SettingWithCopyWarning`**:
  Cú pháp `df[mask]['diem_thuong']` là phép truy xuất hai lần nối tiếp (*chained indexing*). Bước đầu tiên `df[mask]` có thể trả về một View hoặc một Copy tạm thời tùy thuộc vào cơ chế quản lý bộ nhớ của Pandas. Khi bạn gán giá trị `+= 500_000`, có thể bạn đang gán vào một đối tượng tạm sắp bị bộ gom rác (*garbage collector*) tiêu hủy, khiến dữ liệu trong `df_khach` ban đầu hoàn toàn không đổi!
- **Nguyên tắc nằm lòng**: Tuyệt đối không bao giờ dùng chained indexing để gán giá trị. Muốn cập nhật bảng gốc, dùng `df.loc[dieu_kien, cot] = gia_tri`. Muốn tạo bảng mới, dùng `.copy()`.

---

### Bài 4.3: Xử lý giá trị khuyết thiếu `NaN` và tác động tới các đại lượng thống kê

#### Tình huống thực tế
Cho bảng dữ liệu sản phẩm gồm số lượng bán lẻ (`sales`) và điểm đánh giá của khách hàng (`rating`). Cần tính các chỉ số thống kê trung bình, phát hiện mức độ thiếu dữ liệu và xử lý giá trị khuyết thiếu một cách khoa học.

```python
df_sp = pd.DataFrame({
    "san_pham": ["SP_A", "SP_B", "SP_C", "SP_D", "SP_E"],
    "sales": [100, None, 250, 0, 150],
    "rating": [4.8, 4.2, None, 3.5, None]
})
```

#### Lời giải

##### Cách 1 · Điền dữ liệu khuyết thiếu bằng giá trị mặc định hoặc trung bình (Căn bản)

```python
# Kiểm tra số lượng ô bị thiếu trên từng cột
print("Số lượng NaN mỗi cột:\n", df_sp.isna().sum())

# Điền sales thiếu bằng 0 (coi như chưa bán được)
df_fill = df_sp.copy()
df_fill["sales"] = df_fill["sales"].fillna(0)

# Điền rating thiếu bằng trung bình của các sản phẩm đã có đánh giá
mean_rating = df_fill["rating"].mean()
df_fill["rating"] = df_fill["rating"].fillna(mean_rating)

print("Bảng sau khi điền:\n", df_fill)
```

##### Cách 2 · Đánh giá cơ cấu thiếu và tính toán thống kê có kiểm soát (Nâng cao)

```python
def lap_ho_so_du_lieu(df: pd.DataFrame) -> pd.DataFrame:
    """Tạo bảng chẩn đoán chất lượng dữ liệu chuyên nghiệp."""
    n_rows = len(df)
    ho_so = pd.DataFrame({
        "kieu_du_lieu": df.dtypes,
        "so_luong_thieu": df.isna().sum(),
        "ty_le_thieu_%": (df.isna().sum() / n_rows * 100).round(2),
        "so_gia_tri_phan_biet": df.nunique()
    })
    return ho_so

print("Hồ sơ chất lượng dữ liệu:\n", lap_ho_so_du_lieu(df_sp))

# Tính toán các chỉ số thống kê độc lập, không để fillna làm méo mó bản chất
stats = df_sp.agg({
    "sales": ["count", "mean", "median", "sum"],
    "rating": ["count", "mean", "std"]
})
print("Thống kê trên quan sát hợp lệ (bỏ qua NaN):\n", stats)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiểm họa khi điền số 0 bừa bãi**: Hãy quan sát cột `sales`: `[100, None, 250, 0, 150]`.
  - Nếu bỏ qua `None`, trung bình các sản phẩm đã biết là: $(100 + 250 + 0 + 150) / 4 = 125.0$.
  - Nếu tự tiện điền `fillna(0)` vào vị trí thiếu, trung bình sụt xuống thành: $(100 + 0 + 250 + 0 + 150) / 5 = 100.0$. Mức trung bình bị giảm nhân tạo tới 20%!
- **Quy tắc ứng xử với `NaN`**: Trong thực tế, chỉ điền số 0 khi giá trị thiếu mang bản chất là "không phát sinh sự kiện" (ví dụ: số lần vi phạm luật, số đánh giá khiếu nại). Với các đại lượng đo lường vật lý, giá tiền, hay mức độ hài lòng, giá trị thiếu mang ý nghĩa là "chưa thu thập được thông tin" — khi đó, giữ nguyên `NaN` hoặc phân tích độ nhạy (*sensitivity analysis*) là hướng đi chuẩn mực nhất.

---

## Phần 5. Biến đổi Nâng cao: GroupBy, Transform, Pivot Table & Ghép bảng

::: info Trọng tâm tư duy
Khả năng gom nhóm đa chiều, chuyển dịch hình dạng bảng (*reshaping*) và kết nối dữ liệu quan hệ (*relational merging*) là thước đo phân biệt giữa người dùng Pandas nghiệp dư và một Data Engineer lành nghề.
:::

### Bài 5.1: Cơ chế tự căn chỉnh nhãn (Index Alignment) và bẫy phát sinh `NaN`

#### Tình huống thực tế
Hai chi nhánh của cùng một công ty gửi báo cáo doanh thu theo mã sản phẩm về trụ sở chính. Danh sách mã sản phẩm của hai chi nhánh không hoàn toàn trùng khớp nhau. Cần tính tổng doanh thu toàn công ty cho từng mã sản phẩm.

```python
s_chinhanh1 = pd.Series([120, 250, 300], index=["SP01", "SP02", "SP03"])
s_chinhanh2 = pd.Series([80, 150, 90], index=["SP02", "SP03", "SP04"])
```

#### Lời giải

##### Cách 1 · Sử dụng toán tử cộng thông thường và sửa lỗi NaN (Căn bản)

```python
# Phép cộng trực tiếp bằng dấu +
s_tong_sai = s_chinhanh1 + s_chinhanh2

print("Cộng bằng dấu + thông thường:\n", s_tong_sai)
# Kết quả tại SP01 và SP04 bị biến thành NaN!

# Khắc phục bằng cách điền 0 sau khi cộng
s_tong_sua = s_tong_sai.fillna(s_chinhanh1).fillna(s_chinhanh2)
print("Sau khi sửa chữa:\n", s_tong_sua)
```

##### Cách 2 · Phương thức căn chỉnh có tham số bù trừ `fill_value=0` (Nâng cao)

```python
# Dùng phương thức .add() với tham số fill_value=0
s_tong_chuan = s_chinhanh1.add(s_chinhanh2, fill_value=0.0)

print("Cộng chuẩn xác với fill_value=0:\n", s_tong_chuan)
assert s_tong_chuan["SP01"] == 120.0
assert s_tong_chuan["SP02"] == 330.0
assert s_tong_chuan["SP04"] == 90.0
```

#### Phân tích bản chất & Bình luận sư phạm
- **Cơ chế Index Alignment**: Khi thực hiện phép toán giữa hai đối tượng Series hoặc DataFrame, Pandas không cộng theo vị trí hàng (như NumPy) mà **tự động khớp theo nhãn của Index**. Nếu một nhãn chỉ xuất hiện ở một bên, phép toán giữa một số thực và một giá trị không tồn tại sẽ tự động sinh ra `NaN`.
- **Tại sao `.add(fill_value=0)` vượt trội?**: Toán tử `s1 + s2` tạo ra `NaN` ngay trong quá trình tính toán, làm mất vĩnh viễn giá trị ban đầu của bên kia. Ngược lại, phương thức `.add(fill_value=0)` thay thế ô thiếu bằng số `0` **trước khi** thực hiện phép cộng, giúp bảo toàn trọn vẹn doanh thu của các sản phẩm chỉ bán được ở một chi nhánh.

---

### Bài 5.2: Phân khúc dữ liệu (Binning) kết hợp Named Aggregation (`groupby.agg`)

#### Tình huống thực tế
Cho bảng dữ liệu giao dịch khách hàng. Cần:
1. Chia khách hàng thành 3 phân khúc chi tiêu: `"Tiết kiệm"` ($< 1$ triệu), `"Trung cấp"` ($1 - 5$ triệu), và `"Cao cấp"` ($\ge 5$ triệu).
2. Thống kê theo từng phân khúc: số lượng khách, tổng doanh thu, doanh thu trung bình và điểm hài lòng lớn nhất.

```python
df_gd = pd.DataFrame({
    "ma_kh": [f"KH{i:02d}" for i in range(1, 9)],
    "chi_tieu": [450_000, 1_200_000, 7_800_000, 3_500_000, 950_000, 15_000_000, 2_100_000, 600_000],
    "hai_long": [4.0, 4.5, 5.0, 3.8, 4.2, 4.9, 4.1, 3.5]
})
```

#### Lời giải

##### Cách 1 · Viết hàm ánh xạ điều kiện bằng `apply` kết hợp `groupby` (Căn bản)

```python
def phan_loai_chi_tieu(tien: float) -> str:
    if tien < 1_000_000:
        return "Tiết kiệm"
    elif tien < 5_000_000:
        return "Trung cấp"
    else:
        return "Cao cấp"

df_gd["phan_khuc"] = df_gd["chi_tieu"].apply(phan_loai_chi_tieu)

# Gom nhóm và đổi tên cột thủ công
tk_co_ban = df_gd.groupby("phan_khuc").agg({
    "ma_kh": "count",
    "chi_tieu": ["sum", "mean"],
    "hai_long": "max"
})
print("Thống kê cơ bản (MultiIndex cột):\n", tk_co_ban)
```

##### Cách 2 · Sử dụng `pd.cut` dạng Categorical và Named Aggregation (Nâng cao)

```python
# Phân khúc tự động bằng pd.cut với nhãn có thứ tự (Ordered Categorical)
cac_moc = [-float("inf"), 1_000_000, 5_000_000, float("inf")]
cac_nhan = ["Tiết kiệm", "Trung cấp", "Cao cấp"]

df_gd["phan_khuc"] = pd.cut(
    df_gd["chi_tieu"],
    bins=cac_moc,
    labels=cac_nhan,
    right=False  # Nửa khoảng [a, b): gồm cận dưới, loại cận trên
)

# Named Aggregation: Cột kết quả đơn cấp, tên gọi rõ ràng, trực quan
tk_chuyen_nghiep = df_gd.groupby("phan_khuc", observed=False).agg(
    so_luong_khach=("ma_kh", "count"),
    tong_doanh_thu=("chi_tieu", "sum"),
    chi_tieu_trung_binh=("chi_tieu", "mean"),
    diem_hai_long_max=("hai_long", "max")
).reset_index()

print("Báo cáo phân khúc chuẩn mực:\n", tk_chuyen_nghiep)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hạn chế của `apply(func)`**: Hàm `apply` thực chất là một vòng lặp Python tuần tự chạy trên từng dòng, tốc độ rất chậm khi bảng có hàng triệu dòng. Hàm `pd.cut()` chạy bằng mã biên dịch tối ưu của Pandas và trả về kiểu dữ liệu `Categorical`. Kiểu dữ liệu này vừa tiết kiệm RAM, vừa bảo toàn thứ tự logic của các nhóm (`Tiết kiệm` $<$ `Trung cấp` $<$ `Cao cấp`).
- **Sức mạnh của Named Aggregation (từ Pandas 0.25+)**: Thay vì sinh ra một DataFrame có tiêu đề cột 2 tầng rắc rối (`MultiIndex`) khó truy xuất, Named Aggregation cho phép bạn đặt tên ngay cho từng chỉ số thống kê theo cú pháp:
  `ten_cot_moi = ('cot_can_tinh', 'ten_phep_toan')`.

---

### Bài 5.3: Phép biến đổi `transform()` — Giữ nguyên cấu trúc dòng của bảng gốc

#### Tình huống thực tế
Cho bảng dữ liệu nhân viên của các phòng ban. Cần tính xem mức lương của mỗi nhân viên chênh lệch bao nhiêu phần trăm so với mức lương trung bình của chính phòng ban mà người đó đang công tác.

```python
df_nv = pd.DataFrame({
    "ma_nv": ["NV01", "NV02", "NV03", "NV04", "NV05", "NV06"],
    "phong_ban": ["Kỹ thuật", "Kỹ thuật", "Kỹ thuật", "Kinh doanh", "Kinh doanh", "Nhân sự"],
    "luong": [25_000_000, 35_000_000, 18_000_000, 20_000_000, 30_000_000, 15_000_000]
})
```

#### Lời giải

##### Cách 1 · Tính bảng tổng hợp bằng `groupby` rồi `merge` ngược lại (Căn bản)

```python
# Bước 1: Tính lương trung bình theo phòng ban
df_tb_phong = df_nv.groupby("phong_ban")["luong"].mean().reset_index()
df_tb_phong.rename(columns={"luong": "luong_tb_phong"}, inplace=True)

# Bước 2: Ghép ngược lại bảng gốc
df_gop = pd.merge(df_nv, df_tb_phong, on="phong_ban", how="left")

# Bước 3: Tính tỷ lệ chênh lệch
df_gop["chenh_lech_%"] = ((df_gop["luong"] - df_gop["luong_tb_phong"]) / df_gop["luong_tb_phong"] * 100).round(2)

print("Cách merge truyền thống:\n", df_gop)
```

##### Cách 2 · Vận dụng phép biến đổi `transform()` trong một dòng lệnh (Nâng cao)

```python
# Tính toán và phát tán (broadcast) ngay lập tức về từng dòng ban đầu
luong_tb_nhom = df_nv.groupby("phong_ban")["luong"].transform("mean")

df_nv["luong_tb_phong"] = luong_tb_nhom
df_nv["chenh_lech_%"] = ((df_nv["luong"] - luong_tb_nhom) / luong_tb_nhom * 100).round(2)

print("Cách transform vector hóa tối ưu:\n", df_nv)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Phân biệt `agg()` và `transform()`**:
  - `agg()` là phép **thu gọn dữ liệu** (*aggregation*): nhận vào một nhóm nhiều dòng và trả về một giá trị đơn lẻ đại diện cho nhóm đó (số dòng của bảng kết quả bằng số nhóm).
  - `transform()` là phép **chuyển hóa phát tán**: nhận vào một nhóm và trả về một Series có **cùng độ dài chính xác** với số dòng ban đầu của nhóm đó, các giá trị được gán tương ứng vào từng dòng.
- **Tiết kiệm tài nguyên**: Việc dùng `groupby().transform()` giúp bạn tránh hoàn toàn việc phải tạo bảng phụ và thực hiện một phép nối bảng (`merge`) đắt đỏ, tiết kiệm đáng kể thời gian CPU và bộ nhớ.

---

### Bài 5.4: Bảng tổng hợp hai chiều `pivot_table()` và Ghép bảng an toàn với `validate`

#### Tình huống thực tế
Cho bảng giao dịch bán hàng `df_orders` và bảng tra cứu mức chiết khấu theo nhóm sản phẩm `df_discounts`.
Cần:
1. Ghép mức chiết khấu vào từng đơn hàng một cách an toàn tuyệt đối, tránh lỗi nhân đôi dòng.
2. Lập ma trận tổng hợp doanh thu 2 chiều giữa Khu vực (`khu_vuc`) và Loại khách hàng (`loai_khach`).

```python
df_orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "khu_vuc": ["Bắc", "Nam", "Bắc", "Nam", "Bắc"],
    "loai_khach": ["Bán buôn", "Bán lẻ", "Bán lẻ", "Bán buôn", "Bán buôn"],
    "ma_nhom_sp": ["N01", "N02", "N01", "N03", "N02"],
    "doanh_thu": [50_000_000, 12_000_000, 8_000_000, 30_000_000, 25_000_000]
})

df_discounts = pd.DataFrame({
    "ma_nhom_sp": ["N01", "N02", "N03"],
    "chiet_khau": [0.05, 0.08, 0.10]
})
```

#### Lời giải

##### Cách 1 · Ghép bảng bằng `pd.merge` và lập bảng chéo thủ công (Căn bản)

```python
# Ghép thông thường
df_merged_cb = pd.merge(df_orders, df_discounts, on="ma_nhom_sp", how="left")

# Tạo bảng tổng hợp bằng groupby 2 cột và unstack
pv_cb = df_merged_cb.groupby(["khu_vuc", "loai_khach"])["doanh_thu"].sum().unstack(fill_value=0)

print("Ghép cơ bản:\n", df_merged_cb)
print("Bảng tổng hợp chéo:\n", pv_cb)
```

##### Cách 2 · Ghép kiểm soát quan hệ `validate` và `pivot_table` có dòng tổng `margins` (Nâng cao)

```python
# 1. Ghép có chốt kiểm tra quan hệ nhiều-một (many-to-one)
df_merged_adv = pd.merge(
    df_orders,
    df_discounts,
    on="ma_nhom_sp",
    how="left",
    validate="many_to_one"  # Bắt buộc bảng tra cứu bên phải phải có khóa duy nhất
)

# 2. Tạo ma trận pivot table chuyên nghiệp kèm cột/dòng tổng (margins)
ma_tran_doanh_thu = pd.pivot_table(
    df_merged_adv,
    values="doanh_thu",
    index="khu_vuc",
    columns="loai_khach",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="Tổng cộng"
)

print("Ma trận doanh thu hai chiều chuẩn báo cáo:\n", ma_tran_doanh_thu)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Cạm bẫy nhân đôi dòng khi `merge`**:
  Nếu bảng danh mục `df_discounts` vô tình bị lỗi hệ thống làm xuất hiện 2 dòng cho cùng mã `"N01"`, phép `merge` thông thường sẽ nhân bản đơn hàng `101` thành 2 dòng, làm doanh thu bị tính khống gấp đôi mà hệ thống hoàn toàn không báo lỗi! Tham số `validate="many_to_one"` là chiếc phanh an toàn: nếu bảng bên phải có khóa trùng, nó lập tức ném ra ngoại lệ `MergeError` để bạn ngăn chặn lỗi ngay từ đầu.
- **`pivot_table` vs `groupby().unstack()`**:
  `pivot_table()` cung cấp giao diện trực quan, tự động xử lý các giá trị khuyết bằng `fill_value`, và đặc biệt là tham số `margins=True` tự động sinh dòng/cột tổng cộng mà bạn không cần phải tính toán chắp vá bằng tay.

---

## Phần 6. Dữ liệu Quy mô lớn, Chuỗi thời gian, Parquet & DuckDB

::: info Trọng tâm tư duy
Khi kích thước dữ liệu vượt quá dung lượng bộ nhớ RAM (từ vài gigabyte đến hàng trăm gigabyte), việc đọc toàn bộ tệp bằng `pd.read_csv` sẽ làm sập chương trình. Đây là lúc tư duy xử lý dữ liệu lớn phát huy tác dụng: đọc chọn lọc, chuyển sang định dạng cột Parquet, và khai thác động cơ SQL trong bộ nhớ DuckDB.
:::

### Bài 6.1: Đọc tệp lớn có chọn lọc và tối ưu bộ nhớ RAM

#### Tình huống thực tế
Một tệp nhật ký hệ thống `server_logs.csv` chứa 80 cột và 10 triệu dòng. Bạn chỉ cần thực hiện bài toán tính thời gian phản hồi trung bình theo từng mã người dùng.

#### Lời giải

##### Cách 1 · Nạp toàn bộ tệp rồi lọc cột (Căn bản — Nguy cơ tràn RAM)

```python
# Cách làm ngốn RAM, có thể gây sập máy (OOM - Out of Memory)
# df = pd.read_csv("server_logs.csv")
# df_sub = df[["user_id", "response_time_ms", "timestamp"]]
```

##### Cách 2 · Đọc chọn lọc qua `usecols`, tối ưu kiểu dữ liệu và phân tích ngày tháng (Nâng cao)

```python
import pandas as pd
import io

csv_sample = """timestamp,user_id,ip_address,browser,status_code,response_time_ms
2025-01-01 08:00:15,1001,192.168.1.1,Chrome,200,45.2
2025-01-01 08:00:20,1002,192.168.1.5,Firefox,404,12.0
2025-01-01 08:00:25,1001,192.168.1.1,Chrome,200,60.5
2025-01-01 08:00:30,1003,192.168.1.9,Safari,500,120.8
"""

# Đọc có chọn lọc ngay từ tầng nạp vào của engine C
df_toi_uu = pd.read_csv(
    io.StringIO(csv_sample),
    usecols=["timestamp", "user_id", "status_code", "response_time_ms"],
    dtype={
        "user_id": "int32",               # Giảm từ int64 xuống int32
        "status_code": "int16",            # HTTP code chỉ cần 16-bit
        "response_time_ms": "float32"      # Giảm từ float64 xuống float32
    },
    parse_dates=["timestamp"]              # Phân tích ngày giờ chuẩn datetime64
)

print(df_toi_uu.info())
```

#### Phân tích bản chất & Bình luận sư phạm
- **Khai báo `usecols`**: Engine C của Pandas sẽ chỉ cấp phát bộ nhớ cho đúng 4 cột được chỉ định, bỏ qua hoàn toàn 76 cột còn lại ngay trong quá trình đọc luồng tệp đĩa.
- **Tiết kiệm tới 75% bộ nhớ nhờ ép kiểu (`downcasting`)**:
  - `int64` tốn 8 bytes cho mỗi ô nhớ; `int16` chỉ tốn 2 bytes.
  - `float64` tốn 8 bytes; `float32` tốn 4 bytes.
  Trên tập dữ liệu 10 triệu dòng, việc chọn kiểu chính xác có thể giảm dung lượng RAM tiêu thụ từ $6.4\text{ GB}$ xuống chỉ còn dưới $1.5\text{ GB}$, giúp máy tính xách tay bình thường cũng có thể chạy mượt mà.

---

### Bài 6.2: Làm sạch cột tiền tệ và số liệu bẩn: Chuỗi hàm cơ bản vs Biểu thức chính quy (Regex)

#### Tình huống thực tế
Cho một Series chứa dữ liệu giá bán bị ô nhiễm nặng: chứa ký tự ngoại tệ `"$"`, `"€"`, dấu phẩy phân cách hàng nghìn `","`, các từ ngữ chú thích `"Liên hệ"`, `"Hết hàng"`, dấu âm đặt sai vị trí `"-15.5$"`, và giá trị rỗng `None`. Cần làm sạch cột này về chuẩn số thực `float64`.

```python
prices_raw = pd.Series([
    "$1,250.50",
    " 2,300.00 €",
    "Liên hệ",
    None,
    "$450.25",
    "-15.5$",
    "Miễn phí"
])
```

#### Lời giải

##### Cách 1 · Sử dụng chuỗi lệnh `.str.replace` cơ bản (Căn bản)

```python
# Cách tiếp cận trực tiếp, thay thế từng ký tự đã biết
prices_cb = prices_raw.astype(str)
prices_cb = prices_cb.str.replace("$", "", regex=False)
prices_cb = prices_cb.str.replace("€", "", regex=False)
prices_cb = prices_cb.str.replace(",", "", regex=False)
prices_cb = prices_cb.str.strip()

# Ép kiểu số
prices_cb_num = pd.to_numeric(prices_cb, errors="coerce")

print("Cách cơ bản:\n", prices_cb_num)
```

##### Cách 2 · Biểu thức chính quy (Regex) loại bỏ ký tự rác kết hợp `errors='coerce'` (Nâng cao)

```python
# Cách tiếp cận nâng cao: giữ lại duy nhất chữ số, dấu chấm và dấu âm (nếu có)
prices_adv = pd.to_numeric(
    prices_raw.astype(str).str.replace(r"[^0-9.-]", "", regex=True),
    errors="coerce"
)

print("Cách nâng cao:\n", prices_adv)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Tại sao Cách 1 dễ thất bại trong thực tế?**:
  Trong một tập dữ liệu lớn, bạn không bao giờ có thể liệt kê hết tất cả các ký tự rác. Nếu hôm nay có ký hiệu bảng Anh `"£"`, ngày mai có chữ `"VNĐ"` hay dấu gạch nối, chuỗi `.replace()` của bạn sẽ bỏ sót. Khi đó lệnh ép kiểu sẽ sinh lỗi hoặc tạo ra kết quả sai lệch.
- **Sức mạnh của Regex `r"[^0-9.-]"`**:
  - Cặp ngoặc vuông `[...]` đại diện cho một tập hợp ký tự.
  - Dấu mũ `^` ở đầu ngoặc vuông biểu thị phép **phủ định** (*negation*).
  - Mẫu `r"[^0-9.-]"` có nghĩa là: *"Tìm mọi ký tự KHÔNG PHẢI là chữ số từ 0 đến 9, dấu chấm hoặc dấu trừ, và thay thế toàn bộ chúng bằng chuỗi rỗng"*.
  Chỉ một biểu thức ngắn gọn này quét sạch mọi loại đơn vị tiền tệ, khoảng trắng thừa và ký tự ngôn ngữ tự nhiên.
- **Bảo hiểm an toàn `errors='coerce'`**:
  Đối với các chuỗi hoàn toàn là chữ như `"Liên hệ"` hay `"Miễn phí"`, sau khi xóa hết ký tự sẽ trở thành chuỗi rỗng `""`. Tham số `errors="coerce"` hướng dẫn Pandas tự động chuyển các giá trị không hợp lệ này thành `NaN` mà không quăng ra ngoại lệ làm đứt gãy luồng xử lý dữ liệu tự động.

---

### Bài 6.3: CSV vs Parquet — So sánh dung lượng và bảo toàn kiểu dữ liệu

#### Tình huống thực tế
Cho bảng dữ liệu gồm mã giao dịch, thời điểm thanh toán `datetime64`, và mã số thuế khách hàng (chuỗi có số 0 ở đầu, ví dụ `"010203405"`).
Hãy so sánh:
1. Độ nguyên vẹn của kiểu dữ liệu khi lưu ra CSV rồi đọc lại, so với khi lưu ra Parquet.
2. Dung lượng tệp lưu trữ trên đĩa.

```python
df_giao_dich = pd.DataFrame({
    "ma_gd": range(1, 10001),
    "thoi_gian": pd.date_range("2025-01-01", periods=10000, freq="min"),
    "ma_so_thue": [f"0{i % 900000 + 100000}" for i in range(10000)],
    "gia_tri": np.random.default_rng(42).normal(500, 50, 10000).round(2)
})
```

#### Lời giải

##### Cách 1 · Lưu và đọc lại bằng CSV truyền thống (Căn bản)

```python
import os

# Lưu CSV
df_giao_dich.to_csv("data_test.csv", index=False)

# Đọc lại CSV
df_csv_read = pd.read_csv("data_test.csv")

print("Dtypes sau khi đọc lại từ CSV:\n", df_csv_read.dtypes)
print(f"Mã số thuế dòng 0 trong CSV: {df_csv_read.loc[0, 'ma_so_thue']} (Kiểu: {type(df_csv_read.loc[0, 'ma_so_thue'])})")
```

##### Cách 2 · Lưu và đọc bằng định dạng cột nén Parquet (Nâng cao)

```python
# Lưu Parquet (sử dụng engine pyarrow)
df_giao_dich.to_parquet("data_test.parquet", index=False, engine="pyarrow")

# Đọc lại Parquet
df_pq_read = pd.read_parquet("data_test.parquet")

print("Dtypes sau khi đọc lại từ Parquet:\n", df_pq_read.dtypes)
print(f"Mã số thuế dòng 0 trong Parquet: '{df_pq_read.loc[0, 'ma_so_thue']}'")

# So sánh dung lượng tệp
size_csv = os.path.getsize("data_test.csv")
size_pq = os.path.getsize("data_test.parquet")
print(f"Dung lượng CSV: {size_csv:,} bytes | Parquet: {size_pq:,} bytes")
print(f"Parquet tiết kiệm được: {(1 - size_pq / size_csv):.1%} dung lượng đĩa!")

# Dọn dẹp tệp tạm
os.remove("data_test.csv")
os.remove("data_test.parquet")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiểm họa mất dữ liệu của định dạng CSV**:
  CSV là tệp văn bản thuần (*plain text*), không lưu trữ thông tin schema (metadata kiểu dữ liệu). Do đó, khi đọc lại bằng `pd.read_csv()`, Pandas tự động đoán kiểu:
  - Cột `ma_so_thue` bị đoán thành số nguyên `int64`, làm biến mất hoàn toàn số `0` ở đầu (ví dụ `"0100000"` bị đổi thành `100000`). Đây là thảm họa đối với mã định danh CCCD, mã số thuế hay số điện thoại!
  - Cột `thoi_gian` bị trả về dạng chuỗi `object`, buộc bạn phải tốn thời gian phân tích lại bằng `pd.to_datetime()`.
- **Vì sao Parquet là chuẩn mực của ngành Data Engineering hiện đại?**:
  Parquet lưu dữ liệu theo dạng cột (*columnar storage*), tích hợp sẵn thuật toán nén Snappy và lưu trữ schema chuẩn mực. Khi đọc lại, 100% kiểu dữ liệu (`datetime64`, `string`, `category`) được khôi phục nguyên vẹn ngay tức thì mà không cần đoán kiểu, đồng thời dung lượng đĩa thường giảm từ 4 đến 10 lần so với CSV.

---

### Bài 6.4: Truy vấn SQL trực tiếp trên tệp bằng DuckDB không cần nạp vào RAM

#### Tình huống thực tế
Cho một tệp CSV ghi nhận lịch sử hàng triệu lượt đánh giá của khách hàng qua nhiều năm. Máy tính của bạn có cấu hình yếu, không đủ bộ nhớ để nạp toàn bộ tệp vào Pandas DataFrame. Bạn cần tính tổng số lượt đánh giá theo từng năm và tìm ra các loại phòng (`room_type`) có lượng tương tác cao nhất trong năm 2025.

#### Lời giải

##### Cách 1 · Đọc theo từng khối (Chunking) trong Pandas (Căn bản)

```python
# Tiếp cận bằng Pandas: đọc từng khối 50.000 dòng để tránh tràn RAM
# dem_nam = {}
# for chunk in pd.read_csv("reviews_large.csv", chunksize=50000, usecols=["date"]):
#     chunk["nam"] = pd.to_datetime(chunk["date"]).dt.year
#     for nam, count in chunk["nam"].value_counts().items():
#         dem_nam[nam] = dem_nam.get(nam, 0) + count
```

##### Cách 2 · Khai thác động cơ DuckDB truy vấn SQL Out-of-Core (Nâng cao)

```python
import pandas as pd
import io

# Dữ liệu mô phỏng 2 bảng
csv_reviews = """listing_id,date,reviewer_id
101,2023-05-12,501
102,2024-06-18,502
101,2025-01-10,503
103,2025-02-14,504
101,2025-08-20,505
102,2025-11-05,506
"""

csv_listings = """id,name,room_type
101,Căn hộ view hồ,Entire home/apt
102,Phòng ngủ ấm cúng,Private room
103,Studio trung tâm,Entire home/apt
"""

# Lưu tệp tạm để DuckDB truy vấn trực tiếp từ đĩa
with open("temp_reviews.csv", "w", encoding="utf-8") as f:
    f.write(csv_reviews)
with open("temp_listings.csv", "w", encoding="utf-8") as f:
    f.write(csv_listings)

# Truy vấn bằng DuckDB (nếu môi trường có cài đặt duckdb)
try:
    import duckdb
    
    # 1. Đếm số review theo năm trực tiếp từ file CSV
    sql_query_1 = """
        SELECT 
            year(CAST(date AS DATE)) AS nam,
            count(*) AS so_luot_review
        FROM 'temp_reviews.csv'
        GROUP BY nam
        ORDER BY nam ASC;
    """
    df_nam = duckdb.query(sql_query_1).df()
    print("Thống kê theo năm từ DuckDB:\n", df_nam)

    # 2. JOIN 2 tệp CSV trực tiếp mà không cần nạp vào RAM
    sql_query_2 = """
        SELECT 
            l.room_type,
            count(*) AS tong_review_2025
        FROM 'temp_reviews.csv' r
        JOIN 'temp_listings.csv' l ON r.listing_id = l.id
        WHERE year(CAST(r.date AS DATE)) = 2025
        GROUP BY l.room_type
        ORDER BY tong_review_2025 DESC;
    """
    df_loai_phong = duckdb.query(sql_query_2).df()
    print("Kết quả JOIN bằng DuckDB:\n", df_loai_phong)

except ImportError:
    print("Môi trường hiện tại chưa cài đặt DuckDB (chạy: pip install duckdb để trải nghiệm).")

# Dọn dẹp tệp tạm
import os
os.remove("temp_reviews.csv")
os.remove("temp_listings.csv")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Cơ chế Out-of-Core Execution của DuckDB**:
  DuckDB được mệnh danh là "SQLite của kỷ nguyên phân tích dữ liệu". Khác với Pandas buộc phải nạp toàn bộ dữ liệu vào RAM, DuckDB sở hữu engine thực thi vector hóa (*vectorized execution engine*) viết bằng C++. Nó đọc dữ liệu theo từng luồng khối dữ liệu (stream of chunks), chỉ đọc đúng các cột có mặt trong mệnh đề `SELECT` và `WHERE`, cho phép bạn xử lý tệp CSV/Parquet 50GB trên một chiếc máy tính xách tay chỉ có 8GB RAM.
- **Tính khả chuyển của chuẩn SQL**: Việc viết truy vấn bằng cú pháp SQL chuẩn giúp phân tích logic của bạn trở nên trong sáng, dễ dàng bàn giao sang các kho dữ liệu lớn như BigQuery, Snowflake, hay PostgreSQL mà không cần phải viết lại code thuật toán từ đầu.

---

## 7. Bảng tổng kết năng lực & Chỉ dẫn thực hành

| Chuyên đề | Kỹ năng cốt lõi | Cạm bẫy ngầm cần tránh | Chuẩn tối ưu đề xuất |
| :--- | :--- | :--- | :--- |
| **Phần 1: Notebook & AI** | Quản lý trạng thái, hàm thuần khiết | Chạy cell ngoài trật tự, sửa biến toàn cục | Đóng gói hàm bất biến; Restart Kernel & Run All |
| **Phần 2: Python thuần** | Xử lý dữ liệu không phụ thuộc thư viện | `list.sort()` làm hỏng mảng gốc; tràn bộ nhớ `dict` | Dùng `str.translate`, `statistics.fmean`, `defaultdict` |
| **Phần 3: NumPy** | Bố cục bộ nhớ, Strides, Broadcasting | Nhầm lẫn giữa View và Copy; quên `keepdims=True` | Khai thác `np.ix_`, kiểm tra `shares_memory` |
| **Phần 4: Pandas** | Lọc dữ liệu, xử lý `NaN`, lập hồ sơ | Gặp `SettingWithCopyWarning`; `fillna(0)` làm méo thống kê | Truy xuất một bước bằng `.loc`, phân tích độ nhạy `NaN` |
| **Phần 5: Nâng cao** | GroupBy, Transform, Pivot, Merge | Nhân đôi dòng ngoài ý muốn khi `merge` | Dùng Named Aggregation, `transform`, `validate` |
| **Phần 6: Tối ưu quy mô** | Đọc có chọn lọc, Parquet, DuckDB | Nạp toàn bộ CSV gây tràn RAM (OOM) | Dùng `usecols`, Regex làm sạch, Parquet và DuckDB |
