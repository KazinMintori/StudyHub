# Rà soát bài tập Chương 26.61–26.88

## Phạm vi nguồn

- Bài 26.61–26.70: Trang in 874–875, PDF 894–895.
- Bài 26.71–26.80: Trang in 875–876, PDF 895–896.
- Bài 26.81–26.88: Trang in 876–877, PDF 896–897.
- Đã đọc phần sơ đồ trực tiếp trên trang PDF, gồm Hình P26.62, P26.63, P26.66, P26.67, P26.69–P26.75, P26.78, P26.81–P26.84.

## Kết quả kiểm tra

- Đã giữ đủ dải bài 26.61–80 và 26.81–88, mọi câu hỏi và tiểu mục, gồm toàn văn đoạn đọc MCAT và lựa chọn trả lời.
- Đã xác nhận bằng sơ đồ gốc các nhãn dễ bị OCR sai: $C=4{,}00\,\mathrm{\mu F}$ ở bài 26.70, $C=6{,}00\,\mathrm{\mu F}$ ở bài 26.72, $d=30{,}0\,\mathrm{\mu m}$ ở bài 26.69, $C=4{,}62\,\mathrm{\mu F}$ và $Q_0=6{,}90\,\mathrm{\mu C}$ ở bài 26.76, dữ liệu $q$ của bài 26.79 có đơn vị $\mathrm{\mu C}$, mật độ điện dung MCAT là $1\,\mathrm{\mu F/cm^2}$, và lựa chọn bài 26.87 là $100/\mathrm{\mu m^2}$.
- Đã lập hệ phương trình nút độc lập cho cầu nhiều vòng ở bài 26.62 và 26.67. Với bài 26.63, điện áp nút theo chiều mũi tên cho $\mathcal E=-108{,}75\,\mathrm{V}$ theo cực tính vẽ, nên nguồn cần đảo cực và có độ lớn $108{,}75\,\mathrm{V}$. Dòng qua nhánh $10\,\Omega$ là $2/3\,\mathrm{A}$, cho thời gian $13{,}5\,\mathrm{s}$. Cân bằng công suất nguồn và điện trở khớp. Mạch giới hạn công suất ở bài 26.66 được rút gọn theo hình và kiểm tra từng nhánh.
- Đã kiểm tra các giới hạn tụ ở $t=0^+$ và $t\to\infty$, bảo toàn điện tích ở các bài 26.71 và 26.75, cân bằng năng lượng ở 26.71, các tham số RC, hồi quy tuyến tính dữ liệu 26.79, mạng thang vô hạn và suy hao nhiều đoạn ở 26.83–26.85.
- Bộ tính độc lập [verify_chapter26_61_88.py](../verify_chapter26_61_88.py) chạy thành công bằng `python -I`. Nó kiểm tra nút điện, chiều dòng, công suất, năng lượng, hằng số thời gian, hồi quy và đáp án MCAT.
- Đã render 38 khối công thức bằng MathJax. Khối rộng nhất đo được $30{,}0\,\mathrm{ex}$ ở tệp 26.61–80 và $29{,}1\,\mathrm{ex}$ ở tệp 26.81–88. Không phát hiện lỗi phân tích cú pháp TeX.

## Điểm cần lưu ý khi tích hợp

- Bài 26.61 là bài ước lượng đường kính nhưng không chỉ định mật độ dòng điện. Lời giải nêu rõ giả thiết minh họa $5{,}0\,\mathrm{A/mm^2}$ và tính sụt áp theo cả hai lõi cấp nguồn của cáp.
- Số hạng một chiều trong câu (c) của bài 26.81 được in là $V_{in}=15{,}0\,\mathrm{V}$, trong khi câu yêu cầu $V_{out}=7{,}5\,\mathrm{V}$. Theo mô hình lý tưởng ở phần trước, $15{,}0\,\mathrm{V}$ cho đầu ra ngoài miền nguồn. Bản lời giải ghi rõ điểm không tương thích, nêu điểm phân cực cần thiết $1{,}35\,\mathrm{V}$ và vẫn tính độ lợi vi sai từ mô hình là $-10$.
- Các đường dẫn hình dùng tên chuẩn `img/young-26/hinh-p26-NN.png`. Ảnh sẽ được tạo khi bước tích hợp của chương hoàn tất.
- Chưa chạy VitePress build hoặc kiểm tra render trên site vì các tệp này còn là nguyên liệu thô và ảnh tích hợp chưa được tạo.
