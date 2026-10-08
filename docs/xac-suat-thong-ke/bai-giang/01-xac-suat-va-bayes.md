---
course: xac-suat-thong-ke
lecture: 01-xac-suat-va-bayes
section: lecture
title: "Xác suất có điều kiện & Bayes"
prerequisites: ["tap-hop","khong-gian-mau","xac-suat-co-dieu-kien","doc-lap"]
lessonStatus: ready
---


Mục tiêu: phân biệt xác suất trước và sau khi có thông tin, biết chọn mẫu số và tránh đảo nhầm hai xác suất có điều kiện.

## 1. Xác định miền xét trước khi tính

Không gian mẫu chứa toàn bộ kết quả có thể. Biến cố là tập con của không gian mẫu. Với hai biến cố $A,B$:

$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$

Phần giao bị đếm hai lần nên cần trừ một lần. Chỉ dùng $P(A\cup B)=P(A)+P(B)$ khi hai biến cố loại trừ nhau.

## 2. Khi biết B, mẫu số phải là B

Xác suất có điều kiện:

$$P(A\mid B)=\frac{P(A\cap B)}{P(B)},\quad P(B)>0.$$

Hãy hiểu như việc giữ lại những trường hợp thuộc B rồi hỏi bao nhiêu trong số đó thuộc A. Nếu 100 sinh viên có 40 người giải đúng câu hỏi, và 16 trong số 40 người ấy thuộc nhóm ôn tập, thì xác suất thuộc nhóm ôn tập khi biết đã giải đúng là $\frac{16}{40}=0.4$.

Độc lập nghĩa là biết B không làm thay đổi xác suất của A. Khi độc lập, $P(A\cap B)=P(A)P(B)$. Đừng đồng nhất độc lập với loại trừ nhau.

## 3. Bayes đảo chiều điều kiện

Từ $P(A\cap B)=P(B\mid A)P(A)=P(A\mid B)P(B)$, suy ra:

$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}.$$

Nếu A và không A chia hết không gian mẫu thì:

$$P(B)=P(B\mid A)P(A)+P(B\mid \neg A)P(\neg A).$$

Các tên thường gặp: **prior** là $P(A)$, **likelihood** là $P(B\mid A)$, **posterior** là $P(A\mid B)$. Posterior vẫn là xác suất, không phải kết luận chắc chắn.

## 4. Ví dụ dùng số lượng thay công thức

Giả sử trong 100 sinh viên có 20 người thuộc nhóm ôn tập A. Trong A, 80% giải đúng B, còn ngoài A thì tỷ lệ giải đúng là 30%.

| Nhóm | Số người | Giải đúng |
|---|---:|---:|
| Thuộc A | 20 | 16 |
| Không thuộc A | 80 | 24 |
| Tổng | 100 | 40 |

Do đó $P(A\mid B)=\frac{16}{40}=40\%$, dù $P(B\mid A)=80\%$. Hai mẫu số khác nhau: một bên xét người giải đúng, một bên xét nhóm ôn tập.

## 5. Minh họa tương tác

<CodeIllustration type="bayes" />

## 6. Những lỗi cần tránh

- Đảo $P(A\mid B)$ thành $P(B\mid A)$.
- Bỏ qua tỷ lệ ban đầu $P(A)$.
- Quên những trường hợp B xuất hiện khi A không xảy ra.
- Nhân xác suất các biến cố mà chưa kiểm tra độc lập.

<details><summary>Tự kiểm tra: $P(A)=0.5$, $P(B|A)=0.8$, P(B|không A)=0.2. P(A|B) là gì?</summary>

$P(B)=0.8\times0.5+0.2\times0.5=0.5$, nên $P(A\mid B)=\frac{0.4}{0.5}=0.8$.

</details>

[Tiếp: Biến ngẫu nhiên & phân phối](/xac-suat-thong-ke/bai-giang/02-bien-ngau-nhien.md)
