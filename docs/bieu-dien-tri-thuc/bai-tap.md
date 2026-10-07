---
title: Bài tập ôn luyện - Biểu diễn tri thức & Tìm kiếm
description: Tuyển tập bài tập giải thuật tìm kiếm trong không gian trạng thái, A*, Minimax, Alpha-Beta, CSP và suy luận logic/mạng Bayes.
---

# Bài tập ôn luyện: Biểu diễn tri thức & Tìm kiếm

Tài liệu cung cấp hệ thống bài tập cho môn Biểu diễn tri thức & Tìm kiếm, từ xây dựng không gian trạng thái, phân tích độ phức tạp của các chiến lược tìm kiếm đến suy luận hình thức trong trí tuệ nhân tạo.

---

## Phần 1. Tác tử thông minh & Không gian trạng thái

### Bài 1.1: Đặc tả PEAS và phân loại môi trường
Xét hệ thống xe tự hành chở khách trong đô thị (Autonomous Taxi).

1. Hãy chỉ rõ 4 thành phần PEAS (Performance measure, Environment, Actuators, Sensors) của hệ thống này.
2. Phân loại môi trường của xe tự hành theo các chiều thuộc tính:
   - Quan sát được hoàn toàn (Fully observable) hay một phần (Partially observable)?
   - Tác tử đơn (Single agent) hay đa tác tử (Multi-agent)?
   - Tất định (Deterministic) hay ngẫu nhiên (Stochastic)?
   - Tĩnh (Static) hay động (Dynamic)?
   - Rời rạc (Discrete) hay liên tục (Continuous)?

#### Lời giải gợi ý
1. Đặc tả PEAS:
   - **Performance Measure (Hiệu năng):** Độ an toàn (không tai nạn), tốc độ di chuyển hợp lý, tuân thủ luật giao thông, độ êm ái khi lái, tối đa hóa lợi nhuận / tiết kiệm nhiên liệu.
   - **Environment (Môi trường):** Đường phố, đèn giao thông, người đi bộ, các phương tiện khác, điều kiện thời tiết.
   - **Actuators (Cơ cấu chấp hành):** Bánh lái, chân ga, chân phanh, còi, đèn tín hiệu, màn hình hiển thị cho khách.
   - **Sensors (Cảm biến):** Camera trước/sau/hông, LiDAR, Radar, GPS, cảm biến tốc độ bánh xe, gia tốc kế (IMU), cảm biến siêu âm.

2. Phân loại môi trường:
   - *Partially observable:* Camera/LiDAR không thể nhìn thấy xuyên qua các vật cản hoặc góc khuất.
   - *Multi-agent (Competitive & Cooperative):* Có nhiều phương tiện khác cùng lưu thông (vừa hợp tác nhường đường, vừa cạnh tranh không gian làn).
   - *Stochastic:* Hành vi người đi bộ và xe cộ xung quanh không thể dự đoán tuyệt đối chính xác $100\%$.
   - *Dynamic:* Môi trường thay đổi liên tục trong khi tác tử đang suy nghĩ, tính toán lộ trình.
   - *Continuous:* Tọa độ vị trí, góc lái và vận tốc biến thiên liên tục trong không gian thực.

---

## Phần 2. Không gian trạng thái và thuật toán tìm kiếm (BFS, UCS, A*)

### Bài 2.1: So sánh thuật toán UCS và A* trên đồ thị trạng thái
Xét đồ thị không gian trạng thái sau đây. Trạng thái bắt đầu là $S$, trạng thái đích là $G$. Chi phí bước đi được ghi trên các cạnh, và giá trị hàm đánh giá $h(n)$ tại từng đỉnh được cho trong ngoặc vuông:
- $S [h=7]$ trỏ tới $A [h=6]$ (chi phí 2) và $B [h=4]$ (chi phí 4)
- $A$ trỏ tới $C [h=4]$ (chi phí 3) và $D [h=3]$ (chi phí 6)
- $B$ trỏ tới $D [h=3]$ (chi phí 1) và $E [h=2]$ (chi phí 5)
- $C$ trỏ tới $G [h=0]$ (chi phí 5)
- $D$ trỏ tới $G [h=0]$ (chi phí 3)
- $E$ trỏ tới $G [h=0]$ (chi phí 2)

1. Trình bày thứ tự mở rộng nút (node expansion) khi sử dụng thuật toán Tìm kiếm chi phí đồng nhất (Uniform Cost Search - UCS). Chỉ ra đường đi tìm được và tổng chi phí.
2. Kiểm tra tính hợp lệ (Admissible) và tính nhất quán (Consistent / Monotonic) của hàm heuristic $h(n)$ trên đồ thị này.
3. Trình bày thứ tự mở rộng nút khi sử dụng thuật toán A* (đồ thị tìm kiếm sử dụng hàng đợi ưu tiên theo $f(n) = g(n) + h(n)$). Chỉ ra đường đi tối ưu tìm được.

#### Lời giải gợi ý
1. Thuật toán UCS ưu tiên nút có chi phí đường đi từ gốc $g(n)$ nhỏ nhất:
   - Khởi tạo: Hàng đợi ưu tiên $\{S(g=0)\}$.
   - Lấy $S(0)$, mở rộng: thêm $A(g=2), B(g=4)$.
   - Lấy $A(2)$, mở rộng: thêm $C(g=2+3=5), D(g=2+6=8)$. Hàng đợi: $\{B(4), C(5), D(8)\}$.
   - Lấy $B(4)$, mở rộng: $D(g=4+1=5)$ (cập nhật chi phí tốt hơn cho $D$), $E(g=4+5=9)$. Hàng đợi: $\{C(5), D(5), D(8), E(9)\}$.
   - Lấy $C(5)$, mở rộng: $G(g=5+5=10)$.
   - Lấy $D(5)$, mở rộng: $G(g=5+3=8)$ (cập nhật chi phí tốt hơn cho $G$). Hàng đợi: $\{G(8), E(9), G(10)\}$.
   - Lấy $G(8)$: Đích được mở rộng! Kết thúc.
   Đường đi tìm được: $S \to B \to D \to G$ với tổng chi phí $g(G) = 8$.

2. Tính hợp lệ (Admissibility):
   - $h(n) \le h^*(n)$ với mọi $n$, trong đó $h^*(n)$ là chi phí thực tế ngắn nhất từ $n$ đến $G$.
   - $h^*(S) = 8 \ge h(S) = 7$ (hợp lệ).
   - $h^*(A) = \min(3+5, 6+3) = 8 \ge h(A) = 6$ (hợp lệ).
   - $h^*(B) = \min(1+3, 5+2) = 4 \ge h(B) = 4$ (hợp lệ).
   - $h^*(C) = 5 \ge h(C) = 4$ (hợp lệ).
   - $h^*(D) = 3 \ge h(D) = 3$ (hợp lệ).
   - $h^*(E) = 2 \ge h(E) = 2$ (hợp lệ).
   $\implies$ Hàm heuristic là Admissible.

3. Thuật toán A* với $f(n) = g(n) + h(n)$:
   - Khởi tạo: $\{S(f = 0 + 7 = 7)\}$.
   - Mở $S$: $A(g=2, f=2+6=8), B(g=4, f=4+4=8)$.
   - Xét ưu tiên $A(8)$ hoặc $B(8)$. Giả sử mở $A(8)$:
     $C(g=5, f=5+4=9), D(g=8, f=8+3=11)$.
   - Tiếp theo lấy $B(8)$:
     $D(g=5, f=5+3=8), E(g=9, f=9+2=11)$.
   - Tiếp theo lấy $D(8)$:
     $G(g=8, f=8+0=8)$.
   - Nút đích $G(8)$ có $f$ nhỏ nhất trong hàng đợi và được lấy ra $\implies$ Kết thúc với lời giải $S \to B \to D \to G$, chi phí tối ưu là $8$.

---

## Phần 3. Tìm kiếm đối kháng & Bài toán ràng buộc (Minimax, Alpha-Beta, CSP)

### Bài 3.1: Cắt tỉa Alpha–Beta trên cây trò chơi
Cho cây trò chơi 2 người có tổng bằng 0 sau đây. Nút gốc ở tầng MAX, tiếp theo là MIN, rồi đến tầng lá:
- Nút gốc $A$ (MAX) có 3 nút con: $B, C, D$ (MIN).
- Nút $B$ có các nút lá: $4, 6, 3$.
- Nút $C$ có các nút lá: $5, 2, 8$.
- Nút $D$ có các nút lá: $1, 9, 7$.

Giả sử thuật toán duyệt các nhánh từ trái sang phải:

1. Thực hiện chạy từng bước của thuật toán cắt tỉa Alpha-Beta.
2. Ghi rõ giá trị $\alpha, \beta$ tại từng bước cập nhật.
3. Chỉ ra những nút lá nào được cắt tỉa (không cần lượng giá).
4. Giá trị Minimax tại nút gốc là bao nhiêu?

#### Lời giải gợi ý
- Duyệt nhánh con $B$ của $A$:
  - Khởi tạo tại $A$: $\alpha = -\infty, \beta = +\infty$.
  - Xuống $B$ (MIN): $\alpha = -\infty, \beta = +\infty$.
  - Lá 4: $\beta = \min(+\infty, 4) = 4$.
  - Lá 6: $\beta = \min(4, 6) = 4$.
  - Lá 3: $\beta = \min(4, 3) = 3$.
  - Kết thúc nhánh $B$: giá trị của $B$ là $3$.
  - Cập nhật tại $A$ (MAX): $\alpha = \max(-\infty, 3) = 3$.

- Duyệt nhánh con $C$ của $A$:
  - Xuống $C$ (MIN) với $\alpha = 3, \beta = +\infty$.
  - Lá 5: $\beta = \min(+\infty, 5) = 5$.
  - Lá 2: $\beta = \min(5, 2) = 2$.
  - Bây giờ $\alpha = 3 \ge \beta = 2 \implies$ Xảy ra điều kiện cắt tỉa $\alpha \ge \beta$!
  - Cắt nhánh còn lại của $C$ (lá 8 bị bỏ qua, không cần xét).
  - Giá trị trả về từ $C$ là $2$.
  - Tại $A$: $\alpha = \max(3, 2) = 3$ (không đổi).

- Duyệt nhánh con $D$ của $A$:
  - Xuống $D$ (MIN) với $\alpha = 3, \beta = +\infty$.
  - Lá 1: $\beta = \min(+\infty, 1) = 1$.
  - Kiểm tra điều kiện cắt tỉa: $\alpha = 3 \ge \beta = 1 \implies$ Cắt tỉa ngay lập tức!
  - Cắt các nhánh còn lại của $D$ (lá 9 và lá 7 bị bỏ qua).
  - Giá trị trả về từ $D$ là $1$.

- Kết luận:
  - Các nút lá bị cắt tỉa: lá 8 (dưới $C$), lá 9 và lá 7 (dưới $D$).
  - Giá trị Minimax tại nút gốc $A$ là $\alpha = 3$, quyết định tốt nhất của MAX là đi nhánh $B$.

---

## Phần 4. Biểu diễn tri thức & Suy luận Logic

### Bài 4.1: Chuyển đổi sang dạng chuẩn hội (CNF) và Hợp giải Resolution
Cho tập các tri thức sau trong logic mệnh đề:
1. $P \to Q$
2. $Q \to R$
3. $P \lor S$
4. $\neg R$

Mục tiêu: Chứng minh rằng $S$ là hệ quả logic của tập tri thức trên bằng phương pháp phản chứng và nguyên lý Hợp giải (Resolution Refutation).

1. Đưa tất cả các câu trên và phủ định của kết luận vào dạng chuẩn hội (CNF).
2. Lập các bước hợp giải cặp mệnh đề để suy ra mệnh đề rỗng ($\square$).

#### Lời giải gợi ý
1. Chuyển đổi sang CNF:
   - Câu 1: $P \to Q \equiv \neg P \lor Q$ (Mệnh đề 1)
   - Câu 2: $Q \to R \equiv \neg Q \lor R$ (Mệnh đề 2)
   - Câu 3: $P \lor S$ (Mệnh đề 3)
   - Câu 4: $\neg R$ (Mệnh đề 4)
   - Phủ định kết luận: $\neg S$ (Mệnh đề 5)

2. Quá trình hợp giải:
   - Hợp giải (1) và (2) trên $Q$: $(\neg P \lor Q) \land (\neg Q \lor R) \implies \neg P \lor R$ (Mệnh đề 6)
   - Hợp giải (6) và (4) trên $R$: $(\neg P \lor R) \land \neg R \implies \neg P$ (Mệnh đề 7)
   - Hợp giải (3) và (7) trên $P$: $(P \lor S) \land \neg P \implies S$ (Mệnh đề 8)
   - Hợp giải (8) và (5) trên $S$: $S \land \neg S \implies \square$ (Mệnh đề rỗng / Mâu thuẫn)
   Do suy ra mâu thuẫn, giả thiết $\neg S$ sai, do đó $S$ được chứng minh là đúng.
