# Rà soát phần lý thuyết 26.3–26.4

Ngày rà: 12-10-2026.

## Phạm vi và kết luận

Đã đối chiếu hai tệp raw 26.3 và 26.4 với *University Physics with Modern Physics*, ấn bản 15. Phạm vi nguồn là trang in 854–863, tương ứng PDF một-based 874–883. Hai tệp giữ các định nghĩa, mạch suy luận, điều kiện đầu và cuối, ứng dụng, hình, ví dụ có đủ tiểu mục, các ý chính và câu hỏi kiểm tra của hai phần.

Đã chạy bộ tính độc lập bằng Python cho hai cấu hình đo điện trở, các bộ chia dòng và điện áp của ampe kế/vôn kế, các giá trị nạp và phóng tụ, cùng các tích phân điện tích và năng lượng. Tất cả giá trị trong ví dụ khớp với nguồn ở mức làm tròn đã nêu. Công thức hiển thị đã được render bằng MarkdownItMathJax để đo bề rộng. Chưa kiểm tra crop ảnh, build trang hoặc responsive layout. Báo cáo này không nghiệm thu toàn chương 26.

| Phần | Trang in / PDF | Nội dung đã đối chiếu |
| --- | --- | --- |
| 26.3 Dụng cụ đo điện | 854–858 / 874–878 | Điện kế d’Arsonval, dòng toàn thang, ampe kế và điện trở rẽ, vôn kế và điện trở nối tiếp, hai cách mắc đo điện trở, ôm kế, đồng hồ số, điện cơ đồ, chiết áp cân bằng và câu hỏi kiểm tra. |
| 26.4 Mạch R-C | 858–863 / 878–883 | Điều kiện ban đầu của tụ, mạch nạp và phóng, quy tắc vòng kín, tích phân suy ra $q(t)$ và $i(t)$, giới hạn dài hạn, hằng số thời gian, ứng dụng bộ kích nhịp tim, cân bằng năng lượng, hai ví dụ đủ các ý và câu hỏi kiểm tra. |

## Hình cần crop và bản dịch chú thích

Các đường dẫn dưới đây đã được đặt trong raw. Tệp ảnh thuộc bộ crop mà root đang chuẩn bị.

| Hình và trang in | Chú thích nguồn tiếng Anh | Chú thích tiếng Việt trong raw |
| --- | --- | --- |
| 26.13, tr. 854 | Both this voltmeter (left) and ammeter (right) are d’Arsonval galvanometers. | Vôn kế và ampe kế dùng điện kế d’Arsonval. |
| 26.14, tr. 854 | A d’Arsonval galvanometer, showing a pivoted coil with attached pointer, a permanent magnet supplying a magnetic field, and a spring. | Cuộn dây quay, kim, nam châm vĩnh cửu và lò xo trong điện kế d’Arsonval. |
| 26.15, tr. 855 | Using the same meter to measure current and voltage. | Dùng cùng điện kế để đo dòng điện và hiệu điện thế. |
| 26.16, tr. 856 | Ammeter–voltmeter method for measuring resistance. | Hai cách mắc ampe kế và vôn kế khi đo điện trở. |
| 26.17, tr. 857 | Ohmmeter circuit. | Mạch ôm kế có điện trở điều chỉnh. |
| 26.18, tr. 857 | This digital multimeter can be used as a voltmeter, ammeter, or ohmmeter. | Đồng hồ vạn năng số đo điện áp, dòng điện và điện trở. |
| 26.19, tr. 858 | A potentiometer. | Mạch chiết áp cân bằng suất điện động. |
| 26.20, tr. 859 | Charging a capacitor. | Mạch R-C trước và sau khi đóng công tắc để nạp tụ. |
| 26.21, tr. 860 | Current and capacitor charge as functions of time for a charging capacitor. | Đồ thị dòng điện và điện tích của tụ theo thời gian trong quá trình nạp. |
| 26.22, tr. 861 | Discharging a capacitor. | Mạch tụ điện phóng qua điện trở sau khi đóng công tắc. |
| 26.23, tr. 861 | Current and capacitor charge as functions of time for a discharging capacitor. | Đồ thị dòng điện và điện tích của tụ theo thời gian trong quá trình phóng. |
| Ứng dụng không đánh số, tr. 856 | Electromyography. | Điện cơ đồ dùng kim có hai điện cực đo hoạt động điện của cơ bàn tay. |
| Ứng dụng không đánh số, tr. 860 | Pacemakers and Capacitors. | Bộ kích nhịp tim dùng tụ điện để tạo xung điện định kỳ. |

Hai ảnh ứng dụng không có số hình. Raw đang trỏ lần lượt đến `ung-dung-dien-co.png` và `ung-dung-may-tao-nhip-tim.png`. Câu hỏi cuối phần 26.3 nhắc lại Hình 26.12 ở mục 26.2, hình này không thuộc danh sách crop của hai phần hiện tại.

## Kiểm tra định lượng và định dạng toán

| Kiểm tra | Kết quả |
| --- | --- |
| Bề rộng toán ở hai tệp raw | 41 công thức display và 199 công thức inline đã render. Không có lỗi TeX. Bề rộng lớn nhất là 29,491ex cho display và 25,558ex cho inline. Không công thức display nào vượt 30ex, không công thức inline nào vượt 38ex. |
| Số hiệu phương trình trong phần 26.3 | Eq. 26.7 và 26.8, mỗi số xuất hiện đúng một lần. |
| Số hiệu phương trình trong phần 26.4 | Eq. 26.9–26.18, mỗi số xuất hiện đúng một lần và theo thứ tự nguồn. |
| Bộ kiểm tra Python | Thành công. Kiểm tra $R_{\mathrm{sh}}=0{,}408\,\Omega$, điện trở ampe kế tương đương $0{,}400\,\Omega$, điện trở phụ vôn kế $9980\,\Omega$, hai ví dụ đo điện trở và các giá trị R-C. |
| Cân bằng khi nạp | Tích phân số đến $40\tau$ cho nguồn cấp $1{,}44\times10^{-4}\,\mathrm J$, điện trở tỏa $7{,}20\times10^{-5}\,\mathrm J$, tụ lưu $7{,}20\times10^{-5}\,\mathrm J$. Điện tích tích phân được bằng điện tích trên tụ tại thời điểm đó. |
| Cân bằng khi phóng | Tích phân số đến $40\tau$ cho điện tích rời tụ $5{,}00\times10^{-6}\,\mathrm C$ và nhiệt lượng $1{,}25\times10^{-5}\,\mathrm J$, bằng năng lượng ban đầu của tụ. |

Các giá trị làm tròn chính khác gồm $\tau=10\,\mathrm s$, $q/Q_f\approx0{,}99$ và $i/I_0\approx0{,}010$ tại $46\,\mathrm s$, thời gian phóng đến $q=0{,}10Q_0$ khoảng $23\,\mathrm s$, và dòng tại thời điểm ấy là $-5{,}0\times10^{-8}\,\mathrm A$. Dấu âm dùng quy ước chiều dương của dòng nạp.

## Giới hạn của lượt rà soát

Hai phần đã được đối chiếu nội dung và công thức với trích chữ nguồn. Chưa nghiệm thu hình sau crop, giao diện, build, liên kết catalog, Wiki hoặc responsive layout. Các phần còn lại của chương 26, đặc biệt toàn bộ danh mục câu hỏi và bài tập, cần được kiểm kê trước khi root tích hợp chương vào website.
