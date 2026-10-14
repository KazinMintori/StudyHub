Hãy quấn một đoạn dây đồng quanh bút chì để tạo cuộn dây. Khi đặt vào mạch, cuộn có hành vi khác đoạn dây duỗi thẳng. Trong xe chạy xăng, cuộn dây giúp ắc quy 12 V tạo điện áp hàng nghìn volt để đánh lửa bugi. Những cuộn khác được dùng trong đèn huỳnh quang và chôn dưới mặt đường để điều khiển đèn giao thông. Các ứng dụng này cùng dựa vào cảm ứng điện từ.

Trong bài học này, ta khảo sát ba khía cạnh nền tảng của hiện tượng cảm ứng:

1. **Hỗ cảm (Mutual Inductance)**: Dòng điện biến thiên trong một cuộn dây làm từ thông qua một cuộn dây lân cận thay đổi, từ đó gây ra suất điện động cảm ứng trong cuộn dây thứ hai. Đây là nguyên lý làm việc của máy biến áp, các đế sạc không dây cho thiết bị điện tử và hệ thống đánh lửa trong động cơ đốt trong.
2. **Tự cảm (Self-Inductance)**: Dòng điện biến thiên trong chính một mạch điện làm thay đổi từ thông móc vòng với chính mạch đó, dẫn đến sự xuất hiện của một suất điện động tự cảm ngay trong mạch. Một linh kiện mạch điện được chế tạo với độ tự cảm xác định được gọi là **cuộn cảm (inductor)**. Cuộn cảm có đặc tính chống lại sự thay đổi đột ngột của dòng điện, giúp ổn định dòng điện trong mạch một chiều, bảo vệ đường dây truyền tải điện trước các xung sét và duy trì sự phóng điện trong chấn lưu đèn huỳnh quang.
3. **Năng lượng từ trường (Magnetic-Field Energy)**: Muốn thiết lập một dòng điện trong cuộn cảm, nguồn điện bên ngoài phải sinh công để thắng suất điện động tự cảm. Công này không bị tiêu hao thành nhiệt như trong điện trở, mà được tích trữ dưới dạng năng lượng của từ trường. Khi dòng điện giảm về không, năng lượng tích trữ trong từ trường có thể được giải phóng hoàn toàn trở lại mạch điện. Mật độ năng lượng của từ trường tỉ lệ với bình phương độ lớn của cảm ứng từ, tương tự như mật độ năng lượng của điện trường trong tụ điện.

Ta cũng bắt đầu phân tích hành vi của cuộn cảm khi đưa nó vào mạch. Chương sau phát triển việc phân tích cuộn cảm trong mạch xoay chiều, qua đó làm rõ vai trò của linh kiện này trong điện tử.

![Ứng dụng mở đầu: Vòng dây cảm ứng đặt dưới mặt đường tại ngã tư giúp phát hiện xe cộ để điều khiển đèn tín hiệu giao thông.](img/young-30/mo-dau-30.png)

### Câu hỏi mở đầu

Nhiều đèn giao thông tự động chuyển tín hiệu khi có một chiếc ô tô tiến đến nút giao. Quá trình này hoạt động được là do chiếc ô tô chứa:

(i) Vật liệu dẫn điện.

(ii) Vật liệu cách điện mang điện tích tổng cộng khác không.

(iii) Vật liệu sắt từ.

(iv) Vật liệu sắt từ đã bị từ hóa sẵn từ trước.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (iii). Thân và khung xe ô tô chứa một khối lượng thép rất lớn, vốn là vật liệu sắt từ. Khi chiếc xe tiến vào vùng không gian phía trên vòng dây, sự hiện diện của vật liệu sắt từ này làm tăng độ tự cảm của vòng dây, từ đó làm thay đổi dòng điện xoay chiều chạy trong vòng dây. Mạch điện tử nhận biết sự thay đổi này và kích hoạt chuyển tín hiệu đèn giao thông. Cơ chế này không đòi hỏi thân xe phải mang điện tích tổng cộng khác không và không yêu cầu vật liệu sắt từ phải bị từ hóa sẵn từ trước.

</details>

### Mục tiêu học tập

Trong chương này, ta sẽ tìm hiểu:

- 30.1: Cách một dòng điện biến thiên theo thời gian trong một cuộn dây có thể gây ra suất điện động cảm ứng trong cuộn dây thứ hai không nối điện với nó.
- 30.2: Mối liên hệ giữa suất điện động cảm ứng trong một mạch điện với tốc độ biến thiên của dòng điện trong chính mạch điện đó.
- 30.3: Cách tính toán năng lượng tích trữ trong một từ trường.
- 30.4: Cách phân tích mạch chứa điện trở và cuộn cảm (mạch RL).
- 30.5: Nguyên nhân dao động điện trong mạch có cuộn cảm và tụ (mạch LC).
- 30.6: Nguyên nhân dao động suy giảm trong mạch có cuộn cảm, điện trở và tụ (mạch RLC).

### Kiến thức cần ôn lại

Trước khi bắt đầu bài học, ta cần nắm vững các kiến thức nền tảng sau:

- 14.2, 14.3, 14.7: Dao động điều hòa đơn giản và dao động tắt dần.
- 24.1, 24.3: Điện dung và năng lượng điện trường.
- 26.2, 26.4: Các quy tắc Kirchhoff và mạch điện $R$-$C$.
- 28.4, 28.7, 28.8: Lực từ giữa các dây dẫn mang dòng điện, từ trường của ống dây thẳng (solenoid) và độ từ thẩm.
- 29.2, 29.3, 29.7: Định luật cảm ứng Faraday, định luật Lenz, điện trường bảo toàn và điện trường không bảo toàn.
