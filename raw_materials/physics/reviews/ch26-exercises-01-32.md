# Rà soát bài tập cuối Chương 26, bài 26.1–26.32

## Phạm vi và nguồn

Đối chiếu 32 đề bài và lời giải trong `translations/chapter-26/09-bai-tap-01-32.md` với *University Physics with Modern Physics*, bản 15, các trang in 870–872. Các trang PDF mang số 890–892, tương ứng chỉ số trang 889–891 theo quy ước bắt đầu chỉ số từ 0 và độ lệch in +19. Văn bản trích xuất dùng để tra cứu là `qa/physics/full-source/pdf-0890.txt` đến `pdf-0892.txt`. Các hình mạch được xem trên ảnh trang quét để xác định nhánh, cực pin, chiều dòng điện, nút nối và vị trí đồng hồ.

Mỗi bài có một khối đề, một lời giải `detailed-solution:26.N`, phần tóm tắt, hướng giải dạng gạch đầu dòng và các bước tính. Đủ 32 ID theo thứ tự, không thiếu hoặc lặp số. Các bài có hình đều trỏ tới hình tương ứng; 26.27 và 26.28 dùng lại Hình E26.26 theo đề.

## Kết quả rà soát

- Chạy `python raw_materials/physics/verify_chapter26_01_32.py`: Thành công. Tập kiểm tra tính lại số liệu cả 32 bài. Các mạch nhiều nhánh được giải độc lập bằng modified nodal analysis với NumPy, giữ cực tính nguồn và chiều dòng đã khai báo. Hàm giải kiểm tra cân bằng công suất giữa nguồn lý tưởng và điện trở. Các cấu hình E26.26–28 còn kiểm tra riêng điện áp hai thanh dẫn, dòng theo quy tắc nút và $V_{ab}$.
- Dùng MarkdownItMathJax3 để đo công thức trong tệp: 73 công thức hiển thị và 527 công thức nội dòng. Độ rộng lớn nhất lần lượt là 29,35 ex và 31,652 ex. Không có lỗi MathJax, công thức hiển thị nào vượt 30 ex hoặc công thức nội dòng nào vượt 38 ex.
- Đã sửa lỗi quy chiếu điện áp ở E26.26. Giá trị $V=6{,}00\,\mathrm V$ là điện áp giữa hai thanh dẫn, còn $V_{ab}=-3{,}20\,\mathrm V$ là điện áp giữa hai nút a và b. Dòng nhánh dưới là $0{,}600\,\mathrm A$ từ trái sang phải. Trước khi sửa, lời giải nhầm $V$ với $V_{ab}$ và suy ra sai dấu dòng nhánh dưới. Các trường hợp đảo cực ở E26.27 và thay pin ở E26.28 đã được trình bày tách bạch giữa điện áp hai thanh và $V_{ab}$.
- Đã sửa mô tả đường đi điện thế ở E26.32. Đi từ nút dưới lên nút trên qua pin là từ cực âm tới cực dương, nên suất điện động tạo độ tăng thế $25\,\mathrm V$. Kết quả $V_A-V_B=7{,}0\,\mathrm V$ và chiều dòng qua ampe kế được giữ nguyên.
- Các số được kiểm lại gồm cả dòng nhánh, suất điện động, công suất, năng lượng và thời gian đun nước. Với E26.19, thời gian dùng $c_{\mathrm{nước}}=4186\,\mathrm{J/(kg\,K)}$ và giả thiết không thất thoát nhiệt, bỏ qua nhiệt dung bình và điện trở. Mọi kết quả khác giữ theo độ chính xác thích hợp với dữ kiện.

## Đối chiếu hình

Hình E26.1–E26.7 và E26.11 ở trang in 870. Hình E26.13–E26.20 và E26.22–E26.23 ở trang 871. Hình E26.24–E26.26 và E26.29–E26.32 ở trang 872. E26.27 và E26.28 tái sử dụng sơ đồ E26.26, chỉ thay đổi cực tính hoặc suất điện động theo đề.

| Nhãn hình tiếng Anh | Chú thích tiếng Việt trong bài |
| --- | --- |
| Fig. E26.1, straight wire and circular loop | Hai đoạn dây thẳng mắc nối tiếp với một vòng dây tròn |
| Fig. E26.2, protruding resistor X and three parallel resistors | Điện trở X mắc song song với ba điện trở đã biết |
| Fig. E26.5, triangular resistor network | Ba điện trở tạo thành mạng tam giác giữa a, b và c |
| Fig. E26.6, ideal ammeter and voltmeter circuit | Ampe kế đo dòng nhánh 25 ôm và vôn kế mắc song song với điện trở 45 ôm |
| Fig. E26.7, battery with internal resistance and parallel loads | Pin có điện trở trong và điện trở 18 ôm mắc thành một nhánh song song với hai tải |
| Fig. E26.11, parallel pair in series with R3 | Hai điện trở song song mắc nối tiếp với điện trở R3 |
| Fig. E26.13, directly joined middle nodes | Mạng cầu bốn điện trở có hai nút giữa được nối trực tiếp |
| Fig. E26.14, two parallel pairs in series | Hai cặp điện trở song song mắc nối tiếp |
| Fig. E26.15, one bulb in series with three parallel bulbs | Bóng R1 mắc nối tiếp với ba bóng R2, R3 và R4 mắc song song |
| Fig. E26.16, mixed parallel and series network | Nhánh 6 ôm song song với 8 ôm, nối tiếp 25 ôm và mắc song song với 20 ôm |
| Fig. E26.17, 1-ohm and 2-ohm branch parallel to 6 ohms | Nhánh 1 ôm nối tiếp 2 ôm mắc song song với điện trở 6 ôm |
| Fig. E26.18, switch and resistor network | Công tắc nối tiếp với R1 song song với R2, rồi mắc nối tiếp với R3 |
| Fig. E26.19, water heater in a multi-branch circuit | Điện trở 20 ôm làm nóng nước trong mạng có các nhánh song song |
| Fig. E26.20, branch and wire currents given | Ba điện trở song song, với dòng tổng và dòng nhánh R1 được cho |
| Fig. E26.22, two batteries and resistor branches | Nguồn 10 vôn mắc song song với điện trở 30 ôm và nhánh pin 5 vôn cùng điện trở 20 ôm |
| Fig. E26.23, three branches with two known currents | Ba nhánh song song có hai dòng đã biết và hai pin |
| Fig. E26.24, three branches and current arrows | Ba nhánh song song giữa a và b với dòng điện đã biết |
| Fig. E26.25, bridge circuit | Mạng cầu với hai pin, điện trở 3 ôm ở nhánh giữa và ba dòng đã cho |
| Fig. E26.26, three parallel branches with two batteries | Ba nhánh song song chứa hai pin và ba điện trở |
| Fig. E26.29, voltmeter and switched 25-volt battery | Vôn kế đo trên điện trở 50 ôm và nhánh pin 25 vôn được đóng bằng công tắc |
| Fig. E26.30, 75-volt source feeding two parallel branches | Pin 75 vôn nối tiếp 12 ôm cấp cho hai nhánh 48 ôm và pin E nối tiếp 15 ôm |
| Fig. E26.31, switch, voltmeter and ammeter circuit | Mạch gồm pin 25 vôn, điện trở 100 ôm, nhánh pin 15 vôn với điện trở 75 ôm và đồng hồ |
| Fig. E26.32, three-branch bridge with unknown battery | Mạng điện có nhánh giữa gồm 6 ôm, pin 25 vôn và 3 ôm, cùng nhánh cầu bên phải |

Các tệp `img/young-26/hinh-e26-NN.png` hiện chưa có trong thư mục đích và đang chờ phần cắt hình được giao cho lượt tích hợp. Vì vậy đường dẫn Markdown đã được đối chiếu tên và vị trí dự kiến, nhưng chưa thể xác nhận ảnh cuối cùng.

## Giới hạn kiểm chứng

Báo cáo này chỉ xác nhận nội dung và phép tính của nhóm bài tập 26.1–26.32. Bộ giải số kiểm tra nghiệm của mạch theo topology đã nhập, còn việc nhập topology và cực tính được đối chiếu riêng với trang quét. Chưa dựng ảnh cuối, chưa kiểm tra liên kết ảnh sau tích hợp và chưa chạy kiểm thử hiển thị trên trình duyệt hoặc điện thoại. Báo cáo không chứng nhận toàn bộ Chương 26 hay toàn khóa học.
