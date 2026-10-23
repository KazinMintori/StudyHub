<!-- Source: Section 19.1, printed 613–615, PDF 633–635. -->

## 19.1. Hệ nhiệt động

Chúng ta đã nghiên cứu quá trình truyền năng lượng thông qua công cơ học ở các phần cơ học, đồng thời đã tìm hiểu sự truyền nhiệt qua các định luật nhiệt học. Bây giờ, chúng ta kết hợp và tổng quát hóa các nguyên lý đó thành một khuôn khổ hoàn chỉnh.

Quá trình truyền năng lượng luôn gắn liền với một hệ vật lý cụ thể. Hệ này có thể là một thiết bị cơ học, một cơ thể sinh học, hoặc một lượng vật chất xác định, chẳng hạn chất làm lạnh trong máy điều hòa hay hơi nước đang giãn nở trong tuabin. Một cách tổng quát, **hệ nhiệt động** là tập hợp các vật thể bất kỳ được chọn để khảo sát như một khối thống nhất, có khả năng trao đổi năng lượng với môi trường xung quanh.

Một ví dụ quen thuộc là lượng hạt ngô trong một chiếc nồi có nắp đậy. Khi đặt nồi lên bếp, nhiệt lượng được truyền vào hạt ngô qua sự dẫn nhiệt. Khi ngô nổ và nở bung thành bỏng ngô, nó giãn nở và sinh công đẩy nắp nồi dịch chuyển lên trên. Trạng thái của bỏng ngô gồm thể tích, nhiệt độ và áp suất đều thay đổi trong quá trình nổ. Một quá trình diễn ra sự biến đổi trạng thái của hệ nhiệt động được gọi là **quá trình nhiệt động**.

![Hình 19.1: Lượng bỏng ngô trong nồi là một hệ nhiệt động. Trong quá trình nhiệt động này, nhiệt lượng được truyền vào hệ, và hệ sinh công lên môi trường xung quanh để đẩy nắp nồi dịch chuyển.](../img/young-19/a-hinh-19-01.png)

Trong cơ học, chúng ta từng dùng mô hình chất điểm, giản đồ lực và các định luật bảo toàn. Đối với hệ nhiệt động cũng vậy: Điều thiết yếu đầu tiên là phải xác định ranh giới rõ ràng giữa những gì thuộc về hệ và những gì thuộc về môi trường. Chỉ khi đó, ta mới có thể mô tả mạch lạc các dòng năng lượng đi vào hoặc ra khỏi hệ. Trong ví dụ về bỏng ngô, hệ chỉ bao gồm các hạt ngô, còn nồi, nắp nồi và bếp nấu thuộc về môi trường ngoài.

Nhiệt động lực học xuất phát từ rất nhiều bài toán thực tế sinh động:

- Động cơ xăng trong ô tô, động cơ phản lực trên máy bay hay động cơ tên lửa trên tàu vũ trụ đều sử dụng nhiệt tỏa ra từ phản ứng cháy của nhiên liệu để sinh công cơ học đẩy phương tiện chuyển động.
- Mô cơ trong cơ thể sinh vật chuyển hóa hóa năng dự trữ từ thức ăn thành công cơ học tác dụng lên môi trường xung quanh.
- Động cơ hơi nước và tuabin nhiệt điện sử dụng nhiệt đốt than hoặc nhiên liệu để sinh công quay máy phát điện hoặc kéo đoàn tàu.

![Hình 19.2: (a) Động cơ tên lửa sử dụng nhiệt lượng tỏa ra từ quá trình đốt cháy nhiên liệu để sinh công đẩy tàu vũ trụ. (b) Cơ thể người và sinh vật sống là những hệ nhiệt động phức tạp, nhưng các nguyên lý cơ bản của nhiệt động lực học vẫn hoàn toàn chi phối mọi hoạt động trao đổi năng lượng của chúng.](../img/young-19/a-hinh-19-02.png)

### Quy ước dấu của nhiệt lượng và công

Mối quan hệ năng lượng trong mọi quá trình nhiệt động được mô tả thông qua nhiệt lượng $Q$ truyền vào hệ và công cơ học $W$ do hệ sinh ra. Cả $Q$ và $W$ đều có thể nhận giá trị dương, âm hoặc bằng không.

![Hình 19.3: Hệ nhiệt động trao đổi năng lượng với môi trường xung quanh thông qua nhiệt lượng, công cơ học hoặc cả hai. Cần nắm vững quy ước dấu của $Q$ và $W$.](../img/young-19/a-hinh-19-03.png)

Quy ước dấu chuẩn mực được xác định như sau:

- $Q > 0$: Nhiệt lượng truyền vào hệ, tương ứng với việc cung cấp thêm năng lượng cho hệ.
- $Q < 0$: Nhiệt lượng truyền từ hệ ra ngoài môi trường, tương ứng với việc hệ mất bớt năng lượng nhiệt.
- $W > 0$: Công do hệ sinh ra tác dụng lên môi trường ngoài, chẳng hạn khối khí giãn nở đẩy pít-tông ra xa, tương ứng với năng lượng rời khỏi hệ.
- $W < 0$: Công do ngoại lực thực hiện lên hệ, chẳng hạn môi trường nén khối khí lại, tương ứng với năng lượng từ môi trường đi vào hệ.

::: Warning Cẩn trọng với dấu của công trong nhiệt động lực học
Quy ước dấu của công $W$ trong nhiệt động lực học ngược với quy ước thường dùng trong cơ học. Trong cơ học, ta thường gọi công là công do ngoại lực tác dụng lên vật. Trong nhiệt động lực học, việc quy ước $W$ là công do hệ sinh ra thuận tiện hơn nhiều: Khi hệ giãn nở, áp suất, độ biến thiên thể tích và công sinh ra đều mang dấu dương. Chúng ta cần áp dụng nhất quán quy ước dấu này trong toàn bộ các tính toán.
:::

::: Exercise Tự kiểm tra 19.1
Trong bài toán rót cà phê nóng vào cốc nhôm ở điều kiện cách nhiệt với bên ngoài: Dấu của $Q$ đối với cà phê là gì? Đối với cốc nhôm là gì? Nếu một khối hộp trượt có ma sát trên sàn nằm ngang, dấu của $W$ đối với khối hộp theo nhiệt động lực học là gì?

<details><summary>Xem lời giải thích</summary>
Dấu lần lượt là: Âm, dương, dương.

- Cà phê nguội đi do truyền nhiệt cho cốc nhôm, do đó nhiệt lượng rời khỏi cà phê: $Q_{\mathrm{coffee}} < 0$.
- Cốc nhôm nhận nhiệt lượng từ cà phê nóng, do đó nhiệt lượng đi vào cốc nhôm: $Q_{\mathrm{Al}} > 0$.
- Công của lực ma sát tác dụng lên khối hộp mang dấu âm. Nếu gọi công ngoại lực này là $W_{\mathrm{ngoài}}$, thì quy ước đối dấu của câu hỏi cho $W=-W_{\mathrm{ngoài}}>0$. Cần phân biệt quy ước dấu ấy với việc tính công tại một điểm đứng yên trên mặt sàn.

</details>
:::
