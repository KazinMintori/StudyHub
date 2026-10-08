# Sổ nguồn và phạm vi biên soạn môn Cơ sở toán AI

Phiên bản biên soạn cập nhật ngày 08/10/2026, skill `studyhub-lecture` 7.2.0.

## Ranh giới nguồn

- Trang `https://courses.iaidev.com/math-4-AI/2627-1/` chỉ được đọc ở chỉ mục. Dùng số, tên và thứ tự Lecture 00–07; không mở các liên kết Notes, Slides hoặc bài tập để lấy nội dung.
- Sách chính: bản local `toan-cho-ai/docs/Convex_Optimization_Boyd.pdf`, 730 trang PDF. Trong phần đánh số trang Ả Rập, trang PDF = trang in + 14.
- Reference local: `Introduction_to_linear_optimization(Dimitris_Bertsimas).pdf`; dùng chương 2 cho đỉnh/cơ sở và điều kiện có đỉnh tối ưu. `Probabilistic Graphical Models Principles and Techniques, MIT Press, 2009.pdf` là scan phần lớn không có text; không lấy công thức không đọc chắc từ OCR.
- Người dùng đã cho phép bổ sung nguồn chính thức cho phần học sâu. Đã đối chiếu *Deep Learning* chương 8 (trang của tác giả), bài Adam (arXiv), AdaGrad (JMLR), Glorot–Bengio (PMLR), ghi chú BFGS của Madeleine Udell lưu trên Stanford và tài liệu CG của Jonathan Shewchuk trên CMU. Không gán công thức CG cho phụ lục C của CO.
- Ví dụ số và bài tập được tự biên soạn. Các ví dụ này không được gán là bài tập nguyên bản hoặc dữ liệu thực nghiệm của tác giả.

## Đơn vị nguồn → nơi đến

| Nguồn CO | Vai trò | Nơi đến | Lựa chọn độ sâu |
| --- | --- | --- | --- |
| Chương 1, §4.1 | Biến, mục tiêu, miền, infimum | Lecture 01, §1 | Phân biệt khả thi, bị chặn và đạt nghiệm; không dùng lịch sử Dido làm tiên quyết. |
| §1.2.1, §A.1, §A.4–A.5, §7.1, Ví dụ 7.1 | Ma trận, chuẩn, gradient, PSD, nhiễu Gauss | Lecture 00 | Mở từng bước Aᵀr; Gauss nhiều biến có giải thích ký hiệu và chỉ dẫn đọc tùy nhu cầu. |
| §2.1–2.3 | Tập lồi, affine, giao, ảnh/ảnh ngược | Lecture 01, §2; đọc thêm hình học | Tuyến chính chỉ giữ những phép dùng ngay; phối cảnh/ellipsoid ở trang bổ trợ. |
| §2.4–2.6 | Nón, phân tách/tựa, đối ngẫu nón, Pareto | `docs/toan-cho-ai/doc-them/hinh-hoc-tap-loi.md` | Không ép người học xử lý toàn bộ trước khi biết hàm lồi. |
| §3.1–3.2 | Hàm lồi, bậc nhất, bậc hai, quy tắc ghép | Lecture 01, §3–4 | Lý do của cận dưới bậc nhất nằm ngoài hộp gập. |
| §4.2.2–4.2.3 | Cục bộ/toàn cục, tối ưu có biên | Lecture 01, §5 | Giữ cả miền lồi và hàm lồi trong chứng minh. |
| §4.4, §7.1 (tr. 354–355) | QP điều khiển một bước, logistic | Lecture 01, §7 | Mô hình điều khiển tự đặt dựa vào QP; logistic dựa vào mô hình sách và chứng nhận Hessian. |
| §4.2–4.6, §6.3 | Dạng chuẩn, LP/QP/QCQP/SOCP/SDP/GP, điều chuẩn | Lecture 02 | Có chiều dấu, biến phụ và cách thu hồi; phân biệt hiện dạng chuẩn với miền lồi. |
| §5.1–5.2 | Lagrangian, cận dưới, hàm g, Slater | Lecture 03, §1–4 | Tính x trước, nhân tử sau; giải thích nội tương đối trước khi dùng. |
| §5.5–5.6, Ví dụ 5.1 | KKT, gap, độ nhạy, QP đẳng thức | Lecture 03, §5–7 | Giữ điều kiện cần/đủ và dấu nhân tử. |
| §9.2–9.3 | Hướng, line search, gradient | Lecture 04, §1–2 | Bảng trial đầy đủ và code chạy được. |
| §9.5–9.6 | Newton, decrement, self-concordance | Lecture 04, §3–4 | Giữ cơ chế và định nghĩa; cận chi tiết số vòng lặp chỉ dẫn về sách. |
| §10.2–10.3 | Newton–KKT khả thi/chưa khả thi | Lecture 04, §5–6 | Đo phần dư chung; không ép loss giảm tại điểm chưa khả thi. |
| §9.3 + nguồn học sâu bổ sung | SGD, momentum, Nesterov, Glorot | Lecture 05 | Tách nhiễu gradient khỏi động lực vận tốc; nêu giả định lấy mẫu và tuyến tính hóa. |
| Phụ lục C, §9.5 + nguồn bổ sung | AdaGrad, RMSProp, Adam, CG, BFGS | Lecture 06 | Có trạng thái và hai bước Adam, giả thiết SPD/độ cong BFGS, không xếp hạng mạng sâu từ mô phỏng. |
| §4.3, §8.7 (tr. 436–438) + Bertsimas §2.2–2.6 | LP/cơ sở và Bellman trên DAG | Lecture 07 | Min tự biên soạn; max tái hiện đệ quy (8.30). Kết nối với LP tiềm năng. |

## Cách dùng văn phong của giáo trình

Đã đọc trực tiếp các chương 2–5 và 8–10 của bản PDF, gồm cả trang mở đầu chương, định nghĩa, ví dụ và phần chuyển sang thuật toán. Notes không sao chép câu tiếng Anh. Chúng giữ nhịp lập luận của sách: khai báo đối tượng và giả thiết; phát biểu định nghĩa hoặc công thức; giải thích ký hiệu ngay sau đó; rồi mới nêu hệ quả, ví dụ hoặc giới hạn.

StudyHub bổ sung các bước mà sách có thể để người đọc tự suy ra: giải thích mục đích của phép biến đổi, chỉ ra giả thiết được dùng ở dòng nào, và cho một bài nhỏ để tự làm. Không biến sự bổ sung này thành chuỗi tiêu đề hỏi tu từ. Tiêu đề mặc định gọi đúng đối tượng hoặc kết quả; câu hỏi chỉ dùng khi phần đó thực sự trả lời một vướng mắc.

Thuật ngữ được chọn theo lĩnh vực. Cùng từ “tham số” có trang riêng cho mô hình toán học và cho định nghĩa hàm trong lập trình; liên kết tự động chọn nghĩa theo học phần. Tên tiếng Anh được giữ khi đó là tên tra cứu chính hoặc bản dịch chưa ổn định, chẳng hạn likelihood, self-concordant, Adam và BFGS.

## Kiểm kê minh họa sử dụng

Mọi minh họa lấy ý toán từ CO được dựng bằng chương trình. Không chép ảnh sách. Các tọa độ/hàm nhỏ do người biên soạn đặt được ghi cạnh hình; không tuyên bố sao y dữ liệu nguyên bản.

| Quan hệ trong sách | Cách tái hiện | Vị trí |
| --- | --- | --- |
| Hình 2.1, tr. 22: đoạn và đường affine | `MathLab type="segment"`, cùng quy tắc θA+(1−θ)B | Lecture 01 |
| Hình 3.1, tr. 67: dây cung trên đồ thị lồi | `MathLab type="chord"`, x²/−x² và phép so giá trị | Lecture 01 |
| §5.1.3/Hình 5.1: cận Lagrange | `MathLab type="dual"`, g(λ)=λ−λ²/4 | Lecture 03 |
| Hình 9.1, tr. 465: backtracking | Bảng từng trial và code Python tính chính xác | Lecture 04 |
| §9.3/§9.5: đường đồng mức và bước giảm | `MathLab type="optimizer"`, hàm toàn phương có κ chỉnh được | Lecture 04–06 |
| §4.3: hình học LP | `MathLab type="lp"`, đổi mục tiêu trên đa diện có bốn đỉnh | Lecture 07 |
| §8.7, (8.30): đệ quy max trễ trên DAG | `MathLab type="bellman"`, chuyển min/max và tính ngược từng nút | Lecture 07 |

## Những phần không đưa vào tuyến Notes chính

Không tuyên bố bao phủ toàn bộ sách. §3.3–3.6 (liên hợp, giả lồi, log-lồi, bất đẳng thức tổng quát cho hàm) không là tiên quyết của tuyến tám lecture này. Chương 6–8 chỉ dùng các mô hình đã nêu; không viết lại mọi ứng dụng. Chương 11 (phương pháp điểm trong) chưa thuộc lecture của chỉ mục, nên chưa thêm thành lecture thứ chín. Các cận hội tụ chi tiết, phân tích số và bài tập nguyên bản được dẫn về sách, không nén thành khẩu hiệu.

Các ví dụ cũ về đa thức lượng giác với điều kiện liên tục theo t và XOR không dùng trong tuyến chính: chúng thêm đối tượng/nguồn phụ trước khi sinh viên dùng được phép kiểm lồi. Hình học nón, phối cảnh, Pareto giữ ở trang đọc thêm. Đoạn khẳng định tần suất đề thi và lịch sử không được giữ khi thiếu nguồn xác minh.

## Kiểm tra tái lập

```text
node --test scripts/tests/math-ai.test.mjs
python scripts/verify-math-ai.py
node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs toan-cho-ai/<slug>
python .claude/skills/studyhub-lecture/scripts/review_teaching_text.py docs/toan-cho-ai/bai-giang/<slug>.md
npm run ci:build
```

Kiểm tra trình duyệt: `scripts/verify-math-ai-browser.mjs`, `QA_URL` là địa chỉ server local, `CHROME_PATH` có thể chỉ Chrome có sẵn. Báo cáo và screenshot trong `qa/math-ai/` (được gitignore). Không commit text trích xuất nguyên sách trong `raw_materials/extracted/`.

Kết quả nghiệm thu: 8 lecture kiểm tích hợp không lỗi/cảnh báo; 8 Notes rà giọng không có gợi ý; 7 kiểm toán chương trình và các ví dụ số/Python qua. Build cuối thành công. Sau khi giao diện chung hoàn tất, bản build cố định qua 17 nhóm QA, gồm cả 8 lecture ở 375/768/1440px sáng/tối; không tràn trang, lỗi JavaScript, lỗi công thức MathJax hoặc thiếu asset CSS/JS/font. Đã nhìn screenshot các hình và trang môn. Kiểm tự động không được coi là đánh giá kết quả học của sinh viên.
