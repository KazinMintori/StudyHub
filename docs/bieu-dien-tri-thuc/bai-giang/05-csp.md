---
course: bieu-dien-tri-thuc
lecture: 05-csp
section: lecture
title: "Bài toán thỏa mãn ràng buộc"
prerequisites: ["tap-hop","menh-de"]
lessonStatus: draft
description: "Cấu trúc bài toán CSP, thuật toán lan truyền ràng buộc AC-3, quay lui Backtracking và các kỹ thuật heuristic MRV, Degree, LCV."
---

*Học phần AIT2004 — Cơ sở Trí tuệ Nhân tạo*

← [Chương 4: Tìm kiếm đối kháng](/bieu-dien-tri-thuc/bai-giang/04-tim-kiem-doi-khang.md) · [Mục lục môn học](/bieu-dien-tri-thuc/notes/00-muc-luc.md) · [Chương 14: Logic & Biểu diễn tri thức →](/bieu-dien-tri-thuc/bai-giang/14-logic-bieu-dien-tri-thuc.md)

::: info Trọng tâm bài giảng
Trong các giải thuật tìm kiếm truyền thống (BFS, DFS, A\*), trạng thái của bài toán được đối xử như một chiếc "hộp đen" nguyên tử: Thuật toán chỉ có thể kiểm tra xem trạng thái đó có phải là đích hay không, hoặc mở rộng ra các trạng thái con, chứ không thể nhìn thấu cấu trúc bên trong của trạng thái.

**Bài toán Thỏa mãn Ràng buộc (Constraint Satisfaction Problems - CSP)** mở toang chiếc hộp đen đó ra: Mỗi trạng thái được biểu diễn bằng một tập các biến, mỗi biến nhận giá trị trong một miền xác định, và nghiệm của bài toán là một cấu hình thỏa mãn toàn bộ các ràng buộc luật định. Bài giảng này phân tích:
1. **Hình thức hóa CSP:** Bộ ba $(X, D, C)$ và đồ thị ràng buộc (Constraint Graph).
2. **Lan truyền ràng buộc (Constraint Propagation):** Tính nhất quán cung (Arc Consistency) và thuật toán AC-3.
3. **Tìm kiếm quay lui (Backtracking Search):** Ba nguyên lý định hướng heuristic kinh điển: **MRV**, **Degree Heuristic** và **LCV**.
4. **Tìm kiếm cục bộ (Local Search) với Min-Conflicts:** Giải quyết bài toán hàng triệu biến số trong nháy mắt.
:::

---

## 5.1 Định nghĩa hình thức của CSP

Một bài toán thỏa mãn ràng buộc được định nghĩa bởi bộ ba hình thức $(X, D, C)$:
1. **Tập các biến (Variables $X$):**
   $$
   X = \{X_1, X_2, \ldots, X_n\}
   $$
2. **Tập các miền giá trị (Domains $D$):**
   $$
   D = \{D_1, D_2, \ldots, D_n\}
   $$
   Trong đó mỗi $D_i$ là tập các giá trị hợp lệ mà biến $X_i$ có thể nhận. Miền giá trị có thể rời rạc hữu hạn (màu sắc, ngày trong tuần), rời rạc vô hạn (tập số nguyên $\mathbb{Z}$), hoặc liên tục ($\mathbb{R}$).
3. **Tập các ràng buộc (Constraints $C$):**
   $$
   C = \{C_1, C_2, \ldots, C_m\}
   $$
   Mỗi ràng buộc $C_j$ chỉ định một tập biến tham gia (phạm vi - scope) và một quan hệ xác định các bộ giá trị hợp lệ giữa các biến đó.

### Trạng thái và Lời giải
- **Phép gán (Assignment):** Gán giá trị $v \in D_i$ cho một số biến $X_i$.
- **Phép gán nhất quán (Consistent Assignment):** Phép gán không vi phạm bất kỳ ràng buộc nào trong $C$.
- **Phép gán đầy đủ (Complete Assignment):** Mọi biến trong $X$ đều đã được gán giá trị.
- **Lời giải (Solution):** Một phép gán vừa **đầy đủ**, vừa **nhất quán**.

---

## 5.2 Ví dụ kinh điển: Bài toán Tô màu bản đồ

Xét bài toán tô màu các vùng lãnh thổ của nước Úc bằng 3 màu: Đỏ ($\text{red}$), Xanh lá ($\text{green}$), Xanh dương ($\text{blue}$), sao cho hai vùng có chung biên giới không được trùng màu nhau.

```mermaid
flowchart TD
    WA["Tây Úc (WA)"] --- NT["Bắc Úc (NT)"]
    WA --- SA["Nam Úc (SA)"]
    NT --- SA
    NT --- Q["Queensland (Q)"]
    SA --- Q
    SA --- NSW["New South Wales (NSW)"]
    Q --- NSW
    SA --- V["Victoria (V)"]
    NSW --- V
    T["Tasmania (T)"]

    classDef island fill:#f1f5f9,stroke:#64748b,stroke-dasharray: 4 4;
    class T island;
```

Mô hình hóa CSP:
- **Biến:** $X = \{\text{WA}, \text{NT}, \text{SA}, \text{Q}, \text{NSW}, \text{V}, \text{T}\}$
- **Miền giá trị:** $D_i = \{\text{red}, \text{green}, \text{blue}\}$ với mọi $i$.
- **Ràng buộc:** Các cặp kề nhau phải khác màu:
  $$
  \text{WA} \neq \text{NT}, \quad \text{WA} \neq \text{SA}, \quad \text{NT} \neq \text{SA}, \quad \text{NT} \neq \text{Q}, \quad \ldots
  $$

Một lời giải hợp lệ:
$$
\begin{aligned}
\{ &\text{WA}=\text{red},\; \text{NT}=\text{green},\; \text{SA}=\text{blue},\; \text{Q}=\text{red}, \\
   &\text{NSW}=\text{green},\; \text{V}=\text{red},\; \text{T}=\text{red} \}
\end{aligned}
$$

Lưu ý rằng Tasmania ($\text{T}$) là một hòn đảo độc lập không tiếp giáp với vùng nào, do đó nó có thể nhận bất kỳ màu nào mà không ảnh hưởng tới phần còn lại của lục địa.

---

## 5.3 Lan truyền ràng buộc và Thuật toán AC-3

Trước khi tiến hành tìm kiếm, một cỗ máy thông minh sẽ không vội vàng thử từng giá trị mà sẽ **suy luận để thu hẹp miền giá trị** của các biến. Tiến trình này gọi là **Lan truyền ràng buộc (Constraint Propagation)**.

### Tính nhất quán cung (Arc Consistency)
Một cung có hướng $(X_i, X_j)$ được gọi là **nhất quán cung (arc-consistent)** nếu:
> Với mọi giá trị $x \in D_i$, tồn tại ít nhất một giá trị $y \in D_j$ thỏa mãn ràng buộc nhị phân giữa $X_i$ và $X_j$.

Nếu tồn tại một giá trị $x \in D_i$ mà không có bất kỳ giá trị nào trong $D_j$ tương thích với nó, ta có thể **loại bỏ vĩnh viễn $x$ khỏi miền giá trị $D_i$**.

```mermaid
flowchart TD
    Xi["Xi: {red, green}"] -->|Cung (Xi, Xj): Xi != Xj| Xj["Xj: {red}"]
    note["Loại bỏ 'red' khỏi Xi<br/>-> Xi chỉ còn {green}"]
```

### Thuật toán AC-3 (Arc Consistency Algorithm #3)
AC-3 duy trì một hàng đợi chứa tất cả các cung $(X_i, X_j)$ cần kiểm tra tính nhất quán:
1. Lấy một cung $(X_i, X_j)$ ra khỏi hàng đợi.
2. Kiểm tra xem có giá trị nào trong $D_i$ không tìm được "bạn ghép đôi" hợp lệ trong $D_j$ hay không.
3. Nếu có, xóa các giá trị đó khỏi $D_i$.
4. **Điểm mấu chốt:** Nếu miền $D_i$ bị thu hẹp, mọi biến lân cận $X_k$ trỏ tới $X_i$ đều có nguy cơ mất tính nhất quán! Do đó, ta phải thêm lại tất cả các cung $(X_k, X_i)$ (với $k \neq j$) vào hàng đợi để tái kiểm tra.

```cpp
bool revise(CSP& csp, Variable xi, Variable xj) {
    bool revised = false;
    for (auto it = csp.D[xi].begin(); it != csp.D[xi].end(); ) {
        int x = *it;
        bool hasSupport = false;
        for (int y : csp.D[xj]) {
            if (csp.isSatisfied(xi, x, xj, y)) {
                hasSupport = true;
                break;
            }
        }
        if (!hasSupport) {
            it = csp.D[xi].erase(it); // Xóa giá trị không có bạn ghép đôi
            revised = true;
        } else {
            ++it;
        }
    }
    return revised;
}
```

Độ phức tạp thời gian của AC-3: Giả sử bài toán có $c$ ràng buộc nhị phân (tương ứng $2c$ cung) và kích thước miền giá trị lớn nhất là $d$. Mỗi cung $(X_k, X_i)$ chỉ bị đưa vào hàng đợi tối đa $d$ lần (vì $D_i$ chỉ có tối đa $d$ phần tử để bị xóa). Mỗi lần kiểm tra cung tốn $O(d^2)$. Do đó, thời gian tồi nhất của AC-3 là $O(c \cdot d^3)$ — một chi phí rất nhỏ so với việc tìm kiếm vét cạn hàm mũ!

---

## 5.4 Tìm kiếm quay lui (Backtracking Search) và Bộ ba Heuristic

Tìm kiếm quay lui là giải thuật DFS chuyên dụng cho CSP: Tại mỗi bước, ta chọn **một biến chưa được gán**, gán thử lần lượt từng giá trị trong miền của nó, kiểm tra tính nhất quán; nếu gặp ngõ cụt thì lùi lại (backtrack).

Nếu duyệt ngây thơ, không gian tìm kiếm sẽ bùng nổ $O(d^n)$. Để tăng tốc độ lên hàng ngàn lần, người ta áp dụng ba nguyên tắc heuristic:

```mermaid
flowchart TD
    Q1["1. Chọn biến nào tiếp theo?"] --> H1["MRV (Ít giá trị nhất)<br/>+ Degree Heuristic (Bậc cao nhất)"]
    Q2["2. Thử giá trị nào trước?"] --> H2["LCV (Ít ràng buộc nhất)"]
    Q3["3. Phát hiện sớm ngõ cụt?"] --> H3["Forward Checking / MAC (Duy trì AC-3)"]
```

### 1. Heuristic MRV (Minimum Remaining Values — Thất bại sớm nhất)
- **Quy tắc:** Luôn chọn biến có **số lượng giá trị hợp lệ còn lại trong miền ít nhất** để gán trước.
- **Trực giác bản chất:** Triết lý "Thất bại sớm" (Fail-First). Biến nào càng khó gán, càng ít lựa chọn thì phải ưu tiên xử lý ngay. Nếu nhánh này không thể có nghiệm, nó sẽ bị phát hiện và cắt tỉa ngay từ gốc, ngăn không cho cây tìm kiếm phân nhánh vô ích.

### 2. Heuristic Bậc (Degree Heuristic)
- **Quy tắc:** Dùng để phá vỡ thế hòa điểm (tie-breaker) khi có nhiều biến cùng có giá trị MRV nhỏ nhất. Chọn biến tham gia vào **nhiều ràng buộc nhất đối với các biến chưa được gán khác**.
- **Tác dụng:** Giúp thu hẹp tối đa miền giá trị của các biến còn lại ở các bước tiếp theo.

### 3. Heuristic LCV (Least Constraining Value — Để lại đường sống)
- **Quy tắc:** Khi đã chọn được biến, ta phải quyết định thử giá trị nào trước. Heuristic LCV khuyên: **Hãy ưu tiên giá trị nào loại trừ ít phương án lựa chọn nhất của các biến lân cận.**
- **Trực giác bản chất:** Trái ngược với việc chọn biến (cần chọn biến dễ thất bại nhất), khi chọn giá trị, ta mong muốn tìm ra nghiệm càng nhanh càng tốt. Chọn giá trị "hiền lành nhất" sẽ để lại không gian rộng mở nhất cho các biến tiếp theo tìm được nghiệm hợp lệ.

---

## 5.5 Kiểm tra tiến (Forward Checking) và MAC

Mỗi khi ta gán một giá trị cho biến $X$, ta có thể nhìn trước một bước:
- **Forward Checking:** Với mỗi biến chưa gán $Y$ kề với $X$, lập tức xóa khỏi $D_Y$ bất kỳ giá trị nào xung đột với giá trị vừa gán cho $X$. Nếu bất kỳ miền $D_Y$ nào trở thành rỗng ($\emptyset$), ta lập tức quay lui mà không cần bước tiếp!
- **MAC (Maintaining Arc Consistency):** Thay vì chỉ kiểm tra các biến kề trực tiếp, sau mỗi lần gán giá trị, ta kích hoạt thuật toán AC-3 trên toàn bộ các biến chưa gán để lan truyền triệt để mọi hệ quả.

---

## 5.6 Tìm kiếm cục bộ với Heuristic Min-Conflicts

Với các bài toán quy mô khổng lồ (ví dụ bài toán xếp $N$-Hậu với $N = 1.000.000$ quân cờ), phương pháp quay lui hoàn toàn bất lực. Thay vào đó, người ta sử dụng **Tìm kiếm cục bộ (Local Search)**:
1. Bắt đầu từ một phép gán đầy đủ ngẫu nhiên (chấp nhận có nhiều ràng buộc bị vi phạm).
2. Tại mỗi bước lặp, chọn ngẫu nhiên một biến đang bị xung đột.
3. Thay đổi giá trị của biến đó sang giá trị **gây ra ít xung đột nhất với các biến khác (Min-Conflicts Heuristic)**.
4. Lặp lại cho tới khi số lượng xung đột bằng 0.

Kỳ diệu thay, với xác suất rất cao, heuristic Min-Conflicts có thể tìm ra nghiệm của bài toán $1.000.000$-Hậu chỉ sau vài chục đến vài trăm bước di chuyển!

---

## 5.7 Ứng dụng thực tế của CSP trong Công nghiệp

- **Lập thời khóa biểu và Lịch thi đại học:** Phân bổ hàng trăm môn học, giảng viên và phòng thi vào các ca thi sao cho không sinh viên nào bị trùng lịch thi và không phòng thi nào bị quá tải.
- **Lập lịch bay hàng không:** Điều phối máy bay, tổ bay, tiếp viên và cửa ra vào sân bay (Airport Gate Allocation) đáp ứng các quy định an toàn hàng không nghiêm ngặt.
- **Quy hoạch tài nguyên mạng máy tính:** Phân bổ dải tần số vô tuyến cho các trạm phát sóng di động BTS sao cho các trạm kề cận không gây nhiễu sóng lẫn nhau (bài toán tô màu đồ thị thực tế).
- **Trình biên dịch và Phân bổ thanh ghi (Register Allocation):** Phân bổ số lượng thanh ghi vật lý hạn chế của CPU cho hàng ngàn biến số trong mã nguồn chương trình.

---

## Hệ thống bài tập tự luyện {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu luyện tập.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở các bài tập thực chiến có hướng dẫn chi tiết và kiểm chứng tự động.
:::

