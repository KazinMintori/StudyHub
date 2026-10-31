---
title: "Phân bố tốc độ Maxwell"
wikiTerm: "phan-bo-maxwell"
prev: false
next: false
---

# Phân bố tốc độ Maxwell

Phân bố xác suất tốc độ của các phân tử khí cổ điển ở cân bằng nhiệt trong mô hình lý tưởng.

<WikiUsage />

## Giải thích kỹ thuật

Phân bố Maxwell mô tả tốc độ của các phân tử khí lý tưởng cổ điển ở cân bằng nhiệt. Khối lượng của một phân tử là $m>0$, nhiệt độ tuyệt đối là $T>0$, còn tốc độ $v$ không âm. Trong hệ SI, $m$ đo bằng kg và $T$ đo bằng K. Hằng số Boltzmann $k_B$ có đơn vị J/K. Đặt hai hệ số dùng trong phần này:

$$
b=\frac{m}{2k_BT},
$$

$$
C=\frac{4b^{3/2}}{\sqrt{\pi}}.
$$

Mật độ xác suất tốc độ là:

$$
f(v)=Cv^2e^{-bv^2}.
$$

Nếu tốc độ đo bằng m/s thì $f(v)$ có đơn vị s/m. Đại lượng $f(v)\,dv$ là phần phân tử có tốc độ trong khoảng rất nhỏ từ $v$ đến $v+dv$. Nó không phải xác suất để phân tử có đúng một tốc độ duy nhất. Phân bố được chuẩn hóa bởi:

$$
\int_0^\infty f(v)\,dv=1.
$$

Với tổng số $N$ phân tử, gọi $N_{12}$ là số phân tử có tốc độ từ $v_1$ đến $v_2$, trong đó $0\le v_1<v_2$. Khi đó:

$$
N_{12}=N\int_{v_1}^{v_2}f(v)\,dv.
$$

Tốc độ có xác suất lớn nhất là vị trí đỉnh của mật độ $f(v)$:

$$
v_{\mathrm{mp}}=\sqrt{\frac{2k_BT}{m}}.
$$

Tốc độ trung bình và tốc độ căn quân phương lần lượt là:

$$
\bar v=\sqrt{\frac{8k_BT}{\pi m}},
$$

$$
v_{\mathrm{rms}}=\sqrt{\frac{3k_BT}{m}}.
$$

Ba tốc độ thỏa mãn:

$$
v_{\mathrm{mp}}<\bar v<v_{\mathrm{rms}}.
$$

Chúng đặc trưng cho cả phân bố, không có nghĩa mọi phân tử đều chuyển động với cùng một tốc độ hoặc cùng một động năng.

## Ví dụ

Ở cùng nhiệt độ, các phân tử không cùng tốc độ. Phân tử nhẹ hơn có các tốc độ đặc trưng lớn hơn.

## Khi nào cần dùng?

Phân biệt tốc độ trung bình, tốc độ hiệu dụng và tốc độ có xác suất lớn nhất.

## Câu hỏi ôn lại

Tốc độ hiệu dụng có bằng tốc độ trung bình không?

<details><summary>Xem đáp án</summary>

Không. Trung bình bình phương rồi lấy căn và lấy trung bình trực tiếp là hai phép toán khác nhau.

</details>

## Thuật ngữ liên quan

- [Nguyên lý phân bố đều năng lượng](./nguyen-ly-phan-bo-deu-nang-luong.md)
- [Khí lý tưởng](./khi-ly-tuong.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 9–11 và 17–20.
