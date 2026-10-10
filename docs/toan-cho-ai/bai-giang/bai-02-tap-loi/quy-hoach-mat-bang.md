---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: quy-hoach-mat-bang
section: topic
title: "Quy hoạch mặt bằng và phân bổ không gian tối ưu"
description: "Mô hình hóa bài toán bố trí linh kiện vi mạch không chồng lấn, cây phân cắt slicing floorplans, quy hoạch hình học xác định kích thước và tỷ lệ co dãn, tối thiểu hóa độ dài dây dẫn và diện tích bao quanh."
---

Trong thiết kế vi mạch tích hợp quy mô siêu lớn (VLSI), kiến trúc máy tính và thiết kế giao diện tự động (Auto-Layout), bài toán **quy hoạch mặt bằng (floor planning)** đóng vai trò quyết định hiệu năng của toàn bộ hệ thống. Nhiệm vụ là sắp xếp $N$ khối chức năng hình chữ nhật (các lõi xử lý, bộ nhớ đệm, khối tính toán đồ họa) vào một bề mặt chip phẳng sao cho không có hai khối nào đè lên nhau, đồng thời tối thiểu hóa tổng diện tích chip hoặc chiều dài dây dẫn kết nối.

Nhìn từ góc độ tối ưu hóa, bài toán floor planning tổng quát là một bài toán tối ưu tổ hợp NP-khó vì vị trí tương đối giữa các khối (khối này nằm bên trái hay bên phải, bên trên hay bên dưới khối kia) là các quyết định rời rạc. Tuy nhiên, một khi cấu trúc hình học tương đối được ấn định thông qua một cây phân cắt (slicing tree), toàn bộ bài toán chọn kích thước, tỷ lệ khung hình và tọa độ các khối chuyển hóa một cách tự nhiên thành một **Quy hoạch hình học (GP)** hoặc **Quy hoạch tuyến tính (LP)** khả giải tối ưu toàn cục.

## 1. Mô hình hóa bài toán Floor Planning

Giả sử ta cần bố trí $N$ khối hình chữ nhật được đánh số từ $1$ đến $N$. Mỗi khối $i$ được mô tả bởi các biến quyết định:
- Tọa độ góc trái dưới: $(x_i, y_i) \in \mathbb{R}^2$.
- Chiều rộng: $w_i > 0$.
- Chiều cao: $h_i > 0$.

Do đó, khối thứ $i$ chiếm dụng miền không gian kín:

$$
\mathcal{R}_i = [x_i, x_i + w_i] \times [y_i, y_i + h_i].
$$

Toàn bộ $N$ khối phải nằm trọn trong một khung bao hình chữ nhật chung có kích thước chiều rộng $W$ và chiều cao $H$, đặt tại gốc tọa độ:

$$
x_i \ge 0, \quad y_i \ge 0, \quad x_i + w_i \le W, \quad y_i + h_i \le H, \qquad \forall i = 1, \dots, N.
$$

### Ràng buộc về kích thước và hình dạng của từng khối
Các khối phần cứng thường có tính co dãn linh hoạt trong giới hạn công nghệ:
1. **Diện tích tối thiểu**: Mỗi khối phải có diện tích không nhỏ hơn một ngưỡng thiết kế $S_i > 0$:
   $$
   w_i h_i \ge S_i.
   $$
2. **Tỷ lệ khung hình (Aspect Ratio)**: Để tránh các khối quá mỏng hoặc dài ngoằng gây khó khăn khi chế tạo, tỷ số giữa chiều cao và chiều rộng bị kẹp trong một khoảng cho phép:
   $$
   \alpha_i \le \frac{h_i}{w_i} \le \beta_i, \qquad 0 < \alpha_i \le \beta_i.
   $$

## 2. Ràng buộc không chồng lấn và Cây phân cắt (Slicing Floorplans)

Hai khối $i$ và $j$ ($i \ne j$) không đè lên nhau ($\operatorname{int}(\mathcal{R}_i) \cap \operatorname{int}(\mathcal{R}_j) = \emptyset$) khi và chỉ khi thỏa mãn ít nhất một trong bốn quan hệ hình học sau:
1. Khối $i$ nằm hoàn toàn bên trái khối $j$: $x_i + w_i \le x_j$.
2. Khối $i$ nằm hoàn toàn bên phải khối $j$: $x_j + w_j \le x_i$.
3. Khối $i$ nằm hoàn toàn bên dưới khối $j$: $y_i + h_i \le y_j$.
4. Khối $i$ nằm hoàn toàn bên trên khối $j$: $y_j + h_j \le y_i$.

Phép tuyển "hoặc" giữa bốn điều kiện này tạo nên tính phi lồi tổ hợp. Để giải quyết, người ta cố định trước quan hệ thứ tự tương đối bằng cách sử dụng mô hình **mặt bằng phân cắt (Slicing Floorplan)**.

Một mặt bằng phân cắt được tạo thành bằng cách đệ quy chia đôi một hình chữ nhật lớn thành hai hình chữ nhật con bằng một lát cắt ngang (H) hoặc lát cắt dọc (V). Cấu trúc này được biểu diễn bằng một cây nhị phân (Slicing Tree), trong đó các lá là các khối chức năng và các nút nội bộ là các lát cắt. 

Khi cây phân cắt đã cố định, với mỗi cặp khối $(i, j)$, ta luôn xác định được một quan hệ duy nhất có dạng:
- Lát cắt dọc: $x_i + w_i \le x_j$ (khối $i$ ở nhánh trái, khối $j$ ở nhánh phải).
- Lát cắt ngang: $y_i + h_i \le y_j$ (khối $i$ ở nhánh dưới, khối $j$ ở nhánh trên).

Khi đó, toàn bộ các ràng buộc vị trí không chồng lấn trở thành các **bất đẳng thức tuyến tính chuẩn** đối với các biến tọa độ và kích thước.

## 3. Cải dạng Quy hoạch hình học (GP) cho bài toán chọn kích thước

Khi cấu trúc cây phân cắt đã ấn định, ta muốn xác định kích thước $(w_i, h_i)$ và kích thước khung bao $(W, H)$ sao cho tổng diện tích bao quanh $W H$ là nhỏ nhất.

Bài toán có dạng:

$$
\begin{aligned}
\text{minimize}\quad & W H \\
\text{subject to}\quad & w_i h_i \ge S_i, \quad i = 1, \dots, N, \\
& \alpha_i \le h_i w_i^{-1} \le \beta_i, \quad i = 1, \dots, N, \\
& \text{các ràng buộc đường phân cắt dọc và ngang.}
\end{aligned}
$$

Trong cấu trúc slicing tree, chiều rộng và chiều cao của khung bao có thể được biểu diễn như các posynomial của các biến kích thước khối. Cụ thể, nếu hai khối $i$ và $j$ ghép dọc thì chiều rộng tổng là $w_i + w_j$; nếu ghép ngang thì chiều rộng tổng là $\max(w_i, w_j)$.

Ràng buộc diện tích viết lại thành: Biểu thức $S_i w_i^{-1} h_i^{-1} \le 1$ (một ràng buộc posynomial). Ràng buộc tỷ lệ khung hình viết lại thành: Biểu thức $\alpha_i w_i h_i^{-1} \le 1$ và $\beta_i^{-1} h_i w_i^{-1} \le 1$ (các ràng buộc posynomial).

Do đó, toàn bộ bài toán là một **Quy hoạch hình học (GP)** chuẩn tắc trên các biến dương $(w_i, h_i, W, H)$. Sau phép đổi biến logarit $u = \log w, v = \log h$, bài toán trở thành một bài toán tối ưu lồi với hàm mục tiêu lồi và các ràng buộc affine, giải được với hiệu năng số học cao.

## 4. Tối ưu hóa độ dài dây dẫn (Wirelength Optimization)

Bên cạnh mục tiêu diện tích, trong thiết kế mạch tích hợp, nhiệt độ và độ trễ tín hiệu phụ thuộc trực tiếp vào tổng độ dài dây nối giữa các khối. 

Giả sử tâm của khối $i$ có tọa độ:

$$
c_i = \left(x_i + \frac{1}{2}w_i, \; y_i + \frac{1}{2}h_i\right).
$$

Độ dài dây nối Manhattan ($L_1$) giữa hai khối $i$ và $j$ với trọng số kết nối $C_{ij} \ge 0$ (đo lường số lượng đường truyền song song) là:

$$
\text{Wirelength}_{ij} = C_{ij} \left( |c_i^{(x)} - c_j^{(x)}| + |c_i^{(y)} - c_j^{(y)}| \right).
$$

Tổng chiều dài dây nối toàn mạch là:

$$
\Phi_{\text{wire}} = \sum_{1 \le i < j \le N} C_{ij} \left( |c_i^{(x)} - c_j^{(x)}| + |c_i^{(y)} - c_j^{(y)}| \right).
$$

Khi kích thước các khối $(w_i, h_i)$ đã được ấn định, hàm mục tiêu $\Phi_{\text{wire}}$ là tổng của các hàm lồi dạng trị tuyệt đối. Bằng cách đưa vào các biến phụ $u_{ij}, v_{ij} \ge 0$ thỏa mãn:

$$
-u_{ij} \le c_i^{(x)} - c_j^{(x)} \le u_{ij}, \qquad -v_{ij} \le c_i^{(y)} - c_j^{(y)} \le v_{ij},
$$

bài toán tối thiểu hóa chiều dài dây nối đưa thẳng về một bài toán **Quy hoạch tuyến tính (LP)**:

$$
\begin{aligned}
\text{minimize}\quad & \sum_{i < j} C_{ij} (u_{ij} + v_{ij}) \\
\text{subject to}\quad & -u_{ij} \le x_i - x_j + \frac{w_i - w_j}{2} \le u_{ij}, \\
& -v_{ij} \le y_i - y_j + \frac{h_i - h_j}{2} \le v_{ij}, \\
& \text{các ràng buộc không chồng lấn affine trên } (x_i, y_i).
\end{aligned}
$$

## 5. Bài tập tự luyện

::: exercise 1. Quy hoạch hình học cho mặt bằng phân cắt hai khối
Xét hai khối chức năng được ghép cạnh nhau theo phương ngang (lát cắt dọc $V$): Khối 1 nằm bên trái, khối 2 nằm bên phải. Kích thước khung bao là $W = w_1 + w_2$ và $H = \max\{h_1, h_2\}$. Yêu cầu thiết kế:
- Diện tích tối thiểu: Thỏa mãn $w_1 h_1 \ge 4$ và $w_2 h_2 \ge 8$.
- Tỷ lệ khung hình vuông vắn: Thỏa mãn $0{,}5 \le h_1/w_1 \le 2$ và $0{,}5 \le h_2/w_2 \le 2$.
1. Thiết lập bài toán tối thiểu hóa diện tích khung bao $W H$ dưới dạng Quy hoạch hình học (GP).
2. Chuyển bài toán sang dạng lồi bằng phép đổi biến logarit.
3. Tìm kích thước tối ưu của hai khối khi giả định $h_1 = h_2 = H$.
:::

::: solution
1. **Thiết lập dạng GP**:
   Vì $H = \max\{h_1, h_2\}$, ta đặt biến phụ $H$ với $h_1 \le H$ và $h_2 \le H$, tức $h_1 H^{-1} \le 1$ và $h_2 H^{-1} \le 1$.
   Khung bao chiều rộng: $W = w_1 + w_2$.
   Hàm mục tiêu: $W H = (w_1 + w_2) H = w_1 H + w_2 H$ (một posynomial).
   Bài toán GP dạng chuẩn:
   $$
   \begin{aligned}
   \text{minimize}\quad & w_1 H + w_2 H \\
   \text{subject to}\quad & 4 w_1^{-1} h_1^{-1} \le 1, \\
   & 8 w_2^{-1} h_2^{-1} \le 1, \\
   & h_1 H^{-1} \le 1, \quad h_2 H^{-1} \le 1, \\
   & 0{,}5 w_1 h_1^{-1} \le 1, \quad 0{,}5 h_1 w_1^{-1} \le 1, \\
   & 0{,}5 w_2 h_2^{-1} \le 1, \quad 0{,}5 h_2 w_2^{-1} \le 1.
   \end{aligned}
   $$

2. **Dạng lồi qua thang logarit**:
   Đặt $\tilde{w}_i = \log w_i, \tilde{h}_i = \log h_i, \tilde{H} = \log H$.
   Hàm mục tiêu chuyển thành hàm log-sum-exp:
   $$
   f_0 = \log\big(e^{\tilde{w}_1 + \tilde{H}} + e^{\tilde{w}_2 + \tilde{H}}\big) = \tilde{H} + \log\big(e^{\tilde{w}_1} + e^{\tilde{w}_2}\big).
   $$
   Các ràng buộc trở thành affine:
   $$
   \begin{aligned}
   \tilde{w}_1 + \tilde{h}_1 &\ge \log 4, \\
   \tilde{w}_2 + \tilde{h}_2 &\ge \log 8, \\
   \tilde{h}_1 \le \tilde{H}, &\quad \tilde{h}_2 \le \tilde{H}, \\
   -\log 2 \le \tilde{h}_1 - \tilde{w}_1 \le \log 2, &\quad -\log 2 \le \tilde{h}_2 - \tilde{w}_2 \le \log 2.
   \end{aligned}
   $$

3. **Tìm nghiệm tối ưu khi $h_1 = h_2 = H$**:
   Để diện tích khung bao $W H = (w_1 + w_2) H = w_1 H + w_2 H$ nhỏ nhất, các ràng buộc diện tích phải đạt chặt:
   $$
   w_1 = \frac{4}{H}, \qquad w_2 = \frac{8}{H}.
   $$
   Khi đó chiều rộng tổng: $W = w_1 + w_2 = \frac{12}{H}$.
   Tổng diện tích khung bao là $W H = \frac{12}{H} \cdot H = 12$ hằng số!
   Để thỏa mãn tỷ lệ khung hình cho cả hai khối:
   - Với khối 1: Tỷ lệ $0{,}5 \le H^2/4 \le 2$, suy ra $\sqrt{2} \le H \le 2\sqrt{2}$.
   - Với khối 2: Tỷ lệ $0{,}5 \le H^2/8 \le 2$, suy ra $2 \le H \le 4$.
   Giao hai miền nghiệm cho:
   $$
   2 \le H \le 2\sqrt{2} \approx 2{,}828.
   $$
   Chọn nghiệm đối xứng tiện lợi $H = 2$:
   - Khối 1: $h_1 = 2, w_1 = 2$ (tỷ lệ $h_1/w_1 = 1$, hình vuông).
   - Khối 2: $h_2 = 2, w_2 = 4$ (tỷ lệ $h_2/w_2 = 0{,}5$, nằm trong khoảng $[0{,}5; 2]$).
   - Khung bao: $W = 6, H = 2$, tổng diện tích tối ưu $S_{\min} = 12$. Không có diện tích chết (dead space = 0%).
:::

::: exercise 2. Cân bằng dây dẫn bằng Quy hoạch tuyến tính
Cho ba khối chức năng $A, B, C$ có kích thước cố định $1 \times 1$. Khối $A$ được gắn chặt tại tọa độ $(0, 0)$, khối $B$ được gắn chặt tại $(4, 0)$. Khối $C$ là một lõi xử lý trung gian có tọa độ $(x, y)$ cần tìm trong vùng $0 \le x \le 4, 0 \le y \le 3$. Trọng số kết nối dây dẫn là $C_{AC} = 2$ và $C_{BC} = 3$.
1. Viết biểu thức tổng độ dài dây nối Manhattan từ khối $C$ tới hai khối $A$ và $B$.
2. Tìm tọa độ $(x^*, y^*)$ tối ưu giải tích.
3. Thêm một khối cố định $D$ tại $(2, 3)$ với trọng số $C_{CD} = 4$. Tìm vị trí tối ưu mới của khối $C$.
:::

::: solution
1. **Biểu thức tổng độ dài dây dẫn**:
   Tọa độ tâm các khối: $c_A = (0{,}5, \; 0{,}5)$, $c_B = (4{,}5, \; 0{,}5)$, và $c_C = (x + 0{,}5, \; y + 0{,}5)$.
   Đặt biến dịch chuyển tương đối $x \in [0, 4]$ và $y \in [0, 3]$:
   Khoảng cách Manhattan:
   - Từ $A$ đến $C$: $|x - 0| + |y - 0| = x + y$ (vì $x, y \ge 0$).
   - Từ $B$ đến $C$: $|x - 4| + |y - 0| = (4 - x) + y$ (vì $0 \le x \le 4, y \ge 0$).
   Tổng chiều dài có trọng số:
   $$
   f(x, y) = 2(x + y) + 3\big((4 - x) + y\big) = 2x + 2y + 12 - 3x + 3y = 12 - x + 5y.
   $$

2. **Tìm tọa độ tối ưu**:
   Hàm mục tiêu tuyến tính phân rã theo hai biến độc lập:
   $$
   \min_{0 \le x \le 4, 0 \le y \le 3} (12 - x + 5y).
   $$
   - Với biến $y$: Hệ số $+5 > 0$, hàm đồng biến theo $y$. Để cực tiểu, ta chọn $y^* = 0$.
   - Với biến $x$: Hệ số $-1 < 0$, hàm nghịch biến theo $x$. Để cực tiểu, ta chọn $x^* = 4$.
   Vậy vị trí tối ưu là $(x^*, y^*) = (4, 0)$. Khối $C$ đặt sát cạnh khối $B$ do trọng số kết nối $C_{BC} = 3$ lớn hơn $C_{AC} = 2$.
   Giá trị mục tiêu tối ưu: $f(4, 0) = 12 - 4 + 0 = 8$.

3. **Khi bổ sung khối $D$ tại $(2, 3)$ với $C_{CD} = 4$**:
   Khoảng cách từ $C$ đến $D$: $|x - 2| + |y - 3| = |x - 2| + (3 - y)$ (vì $y \le 3$).
   Hàm mục tiêu mới:
   $$
   \begin{aligned}
   g(x, y) &= 12 - x + 5y + 4\big(|x - 2| + 3 - y\big) \\
   &= 12 - x + 5y + 4|x - 2| + 12 - 4y \\
   &= 24 - x + y + 4|x - 2|.
   \end{aligned}
   $$
   - Theo phương $y$: Hàm mục tiêu tăng theo $y$ (hệ số $+1$), do đó nghiệm tối ưu tiếp tục là $y^* = 0$.
   - Theo phương $x$: Xét hàm $h(x) = -x + 4|x - 2|$ trên đoạn $[0, 4]$:
     - Khi $x \in [0, 2]$: $h(x) = -x + 4(2 - x) = 8 - 5x$, nghịch biến, đạt cực tiểu tại $x = 2$ với giá trị $h(2) = 8 - 10 = -2$.
     - Khi $x \in [2, 4]$: $h(x) = -x + 4(x - 2) = 3x - 8$, đồng biến, đạt cực tiểu tại $x = 2$ với giá trị $h(2) = 6 - 8 = -2$.
   
   Như vậy, vị trí tối ưu duy nhất mới là:
   $$
   (x^*, y^*) = (2, 0).
   $$
   Giá trị hàm mục tiêu tối ưu: $g(2, 0) = 24 - 2 + 0 + 4(0) = 22$. Trọng số kết nối lớn của khối $D$ ($C_{CD} = 4$) đã kéo tọa độ $x$ về ngay trung vị $x = 2$.
:::

::: exercise 3. Nới lỏng lồi cho ràng buộc không chồng lấn
Cho hai khối hình vuông kích thước $2 \times 2$. Ràng buộc không chồng lấn là: Biểu thức $|x_1 - x_2| \ge 2$ hoặc $|y_1 - y_2| \ge 2$.
1. Giải thích vì sao miền khả thi của cặp tọa độ $(x_1, y_1)$ và $(x_2, y_2)$ không phải là tập lồi.
2. Nêu kỹ thuật biến đổi sử dụng biến nhị phân (Big-M method) để mô hình hóa ràng buộc này trong Quy hoạch hỗn hợp số nguyên (MILP).
3. Trong phương pháp nới lỏng lồi (Convex Relaxation), nếu bỏ qua tính rời rạc của biến nhị phân, điều gì xảy ra với hai khối?
:::

::: solution
1. **Tính phi lồi của miền khả thi**:
   Miền không chồng lấn là phần bù của một hình vuông mở:
   $$
   \mathcal{F} = \big\{ (\Delta x, \Delta y) \in \mathbb{R}^2 \mid \max\{|\Delta x|, |\Delta y|\} \ge 2 \big\},
   $$
   trong đó $\Delta x = x_1 - x_2$ và $\Delta y = y_1 - y_2$.
   Lấy hai điểm khả thi:
   - Điểm $A = (2, 0) \in \mathcal{F}$ (khối 1 ở bên phải khối 2 khoảng cách 2).
   - Điểm $B = (-2, 0) \in \mathcal{F}$ (khối 1 ở bên trái khối 2 khoảng cách 2).
   Trung điểm của đoạn $AB$ là $M = \frac{1}{2}A + \frac{1}{2}B = (0, 0)$.
   Tại $M$, $\Delta x = 0$ và $\Delta y = 0$, suy ra hai khối đè khít lên nhau, $M \notin \mathcal{F}$.
   Vì đoạn nối giữa hai điểm khả thi chứa điểm không khả thi, miền khả thi hoàn toàn không lồi.

2. **Kỹ thuật Big-M trong MILP**:
   Để chọn một trong bốn điều kiện, ta đưa vào bốn biến nhị phân $b_1, b_2, b_3, b_4 \in \{0, 1\}$ và một hằng số đủ lớn $M > 0$:
   $$
   \begin{aligned}
   x_1 - x_2 + 2 &\le M(1 - b_1), \\
   x_2 - x_1 + 2 &\le M(1 - b_2), \\
   y_1 - y_2 + 2 &\le M(1 - b_3), \\
   y_2 - y_1 + 2 &\le M(1 - b_4), \\
   b_1 + b_2 + b_3 + b_4 &\ge 1.
   \end{aligned}
   $$
   Khi biến nhị phân $b_1 = 1$, vế phải bằng 0 và ràng buộc $x_1 + 2 \le x_2$ có hiệu lực. Các ràng buộc có $b_k = 0$ có vế phải bằng $M$, hoàn toàn bị vô hiệu hóa.

3. **Hiện tượng khi nới lỏng lồi**:
   Khi nới lỏng các biến nhị phân sang khoảng liên tục $b_k \in [0, 1]$, bộ giải tối ưu sẽ chọn $b_1 = b_2 = b_3 = b_4 = 0{,}25$ với tổng bằng 1. Khi đó mỗi ràng buộc đều bị nới lỏng một khoảng $0{,}75 M$. Kết quả là hai khối có thể tự do xuyên thấu và chồng lấn lên nhau để giảm thiểu tối đa độ dài dây nối. Để giải quyết, người ta kết hợp nới lỏng lồi với thuật toán phân nhánh chặn (Branch-and-Bound) hoặc thuật toán di truyền để cố định cây phân cắt trước.
:::

## Tóm tắt

Quy hoạch mặt bằng (Floor Planning) là minh chứng điển hình cho sự kết hợp khéo léo giữa cấu trúc hình học rời rạc và tối ưu hóa lồi liên tục. Mặc dù bài toán vị trí tương đối mang bản chất tổ hợp phi lồi, việc cố định quan hệ thứ tự qua cây phân cắt slicing tree mở đường cho việc áp dụng Quy hoạch hình học (GP) để tìm kích thước và tỷ lệ khung hình tối ưu toàn cục.

Bên cạnh đó, bài toán tối thiểu hóa độ dài dây dẫn kết nối theo chuẩn Manhattan đưa trực tiếp về Quy hoạch tuyến tính (LP), cung cấp các thuật toán giải quyết nhanh chóng và chuẩn xác cho các bài toán phân bổ không gian và bố trí linh kiện quy mô lớn trong công nghiệp bán dẫn và trí tuệ nhân tạo.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press, Chapter 8: Geometric Problems (§8.8).
