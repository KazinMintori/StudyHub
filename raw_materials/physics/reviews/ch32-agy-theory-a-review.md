# Chương 32: Kiểm kê và rà soát lý thuyết phần A (Mục 32.1–32.3)

Ngày: 2026-10-15.
Tác vụ: physics32-agy-a (Theory A: Lời mở đầu và các mục 32.1–32.3).
Trạng thái: Hoàn thành 100% phần việc được giao, đã kiểm tra số học và cú pháp bằng Python, đối chiếu trực tiếp với trang in và PDF nguồn. Sẵn sàng tích hợp.

## 1. Nguồn gốc và phạm vi tài liệu

Nguồn dữ liệu là giáo trình chuẩn *University Physics with Modern Physics* (tái bản lần thứ 15) của Young & Freedman tại tệp `raw_materials/physics/source/young-freedman-15.pdf` (mã SHA256: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`).

- **Phạm vi trang**: Từ trang in 1048 đến 1061, tương ứng trang PDF 1068 đến 1081.
- **Ranh giới kết thúc**: Dừng nghiêm ngặt tại cuối mục 32.3, ngay trước tiêu đề mục 32.4 (Năng lượng và động lượng trong sóng điện từ) ở trang PDF 1081.

| Đơn vị nguồn | Tập tin phân mảnh | Nội dung sư phạm và các thành phần học thuật |
| :--- | :--- | :--- |
| Mở đầu chương | `00-mo-dau.md` | Lời dẫn nhập về bản chất điện từ của ánh sáng, ảnh mở đầu `mo-dau-32.png`, Câu hỏi mở đầu với đầy đủ năm phương án lựa chọn kèm giải thích chi tiết, năm mục tiêu học tập (32.1–32.5) và tám chủ đề kiến thức nền cần ôn lại. |
| Mục 32.1 | `01-maxwell-song-dien-tu.md` | Lịch sử thống nhất điện, từ và ánh sáng của Maxwell; hệ bốn phương trình Maxwell cơ bản (29.18–29.21); cơ chế bức xạ điện từ từ điện tích chuyển động có gia tốc; thí nghiệm lịch sử của Hertz và định nghĩa mét chuẩn; thang sóng điện từ (từ sóng vô tuyến đến tia gamma); Bảng 32.1 dải phổ ánh sáng nhìn thấy; Hình 32.1–32.4; Câu hỏi tự kiểm tra 32.1. |
| Mục 32.2 | `02-song-phang-van-toc-anh-sang.md` | Khái niệm mặt sóng phẳng; chứng minh tính chất sóng ngang từ hai định luật Gauss; áp dụng định luật cảm ứng Faraday chứng minh $E = cB$; áp dụng định luật Ampere mở rộng chứng minh $B = \epsilon_0\mu_0 c E$; suy diễn công thức vận tốc ánh sáng trong chân không $c = 1/\sqrt{\epsilon_0\mu_0}$; sáu đặc tính nền tảng của sóng điện từ; thiết lập vi phân phương trình sóng cấp hai cho $E_y$ và $B_z$; Hình 32.5–32.11; Câu hỏi tự kiểm tra 32.2. |
| Mục 32.3 | `03-song-hinh-sin.md` | Xấp xỉ sóng phẳng từ sóng cầu ở khoảng cách xa; biểu diễn toán học hàm sóng điều hòa $E_y(x,t)$ và $B_z(x,t)$ cùng dạng vector; phân biệt số sóng $k$ với vector đơn vị $\hat{k}$; quan hệ biên độ $E_{\max} = c B_{\max}$; cấu hình sóng truyền theo chiều âm trục tọa độ; Chiến lược giải bài toán 32.1; Ví dụ 32.1 (laser khí $\mathrm{CO_2}$); sóng điện từ trong môi trường điện môi ($v = c/\sqrt{K K_{\text{m}}}$); chiết suất quang học $n$; tính phụ thuộc tần số của hằng số điện môi (hàm điện môi); Ví dụ 32.2 (ánh sáng natri trong kim cương và sóng FM trong ferit); Hình 32.12–32.16; Câu hỏi tự kiểm tra 32.3. Dừng trước mục 32.4. |

## 2. Kiểm kê số lượng thành phần

- **Phương trình đánh số**: Đầy đủ 22 nhãn phương trình theo nguyên tác giáo trình ((29.18)–(29.21), (32.1)–(32.9), (32.10)–(32.19), (32.20)–(32.22)). Mỗi nhãn chỉ xuất hiện duy nhất một lần tại phần giảng giải.
- **Ví dụ trong bài giảng**: Đầy đủ hai ví dụ lớn (Ví dụ 32.1 và Ví dụ 32.2) với cấu trúc ba phần sư phạm mẫu mực: Phân tích và thiết lập bài toán, Thực thi giải toán, và Đánh giá kết quả.
- **Câu hỏi kiểm tra**:
  - Một Câu hỏi mở đầu với năm phương án lựa chọn và lời giải thích cơ chế vật lý gập trong `<details>`.
  - Ba Câu hỏi tự kiểm tra (Tự kiểm tra 32.1, 32.2, 32.3) đặt ngay sau mỗi mục tương ứng, giữ nguyên câu hỏi trực diện và chỉ gập phần đáp án, giải thích.
- **Hình ảnh trích xuất**: Đầy đủ 17 hình ảnh trích xuất trực tiếp bằng PyMuPDF từ bản in PDF gốc với tọa độ pixel chuẩn xác, không vẽ lại, không biến dạng:
  - Một ảnh ứng dụng mở đầu: `mo-dau-32.png`.
  - Mười sáu hình minh họa bài giảng: `hinh-32-01.png` đến `hinh-32-16.png`.
  - Tệp chú thích song ngữ hoàn chỉnh: `docs/.vitepress/physics32-theory-a-image-annotations.mjs` với từng cặp chú thích `[Giải thích tiếng Việt, English label]`.
  - Ghi chú: Không xuất hiện hình vẽ trong các câu hỏi tự kiểm tra của phần nguồn, do đó không tạo các tệp hình giả mạo (`tu-kiem-32-01.png` đến `tu-kiem-32-03.png`).

## 3. Các điểm làm rõ học thuật và sư phạm

1. **Bản chất sóng ngang từ định luật Gauss**: Khẳng định rõ ràng rằng việc không tồn tại thành phần dọc $E_x$ hay $B_x$ là hệ quả tất yếu của hai định luật Gauss cho điện trường và từ trường trên mặt kín hình hộp chữ nhật cắt qua mặt sóng phẳng.
2. **Quy tắc bàn tay phải và mối quan hệ vector**: Vector vận tốc truyền sóng luôn cùng hướng với tích có hướng $\vec{E} \times \vec{B}$. Khi sóng đổi chiều truyền sang $-x$ (như trong Ví dụ 32.1), nếu $\vec{E}$ hướng theo $+z$ ($\hat{k}$) thì $\vec{B}$ bắt buộc phải hướng theo $+y$ ($\hat{j}$) vì $\hat{k} \times \hat{j} = -\hat{i}$.
3. **Ý nghĩa của dấu trong hàm sóng**: Sóng truyền theo chiều dương $+x$ có dạng đối số điều hòa $kx - \omega t$, trong khi sóng truyền theo chiều âm $-x$ có dạng $kx + \omega t$.
4. **Giả thiết môi trường vật chất**: Lý thuyết lan truyền trong chất điện môi áp dụng cho môi trường tuyến tính, đồng nhất và đẳng hướng.
5. **Hằng số điện môi biến thiên theo tần số (Hàm điện môi)**: Nêu bật bản chất vật lý vì sao nước có hằng số điện môi tĩnh rất cao ($80{,}4$) do các phân tử nước phân cực tái định hướng theo điện trường tĩnh, nhưng ở tần số quang học của ánh sáng nhìn thấy ($f \approx 5 \times 10^{14}\,\mathrm{Hz}$), các phân tử không thể xoay kịp và $K$ chỉ còn khoảng $1{,}8$.
6. **Mở bước khó trong phương trình vi phân sóng**: Trình bày rõ ràng bước lấy đạo hàm riêng hỗn hợp của hai phương trình vi phân cấp một suy ra từ Faraday và Ampere: Nhờ tính đối xứng đạo hàm hỗn hợp ($\partial^2 B_z / \partial x \partial t = \partial^2 B_z / \partial t \partial x$), ta khử được một trường để nhận được phương trình vi phân sóng cấp hai thuần túy cho trường còn lại.

## 4. Chuẩn mực định dạng và văn phong

- **Văn phong giáo sư, chính danh**: Không sử dụng các cụm từ thụ động như "theo sách", "sách dùng", "dịch từ giáo trình". Toàn bộ nội dung là bài giảng độc lập, liền mạch, trực diện và giàu tính thuyết phục.
- **Quy tắc dấu câu tiếng Việt**:
  - 100% các từ đứng ngay sau dấu hai chấm (`:`) trong toàn bộ bài giảng đều được viết hoa chữ cái đầu tiên.
  - Hạn chế tối đa và loại bỏ hoàn toàn dấu chấm phẩy (`;`) trong các câu văn xuôi diễn giải, thay thế bằng các liên từ tiếng Việt chuẩn xác (*và, nhưng, đồng thời, cụ thể là, kéo theo, dẫn đến*).
  - Không lạm dụng dấu gạch ngang dài (`—` hoặc `--`) chêm xen giữa câu.
- **Định dạng toán học chống tràn (Zero Math Scrollbars)**:
  - 100% các khối công thức hiển thị đều sử dụng hai dấu `$$` đặt trên dòng độc lập.
  - Mọi công thức hiển thị dài hoặc chuỗi biến đổi đều được bẻ dòng bằng môi trường `\begin{aligned} ... \end{aligned}`, ngắt dòng bằng `\\` và căn lề bằng `&`. Không có chuỗi đẳng thức trải dài trên một dòng.
  - Độ rộng các dòng hiển thị đều nằm trong giới hạn an toàn 15–25ex, loại bỏ hoàn toàn nguy cơ xuất hiện thanh cuộn ngang trên màn hình di động (kể cả độ phân giải hẹp 360px).
  - Cú pháp toán học chuẩn xác: Không sử dụng `\vert{}` hay `\Vert{}`.

## 5. Bằng chứng kiểm tra số học và kiểm thử tự động

Tệp kiểm tra tự động `raw_materials/physics/verify_chapter32_theory_a.py` đã thực hiện toàn diện các phép kiểm tra:

1. **Hằng số cơ bản và vận tốc ánh sáng**:
   - $c_{\text{calc}} = 1/\sqrt{\epsilon_0 \mu_0} = 299\,792\,458{,}08\,\mathrm{m/s}$ trùng khớp với giá trị chuẩn $299\,792\,458\,\mathrm{m/s}$ (sai số tương đối $< 10^{-8}$).
   - Giá trị gần đúng bốn chữ số: $1/\sqrt{(8{,}854 \times 10^{-12})(1{,}257 \times 10^{-6})} = 2{,}998 \times 10^8\,\mathrm{m/s}$.
2. **Ví dụ 32.1 (Laser khí $\mathrm{CO_2}$)**:
   - $\lambda = 10{,}6\,\mu\mathrm{m} \implies k = 5{,}93 \times 10^5\,\mathrm{rad/m}$.
   - $E_{\max} = 1{,}5 \times 10^6\,\mathrm{V/m} \implies B_{\max} = 5{,}0 \times 10^{-3}\,\mathrm{T} = 5{,}0\,\mathrm{mT}$.
   - $\omega = ck = 1{,}78 \times 10^{14}\,\mathrm{rad/s}$, $f = c/\lambda = 2{,}83 \times 10^{13}\,\mathrm{Hz}$.
   - Kiểm tra tích có hướng: $\hat{k} \times \hat{j} = -\hat{i}$ (đúng chiều lan truyền $-x$).
   - Kiểm tra phương trình Faraday vi phân: Sai số phần dư của $k E_{\max} - \omega B_{\max}$ đạt độ chính xác tương đối $< 10^{-10}$.
3. **Ví dụ 32.2 (Sóng điện từ trong vật liệu)**:
   - Câu (a) Kim cương: $f = 5{,}09 \times 10^{14}\,\mathrm{Hz}$, $\lambda_{\text{vacuum}} = 589\,\mathrm{nm}$, $v = 1{,}24 \times 10^8\,\mathrm{m/s} = 0{,}414c$, $\lambda_{\text{diamond}} = 244\,\mathrm{nm}$.
   - Câu (b) Ferit: $f = 90{,}0\,\mathrm{MHz}$, $\lambda_{\text{vacuum}} = 3{,}33\,\mathrm{m}$, $v = 3{,}00 \times 10^6\,\mathrm{m/s} = 0{,}010c$, $\lambda_{\text{ferrite}} = 3{,}33\,\mathrm{cm}$.
4. **Tỉ số vận tốc ánh sáng trong nước**: $1/\sqrt{1{,}8} \approx 0{,}745$, chậm hơn $25{,}5\%$ so với chân không.
5. **Tự kiểm tra 32.2**: Ba tích có hướng vector $\hat{i} \times \hat{j} = \hat{k}$, $(-\hat{k}) \times (-\hat{i}) = \hat{j}$, $\hat{k} \times \hat{j} = -\hat{i}$ đều được kiểm chứng chính xác bằng NumPy.
6. **Kiểm tra tệp và cú pháp**:
   - 17/17 tệp ảnh PNG tồn tại và hợp lệ.
   - 4/4 tệp phân mảnh Markdown tồn tại và tuân thủ tuyệt đối quy định cú pháp, không còn bất kỳ cảnh báo định dạng hay dấu câu nào.
   - Kết quả xuất ra tệp `qa/physics/chapter32/theory-a-numeric-checks.json` với trạng thái `"status": "passed"`.
