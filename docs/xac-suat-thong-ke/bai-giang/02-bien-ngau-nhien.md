---
course: xac-suat-thong-ke
lecture: 02-bien-ngau-nhien
section: lecture
title: "Biến ngẫu nhiên & phân phối"
prerequisites: ["bien-ngau-nhien","to-hop","tich-phan"]
lessonStatus: ready
---


## 1. Từ kết quả tới con số

Biến ngẫu nhiên $X$ gán một giá trị số cho mỗi kết quả. Ví dụ tung hai đồng xu: các kết quả là NN, NS, SN, SS, còn X đếm số mặt ngửa nên nhận 0, 1 hoặc 2. Phân phối mô tả xác suất của các giá trị đó.

Với hai đồng xu cân bằng độc lập, $P(X=0)=1/4$, $P(X=1)=1/2$, $P(X=2)=1/4$. Các xác suất không âm và tổng bằng 1.

## 2. Rời rạc: dùng hàm khối xác suất

Hàm khối xác suất (PMF) $p(x)=P(X=x)$ gắn xác suất với từng giá trị đếm được.

**Bernoulli:** X bằng 1 khi thành công, 0 khi thất bại. $P(X=1)=p$, $P(X=0)=1-p$.

**Nhị thức:** X đếm số thành công trong n phép thử Bernoulli độc lập có cùng p:

$$P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},\quad k=0,\ldots,n.$$

Ví dụ n=3, p=1/2: xác suất đúng 2 lần thành công là $\binom{3}{2}(1/2)^3=3/8$. Tổ hợp đếm ba vị trí có thể của lần thất bại.

## 3. Liên tục: mật độ không phải xác suất tại một điểm

Với biến liên tục có mật độ f, xác suất trên khoảng là:

$$P(a\le X\le b)=\int_a^b f(x)\,dx.$$

Mật độ không âm và có tích phân trên toàn miền bằng 1. f(x) có thể lớn hơn 1; điều bị giới hạn từ 0 đến 1 là xác suất trên khoảng. Với biến liên tục có mật độ, xác suất tại một điểm riêng lẻ bằng 0.

Ví dụ X phân phối đều trên [0,4]: $f(x)=1/4$ trong khoảng này, nên $P(1\le X\le3)=(3-1)/4=1/2$.

## 4. CDF dùng cho cả hai loại

Hàm phân phối tích lũy $F(x)=P(X\le x)$ không giảm, tiến tới 0 ở phía âm vô hạn và 1 ở phía dương vô hạn. Với mọi biến ngẫu nhiên:

$$P(a<X\le b)=F(b)-F(a).$$

Hãy chú ý dấu bằng ở đầu khoảng đối với biến rời rạc. Với ví dụ hai đồng xu, $F(0)=1/4$, $F(1)=3/4$, $F(2)=1$.

## 5. Cách chọn mô hình

1. Định nghĩa X và đơn vị đo.
2. Xác định giá trị rời rạc hay liên tục.
3. Kiểm tra giả định của phân phối; ví dụ nhị thức cần số phép thử cố định, độc lập và cùng xác suất thành công.
4. Viết rõ biến cố rồi mới tính.

<details><summary>Tự kiểm tra: X đều trên [0,4]. P(X=2) và P(1&lt;X&lt;3) là gì?</summary>

$P(X=2)=0$; $P(1<X<3)=1/2$. Mật độ tại 2 là 1/4 nhưng không phải xác suất tại điểm 2.

</details>

[Tiếp: Kỳ vọng, phương sai & mẫu dữ liệu](/xac-suat-thong-ke/bai-giang/03-ky-vong-phuong-sai.md)
