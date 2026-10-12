# Rà nguồn và tính toán: Chương 25.3–25.4

## Phạm vi

Đối chiếu hai bản thảo Notes raw:

- `translations/chapter-25/03-dien-tro.md`: Mục 25.3, trang in 819–822, PDF 839–842.
- `translations/chapter-25/04-suat-dien-dong.md`: Mục 25.4, trang in 822–827, PDF 842–847.

Nguồn chữ là các tệp `qa/physics/full-source/pdf-0839.txt` đến `pdf-0847.txt`. Tôi cũng render contact sheet các trang PDF 839–847 và xem các sơ đồ, bảng màu, đồ thị mạch cùng ảnh ứng dụng. Các phép tính trong ví dụ số được kiểm tra bằng `verify_chapter25_03_04.py`.

## Sổ nội dung theo đơn vị nguồn

| Đơn vị | Trang in / PDF | Nội dung được đưa vào Notes |
| --- | --- | --- |
| Mục 25.3, dẫn nhập và Hình 25.7 | 819 / 839 | Quan hệ vector $\vec E=\rho\vec J$; điều kiện Ohm; dây đồng chất tiết diện đều; $I=JA$, $V=EL$; chiều dòng điện từ điện thế cao đến thấp; sự truyền thế năng cho mạng tinh thể khi va chạm. |
| Kiểm tra mục 25.2 đặt trước mục 25.3 | 819 / 839 | Câu hỏi về mẫu bán dẫn khi hạ nhiệt độ mà giữ E không đổi, đủ ba lựa chọn và giải thích $J=E/\rho$. |
| Điện trở, Hình 25.8, Hình 25.9, Bảng 25.3 | 820 / 840 | Dẫn xuất $R=\rho L/A$; định nghĩa $R=V/I$; phân biệt định luật Ohm với định nghĩa điện trở; đơn vị Ω, kΩ, MΩ; ví dụ dây đồng gia dụng và bóng đèn; sự tương tự áp suất–lưu lượng với giới hạn; mã màu đủ mười chữ số và hệ số nhân; ví dụ 5.7 kΩ, dung sai không vòng/bạc/vàng; công suất cực đại. |
| Nhiệt độ và đồ thị I–V | 820–821 / 840–841 | Công thức gần đúng $R(T)=R_0[1+\alpha(T-T_0)]$, miền áp dụng và ý nghĩa $\Delta R$; điện trở linh kiện; Hình 25.10; đặc trưng điôt thuận/ngược, chỉnh lưu và logic; đảo dấu V đổi chiều dòng ở phần tử Ohm. |
| Ví dụ 25.2, 25.3 và câu hỏi cuối mục | 821–822 / 841–842 | Bài dây đồng giữ đủ ba đại lượng E, V, R và hai cách kiểm tra R; bài phụ thuộc nhiệt độ giữ mốc 20°C, hệ số đồng, kết quả ở 0°C và 100°C; giải thích vì sao tăng gấp đôi điện áp ở dây nóng không làm dòng tăng gấp đôi. |
| Mạch hở, nguồn và suất điện động | 822–823 / 842–843 | Điện tích hai đầu vật dẫn cô lập tạo trường ngược và triệt dòng; nhu cầu mạch kín và cơ chế đưa điện tích lên thế năng cao; tương tự đài phun; định nghĩa emf là công/năng lượng trên một đơn vị điện tích, không phải lực; đơn vị volt; ví dụ 1.5 J/C; các loại nguồn và dạng năng lượng được chuyển hóa; lực không tĩnh điện trong pin, máy phát và máy tĩnh điện; lập luận $V_{ab}=\mathcal E$ cho nguồn lý tưởng; dòng và sụt áp trong vòng lý tưởng. |
| Bảo toàn dòng, điện trở trong và ứng dụng sinh học | 824–825 / 844–845 | Cảnh báo dòng điện không bị tiêu thụ; điện trở trong r và dấu trong $V_{ab}=\mathcal E-Ir$; khi hở mạch/đang cấp dòng/đang nạp; suy ra $I=\mathcal E/(R+r)$; pin không là nguồn dòng cố định; điện trở trong không tách rời nguồn; ứng dụng cá đuối điện gồm khoảng 0.05 V mỗi tế bào, hàng nghìn tế bào, đến 200 V, 30 A trong vài ms, hơn nửa khối lượng cơ thể và ghi chú lịch sử chữa đau đầu/gút được giữ. |
| Bảng 25.4 và Ví dụ khái niệm 25.4, Ví dụ 25.5 | 825–826 / 845–846 | Ký hiệu dây, R, emf, nguồn kèm r, vôn kế và ampe kế; điện trở lý tưởng của từng dụng cụ; mạch hở 12 V, r=2 Ω cho chỉ số 12 V và 0 A; mạch kín thêm 4 Ω cho dòng 2 A, điện áp đầu cực 8 V; sụt áp trên dây lý tưởng bằng không. |
| Ví dụ khái niệm 25.6 và Ví dụ 25.7 | 826–827 / 846–847 | Cả hai cách đặt meter: vôn kế song song đo 8 V, ampe kế nối tiếp đọc 2 A; vôn kế mắc nối tiếp mở mạch cho 12 V và 0 A; ngắn mạch có V=0, I=6 A; giải thích mối nguy của dòng ngắn mạch. |
| Quy tắc điện thế quanh vòng và kiểm tra cuối mục 25.4 | 827 / 847 | Tổng đại số tăng/giảm điện thế bằng không; đồ thị Hình 25.20; mạch phi tuyến cần giải số; giới hạn gần đúng của mô hình emf và r; khác biệt pin cũ và ắc quy lạnh; câu hỏi xếp hạng ba mạch với giải thích tính cả ba dòng. |

## Sổ hình, bảng và chú giải để tích hợp

Các tên đường dẫn dưới đây là quy ước crop đang dùng trong Notes. Cần đặt crop tương ứng vào `docs/vat-ly-2/bai-giang/img/young-25/`. Hình cá đuối là ảnh ứng dụng không mang số hình trong tài liệu, không gọi thành Figure 25.15a.

| Nguồn | Crop dùng trong Notes | Chú giải tiếng Việt dưới hình |
| --- | --- | --- |
| Figure 25.7, trang in 819 / PDF 839: *A conductor with uniform cross section. The current density is uniform over any cross section, and the electric field is constant along the length.* | `hinh-25-07.png` | Dây đồng chất, tiết diện đều; J đồng đều trên từng mặt cắt và E không đổi dọc dây. Dòng quy ước từ điện thế cao đến thấp. |
| Figure 25.8, trang in 820 / PDF 840: *A long fire hose offers substantial resistance to water flow...* | `hinh-25-08.png` | Ống cứu hỏa dài cản dòng; cần chênh áp lớn để có lưu lượng mạnh, tương tự hiệu điện thế cần thiết để duy trì dòng qua dây dài. |
| Figure 25.9, trang in 820 / PDF 840: *This resistor has a resistance of 5.7 kΩ with an accuracy (tolerance) of ±10%.* | `hinh-25-09.png` | Các vòng màu cho trị số điện trở 5.7 kΩ và dung sai ±10%. |
| Table 25.3, trang in 820 / PDF 840: *Color Codes for Resistors.* | Bảng Markdown trong Notes, không cần crop | Bảng mã đủ màu đen đến trắng, chữ số 0–9 và hệ số nhân từ $10^0$ đến $10^9$. |
| Figure 25.10, trang in 821 / PDF 841: *Current–voltage relationships for two devices. Only for a resistor that obeys Ohm’s law as in (a) is current I proportional to voltage V.* | `hinh-25-10.png` | Đồ thị I–V của điện trở Ohm là đường thẳng; điôt có đáp ứng phi tuyến và khác nhau theo chiều. |
| Figure 25.11, trang in 822 / PDF 842: *If an electric field is produced inside a conductor that is not part of a complete circuit, current flows for only a very short time.* | `hinh-25-11.png` | Điện tích tích tụ tại đầu dây cô lập tạo trường ngược; khi trường tổng triệt tiêu, dòng điện dừng. |
| Figure 25.12, trang in 822 / PDF 842: *Just as a water fountain requires a pump, an electric circuit requires a source of electromotive force to sustain a steady current.* | `hinh-25-12.png` | Máy bơm nâng nước tuần hoàn; nguồn suất điện động duy trì dòng bằng cách đưa điện tích lên thế năng cao. |
| Figure 25.13, trang in 823 / PDF 843: *Schematic diagram of a source of emf in an “open-circuit” situation...* | `hinh-25-13.png` | Nguồn hở: Lực điện và lực không tĩnh điện cân bằng trên điện tích dương, không có chuyển động thuần qua hai cực. |
| Figure 25.14, trang in 823 / PDF 843: *Schematic diagram of an ideal source of emf in a complete circuit...* | `hinh-25-14.png` | Nguồn lý tưởng trong mạch kín; dòng ngoài đi từ a đến b, dòng trong nguồn đi từ b đến a. |
| Ảnh trong ứng dụng Bio *Danger: Electric Ray!*, trang in 824 / PDF 844 | `anh-ca-duoi-dien.png` | Cá đuối điện phát xung nhờ các tế bào electroplaque chuyên hóa xếp chồng. Đây là ảnh không đánh số. |
| Figure 25.15, trang in 824 / PDF 844: *The emf of this battery—that is, the terminal voltage when it’s not connected to anything—is 12 V...* | `hinh-25-15.png` | Điện áp không tải của pin là 12 V; khi cấp dòng, điện trở trong làm điện áp đầu cực nhỏ hơn emf. |
| Table 25.4, trang in 825 / PDF 845: *Symbols for Circuit Diagrams.* | Bảng Markdown trong Notes, không cần crop | Ký hiệu dây, điện trở, nguồn, nguồn có r, vôn kế và ampe kế, kèm đặc tính lý tưởng. |
| Figure 25.16, trang in 825 / PDF 845: *A source of emf in an open circuit.* | `hinh-25-16.png` | Mạch hở với emf 12 V và r=2 Ω; ampe kế bằng 0 A, vôn kế chỉ emf 12 V. |
| Figure 25.17, trang in 825–826 / PDF 845–846: *A source of emf in a complete circuit.* | `hinh-25-17.png` | Nguồn 12 V, r=2 Ω cấp cho tải 4 Ω; dòng 2 A và điện áp đầu cực 8 V. |
| Figure 25.18, trang in 826 / PDF 846: *Different placements of a voltmeter and an ammeter in a complete circuit.* | `hinh-25-18.png` | So sánh đo đúng khi vôn kế song song với đo làm hở mạch khi mắc vôn kế lý tưởng nối tiếp. |
| Figure 25.19, trang in 826 / PDF 846: *Our sketch for this problem.* | `hinh-25-19.png` | Dây điện trở không làm nối tắt hai cực nguồn; V đầu cực bằng 0 và dòng chỉ do r giới hạn. |
| Figure 25.20, trang in 827 / PDF 847: *Potential rises and drops in a circuit.* | `hinh-25-20.png` | Đồ thị tăng emf rồi giảm qua điện trở trong và ngoài; sau một vòng điện thế trở về giá trị đầu. |

## Tính toán độc lập

`verify_chapter25_03_04.py` tính lại bằng Python và kiểm tra các đẳng thức chính:

- Ví dụ 25.2: $J=2.044\times10^6$ A/m², $E=0.0352$ V/m, $V=1.758$ V, $R=1.05263$ Ω. Kết quả làm tròn theo độ chính xác dữ kiện là 0.0352 V/m, 1.76 V và 1.05 Ω. Hai cách tính điện trở $\rho L/A$ và $V/I$ khớp.
- Ví dụ 25.3: $R(0^\circ\mathrm C)=0.96747$ Ω, $R(100^\circ\mathrm C)=1.38012$ Ω, tỉ số 1.42652. Dùng kết quả làm tròn hai chữ số có nghĩa sẽ cho tỉ số khoảng 1.42 và mức tăng 42%, đúng cách ghi trong phần đánh giá nguồn. Dùng số chưa làm tròn cho mức tăng xấp xỉ 42.7%.
- Ví dụ khái niệm 25.4: Mạch hở cho $(V_{ab},I)=(12\,\mathrm V,0\,\mathrm A)$.
- Ví dụ 25.5: Mạch tải cho $(V_{ab},I)=(8\,\mathrm V,2\,\mathrm A)$.
- Ví dụ khái niệm 25.6: Cách mắc (a) cho $(8\,\mathrm V,2\,\mathrm A)$; mắc vôn kế nối tiếp ở (b) cho $(12\,\mathrm V,0\,\mathrm A)$.
- Ví dụ 25.7: Ngắn mạch cho $(V_{ab},I)=(0\,\mathrm V,6\,\mathrm A)$.
- Câu hỏi cuối mục 25.4: Các dòng là 1 A, 2 A và 5 A, nên thứ tự là (iii), (ii), (i).

## Giới hạn QA

Đã đối chiếu văn bản đủ các tiểu mục, ví dụ, câu hỏi, cảnh báo, ứng dụng và bảng trên trang 819–827. Đã xem contact sheet PDF gốc ở kích thước thu nhỏ để kiểm tra bố cục và mối liên hệ giữa sơ đồ với phần giải thích. Các crop theo đường dẫn trong sổ hình chưa có sẵn trong repo tại thời điểm viết, vì vậy chưa xác nhận crop cuối cùng, độ nét nhãn hay render Notes ở chiều rộng điện thoại. Chưa chạy build hoặc kiểm tra toàn bộ Chương 25. Báo cáo này chỉ kết luận trong phạm vi hai mục 25.3–25.4.
