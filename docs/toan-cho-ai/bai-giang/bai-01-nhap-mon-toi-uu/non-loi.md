---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: non-loi
section: topic
title: "Nón và nón lồi"
description: "Nón, nón lồi, tổ hợp nón và bao nón, đặt cạnh nhau với bốn loại tổ hợp tuyến tính, affine, lồi và nón. Các ví dụ cơ bản và bài toán kiểm tra một vector có thuộc một nón hay không."
---

Hai chủ đề trước đã cho ta hai cách thu hẹp tổ hợp tuyến tính $\theta_1 x_1 + \cdots + \theta_k x_k$. Đòi tổng các hệ số bằng 1, ta được tổ hợp affine và tập affine. Đòi thêm các hệ số không âm, ta được tổ hợp lồi và tập lồi. Còn một khả năng nữa mà ta chưa xét: Giữ điều kiện **không âm** nhưng **bỏ** điều kiện tổng bằng 1. Trang này cho thấy lựa chọn đó dẫn tới khái niệm **nón**, một đối tượng hình học trông khiêm tốn nhưng lại là nền móng của toàn bộ lý thuyết bất đẳng thức tổng quát và đối ngẫu ở các chủ đề sau.

## 1. Nón: Tập khép kín với phép phóng to

> **Định nghĩa.** Tập $C$ được gọi là **nón**, hay thuần nhất không âm, nếu với mọi $x \in C$ và mọi $\theta \ge 0$, ta có $\theta x \in C$.

Nói bằng hình học, cứ có một điểm $x$ thuộc nón thì cả tia xuất phát từ gốc tọa độ đi qua $x$ cũng thuộc nón. Một nón khác rỗng luôn chứa gốc tọa độ, vì có thể chọn $\theta = 0$. Hình ảnh quen thuộc nhất là chùm sáng phát ra từ một ngọn đèn đặt tại gốc: Mỗi tia sáng là một tia của nón, và vùng được chiếu sáng là toàn bộ nón.

Định nghĩa nón không đòi hỏi tính lồi, và trong thực tế tồn tại nhiều nón không lồi. Hợp của hai trục tọa độ trong $\mathbb{R}^2$ là một nón, vì phóng to một điểm trên trục vẫn được một điểm trên trục, nhưng nó không lồi. Vì vậy ta cần một tên riêng cho những nón vừa là nón vừa lồi.

> **Định nghĩa.** Tập $C$ là **nón lồi** nếu nó vừa lồi vừa là nón. Điều này tương đương với: Với mọi $x_1, x_2 \in C$ và mọi $\theta_1, \theta_2 \ge 0$, ta có $\theta_1 x_1 + \theta_2 x_2 \in C$.

Hãy tự kiểm tra sự tương đương. Nếu $C$ khép kín với mọi tổ hợp $\theta_1 x_1 + \theta_2 x_2$ có hệ số không âm, thì chọn $\theta_2 = 0$ cho tính chất nón, còn chọn $\theta_1 + \theta_2 = 1$ cho tính lồi. Ngược lại, nếu $C$ là nón lồi và $\theta_1 + \theta_2 > 0$, ta viết

$$
\theta_1 x_1 + \theta_2 x_2 = (\theta_1 + \theta_2) \left( \frac{\theta_1}{\theta_1 + \theta_2} x_1 + \frac{\theta_2}{\theta_1 + \theta_2} x_2 \right).
$$

Phần trong ngoặc là một tổ hợp lồi nên thuộc $C$, rồi nhân với số không âm $\theta_1 + \theta_2$ vẫn thuộc $C$ vì $C$ là nón. Trường hợp $\theta_1 = \theta_2 = 0$ cho gốc tọa độ, cũng thuộc $C$.

Về mặt hình học, hình dạng của các tổ hợp $\theta_1 x_1 + \theta_2 x_2$ là một **hình quạt vô hạn** hay **lát bánh** (pie slice) có đỉnh tại gốc tọa độ, hai cạnh biên đi qua $x_1$ và $x_2$. Mép thứ nhất ứng với $\theta_2 = 0$, mép thứ hai ứng với $\theta_1 = 0$. Khác với đoạn thẳng giới hạn của tổ hợp lồi, hình quạt này kéo dài ra vô hạn, bởi vì không có ràng buộc nào chặn cận trên của các hệ số.

<ConeLab type="conic" />

## 2. Tổ hợp nón và bao nón

> **Định nghĩa.** Một điểm có dạng $\theta_1 x_1 + \cdots + \theta_k x_k$ với mọi $\theta_i \ge 0$ được gọi là một **tổ hợp nón** (hay tổ hợp tuyến tính không âm) của $x_1, \ldots, x_k$. **Bao nón** của tập $C$ là tập mọi tổ hợp nón của các điểm thuộc $C$:
> $$\{\theta_1 x_1 + \cdots + \theta_k x_k : x_i \in C,\ \theta_i \ge 0\}.$$

Một tập là nón lồi khi và chỉ khi nó chứa mọi tổ hợp nón của các điểm của nó, và bao nón là nón lồi nhỏ nhất chứa $C$. Các lập luận giống hệt trường hợp tập lồi và tập affine, chỉ thay điều kiện trên hệ số. Về mặt trực quan: Trong mặt phẳng, bao nón của một tập điểm là hình quạt nhỏ nhất có đỉnh ở gốc tọa độ chứa trọn tập đó, hoặc mở rộng thành toàn bộ mặt phẳng nếu tập điểm bao quanh gốc tọa độ.

Mô phỏng ở trên có một ô để thêm vector thứ ba. Khi ba vector được đặt sao cho gốc tọa độ nằm bên trong tam giác tạo bởi ba đầu mút, bao nón của chúng là **toàn bộ mặt phẳng**. Chẳng hạn với $v_1 = (1, 0)$, $v_2 = (-1, 1)$ và $v_3 = (-1, -1)$, vector bất kỳ $(a, b)$ viết được thành tổ hợp nón của ba vector này. Hiện tượng ấy không có ở tổ hợp lồi: Bao lồi của ba điểm chỉ là một tam giác.

## 3. Bốn loại tổ hợp đặt cạnh nhau

Đến đây ta có đủ bốn cách hạn chế hệ số trong tổ hợp $\theta_1 x_1 + \cdots + \theta_k x_k$. Đặt chúng cạnh nhau giúp nhìn thấy cấu trúc chung của chương:

| Loại tổ hợp | Điều kiện trên $\theta$ | Bao của hai điểm $x_1, x_2$ (độc lập tuyến tính) | Loại tập khép kín với tổ hợp đó |
| --- | --- | --- | --- |
| Tuyến tính | Không có | Mặt phẳng qua gốc chứa $x_1, x_2$ | Không gian con |
| Affine | $\sum_i \theta_i = 1$ | Đường thẳng qua $x_1, x_2$ | Tập affine |
| Nón | $\theta_i \ge 0$ | Lát bánh đỉnh ở gốc, mép qua $x_1, x_2$ | Nón lồi |
| Lồi | $\sum_i \theta_i = 1$ và $\theta_i \ge 0$ | Đoạn thẳng $[x_1, x_2]$ | Tập lồi |

Mỗi dòng dưới chứa nhiều ràng buộc hơn dòng trên, ngoại trừ hai dòng giữa không so sánh được với nhau. Từ bảng này đọc ra các quan hệ bao hàm giữa các loại tập: Mọi không gian con vừa là tập affine vừa là nón lồi, mọi tập affine là tập lồi, mọi nón lồi là tập lồi. Chiều ngược lại đều sai: Một đoạn thẳng là tập lồi nhưng không affine và không là nón, một tia xuất phát từ gốc là nón lồi nhưng không affine.

Trước mỗi lập luận trong chương, chỉ cần tự hỏi hai câu: Các hệ số có được âm không, và tổng của chúng có bắt buộc bằng 1 không. Hai câu trả lời đó xác định chính xác cấu trúc hình học tương ứng trong bảng.

## 4. Những tập cơ bản: Affine, lồi hay nón?

Ta rà soát lại một số tập hình học kinh điển dựa trên bảng phân loại ở mục 3:

- Tập rỗng, một điểm $\{x_0\}$ và toàn không gian $\mathbb{R}^n$ là tập affine, do đó lồi.
- Mọi đường thẳng đều là tập affine. Nếu nó đi qua gốc thì nó là không gian con, do đó cũng là nón lồi.
- Một đoạn thẳng là lồi nhưng không affine, trừ khi nó suy biến thành một điểm.
- Một **tia** $\{x_0 + \theta v : \theta \ge 0\}$ với $v \ne 0$ là lồi nhưng không affine. Nó là nón lồi khi gốc của tia là $x_0 = 0$.
- Mọi không gian con đều là tập affine và nón lồi.

Thêm vài ví dụ sẽ gặp lại nhiều lần. **Góc phần tư không âm** $\mathbb{R}^n_+ = \{x : x_i \ge 0 \text{ với mọi } i\}$ là một nón lồi: Cộng hai vector không âm hay nhân với số không âm đều cho vector không âm. Nửa không gian $\{x : a^T x \le 0\}$, có biên đi qua gốc, là nón lồi. Nửa không gian $\{x : a^T x \le 1\}$ thì lồi nhưng không là nón, vì phóng to một điểm có $a^T x = 1$ lên gấp đôi sẽ ra khỏi tập. Ở những chủ đề tiếp theo, ta sẽ gặp hai nón lồi quan trọng bậc nhất trong tối ưu: Nón bậc hai $\{(x, t) : \|x\|_2 \le t\}$ và nón các ma trận nửa xác định dương.

## 5. Một vector có thuộc một nón không?

Cho các vector $a_1, \ldots, a_k \in \mathbb{R}^m$ và một vector $b$. Câu hỏi "$b$ có thuộc bao nón của $a_1, \ldots, a_k$ không?" có thể viết lại thành: Có tồn tại $\theta \in \mathbb{R}^k$ với

$$
\theta \succeq 0, \qquad A\theta = b
$$

hay không, trong đó $A$ là ma trận có các cột $a_1, \ldots, a_k$ và $\theta \succeq 0$ nghĩa là mọi thành phần không âm. Câu hỏi này là một **bài toán khả thi** của quy hoạch tuyến tính, như đã định nghĩa ở chủ đề về bài toán tối ưu. Như vậy câu hỏi hình học "điểm có nằm trong lát bánh không" và câu hỏi đại số "hệ phương trình có nghiệm không âm không" là một.

Câu hỏi ngược lại còn thú vị hơn: Nếu $b$ **không** thuộc nón, làm sao chứng minh điều đó một cách gọn gàng, thay vì nói "tôi đã thử mà không tìm được $\theta$"? Câu trả lời là một siêu phẳng tách $b$ khỏi nón, và đó là nội dung của một định lý nổi tiếng gọi là bổ đề Farkas. Ta sẽ gặp nó dưới dạng các định lý lựa chọn ở chủ đề về siêu phẳng phân tách.

::: example Kiểm tra bằng tay trong mặt phẳng
Cho $a_1 = (2, 1)$ và $a_2 = (1, 3)$. Vector $b = (4, 7)$ có thuộc bao nón của chúng không? Giải $\theta_1 (2, 1) + \theta_2 (1, 3) = (4, 7)$, tức $2\theta_1 + \theta_2 = 4$ và $\theta_1 + 3\theta_2 = 7$. Nhân phương trình thứ hai với 2 rồi trừ phương trình thứ nhất được $5\theta_2 = 10$, nên $\theta_2 = 2$ và $\theta_1 = 1$. Cả hai không âm, vậy $b$ thuộc nón. Với $b' = (4, -1)$, cùng cách giải cho $\theta_2 = -\tfrac65 < 0$. Vì $a_1, a_2$ độc lập tuyến tính, cách biểu diễn là duy nhất, nên $b'$ không thuộc nón.
:::

## 6. Nón trong học máy

Tổ hợp nón xuất hiện mỗi khi một đại lượng được ghép từ các "thành phần" chỉ có thể cộng thêm chứ không thể trừ đi. Vài ví dụ:

- Trong **phân rã ma trận không âm** (nonnegative matrix factorization), mỗi điểm dữ liệu, chẳng hạn một ảnh khuôn mặt với độ sáng điểm ảnh không âm, được xấp xỉ bằng một tổ hợp nón của một số "thành phần cơ sở". Vì không được trừ, các thành phần thường có dạng những bộ phận cục bộ, chẳng hạn mắt hay mũi. Tập các ảnh biểu diễn được chính là bao nón của các thành phần.
- Đầu ra của hàm kích hoạt ReLU, $\max\{0, z\}$, luôn thuộc góc phần tư không âm. Một tầng tuyến tính có trọng số không âm áp lên đầu ra đó cho ra các tổ hợp nón.
- Một bộ phân loại tuyến tính không có hệ số chặn, gán nhãn dương khi $w^T x \ge 0$, có vùng nhãn dương là một nửa không gian qua gốc, tức một nón lồi. Hệ quả là nếu $x$ được gán nhãn dương thì mọi bội dương $2x, 3x, \ldots$ cũng vậy. Thêm hệ số chặn $b$ thì vùng nhãn dương trở thành nửa không gian không qua gốc, và tính chất nón mất đi.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Một nón có nhất thiết phải chứa gốc tọa độ không? Tập $\{x \in \mathbb{R}^2 : x_1 > 0,\ x_2 > 0\}$ có phải là một nón theo định nghĩa chuẩn tắc không?

<details><summary>Xem lời giải thích</summary>

Theo định nghĩa chuẩn với $\theta \ge 0$, một nón khác rỗng luôn phải chứa gốc tọa độ $0 \cdot x = 0$. Tập $\{x_1 > 0, x_2 > 0\}$ không chứa gốc, nên với định nghĩa này nó không phải là một nón: Lấy $x = (1, 1)$ và $\theta = 0$ thì $\theta x = (0, 0)$ nằm ngoài tập. Cần lưu ý rằng một số tài liệu giải tích khác định nghĩa nón với điều kiện mở $\theta > 0$, khi đó tập này lại được coi là nón. Trong toàn bộ chương trình môn học này, ta tuân thủ quy ước chuẩn tắc $\theta \ge 0$.

</details>

**Câu 2.** Giao của hai nón lồi có là nón lồi không? Tổng $K_1 + K_2 = \{x + y : x \in K_1, y \in K_2\}$ thì sao?

<details><summary>Xem lời giải thích</summary>

Cả hai đều là nón lồi. Với giao: Một tổ hợp nón của hai điểm thuộc cả $K_1$ và $K_2$ thuộc từng nón, nên thuộc giao. Với tổng: Nếu $u = x + y$ và $u' = x' + y'$ với $x, x' \in K_1$, $y, y' \in K_2$, thì $\theta u + \theta' u' = (\theta x + \theta' x') + (\theta y + \theta' y')$, mỗi ngoặc thuộc nón tương ứng. Trong mặt phẳng, tổng của hai lát bánh là lát bánh nhỏ nhất chứa cả hai, và nó có thể là cả mặt phẳng nếu hai lát bánh "mở" về hai phía ngược nhau.

</details>

**Câu 3.** Bao nón của một đường tròn không đi qua gốc, chẳng hạn đường tròn tâm $(3, 0)$ bán kính 1, là gì? Bao nón của đường tròn tâm $(0, 0)$ bán kính 1 thì sao?

<details><summary>Xem lời giải thích</summary>

Với đường tròn tâm $(3, 0)$ bán kính 1, các tia từ gốc chạm đường tròn tạo thành một lát bánh giới hạn bởi hai tiếp tuyến kẻ từ gốc. Góc giữa mỗi tiếp tuyến và trục hoành là $\arcsin\tfrac13 \approx 19.5°$, nên bao nón là lát bánh đối xứng qua trục hoành với góc mở khoảng $39°$. Với đường tròn tâm gốc, mọi hướng đều có điểm trên đường tròn, nên bao nón là cả mặt phẳng. Câu hỏi này cho thấy bao nón chỉ "nhìn thấy" các hướng chứ không nhìn thấy khoảng cách tới gốc.

</details>

**Câu 4.** Đúng hay sai: "Nếu $K$ là nón lồi và $K$ chứa một đường thẳng qua gốc, thì $K$ là một không gian con."

<details><summary>Xem lời giải thích</summary>

Sai. Nửa mặt phẳng đóng $\{x \in \mathbb{R}^2 : x_2 \ge 0\}$ là nón lồi và chứa trục hoành, một đường thẳng qua gốc, nhưng không phải không gian con vì nó không chứa $(0, -1)$. Những nón không chứa đường thẳng nào được gọi là nón **nhọn**, và đó là một trong bốn điều kiện của nón chính quy ở chủ đề về bất đẳng thức tổng quát. Nửa mặt phẳng là ví dụ điển hình của một nón lồi không nhọn.

</details>

## 8. Bài tập tự luyện

::: exercise 1. Nón hay không
Tập nào sau đây là nón, tập nào là nón lồi: (a) $\{x \in \mathbb{R}^2 : x_1 \ge |x_2|\}$, (b) $\{x \in \mathbb{R}^2 : x_1 x_2 \ge 0\}$, (c) $\{x \in \mathbb{R}^2 : x_1 + x_2 \le 1\}$, (d) $\{x \in \mathbb{R}^3 : x_1^2 + x_2^2 \le x_3^2,\ x_3 \ge 0\}$.
:::

::: solution
(a) Nón lồi. Nếu $x_1 \ge |x_2|$ và $\theta \ge 0$ thì $\theta x_1 \ge |\theta x_2|$, nên đây là nón. Tập là giao của hai nửa mặt phẳng $x_1 - x_2 \ge 0$ và $x_1 + x_2 \ge 0$ qua gốc, nên lồi. (b) Nón nhưng không lồi: Tập hợp này là hợp của góc phần tư thứ nhất và thứ ba. Hai điểm $(1, 0)$ và $(0, -1)$ thuộc tập, nhưng trung điểm $(\tfrac12, -\tfrac12)$ có tích hai tọa độ âm. (c) Không phải nón: Điểm $(1, 0)$ thuộc tập nhưng $2 \cdot (1, 0) = (2, 0)$ thì không. Tập này lồi vì là nửa mặt phẳng. (d) Nón lồi. Điều kiện tương đương $\sqrt{x_1^2 + x_2^2} \le x_3$, tức $\|(x_1, x_2)\|_2 \le x_3$, chính là nón bậc hai mà chủ đề về chuẩn sẽ chứng minh là lồi. Nếu bỏ điều kiện $x_3 \ge 0$ thì tập gồm cả nón ngược phía dưới, vẫn là nón nhưng không còn lồi.
:::

::: exercise 2. Biểu diễn trong một nón
Cho $a_1 = (1, 0, 1)$, $a_2 = (0, 1, 1)$, $a_3 = (1, 1, 0)$. Vector $b = (3, 1, 2)$ có thuộc bao nón của ba vector này không? Còn $b' = (2, 0, 0)$ thì sao?
:::

::: solution
Giải $\theta_1 a_1 + \theta_2 a_2 + \theta_3 a_3 = b$: Ba phương trình $\theta_1 + \theta_3 = 3$, $\theta_2 + \theta_3 = 1$, $\theta_1 + \theta_2 = 2$. Cộng cả ba được $2(\theta_1 + \theta_2 + \theta_3) = 6$, nên tổng bằng 3. Suy ra $\theta_2 = 0$, $\theta_1 = 2$, $\theta_3 = 1$, đều không âm, nên $b$ thuộc nón. Với $b' = (2, 0, 0)$: Tổng các $\theta$ bằng 1, cho $\theta_2 = 1 - 2 = -1$, $\theta_1 = 1$, $\theta_3 = 1$. Ba vector độc lập tuyến tính nên nghiệm duy nhất, và $\theta_2 < 0$, vì vậy $b'$ không thuộc nón.
:::

## Tóm tắt

Nón là tập khép kín với phép nhân với số không âm, và nón lồi là nón đồng thời lồi, tương đương với việc khép kín đối với tổ hợp có hệ số không âm. Bao nón là nón lồi nhỏ nhất chứa một tập, và trong mặt phẳng nó là một lát bánh đỉnh ở gốc, một nửa mặt phẳng, một đường thẳng hoặc cả mặt phẳng. Bốn loại tổ hợp tuyến tính, affine, nón và lồi khác nhau đúng ở hai câu hỏi: Hệ số có được âm không, và tổng có bắt buộc bằng 1 không.

Kiểm tra một vector có thuộc bao nón của các vector cho trước là một bài toán khả thi của quy hoạch tuyến tính. Chứng minh nó không thuộc nón dẫn tới siêu phẳng phân tách và các định lý lựa chọn, sẽ gặp ở những chủ đề sau.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
- D. D. Lee, H. S. Seung, *Learning the parts of objects by non-negative matrix factorization*, Nature 401 (1999), 788–791.
