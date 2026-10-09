---
title: Bài tập ôn luyện - Giải thuật nền tảng của Khoa học dữ liệu
description: Tuyển tập bài tập phân tích, tính toán giải tích và giải thuật cho dữ liệu quy mô lớn (Streaming, MinHash/LSH, PageRank, SVD).
---

# Bài tập ôn luyện: Giải thuật nền tảng của Khoa học dữ liệu

Tài liệu tuyển chọn hệ thống bài tập cho môn Giải thuật nền tảng của Khoa học dữ liệu. Các bài toán được phân loại theo cấu trúc các phần học thuật của môn, bao gồm câu hỏi lý thuyết định tính, bài toán tính toán giải tích và bài toán phân tích giải thuật.

---

## Phần 1. Dòng dữ liệu lớn và thuật toán phác họa (Data Streams & Sketches)

### Bài 1.1: Phân tích xác suất dương tính giả của Bloom Filter
Một bộ lọc Bloom (Bloom Filter) sử dụng mảng bit có kích thước $m = 64$ bit và $k = 4$ hàm băm độc lập có phân phối đều trên dải $\{0, 1, \dots, m-1\}$. Giả sử ta lần lượt chèn $n = 8$ phần tử vào bộ lọc.

1. Tính xác suất một bit cụ thể vẫn giữ giá trị $0$ sau khi đã chèn toàn bộ $n$ phần tử.
2. Tính xác suất xảy ra lỗi dương tính giả (false positive rate $\epsilon$) khi truy vấn một phần tử chưa từng xuất hiện trong tập hợp.
3. Cho trước số lượng phần tử cần lưu trữ $n$ và kích thước mảng $m$, chứng minh rằng số lượng hàm băm tối ưu $k^*$ nhằm cực tiểu hóa xác suất dương tính giả là:
   $$k^* = \frac{m}{n} \ln 2$$

#### Lời giải gợi ý
1. Sau khi chèn $n$ phần tử với $k$ hàm băm, tổng số lần chọn bit ngẫu nhiên là $k \cdot n$. Xác suất một bit cụ thể không bị gán giá trị $1$ ở một lượt băm là $1 - \frac{1}{m}$. Do các hàm băm độc lập:
   $$P(\text{bit} = 0) = \left(1 - \frac{1}{m}\right)^{kn} \approx e^{-\frac{kn}{m}}$$
   Thay số với $m = 64, k = 4, n = 8$:
   $$P(\text{bit} = 0) \approx \left(1 - \frac{1}{64}\right)^{32} = \left(\frac{63}{64}\right)^{32} \approx e^{-0.5} \approx 0.6050$$

2. Một truy vấn phần tử mới nhận kết quả dương tính giả khi tất cả $k$ vị trí băm của nó đều có giá trị $1$:
   $$\epsilon = \left(1 - P(\text{bit} = 0)\right)^k \approx \left(1 - 0.6050\right)^4 = (0.3950)^4 \approx 0.0243 \quad (2.43\%)$$

3. Xét hàm mục tiêu $f(k) = (1 - e^{-kn/m})^k$. Đặt $p = e^{-kn/m}$, ta có $\ln f(k) = k \ln(1 - p) = -\frac{m}{n} \ln(p) \ln(1-p)$. Đạo hàm theo $p$ và giải $p = \frac{1}{2}$, dẫn đến $e^{-kn/m} = \frac{1}{2} \iff k^* = \frac{m}{n} \ln 2$.

---

### Bài 1.2: Ước lượng số phần tử phân biệt bằng thuật toán Flajolet–Martin (HyperLogLog Intuition)
Cho một dòng dữ liệu chứa các định danh số nguyên. Ta sử dụng hàm băm $h(x)$ ánh xạ mỗi giá trị vào chuỗi nhị phân $32$-bit. Gọi $\rho(y)$ là số lượng số $0$ liên tiếp tính từ bit cuối cùng (least significant bit) của $y = h(x)$ trước khi gặp bit $1$ đầu tiên (ví dụ: $\rho(\dots 1000_2) = 3$).

1. Tại sao giá trị $\rho(h(x)) = r$ lại xuất hiện với xác suất xấp xỉ $2^{-(r+1)}$?
2. Giả sử sau khi duyệt qua toàn bộ dòng dữ liệu, giá trị lớn nhất ghi nhận được là $R = \max_{x} \rho(h(x)) = 5$. Ước lượng số lượng phần tử phân biệt $F_0$ theo công thức Flajolet–Martin cơ sở $2^R / \phi$ (với hệ số hiệu chỉnh $\phi \approx 0.7735$).
3. Nêu nguyên nhân khiến phương sai của ước lượng đơn lẻ rất lớn và cách thức kỹ thuật Stochastic Averaging (chia bucket) khắc phục nhược điểm này.

#### Lời giải gợi ý
1. Với hàm băm lý tưởng phân phối đều ngẫu nhiên, mỗi bit có xác suất nhận giá trị $0$ hoặc $1$ độc lập bằng $\frac{1}{2}$. Do đó, xác suất chuỗi bit kết thúc bằng $r$ chữ số $0$ và tiếp theo là chữ số $1$ là $(\frac{1}{2})^r \times (\frac{1}{2}) = (\frac{1}{2})^{r+1}$.
2. Ước lượng số phần tử phân biệt:
   $$\hat{F}_0 = \frac{2^R}{\phi} = \frac{2^5}{0.7735} \approx \frac{32}{0.7735} \approx 41.37 \approx 41$$
3. Ước lượng đơn lẻ có phương sai lớn vì $R$ là một số nguyên rời rạc, làm cho ước lượng $2^R$ biến thiên theo lũy thừa của 2. Kỹ thuật chia bucket (như trong HyperLogLog) dùng $b$ bit đầu tiên của hàm băm để chia dòng dữ liệu thành $m = 2^b$ bucket độc lập, sau đó lấy trung bình điều hòa (harmonic mean) của các ước lượng trong từng bucket để triệt tiêu ảnh hưởng của các giá trị ngoại lai cực đoan.

---

## Phần 2. Tìm kiếm tương đồng trong không gian nhiều chiều (MinHash & LSH)

### Bài 2.1: Ma trận đặc trưng và tính toán MinHash Signature
Xét tập hợp các văn bản $\{D_1, D_2, D_3, D_4\}$ với tập từ vựng gồm 5 từ $\{w_1, w_2, w_3, w_4, w_5\}$. Ma trận đặc trưng nhị phân (hàng là từ, cột là văn bản) được cho như sau:

| Từ | $D_1$ | $D_2$ | $D_3$ | $D_4$ |
| :--- | :---: | :---: | :---: | :---: |
| $w_1$ | 1 | 0 | 0 | 1 |
| $w_2$ | 0 | 0 | 1 | 0 |
| $w_3$ | 1 | 1 | 0 | 1 |
| $w_4$ | 1 | 0 | 1 | 1 |
| $w_5$ | 0 | 1 | 0 | 0 |

1. Tính độ tương đồng Jaccard thực tế giữa cặp $(D_1, D_4)$ và cặp $(D_1, D_2)$.
2. Áp dụng hai hàm hoán vị ngẫu nhiên $\pi_1 = (2, 4, 1, 5, 3)$ và $\pi_2 = (4, 1, 3, 2, 5)$ (trong đó giá trị biểu thị chỉ số hàng mới sau khi hoán vị). Lập ma trận chữ ký MinHash (MinHash Signature Matrix).
3. Kiểm tra tính chất: $P(h(D_i) = h(D_j)) = J(D_i, D_j)$ qua ví dụ trên.

#### Lời giải gợi ý
1. Tính độ tương đồng Jaccard $J(A, B) = \frac{|A \cap B|}{|A \cup B|}$:
   - Đối với $(D_1, D_4)$: $D_1 = \{w_1, w_3, w_4\}$, $D_4 = \{w_1, w_3, w_4\}$. Do đó $D_1 \cap D_4 = \{w_1, w_3, w_4\}$ và $D_1 \cup D_4 = \{w_1, w_3, w_4\}$.
     $$J(D_1, D_4) = \frac{3}{3} = 1.0$$
   - Đối với $(D_1, D_2)$: $D_1 = \{w_1, w_3, w_4\}$, $D_2 = \{w_3, w_5\}$.
     Giao là $\{w_3\}$, hợp là $\{w_1, w_3, w_4, w_5\}$.
     $$J(D_1, D_2) = \frac{1}{4} = 0.25$$

2. Xét thứ tự duyệt của từng hoán vị:
   - Với $\pi_1$: Thứ tự hàng gốc tương ứng là $w_3 \to w_1 \to w_5 \to w_2 \to w_4$.
     - $D_1$: hàng đầu tiên có số 1 là $w_3 \implies \text{sig}_{\pi_1}(D_1) = 3$ (hoặc chỉ số hàng hoán vị nhỏ nhất là 1).
     - $D_2$: $w_3$ có số 1 $\implies \text{sig}_{\pi_1}(D_2) = 3$.
     - $D_3$: $w_3, w_1, w_5$ đều là 0, hàng đầu tiên có 1 là $w_2 \implies \text{sig}_{\pi_1}(D_3) = 2$.
     - $D_4$: $w_3$ có số 1 $\implies \text{sig}_{\pi_1}(D_4) = 3$.
   - Với $\pi_2$: Thứ tự duyệt tương ứng với hoán vị $\pi_2$. Ta xác định chỉ số hàng xuất hiện bit 1 đầu tiên cho mỗi cột để xây dựng vector chữ ký có kích thước $2 \times 4$.

---

### Bài 2.2: Phân tích đường cong S-curve trong Locality-Sensitive Hashing (LSH)
Một hệ thống LSH chia ma trận chữ ký MinHash gồm $n = 100$ hàng thành $b = 20$ dải (bands), mỗi dải chứa $r = 5$ hàng ($n = b \cdot r$).

1. Thiết lập công thức tính xác suất $P(s)$ để hai tài liệu có độ tương đồng Jaccard $s$ được xem là một cặp ứng viên (candidate pair).
2. Tính xác suất để một cặp văn bản có $s = 0.8$ được phát hiện.
3. Tính xác suất một cặp văn bản có $s = 0.2$ bị nhận nhầm thành cặp ứng viên (false positive).
4. Xác định ngưỡng tương đồng $s_0$ (điểm uốn của đường cong S-curve) tại đó $P(s_0) \approx 0.5$.

#### Lời giải gợi ý
1. Hai tài liệu đồng nhất trong toàn bộ $r$ hàng của một dải cụ thể với xác suất $s^r$.
   Xác suất chúng không đồng nhất trong dải đó là $1 - s^r$.
   Xác suất chúng không đồng nhất trong cả $b$ dải độc lập là $(1 - s^r)^b$.
   Vậy xác suất trở thành cặp ứng viên (ít nhất một dải đồng nhất hoàn toàn) là:
   $$P(s) = 1 - (1 - s^r)^b$$

2. Với $s = 0.8, b = 20, r = 5$:
   $$s^r = (0.8)^5 = 0.32768$$
   $$
   \begin{aligned}
   P(0.8) &= 1 - (1 - 0.32768)^{20} \\
   &= 1 - (0.67232)^{20} \approx 1 - 0.00035 = 0.99965 \quad (99.965\%).
   \end{aligned}
   $$

3. Với $s = 0.2, b = 20, r = 5$:
   $$s^r = (0.2)^5 = 0.00032$$
   $$
   \begin{aligned}
   P(0.2) &= 1 - (1 - 0.00032)^{20} \\
   &\approx 1 - (1 - 20 \times 0.00032) = 20 \times 0.00032 = 0.00638 \quad (0.64\%).
   \end{aligned}
   $$

4. Điểm ngưỡng xấp xỉ:
   $$s_0 \approx \left(\frac{1}{b}\right)^{1/r} = \left(\frac{1}{20}\right)^{\frac{1}{5}} = (0.05)^{0.2} \approx 0.549$$

---

## Phần 3. Phân tích đồ thị liên kết (PageRank & Random Walk)

### Bài 3.1: Tính toán lặp ma trận PageRank với hệ số suy giảm (Damping Factor)
Xét đồ thị web gồm 3 trang $A, B, C$ với các liên kết có hướng:
- $A \to B, A \to C$
- $B \to C$
- $C \to A$

1. Viết ma trận chuyển đổi ngẫu nhiên $M$ của đồ thị.
2. Với hệ số suy giảm $d = 0.85$, viết công thức cập nhật PageRank dạng ma trận:
   $$r^{(k+1)} = d M r^{(k)} + \frac{1 - d}{N} \mathbf{1}$$
3. Khởi tạo $r^{(0)} = [\frac{1}{3}, \frac{1}{3}, \frac{1}{3}]^T$. Thực hiện 2 bước lặp lũy thừa (Power Iteration) để tìm $r^{(1)}$ và $r^{(2)}$.
4. Giải hệ phương trình trạng thái dừng $r^* = d M r^* + \frac{1-d}{N} \mathbf{1}$ cùng điều kiện chuẩn hóa $\sum r_i = 1$ để tìm phân phối PageRank chính xác.

Điều kiện chuẩn hóa viết đầy đủ là $r_1+\cdots+r_N=1$, hay $\sum_{i=1}^N r_i=1$. Chỉ số $i$ chạy qua các trang. Tổng bằng 1 không có nghĩa mọi điểm đều bằng nhau.

#### Lời giải gợi ý
1. Ma trận chuyển vị $M$ (trong đó phần tử $M_{ij}$ là xác suất nhảy từ trang $j$ sang trang $i$):
   - Từ $A$: chia đều cho $B$ và $C \implies$ cột 1 là $[0, \frac{1}{2}, \frac{1}{2}]^T$.
   - Từ $B$: trỏ đến $C \implies$ cột 2 là $[0, 0, 1]^T$.
   - Từ $C$: trỏ đến $A \implies$ cột 3 là $[1, 0, 0]^T$.
   $$M = \begin{bmatrix} 0 & 0 & 1 \\ \frac{1}{2} & 0 & 0 \\ \frac{1}{2} & 1 & 0 \end{bmatrix}$$

2. Với $N = 3, d = 0.85 \implies \frac{1-d}{3} = \frac{0.15}{3} = 0.05$:
   $$r^{(k+1)} = 0.85 \begin{bmatrix} 0 & 0 & 1 \\ 0.5 & 0 & 0 \\ 0.5 & 1 & 0 \end{bmatrix} r^{(k)} + \begin{bmatrix} 0.05 \\ 0.05 \\ 0.05 \end{bmatrix}$$

3. Khởi tạo $r^{(0)} = [0.3333, 0.3333, 0.3333]^T$:
   $$
   \begin{aligned}
   r^{(1)} &= 0.85 \begin{bmatrix} 0.3333 \\ 0.1667 \\ 0.5000 \end{bmatrix} + \begin{bmatrix} 0.05 \\ 0.05 \\ 0.05 \end{bmatrix} \\
   &= \begin{bmatrix} 0.2833 + 0.05 \\ 0.1417 + 0.05 \\ 0.4250 + 0.05 \end{bmatrix} = \begin{bmatrix} 0.3333 \\ 0.1917 \\ 0.4750 \end{bmatrix}.
   \end{aligned}
   $$
   Tiếp tục thay $r^{(1)}$ vào để tính $r^{(2)}$.

---

## Phần 4. Giảm chiều dữ liệu & Phân tích ma trận (SVD & Low-Rank Approximation)

### Bài 4.1: Phân tích giá trị suy biến (SVD) và xấp xỉ hạng thấp
Cho ma trận dữ liệu $A \in \mathbb{R}^{2 \times 2}$:
$$A = \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix}$$

1. Tính ma trận đối xứng $A^T A$ và xác định các giá trị riêng $\lambda_1, \lambda_2$ cùng vector riêng trực chuẩn tương ứng.
2. Xác định các giá trị suy biến $\sigma_1, \sigma_2$ của $A$.
3. Tìm phân tích SVD đầy đủ: $A = U \Sigma V^T$.
4. Xác định ma trận xấp xỉ hạng 1 tốt nhất $A_1$ theo định lý Eckart–Young–Mirsky và tính sai số Frobenius $\|A - A_1\|_F$.

#### Lời giải gợi ý
1. Tính $A^T A$:
   $$A^T A = \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix} \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix} = \begin{bmatrix} 13 & 12 \\ 12 & 13 \end{bmatrix}$$
   Phương trình đặc trưng:
   $$
   \begin{aligned}
   \det(A^T A - \lambda I) &= (13 - \lambda)^2 - 12^2 \\
   &= (13 - \lambda - 12)(13 - \lambda + 12) \\
   &= (1 - \lambda)(25 - \lambda) = 0.
   \end{aligned}
   $$
   Suy ra $\lambda_1 = 25, \lambda_2 = 1$.
   Vector riêng trực chuẩn:
   - Với $\lambda_1 = 25$: $v_1 = \frac{1}{\sqrt{2}} [1, 1]^T$.
   - Với $\lambda_2 = 1$: $v_2 = \frac{1}{\sqrt{2}} [-1, 1]^T$.

2. Giá trị suy biến:
   $$\sigma_1 = \sqrt{\lambda_1} = 5, \quad \sigma_2 = \sqrt{\lambda_2} = 1$$
   Ma trận $\Sigma = \begin{bmatrix} 5 & 0 \\ 0 & 1 \end{bmatrix}$.

3. Ma trận $V = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$. Vector cột của $U$:
   $$u_1 = \frac{1}{\sigma_1} A v_1 = \frac{1}{5} \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix} \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} = \frac{1}{5} \begin{bmatrix} 5/\sqrt{2} \\ 5/\sqrt{2} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
   $$u_2 = \frac{1}{\sigma_2} A v_2 = \frac{1}{1} \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix} \begin{bmatrix} -1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} = \frac{1}{\sqrt{2}} \begin{bmatrix} -1 \\ 1 \end{bmatrix}$$
   Vậy $A = U \Sigma V^T$.

4. Ma trận hạng 1 xấp xỉ tốt nhất:
   $$A_1 = \sigma_1 u_1 v_1^T = 5 \left(\frac{1}{\sqrt{2}} \begin{bmatrix} 1 \\ 1 \end{bmatrix}\right) \left(\frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \end{bmatrix}\right) = \frac{5}{2} \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix} = \begin{bmatrix} 2.5 & 2.5 \\ 2.5 & 2.5 \end{bmatrix}$$
   Sai số Frobenius chính bằng giá trị suy biến bị loại bỏ:
   $$\|A - A_1\|_F = \sigma_2 = 1$$
