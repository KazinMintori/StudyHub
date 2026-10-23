## Chuyển động quay của vật rắn

![Hình 9.0: Chuyển động quay của cánh quạt máy bay quanh một trục cố định trong không gian.](./img/young-09/a-mo-dau.png)

Chuyển động của cánh quạt máy bay, đĩa Blu-ray trong đầu đọc, vòng đu quay khổng lồ và lưỡi cưa tròn của máy cắt gỗ có điểm gì chung? Không có vật thể nào trong số này có thể mô hình hóa thỏa đáng dưới dạng một chất điểm đơn thuần. Mỗi trường hợp đều liên quan đến một vật thể có kích thước thực tế đang quay quanh một trục cố định trong một hệ quy chiếu quán tính.

Hiện tượng quay xuất hiện ở mọi thang đo kích thước trong tự nhiên, từ chuyển động quay của electron trong nguyên tử đến sự tự quay và chuyển động của toàn bộ thiên hà. Chúng ta cần xây dựng các phương pháp tổng quát để mô tả và phân tích chuyển động của vật thể quay. Ở phần này, chúng ta khảo sát các vật thể có kích thước và hình dạng hình học xác định, nói chung có thể vừa tham gia chuyển động tịnh tiến vừa tham gia chuyển động quay.

Trong thế giới thực, các vật thể vật lý chịu lực tác dụng có thể bị biến dạng: Chúng có thể bị kéo giãn, xoắn vặn hoặc nén ép. Ở giai đoạn đầu này, chúng ta tạm thời bỏ qua mọi sự biến dạng ấy và giả thiết rằng vật thể có hình dạng cùng kích thước hoàn toàn xác định và không đổi. Mô hình lý tưởng hóa này được gọi là **vật rắn** (rigid body).

Chúng ta bắt đầu với ngôn ngữ động học để mô tả chuyển động quay của vật rắn. Tiếp theo, biểu thức động năng quay cho phép vận dụng phương pháp năng lượng để phân tích chuyển động này. Sau đó, các nguyên lý động lực học sẽ liên hệ lực tác dụng lên vật với chuyển động quay của nó.

### Mục tiêu học tập

Sau khi học xong chương này, người học có thể:

- **Mục tiêu 9.1**: Mô tả chuyển động quay của vật rắn thông qua tọa độ góc, vận tốc góc và gia tốc góc.
- **Mục tiêu 9.2**: Phân tích chuyển động quay của vật rắn khi gia tốc góc không đổi theo thời gian.
- **Mục tiêu 9.3**: Thiết lập mối liên hệ giữa chuyển động quay của vật rắn với vận tốc dài và gia tốc dài của một điểm bất kỳ trên vật.
- **Mục tiêu 9.4**: Hiểu rõ ý nghĩa vật lý của momen quán tính quanh một trục quay và mối liên hệ với động năng quay.
- **Mục tiêu 9.5**: Liên hệ giá trị momen quán tính giữa hai trục quay song song thông qua định lý trục song song.
- **Mục tiêu 9.6**: Tính toán momen quán tính cho các vật thể có dạng hình học xác định.

### Kiến thức nền tảng cần ôn tập

Để tiếp thu tốt nội dung, người học nên rà soát lại các kiến thức sau:

- **Phép nhân vectơ**: Tích có hướng của hai vectơ và quy tắc bàn tay phải.
- **Động học chuyển động thẳng**: Vận tốc dài, gia tốc dài và các phương trình chuyển động thẳng biến đổi đều với gia tốc không đổi.
- **Chuyển động tròn**: Chuyển động tròn đều, gia tốc hướng tâm và tiếp tuyến.
- **Định luật bảo toàn năng lượng cơ học**: Sử dụng năng lượng để giải bài toán cơ học.

::: info Câu hỏi tư duy khởi đầu chương
Mỗi cánh trên cánh quạt đang quay của một chiếc máy bay có dạng tương tự như một thanh mảnh dài. Giả sử mỗi cánh quạt được kéo dài gấp đôi chiều dài ban đầu, trong khi khối lượng của mỗi cánh và tốc độ góc của cánh quạt vẫn giữ nguyên không đổi. Khi đó, động năng của các cánh quạt đang quay sẽ tăng lên theo hệ số nào?

- (i) Tăng 2 lần.
- (ii) Tăng 4 lần.
- (iii) Tăng 8 lần.
- (iv) Động năng không thay đổi.
- (v) Động năng giảm đi chứ không tăng.

<details><summary>Xem lời giải thích</summary>

**Đáp án đúng: (ii)**.

Mỗi cánh quạt có thể xem như một thanh mảnh đồng chất chiều dài $L$ quay quanh trục đi qua một đầu. Momen quán tính của thanh đối với trục quay đi qua đầu thanh tỉ lệ với bình phương chiều dài:
$$
I = \frac{1}{3} M L^2
$$

Khi chiều dài thanh tăng gấp đôi thành $L' = 2L$ trong khi khối lượng $M$ không đổi, momen quán tính mới sẽ là:
$$
I' = \frac{1}{3} M (2L)^2 = 4I
$$

Vì tốc độ góc $\omega$ giữ nguyên, động năng quay tỉ lệ thuận với momen quán tính theo hệ thức:
$$
K = \frac{1}{2} I \omega^2
$$

Do đó động năng quay mới tăng lên 4 lần:
$$
K' = 4K
$$

</details>
:::
