---
course: "xu-ly-du-lieu"
section: "notes"
prerequisites: ["bien-kieu","list","dictionary"]
lessonStatus: "reference"
---

# Lập Trình Xử Lý Dữ Liệu 

Môn học **Lập trình Xử lý Dữ liệu** sử dụng NumPy, pandas và Polars để tổ chức, phân tích và làm sạch dữ liệu. Người học cũng xây dựng các quy trình xử lý dữ liệu có thể kiểm tra và thực hiện lại.

---

##  Lộ trình Ôn tập Trọng tâm

```mermaid
flowchart LR
    A["1. NumPy & Vectorization"] --> B["2. Pandas Data Wrangling"]
    B --> C["3. Làm sạch & Biến đổi"]
    C --> D["4. SQL & Lưu trữ Dữ liệu"]
    D --> E["5. Trực quan hóa (EDA)"]
```

##  Danh mục Bài học

- [**Bài 1: Tổng quan môn học, công cụ & chính sách AI**](./bai-01-tong-quan-cong-cu-chinh-sach-ai.md)
  - Ẩn dụ gian bếp nhà hàng: 5 công đoạn xử lý dữ liệu
  - Môi trường lập trình: `venv`, `requirements.txt`, `.python-version`
  - Chính sách sử dụng AI (Chế độ đóng  vs Chế độ mở )
- [**Bài 2: Python cơ bản cho xử lý dữ liệu**](./bai-02-python-co-ban.md)
  - So sánh và chọn đúng cấu trúc: `list`, `dict`, `set`, `tuple`
  - Tư duy viết hàm, lambda và xử lý chuỗi dữ liệu
- [**Bài 3: NumPy và tư duy vector hoá**](./bai-03-numpy.md)
  - Bản chất `ndarray` trong bộ nhớ và tại sao nhanh hơn `list`
  - Broadcasting, Vectorization và các hàm toán học mảng
- [**Bài 4: Làm quen với pandas**](./bai-04-lam-quen-pandas.md)
  - Khắc phục nhược điểm của mảng không tên: Cấu trúc Series & DataFrame
  - Đọc ghi file (CSV, Excel), kiểm tra kiểu dữ liệu và tổng quan
- [**Bài 5: Series & DataFrame chuyên sâu**](./bai-05-series-dataframe-chuyen-sau.md)
  - Phân biệt triệt để `loc` vs `iloc`, Index Alignment và bẫy phát sinh `NaN`
  - Lọc dữ liệu điều kiện boolean indexing và các phép biến đổi cốt lõi
