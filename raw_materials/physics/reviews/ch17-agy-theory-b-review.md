# Báo cáo rà soát nội bộ (Internal Review): Vật lý 1 — Chương 17 (Theory B)

- **Môn học**: Vật lý 1 (Physics 1)
- **Phạm vi bài giảng**: Chương 17, các mục 17.5, 17.6, 17.7 và Toàn bộ trang tóm tắt chương 17 (Trang PDF 572–588)
- **Tài liệu nguồn**: `raw_materials/physics/source/young-freedman-15.pdf` (SHA256: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`)
- **Tác vụ**: Evidence-based Correction 1 (Call 2/3)

---

## 1. Danh mục các tệp thuộc quyền sở hữu (Owned Files Inventory)

Mọi thay đổi chỉ diễn ra trên đúng các đường dẫn được cấp quyền sở hữu trong bản kế hoạch đã cam kết:

| STT | Đường dẫn tệp | Trạng thái | Nội dung chính |
| :--- | :--- | :--- | :--- |
| 1 | `raw_materials/physics/translations/chapter-17/05-nhiet-luong.md` | Đã hoàn thiện | Mục 17.5: Bản chất nhiệt lượng, đơn vị, nhiệt dung riêng, nhiệt dung mol, Ví dụ 17.5, 17.6, TYU 17.5 |
| 2 | `raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md` | Đã hoàn thiện & căn chỉnh Math | Mục 17.6: Các pha, nhiệt chuyển pha, nhiệt lượng kế, Ví dụ 17.7, 17.8, 17.9, 17.10, TYU 17.6 |
| 3 | `raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md` | Đã hoàn thiện | Mục 17.7: Dẫn nhiệt, đối lưu, bức xạ nhiệt, Bảng 17.5, Ví dụ 17.11–17.15, các ứng dụng, khí hậu & hiệu ứng nhà kính, TYU 17.7 |
| 4 | `raw_materials/physics/translations/chapter-17/17-tom-tat.md` | Đã hoàn thiện | Toàn bộ trang PDF 588: Tóm tắt 4 khối kiến thức, toàn bộ phương trình tổng kết (17.1 đến 17.26) và 4 sơ đồ |
| 5 | `scripts/prepare-physics1-17-theory-b-assets.py` | Đã tạo | Mã nguồn trích xuất 21 hình ảnh minh họa từ PDF gốc ở độ phân giải $3\times$ |
| 6 | `docs/.vitepress/physics1-17-theory-b-image-annotations.mjs` | Đã tạo & xác thực | Từ điển chú thích song ngữ cho toàn bộ 21 hình ảnh |
| 7 | `raw_materials/physics/verify_chapter17_theory_b.py` | Đã cập nhật & vượt qua | Bộ kiểm thử số học, năng lượng chuyển pha, dẫn nhiệt, bức xạ và kiểm tra khớp pixel RGB tươi từ PDF gốc |
| 8 | `raw_materials/physics/reviews/ch17-agy-theory-b-review.md` | Đang hoàn thiện | Bản báo cáo rà soát nội bộ độc lập |
| 9 | `docs/vat-ly-1/bai-giang/img/young-17/b-*.png` | Đã tạo (21 tệp) | Toàn bộ 21 tệp ảnh PNG phẳng độc quyền cho nhánh Theory B |

---

## 2. Bảng đối chiếu số liệu tính toán chi tiết (Numerical Verification Ledger)

Mọi ví dụ và bài kiểm tra hiểu biết đều được kiểm tra độc lập bằng mã Python nghiêm ngặt, bảo đảm khớp chính xác từng thông số đầu vào và kết quả đầu ra của giáo trình gốc.

### Bảng 2.1: Các ví dụ dạy học từ Mục 17.5 đến Mục 17.7

| Bài toán | Đại lượng đầu vào | Công thức & Bước biến đổi | Kết quả đầu ra | Ghi chú & Đơn vị |
| :--- | :--- | :--- | :--- | :--- |
| **Đơn vị nhiệt** | $1\,\mathrm{cal}$, $1\,\mathrm{kcal}$, $1\,\mathrm{Btu}$ | $1\,\mathrm{cal} = 4{,}186\,\mathrm{J}$ | $4{,}186\,\mathrm{J}$ | Định nghĩa cơ học của nhiệt |
| | | $1\,\mathrm{kcal} = 4186\,\mathrm{J}$ | $4186\,\mathrm{J}$ | Calo dinh dưỡng |
| | | $1\,\mathrm{Btu} = 1055\,\mathrm{J} = 778\,\mathrm{ft\cdot lb} = 252\,\mathrm{cal}$ | $1055\,\mathrm{J}$ | Đơn vị nhiệt Anh |
| **Ví dụ 17.5** | $m = 80{,}0\,\mathrm{kg}$, $\Delta T = 2{,}0\,\mathrm{C^\circ}$ | Mô hình toàn nước: $Q = mc_{\mathrm{nuoc}}\Delta T$ | $6{,}7 \times 10^5\,\mathrm{J} = 160\,\mathrm{kcal}$ | Đã quy đổi chính xác kcal |
| | $c_{\mathrm{nuoc}} = 4190\,\mathrm{J/(kg\cdot K)}$ | Mô hình mô cơ thể: $Q = mc_{\mathrm{body}}\Delta T$ | $5{,}6 \times 10^5\,\mathrm{J} = 133\,\mathrm{kcal}$ | $c_{\mathrm{body}} = 3480\,\mathrm{J/(kg\cdot K)}$ |
| **Ví dụ 17.6** | $m = 23\,\mathrm{mg} = 23 \times 10^{-6}\,\mathrm{kg}$ | $dT/dt = (dQ/dt) / (mc)$ | $0{,}46\,\mathrm{K/s} = 0{,}46\,\mathrm{C^\circ/s}$ | Đã xác nhận đổi $23\,\mathrm{mg} = 23 \times 10^{-6}\,\mathrm{kg}$ |
| | $P = dQ/dt = 7{,}4\,\mathrm{mW} = 7{,}4 \times 10^{-3}\,\mathrm{W}$ | $(0{,}45637\,\mathrm{K/s}) \times 60\,\mathrm{s/min}$ | $27\,\mathrm{C^\circ/min}$ | Chip silicon nóng lên nhanh chóng |
| | $c_{\mathrm{Si}} = 705\,\mathrm{J/(kg\cdot K)}$ | | | |
| **TYU 17.5** | $\Delta T = 1\,\mathrm{K}$, $1\,\mathrm{kg}$ và $1\,\mathrm{mol}$ | $Q = mc\Delta T$ hoặc $Q = nC\Delta T$ | (ii) $2428\,\mathrm{J} >$ (i) $138\,\mathrm{J} >$ (iv) $111{,}9\,\mathrm{J} >$ (iii) $27{,}7\,\mathrm{J}$ | Thứ tự giảm dần: (ii), (i), (iv), (iii) |
| **Ví dụ 17.7** | Cà phê: $m = 0{,}300\,\mathrm{kg}$, $70{,}0^\circ\mathrm{C}$ | Cân bằng nhiệt lượng: $Q_{\mathrm{coffee}} + Q_{\mathrm{cup}} = 0$ | $T = 66{,}0^\circ\mathrm{C}$ | Nhiệt độ cân bằng cuối |
| | Cốc nhôm: $m = 0{,}120\,\mathrm{kg}$, $20{,}0^\circ\mathrm{C}$ | $Q_{\mathrm{coffee}} = -5024\,\mathrm{J}$, $Q_{\mathrm{cup}} = +5024\,\mathrm{J}$ | $5024\,\mathrm{J} = 5{,}02\,\mathrm{kJ}$ | Nhiệt lượng truyền qua lại |
| **Ví dụ 17.8** | Nước ngọt: $m = 0{,}25\,\mathrm{kg}$, $25{,}0^\circ\mathrm{C}$ | $Q_{\mathrm{cola}} + Q_{\mathrm{ice,warm}} + Q_{\mathrm{ice,melt}} = 0$ | $m_{\mathrm{ice}} = 0{,}070\,\mathrm{kg} = 70\,\mathrm{g}$ | Lượng đá tan làm lạnh cola về $0^\circ\mathrm{C}$ |
| | Nước đá: $-20{,}0^\circ\mathrm{C}$, $L_f = 3{,}34 \times 10^5\,\mathrm{J/kg}$ | $c_{\mathrm{ice}} = 2100\,\mathrm{J/(kg\cdot K)}$ | | Khớp kết quả $69{,}6\,\mathrm{g} \approx 70\,\mathrm{g}$ |
| **Ví dụ 17.9** | Nồi đồng: $m = 2{,}0\,\mathrm{kg}$, $150^\circ\mathrm{C}$ | Khảo sát 3 trường hợp: | $T = 100^\circ\mathrm{C}$ | Có $3{,}4\,\mathrm{g}$ nước sôi thành hơi |
| | Nước: $m = 0{,}10\,\mathrm{kg}$, $25^\circ\mathrm{C}$ | TH1: $T = 106^\circ\mathrm{C} > 100^\circ\mathrm{C}$ (mâu thuẫn) | $m_{\mathrm{steam}} = 3{,}4 \times 10^{-3}\,\mathrm{kg}$ | Khối lượng nước lỏng còn lại: |
| | $c_{\mathrm{Cu}} = 390\,\mathrm{J/(kg\cdot K)}$, $L_v = 2{,}256 \times 10^6\,\mathrm{J/kg}$ | TH2: $x = 0{,}034 \implies m_{\mathrm{steam}} = 3{,}4\,\mathrm{g}$ | $m_{\mathrm{water}} = 0{,}097\,\mathrm{kg} = 97\,\mathrm{g}$ | Ngưỡng hóa hơi toàn bộ: $15\,\mathrm{g}$ nước |
| **Ví dụ 17.10** | Đun $1{,}00\,\mathrm{kg}$ nước $20^\circ\mathrm{C} \to 100^\circ\mathrm{C}$ | $Q_{\mathrm{warm}} = 3{,}35 \times 10^5\,\mathrm{J}$ | $Q_{\mathrm{total}} = 8{,}99 \times 10^5\,\mathrm{J}$ | Nhiệt lượng có ích nhận vào |
| | Hóa hơi $0{,}25\,\mathrm{kg}$ nước ở $100^\circ\mathrm{C}$ | $Q_{\mathrm{boil}} = 5{,}64 \times 10^5\,\mathrm{J}$ | $Q_{\mathrm{combustion}} = 3{,}00 \times 10^6\,\mathrm{J}$ | Hiệu suất bếp $30\%$ |
| | Xăng: $L_c = 46000\,\mathrm{J/g}$ | $m_{\mathrm{gas}} = Q_{\mathrm{combustion}} / L_c$ | $m_{\mathrm{gas}} = 65\,\mathrm{g}$ | Đun tiếp $0{,}75\,\mathrm{kg}$ cần thêm $123\,\mathrm{g}$ xăng |
| **TYU 17.6** | Nhiệt lượng cung cấp đều đặn | $Q_{\mathrm{total}} = Q_1 + Q_2 + Q_3$ | $Q(t/2) = 15{,}05 \times 10^5 m$ | Vượt qua $Q_1+Q_2 = 7{,}53 \times 10^5 m$ |
| | Tại thời điểm $t/2$ | $Q_{\mathrm{du}} = 7{,}52 \times 10^5 m$ đang hóa hơi | Trạng thái: Hỗn hợp nước và hơi ở $100^\circ\mathrm{C}$ | Lựa chọn đúng: (iv) |
| **Ứng dụng sinh học** | Lông cáo: $k = 0{,}04\,\mathrm{W/(m\cdot K)}$, $1\,\mathrm{cm}$ | Cùng nhiệt trở $L_1/k_1 = L_2/k_2$ | $L_{\mathrm{mo}} = 1\,\mathrm{cm} \times (0{,}24 / 0{,}04) = 6\,\mathrm{cm}$ | Cần lớp mỡ dày gấp 6 lần |
| | Mỡ cá voi: $k = 0{,}24\,\mathrm{W/(m\cdot K)}$ | | | |
| **Ví dụ 17.11** | Thùng xốp: $A = 0{,}80\,\mathrm{m^2}$, $L = 0{,}020\,\mathrm{m}$ | $H = kA(T_H - T_C)/L$ | $H = 32{,}4\,\mathrm{W} = 32{,}4\,\mathrm{J/s}$ | Dòng nhiệt dẫn qua thành xốp |
| | $k = 0{,}027\,\mathrm{W/(m\cdot K)}$, $\Delta T = 30\,\mathrm{C^\circ}$ | $Q = Ht = (32{,}4)(10800\,\mathrm{s})$ | $Q = 3{,}50 \times 10^5\,\mathrm{J}$ | Tổng nhiệt lượng trong 3 giờ |
| | $t = 3\,\mathrm{h} = 10800\,\mathrm{s}$ | $m = Q / L_f$ | $m = 1{,}0\,\mathrm{kg}$ | Khối lượng đá tan chảy |
| **Ví dụ 17.12** | Thép: $L_S = 0{,}100\,\mathrm{m}$, $k_S = 50{,}2\,\mathrm{W/(m\cdot K)}$ | Hai thanh ghép nối tiếp: $H_S = H_{\mathrm{Cu}}$ | $T_{\mathrm{moi\,noi}} = 20{,}7^\circ\mathrm{C}$ | Nhiệt độ tại mối nối |
| | Đồng: $L_{\mathrm{Cu}} = 0{,}200\,\mathrm{m}$, $k_{\mathrm{Cu}} = 385\,\mathrm{W/(m\cdot K)}$ | $T = \frac{(k_S/L_S)T_H + (k_{\mathrm{Cu}}/L_{\mathrm{Cu}})T_C}{(k_S/L_S) + (k_{\mathrm{Cu}}/L_{\mathrm{Cu}})}$ | $H = 15{,}9\,\mathrm{W}$ | Dòng nhiệt ổn định qua hệ |
| | $A = 4{,}00 \times 10^{-4}\,\mathrm{m^2}$, $T_H = 100^\circ\mathrm{C}$, $T_C = 0^\circ\mathrm{C}$ | $H = (k_S A / L_S)(T_H - T)$ | | Thép chịu sụt áp nhiệt lớn hơn |
| **Ví dụ 17.13** | Hai thanh trong Ví dụ 17.12 ghép song song | $H_S = (k_S A / L_S)\Delta T$ | $H_S = 20{,}1\,\mathrm{W}$ | Dòng nhiệt qua thép |
| | $\Delta T = 100\,\mathrm{K}$ đặt lên từng thanh | $H_{\mathrm{Cu}} = (k_{\mathrm{Cu}} A / L_{\mathrm{Cu}})\Delta T$ | $H_{\mathrm{Cu}} = 77{,}0\,\mathrm{W}$ | Dòng nhiệt qua đồng |
| | | $H = H_S + H_{\mathrm{Cu}}$ | $H_{\mathrm{tong}} = 97{,}1\,\mathrm{W}$ | Lớn gấp hơn 6 lần so với nối tiếp |
| **Ví dụ 17.14** | Tấm thép: $a = 0{,}10\,\mathrm{m}$, 2 mặt | $A = 2a^2 = 0{,}020\,\mathrm{m^2}$ | $H = 900\,\mathrm{W}$ | Công suất bức xạ từ tấm thép nung đỏ |
| | $T = 800^\circ\mathrm{C} = 1073\,\mathrm{K}$, $e = 0{,}60$ | $H = Ae\sigma T^4$ | Khớp giá trị chính xác $900\,\mathrm{W}$ | |
| **Ví dụ 17.15** | Người: $A = 1{,}20\,\mathrm{m^2}$, $e = 1{,}0$ | Bức xạ phát ra: $H = Ae\sigma T^4$ | $H_{\mathrm{phat}} = 574\,\mathrm{W}$ | Phát ra bức xạ hồng ngoại |
| | $T = 30^\circ\mathrm{C} = 303\,\mathrm{K}$, $T_s = 20^\circ\mathrm{C} = 293\,\mathrm{K}$ | Mất nhiệt ròng: $H_{\mathrm{net}} = Ae\sigma(T^4 - T_s^4)$ | $H_{\mathrm{net}} = 72\,\mathrm{W}$ | Hấp thụ từ phòng $502\,\mathrm{W}$ |
| **TYU 17.7** | Ba bức tường: Bê tông, đồng, thép ở $20^\circ\mathrm{C}$ | $H = kA\Delta T / L$, phụ thuộc vào $k$ | Đồng cảm thấy lạnh nhất: (ii) | $k_{\mathrm{Cu}} = 385 \gg k_S = 50{,}2 \gg k_{\mathrm{be\,tong}} = 0{,}8$ |

---

## 3. Danh mục hình ảnh và kiểm tra độ khớp pixel (Fresh RGB Crop & Annotation Verification)

Toàn bộ 21 hình ảnh đều được trích xuất trực tiếp từ tệp PDF gốc `young-freedman-15.pdf` ở tỉ lệ phóng đại $3\times$ (độ phân giải cao, $300\,\mathrm{DPI}$ tương đương), cắt chính xác vùng hình vẽ và bảng biểu, không chém vào chữ tiêu đề hay nội dung văn bản xung quanh.

| Tên tệp ảnh PNG | Trang PDF | Tọa độ Bounding Box (pt) | Kích thước pixel | Độ lệch pixel so với PDF tươi |
| :--- | :--- | :--- | :--- | :--- |
| `b-hinh-17-15.png` | 572 | `(33.0, 103.0, 192.0, 448.0)` | $477 \times 1035$ | $0$ (Exact match) |
| `b-hinh-17-16.png` | 572 | `(34.0, 558.0, 194.0, 683.0)` | $480 \times 375$ | $0$ (Exact match) |
| `b-hinh-17-17.png` | 573 | `(465.0, 213.0, 602.0, 330.0)` | $411 \times 351$ | $0$ (Exact match) |
| `b-hinh-17-18.png` | 574 | `(32.0, 373.0, 194.0, 521.0)` | $486 \times 444$ | $0$ (Exact match) |
| `b-hinh-17-19.png` | 576 | `(33.0, 154.0, 194.0, 292.0)` | $483 \times 414$ | $0$ (Exact match) |
| `b-hinh-17-20.png` | 577 | `(76.0, 95.0, 485.0, 280.0)` | $1227 \times 555$ | $0$ (Exact match) |
| `b-hinh-17-21.png` | 577 | `(453.0, 428.0, 617.0, 579.0)` | $492 \times 453$ | $0$ (Exact match) |
| `b-hinh-17-22.png` | 578 | `(33.0, 156.0, 194.0, 353.0)` | $483 \times 591$ | $0$ (Exact match) |
| `b-hinh-17-23.png` | 578 | `(33.0, 522.0, 194.0, 631.0)` | $483 \times 327$ | $0$ (Exact match) |
| `b-hinh-17-24.png` | 581 | `(455.0, 85.0, 610.0, 340.0)` | $465 \times 765$ | $0$ (Exact match) |
| `b-ung-dung-17-01.png` | 582 | `(27.0, 193.0, 195.0, 369.0)` | $504 \times 528$ | $0$ (Exact match) |
| `b-hinh-17-25.png` | 583 | `(85.0, 220.0, 332.0, 353.0)` | $741 \times 399$ | $0$ (Exact match) |
| `b-hinh-17-26.png` | 583 | `(75.0, 638.0, 341.0, 731.0)` | $798 \times 279$ | $0$ (Exact match) |
| `b-hinh-17-27.png` | 584 | `(74.0, 197.0, 214.0, 327.0)` | $420 \times 390$ | $0$ (Exact match) |
| `b-hinh-17-28.png` | 584 | `(33.0, 455.0, 194.0, 662.0)` | $483 \times 621$ | $0$ (Exact match) |
| `b-hinh-17-29.png` | 585 | `(453.0, 225.0, 614.0, 348.0)` | $483 \times 369$ | $0$ (Exact match) |
| `b-hinh-17-30.png` | 587 | `(75.0, 538.0, 588.0, 732.0)` | $1539 \times 582$ | $0$ (Exact match) |
| `b-tom-tat-01.png` | 588 | `(447.0, 87.0, 577.0, 207.0)` | $390 \times 360$ | $0$ (Exact match) |
| `b-tom-tat-02.png` | 588 | `(447.0, 242.0, 577.0, 307.0)` | $390 \times 195$ | $0$ (Exact match) |
| `b-tom-tat-03.png` | 588 | `(447.0, 377.0, 577.0, 487.0)` | $390 \times 330$ | $0$ (Exact match) |
| `b-tom-tat-04.png` | 588 | `(447.0, 562.0, 577.0, 652.0)` | $390 \times 270$ | $0$ (Exact match) |

Từ điển `docs/.vitepress/physics1-17-theory-b-image-annotations.mjs`: Đã xác thực thành công cấu trúc xuất khẩu `physics1Chapter17TheoryBImageAnnotations`, đủ 21 khóa tương ứng 21 hình ảnh, 0 nhãn tiếng Anh trùng lặp trong cùng một hình, 0 cặp song ngữ đồng nhất, không phát sinh từ ngữ bịa đặt.

---

## 4. Xử lý các yêu cầu sư phạm đặc thù về Khí hậu và Hiệu ứng nhà kính

Tuân thủ nghiêm ngặt chỉ dẫn:
1. **Phân biệt rạch ròi vai trò của các khí nhà kính**: Làm rõ hiện tượng nhiệt độ bề mặt Trái Đất cao hơn $33\,\mathrm{K}$ ($33^\circ\mathrm{C}$) so với trạng thái không có khí quyển là kết quả của toàn bộ hiệu ứng nhà kính tự nhiên (trong đó hơi nước $\mathrm{H_2O}$ là thành phần hấp thụ hồng ngoại dồi dào nhất, cùng với chu trình phản hồi hơi nước do $\mathrm{CO_2}$ kích hoạt), chứ không phải do riêng sự hấp thụ trực tiếp của một mình $\mathrm{CO_2}$.
2. **Kịch bản lịch sử năm 2050 đạt 600 ppm**: Được trình bày chuẩn mực dưới dạng kịch bản mô hình dự báo phát thải mang tính lịch sử của giáo trình gốc khi tiếp tục tiêu thụ nhiên liệu hóa thạch không kiểm soát, tuyệt đối không khẳng định kịch bản 600 ppm vào năm 2050 là một sự thật tất yếu ở mốc thời gian hiện tại 2026.
3. **Dữ liệu Hình 17.30 (a, b)**: Phản ánh trung thực dữ liệu lõi băng Nam Cực 400.000 năm (chưa từng vượt $300\,\mathrm{ppm}$) và thời kỳ công nghiệp vượt $400\,\mathrm{ppm}$, kèm độ tăng nhiệt độ trung bình toàn cầu $0{,}9^\circ\mathrm{C}$ kể từ thập niên 1950 ($\approx 0{,}18\,\mathrm{C^\circ}/\text{thập kỷ}$).

---

## 5. Kết quả thực thi các lệnh kiểm thử tiêu chuẩn (Command Execution & Exit Codes)

1. **Bộ kiểm thử số học và khớp pixel RGB tươi**:
   ```powershell
   C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter17_theory_b.py
   ```
   - **Mã thoát (Exit Code)**: `0`
   - **Kết quả**: `status: "passed"` cho toàn bộ 15 trường hợp kiểm thử số học (Ví dụ 17.5 đến 17.15, TYU 17.5, 17.6, 17.7, ứng dụng sinh học) và 21/21 ảnh PNG khớp pixel tuyệt đối với bản render tươi từ PDF gốc (`diff = 0`).

2. **Công cụ kiểm tra toán học và cú pháp nghiêm ngặt (Strict Math Helper)**:
   ```powershell
   node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . raw_materials/physics/translations/chapter-17/05-nhiet-luong.md raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md raw_materials/physics/translations/chapter-17/17-tom-tat.md
   ```
   - **Mã thoát (Exit Code)**: `0`
   - **Kết quả**:
     - `display`: $91$ khối công thức hiển thị (tất cả đều có độ rộng $\le 25\,\mathrm{ex}$).
     - `inline`: $732$ công thức nội dòng (tất cả đều có độ rộng $\le 27\,\mathrm{ex}$).
     - `findings`: `[]` (Không có bất kỳ cảnh báo hoặc lỗi nào).
     - Không có dấu `$$` bị lệch khỏi cột 0, không có dấu `$` đơn lẻ đứng một mình, không có đường dẫn cục bộ máy tính.

3. **Kiểm tra mô-đun chú thích hình ảnh**:
   ```powershell
   node --input-type=module -e "import('./docs/.vitepress/physics1-17-theory-b-image-annotations.mjs').then(m=>console.log(Object.keys(m)))"
   ```
   - **Mã thoát (Exit Code)**: `0`
   - **Kết quả**: `[ 'physics1Chapter17TheoryBImageAnnotations' ]`

---

## 6. Các vấn đề còn tồn đọng và lỗi định ngạch (Remaining Issues, Unknowns, Quota Errors)

- **Lỗi định ngạch (Quota Errors)**: Không có.
- **Quyền hạn (Permissions)**: Tuân thủ đầy đủ chỉ đạo, không truy cập mạng, không cài đặt gói ngoài, không build toàn cục hay tự ý commit/push.
- **Ranh giới tệp tin (File Boundaries)**: Chỉ thao tác đúng trên 8 tệp thuộc danh mục sở hữu độc quyền và 21 tệp ảnh `b-*.png`, bảo đảm tính nguyên vẹn của toàn bộ hệ thống StudyHub.
