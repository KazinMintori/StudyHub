# Nguồn và biên soạn môn Lập trình xử lý dữ liệu

Trục biên soạn hiện hành gồm 13 chương và hai phụ lục của Wes McKinney. Xem `authoring-map.md` để biết ranh giới nguồn, `authoring-contract.json` để biết slug và tiên quyết, `source-inventory.json` để biết các trang đã truy cập. Các tệp `bai-*.md` cũ bên dưới chỉ là bản lưu của lần biên soạn trước, không quyết định nội dung xuất bản.

Nội dung chính ở `docs/xu-ly-du-lieu/bai-giang/` và `src/content/courses/xu-ly-du-lieu/lectures/`. Bài giảng tiếng Việt được biên soạn độc lập, không dịch toàn văn hoặc sao chép lời văn được bảo hộ. IAI chỉ bổ sung kỹ thuật liên quan và bài tập phù hợp. Phần chuyển thể IAI giữ ghi công và [CC BY-NC-SA 4.0](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

`python scripts/collect-data-processing-sources.py` cập nhật kiểm kê. Văn bản đầy đủ chỉ được lưu trong thư mục tạm của hệ điều hành để đối chiếu, không đưa vào website. `node scripts/integrate-data-course.mjs` cập nhật catalog sau khi đã đủ bài giảng. Không build toàn site trên máy cục bộ.

Thư mục lưu trữ nguồn tài liệu, ánh xạ chương trình và công cụ đối chiếu phục vụ biên soạn học phần Xử lý dữ liệu.

---

## 1. Giáo trình & Tài liệu Tham khảo Trực tuyến (Web References)

1. **Python for Data Analysis (3rd Edition)** — *Wes McKinney* (O'Reilly Media)
   - **Bản đọc trực tuyến chính thức:** [wesmckinney.com/book](https://wesmckinney.com/book/)
   - **Kho mã nguồn ví dụ (MIT License):** [github.com/wesm/pydata-book](https://github.com/wesm/pydata-book)
   - **Nội dung:** Cấu trúc dữ liệu Series, DataFrame của pandas, mảng ndarray của NumPy, làm sạch dữ liệu, xử lý chuỗi và chuỗi thời gian (time-series).

2. **Python Data Science Handbook (2nd Edition)** — *Jake VanderPlas* (O'Reilly Media)
   - **Bản đọc trực tuyến miễn phí:** [jakevdp.github.io/PythonDataScienceHandbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
   - **Kho Jupyter Notebooks:** [github.com/jakevdp/PythonDataScienceHandbook](https://github.com/jakevdp/PythonDataScienceHandbook)
   - **Nội dung:** Hướng dẫn thực hành chuyên sâu từ cơ bản đến nâng cao về NumPy, Pandas, Matplotlib và Scikit-Learn.

3. **Tài liệu Kỹ thuật Chính thức (Official Documentation)**:
   - **Pandas:** [pandas.pydata.org/docs](https://pandas.pydata.org/docs/)
   - **NumPy:** [numpy.org/doc/stable](https://numpy.org/doc/stable/)
   - **Matplotlib:** [matplotlib.org/stable](https://matplotlib.org/stable/)
   - **Seaborn:** [seaborn.pydata.org](https://seaborn.pydata.org/)

4. **R for Data Science (2nd Edition)** — *Hadley Wickham, Mine Çetinkaya-Rundel, Garrett Grolemund*
   - **Bản trực tuyến mở:** [r4ds.hadley.nz](https://r4ds.hadley.nz/)
   - **Nội dung:** Nguyên lý dữ liệu gọn gàng (Tidy Data), trực quan hóa dữ liệu và tư duy thẩm định phân tích dữ liệu.

---

## 2. Cấu trúc Quản lý Học liệu Cục bộ

- `source-map.json`: Bảng ánh xạ từng bài giảng của StudyHub với các chương và chủ đề kỹ thuật tương ứng.
- `scripts/verify-data-processing.py`: Script kiểm thử tự động toàn bộ mã Python, kết quả tính toán và ca biên trong bài giảng.
- `scripts/generate-data-processing-charts.py`: Script sinh lại các biểu đồ dữ liệu thực tế cho bài 12–14.
