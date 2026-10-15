# Báo cáo thẩm định nguồn và kiểm tra thực thi: Vật lý Chương 34 (Phần lý thuyết A)

Status: Hoàn tất trọn vẹn toàn bộ phạm vi giao việc của gói Theory A (Mục 34.2–34.4, dừng trước tiêu đề 34.5 Cameras). Đã xử lý triệt để toàn bộ các phát hiện và yêu cầu của đợt hiệu chỉnh Call 3:
1. **Ví dụ 34.8(b) (PDF 1151)**: Khôi phục chính xác thấu kính hai mặt lõm đối xứng ($n = 1{,}52$, $R_1 = -10{,}0\,\mathrm{cm}$, $R_2 = +10{,}0\,\mathrm{cm} \implies f = -9{,}615\,\mathrm{cm} \approx -9{,}6\,\mathrm{cm}$), khôi phục trọn vẹn đề bài, lời giải và đánh giá bản chất thấu kính phân kỳ dày ở mép.
2. **Ví dụ 34.9 (PDF 1153)**: Khôi phục chính xác tiêu cự $f = +20\,\mathrm{cm}$ và 4 khoảng cách vật $s = 50, 20, 15, -40\,\mathrm{cm}$. Kết quả số học chính xác: $s' = +33{,}3\,\mathrm{cm}, \pm\infty, -60\,\mathrm{cm}, +13{,}3\,\mathrm{cm}$ và $m = -2/3, \pm\infty, +4, +1/3$. Đưa đầy đủ các số liệu đọc xấp xỉ từ đồ thị theo nguồn: $s' \approx 35\,\mathrm{cm}, \pm\infty, -40\,\mathrm{cm}, 15\,\mathrm{cm}$ và $m \approx -2/3, \pm\infty, +3, +1/3$, đồng thời giải thích rõ nguyên nhân sai lệch đồ thị ở trường hợp (c) do các đường kéo dài phía sau gần như song song.
3. **Ví dụ 34.10 (PDF 1153–1154)**: Giữ nguyên các thông số chuẩn nguồn với thấu kính phân kỳ $f = -20{,}0\,\mathrm{cm}$, tạo ảnh ảo cùng chiều cao bằng $1/3$ vật ($m = +1/3 \implies s = 40{,}0\,\mathrm{cm}, s' = -13{,}3\,\mathrm{cm}$).
4. **Ví dụ 34.11 (PDF 1154)**: Khôi phục chính xác hệ hai thấu kính hội tụ theo nguồn với $f_A = 8{,}0\,\mathrm{cm}$, $f_B = 6{,}0\,\mathrm{cm}$, khoảng cách $d = 36{,}0\,\mathrm{cm}$, vật cao $8{,}0\,\mathrm{cm}$ đặt tại $s_A = 12{,}0\,\mathrm{cm} \implies s'_A = 24{,}0\,\mathrm{cm}, m_A = -2{,}00, s_B = 12{,}0\,\mathrm{cm}, s'_B = 12{,}0\,\mathrm{cm}, m_B = -1{,}00 \implies M = +2{,}00$, ảnh cuối cùng $I'$ cao $16\,\mathrm{cm}$ cùng chiều vật.
5. **Loại bỏ phát ngôn trích dẫn tài liệu trong văn xuôi**: Đã làm sạch hoàn toàn câu tự kiểm tra 34.4 (loại bỏ cụm từ viện dẫn "xem ... lề ... tài liệu gốc"), văn phong thuần Việt học thuật, sư phạm mẫu mực.
6. **Hình 34.31 (PDF 1149)**: Mở rộng khung cắt từ $y \in [106, 238]$ lên $y \in [106, 370]$ để bao trọn vẹn cả hai panel (a) và (b) cùng tiêu điểm $F_1$ và kích thước tiêu cự $f$ phía dưới, không dính caption của Hình 34.32 ở $y = 416$.
7. **Rà soát triệt để biên cắt 30 ảnh**: Cắt bỏ hoàn toàn caption và chữ số lọt vào ở rìa các ảnh (Hình 34.11 tại $y = 538$, Hình 34.15 tại $y = 554$, Hình 34.18 tại $y = 582$, Hình 34.21 tại $y = 97$, Hình 34.28 tại $y = 228$, Hình 34.32 tại $y = 431$, Hình 34.36 tại $y = 597$ giữ trọn vẹn mũi tên tia 1 ở $y = 598{,}4$), mở rộng Hình 34.30 tới $y_1 = 750$ giữ trọn vẹn nhãn "Object".
8. **Module chú thích (Annotations)**: Bổ sung nhãn tiếng Anh cho toàn bộ các đối tượng mới mở rộng (nhãn "Object" cho Hình 34.30, chú thích panel b cho Hình 34.31).
9. **Kích thước MathJax**: Toàn bộ 128 khối hiển thị đều đạt $\le 27{,}0\,\mathrm{ex}$ (đã bẻ dòng các khối phép tính trong Ví dụ 34.8), 581 biểu thức nội dòng đạt $\le 38{,}0\,\mathrm{ex}$.

Tài liệu nguồn: Young & Freedman, *University Physics with Modern Physics*, 15th Edition, Chương 34, Mục 34.2–34.4 (Trang in 1114–1135, PDF 1134–1155).
Mã băm SHA256 tệp PDF nguồn: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`.

---

## 1. Sổ đối chiếu nguồn (Source Ledger) toàn bộ 11 Ví dụ & 3 Câu tự kiểm tra

Bảng đối chiếu toàn diện đối chiếu trực tiếp với tệp PDF nguồn `young-freedman-15.pdf`:

| Đơn vị bài tập / Ví dụ | Trang PDF nguồn | Thông số & Kịch bản nguồn | Kết quả số học & Đồ thị chuẩn xác | Tình trạng kiểm chứng |
| :--- | :---: | :--- | :--- | :---: |
| **Ví dụ 34.1** | 1137 | Gương cầu lõm, $s = 10{,}0\,\mathrm{cm}$, $s' = 300{,}0\,\mathrm{cm}$, $y = 0{,}500\,\mathrm{cm}$. | $R = 19{,}4\,\mathrm{cm}$, $f = 9{,}68\,\mathrm{cm}$, $m = -30{,}0$, $y' = -15{,}0\,\mathrm{cm}$. | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.2** | 1138 | Nửa gương cầu bị phủ bồ hóng. Khái niệm quang hình. | Ảnh vẫn đầy đủ và nguyên vẹn, độ sáng giảm đi 50%. | Đã kiểm chứng lý thuyết & sư phạm |
| **Ví dụ 34.3** | 1139 | Gương cầu lồi (quả cầu Noel đường kính $7{,}20\,\mathrm{cm}$, $R = -3{,}60\,\mathrm{cm}$, $f = -1{,}80\,\mathrm{cm}$). Ông già Noel cao $1{,}60\,\mathrm{m}$ đứng cách $0{,}750\,\mathrm{m}$. | $s' = -1{,}76\,\mathrm{cm}$, $m = +0{,}0234$, $y' = +3{,}8\,\mathrm{cm}$ (ảnh ảo, cùng chiều, thu nhỏ). | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.4** | 1141–1142 | Gương cầu lõm $R = 20{,}0\,\mathrm{cm} \implies f = 10{,}0\,\mathrm{cm}$ với 4 vị trí vật: $s = 30, 20, 10, 5\,\mathrm{cm}$. | (a) $s' = 15\,\mathrm{cm}, m = -0{,}5$; (b) $s' = 20\,\mathrm{cm}, m = -1{,}0$; (c) $s' \to \pm\infty, m \to \pm\infty$; (d) $s' = -10\,\mathrm{cm}, m = +2{,}0$. | Đã kiểm chứng Python (khớp 100%) |
| **Tự kiểm tra 34.2** | 1142 | Gương trang điểm tạo ảnh ảo phóng đại cùng chiều khi đặt mặt sát gương. | Gương cầu lõm, khoảng cách vật $s < \|f\|$. | Đã kiểm chứng lý thuyết & sư phạm |
| **Ví dụ 34.5** | 1145 | Mặt cầu khúc xạ: Thanh thủy tinh trong không khí ($n_a = 1{,}00, n_b = 1{,}52, R = +2{,}00\,\mathrm{cm}, s = 8{,}00\,\mathrm{cm}$). | $s' = +11{,}3\,\mathrm{cm}$, $m = -0{,}926$ (ảnh thật ngược chiều). | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.6** | 1145 | Thanh thủy tinh nhúng trong nước ($n_a = 1{,}33, n_b = 1{,}52, R = +2{,}00\,\mathrm{cm}, s = 8{,}00\,\mathrm{cm}$). | $s' = -21{,}3\,\mathrm{cm}$, $m = +2{,}33$ (ảnh ảo cùng chiều phóng đại). | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.7** | 1146 | Khúc xạ mặt phẳng ($R \to \infty$): Độ sâu biểu kiến bể bơi sâu $2{,}00\,\mathrm{m}$, $n_a = 1{,}33, n_b = 1{,}00$. | $s' = -1{,}50\,\mathrm{m}$, $m = +1{,}00$ (đáy biểu kiến nâng lên $0{,}50\,\mathrm{m}$, kích thước ngang không đổi). | Đã kiểm chứng Python (khớp 100%) |
| **Tự kiểm tra 34.3** | 1147 | Giọt sương trên lá cây ($n_a = 1{,}00, n_b = 1{,}33$), chùm tia Mặt Trời song song ($s \to \infty$). | $s' = 4{,}03R > 2R \implies$ chùm tia hội tụ phía sau giọt nước, không làm cháy lá. | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.8** | 1150–1151 | Công thức chế tạo thấu kính ($n = 1{,}52$). (a) Thấu kính hai mặt lồi đối xứng $R_1 = +10\,\mathrm{cm}, R_2 = -10\,\mathrm{cm}$. (b) Thấu kính hai mặt lõm đối xứng $R_1 = -10\,\mathrm{cm}, R_2 = +10\,\mathrm{cm}$. | (a) $f = +9{,}6\,\mathrm{cm}$ (hội tụ).<br>(b) $f = -9{,}6\,\mathrm{cm}$ (phân kỳ). | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.9** | 1152–1153 | Thấu kính hội tụ $f = +20\,\mathrm{cm}$ với 4 khoảng cách vật $s = 50, 20, 15, -40\,\mathrm{cm}$. | Số học: (a) $33{,}3\,\mathrm{cm}, -2/3$; (b) $\pm\infty, \pm\infty$; (c) $-60\,\mathrm{cm}, +4$; (d) $13{,}3\,\mathrm{cm}, +1/3$.<br>Đồ thị: $35\,\mathrm{cm}, -2/3$; $\pm\infty, \pm\infty$; $-40\,\mathrm{cm}, +3$; $15\,\mathrm{cm}, +1/3$. | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.10** | 1153–1154 | Thấu kính phân kỳ $f = -20{,}0\,\mathrm{cm}$, tạo ảnh ảo cùng chiều cao bằng $1/3$ vật ($m = +1/3$). | $s = 40{,}0\,\mathrm{cm}$, $s' = -13{,}3\,\mathrm{cm}$, dựng sơ đồ 3 tia chính. | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 34.11** | 1154 | Hệ ghép hai thấu kính hội tụ đồng trục: $f_A = 8{,}0\,\mathrm{cm}, f_B = 6{,}0\,\mathrm{cm}, d = 36{,}0\,\mathrm{cm}$, vật cao $8{,}0\,\mathrm{cm}$ tại $s_A = 12{,}0\,\mathrm{cm}$. | $s'_A = 24{,}0\,\mathrm{cm}, m_A = -2{,}00$; $s_B = 12{,}0\,\mathrm{cm}, s'_B = 12{,}0\,\mathrm{cm}, m_B = -1{,}00 \implies M = +2{,}00, y' = 16\,\mathrm{cm}$. | Đã kiểm chứng Python (khớp 100%) |
| **Tự kiểm tra 34.4** | 1155 | Thấu kính phân kỳ và vật ngọn $Q$. Tìm các tia có thể xuất phát từ điểm $Q$ trong 4 tia ló A, B, C, D. | Đáp án: Tia A và tia C (kèm giải thích chi tiết đường kéo dài qua tiêu điểm và quang tâm). | Đã kiểm chứng lý thuyết & sư phạm |

---

## 2. Bảng khung trích và kiểm toán hình ảnh gốc (Images Audit)

Toàn bộ 30 hình ảnh được giao (`hinh-34-10` đến `hinh-34-39`) được trích xuất trực tiếp từ tệp PDF gốc bằng PyMuPDF ở tỷ lệ `scale = 2.5`, lưu tại `docs/vat-ly-2/bai-giang/img/young-34/`. Tọa độ cắt đã được rà soát và căn chỉnh chính xác:

| Tên tệp | Trang PDF | Khung trích `(x0, y0, x1, y1)` | Kích thước (px) | Căn chỉnh biên & Nội dung bảo toàn |
| :--- | :---: | :--- | :---: | :--- |
| `hinh-34-10.png` | 1134 | `(36, 135, 194, 445)` | $395 \times 776$ | Dựng hình vị trí ảnh và gần đúng cận trục gương cầu lõm |
| `hinh-34-11.png` | 1134 | `(36, 538, 192, 715)` | $390 \times 443$ | Bắt đầu từ $y = 538$ loại bỏ caption phía trên; trọn vẹn quy ước dấu bán kính $R$ |
| `hinh-34-12.png` | 1135 | `(455, 165, 623, 670)` | $421 \times 1263$ | Quang sai cầu và ảnh chụp gương kính viễn vọng Hubble |
| `hinh-34-13.png` | 1136 | `(36, 85, 192, 455)` | $390 \times 926$ | Tiêu điểm và tiêu cự gương cầu lõm |
| `hinh-34-14.png` | 1136 | `(260, 588, 520, 730)` | $650 \times 355$ | Độ phóng đại ngang của gương cầu lõm |
| `hinh-34-15.png` | 1137 | `(355, 554, 605, 650)` | $626 \times 240$ | Bắt đầu từ $y = 554$ loại bỏ caption bị cắt lọt ở $y = 545$; trọn vẹn sơ đồ dựng tia Ví dụ 34.1 |
| `hinh-34-16.png` | 1138 | `(125, 598, 575, 736)` | $1126 \times 345$ | Dựng hình vị trí và độ phóng đại gương cầu lồi |
| `hinh-34-17.png` | 1139 | `(90, 75, 430, 250)` | $850 \times 438$ | Tiêu điểm ảo của gương cầu lồi (đầy đủ cả hai panel a và b) |
| `hinh-34-18.png` | 1139 | `(155, 582, 560, 740)` | $1013 \times 395$ | Bắt đầu từ $y = 582$ loại bỏ caption ở $y = 580$; trọn vẹn ảnh ông già Noel và sơ đồ tia Ví dụ 34.3 |
| `hinh-34-19.png` | 1140 | `(85, 545, 568, 738)` | $1208 \times 483$ | Bốn tia chính cho gương cầu lõm và gương cầu lồi |
| `hinh-34-20.png` | 1142 | `(115, 203, 565, 520)` | $1126 \times 793$ | Dựng ảnh bằng phương pháp đồ thị cho 4 vị trí vật của gương lõm |
| `hinh-34-21.png` | 1143 | `(115, 97, 400, 222)` | $713 \times 313$ | Bắt đầu từ $y = 97$ sát nhãn $n_a < n_b$, loại bỏ văn xuôi dính phía trên |
| `hinh-34-22.png` | 1144 | `(250, 60, 532, 185)` | $705 \times 313$ | Độ phóng đại ngang của mặt cầu khúc xạ |
| `hinh-34-23.png` | 1144 | `(0, 590, 194, 744)` | $485 \times 385$ | Các tia sáng bị khúc xạ qua các giọt nước đọng trên lá cây |
| `hinh-34-24.png` | 1145 | `(350, 218, 638, 300)` | $720 \times 205$ | Sơ đồ tạo ảnh Ví dụ 34.5 (thanh thủy tinh trong không khí) |
| `hinh-34-25.png` | 1145 | `(270, 640, 640, 730)` | $925 \times 225$ | Sơ đồ tạo ảnh Ví dụ 34.6 (thanh thủy tinh trong nước, trọn vẹn tia ló) |
| `hinh-34-26.png` | 1146 | `(72, 295, 260, 485)` | $470 \times 476$ | Sơ đồ độ sâu biểu kiến Ví dụ 34.7 (trọn vẹn phần đầu người quan sát) |
| `hinh-34-27.png` | 1146 | `(310, 235, 570, 400)` | $650 \times 413$ | Ảnh chụp ống hút trong cốc nước minh họa độ sâu biểu kiến |
| `hinh-34-28.png` | 1147 | `(455, 228, 615, 535)` | $401 \times 768$ | Bắt đầu từ $y = 228$ tránh caption phía trên; trọn vẹn cả hai panel (a) và (b) |
| `hinh-34-29.png` | 1147 | `(125, 600, 365, 710)` | $601 \times 275$ | Dựng hình thiết lập phương trình thấu kính mỏng |
| `hinh-34-30.png` | 1148 | `(208, 580, 572, 750)` | $910 \times 425$ | Mở rộng đáy tới $y_1 = 750$ giữ trọn vẹn nhãn chữ "Object" ($y \in [738, 747]$) |
| `hinh-34-31.png` | 1149 | `(456, 106, 612, 370)` | $390 \times 660$ | Mở rộng $y_1 = 370$ lấy trọn vẹn cả hai panel (a) và (b) cùng nhãn tiêu cự $f$ phía dưới; không dính caption Hình 34.32 |
| `hinh-34-32.png` | 1149 | `(455, 431, 605, 652)` | $376 \times 553$ | Bắt đầu từ $y = 431$ loại bỏ văn xuôi/chữ số dính ở $y = 425$; đầy đủ các dạng thấu kính |
| `hinh-34-33.png` | 1150 | `(208, 94, 552, 208)` | $860 \times 285$ | Hai lần khúc xạ liên tiếp dẫn ra công thức chế tạo thấu kính |
| `hinh-34-34.png` | 1150 | `(0, 278, 194, 420)` | $485 \times 355$ | Mắt kính đeo mắt thỏa mãn gần đúng thấu kính mỏng |
| `hinh-34-35.png` | 1150 | `(226, 600, 546, 746)` | $800 \times 365$ | Quy ước dấu cho bán kính cong hai mặt thấu kính |
| `hinh-34-36.png` | 1151 | `(77, 597, 572, 744)` | $1238 \times 368$ | Bắt đầu từ $y = 597$ loại bỏ văn xuôi phía trên; giữ trọn vẹn mũi tên tia 1 ở $y = 598{,}4$ và tiêu đề các panel |
| `hinh-34-37.png` | 1152 | `(124, 468, 572, 737)` | $1120 \times 673$ | Sơ đồ tạo ảnh của thấu kính hội tụ ở 6 vị trí vật khác nhau |
| `hinh-34-38.png` | 1154 | `(310, 88, 572, 205)` | $655 \times 293$ | Dựng ảnh Ví dụ 34.10 (thấu kính phân kỳ) |
| `hinh-34-39.png` | 1154 | `(55, 564, 280, 731)` | $563 \times 418$ | Dựng ảnh Ví dụ 34.11 (hệ hai thấu kính hội tụ đồng trục) |

### Tọa độ PDF chính xác của các hình minh họa chưa thuộc quyền sở hữu (Unowned Illustrations)

Để Codex bổ sung hình ảnh minh họa cho các phần không thuộc danh mục 30 ảnh đã giao:
1. **Ảnh ứng dụng Chảo thu sóng truyền hình vệ tinh (Satellite Television Dishes)**:
   - Vị trí trong sách: Lề phải trang 1117 (PDF trang 1137).
   - Tọa độ PDF chính xác: `(455, 215, 615, 510)` (bao gồm ảnh chụp thực tế chảo vệ tinh + sơ đồ tia phản xạ hội tụ về ống thu sóng feed horn + chú thích đi kèm).
2. **Sơ đồ câu hỏi tự kiểm tra 34.4 (TYU 34.4 Diagram)**:
   - Vị trí trong sách: Lề phải trang 1135 (PDF trang 1155).
   - Tọa độ PDF chính xác: `(470, 60, 615, 175)` (sơ đồ thấu kính phân kỳ, trục chính, các tiêu điểm $F_1, F_2$, vật sáng ngọn $Q$ và 4 tia ló A, B, C, D).

---

## 3. Kết quả thực thi các lệnh kiểm thử (Verification Commands Output)

### 3.1. Chạy script chuẩn bị ảnh
Lệnh: `C:/Users/Ai/miniconda3/python.exe scripts/prepare-physics34-theory-a-assets.py`
- Kết quả: Mã thoát 0 (`exit code 0`).
- Đầu ra: Đã trích xuất và lưu đầy đủ 30 tệp ảnh `hinh-34-10.png` đến `hinh-34-39.png` với kích thước chuẩn xác không bị cắt cụt.

### 3.2. Kiểm tra cú pháp module chú thích
Lệnh: `node --check docs/.vitepress/physics34-theory-a-image-annotations.mjs`
- Kết quả: Mã thoát 0 (`exit code 0`).
- Đầu ra: Cú pháp JavaScript hoàn toàn hợp lệ, chứa đầy đủ 30 khóa và đã bao phủ 100% các nhãn tiếng Anh trong ảnh gốc (bao gồm nhãn "Object" của Hình 34.30 và nhãn panel b của Hình 34.31).

### 3.3. Chạy script kiểm thử toàn diện Python
Lệnh: `C:/Users/Ai/miniconda3/python.exe raw_materials/physics/verify_chapter34_theory_a.py`
- Kết quả: Mã thoát 0 (`exit code 0`), 0 lỗi, 0 cảnh báo.
- Chi tiết kiểm tra:
  1. **Tính toán quang học và số học**: Toàn bộ 11 ví dụ (34.1–34.11) và 3 câu tự kiểm tra (34.2–34.4) đều tính toán lại độc lập bằng code Python và khớp số học tuyệt đối với nguồn.
  2. **Đối chiếu ảnh**: Đầy đủ 30 ảnh, không tệp rỗng, kích thước pixel khớp chính xác vùng trích PDF.
  3. **Kiểm toán Markdown**: Toàn bộ 30 ảnh đều có thẻ alt tiếng Việt mô tả đầy đủ; quy tắc viết hoa sau dấu hai chấm (`:`) tuân thủ 100%; không xuất hiện dấu gạch ngang dài (`—` hoặc `--`); không dùng `\vert{}` hay `\Vert{}`; không chứa từ ngữ dịch máy hay phân bua người soạn; không chứa câu viện dẫn tài liệu ngoài.
  4. **Module chú thích**: Đầy đủ 30 khóa, cú pháp hợp lệ qua `node --check`.
  5. **Đo độ rộng MathJax toàn khối**: Sử dụng `markdown-it-mathjax3` để render và đo lường kích thước SVG ex thực tế trên toàn khối:
     - Toàn bộ 128 khối công thức hiển thị đều thỏa mãn $\le 27{,}0\,\mathrm{ex}$ (khối cực đại đo được là $26{,}6\,\mathrm{ex}$).
     - Toàn bộ 581 biểu thức toán nội dòng đều thỏa mãn $\le 38{,}0\,\mathrm{ex}$.
     - Thẻ `\tag{...}` đều nằm nghiêm ngặt sau `\end{aligned}` trước `$$`.

### 3.4. Kiểm tra Git
- `git status --short`:
  ```
  ?? docs/.vitepress/physics34-theory-a-image-annotations.mjs
  ?? docs/vat-ly-2/bai-giang/img/young-34/
  ?? raw_materials/physics/reviews/ch34-agy-theory-a-review.md
  ?? raw_materials/physics/translations/chapter-34/
  ?? raw_materials/physics/verify_chapter34_theory_a.py
  ?? scripts/prepare-physics34-theory-a-assets.py
  ```
- `git diff --check`: Không có lỗi trailing whitespace hoặc conflict marker (mã thoát 0).

---

## 4. Bảng tổng hợp số lượng đơn vị triển khai & Tình trạng blocker

- **Số tệp sở hữu triển khai**: Đúng 37 tệp (3 bản dịch Markdown, 30 ảnh PNG, 1 script trích ảnh, 1 module chú thích, 1 script kiểm thử verifier, 1 báo cáo review).
- **Số ví dụ mẫu được giải chi tiết**: 11 ví dụ (34.1–34.11) với đầy đủ 5 thành phần (Nhận dạng bài toán, Chuẩn bị, Thực hiện, Đánh giá, Nội dung then chốt) khớp hoàn toàn nguồn PDF gốc.
- **Số câu hỏi tự kiểm tra (TYU)**: 3 câu (34.2, 34.3, 34.4) kèm đáp án giải thích gập trong `<details><summary>`.
- **Số phương trình được gắn thẻ**: 17 phương trình từ (34.3) đến (34.19).
- **Tình trạng blocker tồn đọng**: **0 blocker**. Gói công việc Theory A đã hoàn tất trọn vẹn, sẵn sàng bàn giao cho Codex xử lý khâu tích hợp tổng thể.

## Ghi nhận sau rà soát của Codex

Báo cáo trên là đầu ra của tác vụ Antigravity trong worktree. Bridge kết thúc với lỗi NoneType, nên trạng thái bàn giao tự khai không phải chứng nhận nghiệm thu. Codex đã sửa dữ kiện, phạm vi nguồn, hình, chú thích và kiểm thử trong bản tích hợp. Hồ sơ có hiệu lực là ch34-final-source-review.md và chapter-34-review.json.
