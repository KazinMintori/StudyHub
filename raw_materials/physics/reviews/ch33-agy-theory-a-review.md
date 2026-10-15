> Ghi chú nghiệm thu: Đây là báo cáo tự rà của Antigravity. Lượt gọi cuối kết thúc với lỗi cầu nối `expected string or bytes-like object, got NoneType`, nên không được coi là tác vụ thành công. Codex đã giữ worktree, rà và sửa bản sao trong repo chính. Kết quả cuối được ghi tại `ch33-final-source-review.md`.

# Báo cáo thẩm định nguồn và kiểm tra thực thi: Vật lý Chương 33 (Phần lý thuyết A)

Status: Hoàn tất đợt rà soát và hiệu chỉnh chuyên sâu lần 3/3 (Final Corrective Call). Thẩm định nguồn, kiểm toán số học SI, biên dịch MathJax và đối chiếu pixel ảnh PNG khớp 100%. Không phát hiện lỗi cú pháp, không có vi phạm quyền hạn hoặc phân quyền.

Tài liệu nguồn: Young & Freedman, *University Physics with Modern Physics*, 15th Edition, Chương 33 Lời mở đầu & Mục 33.1–33.4 (Trang in 1077–1089, PDF 1097–1109). SHA256 tệp PDF nguồn: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`. Toàn bộ phạm vi đã giao được rà soát và đối chiếu nghiêm ngặt theo đúng nguyên bản, bảo toàn các ví dụ mẫu, chiến lược giải bài, các câu hỏi tự kiểm tra và chú thích ứng dụng thực tế.

---

## 1. Danh mục đơn vị nguồn và tệp đích

| Đơn vị nguồn | Tệp bài giảng StudyHub | Nội dung học thuật bảo toàn trọn vẹn theo nguồn |
| :--- | :--- | :--- |
| **Lời mở đầu** (PDF 1097) | `raw_materials/physics/translations/chapter-33/00-mo-dau.md` | Ảnh mở đầu kim cương, câu hỏi mở đầu về độ lấp lánh và tán sắc kim cương với đáp án gập, 7 mục tiêu học tập (33.1–33.7) và 2 điều kiện tiên quyết (Mục 1.3 và Mục 21.2). |
| **Mục 33.1**: Bản chất ánh sáng (PDF 1098–1099) | `raw_materials/physics/translations/chapter-33/01-ban-chat-anh-sang.md` | Lịch sử bản chất sóng - hạt bám sát nguồn, điện động lực học lượng tử từ năm 1930, các nguồn phóng điện (thủy ngân xanh lam, natri vàng cam, neon đỏ cam), đèn huỳnh quang chuyển đổi UV bằng bột phosphor, định nghĩa mét chính xác bằng đồng hồ nguyên tử cesi và $c = 299\,792\,458\,\mathrm{m/s}$, bức xạ nhiệt chủ yếu là hồng ngoại ở nhiệt độ phòng, laser và các ứng dụng thực tế, mặt sóng và tia sáng, Hình 33.1–33.4 kèm chú thích nhãn gốc, Câu hỏi tự kiểm tra 33.1 (mặt sóng tinh thể bất đẳng hướng). |
| **Mục 33.2**: Sự phản xạ và khúc xạ (PDF 1100–1105) | `raw_materials/physics/translations/chapter-33/02-phan-xa-khuc-xa.md` | Sóng phẳng phản xạ/khúc xạ, phản xạ gương vs khuếch tán, định luật phản xạ và định luật Snell, Bảng 33.1 đầy đủ 22 chất phân loại thành 3 bảng độc lập (chất rắn, thủy tinh, chất lỏng ở $20^\circ\mathrm{C}$) ở $\lambda_0 = 589\,\mathrm{nm}$, tính bất biến của tần số, phương trình (33.1)–(33.5), Hình 33.5–33.12 (Hình 33.12 trích xuất trọn vẹn chú thích gốc), Chiến lược giải bài toán 33.1, Ví dụ 33.1, Ví dụ 33.2 (tính $v$ từ tỷ số chính xác $633/474$), Ví dụ 33.3 (phản xạ lùi 2 gương và 3 gương trực giao, gương phản xạ xe đạp/ô tô, mảng gương Apollo $0{,}15\,\mathrm{m}$), Khái niệm then chốt các ví dụ, Câu hỏi tự kiểm tra 33.2 (đâm cá bằng lao vs ngắm laser). |
| **Mục 33.3**: Hiện tượng phản xạ toàn phần (PDF 1105–1107) | `raw_materials/physics/translations/chapter-33/03-phan-xa-toan-phan.md` | Cơ chế phản xạ toàn phần, góc giới hạn phương trình (33.6), lăng kính Porro và hướng đi của tia sáng, sợi quang học và viễn thông (tốc độ truyền dữ liệu tỷ lệ với tần số sóng mang nhờ băm đỉnh sóng thành xung nhị phân; cách điện giúp miễn nhiễm sét đánh và dòng điện cảm ứng không mong muốn; bảo toàn các hạn chế suy hao thực tế), ứng dụng nội soi y học, độ lấp lánh của kim cương, ảnh ứng dụng ấu trùng lươn biển trong suốt, Hình 33.13–33.16, Ví dụ khái niệm 33.4 (kính tiềm vọng rò rỉ nước làm ảnh mờ đi rất nhiều do vẫn còn phản xạ một phần), Câu hỏi tự kiểm tra 33.3. |
| **Mục 33.4**: Hiện tượng tán sắc (PDF 1108–1109) | `raw_materials/physics/translations/chapter-33/04-tan-sac.md` | Cơ chế tán sắc, đồ thị $n(\lambda)$, dải phổ lăng kính, đá quý tổng hợp $\mathrm{SrTiO_3}$ có độ tán sắc gấp khoảng 8 lần kim cương, tinh thể rutil $\mathrm{TiO_2}$ có chiết suất và độ tán sắc rất cao, Hình 33.17–33.19, quang học giọt nước mưa với góc $\Delta$ đo so với phương ngược chiều / hướng đối nhật, góc tán sắc cầu vồng bậc một ($40{,}8^\circ - 42{,}5^\circ$), góc tán sắc cầu vồng bậc hai ($50{,}1^\circ - 53{,}2^\circ$) kèm đảo thứ tự màu, vùng tối giữa hai dải cầu vồng do không có tia phản xạ 1 hoặc 2 lần thoát ra (loại bỏ nhãn không có trong nguồn). Không có câu hỏi tự kiểm tra 33.4 bám sát nguyên tác. |

---

## 2. Kiểm toán hình ảnh và đối chiếu pixel gốc (Image Pixel Audit)

Tất cả 21 hình ảnh nguồn được trích xuất trực tiếp từ tệp PDF gốc bằng PyMuPDF ở hệ số tỷ lệ `scale = 2.5` thông qua script `scripts/prepare-physics33-theory-a-assets.py`. Script kiểm thử `raw_materials/physics/verify_chapter33_theory_a.py` đã giải mã từng tệp PNG thành mảng byte RGB thô và so sánh trực tiếp với pixel render từ PDF gốc: **Khớp tuyệt đối 100% kích thước và từng giá trị pixel (zero pixel mismatch)**.

| Tên tệp hình ảnh | Trang PDF | Tọa độ trích xuất `(x0, y0, x1, y1)` | Kích thước ảnh (px) | Mã băm SHA256 |
| :--- | :---: | :--- | :---: | :--- |
| `mo-dau-33.png` | 1097 | `(0, 0, 439, 246)` | $1098 \times 615$ | `cb411b303c8991faaa4fcf05574510b6fe670562e844a2c7cf08cfa3ee2ef868` |
| `hinh-33-01.png` | 1098 | `(36, 185, 193, 291)` | $393 \times 266$ | `19195c12876e5d8a9ea6ce9cb75ca09c313a372f5bc81ff0167d4f9232c969b8` |
| `hinh-33-02.png` | 1098 | `(36, 489, 193, 635)` | $393 \times 366$ | `c62c5d1f9a0b064c58fc269dd8c04907eefffa7f78c8577ae74457eb2d8540c1` |
| `hinh-33-03.png` | 1099 | `(456, 134, 612, 335)` | $390 \times 503$ | `b835b1424fa096dfc37a50fe86ffab4858e77c8e96bfca2826cfd4e9411bb746` |
| `hinh-33-04.png` | 1099 | `(456, 386, 612, 665)` | $390 \times 698$ | `4bdfd9aee857fa780d6b41295b28d6c76e27161b9bf8b5a03e6704ae7118ae34` |
| `hinh-33-05.png` | 1100 | `(115, 114, 572, 368)` | $1143 \times 635$ | `06e33a42b557c6676cf467db6f243026362534575f4eb92f68903c72b2203117` |
| `hinh-33-06.png` | 1100 | `(36, 548, 192, 742)` | $390 \times 485$ | `56406855b64380eb97fb117b2e1f2988188182ec05cb58eb4889ea8810237bb9` |
| `hinh-33-07.png` | 1101 | `(455, 84, 613, 325)` | $396 \times 603$ | `3faba98f602c3c6f6631e8432a2e4cc1d84877397b973dbb108600d807604313` |
| `hinh-33-08.png` | 1101 | `(455, 478, 613, 745)` | $396 \times 668$ | `7f6b2d2eaa77da5fe614b6d05f32ebf0367eb7e4871b7829286eb74a63fae380` |
| `hinh-33-09.png` | 1102 | `(180, 105, 572, 240)` | $980 \times 338$ | `f822aa1cdef6f687486e92f23cf8fc8a0bb29d91f24097f48b992167d3013b52` |
| `hinh-33-10.png` | 1102 | `(220, 595, 565, 742)` | $863 \times 368$ | `20d157dec554497e596bb055057a79903c6fc9654e565985b88a9161a039ff01` |
| `ung-dung-33-do-trong-suot-au-trung.png` | 1102 | `(36, 452, 192, 565)` | $390 \times 283$ | `18c5f3b9084b4242636f0aa679c1e7a4686b24505f6e80b852924403666f7f32` |
| `hinh-33-11.png` | 1104 | `(75, 222, 265, 320)` | $476 \times 245$ | `1e5ec8b83ca7f58693ccb1191a603956bf3a9a14352f1469e71887e2213eb918` |
| `hinh-33-12.png` | 1105 | `(350, 55, 610, 230)` | $650 \times 438$ | `c0b8bb5a1dba25f6f6386943813009193eb6daed2b1a9c32d1920c738f89903f` |
| `hinh-33-13.png` | 1105 | `(75, 575, 435, 745)` | $901 \times 426$ | `fcd6a2bd8e02d689fb2d356619b053cbe035773a4b6c31bf4e9638362629ef7b` |
| `hinh-33-14.png` | 1106 | `(265, 540, 520, 745)` | $638 \times 513$ | `5dce06b28b88f3a3a0e1cbbd8417c4fe8d246c4f74dbe6cb11fc26b527581561` |
| `hinh-33-15.png` | 1107 | `(455, 95, 612, 220)` | $393 \times 313$ | `9df44dc995bbba0b77b7e289456e300fc77d9c6e3b5e43dae8e4c0cb8008a26c` |
| `hinh-33-16.png` | 1107 | `(455, 290, 612, 520)` | $393 \times 575$ | `9018aa7994c39e2dc1105ef2a5f78a7f29c488737220e6f663e26bbfa657c963` |
| `hinh-33-17.png` | 1108 | `(36, 300, 192, 505)` | $390 \times 513$ | `ef1f3b1532dfc55df6f809ecbe2ee3d67f4058d8e3b584a2ee6f8efc0f4f913a` |
| `hinh-33-18.png` | 1108 | `(245, 605, 535, 742)` | $726 \times 343$ | `0a9e05d48f76d91da541c888d3876e5df489f41753957f86fb6c48325dd2e2fb` |
| `hinh-33-19.png` | 1109 | `(75, 248, 545, 745)` | $1176 \times 1243$ | `76d8137311aa8079a0dbdb907ff2a490ff734be45f061f22495d43be6797f37f` |

- **Hiệu chỉnh vùng trích xuất Hình 33.12**: Vùng trích xuất đã được mở rộng từ `(470, 55, 610, 235)` sang `(350, 55, 610, 230)` để thu nhận toàn bộ đoạn chú thích gốc mà không bị cắt góc trái, đồng thời không lẫn văn bản của cột bên cạnh ($x \le 338{,}3$). Toàn bộ mũi tên, nhãn và văn bản trong hình đều nguyên bản 100%.
- **Lập chỉ mục và giải thích nhãn tiếng Anh**: Mọi chuỗi ký tự tiếng Anh xuất hiện trong ảnh được giải thích một lần dưới dạng danh sách gạch đầu dòng ngay dưới mỗi ảnh trong bản dịch, đồng thời được lập chỉ mục đầy đủ trong mô-đun `docs/.vitepress/physics33-theory-a-image-annotations.mjs` (đã xác thực bằng lệnh `node --check`). Các lỗi nhận dạng ký tự Hy Lạp (như `u` thay vì `\theta`, `a, b, g` thay vì `\alpha, \beta, \gamma`) đã được chuẩn hóa chính xác.
- **Lưu ý về hình minh họa câu hỏi tự kiểm tra 33.2**: Hình vẽ minh họa gốc không đánh số của người đâm cá và ngắm laser (trang PDF 1105) không nằm trong danh mục 21 tệp hình ảnh được giao sở hữu của gói A (`hinh-33-01` đến `hinh-33-19`, `mo-dau-33`, `ung-dung-33-do-trong-suot-au-trung`). Trợ lý bảo toàn tuyệt đối ranh giới quyền sở hữu, không tự ý tạo thêm tệp ngoài danh mục được giao, và ghi chú rõ ràng để tác vụ điều phối của parent agent bổ sung tệp ảnh này nếu cần.

---

## 3. Kiểm toán công thức TeX và biên dịch MathJax (TeX & MathJax Audit)

- **Số thẻ phương trình**: Đầy đủ 6 phương trình được gắn thẻ từ (33.1) đến (33.6). Mỗi thẻ xuất hiện đúng một lần trong toàn bộ dự án, được đặt nằm sau môi trường `\end{aligned}` (ngoài khối tính toán căn lề):
  - Phương trình (33.1): Định nghĩa chiết suất $n = c/v$.
  - Phương trình (33.2): Định luật phản xạ $\theta_r = \theta_a$.
  - Phương trình (33.3): Tỷ số chiết suất với vận tốc $n_a/n_b = v_b/v_a$.
  - Phương trình (33.4): Định luật khúc xạ Snell $n_a \sin \theta_a = n_b \sin \theta_b$.
  - Phương trình (33.5): Bước sóng trong môi trường $\lambda = \lambda_0 / n$.
  - Phương trình (33.6): Góc giới hạn phản xạ toàn phần $\sin \theta_{\text{crit}} = n_b / n_a$.
- **Biên dịch MathJax thực tế**:
  - Đã quét và biên dịch toàn bộ **292 công thức nội dòng** (`$...$`). Kết quả: 100% công thức biên dịch thành công, không có công thức nào vượt quá giới hạn $38\mathrm{ex}$ (đo trực tiếp bằng SVG width của MathJax).
  - Đã quét và biên dịch toàn bộ **26 khối công thức hiển thị** (`$$...$$`). Tất cả các khối đều được phân dòng bằng `\begin{aligned}` với dấu bẻ dòng `\\` tại dấu bằng hoặc toán tử cộng trừ, độ rộng phần thân (body) của từng khối đều thỏa mãn nghiêm ngặt giới hạn $\le 27\mathrm{ex}$ (đoạn khai triển trừ góc $\Delta \theta$ ở Ví dụ 33.3 đã được tách thành hai dòng căn lề ngắn hơn).
  - Dấu mở `$$` và đóng `$$` đều nằm trên một dòng riêng biệt.
  - Tuyệt đối không sử dụng cú pháp cấm `\vert{}` hay `\Vert{}` (dùng trực tiếp $|...|$ hoặc $\|...\|$).

---

## 4. Kiểm chứng số học và giải thích học thuật độc lập (SI & Optics Re-computation)

Mọi phép tính trong các ví dụ và câu hỏi tự kiểm tra đều được viết mã Python tính toán lại độc lập từ các hằng số nền tảng của hệ đo lường quốc tế SI:

1. **Ví dụ 33.1 (Phản xạ và khúc xạ nước - thủy tinh)**:
   - Dữ kiện: $n_a = 1{,}33$, $n_b = 1{,}52$, $\theta_a = 60{,}0^\circ$.
   - Góc phản xạ: $\theta_r = \theta_a = 60{,}0^\circ$.
   - Khúc xạ theo Snell: $\sin \theta_b = \frac{1{,}33}{1{,}52} \sin(60{,}0^\circ) = 0{,}875 \times \frac{\sqrt{3}}{2} \approx 0{,}7578 \implies \theta_b = \arcsin(0{,}7578) \approx 49{,}3^\circ$.
   - Tia khúc xạ lệch lại gần pháp tuyến vì truyền sang môi trường chiết quang hơn ($n_b > n_a$).
2. **Ví dụ 33.2 (Chiết suất của thủy dịch mắt người)**:
   - Dữ kiện: Bước sóng laser trong không khí $\lambda_0 = 633\,\mathrm{nm}$, trong thủy dịch $\lambda = 474\,\mathrm{nm}$.
   - Chiết suất: $n = \lambda_0 / \lambda = 633 / 474 \approx 1{,}3354 \approx 1{,}34$.
   - Tốc độ truyền: Tính từ giá trị chưa làm tròn $v = c / n = 3{,}00 \times 10^8 / (633/474) \approx 2{,}246 \times 10^8\,\mathrm{m/s} \approx 2{,}25 \times 10^8\,\mathrm{m/s}$ (tránh mâu thuẫn số học khi lấy $1{,}34$ tính ra $2{,}2388$).
   - Tần số: $f = v / \lambda = c / \lambda_0 \approx 4{,}74 \times 10^{14}\,\mathrm{Hz}$.
   - Khẳng định tính bảo toàn tần số dao động tuyệt đối qua mặt phân cách hai môi trường.
3. **Ví dụ 33.3 (Hai gương phẳng vuông góc)**:
   - Góc tới gương 1 là $\theta_1$. Góc tới gương 2 là $\theta_2 = 90^\circ - \theta_1$.
   - Góc đổi hướng tại gương 1 là $\Delta \theta_1 = 180^\circ - 2\theta_1$; tại gương 2 là $\Delta \theta_2 = 180^\circ - 2(90^\circ - \theta_1) = 2\theta_1$.
   - Tổng độ đổi hướng: $\Delta \theta = \Delta \theta_1 + \Delta \theta_2 = 180^\circ$.
   - Dưới góc độ vector vận tốc: Tia phản xạ gương ngang đổi dấu $v_y \to -v_y$, gương đứng đổi dấu $v_x \to -v_x$, tổng vector vận tốc đảo chiều $\vec{v} \to -\vec{v}$.
   - Hệ 3 gương trực giao (góc khối): Tia phản xạ lùi song song ngược chiều khi đập trúng cả 3 mặt gương (tia phản xạ ngược chiều nhưng không nhất thiết trùng khít đường truyền ban đầu). Ứng dụng trong tấm phản quang xe đạp/ô tô và mảng gương phản xạ Apollo trên Mặt Trăng ($0{,}15\,\mathrm{m}$).
4. **Ví dụ 33.4 (Kính tiềm vọng rò rỉ nước)**:
   - Trong không khí ($n=1{,}00$): $\theta_{\text{crit}} = \arcsin(1{,}00 / 1{,}52) \approx 41{,}1^\circ$. Góc tới $45^\circ > 41{,}1^\circ \implies$ phản xạ toàn phần xảy ra.
   - Khi bị ngập nước ($n=1{,}33$): $\theta_{\text{crit}} = \arcsin(1{,}33 / 1{,}52) \approx 61{,}0^\circ$. Góc tới $45^\circ < 61{,}0^\circ \implies$ phản xạ toàn phần bị phá vỡ, phần lớn ánh sáng khúc xạ thoát vào nước, nhưng tại mặt phân cách vẫn còn phản xạ một phần nên hình ảnh bị mờ đi rất nhiều (greatly dims).
5. **Câu hỏi mở đầu (Độ lấp lánh và màu sắc của kim cương)**:
   - Chiết suất lớn $n = 2{,}417$ dẫn tới góc giới hạn rất nhỏ $\theta_{\text{crit}} \approx 24{,}4^\circ$, giam giữ ánh sáng và phản xạ toàn phần ra mặt trên.
   - Hiện tượng tán sắc phân tách các bước sóng khác nhau thành dải màu quang phổ rực rỡ. Chọn (iv) gồm cả (i) và (ii).
6. **Câu hỏi tự kiểm tra 33.1 (Mặt sóng tinh thể bất đẳng hướng)**:
   - Vận tốc $v_y > v_x = v_z$ dẫn tới mặt sóng ellipsoid có trục lớn dọc theo trục $y$. Chọn (iii).
7. **Câu hỏi tự kiểm tra 33.2 (Ngắm đâm cá bằng lao vs ngắm bằng súng laser)**:
   - Lao bay theo đường đạn thẳng: Phải ngắm xuống dưới vị trí biểu kiến của con cá. Chọn (ii).
   - Laser là ánh sáng tuân theo nguyên lý thuận nghịch đường đi tia sáng: Ngắm trực diện vào vị trí biểu kiến. Chọn (iii).
8. **Câu hỏi tự kiểm tra 33.3 (Các trường hợp phản xạ toàn phần)**:
   - Trường hợp (i): Nước sang không khí, $\theta_{\text{crit}} \approx 48{,}8^\circ < 70^\circ \implies$ có phản xạ toàn phần.
   - Trường hợp (ii): Thủy tinh sang nước, $\theta_{\text{crit}} \approx 61{,}0^\circ < 70^\circ \implies$ có phản xạ toàn phần.
   - Trường hợp (iii): Nước sang thủy tinh ($n_a < n_b$) $\implies$ không bao giờ xảy ra phản xạ toàn phần. Chọn (i) và (ii).
9. **Hiện tượng tán sắc và cầu vồng (Mục 33.4)**:
   - Cầu vồng bậc một (1 lần phản xạ nội): $\cos\theta = \sqrt{(n^2 - 1)/3}$. Cho màu đỏ ($n=1{,}331$): góc tán sắc $\Delta = 42{,}5^\circ$; cho màu tím ($n=1{,}344$): góc tán sắc $\Delta = 40{,}8^\circ$. Dải đỏ ở ngoài cùng phía trên, dải tím ở trong cùng phía dưới. Góc $\Delta$ được đo so với phương phản xạ ngược chiều (hướng đối nhật), chứ không phải phương tới ban đầu.
   - Cầu vồng bậc hai (2 lần phản xạ nội): $\cos\theta = \sqrt{(n^2 - 1)/8}$. Cho màu đỏ: góc tán sắc $\Delta = 50{,}1^\circ$; cho màu tím: góc tán sắc $\Delta = 53{,}2^\circ$. Thứ tự màu bị đảo ngược (tím ở phía trên, đỏ ở phía dưới).
   - Vùng tối giữa hai dải cầu vồng do không có tia sáng nào phản xạ một lần hay hai lần thoát ra trong dải góc từ $42{,}5^\circ$ đến $50{,}1^\circ$.

---

## 5. Chuẩn mực hành văn và phong cách sư phạm ("Giảng như giáo sư")

- **Viết hoa sau dấu hai chấm (`:`)**: Toàn bộ các câu văn xuôi, tiêu đề mục, đề mục danh sách và nhãn giải thích hình ảnh đều tuân thủ nghiêm ngặt quy tắc viết hoa chữ cái đầu tiên ngay sau dấu hai chấm (`:`).
- **Hạn chế dấu gạch ngang dài (em dash `—`)**: Loại bỏ triệt để các dấu gạch ngang dài kiểu dịch máy trong văn xuôi; thay thế bằng từ nối tiếng Việt chuẩn mực (*cụ thể là, tức là, đồng nghĩa với việc*) hoặc tách thành các câu đơn độc lập.
- **Không có lối viết "nghĩ thành tiếng"**: Lời giải ví dụ và câu tự kiểm tra được trình bày dứt khoát, sư phạm, chuẩn mực.
- **Không bịa đặt tần suất lỗi sinh viên hay bẫy thi cử cảm tính**: Trình bày trực diện bản chất vật lý đối chiếu giữa hai trường hợp (như sự đối lập giữa ngọn lao bay thẳng và chùm laser khúc xạ thuận nghịch trong câu tự kiểm tra 33.2).
- **Độ dài câu**: Các câu văn xuôi đều dưới 50–55 từ, nhịp điệu tự nhiên, trong sáng.

---

## 6. Lệnh kiểm thử và kết quả xác minh

1. **Kiểm tra cú pháp mô-đun chú thích nhãn ảnh**:
   ```powershell
   node --check docs/.vitepress/physics33-theory-a-image-annotations.mjs
   ```
   *Kết quả*: Exit code 0 (hợp lệ 100%).

2. **Chạy verifier kiểm tra toàn diện độc lập**:
   ```powershell
   python raw_materials/physics/verify_chapter33_theory_a.py
   ```
   *Kết quả*: Exit code 0. Toàn bộ 4 ví dụ, 4 câu tự kiểm tra, cơ chế tán sắc cầu vồng, 21 ảnh so khớp pixel PDF, 6 thẻ phương trình, 292 công thức nội dòng ($\le 38\mathrm{ex}$) và 26 khối công thức hiển thị ($\le 27\mathrm{ex}$) đều vượt qua thẩm định.

3. **Chạy bộ bài kiểm thử tự động của skill**:
   ```powershell
   python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
   ```
   *Kết quả*: Đạt toàn bộ bài kiểm thử tự động của skill.

---

## 7. Giới hạn sở hữu và bàn giao

- **Số tệp sở hữu chỉnh sửa**: Đúng 30 tệp được chỉ định trong kế hoạch `docs/agy-plans/2026-10-15-physics33-a.md`.
- **Tệp ngoài phạm vi**: Toàn bộ catalog, package.json, wiki chung, workspace chính và các worktree khác hoàn toàn ở trạng thái nguyên vẹn (read-only).
- Không tự ý chạy `npm run ci:build` hay `npm run build` trên máy cục bộ; khâu build toàn cục được ủy thác hoàn toàn cho GitHub Actions khi commit và push.
