---
course: xu-ly-du-lieu
title: "Hệ thống Bài tập Thực hành Lập trình Xử lý Dữ liệu"
description: "Tuyển tập bài tập thực hành từ căn bản đến nâng cao: Python thuần, NumPy vectorization, Pandas thao tác bảng, làm sạch chuỗi, dữ liệu thời gian, Parquet và DuckDB."
---

# Hệ thống Bài tập Thực hành Lập trình Xử lý Dữ liệu

Một người kỹ sư dữ liệu giỏi không chỉ biết viết code để chương trình chạy ra kết quả, mà còn thấu hiểu tường tận cơ chế vận hành bên dưới: Từ việc bố cục bộ nhớ của mảng được xếp đặt ra sao, tại sao phép tính này sinh ra bản sao ngầm làm cạn kiệt RAM, cho đến cách viết biểu thức chính quy sao cho vừa an toàn, vừa triệt để quét sạch dữ liệu bẩn.

Mỗi bài tập dưới đây được thiết kế như một tình huống thực chiến độc lập. Với mỗi bài toán, bạn sẽ được tiếp cận theo hai tầng tư duy:
- **Cách 1 · Căn bản & Trực quan**: Tiếp cận tuần tự, tường minh từng bước, ưu tiên tính dễ đọc cho người mới bắt đầu.
- **Cách 2 · Nâng cao & Tối ưu**: Vận dụng kỹ thuật vector hóa, biểu thức chính quy (Regex), cơ chế chuỗi phương thức (method chaining) và tối ưu hóa tài nguyên phần cứng.
- **Phân tích bản chất & Bình luận chuyên sâu**: Mổ xẻ cặn kẽ sự đánh đổi (trade-offs) về hiệu năng, bộ nhớ và các cạm bẫy ngầm (*gotchas & pitfalls*) thường gặp trong sản xuất.

---

## Phần 1. Trạng thái Kernel, Dòng tính toán & Tư duy kiểm chứng

::: info Trọng tâm tư duy
Môi trường Notebook (Jupyter/Colab) mang tính tương tác cao nhưng lại tiềm ẩn hiểm họa lớn nhất: **Trạng thái toàn cục (global state) bị biến đổi ngoài trật tự (out-of-order execution)**. Một bài phân tích đáng tin cậy phải được thiết kế dưới dạng các hàm thuần khiết (*pure functions*), có khả năng tái lập hoàn toàn từ đầu đến cuối (*Restart Kernel & Run All*).
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
Một chuỗi khách sạn lưu dữ liệu phòng ở dạng tệp CSV. Cột giá phòng (`price`) chứa dữ liệu hỗn hợp: Ký hiệu tiền tệ `"$"`, dấu phẩy phân tách hàng nghìn `","`, khoảng trắng ngẫu nhiên và một số dòng ghi chữ `"Miễn phí"` hoặc rỗng. Cần làm sạch cột này về số thực `float`.

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
- **Strides là gì?**: Khái niệm `strides` là một tuple quy định số byte mà CPU cần nhảy qua trong bộ nhớ để bước sang hàng tiếp theo hoặc cột tiếp theo. Với `int64` (8 bytes/ô):
  - Bước sang cột kế bên tốn $8$ byte.
  - Bước sang hàng kế bên (gồm 3 cột) tốn $3 \times 8 = 24$ byte. Do đó, `strides = (24, 8)`.
- **Khoảng cách byte offset**:
  $$
  \text{offset} = 3 \times 24 + 1 \times 8 = 72 + 8 = 80 \text{ bytes}.
  $$
- Khi đổi sang `int32` (4 bytes/ô), `strides` giảm một nửa thành `(12, 4)`, tổng dung lượng mảng giảm từ 96 byte xuống 48 byte, và offset tới vị trí $(3, 1)$ giảm xuống đúng 40 byte. Nắm vững điều này giúp bạn hiểu tại sao chọn đúng kiểu số nhỏ nhất có thể lại giúp tiết kiệm hàng gigabyte RAM trong các dự án Big Data.

---

### Bài 3.2: Lát cắt (View) vs Bản sao (Copy): Bẫy biến đổi dữ liệu ngầm

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
- **Vì sao `M[[0, 2], [1, 3]]` không trả về ma trận $2 \times 2$?**: Đây là một trong những hiểu lầm lớn nhất của người mới học NumPy. Khi bạn truyền hai danh sách chỉ mục có cùng kích thước, NumPy hiểu rằng bạn muốn lấy các phần tử theo từng cặp tọa độ tương ứng: Ô $(0, 1)$ và ô $(2, 3)$ $\implies$ kết quả trả về là một mảng 1 chiều có shape `(2,)`.
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
  - Hai trục tương thích nếu: Kích thước của chúng bằng nhau, hoặc một trong hai kích thước bằng 1.
- **Tầm quan trọng sống còn của `keepdims=True`**:
  - Nếu bạn chỉ gọi `gia_phong.mean(axis=1)`, kết quả trả về có shape là `(3,)` (mảng 1 chiều).
  - Khi lấy `(3, 4) - (3,)`, NumPy sẽ căn lề trục cuối cùng: Trục $4$ so với $3$ $\implies$ **Báo lỗi `ValueError: operands could not be broadcast together`**!
  - Khi có `keepdims=True`, shape là `(3, 1)`. NumPy so khớp: Trục 1 có $1$ tự nhân bản thành $4$, đồng thời trục 0 có $3$ khớp với $3$. Phép toán diễn ra hoàn hảo ở tốc độ C tối đa.

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
  - `.loc` làm việc dựa trên **Nhãn (Labels)**: Cú pháp `df.loc['a':'c']` sẽ lấy bao gồm cả điểm cuối `'c'`.
  - `.iloc` làm việc dựa trên **Vị trí chỉ số nguyên (Integer positions)**: Cú pháp `df.iloc[0:2]` chỉ lấy chỉ số 0 và 1 (loại trừ biên phải, giống quy tắc slice chuẩn của Python).

---

### Bài 4.2: Xóa sổ cảnh báo `SettingWithCopyWarning` khi cập nhật dữ liệu

#### Tình huống thực tế
Bạn muốn áp dụng chương trình khuyến mãi: Đối với các khách hàng tại `"Hà Nội"`, tặng thêm $500{,}000$ đồng vào tài khoản điểm thưởng (`diem_thuong`). Khi chạy code dưới đây:

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
- **Quy tắc ứng xử với `NaN`**: Trong thực tế, chỉ điền số 0 khi giá trị thiếu mang bản chất là "không phát sinh sự kiện" (ví dụ: Số lần vi phạm luật, số đánh giá khiếu nại). Với các đại lượng đo lường vật lý, giá tiền, hay mức độ hài lòng, giá trị thiếu mang ý nghĩa là "chưa thu thập được thông tin", khi đó, giữ nguyên `NaN` hoặc phân tích độ nhạy (*sensitivity analysis*) là hướng đi chuẩn mực nhất.

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
2. Thống kê theo từng phân khúc: Số lượng khách, tổng doanh thu, doanh thu trung bình và điểm hài lòng lớn nhất.

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

### Bài 5.3: Phép biến đổi `transform()`: Giữ nguyên cấu trúc dòng của bảng gốc

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
  - `agg()` là phép **thu gọn dữ liệu** (*aggregation*): Nhận vào một nhóm nhiều dòng và trả về một giá trị đơn lẻ đại diện cho nhóm đó (số dòng của bảng kết quả bằng số nhóm).
  - `transform()` là phép **chuyển hóa phát tán**: Nhận vào một nhóm và trả về một Series có **cùng độ dài chính xác** với số dòng ban đầu của nhóm đó, các giá trị được gán tương ứng vào từng dòng.
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
  Nếu bảng danh mục `df_discounts` vô tình bị lỗi hệ thống làm xuất hiện 2 dòng cho cùng mã `"N01"`, phép `merge` thông thường sẽ nhân bản đơn hàng `101` thành 2 dòng, làm doanh thu bị tính khống gấp đôi mà hệ thống hoàn toàn không báo lỗi! Tham số `validate="many_to_one"` là chiếc phanh an toàn: Nếu bảng bên phải có khóa trùng, nó lập tức ném ra ngoại lệ `MergeError` để bạn ngăn chặn lỗi ngay từ đầu.
- **`pivot_table` vs `groupby().unstack()`**:
  `pivot_table()` cung cấp giao diện trực quan, tự động xử lý các giá trị khuyết bằng `fill_value`, và đặc biệt là tham số `margins=True` tự động sinh dòng/cột tổng cộng mà bạn không cần phải tính toán chắp vá bằng tay.

---

## Phần 6. Dữ liệu Quy mô lớn, Chuỗi thời gian, Parquet & DuckDB

::: info Trọng tâm tư duy
Khi kích thước dữ liệu vượt quá dung lượng bộ nhớ RAM (từ vài gigabyte đến hàng trăm gigabyte), việc đọc toàn bộ tệp bằng `pd.read_csv` sẽ làm sập chương trình. Đây là lúc tư duy xử lý dữ liệu lớn phát huy tác dụng: Đọc chọn lọc, chuyển sang định dạng cột Parquet, và khai thác động cơ SQL trong bộ nhớ DuckDB.
:::

### Bài 6.1: Đọc tệp lớn có chọn lọc và tối ưu bộ nhớ RAM

#### Tình huống thực tế
Một tệp nhật ký hệ thống `server_logs.csv` chứa 80 cột và 10 triệu dòng. Bạn chỉ cần thực hiện bài toán tính thời gian phản hồi trung bình theo từng mã người dùng.

#### Lời giải

##### Cách 1 · Nạp toàn bộ tệp rồi lọc cột (Căn bản: Nguy cơ tràn RAM)

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
  - `int64` tốn 8 bytes cho mỗi ô nhớ, trong khi `int16` chỉ tốn 2 bytes.
  - `float64` tốn 8 bytes, trong khi `float32` chỉ tốn 4 bytes.
  Trên tập dữ liệu 10 triệu dòng, việc chọn kiểu chính xác có thể giảm dung lượng RAM tiêu thụ từ $6.4\text{ GB}$ xuống chỉ còn dưới $1.5\text{ GB}$, giúp máy tính xách tay bình thường cũng có thể chạy mượt mà.

---

### Bài 6.2: Làm sạch cột tiền tệ và số liệu bẩn: Chuỗi hàm cơ bản vs Biểu thức chính quy (Regex)

#### Tình huống thực tế
Cho một Series chứa dữ liệu giá bán bị ô nhiễm nặng: Chứa ký tự ngoại tệ `"$"`, `"€"`, dấu phẩy phân cách hàng nghìn `","`, các từ ngữ chú thích `"Liên hệ"`, `"Hết hàng"`, dấu âm đặt sai vị trí `"-15.5$"`, và giá trị rỗng `None`. Cần làm sạch cột này về chuẩn số thực `float64`.

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

### Bài 6.3: CSV vs Parquet: So sánh dung lượng và bảo toàn kiểu dữ liệu

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

## Phần 7. Xử lý Dữ liệu Chuỗi & Biểu thức Chính quy (Regex)

::: info Trọng tâm tư duy
Dữ liệu văn bản trong thực tế luôn chứa đầy rác: Khoảng trắng thừa, thẻ HTML, ký tự đặc biệt, định dạng số điện thoại hay email hỗn tạp. Việc thành thạo **Biểu thức chính quy (Regex)** kết hợp các phương thức chuỗi vector hóa của Pandas (`.str`) là chìa khóa để trích xuất tri thức chuẩn xác từ dữ liệu phi cấu trúc.
:::

### Bài 7.1: Làm sạch văn bản HTML và chuẩn hóa khoảng trắng

#### Tình huống thực tế
Một trang tin bất động sản thu thập dữ liệu mô tả căn hộ từ web scraping. Cột `mo_ta` bị lẫn các thẻ HTML (`<p>`, `<b>`, `<br/>`), các ký tự thực thể HTML (`&amp;`, `&quot;`), và khoảng trắng ngắt quãng hỗn độn (`\n`, `\t`, nhiều dấu cách liên tiếp). Cần làm sạch cột này thành văn bản thuần sạch sẽ.

```python
import pandas as pd

df_bds = pd.DataFrame({
    "ma_tin": ["BDS01", "BDS02", "BDS03"],
    "mo_ta": [
        "<p>Căn hộ <b>2 phòng ngủ</b> view hồ Tây.<br/>Giá &amp; chính sách cực tốt!   </p>",
        "<div>Nhà phố &quot;mặt tiền&quot;\n\tkinh doanh sầm uất.   Liên hệ ngay!</div>",
        "   Chính chủ   cần bán gấp trong tuần...   "
    ]
})
```

#### Lời giải

##### Cách 1 · Chuỗi hàm thay thế ký tự thủ công (Căn bản)

```python
mo_ta_sach = []
for van_ban in df_bds["mo_ta"]:
    # Thay thế từng thẻ HTML đã biết
    s = van_ban.replace("<p>", "").replace("</p>", "").replace("<b>", "").replace("</b>", "")
    s = s.replace("<br/>", " ").replace("<div>", "").replace("</div>", "")
    s = s.replace("&amp;", "&").replace("&quot;", '"')
    # Gom khoảng trắng bằng cách split rồi join lại
    s = " ".join(s.split())
    mo_ta_sach.append(s)

df_bds["mo_ta_sach_cb"] = mo_ta_sach
print("Cách làm thủ công:\n", df_bds[["ma_tin", "mo_ta_sach_cb"]])
```

##### Cách 2 · Biểu thức chính quy kết hợp `html.unescape` vector hóa (Nâng cao)

```python
import re
import html

def lam_sach_van_ban(s: str) -> str:
    if not isinstance(s, str):
        return ""
    # Bước 1: Giải mã toàn bộ HTML entities (&amp; -> &, &quot; -> ", v.v.)
    van_ban = html.unescape(s)
    # Bước 2: Xóa sạch mọi thẻ HTML bằng mẫu <[^>]+>
    van_ban = re.sub(r"<[^>]+>", " ", van_ban)
    # Bước 3: Thu gọn mọi chuỗi ký tự trắng liên tiếp (\n, \t, space) thành 1 dấu cách duy nhất
    van_ban = re.sub(r"\s+", " ", van_ban).strip()
    return van_ban

# Vector hóa qua .apply() hoặc .str.replace()
df_bds["mo_ta_chuan"] = df_bds["mo_ta"].apply(lam_sach_van_ban)
print("Cách nâng cao với Regex & html.unescape:\n", df_bds[["ma_tin", "mo_ta_chuan"]])
```

#### Phân tích bản chất & Bình luận sư phạm
- **Mẫu `<[^>]+>` hoạt động ra sao?**:
  Một sai lầm kinh điển của người mới học Regex là viết `<.*>` để tìm thẻ HTML. Do tính chất tham lam (*greedy*), `<.*>` sẽ nuốt chửng toàn bộ từ dấu `<` đầu tiên của `<p>` cho đến dấu `>` cuối cùng của `</p>`, xóa sạch cả nội dung văn bản bên trong! Mẫu `<[^>]+>` sử dụng lớp ký tự phủ định: Bắt đầu bằng `<`, theo sau bởi một hoặc nhiều ký tự **không phải là `>`**, rồi kết thúc bằng `>`. Nó khớp chính xác từng thẻ HTML đơn lẻ một cách an toàn tuyệt đối.
- **Thư viện chuẩn `html.unescape`**: Tuyệt đối không tự viết hàng chục lệnh `.replace("&amp;", "&")`. Thư viện `html` có sẵn của Python nắm giữ bảng tra cứu toàn bộ hàng nghìn mã HTML entities chuẩn W3C, xử lý triệt để cả các mã dạng số như `&#39;`.

---

### Bài 7.2: Trích xuất thông tin liên hệ đa trường bằng Capturing Groups

#### Tình huống thực tế
Cho đoạn văn bản rao vặt chứa số điện thoại liên hệ và địa chỉ email của người bán. Cần trích xuất số điện thoại (chấp nhận các định dạng phổ biến tại Việt Nam: `0912.345.678`, `0988 123 456`, `+84 901 234 567`) và địa chỉ email.

```python
tin_rao = pd.Series([
    "Căn hộ Ecohome, liên hệ chính chủ: 0912.345.678 hoặc email: contact@ecohome.vn để xem nhà.",
    "Bán gấp đất nền, hotline: +84 988 123 456 (gặp Tuấn), hòm thư: tuan.bds_hn@land-group.com.vn",
    "Cho thuê văn phòng trọn gói, liên lạc số 0901234567, không tiếp trung gian."
])
```

#### Lời giải

##### Cách 1 · Tìm kiếm tuần tự từng trường bằng biểu thức đơn giản (Căn bản)

```python
import re

danh_sach_sdt = []
danh_sach_email = []

for tin in tin_rao:
    # Tìm số điện thoại
    khop_sdt = re.search(r"(?:\+84|0)\d{2,3}[.\s]?\d{3}[.\s]?\d{3,4}", tin)
    sdt = khop_sdt.group(0) if khop_sdt else None
    
    # Tìm email
    khop_email = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", tin)
    email = khop_email.group(0) if khop_email else None
    
    danh_sach_sdt.append(sdt)
    danh_sach_email.append(email)

df_lien_he = pd.DataFrame({"sdt": danh_sach_sdt, "email": danh_sach_email})
print("Kết quả trích xuất tuần tự:\n", df_lien_he)
```

##### Cách 2 · Trích xuất bảng trực tiếp bằng Named Capturing Groups và `.str.extract` (Nâng cao)

```python
# Thiết lập các nhóm bắt có tên (Named Capturing Groups)
mau_sdt = r"(?P<sdt>(?:\+84\s?|0)\d{2,3}[.\s]?\d{3}[.\s]?\d{3,4})"
mau_email = r"(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"

# Kết hợp trích xuất trực tiếp ra DataFrame bằng Pandas
df_kq = pd.DataFrame({
    "sdt": tin_rao.str.extract(mau_sdt, expand=True)["sdt"],
    "email": tin_rao.str.extract(mau_email, expand=True)["email"]
})

# Chuẩn hóa số điện thoại: bỏ toàn bộ dấu chấm, dấu cách và đổi +84 thành 0
df_kq["sdt_chuan"] = df_kq["sdt"].str.replace(r"[.\s]", "", regex=True).str.replace(r"^\+84", "0", regex=True)

print("Kết quả trích xuất vector hóa và chuẩn hóa:\n", df_kq)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Non-capturing group `(?:...)`**: Khi bạn cần nhóm các ký tự lại để áp dụng toán tử hoặc (ví dụ `(?:\+84\s?|0)`), hãy dùng cú pháp `(?:...)` thay vì `(...)`. Cú pháp này báo cho động cơ Regex biết chỉ gom nhóm logic mà không lưu trữ vào bộ nhớ bắt giữ (*capturing buffer*), giúp tăng tốc độ tìm kiếm và tránh làm xáo trộn thứ tự các cột khi gọi `.str.extract()`.
- **Ranh giới từ `\b`**: Trong thực tế, hãy luôn cân nhắc thêm ranh giới từ `\b` vào đầu mẫu số điện thoại để tránh trường hợp số điện thoại bị khớp nhầm vào phần đuôi của một mã số tài khoản ngân hàng hay mã căn hộ kéo dài.

---

### Bài 7.3: Bẫy khớp tham lam (Greedy) vs Lười biếng (Lazy)

#### Tình huống thực tế
Cho chuỗi trích xuất bình luận của khách hàng chứa nhiều đoạn trích dẫn nằm trong dấu ngoặc kép:
`text = 'Khách nhận xét: "Phòng rất rộng" nhưng "vệ sinh quá bẩn" và "nhân viên thô lỗ".'`
Hãy trích xuất danh sách tất cả các cụm nhận xét độc lập nằm giữa các cặp dấu ngoặc kép.

#### Lời giải

##### Cách 1 · Lỗi kinh điển khi dùng toán tử tham lam `.*` (Căn bản: Kết quả sai)

```python
import re

text = 'Khách nhận xét: "Phòng rất rộng" nhưng "vệ sinh quá bẩn" và "nhân viên thô lỗ".'

# Dùng toán tử tham lam .* thông thường
sai = re.findall(r'"(.*)"', text)
print("Kết quả tham lam (SAI):\n", sai)
# Kết quả chỉ có đúng 1 phần tử duy nhất nuốt chửng cả câu:
# ['Phòng rất rộng" nhưng "vệ sinh quá bẩn" và "nhân viên thô lỗ']
```

##### Cách 2 · Sử dụng Regex lười biếng `.*?` hoặc lớp ký tự phủ định `"[^"]+"` (Nâng cao)

```python
# Cách 2a: Thêm dấu hỏi ? để biến thành khớp lười biếng (Lazy / Non-greedy)
dung_lazy = re.findall(r'"(.*?)"', text)
print("Cách 2a (Lazy .*?):\n", dung_lazy)

# Cách 2b: Dùng tập phủ định "[^"]+" (Tối ưu hiệu năng, không quay lui)
dung_negated = re.findall(r'"([^"]+)"', text)
print("Cách 2b (Phủ định [^\"]+):\n", dung_negated)

assert dung_lazy == dung_negated == ['Phòng rất rộng', 'vệ sinh quá bẩn', 'nhân viên thô lỗ']
```

#### Phân tích bản chất & Bình luận sư phạm
- **Cơ chế tham lam (Greedy Matching)**: Trong các biểu thức chính quy, các lượng từ `*`, `+` mặc định hoạt động theo cơ chế tham lam: Chúng cố gắng "nuốt" càng nhiều ký tự càng tốt cho đến tận cuối chuỗi, sau đó mới quay lui (*backtrack*) dần dần để tìm ký tự đóng `"`. Điều này giải thích tại sao `r'"(.*)"'` nuốt chửng từ dấu ngoặc kép đầu tiên đến dấu ngoặc kép cuối cùng.
- **Vì sao Cách 2b (`"[^"]+"`) tối ưu hơn Cách 2a (`".*?"`)?**:
  Khớp lười biếng `.*?` phải liên tục kiểm tra điều kiện dừng sau từng ký tự một, gây ra chi phí kiểm tra lặp lại rất lớn. Ngược lại, mẫu phủ định `[^"]+` thông báo dứt khoát cho máy trạng thái hữu hạn (NFA): *"Cứ đọc thẳng liên tục mọi ký tự cho đến khi chạm đúng dấu ngoặc kép tiếp theo thì dừng ngay"*. Nó không bao giờ phải quay lui (*zero backtracking*), tốc độ thực thi nhanh hơn từ 3 đến 10 lần trên các đoạn văn bản dài.

---

### Bài 7.4: Tách chuỗi và mã hóa tiện nghi đa giá trị (Multi-label One-Hot Encoding)

#### Tình huống thực tế
Cho bảng dữ liệu khách sạn, trong đó cột `amenities` chứa danh sách các tiện ích phòng dưới dạng chuỗi ngăn cách bởi dấu chấm phẩy. Cần chuyển đổi cột này thành ma trận nhị phân 0/1 (*One-Hot Encoding*) cho từng loại tiện ích để chuẩn bị dữ liệu đầu vào cho mô hình máy học.

```python
df_ks = pd.DataFrame({
    "hotel_id": ["H01", "H02", "H03"],
    "amenities": [
        "Wifi; Máy lạnh; Bể bơi; Ban công",
        "Wifi; Bãi đỗ xe",
        "Máy lạnh; Bể bơi; Bãi đỗ xe"
    ]
})
```

#### Lời giải

##### Cách 1 · Lặp thủ công và tạo từng cột bằng vòng lặp Python (Căn bản)

```python
# Bước 1: Tìm tất cả các loại tiện nghi phân biệt
tap_tien_nghi = set()
ds_tach = []
for chuoi in df_ks["amenities"]:
    cac_muc = [muc.strip() for muc in chuoi.split(";")]
    ds_tach.append(cac_muc)
    tap_tien_nghi.update(cac_muc)

# Bước 2: Tạo ma trận nhị phân thủ công
danh_sach_cot = sorted(tap_tien_nghi)
ma_tran = []
for cac_muc in ds_tach:
    dong = [1 if tn in cac_muc else 0 for tn in danh_sach_cot]
    ma_tran.append(dong)

df_encoded_cb = pd.concat([df_ks[["hotel_id"]], pd.DataFrame(ma_tran, columns=danh_sach_cot)], axis=1)
print("Cách mã hóa thủ công:\n", df_encoded_cb)
```

##### Cách 2 · Sử dụng `.str.get_dummies()` vector hóa trong một dòng lệnh (Nâng cao)

```python
# Tách và tạo ma trận One-Hot tự động ngay ở tầng C của Pandas
df_dummies = df_ks["amenities"].str.get_dummies(sep="; ")

# Ghép với cột ID ban đầu
df_encoded_adv = pd.concat([df_ks[["hotel_id"]], df_dummies], axis=1)

print("Cách get_dummies vector hóa chuyên nghiệp:\n", df_encoded_adv)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Sức mạnh của `.str.get_dummies()`**:
  Thay vì phải viết hai vòng lặp lồng nhau phức tạp để thu thập tập hợp duy nhất và gán giá trị, phương thức `.str.get_dummies(sep=...)` của Pandas thực hiện toàn bộ quy trình: Băm từ khóa, loại bỏ khoảng trắng theo dấu phân cách, và sinh ra một DataFrame nhị phân thưa tối ưu chỉ trong một thao tác duy nhất.
- **Lưu ý dấu phân cách**: Hãy chú ý dấu cách sau dấu chấm phẩy (`sep="; "`). Nếu chỉ viết `sep=";"`, các mục đứng sau sẽ bị dính khoảng trắng ở đầu (`" Máy lạnh"` thay vì `"Máy lạnh"`), dẫn đến việc sinh ra các cột bị trùng lặp giả tạo.

---

## Phần 8. Xử lý Dữ liệu Thời gian & Chuỗi Thời gian (Time Series)

::: info Trọng tâm tư duy
Thời gian là một chiều dữ liệu đặc thù: Nó vừa mang tính liên tục, vừa tuân theo các chu kỳ lịch không đều (tháng 28 đến 31 ngày, năm nhuận, chu kỳ tuần). Việc làm chủ `DatetimeIndex`, `resample()`, `rolling()` và phép dịch chuyển `shift()` là nền tảng để phân tích tăng trưởng và dự báo chuỗi thời gian.
:::

### Bài 8.1: Đổi kiểu ngày giờ an toàn và phân biệt `NaT` lỗi đọc với thiếu từ nguồn

#### Tình huống thực tế
Cho bảng ghi nhận thông tin đặt phòng gồm ngày nhận phòng (`check_in`) và ngày trả phòng (`check_out`). Cần:
1. Chuyển đổi hai cột sang kiểu `datetime64[ns]`.
2. Phân biệt rõ: Ô nào vốn bị để trống từ nguồn, và ô nào bị lỗi do người dùng nhập chuỗi sai định dạng (ví dụ `"2025/15/01"`).
3. Tính số đêm lưu trú hợp lệ (`so_dem = check_out - check_in`) và phát hiện các đơn hàng có logic phi lý (ngày trả phòng xảy ra trước ngày nhận phòng).

```python
df_booking = pd.DataFrame({
    "booking_id": ["B01", "B02", "B03", "B04", "B05"],
    "check_in": ["2025-01-10", "2025-01-15", "sai_dinh_dang", None, "2025-02-01"],
    "check_out": ["2025-01-14", "2025-01-12", "2025-01-20", "2025-01-25", "2025-02-05"]
})
```

#### Lời giải

##### Cách 1 · Lặp từng dòng với `datetime.strptime` và bắt lỗi `ValueError` (Căn bản)

```python
from datetime import datetime

so_dem_cb = []
trang_thai_cb = []

for _, row in df_booking.iterrows():
    cin_raw, cout_raw = row["check_in"], row["check_out"]
    if cin_raw is None or cout_raw is None:
        trang_thai_cb.append("Thiếu dữ liệu gốc")
        so_dem_cb.append(None)
        continue
    try:
        d_in = datetime.strptime(cin_raw, "%Y-%m-%d")
        d_out = datetime.strptime(cout_raw, "%Y-%m-%d")
        delta = (d_out - d_in).days
        if delta <= 0:
            trang_thai_cb.append("Phi lý (ngày về trước ngày đến)")
            so_dem_cb.append(delta)
        else:
            trang_thai_cb.append("Hợp lệ")
            so_dem_cb.append(delta)
    except ValueError:
        trang_thai_cb.append("Lỗi định dạng ngày")
        so_dem_cb.append(None)

df_booking["so_dem_cb"] = so_dem_cb
df_booking["trang_thai_cb"] = trang_thai_cb
print("Xử lý tuần tự thủ công:\n", df_booking)
```

##### Cách 2 · Vector hóa với `pd.to_datetime` kết hợp phân loại lỗi chuẩn mực (Nâng cao)

```python
# 1. Đánh dấu các ô vốn đã rỗng từ đầu nguồn
goc_cin_thieu = df_booking["check_in"].isna()

# 2. Ép kiểu an toàn với errors='coerce' (lỗi biến thành NaT)
df_booking["cin_dt"] = pd.to_datetime(df_booking["check_in"], format="%Y-%m-%d", errors="coerce")
df_booking["cout_dt"] = pd.to_datetime(df_booking["check_out"], format="%Y-%m-%d", errors="coerce")

# 3. Phân biệt chính xác: NaT mới sinh ra do lỗi format
df_booking["loi_dinh_dang_cin"] = df_booking["cin_dt"].isna() & ~goc_cin_thieu

# 4. Tính số đêm bằng phép trừ vector và trích xuất .dt.days
df_booking["so_dem"] = (df_booking["cout_dt"] - df_booking["cin_dt"]).dt.days

# 5. Kiểm tra tính bất biến nghiệp vụ: số đêm phải dương
df_booking["hop_le"] = df_booking["so_dem"] > 0

print("Xử lý vector hóa chuẩn kỹ sư dữ liệu:\n", df_booking[[
    "booking_id", "so_dem", "loi_dinh_dang_cin", "hop_le"
]])
```

#### Phân tích bản chất & Bình luận sư phạm
- **`NaT` (Not a Time) là gì?**: Trong Pandas, `NaT` là giá trị đặc biệt đại diện cho thời điểm khuyết thiếu (tương đương với `NaN` của kiểu số thực). `NaT` có thể tham gia vào các phép trừ vector: Kết quả trừ giữa một mốc ngày với `NaT` sẽ trả về `NaT` mà không làm sập chương trình.
- **Bẫy gom chung lỗi**: Người làm dữ liệu thiếu kinh nghiệm thường chỉ gọi `pd.to_datetime(errors='coerce')` rồi kết luận rằng mọi giá trị `NaT` đều là "khách hàng không nhập ngày". Hãy luôn ghi nhận số ô bị rỗng từ trước (`isna()`) để tách bạch rành mạch giữa *dữ liệu thiếu tự nhiên* và *dữ liệu bị lỗi trong quá trình thu thập/chuyển đổi*.

---

### Bài 8.2: Tổng hợp dữ liệu theo chu kỳ lịch (Resampling) và bẫy kỳ chụp ảnh cắt ngang

#### Tình huống thực tế
Cho bảng ghi nhận số lượt đánh giá của khách hàng từ đầu năm 2024 đến ngày 20/06/2025 (thời điểm trích xuất dữ liệu snapshot). Cần:
1. Tổng hợp số lượt đánh giá theo từng quý (`QE`).
2. Nhận diện và loại bỏ bẫy sai lệch do quý cuối cùng chưa kết thúc trọn vẹn (*Snapshot Truncation Bias*).

```python
# Tạo chuỗi thời gian mẫu với 500 đánh giá ngẫu nhiên
rng = np.random.default_rng(42)
ngay_ngau_nhien = pd.to_datetime("2024-01-01") + pd.to_timedelta(
    rng.integers(0, 536, size=500), unit="D"
)
df_rv = pd.DataFrame({"review_id": range(1, 501), "ngay": ngay_ngau_nhien}).sort_values("ngay")
```

#### Lời giải

##### Cách 1 · Trích xuất năm quý rồi GroupBy (Căn bản)

```python
df_cb = df_rv.copy()
df_cb["nam"] = df_cb["ngay"].dt.year
df_cb["quy"] = df_cb["ngay"].dt.quarter

tk_quy_cb = df_cb.groupby(["nam", "quy"]).size().reset_index(name="so_review")
print("Tổng hợp theo quý cơ bản:\n", tk_quy_cb)
```

##### Cách 2 · Vận dụng `resample('QE')` trên DatetimeIndex và lọc kỳ trọn vẹn (Nâng cao)

```python
# Thiết lập DatetimeIndex
df_ts = df_rv.set_index("ngay")

# Resample theo quý kết thúc (Quarter End)
tk_resample = df_ts.resample("QE").size().rename("so_review").to_frame()

# Xác định mốc snapshot trích xuất dữ liệu
moc_snapshot = df_rv["ngay"].max()
print(f"Mốc snapshot dữ liệu: {moc_snapshot.strftime('%Y-%m-%d')}")

# Kiểm tra xem quý cuối cùng đã kết thúc chưa
# Một quý kết thúc tại ngày cuối cùng của quý đó
ngay_cuoi_quy_hien_tai = tk_resample.index[-1]
quy_da_ket_thuc = moc_snapshot >= ngay_cuoi_quy_hien_tai

if not quy_da_ket_thuc:
    print(f"Cảnh báo: Quý {tk_resample.index[-1].strftime('%Y-Q%q')} chưa kết thúc trọn vẹn! Đang loại bỏ để tránh thiên lệch.")
    tk_quy_chuan = tk_resample.iloc[:-1]
else:
    tk_quy_chuan = tk_resample

print("Báo cáo theo quý chuẩn mực phân tích:\n", tk_quy_chuan)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiểm họa của kỳ cắt ngang (Truncation Bias)**:
  Nếu bạn giữ nguyên quý 2 năm 2025 (mới chỉ chạy được đến ngày 20/06, thiếu mất 10 ngày cuối cùng), con số tổng của quý đó sẽ thấp hơn bình thường. Khi vẽ đồ thị đường, đường biểu diễn sẽ lao dốc ở điểm cuối cùng, dễ khiến ban giám đốc hiểu lầm rằng chất lượng dịch vụ hoặc lượng khách hàng đang bị sụt giảm nghiêm trọng.
- **`resample()` vs `groupby()`**:
  `resample()` làm việc trực tiếp trên cấu trúc thời gian của `DatetimeIndex`. Điểm ưu việt tuyệt đối của nó so với `groupby()` là nếu trong một quý nào đó **hoàn toàn không có đánh giá nào phát sinh**, `resample()` vẫn tự động tạo ra dòng cho quý đó với giá trị `0`, giúp bảo toàn tính liên tục của trục thời gian.

---

### Bài 8.3: Cửa sổ trượt (Rolling Window): Làm mịn dao động tuần

#### Tình huống thực tế
Doanh số bán lẻ của một siêu thị biến động mạnh theo ngày trong tuần: Thứ Bảy và Chủ Nhật luôn cao gấp 3 lần ngày thường. Hãy tính đường trung bình trượt 7 ngày (*7-day rolling average*) để triệt tiêu hiệu ứng ngày trong tuần, và xác định cửa sổ 7 ngày liên tiếp nào có tổng doanh số cao kỷ lục.

```python
# Tạo dữ liệu doanh thu 30 ngày (đơn vị: triệu đồng)
rng = np.random.default_rng(123)
ngay_30 = pd.date_range("2025-03-01", periods=30, freq="D")
# Ngày cuối tuần (thứ 7, CN có index 5, 6) được nhân thêm hệ số 2.5
he_so_tuan = np.where(ngay_30.dayofweek >= 5, 2.5, 1.0)
doanh_so_goc = (rng.normal(50, 5, size=30) * he_so_tuan).round(1)

df_sales = pd.DataFrame({"ngay": ngay_30, "doanh_thu": doanh_so_goc}).set_index("ngay")
```

#### Lời giải

##### Cách 1 · Lặp thủ công qua từng lát cắt 7 ngày (Căn bản)

```python
tb_truot_cb = [None] * len(df_sales)
values = df_sales["doanh_thu"].tolist()

for i in range(6, len(values)):
    lat_cat = values[i - 6 : i + 1]
    tb_truot_cb[i] = round(sum(lat_cat) / 7.0, 2)

df_sales["tb_truot_cb"] = tb_truot_cb
print("5 dòng đầu cách thủ công:\n", df_sales.head(10))
```

##### Cách 2 · Sử dụng `.rolling(7, min_periods=1)` và tìm đỉnh cao nhất (Nâng cao)

```python
# 1. Tính trung bình trượt 7 ngày
# min_periods=1 giúp tính toán ngay từ ngày đầu tiên (không bị NaN ở 6 ngày đầu)
df_sales["tb_truot_7d"] = df_sales["doanh_thu"].rolling(window=7, min_periods=1).mean().round(2)

# 2. Tính tổng doanh thu trượt 7 ngày trọn vẹn (window=7 chuẩn)
tong_truot_7d = df_sales["doanh_thu"].rolling(window=7).sum()

# 3. Tìm thời điểm kết thúc của cửa sổ có tổng doanh thu kỷ lục
ngay_dinh = tong_truot_7d.idxmax()
doanh_thu_ky_luc = tong_truot_7d.loc[ngay_dinh]
ngay_bat_dau = ngay_dinh - pd.Timedelta(days=6)

print(f"Cửa sổ 7 ngày đạt đỉnh cao nhất: từ {ngay_bat_dau.strftime('%d/%m')} đến {ngay_dinh.strftime('%d/%m')}")
print(f"Tổng doanh thu kỷ lục: {doanh_thu_ky_luc:.1f} triệu đồng (Trung bình: {doanh_thu_ky_luc/7:.1f} tr/ngày)")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Vai trò làm mịn của Rolling Window**: Dao động chu kỳ tuần (*weekly seasonality*) là một dạng nhiễu tần số cao. Việc lấy trung bình trên đúng một chu kỳ trọn vẹn (7 ngày) triệt tiêu hoàn toàn hiệu ứng cuối tuần, làm lộ rõ xu hướng tăng trưởng nền tảng (*underlying trend*) của doanh nghiệp.
- **Ý nghĩa của `min_periods`**:
  Nếu không khai báo `min_periods`, 6 ngày đầu tiên của bảng sẽ mang giá trị `NaN` vì hệ thống chưa tích lũy đủ 7 quan sát. Bằng cách đặt `min_periods=1`, Pandas sẽ tính trung bình trên số ngày thực có (ngày 1 lấy chính nó, ngày 2 lấy trung bình 2 ngày), giúp dữ liệu sẵn sàng hiển thị trọn vẹn ngay từ điểm bắt đầu.

---

### Bài 8.4: Tính toán tăng trưởng cùng kỳ (Year-over-Year - YoY) và Bẫy so sánh quý dang dở

#### Tình huống thực tế
Một chuỗi bán lẻ điện máy tại Việt Nam muốn theo dõi đà tăng trưởng doanh số theo quý qua 3 năm (2023 - 2025). Dữ liệu được trích xuất (snapshot) vào ngày `2025-08-20` (giữa Quý 3/2025). Ban giám đốc yêu cầu tính chỉ số tăng trưởng cùng kỳ (Year-over-Year - YoY) cho từng quý:
$$
\begin{aligned}
YoY_t = \frac{V_t - V_{t-4}}{V_{t-4}} \times 100\%
\end{aligned}
$$

Nếu chỉ đơn thuần gọi `.pct_change(4)`, Quý 3/2025 sẽ bị so sánh số liệu mới trải qua 51 ngày với Quý 3/2024 trọn vẹn 92 ngày, dẫn đến một con số sụt giảm giả tạo ($-40\%$) gây hoảng loạn không đáng có cho ban điều hành! Hãy xây dựng giải pháp phân tích:
1. Tổng hợp doanh số theo từng quý và nhận diện tính trọn vẹn của từng quý (`is_complete`).
2. Với các quý đã trọn vẹn: Tính chỉ số tăng trưởng YoY chuẩn xác.
3. Với quý dang dở: Chỉ so sánh trên cùng khoảng thời gian tương đương (51 ngày đầu của Quý 3/2024) hoặc chuẩn hóa thành doanh số bình quân ngày ($Sales / Days$).
4. Định dạng chuỗi báo cáo chuyên nghiệp (`+12.4%`, `-3.8%`, hoặc `Chưa đủ kỳ gốc`).

```python
# Tạo dữ liệu giả lập doanh thu hàng ngày từ 01/01/2023 đến 20/08/2025
rng = np.random.default_rng(2025)
ngay_ds = pd.date_range("2023-01-01", "2025-08-20", freq="D")
# Doanh số tăng dần qua các năm, có tính thời vụ cao vào Q4 (mua sắm cuối năm)
xu_huong_nam = 1.0 + (ngay_ds.year - 2023) * 0.15
thoi_vu_quy = np.where(ngay_ds.quarter == 4, 1.4, 1.0)
doanh_so = (rng.normal(100, 10, size=len(ngay_ds)) * xu_huong_nam * thoi_vu_quy).round(1)

df_doanh_so = pd.DataFrame({"ngay": ngay_ds, "doanh_thu": doanh_so}).set_index("ngay")
```

#### Lời giải

##### Cách 1 · Resample quý trực tiếp và tính `pct_change(4)` (Căn bản: Bẫy số liệu)

```python
# 1. Resample theo quý lịch kết thúc
df_quy_cb = df_doanh_so.resample("QE")["doanh_thu"].sum().to_frame()

# 2. Tính YoY bằng pct_change(4)
df_quy_cb["yoy_cb"] = (df_quy_cb["doanh_thu"].pct_change(periods=4) * 100).round(1)

print("Tổng hợp theo quý (Căn bản):
", df_quy_cb.tail(6))
# BẪY NGUY HIỂM: Quý 3/2025 ghi nhận tăng trưởng âm sâu (~ -40% đến -45%)!
# Ban giám đốc có thể nghĩ rằng tình hình kinh doanh sụp đổ,
# nhưng thực chất chỉ vì Q3/2025 mới chỉ có 51 ngày thay vì 92 ngày!
```

##### Cách 2 · Nhận diện quý dang dở và Chuẩn hóa tốc độ bình quân ngày (Nâng cao)

```python
def phan_tich_yoy_chuan_xac(df: pd.DataFrame, ngay_snapshot: str) -> pd.DataFrame:
    moc_snapshot = pd.Timestamp(ngay_snapshot)
    
    # 1. Tổng hợp theo quý và tính số ngày thực có trong mỗi quý
    quy_grp = df.groupby(df.index.to_period("Q"))
    
    df_bc = quy_grp.agg(
        tong_doanh_thu=("doanh_thu", "sum"),
        so_ngay_thuc=("doanh_thu", "count"),
        ngay_dau=("doanh_thu", lambda s: s.index.min()),
        ngay_cuoi=("doanh_thu", lambda s: s.index.max())
    )
    
    # 2. Xác định ngày cuối lý thuyết của từng quý
    df_bc["ngay_cuoi_ly_thuyet"] = df_bc.index.to_timestamp(how="end").normalize()
    # Quý trọn vẹn nếu ngày cuối thực tế bằng hoặc sau ngày cuối lý thuyết
    df_bc["tron_ven"] = df_bc["ngay_cuoi"] >= df_bc["ngay_cuoi_ly_thuyet"]
    
    # 3. Tính doanh thu bình quân ngày (Daily Run-rate) để so sánh công bằng
    df_bc["doanh_thu_ngay"] = df_bc["tong_doanh_thu"] / df_bc["so_ngay_thuc"]
    
    # 4. Tính YoY theo tổng doanh thu (chỉ áp dụng cho quý trọn vẹn)
    doanh_thu_cung_ky = df_bc["tong_doanh_thu"].shift(4)
    yoy_tong = (df_bc["tong_doanh_thu"] - doanh_thu_cung_ky) / doanh_thu_cung_ky * 100
    
    # 5. Tính YoY theo bình quân ngày (áp dụng được cho cả quý dang dở!)
    runrate_cung_ky = df_bc["doanh_thu_ngay"].shift(4)
    yoy_runrate = (df_bc["doanh_thu_ngay"] - runrate_cung_ky) / runrate_cung_ky * 100
    
    # 6. Đóng gói kết quả báo cáo chuyên nghiệp
    ket_qua = pd.DataFrame(index=df_bc.index)
    ket_qua["tong_doanh_thu"] = df_bc["tong_doanh_thu"].round(1)
    ket_qua["so_ngay"] = df_bc["so_ngay_thuc"]
    ket_qua["trang_thai"] = np.where(df_bc["tron_ven"], "Trọn vẹn", "Dang dở (Snapshot)")
    
    # Định dạng chuỗi hiển thị
    def format_yoy(val, is_complete):
        if pd.isna(val):
            return "N/A (Chưa đủ mốc)"
        dau = "+" if val > 0 else ""
        canh_bao = "" if is_complete else " *"
        return f"{dau}{val:.1f}%{canh_bao}"
    
    ket_qua["yoy_bao_cao"] = [
        format_yoy(val, comp) for val, comp in zip(yoy_runrate, df_bc["tron_ven"])
    ]
    
    return ket_qua

ket_qua_yoy = phan_tich_yoy_chuan_xac(df_doanh_so, "2025-08-20")
print("Báo cáo tăng trưởng YoY chuẩn mực sư phạm:
", ket_qua_yoy.tail(6))
```

#### Phân tích bản chất & Bình luận sư phạm
- **Bản chất của chỉ số tăng trưởng cùng kỳ (YoY)**:
  Trong phân tích tài chính và bán lẻ, so sánh cùng kỳ năm trước (*Year-over-Year*) là chỉ số quan trọng bậc nhất vì nó tự động triệt tiêu yếu tố thời vụ (*seasonality*). Ví dụ: Quý 4 luôn có Tết hoặc Giáng sinh nên doanh thu luôn cao hơn Quý 3 ($QoQ > 0$), nhưng so với Quý 4 năm trước lại có thể sụt giảm ($YoY < 0$).
- **Nguyên tắc "So sánh quả táo với quả táo" (Apples-to-Apples)**:
  Khi snapshot dữ liệu tại ngày 20/08/2025, Quý 3 mới chỉ chạy được $55\%$ thời gian. Việc so sánh trực tiếp tổng sản lượng là so sánh "táo với cam". Giải pháp đúng đắn là chuyển sang so sánh **tốc độ doanh thu bình quân ngày (Daily Run-rate)** hoặc trích xuất đúng 51 ngày đầu tiên của Quý 3/2024 để đối chiếu song song.

---


## Phần 9. Đảm bảo Chất lượng Dữ liệu & Kiểm thử Chéo bảng (Cross-table QA)

::: info Trọng tâm tư duy
Một bảng dữ liệu đơn lẻ trông có thể rất sạch, nhưng khi ghép nối vào toàn bộ hệ thống cơ sở dữ liệu, các lỗi nghiêm trọng mới bắt đầu lộ diện: **Bản ghi con mồ côi (orphaned records)**, **khóa tự nhiên bị trùng lặp**, và **con số tổng hợp dẫn xuất bị lệch pha**. Một kỹ sư dữ liệu chuyên nghiệp luôn xây dựng bộ kiểm thử chất lượng (QA report) tự động trước khi nạp dữ liệu vào kho.
:::

### Bài 9.1: Kiểm tra toàn vẹn khóa ngoại và phát hiện bản ghi mồ côi

#### Tình huống thực tế
Cho bảng thông tin phòng nghỉ `df_listings` và bảng lịch sử đánh giá `df_reviews`. Cần kiểm tra xem có đánh giá nào mang `listing_id` không hề tồn tại trong bảng phòng không (bản ghi mồ côi do phòng đã bị xóa nhưng đánh giá chưa được dọn sạch).

```python
df_listings = pd.DataFrame({
    "id": [101, 102, 103],
    "name": ["Phòng view hồ", "Studio phố cổ", "Căn hộ cao cấp"]
})

df_reviews = pd.DataFrame({
    "review_id": [1, 2, 3, 4, 5],
    "listing_id": [101, 102, 999, 101, 888],  # 999 và 888 không tồn tại trong listings
    "rating": [5, 4, 1, 5, 2]
})
```

#### Lời giải

##### Cách 1 · Ghép bảng `merge` với cờ `indicator=True` (Căn bản)

```python
# Ghép left join với indicator
df_kiem_tra = pd.merge(
    df_reviews,
    df_listings[["id"]],
    left_on="listing_id",
    right_on="id",
    how="left",
    indicator=True
)

# Các dòng có _merge == 'left_only' là bản ghi mồ côi
cac_dong_mo_coi_cb = df_kiem_tra[df_kiem_tra["_merge"] == "left_only"]
print(f"Số lượng đánh giá mồ côi (Cách 1): {len(cac_dong_mo_coi_cb)}")
print(cac_dong_mo_coi_cb[["review_id", "listing_id"]])
```

##### Cách 2 · Vector hóa với toán tử phủ định `~` và `isin()` (Nâng cao)

```python
# Kiểm tra sự tồn tại trong tập khóa chính bằng Hash Table tầng C
tap_khoa_hop_le = set(df_listings["id"])
mat_na_mo_coi = ~df_reviews["listing_id"].isin(tap_khoa_hop_le)

so_luong_loi = mat_na_mo_coi.sum()
cac_id_sai = df_reviews.loc[mat_na_mo_coi, "listing_id"].unique().tolist()

print(f"Báo cáo QA: Phát hiện {so_luong_loi} dòng không khớp khóa ngoại!")
print(f"Danh sách mã phòng mồ côi vi phạm: {cac_id_sai}")
assert so_luong_loi == 2 and set(cac_id_sai) == {999, 888}
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiệu năng của `isin()` so với `merge()`**:
  Phép nối bảng `merge()` phải tạo ra một DataFrame trung gian, cấp phát bộ nhớ cho các cột mới và sắp xếp lại chỉ mục. Khi bảng đánh giá có hàng chục triệu dòng, `merge` sẽ rất tốn RAM và thời gian CPU. Ngược lại, `isin(set)` chuyển tập khóa chính thành một bảng băm (*Hash Set*) và thực hiện tra cứu $O(1)$ cho mỗi dòng của bảng review, nhanh hơn gấp nhiều lần và tiết kiệm tối đa bộ nhớ.
- **Tính toàn vẹn tham chiếu (Referential Integrity)**: Trong kiến trúc kho dữ liệu, các bản ghi mồ côi sẽ làm sai lệch nghiêm trọng các phép nối `INNER JOIN` (làm mất dữ liệu) hoặc phép tính tổng doanh thu/đánh giá.

---

### Bài 9.2: Đóng gói báo cáo kiểm tra chất lượng dữ liệu (QA Report)

#### Tình huống thực tế
Cho bảng thông tin chỗ ở `df_listings` có cột ghi sẵn `number_of_reviews` (tổng số đánh giá) và bảng chi tiết `df_reviews`. Hãy xây dựng một quy trình kiểm thử 3 bước và đóng gói thành một bảng `qa_report` gồm 3 cột: `quy_tac`, `so_dong_loi`, `danh_gia`:
1. **Kiểm tra miền thời gian**: Không có đánh giá nào xảy ra trong tương lai (sau ngày `2025-06-30`).
2. **Kiểm tra khóa tự nhiên**: Cặp `(listing_id, date, reviewer_id)` không được phép trùng lặp.
3. **Đối chiếu số liệu dẫn xuất**: Cột `number_of_reviews` trong bảng phòng phải khớp đúng số dòng thực đếm từ bảng đánh giá.

```python
df_listings = pd.DataFrame({
    "id": [101, 102, 103],
    "number_of_reviews": [3, 1, 5]  # Phòng 103 ghi 5 nhưng thực tế chỉ có 1 review
})

df_reviews = pd.DataFrame({
    "listing_id": [101, 101, 101, 102, 103, 101],
    "date": pd.to_datetime(["2025-01-01", "2025-02-01", "2025-03-01", "2025-01-10", "2026-12-31", "2025-01-01"]),
    "reviewer_id": [1, 2, 3, 4, 5, 1]  # Dòng 0 và dòng 5 bị trùng hoàn toàn
})
```

#### Lời giải

##### Cách 1 · Kiểm tra rời rạc từng điều kiện bằng câu lệnh `assert` (Căn bản)

```python
# 1. Kiểm tra ngày tương lai
loi_ngay = (df_reviews["date"] > "2025-06-30").sum()

# 2. Kiểm tra trùng lặp
loi_trung = df_reviews.duplicated(subset=["listing_id", "date", "reviewer_id"]).sum()

# 3. Kiểm tra khớp số đếm
dem_thuc = df_reviews.groupby("listing_id").size()
# So sánh thủ công
print(f"Lỗi ngày tương lai: {loi_ngay}, Lỗi trùng: {loi_trung}")
```

##### Cách 2 · Đóng gói tự động thành Bảng Kiểm chuẩn Chất lượng `qa_report` (Nâng cao)

```python
def tao_bao_cao_qa(listings: pd.DataFrame, reviews: pd.DataFrame, moc_ngay: str) -> pd.DataFrame:
    danh_sach_kiem_tra = []

    # Quy tắc 1: Miền thời gian hợp lệ
    n_tuong_lai = (reviews["date"] > moc_ngay).sum()
    danh_sach_kiem_tra.append({
        "quy_tac": "Ngày review không vượt quá mốc snapshot",
        "so_dong_loi": int(n_tuong_lai),
        "danh_gia": "ĐẠT" if n_tuong_lai == 0 else "CẢNH BÁO (có ngày tương lai)"
    })

    # Quy tắc 2: Khóa tự nhiên không trùng lặp
    n_trung_lap = reviews.duplicated(subset=["listing_id", "date", "reviewer_id"]).sum()
    danh_sach_kiem_tra.append({
        "quy_tac": "Khóa tự nhiên (listing_id, date, reviewer_id) duy nhất",
        "so_dong_loi": int(n_trung_lap),
        "danh_gia": "ĐẠT" if n_trung_lap == 0 else "LỖI (trùng bản ghi)"
    })

    # Quy tắc 3: Đối chiếu số lượng dẫn xuất với số đếm thực tế
    dem_thuc_te = reviews.groupby("listing_id").size().rename("so_dem_thuc")
    doi_chieu = listings[["id", "number_of_reviews"]].merge(
        dem_thuc_te, left_on="id", right_index=True, how="left"
    ).fillna({"so_dem_thuc": 0})
    
    n_lech_so = (doi_chieu["number_of_reviews"] != doi_chieu["so_dem_thuc"]).sum()
    danh_sach_kiem_tra.append({
        "quy_tac": "Khớp số lượng review ghi sẵn với số dòng thực tế",
        "so_dong_loi": int(n_lech_so),
        "danh_gia": "ĐẠT" if n_lech_so == 0 else "LỆCH SỐ LIỆU (cần tính lại)"
    })

    return pd.DataFrame(danh_sach_kiem_tra)

qa_result = tao_bao_cao_qa(df_listings, df_reviews, "2025-06-30")
print("Báo cáo QA chuẩn mực:\n", qa_result.to_string(index=False))
```

#### Phân tích bản chất & Bình luận sư phạm
- **Tư duy QA trong Data Engineering**: Trong phát triển phần mềm, bạn có kiểm thử đơn vị (*Unit Test*). Trong kỹ thuật dữ liệu, bạn bắt buộc phải có **Kiểm thử dữ liệu (Data Quality Test)**. Thay vì để các lỗi sai phát tán âm thầm vào báo cáo của ban lãnh đạo, một bảng `qa_report` được thực thi tự động sau mỗi lần nạp dữ liệu sẽ lập tức cảnh báo bất kỳ sai lệch nào.

---

### Bài 9.3: Thẩm định độ lệch cửa sổ 12 tháng gần nhất (LTM Mismatch) và Bẫy năm nhuận

#### Tình huống thực tế
Trong bảng thông tin nhà cung cấp có cột dẫn xuất `so_don_ltm` (số đơn hàng trong 12 tháng gần nhất, tức *Last Twelve Months*). Ngày chụp snapshot hệ thống là `2024-03-01` (năm 2024 là năm nhuận có 366 ngày).
Hai nhóm kỹ sư nội bộ xây dựng bộ lọc thời gian theo hai công thức khác nhau:
- **Nhóm Kỹ thuật (Trừ ngày tuyệt đối)**: Điều kiện `ngay >= snapshot_date - pd.Timedelta(days=365)` $\implies$ rơi vào `2023-03-02` (vô tình bỏ sót ngày `2023-03-01` do năm 2024 có ngày nhuận 29/02!).
- **Nhóm Nghiệp vụ (Trừ lịch tròn theo năm)**: Điều kiện `ngay >= snapshot_date - pd.DateOffset(years=1)` $\implies$ rơi vào đúng ngày `2023-03-01`.

Hãy viết mã đối chiếu độ lệch kết quả giữa hai cách tiếp cận, phát hiện các đơn hàng rơi vào "vùng tranh chấp ranh giới biên" (*boundary dispute zone*), và giải thích nguyên tắc đồng nhất định nghĩa dữ liệu.

```python
# Giả lập dữ liệu đơn hàng xung quanh ranh giới 1 năm
snapshot_date = pd.Timestamp("2024-03-01")

df_don_hang = pd.DataFrame({
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "supplier_id": ["NCC_A", "NCC_A", "NCC_B", "NCC_B", "NCC_A"],
    "order_date": pd.to_datetime([
        "2023-02-28",  # Ngoài phạm vi 12 tháng
        "2023-03-01",  # VÙNG TRANH CHẤP: Đúng 1 năm trước (DateOffset lấy, Timedelta bỏ sót!)
        "2023-03-02",  # Cả 2 cách đều lấy
        "2024-02-15",  # Trong phạm vi
        "2024-02-29"   # Ngày nhuận đặc biệt
    ]),
    "amount": [5.0, 12.0, 8.0, 15.0, 20.0]
})
```

#### Lời giải

##### Cách 1 · Lọc đơn lẻ bằng Timedelta 365 ngày (Căn bản: Bỏ sót ngày nhuận)

```python
# Nhóm Kỹ thuật dùng timedelta 365 ngày
moc_365 = snapshot_date - pd.Timedelta(days=365)
print(f"Mốc thời gian Timedelta(365 days): {moc_365.strftime('%Y-%m-%d')}")
# Kết quả là 2023-03-02, bỏ sót ngày 2023-03-01!

don_ltm_cb = df_don_hang[df_don_hang["order_date"] >= moc_365]
so_don_cb = don_ltm_cb.groupby("supplier_id")["order_id"].count()
print("Số đơn LTM theo Timedelta(365d):
", so_don_cb)
```

##### Cách 2 · So sánh đối chứng với DateOffset và Phân tích vùng biên (Nâng cao)

```python
def doi_chieu_dinh_nghia_ltm(df: pd.DataFrame, snapshot: pd.Timestamp) -> pd.DataFrame:
    # Mốc 1: Theo năm lịch tròn (DateOffset)
    moc_offset = snapshot - pd.DateOffset(years=1)
    # Mốc 2: Theo 365 ngày tuyệt đối (Timedelta)
    moc_delta = snapshot - pd.Timedelta(days=365)
    
    print(f"Mốc DateOffset(years=1): {moc_offset.strftime('%Y-%m-%d')}")
    print(f"Mốc Timedelta(days=365):  {moc_delta.strftime('%Y-%m-%d')}")
    
    # Lọc 2 tập
    mask_offset = df["order_date"] >= moc_offset
    mask_delta = df["order_date"] >= moc_delta
    
    # Bản ghi rơi vào vùng tranh chấp (DateOffset lấy nhưng Timedelta bỏ sót)
    vung_tranh_chap = df[mask_offset & (~mask_delta)]
    print(f"
Phát hiện {len(vung_tranh_chap)} đơn hàng rơi vào vùng ranh giới biên:")
    print(vung_tranh_chap[["order_id", "supplier_id", "order_date", "amount"]])
    
    # Tổng hợp đối chiếu theo nhà cung cấp
    ltm_offset = df[mask_offset].groupby("supplier_id")["order_id"].count().rename("so_don_offset")
    ltm_delta = df[mask_delta].groupby("supplier_id")["order_id"].count().rename("so_don_delta")
    
    bang_doi_chieu = pd.concat([ltm_offset, ltm_delta], axis=1).fillna(0).astype(int)
    bang_doi_chieu["lech_pha"] = bang_doi_chieu["so_don_offset"] - bang_doi_chieu["so_don_delta"]
    
    return bang_doi_chieu

bang_ltm = doi_chieu_dinh_nghia_ltm(df_don_hang, snapshot_date)
print("
Bảng đối chiếu độ lệch LTM giữa hai định nghĩa:
", bang_ltm)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Bẫy năm nhuận trong chuỗi thời gian**: Một năm dương lịch thông thường có 365 ngày, nhưng năm nhuận (như 2024, 2028) có 366 ngày. Khi lấy ngày snapshot `2024-03-01` trừ đi 365 ngày, bạn mới chỉ lùi về ngày `2023-03-02`, khiến mốc tròn một năm `2023-03-01` bị bỏ rơi ngoài rìa!
- **DateOffset vs Timedelta**: Lớp `pd.Timedelta` đại diện cho một khoảng thời gian vật lý cố định (chính xác từng giây), trong khi `pd.DateOffset` đại diện cho khoảng thời gian theo **quy ước lịch của con người** (bảo toàn ngày và tháng). Trong các báo cáo kinh doanh tài chính, khái niệm "1 năm qua" luôn được hiểu là cùng ngày này năm ngoái, do đó bắt buộc phải sử dụng `pd.DateOffset(years=1)`.

---


## Phần 10. Xử lý Dữ liệu Văn bản với LLM & Kỷ luật Đo lường

::: info Trọng tâm tư duy
Ứng dụng Mô hình Ngôn ngữ Lớn (LLM) vào xử lý dữ liệu phi cấu trúc không phải là "gọi prompt và tin tưởng mù quáng". Để đưa LLM vào sản xuất, bạn bắt buộc phải xây dựng **phương pháp đối chứng (Baseline)**, **ràng buộc cấu trúc dữ liệu đầu ra bằng Schema (Pydantic)**, và **đo lường độ chính xác trên tập nhãn chuẩn vàng (Gold Standard)**.
:::

### Bài 10.1: Xây dựng phương pháp đối chứng (Baseline) không dùng LLM

#### Tình huống thực tế
Cho danh sách các đoạn bình luận của khách hàng về dịch vụ phòng khách sạn. Cần phân loại cảm xúc thành 3 nhãn: `"positive"`, `"negative"`, hoặc `"neutral"`. Trước khi chi ngân sách gọi API LLM, hãy xây dựng một mô hình đối chứng dựa trên tập từ khóa (*Rule-based Baseline*) với chi phí 0 đồng.

```python
danh_gia_mau = [
    {"id": 1, "text": "Phòng rất sạch sẽ, chủ nhà thân thiện và nhiệt tình."},
    {"id": 2, "text": "Vị trí gần biển, phòng tạm ổn."},
    {"id": 3, "text": "Quá thất vọng, phòng đầy mùi ẩm mốc và máy lạnh hỏng."},
    {"id": 4, "text": "Không gian yên tĩnh, giá cả hợp lý."},
    {"id": 5, "text": "Dịch vụ cực kỳ tệ, không bao giờ quay lại!"}
]
```

#### Lời giải

##### Cách 1 · Duyệt vòng lặp với kiểm tra chuỗi con cơ bản (Căn bản)

```python
tu_tich_cuc = ["sạch sẽ", "thân thiện", "nhiệt tình", "hợp lý", "tuyệt vời"]
tu_tieu_cuc = ["thất vọng", "ẩm mốc", "hỏng", "tệ", "kinh khủng"]

nhan_baseline_cb = []
for item in danh_gia_mau:
    t = item["text"].lower()
    score = 0
    for w in tu_tich_cuc:
        if w in t:
            score += 1
    for w in tu_tieu_cuc:
        if w in t:
            score -= 1
            
    if score > 0:
        nhan_baseline_cb.append("positive")
    elif score < 0:
        nhan_baseline_cb.append("negative")
    else:
        nhan_baseline_cb.append("neutral")

print("Gán nhãn baseline cơ bản:", nhan_baseline_cb)
```

##### Cách 2 · Vector hóa từ khóa với Regex và xây dựng hàm phân loại chuẩn hóa (Nâng cao)

```python
import re

PAT_POS = re.compile(r"\b(sạch sẽ|thân thiện|nhiệt tình|hợp lý|tuyệt vời|tốt|đẹp)\b", re.IGNORECASE)
PAT_NEG = re.compile(r"\b(thất vọng|ẩm mốc|hỏng|tệ|kinh khủng|bẩn|kém)\b", re.IGNORECASE)

def phan_loai_baseline(text: str) -> str:
    n_pos = len(PAT_POS.findall(text))
    n_neg = len(PAT_NEG.findall(text))
    chênh_lệch = n_pos - n_neg
    if chênh_lệch > 0:
        return "positive"
    elif chênh_lệch < 0:
        return "negative"
    return "neutral"

ket_qua_baseline = [
    {**d, "sentiment_baseline": phan_loai_baseline(d["text"])}
    for d in danh_gia_mau
]
print("Baseline nâng cao chuẩn hóa:\n", json.dumps(ket_qua_baseline, ensure_ascii=False, indent=2))
```

#### Phân tích bản chất & Bình luận sư phạm
- **Vì sao bắt buộc phải có Baseline trước khi dùng LLM?**:
  Trong một bài toán thực tế, giải pháp Rule-based bằng từ khóa thường đã có thể giải quyết tốt $70\% - 80\%$ trường hợp thông thường với tốc độ xử lý hàng trăm nghìn dòng mỗi giây và chi phí bằng 0. Khi áp dụng LLM, mục tiêu của bạn là đo lường xem LLM có thể xử lý tốt hơn ở $20\%$ trường hợp phức tạp (như có từ phủ định *"phòng không sạch chút nào"*, mỉa mai, nói giảm nói tránh) hay không. Nếu không có mốc đối chứng, bạn không thể chứng minh được hiệu quả đầu tư (*ROI*) của dự án AI.

---

### Bài 10.2: Ràng buộc Schema với Pydantic và Đo lường chất lượng nhãn

#### Tình huống thực tế
Giả sử bạn gọi LLM để trích xuất thông tin có cấu trúc từ đánh giá. Kết quả trả về từ mô hình ngôn ngữ cần được kiểm duyệt chặt chẽ bằng Pydantic `BaseModel`. Sau đó, đối chiếu nhãn dự đoán với tập nhãn chuẩn vàng (*Gold Standard*) để tính toán độ chính xác tổng thể (*Accuracy*).

```python
# Phản hồi giả lập từ LLM (chứa 1 kết quả vi phạm schema và 1 kết quả đoán sai nhãn)
raw_llm_responses = [
    {"id": 1, "sentiment": "positive", "rating": 5, "aspects": ["vệ sinh", "chủ nhà"]},
    {"id": 2, "sentiment": "neutral", "rating": 4, "aspects": ["vị trí"]},
    {"id": 3, "sentiment": "negative", "rating": 1, "aspects": ["vệ sinh", "tiện nghi"]},
    {"id": 4, "sentiment": "sieu_tot", "rating": 5, "aspects": []},  # LỖI: nhãn sai enum
    {"id": 5, "sentiment": "positive", "rating": 1, "aspects": ["dịch vụ"]}   # ĐOÁN SAI so với Gold
]

# Tập nhãn chuẩn vàng do chuyên gia gán nhãn thủ công (Gold Standard)
GOLD_LABELS = {
    1: "positive",
    2: "neutral",
    3: "negative",
    4: "positive",
    5: "negative"
}
```

#### Lời giải

##### Cách 1 · Tự viết hàm kiểm tra kiểu bằng các câu lệnh `if` lồng nhau (Căn bản)

```python
nhan_hop_le = {"positive", "negative", "neutral"}
hop_le_cb = []
loi_cb = []

for item in raw_llm_responses:
    s = item.get("sentiment")
    r = item.get("rating")
    if s in nhan_hop_le and isinstance(r, int) and 1 <= r <= 5:
        hop_le_cb.append(item)
    else:
        loi_cb.append(item)

print(f"Số lượng hợp lệ: {len(hop_le_cb)}, Số lượng lỗi: {len(loi_cb)}")
```

##### Cách 2 · Kiểm chuẩn bằng Pydantic `BaseModel` và Đo độ chính xác (Nâng cao)

```python
from pydantic import BaseModel, Field, ValidationError
from typing import Literal

# Định nghĩa Schema nghiêm ngặt
class ReviewExtraction(BaseModel):
    id: int
    sentiment: Literal["positive", "negative", "neutral"]
    rating: int = Field(ge=1, le=5)
    aspects: list[str]

danh_sach_hop_le = []
danh_sach_loi_schema = []

for resp in raw_llm_responses:
    try:
        obj = ReviewExtraction(**resp)
        danh_sach_hop_le.append(obj)
    except ValidationError as e:
        danh_sach_loi_schema.append({"id": resp.get("id"), "error": str(e.errors()[0]["msg"])})

print(f"Chặn thành công {len(danh_sach_loi_schema)} phản hồi vi phạm Schema:")
print(danh_sach_loi_schema)

# Đo lường Accuracy trên các đầu ra hợp lệ
dung = sum(1 for obj in danh_sach_hop_le if obj.sentiment == GOLD_LABELS.get(obj.id))
tong = len(danh_sach_hop_le)
accuracy = dung / tong if tong > 0 else 0.0

print(f"Độ chính xác (Accuracy) trên tập hợp lệ: {dung}/{tong} = {accuracy:.2%}")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Schema là tầng phòng thủ đầu tiên**: Khi làm việc với LLM, đầu ra là chuỗi văn bản không xác định. Việc dùng Pydantic với kiểu `Literal["positive", "negative", "neutral"]` giúp loại bỏ ngay lập tức các kết quả bị "ảo giác" (*hallucination*) sinh ra nhãn lạ như `"sieu_tot"` trước khi chúng xâm nhập vào cơ sở dữ liệu.
- **Kỷ luật đo lường (Measurement Discipline)**: Không bao giờ đánh giá mô hình bằng trực giác *"tôi thấy nó chạy khá tốt"*. Hãy luôn có một tập nhãn chuẩn vàng nhỏ (khoảng 100 đến 300 mẫu) được kiểm duyệt bằng tay, tính toán tường minh Accuracy, Precision và Recall để đưa ra con số định lượng thuyết phục.

---

### Bài 10.3: Dự toán ngân sách Token API trước khi gọi và Hậu kiểm ngữ nghĩa tự động (Semantic Assertion)

#### Tình huống thực tế
Bạn phụ trách xử lý 5,000 phản hồi đánh giá của khách hàng bằng mô hình ngôn ngữ lớn (LLM). Để đảm bảo tính chuyên nghiệp và kỷ luật kỹ thuật:
1. **Dự toán ngân sách (FinOps)**: Trước khi kích hoạt đường ống xử lý, hãy viết hàm tính toán lượng token dự kiến cho prompt đầu vào và phản hồi đầu ra, tính tổng chi phí theo bảng giá API ($0.15\$$ / 1M input tokens, $0.60\$$ / 1M output tokens), và quy đổi sang VNĐ (tỷ giá 25,400 VNĐ/\$).
2. **Hậu kiểm ngữ nghĩa tự động (Semantic Assertion)**: Mô hình trả về kết quả tuân thủ đúng Schema Pydantic, nhưng vẫn có thể chứa đựng các **mâu thuẫn ngữ nghĩa nội tại (Semantic Conflict)** mà schema không thể bắt được:
   - *Xung đột 1*: Khách hàng chấm điểm `rating >= 4` (hài lòng) nhưng LLM lại gán `sentiment = "negative"`.
   - *Xung đột 2*: Khách hàng chấm điểm `rating <= 2` (thất vọng) nhưng LLM lại gán `sentiment = "positive"`.
   - *Xung đột 3*: Đánh giá dài trên 30 từ nhưng danh sách trích xuất khía cạnh `aspects` lại rỗng.
   Hãy viết bộ lọc kiểm thử tự động để gắn cờ phân loại và xuất danh sách các bản ghi đáng ngờ chuyển cho con người thẩm định lại (*Human-in-the-loop*).

```python
# Mẫu đánh giá và phản hồi giả lập từ LLM sau khi đã vượt qua Pydantic
du_lieu_llm = pd.DataFrame([
    {"id": 1, "text": "Phòng nghỉ tuyệt vời, nhân viên lễ tân cực kỳ chu đáo.", "rating": 5, "sentiment": "positive", "aspects": ["phòng", "nhân viên"]},
    {"id": 2, "text": "Khách sạn quá bẩn, máy lạnh hỏng không thể ngủ nổi.", "rating": 1, "sentiment": "negative", "aspects": ["vệ sinh", "tiện nghi"]},
    {"id": 3, "text": "Dịch vụ phòng rất tốt nhưng đồ ăn sáng hơi nguội.", "rating": 4, "sentiment": "negative", "aspects": ["dịch vụ", "ẩm thực"]}, # XUNG ĐỘT 1: 4 sao nhưng nhãn negative
    {"id": 4, "text": "Thất vọng toàn tập, phòng ẩm mốc và có mùi khó chịu.", "rating": 1, "sentiment": "positive", "aspects": ["vệ sinh"]},          # XUNG ĐỘT 2: 1 sao nhưng nhãn positive
    {"id": 5, "text": "Khách sạn nằm ở vị trí trung tâm, rất thuận tiện đi lại, phòng ốc bài trí tinh tế, view ngắm hoàng hôn tuyệt đẹp.", "rating": 5, "sentiment": "positive", "aspects": []} # XUNG ĐỘT 3: Review dài nhưng aspects rỗng
])
```

#### Lời giải

##### Cách 1 · Ước tính thủ công và lọc câu lệnh `if` rải rác (Căn bản)

```python
# 1. Ước tính thô
# Tiếng Việt trung bình ~1.5 đến 2 token mỗi từ
so_luong_mau = 5000
tu_trung_binh_prompt = 150 # Prompt mẫu + text đánh giá
token_in = so_luong_mau * tu_trung_binh_prompt * 1.5
token_out = so_luong_mau * 50 * 1.5

chi_phi_usd = (token_in / 1e6 * 0.15) + (token_out / 1e6 * 0.60)
print(f"Chi phí ước tính thô: {chi_phi_usd:.3f} USD (~{chi_phi_usd * 25400:,.0f} VNĐ)")

# 2. Lọc xung đột bằng vòng lặp if
danh_sach_nghi_ngo = []
for _, r in du_lieu_llm.iterrows():
    if (r["rating"] >= 4 and r["sentiment"] == "negative") or        (r["rating"] <= 2 and r["sentiment"] == "positive"):
        danh_sach_nghi_ngo.append(r["id"])
print("ID nghi ngờ mâu thuẫn điểm số:", danh_sach_nghi_ngo)
```

##### Cách 2 · Đóng gói Hàm Dự toán FinOps và Bộ Hậu kiểm Ngữ nghĩa Tự động (Nâng cao)

```python
# 1. Hàm dự toán ngân sách API chuyên nghiệp
def du_toan_ngan_sach_llm(n_samples: int, avg_input_chars: int, max_output_tokens: int = 100) -> dict:
    # Quy tắc thực nghiệm tiếng Việt có dấu: 1 token ~ 2.5 ký tự UTF-8
    est_input_tokens_per_sample = int(avg_input_chars / 2.5) + 80 # 80 token system prompt
    total_input_tokens = n_samples * est_input_tokens_per_sample
    total_output_tokens = n_samples * max_output_tokens
    
    # Đơn giá chuẩn (USD / 1 triệu token)
    cost_in = (total_input_tokens / 1_000_000) * 0.15
    cost_out = (total_output_tokens / 1_000_000) * 0.60
    total_usd = cost_in + cost_out
    total_vnd = total_usd * 25_400
    
    return {
        "so_luong_mau": n_samples,
        "tong_input_tokens": total_input_tokens,
        "tong_output_tokens": total_output_tokens,
        "chi_phi_usd": round(total_usd, 4),
        "chi_phi_vnd": int(total_vnd)
    }

du_toan = du_toan_ngan_sach_llm(n_samples=5000, avg_input_chars=350, max_output_tokens=80)
print("Dự toán ngân sách LLM:
", json.dumps(du_toan, indent=2, ensure_ascii=False))

# 2. Bộ hậu kiểm ngữ nghĩa tự động (Semantic Assertion Engine)
def hau_kiem_ngu_nghia(df: pd.DataFrame) -> pd.DataFrame:
    df_qa = df.copy()
    
    # Định nghĩa các điều kiện vi phạm bất biến nghiệp vụ
    cond_xung_dot_cao = (df_qa["rating"] >= 4) & (df_qa["sentiment"] == "negative")
    cond_xung_dot_thap = (df_qa["rating"] <= 2) & (df_qa["sentiment"] == "positive")
    
    # Đếm số từ trong đoạn văn bản
    so_tu = df_qa["text"].str.split().str.len()
    cond_thieu_aspects = (so_tu >= 15) & (df_qa["aspects"].apply(len) == 0)
    
    # Phân loại trạng thái kiểm định
    df_qa["qa_status"] = "PASSED"
    df_qa.loc[cond_xung_dot_cao, "qa_status"] = "ALERT_CONFLICT_HIGH_RATING"
    df_qa.loc[cond_xung_dot_thap, "qa_status"] = "ALERT_CONFLICT_LOW_RATING"
    df_qa.loc[cond_thieu_aspects, "qa_status"] = "ALERT_EMPTY_ASPECTS"
    
    return df_qa

df_kiem_dinh = hau_kiem_ngu_nghia(du_lieu_llm)
ty_le_loi = (df_kiem_dinh["qa_status"] != "PASSED").mean() * 100
print(f"
Kết quả hậu kiểm: Tỷ lệ bản ghi đáng ngờ = {ty_le_loi:.1f}%")
print(df_kiem_dinh[["id", "rating", "sentiment", "qa_status"]])
```

#### Phân tích bản chất & Bình luận sư phạm
- **FinOps trong Khoa học Dữ liệu**: Không bao giờ nhấn nút chạy một pipeline gọi LLM trên hàng chục nghìn dòng mà không tính toán trước chi phí và thời gian thực thi (*Latency*). Một phép tính dự toán trước chỉ mất 2 phút nhưng bảo vệ bạn khỏi các sự cố tiêu lạm ngân sách đám mây.
- **Hậu kiểm Assertion: Tầng phòng thủ thứ hai**:
  Schema Pydantic chỉ đảm bảo **tính toàn vẹn về mặt cú pháp** (*Syntactic Integrity*, tức đúng kiểu int, đúng chuỗi enum). Nó hoàn toàn bất lực trước **tính toàn vẹn về mặt nghiệp vụ** (*Semantic/Business Invariant*). Việc đặt các luật Assertion để sàng lọc những trường hợp mâu thuẫn giữa điểm số và cảm xúc giúp xây dựng mô hình Hybrid: Máy móc xử lý $95\%$ trường hợp thông thường, con người chỉ cần can thiệp rà soát $5\%$ trường hợp có cờ cảnh báo (*Human-in-the-loop*).

---


## Phần 11. Trực quan hóa Dữ liệu Cơ bản & Nhận diện Biểu đồ Biến dạng

::: info Trọng tâm tư duy
Mục đích tối thượng của biểu đồ là trả lời một câu hỏi phân tích cụ thể, không phải để "trang trí". Một biểu đồ tốt giúp người xem nắm bắt ngay quy luật dữ liệu. Ngược lại, một biểu đồ bị thiết kế sai (cắt ngắn trục tung, chọn sai số bins) sẽ bóp méo sự thật và dẫn dắt người xem đến các quyết định sai lầm.
:::

### Bài 11.1: Histogram và lựa chọn số khoảng chia (Bins): Vạch trần phân phối hai đỉnh

#### Tình huống thực tế
Cho dữ liệu khảo sát số ngày mở bán trong năm (`availability_365`) của 1,000 chỗ ở. Dữ liệu thực tế có phân phối hai cực: Một nhóm lớn chỉ mở cửa bán dưới 15 ngày (hoặc đóng cửa hoàn toàn), và một nhóm khác mở bán chuyên nghiệp gần như quanh năm (trên 340 ngày), ở khoảng giữa rất ít phòng.
Hãy so sánh:
1. Khi vẽ histogram với `bins=5` (quá ít).
2. Khi vẽ histogram với `bins=40` (chuẩn xác).

```python
# Tạo dữ liệu giả lập phân phối hai cực (bimodal)
rng = np.random.default_rng(42)
nhom_it = rng.integers(0, 20, size=400)
nhom_nhieu = rng.integers(330, 366, size=500)
nhom_giua = rng.integers(20, 330, size=100)
availability = np.concatenate([nhom_it, nhom_nhieu, nhom_giua])
```

#### Lời giải

##### Cách 1 · Vẽ histogram mặc định với số bins tùy tiện (Căn bản: Che giấu bản chất)

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
# Bins=5 làm phẳng hoàn toàn phân phối hai đỉnh
plt.hist(availability, bins=5, color="skyblue", edgecolor="black")
plt.title("Biểu đồ với bins=5 (Che giấu cấu trúc hai cực)")
plt.xlabel("Số ngày mở bán trong năm")
plt.ylabel("Số lượng phòng")
plt.close() # Không hiển thị ở môi trường script
```

##### Cách 2 · Thiết lập `bins=40` phơi bày phân phối hai cực và gắn thông điệp cụ thể (Nâng cao)

```python
fig, ax = plt.subplots(figsize=(9, 5))

# Sử dụng bins=40 tương ứng với các khoảng ~9 ngày
n, bins, patches = ax.hist(
    availability,
    bins=40,
    color="#2b5c8f",
    edgecolor="white",
    linewidth=0.8,
    alpha=0.85
)

# Đặt tiêu đề truyền tải thông điệp phân tích thay vì mô tả kỹ thuật
ax.set_title(
    "Phân phối số ngày mở bán: Thị trường phân cực rõ rệt\n(Chủ yếu mở quanh năm hoặc gần như đóng cửa)",
    fontsize=12,
    fontweight="bold",
    pad=15
)
ax.set_xlabel("Số ngày mở bán trong năm (ngày)", fontsize=10)
ax.set_ylabel("Số lượng chỗ ở", fontsize=10)
ax.grid(axis="y", linestyle="--", alpha=0.5)

# Đánh dấu 2 đỉnh phân cực
ax.annotate("Đỉnh đóng cửa\n(0-20 ngày)", xy=(10, 250), xytext=(60, 260),
            arrowprops=dict(facecolor="red", arrowstyle="->"))
ax.annotate("Đỉnh mở quanh năm\n(340-365 ngày)", xy=(350, 300), xytext=(220, 310),
            arrowprops=dict(facecolor="green", arrowstyle="->"))

plt.tight_layout()
plt.close()
print("Đã thiết lập biểu đồ phân phối hai đỉnh chuẩn mực!")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiệu ứng nén của số lượng Bins**: Khi bạn chọn số `bins` quá ít (ví dụ `bins=5`), các khoảng chia quá rộng (mỗi khoảng hơn 70 ngày) đã nuốt chửng hai đỉnh nhọn ở hai đầu biên, biến biểu đồ thành một hình chữ U nông hoặc một đường cong thoai thoải giả tạo. Ngược lại, nếu chọn `bins` quá lớn (ví dụ `bins=200`), biểu đồ sẽ bị nhiễu răng cưa do cỡ mẫu mỗi cột quá nhỏ.
- **Tiêu đề biểu đồ phải có linh hồn**: Một kỹ sư dữ liệu giỏi không bao giờ đặt tiêu đề chung chung kiểu *"Biểu đồ histogram của availability_365"*. Hãy đặt tiêu đề trả lời cho câu hỏi: *"Người xem cần nhận ra điều gì từ biểu đồ này?"*.

---

### Bài 11.2: Phát hiện và sửa chữa biểu đồ cột bị cắt ngắn trục tung (Truncated Axis)

#### Tình huống thực tế
Một bản báo cáo kinh doanh nội bộ so sánh tỷ lệ hoàn thành đơn hàng đúng hạn của hai đội giao vận:
- Đội Alpha: Đạt $96.0\%$.
- Đội Beta: Đạt $98.5\%$.
Người thiết kế biểu đồ đặt trục $Y$ bắt đầu từ $95.0\%$, khiến cột của đội Beta trông cao gấp gần $2.5$ lần so với đội Alpha, tạo cảm giác chênh lệch một trời một vực. Hãy phân tích sai lệch và viết mã dựng lại biểu đồ trung thực.

#### Lời giải

##### Cách 1 · Nhận diện sai lệch bằng công thức tỷ lệ trực quan (Căn bản)

```python
val_alpha = 96.0
val_beta = 98.5

# 1. Chênh lệch số học thực tế
chenh_lech_thuc = (val_beta - val_alpha) / val_alpha * 100
print(f"Mức tăng trưởng số học thực tế: {chenh_lech_thuc:.2f}%")

# 2. Chênh lệch nhìn thấy khi trục Y bắt đầu từ 95.0
chieu_cao_nhin_alpha = val_alpha - 95.0  # = 1.0 đơn vị
chieu_cao_nhin_beta = val_beta - 95.0    # = 3.5 đơn vị
ty_le_nhin_thay = chieu_cao_nhin_beta / chieu_cao_nhin_alpha
print(f"Mức chênh lệch thị giác bị phóng đại: Gấp {ty_le_nhin_thay:.1f} lần!")
```

##### Cách 2 · Tái lập biểu đồ trung thực với trục tung bắt đầu từ 0 (Nâng cao)

```python
fig, (ax_sai, ax_dung) = plt.subplots(1, 2, figsize=(12, 5))

doi = ["Đội Alpha", "Đội Beta"]
ty_le = [96.0, 98.5]

# Biểu đồ sai: Trục tung bị cắt ngắn (Truncated Axis)
ax_sai.bar(doi, ty_le, color=["#d9534f", "#5cb85c"], width=0.5)
ax_sai.set_ylim(95.0, 100.0)
ax_sai.set_title("GÂY HIỂU SAI: Trục Y từ 95%\n(Phóng đại chênh lệch gấp 3.5 lần)", color="red")
ax_sai.set_ylabel("Tỷ lệ hoàn thành (%)")

# Biểu đồ đúng: Trục tung bắt đầu từ 0 chuẩn mực
ax_dung.bar(doi, ty_le, color=["#4a90e2", "#50e3c2"], width=0.5)
ax_dung.set_ylim(0, 110.0)
ax_dung.set_title("TRUNG THỰC: Trục Y bắt đầu từ 0%\n(Chênh lệch thực tế khiêm tốn: 2.5 điểm %)", color="green")
ax_dung.set_ylabel("Tỷ lệ hoàn thành (%)")

# Ghi chú con số trực tiếp lên đầu cột
for ax in (ax_sai, ax_dung):
    for i, v in enumerate(ty_le):
        ax.text(i, v + 0.3, f"{v:.1f}%", ha="center", fontweight="bold")

plt.tight_layout()
plt.close()
print("Đã đối chiếu thành công hai biểu đồ!")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Nguyên tắc bất biến của Biểu đồ Cột (Bar Chart)**: Biểu đồ cột mã hóa dữ liệu bằng **chiều dài của thanh cột**. Não bộ con người tự động so sánh tỷ lệ giữa chiều dài của hai thanh để suy ra tỷ lệ chênh lệch giá trị. Khi bạn cắt ngắn trục tung, tỷ lệ chiều dài thị giác không còn tương ứng với tỷ lệ số học, biến biểu đồ thành một công cụ ngụy tạo số liệu.
- **Khi nào được phép thu hẹp trục $Y$?**: Bạn chỉ được phép thu hẹp thang đo trục $Y$ trên **Biểu đồ Đường (Line Chart)** khi mục tiêu là theo dõi sự biến động (*fluctuation*) của một chuỗi thời gian liên tục (ví dụ: Chỉ số chứng khoán VN-Index hay nhiệt độ cơ thể người bệnh), và bắt buộc phải ghi chú rõ ràng thang đo trên đồ thị.

---

### Bài 11.3: Thiết kế biểu đồ thanh ngang có nhãn trực tiếp (`ax.bar_label`) và Kiểm thử thuộc tính đồ thị bằng `assert`

#### Tình huống thực tế
Phân tích tỷ lệ khách sạn đạt chứng chỉ "Du lịch Bền vững" theo 8 quận du lịch lớn. Tên các quận có độ dài không đồng đều và khá dài (*"Quận Hoàn Kiếm"*, *"Quận Hai Bà Trưng"*, *"Quận Nam Từ Liêm"*, v.v.).
Yêu cầu:
1. Vẽ biểu đồ thanh ngang (*Horizontal Bar Chart*) thay vì cột dọc để nhãn tên quận hiển thị tự nhiên từ trái sang phải, không bị xoay nghiêng hoặc đè chữ.
2. Sắp xếp các thanh theo thứ tự tăng dần để quận có tỷ lệ cao nhất nằm ở vị trí trên cùng.
3. Sử dụng `ax.bar_label` hiển thị con số phần trăm trực tiếp ngay cạnh mỗi thanh, loại bỏ hoàn toàn các đường viền trục trên, phải và trục hoành bên dưới để đạt tỷ lệ mực-dữ liệu (*Data-Ink Ratio*) tối ưu.
4. Đóng gói mã nguồn thành hàm và viết bộ kiểm thử tự động bằng `assert` kiểm tra tính toàn vẹn của đối tượng biểu đồ (kiểm tra giới hạn trục hoành bắt đầu từ 0, kiểm tra số lượng thanh cột vẽ ra).

```python
df_ben_vung = pd.DataFrame({
    "quan": [
        "Quận Hoàn Kiếm", "Quận Ba Đình", "Quận Tây Hồ", "Quận Đống Đa",
        "Quận Hai Bà Trưng", "Quận Cầu Giấy", "Quận Nam Từ Liêm", "Quận Hà Đông"
    ],
    "ty_le": [42.5, 38.0, 35.2, 28.4, 25.1, 21.0, 18.5, 12.3]
})
```

#### Lời giải

##### Cách 1 · Vẽ biểu đồ cột dọc mặc định và xoay nhãn chữ (Căn bản: Kém trực quan)

```python
# Vẽ cột đứng cơ bản
plt.figure(figsize=(10, 4))
plt.bar(df_ben_vung["quan"], df_ben_vung["ty_le"], color="cornflowerblue")
plt.xticks(rotation=45, ha="right") # Bắt buộc phải xoay chữ do tên quận quá dài
plt.ylabel("Tỷ lệ bền vững (%)")
plt.title("Biểu đồ cột đứng truyền thống (Khó đọc nhãn)")
plt.close()
```

##### Cách 2 · Biểu đồ thanh ngang với `ax.bar_label` và Kiểm thử bằng `assert` (Nâng cao)

```python
def ve_bieu_do_thanh_ngang(df: pd.DataFrame, cot_danh_muc: str, cot_gia_tri: str) -> tuple[plt.Figure, plt.Axes]:
    # 1. Sắp xếp tăng dần để giá trị lớn nhất nổi bật ở trên cùng của trục tung
    df_sap_xep = df.sort_values(by=cot_gia_tri, ascending=True).reset_index(drop=True)
    
    fig, ax = plt.subplots(figsize=(9, 5))
    
    # 2. Vẽ thanh ngang ax.barh
    mau_thanh = ["#8ecae6"] * (len(df_sap_xep) - 1) + ["#023047"] # Đổi màu thanh top 1
    bars = ax.barh(df_sap_xep[cot_danh_muc], df_sap_xep[cot_gia_tri], color=mau_thanh, height=0.65)
    
    # 3. Gắn nhãn giá trị trực tiếp lên chóp thanh
    ax.bar_label(bars, fmt="%.1f%%", padding=5, fontsize=10, fontweight="bold", color="#023047")
    
    # 4. Tối ưu hóa Data-Ink Ratio: ẩn trục X và viền không cần thiết
    ax.set_xlim(0, max(df_sap_xep[cot_gia_tri]) * 1.18) # Tạo khoảng trống cho nhãn
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_color("#cccccc")
    ax.xaxis.set_visible(False) # Ẩn hoàn toàn trục X vì đã có nhãn trực tiếp
    
    # Tiêu đề tập trung vào thông điệp
    ax.set_title(
        "Tỷ lệ Cơ sở Lưu trú Đạt Chứng nhận Du lịch Bền vững theo Quận\n(Hoàn Kiếm dẫn đầu với 42.5%, gấp 3.5 lần Hà Đông)",
        fontsize=11, fontweight="bold", pad=15, loc="left"
    )
    
    plt.tight_layout()
    return fig, ax

fig, ax = ve_bieu_do_thanh_ngang(df_ben_vung, "quan", "ty_le")

# 5. BỘ KIỂM THỬ ĐỒ THỊ BẰNG ASSERT (Visual Testing)
# Kiểm tra trục hoành bắt đầu đúng từ 0 (không cắt cụt)
assert ax.get_xlim()[0] == 0, "LỖI: Trục hoành phải bắt đầu từ gốc 0!"
# Kiểm tra số lượng thanh vẽ ra khớp với số quận
so_thanh = len(ax.containers[0].patches)
assert so_thanh == len(df_ben_vung), f"LỖI: Kỳ vọng {len(df_ben_vung)} thanh, thực tế vẽ {so_thanh}!"
print("Toàn bộ các điều kiện kiểm thử biểu đồ đã ĐẠT chuẩn mực!")
plt.close(fig)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Khi nào bắt buộc dùng Biểu đồ Thanh ngang (Horizontal Bar)?**:
  Bất cứ khi nào danh mục có tên dài (tên cơ quan, địa danh, câu hỏi trắc nghiệm) hoặc số lượng danh mục từ 7 trở lên, hãy từ bỏ biểu đồ cột đứng. Não bộ con người đọc văn bản theo chiều ngang. Việc ép người đọc phải nghiêng đầu $45^\circ$ để đọc nhãn trục hoành là một sự thất bại về mặt thiết kế truyền thông.
- **Sức mạnh của `ax.bar_label` và Tỷ lệ Mực-Dữ liệu (Data-Ink Ratio)**:
  Bằng cách đưa con số trực tiếp lên đầu mỗi thanh, bạn giải phóng người xem khỏi việc phải dóng mắt từ đỉnh cột xuống trục hoành để ước lượng giá trị. Điều này cho phép bạn xóa bỏ hoàn toàn trục hoành, các vạch chia (*ticks*) và lưới ngang rối mắt, tạo nên một biểu đồ thanh lịch và tập trung tối đa vào thông điệp dữ liệu.

---


## Phần 12. Trực quan hóa Nâng cao & Phản biện Thống kê

::: info Trọng tâm tư duy
Phân tích nâng cao đòi hỏi bạn phải nhìn sâu vào các tầng lớp dữ liệu: Dùng Boxplot phân rã phân phối theo biến phân loại đa tầng (`hue`), và luôn cảnh giác cao độ trước các thủ thuật thống kê tinh vi như **chọn kỳ gốc có lợi (cherry-picking)**.
:::

### Bài 12.1: Seaborn Boxplot kết hợp Hue và giải mã râu hộp Tukey

#### Tình huống thực tế
Cho bảng dữ liệu giá phòng khách sạn phân theo hai tiêu chí: Loại phòng (`room_type`: Căn hộ nguyên căn vs Phòng riêng) và Kiểu chủ nhà (`kieu_host`: Chuyên nghiệp vs Nghiệp dư).
Hãy vẽ biểu đồ hộp phân rã hai chiều bằng Seaborn và giải thích chính xác cơ chế xác định ranh giới râu hộp (*whiskers*).

```python
import seaborn as sns

# Tạo dữ liệu giả lập có chủ đích
rng = np.random.default_rng(99)
n_samples = 200

df_hotel = pd.DataFrame({
    "room_type": rng.choice(["Nguyên căn", "Phòng riêng"], size=n_samples),
    "kieu_host": rng.choice(["Chuyên nghiệp", "Nghiệp dư"], size=n_samples),
    "price": rng.lognormal(mean=5.0, sigma=0.5, size=n_samples).round(1)
})
# Thêm một vài điểm ngoại lai cực lớn
df_hotel.loc[0, "price"] = 800.0
df_hotel.loc[1, "price"] = 950.0
```

#### Lời giải

##### Cách 1 · Tính toán các tứ phân vị và ranh giới râu hộp thủ công (Căn bản)

```python
# Khảo sát nhóm 'Nguyên căn' của host 'Chuyên nghiệp'
nhom = df_hotel.query("room_type == 'Nguyên căn' and kieu_host == 'Chuyên nghiệp'")["price"]

q1 = nhom.quantile(0.25)
q2 = nhom.quantile(0.50)  # Median
q3 = nhom.quantile(0.75)
iqr = q3 - q1

hang_rao_duoi = q1 - 1.5 * iqr
hang_rao_tren = q3 + 1.5 * iqr

# Tìm điểm dừng thực tế của râu hộp (quan sát thực xa nhất bên trong hàng rào)
rau_duoi = nhom[nhom >= hang_rao_duoi].min()
rau_tren = nhom[nhom <= hang_rao_tren].max()
diem_ngoai_lai = nhom[(nhom < hang_rao_duoi) | (nhom > hang_rao_tren)].tolist()

print(f"Q1 = {q1:.1f}, Q2 (Median) = {q2:.1f}, Q3 = {q3:.1f}, IQR = {iqr:.1f}")
print(f"Hàng rào lý thuyết: [{hang_rao_duoi:.1f}, {hang_rao_tren:.1f}]")
print(f"Đầu râu thực tế dừng tại: [{rau_duoi:.1f}, {rau_tren:.1f}]")
print(f"Các điểm ngoại lai ngoài râu: {diem_ngoai_lai}")
```

##### Cách 2 · Biểu đồ Boxplot kết hợp Stripplot phơi bày mật độ thực tế (Nâng cao)

```python
plt.figure(figsize=(10, 6))

# Lớp 1: Boxplot thể hiện tóm tắt 5 con số thống kê
ax = sns.boxplot(
    data=df_hotel,
    x="price",
    y="room_type",
    hue="kieu_host",
    palette="Set2",
    showmeans=True,  # Hiển thị thêm điểm Mean để so sánh với Median
    meanprops={"marker": "o", "markerfacecolor": "red", "markeredgecolor": "red", "markersize": "6"}
)

# Lớp 2: Stripplot bán trong suốt chồng lên trên để phơi bày cỡ mẫu và mật độ điểm thật
sns.stripplot(
    data=df_hotel,
    x="price",
    y="room_type",
    hue="kieu_host",
    dodge=True,
    alpha=0.35,
    color="black",
    jitter=0.2
)

ax.set_title("Phân phối giá theo loại phòng và phân khúc chủ nhà\n(Điểm đỏ: Mean | Đường giữa hộp: Median)", fontsize=12, fontweight="bold")
ax.set_xlabel("Giá phòng (USD/đêm)")
ax.set_ylabel("Loại phòng")

plt.tight_layout()
plt.close()
print("Đã vẽ biểu đồ hộp phân rã hai chiều chuẩn mực!")
```

#### Phân tích bản chất & Bình luận sư phạm
- **Quy tắc vàng của râu hộp Tukey**:
  Nhiều người lầm tưởng rằng hai đầu râu của boxplot luôn kéo dài tới đúng vị trí của hàng rào Tukey ($Q_1 - 1.5 \times IQR$ và $Q_3 + 1.5 \times IQR$). Đây là một hiểu lầm phổ biến. Râu chỉ dừng tại **quan sát thực tế xa nhất vẫn nằm bên trong hàng rào**, chứ không bao giờ dừng lại ở một con số hư cấu giữa khoảng trống dữ liệu.
- **Sức mạnh của việc chồng lớp `stripplot`**: Boxplot che giấu hoàn toàn cỡ mẫu. Một chiếc hộp vẽ từ 5 quan sát trông có thể y hệt một chiếc hộp vẽ từ 50,000 quan sát. Việc chồng thêm lớp điểm thực giúp người thẩm định nhìn thấy ngay cỡ mẫu thực và mật độ phân bố dày mỏng phía sau chiếc hộp.

---

### Bài 12.2: Phản biện chiêu trò chọn kỳ gốc có lợi (Cherry-picking Baseline)

#### Tình huống thực tế
Một bản báo cáo kinh doanh công bố: *"Số lượng giao dịch trong tháng 06/2025 tăng trưởng phi mã tới $120\%$ so với cùng kỳ năm trước!"*.
Khi truy xuất chuỗi dữ liệu 3 năm, bạn phát hiện:
- Tháng 06/2023: Đạt 1,000 giao dịch (hoạt động bình thường).
- Tháng 06/2024: Đạt 450 giao dịch (tháng xảy ra sự cố sập máy chủ toàn hệ thống).
- Tháng 06/2025: Đạt 990 giao dịch.
Hãy viết đoạn mã tính toán và phân tích xem mức tăng trưởng $120\%$ có phản ánh đúng thực chất năng lực kinh doanh hay không.

#### Lời giải

##### Cách 1 · Tính toán tốc độ tăng trưởng cơ bản theo công thức công bố (Căn bản)

```python
gd_2023 = 1000
gd_2024 = 450
gd_2025 = 990

# Công thức tăng trưởng YoY được báo cáo đưa ra
tang_truong_yoy = (gd_2025 - gd_2024) / gd_2024 * 100
print(f"Tăng trưởng công bố (so với đáy 2024): +{tang_truong_yoy:.1f}%")
```

##### Cách 2 · Phân tích độ nhạy đa mốc tham chiếu và vẽ chuỗi thời gian bối cảnh (Nâng cao)

```python
# Xây dựng bảng đánh giá đa chiều với các kỳ gốc khác nhau
bang_phan_bien = pd.DataFrame([
    {
        "ky_goc_so_sanh": "So với tháng 06/2024 (Đáy khủng hoảng)",
        "gia_tri_goc": gd_2024,
        "tang_truong_%": round((gd_2025 - gd_2024) / gd_2024 * 100, 2),
        "y_nghia_thuc_chat": "Tăng trưởng phục hồi kỹ thuật từ đáy suy thoái"
    },
    {
        "ky_goc_so_sanh": "So với tháng 06/2023 (Kỳ hoạt động bình thường)",
        "gia_tri_goc": gd_2023,
        "tang_truong_%": round((gd_2025 - gd_2023) / gd_2023 * 100, 2),
        "y_nghia_thuc_chat": "Suy giảm nhẹ (-1.0%), doanh nghiệp chưa lấy lại mức đỉnh cũ"
    },
    {
        "ky_goc_so_sanh": "So với mức trung bình 2 năm trước (725 giao dịch)",
        "gia_tri_goc": 725,
        "tang_truong_%": round((gd_2025 - 725) / 725 * 100, 2),
        "y_nghia_thuc_chat": "Tăng trưởng thực chất ở mức vừa phải (+36.6%)"
    }
])

print("Bảng thẩm định phản biện kỳ gốc:\n", bang_phan_bien.to_string(index=False))
```

#### Phân tích bản chất & Bình luận sư phạm
- **Bản chất của thủ thuật Cherry-picking**:
  Bằng cách cố tình chọn một kỳ gốc có mẫu số rất thấp (thời điểm đáy dịch bệnh, khủng hoảng, hoặc sự cố kỹ thuật), bất kỳ sự phục hồi tự nhiên nào cũng bị thổi phồng thành "tăng trưởng thần kỳ".
- **Văn phong phản biện của giáo sư**:
  Trong vai trò người thẩm định, không vội vàng phủ nhận con số tính toán học thuật ($990$ so với $450$ đúng là tăng $120\%$), nhưng bạn phải chỉ rõ bối cảnh: *"Mức tăng $120\%$ này chỉ là sự phục hồi kỹ thuật từ đáy sự cố năm 2024. Khi so sánh với mốc vận hành chuẩn năm 2023 (1,000 đơn), hoạt động của doanh nghiệp thực chất đang đi ngang hoặc giảm nhẹ $1.0\%$."*

---

## Phần 13. Kể chuyện bằng Dữ liệu & Thẩm định Phân tích

::: info Trọng tâm tư duy
Một bản phân tích xuất sắc không kết thúc ở các dòng code hay đồ thị, mà kết thúc ở **thông điệp ra quyết định**. Kỹ năng kể chuyện bằng dữ liệu (*Data Storytelling*) đòi hỏi bạn phải cấu trúc thông điệp theo mô hình Kim tự tháp, dùng từ ngữ chuẩn xác, và có năng lực vạch trần các nghịch lý toán học phức tạp như **Nghịch lý Simpson**.
:::

### Bài 13.1: Xây dựng và giải mã Nghịch lý Simpson (Simpson's Paradox)

#### Tình huống thực tế
Một sàn thương mại điện tử thử nghiệm giao diện thanh toán mới (B) so với giao diện cũ (A). Thử nghiệm chạy trên hai nhóm thiết bị: Điện thoại di động (*Mobile*) và Máy tính (*Desktop*).
Dữ liệu ghi nhận:
- **Nhóm Mobile**:
  - Giao diện A: 10 đơn thành công trên 100 lượt truy cập ($10.0\%$).
  - Giao diện B: 20 đơn thành công trên 150 lượt truy cập ($13.3\%$). (B thắng A!)
- **Nhóm Desktop**:
  - Giao diện A: 180 đơn thành công trên 200 lượt truy cập ($90.0\%$).
  - Giao diện B: 95 đơn thành công trên 100 lượt truy cập ($95.0\%$). (B thắng A!)
Hãy tính tỷ lệ chuyển đổi **gộp toàn bộ** của giao diện A và giao diện B, giải thích nghịch lý tại sao B thắng trên từng phân khúc nhưng lại thua khi tính tổng thể.

#### Lời giải

##### Cách 1 · Tính toán gộp đơn giản dẫn đến quyết định sai lầm (Căn bản)

```python
# Tính tổng số đơn thành công và tổng lượt truy cập
thanh_cong_A = 10 + 180
tong_truy_cap_A = 100 + 200
ty_le_gop_A = thanh_cong_A / tong_truy_cap_A

thanh_cong_B = 20 + 95
tong_truy_cap_B = 150 + 100
ty_le_gop_B = thanh_cong_B / tong_truy_cap_B

print(f"Giao diện A gộp: {thanh_cong_A}/{tong_truy_cap_A} = {ty_le_gop_A:.2%}")
print(f"Giao diện B gộp: {thanh_cong_B}/{tong_truy_cap_B} = {ty_le_gop_B:.2%}")

# Kết quả gộp: A (63.33%) cao hơn hẳn B (46.00%)!
# Nếu nhìn vào con số gộp, ban giám đốc sẽ quyết định KHAI TỬ giao diện B!
```

##### Cách 2 · Phân rã cấu trúc trọng số và phơi bày biến gây nhiễu (Nâng cao)

```python
import pandas as pd

# Mô hình hóa dữ liệu dạng bảng quan hệ
df_simpson = pd.DataFrame([
    {"giao_dien": "A", "thiet_bi": "Mobile", "thanh_cong": 10, "tong": 100},
    {"giao_dien": "A", "thiet_bi": "Desktop", "thanh_cong": 180, "tong": 200},
    {"giao_dien": "B", "thiet_bi": "Mobile", "thanh_cong": 20, "tong": 150},
    {"giao_dien": "B", "thiet_bi": "Desktop", "thanh_cong": 95, "tong": 100},
])

df_simpson["ty_le"] = (df_simpson["thanh_cong"] / df_simpson["tong"] * 100).round(2)

# Tính tỷ trọng phân bổ mẫu trên từng thiết bị
df_simpson["ty_trong_nhom_%"] = (
    df_simpson["tong"] / df_simpson.groupby("giao_dien")["tong"].transform("sum") * 100
).round(2)

print("Phân rã cơ cấu nghịch lý Simpson:\n", df_simpson)

# Giải mã nguyên nhân:
# - Desktop có tỷ lệ chuyển đổi nền rất cao (90-95%)
# - Mobile có tỷ lệ chuyển đổi nền rất thấp (10-13%)
# - Giao diện A được phân bổ tới 66.7% lưu lượng vào Desktop (hưởng lợi từ phân khúc dễ ăn)
# - Giao diện B bị phân bổ tới 60.0% lưu lượng vào Mobile (gánh nặng từ phân khúc khó nhằn)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Cơ chế của Nghịch lý Simpson**:
  Nghịch lý Simpson xuất hiện khi ta tính trung bình gộp mà bỏ qua một **biến gây nhiễu (Confounding Variable)** quan trọng (ở đây là *Loại thiết bị*). Do tỷ lệ chia lưu lượng không đồng đều giữa hai nhánh thử nghiệm, giao diện A được hưởng lợi thế cơ cấu khi có phần lớn người dùng đến từ Desktop.
- **Bài học ra quyết định**:
  Trong thực tế, **giao diện B mới là giao diện tối ưu vượt trội** vì trên bất kỳ thiết bị nào nó cũng đem lại tỷ lệ chuyển đổi cao hơn ($13.3\% > 10.0\%$ trên Mobile, và $95.0\% > 90.0\%$ trên Desktop). Bài học đắt giá cho mọi nhà khoa học dữ liệu: **Tuyệt đối không bao giờ đưa ra kết luận chỉ dựa trên con số trung bình gộp khi cơ cấu tỷ trọng giữa các nhóm có sự mất cân bằng nghiêm trọng**.

---

### Bài 13.2: Quy trình thẩm định 4 bước một kết luận phân tích số liệu

#### Tình huống thực tế
Một đối tác gửi tới bản báo cáo có kết luận đinh ninh:
*"Người dùng mua hàng vào ban đêm chi tiêu trung bình $1.5$ triệu đồng/đơn, cao hơn $50\%$ so với người mua ban ngày ($1.0$ triệu đồng). Vì vậy, chương trình khuyến mãi ban đêm đã kích thích người tiêu dùng mua sắm phóng tay hơn."*
Hãy đóng vai một chuyên gia thẩm định dữ liệu, triển khai quy trình thẩm định 4 bước chuẩn mực để chỉ ra các lỗ hổng phương pháp và viết lại kết luận đúng mức.

#### Lời giải

##### Phân tích theo Quy trình Thẩm định 4 Bước của Giáo sư

```python
# Dữ liệu mô phỏng tình huống
don_hang_dem = [1_000_000, 800_000, 1_200_000, 15_000_000] # 1 đơn cực lớn 15 triệu (outlier)
don_hang_ngay = [950_000, 1_050_000, 1_000_000, 1_000_000]

mean_dem = np.mean(don_hang_dem)       # 4.5 triệu (hoặc ví dụ 1.5 triệu)
median_dem = np.median(don_hang_dem)   # 1.1 triệu

mean_ngay = np.mean(don_hang_ngay)     # 1.0 triệu
median_ngay = np.median(don_hang_ngay) # 1.0 triệu

print(f"Ban đêm: Mean = {mean_dem/1e6:.2f}tr | Median = {median_dem/1e6:.2f}tr")
print(f"Ban ngày: Mean = {mean_ngay/1e6:.2f}tr | Median = {median_ngay/1e6:.2f}tr")
```

1. **Bước 1 · Truy số (Check the Numbers)**:
   - Truy ngược lại cơ sở dữ liệu thô: Cỡ mẫu ban đêm là bao nhiêu đơn? Cỡ mẫu ban ngày là bao nhiêu đơn?
   - Con số $1.5$ triệu đồng ban đêm là trung bình cộng (*Mean*) hay trung vị (*Median*)? Nếu cỡ mẫu ban đêm chỉ có một vài đơn ngoại lai giá trị cực lớn (như đồ điện tử, laptop), trung bình cộng sẽ bị kéo lệch nghiêm trọng.
2. **Bước 2 · Kiểm tra phương pháp (Methodological Audit)**:
   - So sánh trung vị: Trung vị ban đêm ($1.1$ triệu) chỉ nhỉnh hơn ban ngày ($1.0$ triệu) đúng $10\%$, hoàn toàn không có mức chênh lệch khủng khiếp $50\%$ như báo cáo rêu rao.
   - Kiểm tra cơ cấu mặt hàng: Khách hàng mua đêm có phải chủ yếu mua các sản phẩm giá trị cao (đồ công nghệ) hay không?
3. **Bước 3 · Đánh giá diễn giải (Interpretive Scrutiny)**:
   - **Lỗi ngụy biện nhân quả (Causality Fallacy)**: Kết luận khẳng định *"khuyến mãi ban đêm đã kích thích người tiêu dùng mua sắm phóng tay hơn"* là một phát biểu võ đoán. Dữ liệu quan sát chỉ cho thấy mối liên hệ đồng thời giữa *thời điểm mua* và *giá trị giỏ hàng*, không hề chứng minh chương trình khuyến mãi là *nguyên nhân* trực tiếp gây ra hành vi chi tiêu nhiều hơn (nguyên nhân có thể do người có thu nhập cao thường chỉ có thời gian rảnh lướt web vào đêm muộn).
4. **Bước 4 · Phán quyết & Viết lại đúng mức (Verdict & Revision)**:
   - **Phán quyết**: Bác bỏ kết luận nhân quả, đồng thời yêu cầu báo cáo lại bằng đại lượng trung vị và kiểm soát theo cơ cấu danh mục hàng hóa.
   - **Câu viết lại đúng mức sư phạm**:
     > *"Trong tập dữ liệu khảo sát, các đơn hàng phát sinh vào khung giờ đêm ghi nhận giá trị trung vị cao hơn khoảng 10% so với ban ngày. Cần thực hiện thử nghiệm A/B ngẫu nhiên có đối chứng trước khi khẳng định chương trình khuyến mãi ban đêm có tác động thúc đẩy giá trị giỏ hàng."*

---

### Bài 13.3: Tái cấu trúc thông điệp theo Kim tự tháp Minto và Chuẩn hóa phát ngôn đúng mức với số liệu

#### Tình huống thực tế
Một nhà phân tích dữ liệu thực tập gửi bản thảo báo cáo chiến dịch ra mắt dịch vụ phòng cao cấp:
*"Chúng tôi đã họp từ tháng 1, sau đó thu thập dữ liệu đặt phòng. Đến tháng 5 chúng tôi triển khai chương trình hội viên Vàng. Dữ liệu cho thấy chiến dịch đã tạo ra sự đột phá thần kỳ: Tỷ lệ đặt phòng lặp lại tăng vọt 5% từ 20% lên 25%, chứng tỏ chương trình hội viên là chìa khóa duy nhất thúc đẩy lòng trung thành của khách hàng."*

Hãy chỉ ra 4 lỗi diễn đạt số liệu nghiêm trọng trong đoạn văn trên, và tái cấu trúc lại toàn bộ báo cáo theo mô hình **Kim tự tháp Minto (Minto Pyramid Principle)**:
1. **Đỉnh tháp (Hành động & Kết luận cốt lõi)**: Đưa khuyến nghị then chốt lên câu đầu tiên.
2. **Tầng giữa (Các luận điểm chính - MECE)**: Tách bạch các trụ cột bằng chứng độc lập và toàn diện.
3. **Đáy tháp (Bằng chứng số liệu & Độ tin cậy)**: Cung cấp con số định lượng chuẩn mực và khoảng tin cậy.

#### Lời giải

##### Phân tích 4 lỗi diễn đạt số liệu nghiêm trọng (Audit Report)
1. **Lỗi 1 · Nhầm lẫn giữa Thay đổi Phần trăm (%) và Điểm Phần trăm (Percentage Points)**:
   Tỷ lệ tăng từ $20\%$ lên $25\%$ là mức tăng **5 điểm phần trăm (percentage points)**, hoặc mức tăng tương đối bằng:
   $$
   \begin{aligned}
   \frac{25\% - 20\%}{20\%} = \frac{5}{20} = +25\%
   \end{aligned}
   $$
   Viết *"tăng vọt 5%"* là sai bản chất toán học (nếu tăng $5\%$ thì từ $20\%$ chỉ lên $20\% \times 1.05 = 21\%$).
2. **Lỗi 2 · Ngôn từ phóng đại, phi học thuật**:
   Các cụm từ *"đột phá thần kỳ"*, *"tăng vọt"* là văn phong quảng cáo cảm tính, làm giảm sút nghiêm trọng tính khách quan của một bản báo cáo khoa học dữ liệu.
3. **Lỗi 3 · Ngụy biện quy chụp quan hệ nhân quả (Post Hoc Ergo Propter Hoc)**:
   Chương trình hội viên diễn ra vào tháng 5 và tỷ lệ quay lại tăng lên, nhưng tháng 5-6 cũng là mùa cao điểm du lịch hè! Chưa thể khẳng định chương trình hội viên là *"nguyên nhân duy nhất"* khi chưa kiểm soát biến mùa vụ hoặc làm thử nghiệm A/B đối chứng.
4. **Lỗi 4 · Kể chuyện tuần tự thời gian ru ngủ người nghe**:
   Kể lể *"chúng tôi đã họp từ tháng 1, sau đó thu thập dữ liệu..."* khiến người ra quyết định mất kiên nhẫn. Lãnh đạo cần biết ngay: **"Kết luận là gì và tôi cần làm gì tiếp theo?"**.

##### Bản viết lại chuẩn mực theo Kim tự tháp Minto (Executive Summary)

```markdown
### ĐỀ XUẤT HÀNH ĐỘNG (Đỉnh tháp Minto)
Mở rộng chương trình "Hội viên Vàng" trên toàn hệ thống trong Quý 4/2026, dự kiến đóng góp thêm 2.4 tỷ VNĐ doanh thu từ khách hàng thân thiết.

### BA LẬP LUẬN THEN CHỐT (Tầng giữa - MECE)
1. **Tỷ lệ giữ chân khách hàng tăng trưởng vững chắc**: Tỷ lệ đặt phòng lặp lại tăng 5.0 điểm phần trăm (tương đương tăng trưởng tương đối +25.0% so với cùng kỳ).
2. **Đã kiểm soát yếu tố mùa vụ**: So sánh đối chứng với nhóm khách hàng không tham gia hội viên trong cùng khung giờ mùa hè cho thấy hiệu ứng thực dương thuần túy đạt +3.2 điểm phần trăm (p-value < 0.01).
3. **Chi phí thu hút khách hàng thấp hơn 40%**: Chi phí duy trì hội viên cũ chỉ bằng 60% chi phí chạy quảng cáo tìm kiếm khách hàng mới.

### BẰNG CHỨNG SỐ LIỆU ĐỊNH LƯỢNG (Đáy tháp)
- Cỡ mẫu khảo sát: N = 4,200 khách hàng trong giai đoạn 01/05 - 31/07.
- Tỷ lệ quay lại nhóm hội viên: 25.0% (KTC 95%: [23.8%, 26.2%]).
- Tỷ lệ quay lại nhóm đối chứng: 20.0% (KTC 95%: [18.9%, 21.1%]).
- Mức chênh lệch thuần: +5.0 điểm phần trăm (Z = 4.12, có ý nghĩa thống kê cao).
```

#### Phân tích bản chất & Bình luận sư phạm
- **Nguyên lý Minto: Đi từ Câu trả lời (Answer First)**:
  Người bận rộn không có thời gian đọc hành trình tìm kiếm gian nan của bạn. Hãy luôn đặt câu trả lời và đề xuất hành động ở câu đầu tiên. Cấu trúc kim tự tháp giúp người đọc có thể dừng lại ở bất kỳ tầng nào mà vẫn nắm trọn vẹn thông điệp cốt lõi.
- **Kỷ luật phát ngôn số liệu**: Một nhà khoa học dữ liệu uy tín luôn phân định rạch ròi giữa **Điểm phần trăm** và **Tỷ lệ phần trăm**, không bao giờ gắn kết quan hệ nhân quả một cách tùy tiện, và luôn công bố khoảng tin cậy (*Confidence Interval*) cùng cỡ mẫu khảo sát.

---


## 14. Bảng tổng kết năng lực & Chỉ dẫn thực hành toàn diện

| Chuyên đề | Kỹ năng cốt lõi | Cạm bẫy ngầm cần tránh | Chuẩn tối ưu đề xuất |
| :--- | :--- | :--- | :--- |
| **Phần 1: Notebook & AI** | Quản lý trạng thái, hàm thuần khiết | Chạy cell ngoài trật tự, sửa biến toàn cục | Đóng gói hàm bất biến; Restart Kernel & Run All |
| **Phần 2: Python thuần** | Xử lý dữ liệu không phụ thuộc thư viện | `list.sort()` làm hỏng mảng gốc; tràn bộ nhớ `dict` | Dùng `str.translate`, `statistics.fmean`, `defaultdict` |
| **Phần 3: NumPy** | Bố cục bộ nhớ, Strides, Broadcasting | Nhầm lẫn giữa View và Copy; quên `keepdims=True` | Khai thác `np.ix_`, kiểm tra `shares_memory` |
| **Phần 4: Pandas cơ bản** | Lọc dữ liệu, xử lý `NaN`, lập hồ sơ | Gặp `SettingWithCopyWarning`; `fillna(0)` làm méo thống kê | Truy xuất một bước bằng `.loc`, phân tích độ nhạy `NaN` |
| **Phần 5: Pandas nâng cao** | GroupBy, Transform, Pivot, Merge | Nhân đôi dòng ngoài ý muốn khi `merge` | Dùng Named Aggregation, `transform`, `validate` |
| **Phần 6: Tối ưu quy mô** | Đọc có chọn lọc, Parquet, DuckDB | Nạp toàn bộ CSV gây tràn RAM (OOM) | Dùng `usecols`, Regex làm sạch, Parquet và DuckDB |
| **Phần 7: Chuỗi & Regex** | Biểu thức chính quy, tách nhãn nhị phân | Mẫu tham lam `.*` nuốt chửng văn bản; sót ký tự lạ | Dùng mẫu phủ định `[^"]+`, `(?:...)`, `get_dummies` |
| **Phần 8: Dữ liệu thời gian** | DatetimeIndex, Resampling, Rolling, Tăng trưởng YoY | Bẫy so sánh quý snapshot dang dở; `min_periods` gây NaN | Nhận diện kỳ trọn vẹn; chuẩn hóa doanh thu ngày; `rolling(min_periods=1)` |
| **Phần 9: Đảm bảo chất lượng** | Kiểm thử chéo bảng, bản ghi mồ côi, LTM | Lệch pha cột dẫn xuất; bẫy năm nhuận Timedelta vs DateOffset | Dùng vector `~isin()`, xây dựng `qa_report`, chuẩn hóa cửa sổ LTM lịch tròn |
| **Phần 10: Xử lý LLM** | Pydantic Schema, Baseline, Dự toán Token & Hậu kiểm | Chi phí API vượt trần; xung đột ngữ nghĩa nội tại giữa điểm và nhãn | Dự toán FinOps trước khi gọi; Schema Pydantic; bộ luật Semantic Assertion |
| **Phần 11: Trực quan cơ bản** | Histogram, Biểu đồ thanh ngang, Visual Test `assert` | Cắt ngắn trục tung; nhãn trục x chen chúc; che giấu 2 đỉnh | Thanh ngang `ax.bar_label` tối ưu Data-Ink; kiểm thử biểu đồ bằng `assert` |
| **Phần 12: Trực quan nâng cao** | Seaborn Boxplot, phản biện thống kê đa mốc | Râu hộp Tukey dừng ở lý thuyết; chiêu trò cherry-picking mốc đáy | Lồng `stripplot` kiểm tra cỡ mẫu; vẽ chuỗi toàn cảnh phản biện mốc so sánh |
| **Phần 13: Kể chuyện dữ liệu** | Kim tự tháp Minto, Nghịch lý Simpson, Lời đúng mức | Nhầm lẫn phần trăm vs điểm phần trăm; quy chụp nhân quả cảm tính | Cấu trúc Answer-First (Minto); kiểm soát biến gây nhiễu; thẩm định 4 bước |


