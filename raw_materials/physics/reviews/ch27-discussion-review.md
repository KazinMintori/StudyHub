# Rà soát đối chiếu: Câu hỏi thảo luận Q27.1–Q27.18

## Phạm vi nguồn

Các câu hỏi Q27.1–Q27.12 nằm ở trang in 908 (PDF 928); Q27.13–Q27.18 ở trang in 909 (PDF 929). Đã render và xem trực tiếp cả hai trang, kể cả Hình Q27.12. Mọi đề bài và tiểu mục đã được giữ. Mỗi câu trong tệp `12-cau-hoi-thao-luan.md` có lời giải gấp ngay sau đề.

## Các điểm đã kiểm tra

- Quy tắc bàn tay phải dùng cho điện tích dương; điện tích âm làm lực đảo chiều.
- Hạt có vận tốc song song từ trường không chịu lực. Hạt có thành phần vận tốc dọc trường tạo chuyển động xoắn ốc. Vòng dây mềm nở ra khi mômen từ cùng chiều từ trường.
- Hình Q27.12 cho $\vec B$ theo $+x$. Tính tích có hướng từ mũi tên trong hình cho lực lần lượt tại $a,b,c,d,e$ là $-z,+y,0,0,-y$.
- Ước lượng Q27.13 nêu rõ giả thiết cho cận trên: Cột dài $10\,\mathrm{m}$, từ trường Trái Đất $5\times10^{-5}\,\mathrm{T}$, dòng cực đại $10^5\,\mathrm{A}$, cho lực không quá khoảng $50\,\mathrm{N}$ khi dây vuông góc trường.
- Q27.16 phân biệt động cơ cuộn kích từ nối cùng nguồn (đảo đồng thời $\vec\mu$ và $\vec B$, nên chiều mômen giữ nguyên) với động cơ nam châm vĩnh cửu (đảo dòng phần quay làm mômen đảo chiều). Cách diễn đạt này tránh khái quát hóa sai một cấu hình motor cho mọi loại motor.
- Q27.18 giải thích định tính bằng mật độ hạt tải: Với dòng, từ trường và kích thước cố định, $V_H$ tỉ lệ nghịch với mật độ hạt tải điện.

Script Python `raw_materials/physics/verify_chapter27_discussion.py` chạy đạt sau khi chuẩn hóa phép so sánh sai số theo độ lớn của đại lượng. Script kiểm tra các chiều véc-tơ trong hình, tính chất lực từ không sinh công, hai cấu hình động cơ ở Q27.16 và ước lượng Q27.13. MathJax render độc lập 23 công thức hiển thị và 270 công thức nội dòng trong hai tệp liên quan: Không có lỗi TeX, công thức hiển thị rộng hơn 30ex hay công thức nội dòng rộng hơn 38ex. Công cụ rà soát văn bản trả về 0 gợi ý. Liên kết hình Q27.12 trong bản dịch trỏ tới ảnh trang đã render để rà soát. Bản render hai trang nguồn cùng hình Q27.12 nằm trong `raw_materials/physics/reviews/ch27-guided-discussion-pages/`.
