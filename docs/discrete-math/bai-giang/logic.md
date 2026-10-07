---
course: discrete-math
lecture: logic
section: lecture
title: "Logic mệnh đề & vị từ"
prerequisites: ["menh-de","luong-tu"]
lessonStatus: ready
---


Logic toán học là nền tảng giúp máy tính "suy nghĩ" thông qua các giá trị đúng/sai ($1$ và $0$) và các cổng logic trong vi xử lý.

---

## 1. Các Phép Toán Mệnh Đề Cơ Bản

Cho hai mệnh đề $p$ và $q$:

| $p$ | $q$ | Phủ định $\neg p$ | Hội $p \land q$ (AND) | Tuyển $p \lor q$ (OR) | Kéo theo $p \rightarrow q$ | Tương đương $p \leftrightarrow q$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1 | 0 | 1 | 1 | **1** | 1 |
| 1 | 0 | 0 | 0 | 1 | **0** | 0 |
| 0 | 1 | 1 | 0 | 1 | **1** | 0 |
| 0 | 0 | 1 | 0 | 0 | **1** | 1 |

::: tip Lưu ý Vàng về Phép Kéo Theo $p \rightarrow q$
Phép kéo theo $p \rightarrow q$ chỉ **SAI** duy nhất trong trường hợp: **Tiền đề ĐÚNG mà Kết luận SAI** ($1 \rightarrow 0 = 0$).  
Nếu tiền đề $p$ đã SAI ($0$), thì dù $q$ là gì, mệnh đề $p \rightarrow q$ vẫn luôn **ĐÚNG**!
:::

---

## 2. Luật De Morgan (Rất hay dùng để Rút gọn Biểu thức)

$$\neg (p \land q) \equiv \neg p \lor \neg q$$
$$\neg (p \lor q) \equiv \neg p \land \neg q$$

*Quy tắc nhớ:* Phủ định của một tích là tổng các phủ định; Phủ định của một tổng là tích các phủ định.
