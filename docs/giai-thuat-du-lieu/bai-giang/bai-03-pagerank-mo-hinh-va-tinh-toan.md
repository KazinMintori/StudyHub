---
course: giai-thuat-du-lieu
lecture: bai-03-pagerank-mo-hinh-va-tinh-toan
section: lecture
title: "PageRank: mô hình & tính toán"
prerequisites: ["do-thi","ma-tran"]
lessonStatus: ready
---

← [Bài 02: Map-Reduce](/giai-thuat-du-lieu/bai-giang/bai-02-mapreduce-va-xu-ly-du-lieu-lon.md) · [Mục lục](/giai-thuat-du-lieu/index.md)

## 1. Đặt bài toán và phân tích liên kết đồ thị Web

Trong các hệ thống tìm kiếm thông tin truyền thống (Information Retrieval), việc xếp hạng tài liệu dựa chủ yếu trên sự tương đồng văn bản giữa truy vấn và nội dung (như tần suất từ khóa TF-IDF hoặc BM25). Trên môi trường World Wide Web, phương pháp này bộc lộ hai hạn chế căn bản:

1. **Hiện tượng thao túng nội dung (Keyword Spamming):** Tác giả trang web có thể chủ động lặp lại từ khóa nhiều lần hoặc chèn văn bản ẩn để tăng thứ hạng tìm kiếm.
2. **Thiếu độ đo độ tin cậy độc lập:** Nội dung trang web không phản ánh được mức độ uy tín thực tế của nguồn thông tin.

Để giải quyết vấn đề trên, thuật toán PageRank (Brin & Page, 1998) tiếp cận bài toán xếp hạng dựa trên cấu trúc liên kết siêu văn bản (hyperlink structure):
- Một liên kết có hướng từ trang $j$ đến trang $i$ ($j \to i$) được coi là một sự thừa nhận hoặc giới thiệu từ $j$ dành cho $i$.
- Độ quan trọng của trang $i$ phụ thuộc vào số lượng trang trỏ đến $i$ và mức độ quan trọng của chính các trang trỏ đó.

---

## 2. Mô hình người lướt ngẫu nhiên và chuỗi Markov

### 2.1. Không gian trạng thái và xác suất chuyển

Xét đồ thị có hướng $G = (V, E)$ biểu diễn mạng Web với $N = |V|$ đỉnh. Giả sử một người dùng duyệt web theo mô hình ngẫu nhiên (Random Surfer):
- Tại thời điểm $t$, người dùng đang ở trang $j$.
- Nếu trang $j$ có bậc ra $d_j > 0$, người dùng chọn ngẫu nhiên một trong $d_j$ liên kết ra ngoài với xác suất đồng đều $\frac{1}{d_j}$ để chuyển sang trang kế tiếp.

Mô hình trên cấu thành một chuỗi Markov rời rạc thời gian trên không gian trạng thái hữu hạn $V$. Ma trận chuyển tiếp $M \in \mathbb{R}^{N \times N}$ được định nghĩa bởi:

$$M_{ij} = \begin{cases} \frac{1}{d_j} & \text{nếu } (j, i) \in E \\ 0 & \text{ngược lại} \end{cases}$$

Trong đó, phần tử $M_{ij}$ thể hiện xác suất chuyển từ trạng thái $j$ sang trạng thái $i$. Nếu mọi đỉnh đều có bậc ra $d_j > 0$, thì tổng mỗi cột của $M$ bằng 1:
$$\sum_{i=1}^N M_{ij} = 1 \quad \forall j$$
Khi đó $M$ là một ma trận ngẫu nhiên theo cột (column-stochastic matrix).

### 2.2. Phân phối dừng

Gọi $r_i$ là xác suất người lướt ngẫu nhiên có mặt tại trang $i$ tại trạng thái cân bằng dài hạn. Theo phương trình cân bằng dòng xác suất:

$$r_i = \sum_{j: (j, i) \in E} \frac{r_j}{d_j}$$

Viết dưới dạng vector ma trận:
$$\mathbf{r} = M \mathbf{r}$$

Vector $\mathbf{r} = [r_1, r_2, \dots, r_N]^T$ thỏa mãn điều kiện chuẩn hóa $\sum_{i=1}^N r_i = 1$. Về mặt đại số tuyến tính, $\mathbf{r}$ chính là vector riêng chính (principal eigenvector) của $M$ ứng với trị riêng $\lambda = 1$.

---

## 3. Thuật toán lặp lũy thừa (Power Iteration)

Đối với đồ thị Web quy mô lớn ($N > 10^9$), việc giải phương trình đặc trưng hoặc khử ma trận trực tiếp là không khả thi về mặt tính toán. Phương pháp số được sử dụng là **lặp lũy thừa** (Power Iteration):

### Thuật toán:

1. **Khởi tạo:**
   $$\mathbf{r}^{(0)} = \left[ \frac{1}{N}, \frac{1}{N}, \dots, \frac{1}{N} \right]^T$$
2. **Bước lặp:** Tại bước $t + 1$:
   $$\mathbf{r}^{(t+1)} = M \mathbf{r}^{(t)}$$
3. **Tiêu chuẩn hội tụ:** Dừng khi chuẩn chênh lệch nhỏ hơn ngưỡng $\epsilon$:
   $$\|\mathbf{r}^{(t+1)} - \mathbf{r}^{(t)}\|_1 = \sum_{i=1}^N \left| r_i^{(t+1)} - r_i^{(t)} \right| < \epsilon$$

Theo định lý Perron-Frobenius, dãy $\{\mathbf{r}^{(t)}\}$ sẽ hội tụ về nghiệm duy nhất nếu ma trận $M$ là ngẫu nhiên, tối giản (irreducible) và phi chu kỳ (aperiodic).

---

## 4. Các cấu trúc đồ thị đặc biệt: Dead Ends và Spider Traps

Trên đồ thị thực tế, hai điều kiện tối giản và ngẫu nhiên thường bị vi phạm do hai cấu trúc sau:

### 4.1. Đỉnh cụt (Dead Ends)
Đỉnh cụt là các trang không có liên kết ra ($d_j = 0$). Trong ma trận $M$, cột tương ứng chứa toàn giá trị 0 (ma trận trở thành sub-stochastic).

- **Hệ quả:** Xác suất tại các đỉnh này không được chuyển tiếp sang các đỉnh khác. Sau mỗi vòng lặp, tổng chuẩn $\|\mathbf{r}^{(t)}\|_1$ suy giảm dần về 0.
- **Xử lý:** Quy ước nếu gặp đỉnh cụt, người dùng chuyển ngẫu nhiên đến một đỉnh bất kỳ trong toàn bộ mạng với xác suất $\frac{1}{N}$.

### 4.2. Bẫy chu trình (Spider Traps)
Bẫy chu trình là tập hợp các đỉnh chỉ có liên kết nội bộ, không có đường ra tới phần còn lại của đồ thị (ví dụ một trang tự trỏ vào chính nó).

- **Hệ quả:** Xác suất tích tụ dần trong bẫy qua các bước lặp. Tại trạng thái dừng, toàn bộ điểm số của mạng dồn về các đỉnh trong bẫy ($r_i \to 1$), trong khi các đỉnh khác tiệm cận 0.

---

## 5. Mô hình suy giảm và bước nhảy ngẫu nhiên (Random Walk with Teleportation)

Để đảm bảo tính hội tụ đồng thời giải quyết triệt để Dead Ends và Spider Traps, mô hình người lướt ngẫu nhiên được điều chỉnh bổ sung cơ chế **nhảy ngẫu nhiên (teleportation)**:

Tại mỗi bước:
- Với xác suất $\beta \in (0, 1)$, người dùng di chuyển theo liên kết có sẵn.
- Với xác suất $1 - \beta$, người dùng nhảy ngẫu nhiên đến một trang bất kỳ trên toàn bộ mạng.

Phương trình PageRank hiệu chỉnh:

$$\mathbf{r} = \beta M \mathbf{r} + \frac{1 - \beta}{N} \mathbf{1}$$

Trong đó:
- $\beta$ là hệ số suy giảm (damping factor), thực nghiệm thực tế thường đặt $\beta = 0.85$.
- $\mathbf{1} \in \mathbb{R}^{N \times 1}$ là vector gồm toàn phần tử 1.
- Ma trận chuyển tiếp hiệu chỉnh tương đương:
  $$A = \beta M + \frac{1 - \beta}{N} \mathbf{E}$$
  với $\mathbf{E} = \mathbf{1}\mathbf{1}^T$. Ma trận $A$ là ma trận dương và ngẫu nhiên theo cột, đảm bảo chuỗi Markov có phân phối dừng duy nhất và hội tụ tuyến tính với tốc độ phụ thuộc vào $\beta$.

---

## 6. Ví dụ tính toán từng bước

Xét đồ thị gồm 3 trang $A, B, C$ với tập liên kết: $A \to B, A \to C, B \to C, C \to A$.

Bậc ra: $d_A = 2, d_B = 1, d_C = 1$.

Ma trận chuyển tiếp $M$:
$$M = \begin{bmatrix}
0 & 0 & 1 \\
1/2 & 0 & 0 \\
1/2 & 1 & 0
\end{bmatrix}$$

Chọn $\beta = 0.85, N = 3$. Thành phần nhảy ngẫu nhiên: $\frac{1 - \beta}{N} = \frac{0.15}{3} = 0.05$.

### Bước 0:
$$\mathbf{r}^{(0)} = \begin{bmatrix} 1/3 \\ 1/3 \\ 1/3 \end{bmatrix} \approx \begin{bmatrix} 0.3333 \\ 0.3333 \\ 0.3333 \end{bmatrix}$$

### Bước 1:
$$M \mathbf{r}^{(0)} = \begin{bmatrix} 0.3333 \\ 0.1667 \\ 0.5000 \end{bmatrix}$$
$$\mathbf{r}^{(1)} = 0.85 \begin{bmatrix} 0.3333 \\ 0.1667 \\ 0.5000 \end{bmatrix} + \begin{bmatrix} 0.05 \\ 0.05 \\ 0.05 \end{bmatrix} = \begin{bmatrix} 0.3333 \\ 0.1917 \\ 0.4750 \end{bmatrix}$$

### Bước 2:
$$M \mathbf{r}^{(1)} = \begin{bmatrix} 0.4750 \\ 0.1667 \\ 0.3583 \end{bmatrix}$$
$$\mathbf{r}^{(2)} = 0.85 \begin{bmatrix} 0.4750 \\ 0.1667 \\ 0.3583 \end{bmatrix} + \begin{bmatrix} 0.05 \\ 0.05 \\ 0.05 \end{bmatrix} = \begin{bmatrix} 0.4538 \\ 0.1917 \\ 0.3546 \end{bmatrix}$$

Sau khi lặp đến hội tụ ($\epsilon < 10^{-5}$):
$$\mathbf{r}^* \approx \begin{bmatrix} 0.3877 \\ 0.2148 \\ 0.3975 \end{bmatrix}$$

Thứ hạng các trang: $C > A > B$.

---

## 7. Cài đặt thuật toán trên mô hình phân tán MapReduce

Trong điều kiện $N$ rất lớn, việc tính toán $\mathbf{r}^{(t+1)} = \beta M \mathbf{r}^{(t)} + \frac{1 - \beta}{N} \mathbf{1}$ được tổ chức trên kiến trúc phân tán như sau:

- Biểu diễn đồ thị thưa: Mỗi dòng lưu bản ghi `(u, r_u, [v_1, v_2, ..., v_k])` với $u$ là trang nguồn, $r_u$ là điểm số tại bước hiện tại, và danh sách các đỉnh kề $v_i$.
- **Giai đoạn Map:**
  - Nhận đầu vào là bản ghi đỉnh $u$.
  - Phát cặp khóa-giá trị: `(v_i, r_u / k)` cho từng đỉnh kề $v_i$.
  - Phát lại cấu trúc đồ thị: `(u, [v_1, ..., v_k])` để duy trì dữ liệu liên kết cho vòng sau.
- **Giai đoạn Reduce:**
  - Nhóm theo khóa $v_i$.
  - Tính tổng các giá trị đóng góp: $S_{v_i} = \sum \text{values}$.
  - Tính điểm mới: $r_{v_i}^{\text{mới}} = \beta \cdot S_{v_i} + \frac{1 - \beta}{N}$.
  - Ghi bản ghi cập nhật ra hệ thống lưu trữ phân tán.

---

## 8. Cài đặt tham khảo bằng Python

```python
import numpy as np

def pagerank(M, beta=0.85, tol=1e-6, max_iter=100):
    """
    Tính vector PageRank bằng phương pháp lặp lũy thừa.
    
    Tham số:
        M: np.ndarray, kích thước (N, N), ma trận chuyển tiếp Markov.
        beta: float, hệ số suy giảm (mặc định 0.85).
        tol: float, ngưỡng hội tụ cho chuẩn L1.
        max_iter: int, số vòng lặp tối đa.
        
    Trả về:
        r: np.ndarray, vector điểm phân phối dừng (N,).
    """
    N = M.shape[0]
    r = np.ones(N) / N
    teleport = (1.0 - beta) / N

    for it in range(max_iter):
        r_next = beta * M.dot(r) + teleport
        diff = np.linalg.norm(r_next - r, ord=1)
        r = r_next
        if diff < tol:
            break

    return r

if __name__ == '__main__':
    # Ma trận chuyển tiếp ví dụ mục 6
    M = np.array([
        [0.0, 0.0, 1.0],
        [0.5, 0.0, 0.0],
        [0.5, 1.0, 0.0]
    ])

    scores = pagerank(M)
    for idx, name in enumerate(['A', 'B', 'C']):
        print(f"Trang {name}: {scores[idx]:.4f}")
```

---

← [Bài 02: Map-Reduce](/giai-thuat-du-lieu/bai-giang/bai-02-mapreduce-va-xu-ly-du-lieu-lon.md) · [Mục lục học phần](/giai-thuat-du-lieu/index.md)
