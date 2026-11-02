---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-4-datalog-ngon-ngu-luat-quan-he
title: "15.4 Datalog: Ngôn ngữ luật quan hệ"
description: "Ngôn ngữ Datalog mở rộng câu tuyển xác định cho quan hệ và cá thể: Cú pháp luật, sự kiện, truy vấn chứa biến và cơ chế rút trích câu trả lời."
---

Datalog mở rộng ngôn ngữ các câu tuyển xác định mệnh đề ([propositional definite clauses](https://artint.info/3e/html/ArtInt3e.Ch5.S2.html)) để tích hợp đầy đủ các cá thể và mối quan hệ. Ta có thể xem Datalog như một ngôn ngữ logic vị từ rút gọn:

1. **Chỉ cho phép các câu tuyển xác định (definite clauses)** có dạng:

   $$
   h \leftarrow a_{1} \wedge \ldots \wedge a_{m}
   $$

   Trong đó, $h$ là đầu tuyển (head) và $a_{1} \wedge \ldots \wedge a_{m}$ là thân tuyển (body).
   - Nếu $m > 0$, câu tuyển được gọi là một **luật** (rule).
   - Nếu $m = 0$, ký hiệu suy luận "$\leftarrow$" được lược bỏ và câu tuyển được gọi là một **sự kiện** (fact).
2. **Không khai báo lượng từ tường minh**: Mọi biến logic xuất hiện trong câu tuyển đều được mặc định lượng từ hóa với mọi ($\forall$) ở phạm vi toàn bộ câu.

Ví dụ, câu tuyển $h(X) \leftarrow b(X, Y)$ có ngữ nghĩa hình thức là:

$$
\forall X~\forall Y~\Big(h(X) \leftarrow b(X, Y)\Big)
$$

Biểu thức này tương đương logic với:

$$
\forall X~\Big(h(X) \leftarrow \exists Y~b(X, Y)\Big)
$$

Datalog giữ vị trí trung tâm trong khoa học dữ liệu và trí tuệ nhân tạo vì nó vừa là một ngôn ngữ biểu diễn tri thức khai báo, vừa đóng vai trò như một ngôn ngữ cơ sở dữ liệu để định nghĩa và truy vấn các quan hệ.

::: example Ví dụ 15.10: Biểu diễn quan hệ bảng thời khóa biểu
Trong hệ quản trị cơ sở dữ liệu quan hệ, bảng thời khóa biểu thường được tổ chức như sau:

| Khóa học (Course) | Lớp học phần (Section) | Giờ học (Time) | Phòng học (Room) |
| :--- | :--- | :--- | :--- |
| `cs111` | `7` | `830` | `dp101` |
| `cs422` | `2` | `1030` | `cc208` |
| `cs502` | `1` | `1230` | `dp202` |

Trong Datalog, bảng dữ liệu này được mô hình hóa tự nhiên bằng vị từ 4 ngôi `scheduled(Course, Section, Time, Room)` với ba sự kiện cụ thể:

```prolog
scheduled(cs111, 7, 830, dp101).
scheduled(cs422, 2, 1030, cc208).
scheduled(cs502, 1, 1230, dp202).
```

Giả sử ta có thêm quan hệ sinh viên đăng ký môn học `enrolled(StudentNum, Course, Section)`. Quan hệ `busy(StudentNum, Time)` (xác định sinh viên có lịch bận vào giờ nào) chính là phép kết nối tự nhiên (join) giữa hai bảng, sau đó chiếu (project) lên mã sinh viên và thời gian:

```prolog
busy(Student, Time) :-
    enrolled(Student, Course, Section),
    scheduled(Course, Section, Time, Room).
```

Ý nghĩa trực giác: Một sinh viên có lịch bận tại một khung giờ nếu sinh viên đó đăng ký một lớp học phần được xếp lịch đúng vào khung giờ ấy.
:::

::: example Ví dụ 15.11: Tách biệt tri thức miền và dữ liệu ngôi nhà cụ thể
Xét lại bài toán mạch điện gia đình. Bằng cách tiếp cận quan hệ, ta tách biệt rõ ràng hai nhóm tri thức:

1. **Tri thức tổng quát về nguyên lý vận hành của mạch điện**:
   - Một bóng đèn phát sáng nếu nó là bóng đèn, có dòng điện chạy vào và không bị hỏng:

     <span class="logic-expression logic-block">lit(L) ← light(L) ∧ live(L) ∧ ok(L)</span>

   - Dòng điện lan truyền đệ quy qua các dây dẫn nối tiếp nhau:

     <span class="logic-expression logic-block">live(X) ← connected_to(X, Y) ∧ live(Y)</span>

   - Nguồn điện lưới bên ngoài luôn có điện:

     $$
     live(outside)
     $$

2. **Cấu hình phần cứng cụ thể của ngôi nhà**:
   ```prolog
   light(l1).
   light(l2).
   down(s1).
   up(s2).
   ok(cb1).
   connected_to(w0, w1) :- up(s2).
   connected_to(w0, w2) :- down(s2).
   connected_to(w1, w3) :- up(s1).
   connected_to(w3, outside) :- ok(cb1).
   ```

Toàn bộ nguyên lý vật lý được tổng quát hóa bằng các biến ($L, X, Y$). Khi cấu hình ngôi nhà thay đổi, ta chỉ cần cập nhật danh sách các sự kiện nối dây mà không phải viết lại quy tắc dẫn điện.
:::

## 15.4.1 Truy vấn chứa biến (Queries with Variables)

Trong logic mệnh đề, người dùng chỉ có thể đặt câu hỏi dạng Có/Không (yes/no). Trong Datalog, các **truy vấn chứa biến** cho phép người dùng tìm kiếm các cá thể thỏa mãn điều kiện bài toán:

- Một **thể hiện** (instance) của truy vấn thu được bằng cách thay thế các biến bằng các số hạng. Mọi lần xuất hiện của cùng một biến phải được thay thế bằng cùng một số hạng duy nhất.
- Câu trả lời cho một truy vấn chứa biến là:
  - Một phép gán cụ thể cho các biến sao cho thể hiện đó là hệ quả logic của cơ sở tri thức ($KB \models q\theta$).
  - Hoặc câu trả lời `no`, nghĩa là không tồn tại thể hiện nào là hệ quả logic. Quá trình tìm kiếm các phép gán biến thỏa mãn được gọi là **rút trích câu trả lời** (answer extraction).

> [!NOTE]
> Câu trả lời `no` không đồng nghĩa với việc câu hỏi bị sai trong thế giới thực; nó chỉ phản ánh rằng cơ sở tri thức hiện tại chưa đủ thông tin để chứng minh khẳng định đó.

::: example Ví dụ 15.12: Cơ sở dữ liệu địa lý Nam Mỹ
Xét cơ sở tri thức Datalog mô tả một số quốc gia Nam Mỹ:

```prolog
% country(C): C là một quốc gia
country(argentina).
country(brazil).
country(chile).
country(paraguay).
country(peru).

% area(C, A): Quốc gia C có diện tích A (km²)
area(argentina, 2780400).
area(brazil, 8515767).
area(chile, 756102).
area(paraguay, 406756).
area(peru, 1285216).

% language(C, L): Ngôn ngữ chính thức L của quốc gia C
language(argentina, spanish).
language(brazil, portuguese).
language(chile, spanish).
language(paraguay, spanish).
language(peru, spanish).

% borders0(C1, C2): C1 và C2 có chung biên giới (C1 đứng trước C2 theo bảng chữ cái)
borders0(chile, peru).
borders0(argentina, chile).
borders0(brazil, peru).
borders0(argentina, brazil).
borders0(brazil, paraguay).
borders0(argentina, paraguay).

% borders(C1, C2): Quan hệ đối xứng hai chiều
borders(X, Y) :- borders0(X, Y).
borders(X, Y) :- borders0(Y, X).
```

Khi người dùng đặt câu hỏi truy vấn:

1. Truy vấn kiểm tra không biến:

   $$
   \text{ask } language(chile, spanish)
   $$

   Hệ thống trả lời: `yes`.
2. Truy vấn ngoài phạm vi tri thức:

   $$
   \text{ask } language(venezuela, spanish)
   $$

   Hệ thống trả lời: `no` (do cơ sở dữ liệu chưa có thông tin về Venezuela).
3. Truy vấn tìm kiếm cá thể:

   $$
   \text{ask } language(C, spanish)
   $$

   Hệ thống trả về 4 kết quả: $C = argentina$, $C = chile$, $C = paraguay$, $C = peru$.
4. Truy vấn quan hệ đối xứng:
   - $\text{ask } borders0(paraguay, X)$ trả về `no`, vì trong danh sách gốc, Paraguay luôn đứng sau theo thứ tự bảng chữ cái.
   - $\text{ask } borders(paraguay, X)$ khai thác hai luật đối xứng và trả về 2 nghiệm: $X = argentina$ và $X = brazil$.
   - $\text{ask } borders(X, Y)$ trả về toàn bộ $6 \times 2 = 12$ cặp biên giới hai chiều.
5. Truy vấn kết hợp điều kiện số học: "Tìm quốc gia giáp ranh với Chile có diện tích lớn hơn 2.000.000 km²":

   <span class="logic-expression logic-block">ask  borders(chile, Y) ∧ area(Y, A) ∧ A &gt; 2000000</span>

   Hệ thống kết hợp thông tin biên giới và diện tích để trả về kết quả duy nhất: $Y = argentina, A = 2780400$.
:::

::: example Ví dụ 15.13: Phân biệt cá thể thực tế và chuỗi ký tự tên gọi
Xét các sự kiện về thủ đô và tên gọi:

```prolog
capital(argentina, buenos_aires).
capital(chile, santiago).
capital(peru, lima).
capital(brazil, brasilia).
capital(paraguay, asuncion).

name(buenos_aires, "Buenos Aires").
name(santiago, "Santiago").
name(lima, "Lima").
name(chile, "Chile").
```

Cần phân biệt rõ giữa hằng số thực thể $chile$ (chỉ quốc gia Chile, một thực thể địa lý có chiều dài bắc - nam hơn 4.270 km) và hằng số chuỗi `"Chile"` (chỉ chuỗi văn bản gồm 5 ký tự chữ cái).

Để truy vấn tên chuỗi của thủ đô nước Chile, ta kết hợp hai nguyên tử vị từ:

<span class="logic-expression logic-block">ask  capital(chile, C) ∧ name(C, N)</span>

Hệ thống suy ra biến thực thể $C = santiago$ và rút trích được chuỗi tên gọi $N = \text{"Santiago"}$.
:::

## Tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Nguồn trực tuyến: [https://artint.info/3e/html/ArtInt3e.Ch15.S4.html](https://artint.info/3e/html/ArtInt3e.Ch15.S4.html).
