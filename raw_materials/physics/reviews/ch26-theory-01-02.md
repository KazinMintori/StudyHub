# Rà soát bản chuẩn bị Chương 26.1–26.2

## Phạm vi và căn cứ đối chiếu

Đã đối chiếu hai bản dịch với PDF cục bộ tại source/young-freedman-15.pdf và văn bản QA qa/physics/full-source/pdf-0864.txt đến pdf-0874.txt. Trang in 844 tương ứng PDF một-based 864, tức chỉ số PyMuPDF 863. Phạm vi bao phủ trọn Mục 26.1 và Mục 26.2, kể cả câu tự kiểm cuối mỗi mục. Trang in 855 / PDF 875 mở đầu Mục 26.3 và nằm ngoài phạm vi.

| Đơn vị nguồn | Trạng thái | Nội dung đã chuyển |
| --- | --- | --- |
| 26.1, trang in 844–846 / PDF 864–866 | Đạt | Mở đầu về ứng dụng điện trở, bốn cấu hình ở Hình 26.1, điện trở tương đương, mạch nối tiếp và song song, phương trình (26.1)–(26.4), quan hệ giữa dòng nhánh và điện trở. Giữ hai cảnh báo phân biệt quy tắc điện trở với tụ điện và ứng dụng đèn ô tô mắc song song. |
| Chiến lược 26.1, trang in 847 / PDF 867 | Đạt | Đủ các bước nhận diện, bố trí, thực hiện và đánh giá mạng nối tiếp/song song. |
| Ví dụ 26.1, trang in 847–848 / PDF 867–868 | Đạt | Giữ mạng 4 Ω nối tiếp với cặp 6 Ω và 3 Ω song song, quá trình rút gọn rồi khôi phục dòng và hiệu điện thế. Các kết quả Req = 6 Ω, I = 3 A, Vcb = 6 V, I6 = 1 A và I3 = 2 A đã được tính độc lập. |
| Ví dụ 26.2, trang in 848–849 / PDF 868–869 | Đạt | Giữ hai cách mắc, dòng điện, hiệu điện thế, công suất từng bóng và toàn mạng, tình huống một bóng đứt, giới hạn của mô hình bóng có điện trở không đổi và so sánh độ sáng. |
| Câu tự kiểm 26.1, trang in 849 / PDF 869 | Đạt | Giữ cả bốn phương án xếp hạng và lời giải cho các điện trở tương đương 3R, R/3, 3R/2 và 2R/3. |
| 26.2, trang in 849–851 / PDF 869–871 | Đạt | Giữ lý do cần quy tắc Kirchhoff, định nghĩa nút và vòng kín, cơ sở bảo toàn điện tích và tính bảo toàn của lực tĩnh điện, phương trình (26.5), (26.6), quy ước dấu, cảnh báo dòng điện không chia đều và toàn bộ Chiến lược 26.2. |
| Ví dụ 26.3, trang in 851–852 / PDF 871–872 | Đạt | Giữ mạch một vòng, chiều dòng giả định, hai đường tính Vab, công suất hai suất điện động, ý nghĩa pin đang nạp, công suất tỏa nhiệt và ứng dụng khởi động xe. |
| Ví dụ 26.4, trang in 852 / PDF 872 | Đạt | Giữ ba ẩn, phương trình nút, các phương trình vòng, cực tính thực của pin và ba cách tính Vba. |
| Ví dụ 26.5, trang in 853 / PDF 873 | Đạt | Giữ công suất suất điện động, điện trở trong bộ nguồn, công suất thuần, pin đang nạp, bóng đèn và phép cân bằng công suất. Bản dịch phân biệt phần tỏa nhiệt với năng lượng được lưu trữ trong pin để các con số trong ví dụ nhất quán. |
| Ví dụ 26.6, trang in 853 / PDF 873 | Đạt | Giữ ba phương trình vòng (1)–(3), hai phương trình rút gọn (1′), (2′), phép khử ẩn, năm dòng nhánh, chiều thực của I3, điện trở tương đương và phép thế kiểm tra dấu. |
| Câu tự kiểm 26.2 và Ví dụ 26.7, trang in 854 / PDF 874 | Đạt | Giữ câu hỏi trừ phương trình, lời giải xác định đường c→b→d→a→c và tính phụ thuộc của phương trình. Ví dụ 26.7 giữ hai đường tính Vab = −1 V và kết luận mọi đường nối cùng hai điểm cho một hiệu điện thế. |

## Kiểm tra tính toán

Đã chạy python -X utf8 -I raw_materials/physics/verify_chapter26_01_02.py. Script dùng thư viện chuẩn, tính lại các kết quả số trong Ví dụ 26.1–26.7 và câu tự kiểm, kiểm tra dòng tại nút, dấu hiệu điện thế theo đường đi, ba phương trình vòng của mạch cầu và cân bằng công suất. Tất cả kiểm tra số và dấu đều đạt.

Các mốc chính được xác nhận: Cặp 6 Ω song song 3 Ω có điện trở tương đương 2 Ω. Toàn mạng Ví dụ 26.1 có Req = 6 Ω và dòng 3 A. Hai bóng nối tiếp tiêu thụ 8 W mỗi bóng, còn hai bóng song song tiêu thụ 32 W mỗi bóng. Trong Ví dụ 26.3, I = 0,5 A, Vab = 9,5 V, công suất hai suất điện động là 6 W và −2 W. Trong Ví dụ 26.4–26.5, I = 3 A, r = 2 Ω, E = −5 V, Vba = 6 V và công suất thuần 18 W = 5 W + 1 W + 12 W. Với mạch cầu, (I1,I2,I3) = (6,5,−1) A, hai dòng nhánh còn lại là 7 A và 4 A, dòng nguồn là 11 A, Req = 13/11 Ω ≈ 1,2 Ω.

## Rà soát MathJax sau chỉnh sửa

Đã sửa khối phương trình (26.2) bị thiếu môi trường căn lề, viết lại phép song song hai điện trở với căn lề hợp lệ, và khai triển ba số hạng đầu trước tổng có miền chỉ số $i=1,\ldots,n$. Phần giải thích bằng lời cho (26.4) đã được chuyển ra ngoài TeX. Các phép tính dài trong Ví dụ 26.1–26.6 được ngắt tại dấu bằng hoặc phép cộng.

MathJax đã phân tích 27 khối hiển thị của bản 26.1 và 34 khối hiển thị của bản 26.2. Không có khối lỗi cú pháp hoặc rộng quá 30ex. Bề rộng lớn nhất lần lượt là 29,838ex và 29,720ex. Kiểm tra riêng công thức nội dòng cho 104 biểu thức và 171 biểu thức, không có biểu thức nào lỗi hoặc rộng quá 38ex; bề rộng lớn nhất là 33,207ex và 21,311ex. Các số hiệu (26.1)–(26.6) mỗi số xuất hiện đúng một lần. Sau chỉnh sửa, verify_chapter26_01_02.py chạy đạt, gồm các kiểm tra công suất và phương trình nút, vòng.

## Danh sách hình và nhãn tiếng Anh cần dịch

Hai bản dịch đã gắn đường dẫn dự kiến cho hình 26.1–26.12 dưới img/young-26/. Cần crop các hình và thay nhãn tiếng Anh bên trong ảnh theo bảng dưới đây trước khi tích hợp Notes.

| Hình, trang in | Caption tiếng Anh trong PDF | Caption tiếng Việt | Nhãn tiếng Anh nằm trong hình cần dịch hoặc giữ |
| --- | --- | --- | --- |
| 26.1, tr. 845 | “Four different ways of connecting three resistors.” | Bốn cách mắc ba điện trở. | Các phần (a)–(d), R1, R2, R3, a, b, x, y, I. |
| 26.2, tr. 846 | “A car’s headlights and taillights are connected in parallel. Hence each light is exposed to the full potential difference supplied by the car’s electrical system, giving maximum brightness. Another advantage is that if one headlight or taillight burns out, the other one keeps shining (see Example 26.2).” | Đèn pha và đèn hậu ô tô mắc song song. Mỗi đèn nhận toàn bộ hiệu điện thế của hệ thống điện trên xe và đạt độ sáng tối đa. Nếu một đèn hỏng, các đèn còn lại vẫn sáng (xem Ví dụ 26.2). | Không thấy nhãn đại lượng trong ảnh. |
| 26.3, tr. 847–848 | “Steps in reducing a combination of resistors to a single equivalent resistor and finding the current in each resistor.” | Các bước rút gọn tổ hợp điện trở thành một điện trở tương đương và tìm dòng qua từng điện trở. | Các phần (a)–(f), E = 18 V, r = 0, 4 Ω, 6 Ω, 3 Ω, 2 Ω, a, b, c. |
| 26.4, tr. 848 | “Our sketches for this problem.” | Sơ đồ dùng cho bài toán này. | “(a) Light bulbs in series”, “(b) Light bulbs in parallel”, a, b, c, d, e. |
| 26.5, tr. 849 | “When connected to the same source, two incandescent light bulbs in series (shown at top) draw less power and glow less brightly than when they are in parallel (shown at bottom).” | Hai bóng dây tóc nối tiếp ở phía trên nhận công suất nhỏ hơn và sáng yếu hơn khi mắc song song ở phía dưới, khi cùng nối với một nguồn. | Không thấy nhãn đại lượng trong ảnh. |
| 26.6, tr. 849–850 | “Two networks that cannot be reduced to simple series-parallel combinations of resistors.” | Hai mạng không thể rút gọn thành các tổ hợp điện trở nối tiếp/song song đơn giản. | “Junction”, “Not a junction”, “Loop 1”, “Loop 2”, “Loop 3”, (1)–(4), E1, E2, r1, r2, R, R1–R4, Rm, a–f. |
| 26.7, tr. 850 | “Kirchhoff’s junction rule states that as much current flows into a junction as flows out.” | Quy tắc nút Kirchhoff nói rằng dòng điện đi vào nút bằng dòng điện đi ra. | “(a) Kirchhoff’s junction rule”, “(b) Water-pipe analogy”, “Junction”, I1, I2, I1 + I2. |
| 26.8, tr. 850 | “Use these sign conventions when you apply Kirchhoff’s loop rule. In each part of the figure ‘Travel’ is the direction that we imagine going around the loop, which is not necessarily the direction of the current.” | Dùng quy ước dấu khi áp dụng quy tắc vòng Kirchhoff. “Chiều đi” là chiều giả định khi đi quanh vòng và không nhất thiết trùng với chiều dòng điện. | “(a) Sign conventions for emfs”, “(b) Sign conventions for resistors”, “Travel”, +E, −E, +IR, −IR, R, I, các cực + và −. |
| 26.9, tr. 851 | “Applying the junction rule to point a reduces the number of unknown currents from three to two.” | Áp dụng quy tắc nút tại điểm a làm giảm số dòng điện chưa biết từ ba xuống hai. | “(a) Three unknown currents: I1, I2, I3”, “(b) Applying the junction rule to point a eliminates I3”, I1 + I2, I1, I2, I3, a, R1–R3, r1, r2, E1, E2. |
| 26.10, tr. 851–852 | “(a) In this example we travel around the loop in the same direction as the assumed current, so all the IR terms are negative. The potential decreases as we travel from + to − through the bottom emf but increases as we travel from − to + through the top emf. (b) A real-life example of a circuit of this kind.” | (a) Chiều đi quanh vòng trùng với chiều dòng điện giả định nên mọi số hạng IR đều âm. Đi qua nguồn dưới từ cực + đến cực − thì điện thế giảm, còn đi qua nguồn trên từ cực − đến cực + thì điện thế tăng. (b) Tình huống thực tế tương tự. | “Travel”, “Dead battery”, “Live battery”, các cực +, −, 12 V, 4 V, 2 Ω, 3 Ω, 4 Ω, 7 Ω, I, a, b. |
| 26.11, tr. 852 | “In this circuit a power supply charges a run-down battery and lights a bulb. An assumption has been made about the polarity of the emf of the battery. Is this assumption correct?” | Bộ nguồn nạp pin yếu và làm sáng bóng đèn. Cực tính của suất điện động pin đã được giả định. Giả định đó có đúng không? | 12 V, 1 A, I, a, b, r, 2 A, E, 1 Ω, 3 Ω, các vòng (1)–(3), cực +. |
| 26.12, tr. 853 | “A network circuit with several resistors.” | Mạng điện gồm nhiều điện trở. | I1, I2, I3, I1−I3, I2+I3, I1+I2, 13 V, 2 Ω, bốn điện trở 1 Ω, a–d, các vòng (1)–(3). |

## Giới hạn rà soát

Đây là nguyên liệu cho hai mục 26.1–26.2. Chương 26 còn phần mở đầu, Mục 26.3–26.5, tóm tắt, hướng dẫn thực hành, câu hỏi thảo luận và hệ bài tập. Những phần đó chưa nằm trong hai bản dịch này. Hình mới có đường dẫn dự kiến, chưa có crop nên chưa kiểm tra chữ Việt trực tiếp trên ảnh hoặc bề rộng 320 px.
