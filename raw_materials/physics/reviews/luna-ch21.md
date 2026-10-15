# Rà độc lập chương 21, Young & Freedman ấn bản 15

## Disposition sau lượt rà trước push, 12/10/2026

Đã đọc lại các đoạn và mở trực tiếp sáu ảnh đã sửa. Các finding dưới đây đã được xử lý trong phạm vi được giao:

- `raw_materials/physics/translations/chapter-21/11-bai-tap-01-30.md`: Đề 21.1 nay gọi đúng “quả cầu nhỏ bằng chì”. Tóm tắt lời giải ngay bên dưới vẫn viết “Cầu chì $m=8.00\,\mathrm g$”, có thể bị hiểu là thiết bị cầu chì. Đổi thành “Quả cầu bằng chì” để nhất quán.
- `raw_materials/physics/translations/chapter-21/14-bai-tong-hop-81-92.md`: Lời giải 21.91 đã khai triển bình phương, tách nghiệm ban đầu $\Delta=0$ và nghiệm quay đầu $\Delta>0$, đồng thời nêu điều kiện $0<\alpha<1$. Finding này đã giải quyết.
- `raw_materials/physics/translations/chapter-21/15-bai-nang-cao-mcat.md`: Lời giải 21.93 đã mở đối xứng, đổi biến và cận ở tích phân trong, rồi nguyên hàm và cận ở tích phân ngoài. Phần (e) vẫn ghi “Khai triển $H(a)$ cho kết quả” sau khi giới thiệu nguyên hàm $H$, nên bước thế $H(a)$ vào $H(\infty)-H(a)$ và khai triển các hạng để ra công thức đóng còn hơi tắt. Công thức đúng, nhưng có thể hiển thị thêm dòng thay thế và rút gọn nếu muốn lời giải tự kiểm tra được từng hạng.

  Dòng rút gọn trung gian cụ thể là:

  $$
H(\infty)-H(a) = L\ln\frac{L+\sqrt{a^2+L^2}}{a}+a-\sqrt{a^2+L^2}.
$$

  Nhân dòng này với $2kQ^2/L^2$ cho biểu thức thế năng đang có.
- `raw_materials/physics/translations/chapter-21/15-bai-nang-cao-mcat.md`: Lời giải 21.97 nay trình bày tích phân tạo trường, tích phân lực trên thanh kia, thế cận và giới hạn xa. Finding này đã giải quyết.
- `docs/vat-ly-2/bai-giang/img/young-21/hinh-21-9.png`, `hinh-21-17.png`, `hinh-21-20.png`, `hinh-21-22.png`, `hinh-21-30.png` và `hinh-p21-96.png`: Đã mở từng crop ở kích thước gốc. Hình 21.9 có đủ chữ “Ground” và ký hiệu đất. Hình 21.17, 21.22 và P21.96 không còn chữ thân bài dính vào hình. Chú thích Hình 21.20 và 21.30 được giữ trọn câu. Không thấy vấn đề mới về nghĩa hoặc nhãn sau khi sửa.

Tính lại độc lập bằng Python cho dữ kiện ví dụ của 21.91 cho $m_{\max}=0.05762\,\mathrm{kg}$, $\Delta_{\max}=0.10689\,\mathrm m$. Bài 21.93 cho $U=5.366\,\mathrm J$, $v_{\mathrm{rel}}=6.552\,\mathrm{m/s}$. Bài 21.97 đúng với công thức đề và giới hạn $a\gg L$. Không sửa các tệp nội dung, ảnh, catalog, CSS hoặc Git trong lượt xác nhận này.

Phạm vi đối chiếu là chương in trang 678–717, tương ứng PDF trang 698–737; phần lời giải đáp số cuối chương dùng phụ lục PDF 1559–1560. Tôi đã đọc quy chuẩn StudyHub, `studyhub-lecture/SKILL.md`, `references/repo-format.md` và `references/teaching-review.md`, kiểm tra nội dung Notes và các include thực tế, xem montage trang nguồn và các montage ảnh đã cắt. Tôi không sửa Notes, catalog, CSS hoặc ảnh.

## Kết quả rà soát

### Findings tại lượt rà ban đầu

1. **Crop Hình 21.9 làm cụt nhãn “Ground”.** Tệp `docs/vat-ly-2/bai-giang/img/young-21/hinh-21-9.png` cắt mất phần dưới của chữ “Ground” và biểu tượng nối đất, trong khi trang nguồn in 684 hiển thị trọn nhãn và ký hiệu. Caption ở `raw_materials/physics/translations/chapter-21/02-vat-dan-cach-dien.md:47` nhận diện vật nối đất nhưng không bù được chữ bị cắt trong hình. Nới crop xuống dưới để giữ đủ nhãn và biểu tượng.

2. **Crop Hình P21.96 dính một mẩu chữ ngoài sơ đồ.** `docs/vat-ly-2/bai-giang/img/young-21/hinh-p21-96.png` có vài nét chữ bị cắt ngay dưới cạnh đáy hình. Trang nguồn in 716 đặt riêng hình tam giác và không có chữ đó trong hình. Đề bài và ảnh được đặt tại `raw_materials/physics/translations/chapter-21/15-bai-nang-cao-mcat.md:157`–`161`. Cắt lại sát phần sơ đồ, bỏ mẩu chữ thừa.

3. **Lời giải 21.91 nhảy qua phép đại số tìm độ sâu quay đầu.** Tại `raw_materials/physics/translations/chapter-21/14-bai-tong-hop-81-92.md:344`, lời giải đi thẳng từ $\alpha\Delta=\sqrt{\Delta^2+R^2}-R$ sang $\Delta_{\max}=2R\alpha/(1-\alpha^2)$. Nên thêm bước bình phương hai vế, khử $R^2$, rồi chia nghiệm khác không: $2R\alpha\Delta=(1-\alpha^2)\Delta^2$. Đây là đúng bước cần mở để sinh viên thấy điều kiện $0<\alpha<1$ và cách chọn nghiệm vật lý.

4. **Lời giải 21.97 không khai triển nguyên hàm và thế cận của tích phân lực.** Tại `raw_materials/physics/translations/chapter-21/15-bai-nang-cao-mcat.md:238`, tích phân trên thanh thứ hai lập đúng nhưng kết quả log được ghi ngay dòng kế. Nên chèn nguyên hàm của hai số hạng $1/(x+a/2)$ và $1/(x+a/2+L)$ cùng phép thế hai cận $a/2$ và $a/2+L$. Kết quả cuối phù hợp công thức đề bài ở trang in 717, nhưng hiện thiếu phần chứng minh mà đề yêu cầu “chứng tỏ”.

5. **Lời giải 21.93 lược hai tích phân cốt lõi của bài thanh song song.** Tại `raw_materials/physics/translations/chapter-21/15-bai-nang-cao-mcat.md:30`–`62`, lời giải nêu tích phân theo $y_1$, ghi kết quả sau tích phân đó, rồi đưa lực tổng cuối cùng sau tích phân theo $y_2$ mà không cho các nguyên hàm/thế cận. Nên mở ít nhất một lần phép thế biến và nguyên hàm ở mỗi tích phân để người học kiểm tra được hệ số 2 và giới hạn $a\gg L$. Phần (e) sau đó dùng công thức thế năng đóng để tính số, nên càng cần chỉ ra liên hệ giữa tích phân lực và kết quả đó.

6. **Bài 21.1 dịch sai vật thể.** `raw_materials/physics/translations/chapter-21/11-bai-tap-01-30.md:10` viết “cầu chì nhỏ”, nghĩa là cầu chì điện. Nguồn trang in 709 ghi “small lead sphere”, tức quả cầu nhỏ bằng chì. Sửa thành “quả cầu chì nhỏ” hoặc “quả cầu nhỏ bằng chì”; phần khối lượng, điện tích, số hiệu nguyên tử và khối lượng mol còn lại đều khớp.

### Không thấy lỗi chặn về nội dung đã spot-check

- Bài 21.62 chủ động nêu đề thiếu hướng điện trường, rồi cho hai cấu hình khác nhau cùng khớp tốc độ cuối và hai giá trị trường 770 N/C, 468 N/C (`13-bai-tong-hop-57-80.md:159`). Tính độc lập bằng công–động năng cho trường thẳng đứng và bằng thời gian rơi cho trường ngang cho đúng hai giá trị này. Cách trình bày tránh gán một đáp số duy nhất cho đề thiếu điều kiện.
- Bài 21.91 ghi rõ phải có $m<m_{\max}$ để hạt quay đầu, không nhận trường hợp bằng ngưỡng (`14-bai-tong-hop-81-92.md:305`). Tính lại với dữ kiện đề cho được $m_{\max}=0.05762$ kg và $\Delta_{\max}=0.10689$ m, phù hợp 57,7 g và 10,7 cm sau làm tròn.
- Bài 21.93 tính thế năng ban đầu 5,366 J. Với hai thanh 0,500 kg chuyển động ngược chiều, bảo toàn động lượng cho $v_{rel}=2\sqrt{U/m}=6.55$ m/s, khớp lời giải `15-bai-nang-cao-mcat.md:18` và hiệu chỉnh trong hồ sơ cũ. Hai tích phân trên các thanh được nêu nhưng phần biến đổi đến biểu thức đóng còn tóm tắt, như mục cần sửa phía trên.
- Bài 21.97 biểu thức lực và giới hạn xa thỏa kiểm tra đại số độc lập. Với $z=L/a\ll1$, $2\ln(1+z)-\ln(1+2z)=z^2+O(z^3)$, do đó $F\sim kQ^2/a^2$ như lời giải ở `15-bai-nang-cao-mcat.md:194`.
- Prerequisites của Notes khớp các khái niệm Wiki: Vector, tích vô hướng, tích có hướng, lực, cân bằng cơ học và đường dòng chất lưu. Các trang Wiki tương ứng đều có mục `Giải thích kỹ thuật`; phép tương tự đường sức và đường dòng được giới hạn đúng, không đồng nhất trường điện với dòng chảy.

## Đối chiếu lý thuyết trang in 678–705

| Trang in / mục | Đơn vị đã so | Kết quả về nội dung, điều kiện và mạch giảng |
| --- | --- | --- |
| 678 / Mở đầu | Câu hỏi nước, động cơ học chương, mục tiêu và kiến thức cần ôn | Đủ năm lựa chọn, nêu đúng lưỡng cực nước, các chủ đề và nền toán/cơ học. Câu hỏi được để mở rồi giải sau mục 21.7 như mạch nguồn. |
| 679–682 / 21.1 | Hổ phách; hai loại điện tích; Caution cùng dấu/trái dấu; máy in laser; cấu tạo nguyên tử; Hình 21.1–21.5; bảo toàn, lượng tử hóa, lực có nguồn gốc điện; câu ôn lại | Các phát biểu, định nghĩa, giá trị khối lượng và độ bất định, mô tả nguyên tử/ion, cơ chế máy in, câu hỏi và đáp án đều khớp. Có Hình 21.1–21.5 và giải thích nhãn/caption. Không thấy mất luận cứ về chuyển electron hoặc hệ kín. |
| 682–684 / 21.2 | Vật dẫn/cách điện/bán dẫn; hưởng ứng và nối đất; phân cực; sơn tĩnh điện; câu ôn lại | Đúng thứ tự cơ chế: Phân bố lại khi thanh đến gần, nối đất khi thanh còn gần, tháo đất trước khi lấy thanh ra. Giải thích đúng vì sao cả lược dương và âm hút vật cách điện trung hòa. Hình 21.6–21.9, ứng dụng và đáp án câu hỏi đều có. Crop nhãn “Ground” của Hình 21.9 bị cắt đã ghi ở mục ảnh. |
| 685–689 / 21.3 | Định luật Coulomb, điều kiện điện tích điểm và chân không, SI/epsilon-zero, xấp xỉ không khí; ứng dụng xơ nang; Ví dụ 21.1–21.4; nguyên lý chồng chất; chiến lược 21.1; câu ôn lại | Độ lớn, dấu/hướng, định luật III Newton, quy đổi SI, giới hạn do vật chất giữa nguồn và con số hiệu chỉnh không khí đều được giữ. Ví dụ 1–4, bước vector và thành phần, đối xứng, phần hướng dẫn bài giải, ứng dụng và đáp án câu ôn lại đều có. |
| 690–694 / 21.4 | Ý tưởng trường, điện tích thử, quan hệ lực–trường, tương tự trọng trường; Caution cho vật tích điện lớn; trường điện tích điểm và hướng $\hat r$; trường vector/đều; vật dẫn; ứng dụng cá mập; Ví dụ 21.5–21.7; câu ôn lại | Phân biệt điểm nguồn/điểm trường, dấu điện tích thử, trường do nguồn khác tạo và hướng trường điểm âm/dương đều chính xác. Giữ điều kiện trường bên trong vật liệu dẫn ở cân bằng tĩnh điện và ngoại lệ lỗ rỗng. Ba ví dụ và đáp án câu hỏi giữ đủ dữ kiện, đơn vị, dấu và hướng. |
| 695–699 / 21.5 | Chồng chất trường; mật độ $\lambda,\sigma,\rho$; chiến lược 21.2; Ví dụ 21.8–21.12; Caution trường không phải dòng chảy; câu ôn lại | Tổng vector, khai triển tổng hữu hạn, đơn vị mật độ, cận tích phân, lập luận đối xứng, giới hạn trường xa/gần và cộng trường hai mặt đều được trình bày. Các điều kiện $x>0$, $x\gg a$, $a\gg x$, $R\gg x$ được nêu. Câu ôn lại và hướng $-y$ có lập luận thành phần. |
| 700–701 / 21.6 | Định nghĩa đường sức, mật độ biểu thị độ lớn định tính, hình ba cấu hình, hạt cỏ phân cực, Caution quỹ đạo, câu ôn lại | Giữ rõ tính tương tự toán học nhưng không có vật chất chảy; không suy ra độ lớn trường không đổi dọc một đường; giữ cảnh báo quỹ đạo khác đường sức và điều kiện đường thẳng cho đáp án câu hỏi. Hình 21.27–21.29 và phần quan sát bằng hạt cỏ có mặt. |
| 701–705 / 21.7 | Định nghĩa lưỡng cực; nước/dung môi; mômen, mômen lực, cân bằng; thế năng; trường không đều; cá dao điện; Ví dụ 21.13–21.14; câu ôn lại | Hướng $\vec p$ từ âm sang dương, $\vec\tau=\vec p\times\vec E$, bền/không bền, $U=-\vec p\cdot\vec E$, giả thiết trường đều cho hợp lực bằng không, và gần đúng xa $1/r^3$ đều khớp. Câu mở đầu, ứng dụng, hai ví dụ và đáp án không làm mất giả thiết chính. |

Đã rà trực tiếp OCR theo tất cả trang PDF 698–725 và so nội dung với bảy tệp lý thuyết, phần mở đầu, hình và câu hỏi tương ứng. Một số phép tính minh họa được tính lại bằng Python độc lập: Ví dụ 21.1 cho $3.1275\times10^{35}$, Ví dụ 21.3 cho $-28.09\,\mu\mathrm N$, Ví dụ 21.4 cho $0.4602\,\mathrm N$, các điểm a/b/c của Ví dụ 21.8 lần lượt cho khoảng $9.74\times10^4$, $-6.19\times10^4$, $4.91\times10^3\,\mathrm{N/C}$, và Ví dụ 21.13 cho $\tau=5.74\times10^{-24}\,\mathrm{N,m}$, $U=8.19\times10^{-24}\,\mathrm J$. Các giá trị khớp số làm tròn trong bài.

## Sổ tính đầy đủ

| Đơn vị nguồn | Nơi đến được xác nhận | Ghi chú |
| --- | --- | --- |
| Mở đầu, trang in 678 | `00-mo-dau.md`, include trong Notes chính | Có tình huống tĩnh điện, mục tiêu học, kiến thức cần ôn và câu hỏi nước; lời giải được đặt sau phần lưỡng cực. |
| Mục 21.1–21.7, trang in 679–705 | Bảy include lý thuyết trong `translations/chapter-21/01` đến `07`, hiển thị qua TopicMap | Các ví dụ đánh số 21.1–21.14, công thức đánh số 21.1–21.18 và hình lý thuyết 21.1–21.34 được đối chiếu qua trang/tiêu đề và bộ ảnh. |
| Tóm tắt, trang in 706 | `08-tom-tat.md`, include trong Notes chính | Đủ các nhóm điện tích, Coulomb, điện trường, chồng chất, đường sức và lưỡng cực. |
| Luyện tập có hướng dẫn, trang in 707 | `09-luyen-tap-huong-dan.md`, đặt trong khu Bài tập | 12 biến thể theo ví dụ và một bài tổng hợp nửa vòng. |
| 23 câu thảo luận, trang in 708 | `10-cau-hoi-thao-luan.md`, trong khu Bài tập | Tệp có các câu Q21.1–Q21.23. |
| 101 bài 21.1–21.101, trang in 709–717 | Các include `11`–`15`, trong khu Bài tập | Đã kiểm tra đủ ID 1–101 và có lời giải gập cho từng ID. Phần đáp số cuối chương nằm trong include riêng. |
| Đáp số, trang in 717 và phụ lục A-14–A-15 | `16-dap-an-cuoi-chuong.md`, `17-dap-so-bai-le.md` | Có đáp án câu mở đầu, biến thể có hướng dẫn và đáp số bài lẻ. Các bài được nêu sai khác với phụ lục có ghi rõ điều kiện hoặc dữ kiện, gồm 21.62, 21.91, 21.93. |

### Đối chiếu từng đề cuối chương

| Trang in / PDF | ID đã so đề | Kết quả đối chiếu đề |
| --- | --- | --- |
| 709 / 729 | 21.1–21.19 | Đủ mọi câu và ý nhỏ; 21.1 dùng sai từ “cầu chì” cho quả cầu bằng chì. Dữ kiện khác, các tổ hợp điện tích DNA và khoảng cách được giữ. |
| 710 / 730 | 21.20–21.34 | Đủ dữ kiện, hướng trường/chuyển động, ý nhỏ và hình được gọi tên. Đã mở trang ảnh để phân biệt các thời gian micro giây ở 21.21 và 21.24 với mili giây. |
| 711 / 731 | 21.35–21.49 | Khớp giá trị điện tích, tọa độ, dấu, yêu cầu thành phần/độ lớn/hướng và các hình E21.34, E21.37–E21.41. |
| 712 / 732 | 21.50–21.63 | Khớp mật độ, hình học dây/vòng/lưỡng cực, các mục a–c và hình. Bài 21.62 đúng là thiếu hướng trường ở đề; lời giải nhận diện thiếu điều kiện và đưa trường hợp có điều kiện. |
| 713 / 733 | 21.64–21.77 | Khớp điều kiện lực/chiều trường, các giá trị, đơn vị và mọi mục con. Giữ các yêu cầu ước lượng ở 21.65–21.66 và gợi ý/giới hạn mô hình ở các bài liên quan. |
| 714 / 734 | 21.78–21.87 | Khớp kích thước bản, đoạn quan sát, giới hạn xa, khoảng cách, hai phía trục và yêu cầu dao động; các hình P21.78–P21.87 đều được chèn. |
| 715 / 735 | 21.88–21.92 | Khớp bối cảnh thiết kế máy in, dữ liệu đo và cả hai đồ thị ở 21.90, cùng các điều kiện quay đầu và mômen ở 21.91–21.92. |
| 716 / 736 | 21.93–21.100 | Khớp các cấu hình thanh/điện tích, từng mục a–g, hình học 21.95–21.96, phần MCAT và bốn phương án đường sức 21.100. Crop P21.96 có mẩu chữ thừa, đã ghi riêng ở trên. |
| 717 / 737 | 21.101 | Khớp $+40$ pC, thân cây 30 cm, khoảng cách gần nhất 15 cm và đủ bốn lựa chọn đơn vị N/C; hình P21.100 của câu trước xuất hiện đầy đủ trên trang nguồn. |

> **Giới hạn rà soát:** Đã đối chiếu lần lượt toàn bộ đề 21.1–21.101 theo bản dịch và PDF trang 729–737, gồm dữ kiện, đơn vị, dấu/hướng, mọi ý nhỏ, tình huống, gợi ý và hình được gọi. Đã mở ảnh nguồn cả chín trang bài tập và mở trực tiếp hai crop có vấn đề. Lời giải không được đọc line-by-line cho cả 101 bài; phần tính đúng toán được spot-check ở các bài tích phân, điều kiện đề thiếu và ngưỡng quay đầu nêu trên.
