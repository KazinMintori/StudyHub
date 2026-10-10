---
course: discrete-math
lecture: logic
section: lecture
title: "Logic mệnh đề & vị từ"
prerequisites: ["menh-de","luong-tu"]
lessonStatus: ready
description: "Nền tảng logic toán học, bảng chân trị, phép biến đổi tương đương, lượng từ vị từ và phương pháp suy luận hình thức."
---

Logic toán học là nền tảng giúp máy tính tư duy thông qua các giá trị chân lý đúng và sai ($1$ và $0$), đồng thời là cơ sở thiết kế các cổng logic trong mạch tích hợp vi xử lý.

---

## 1. Các phép toán mệnh đề cơ bản

Cho hai mệnh đề $p$ và $q$:

| $p$ | $q$ | Phủ định $\neg p$ | Hội $p \land q$ (AND) | Tuyển $p \lor q$ (OR) | Kéo theo $p \rightarrow q$ | Tương đương $p \leftrightarrow q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 0 | 1 | 1 | **1** | 1 |
| 1 | 0 | 0 | 0 | 1 | **0** | 0 |
| 0 | 1 | 1 | 0 | 1 | **1** | 0 |
| 0 | 0 | 1 | 0 | 0 | **1** | 1 |

::: tip Lưu ý về phép kéo theo $p \rightarrow q$
Phép kéo theo $p \rightarrow q$ chỉ **SAI** duy nhất trong trường hợp: **Tiền đề ĐÚNG mà Kết luận SAI** ($1 \rightarrow 0 = 0$).  
Nếu tiền đề $p$ đã SAI ($0$), thì dù $q$ nhận giá trị gì, mệnh đề $p \rightarrow q$ vẫn luôn **ĐÚNG** (chân lý rỗng).
:::

---

## 2. Các luật tương đương logic kinh điển

### Luật De Morgan
Luật De Morgan dùng để biến đổi phủ định của hội và tuyển:

$$
\begin{aligned}
\neg (p \land q) &\equiv \neg p \lor \neg q \\
\neg (p \lor q) &\equiv \neg p \land \neg q
\end{aligned}
$$

### Luật kéo theo và phản đảo
Mọi phép kéo theo đều có thể đưa về phép tuyển:

$$
p \rightarrow q \equiv \neg p \lor q
$$

Mệnh đề phản đảo luôn tương đương logic với mệnh đề gốc:

$$
p \rightarrow q \equiv \neg q \rightarrow \neg p
$$

### Phủ định của lượng từ vị từ
Khi đưa phép phủ định qua lượng từ, ta hoán đổi giữa lượng từ với mọi ($\forall$) và tồn tại ($\exists$):

$$
\begin{aligned}
\neg \forall x P(x) &\equiv \exists x \neg P(x) \\
\neg \exists x P(x) &\equiv \forall x \neg P(x)
\end{aligned}
$$

---

## 3. Hệ thống bài tập tự luyện {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu luyện tập.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở các bài tập thực chiến có hướng dẫn chi tiết và kiểm chứng tự động.
:::

