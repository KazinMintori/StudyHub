![Hình 2.0: Vận động viên điền kinh tăng tốc bứt phá và giảm tốc sau vạch đích — hiện tượng điển hình của chuyển động một chiều](img/young-02/mo-chuong-chay.png)

::: exercise Khởi động: Khi nào thì người chạy thực sự có gia tốc?
Trong một cuộc chạy nước rút cự ly $100\,\mathrm m$, vận động viên tăng tốc dũng mãnh ngay sau phát súng lệnh, duy trì tốc độ cao nhất qua vạch đích, rồi dần dần chậm lại sau khi đã kết thúc cuộc đua. Trong giai đoạn nào của chuyển động, ta có thể khẳng định chính xác về mặt vật lý rằng người chạy đang có gia tốc?

(i) Chỉ trong khi thi đấu trên đường chạy;  
(ii) Chỉ sau khi đã vượt qua vạch đích;  
(iii) Cả trong khi thi đấu và sau khi qua vạch đích;  
(iv) Không giai đoạn nào có gia tốc;  
(v) Kết quả phụ thuộc vào mức độ tăng tốc ban đầu.
:::

Một chiếc máy bay thương mại cần một đường băng dài bao nhiêu mét để đạt đủ tốc độ cất cánh an toàn? Khoảng cách phanh khẩn cấp của một chiếc ô tô trên đường cao tốc tăng lên gấp mấy lần khi tốc độ xe tăng gấp đôi? Khi bạn vô tình làm tuột tay một chiếc cốc thủy tinh, bạn có đúng bao nhiêu phần trăm giây để kịp vung tay chụp lại trước khi nó vỡ tan trên sàn nhà?

Tất cả những câu hỏi sinh động trên đều quy tụ về bài toán của **động học** (*kinematics*) — phân ngành cơ học nghiên cứu việc mô tả chuyển động của các vật thể trong không gian và thời gian mà chưa cần xét đến nguyên nhân gây ra chuyển động (lực).

Chương 2 khởi đầu hành trình cơ học bằng trường hợp cơ bản và quan trọng nhất: **chuyển động trên đường thẳng (chuyển động một chiều)**. Chúng ta sẽ xây dựng hệ thống khái niệm định lượng chặt chẽ để phân biệt những cặp đại lượng thường bị đánh đồng trong ngôn ngữ đời thường:
- **Độ dời** và **Quãng đường**;
- **Vận tốc** và **Tốc độ**;
- **Gia tốc tức thời** và sự thay đổi tốc độ (xóa tan ngộ nhận muôn thuở: gia tốc âm không đồng nghĩa với chuyển động chậm dần!).

Đặc biệt, chương này sẽ trang bị cho bạn hệ 4 phương trình động học kinh điển cho chuyển động biến đổi đều, làm chủ hiện tượng rơi tự do dưới tác dụng của trọng trường, và vận dụng công cụ giải tích vi tích phân ($dx/dt, dv/dt, \int v\,dt$) để khai mở các chuyển động phức tạp trong thế giới thực.

### Mục tiêu học tập trọng tâm

1. **Độ dời và vận tốc trung bình (Mục 2.1):** Nắm vững bản chất đại số của tọa độ vị trí, độ dời $\Delta x$, và mối liên hệ giữa vận tốc trung bình với độ dốc của cát tuyến trên đồ thị $x-t$.
2. **Vận tốc tức thời (Mục 2.2):** Hiểu sâu sắc khái niệm đạo hàm $v_x = dx/dt$ như là tiếp tuyến của đồ thị chuyển động; phân biệt rạch ròi vận tốc tức thời và tốc độ tức thời.
3. **Gia tốc (Mục 2.3):** Làm chủ đạo hàm bậc hai $a_x = dv_x/dt = d^2x/dt^2$; nhận thức quy tắc then chốt về dấu của tích $v_x \cdot a_x$ quyết định chuyển động nhanh dần hay chậm dần; khám phá ứng dụng cảm biến gia tốc MEMS trong smartphone và túi khí ô tô.
4. **Chuyển động thẳng biến đổi đều (Mục 2.4):** Làm chủ 4 phương trình động học cốt lõi; khai thác công thức độc lập với thời gian ($v_x^2 - v_{0x}^2 = 2a_x\Delta x$) và ý nghĩa diện tích dưới đồ thị $v-t$.
5. **Rơi tự do (Mục 2.5):** Giải mã chuyển động của vật dưới gia tốc trọng trường $g$; phân tích sâu trạng thái tại đỉnh quỹ đạo ném đứng (tại sao vận tốc triệt tiêu nhưng gia tốc vẫn khác không!).
6. **Tích phân trong động học (Mục 2.6):** Sử dụng tích phân xác định để truy tìm vận tốc từ gia tốc và vị trí từ vận tốc khi gia tốc biến thiên theo thời gian.

### Kiến thức nền tảng cần huy động (từ Chương 1)

- **Vector độ dời và đại số thành phần:** Chiếu vector lên trục tọa độ định hướng (Mục 1.7, 1.8).
- **Phân tích thứ nguyên và đổi đơn vị:** Quy đổi nhịp nhàng giữa $\mathrm{m/s}$ và $\mathrm{km/h}$ (Mục 1.4).
