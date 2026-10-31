---
title: "Mô hình giọt chất lỏng"
wikiTerm: "mo-hinh-giot-chat-long"
prev: false
next: false
---

# Mô hình giọt chất lỏng

Mô hình hạt nhân có mật độ gần như không đổi, mô tả năng lượng liên kết bằng các đóng góp thể tích, bề mặt, Coulomb, bất đối xứng và ghép đôi.

<WikiUsage />

## Giải thích kỹ thuật

Mô hình giọt chất lỏng dựa trên mật độ hạt nhân gần như không đổi và tính bão hòa của lực hạt nhân. Trong gần đúng đang xét, tương tác hạt nhân gần độc lập với điện tích và có tầm tác dụng cỡ 10⁻¹⁵ m. Mỗi nucleon chủ yếu tương tác mạnh với một số ít láng giềng gần.

Nucleon trong lòng hạt nhân có nhiều láng giềng hơn nucleon ở bề mặt. Đóng góp thể tích làm tăng liên kết, còn hiệu ứng bề mặt và lực đẩy điện giữa các proton làm giảm liên kết. Hai đóng góp khác mô tả sự chênh lệch số proton với số neutron và sự ghép đôi các nucleon cùng loại.

Gọi A = Z+N. Năm đóng góp đã mang dấu được viết như sau:

$$
\begin{aligned}
&E_V=C_1A,\\
&E_S=-C_2A^{2/3},\\
&E_C=-C_3\frac{Z(Z-1)}{A^{1/3}},\\
&E_A=-C_4\frac{(A-2Z)^2}{A}.
\end{aligned}
$$

Số hạng ghép đôi được xác định bởi:

$$
E_P=\begin{cases}
+C_5A^{-4/3},&Z,N\ \text{chẵn},\\
-C_5A^{-4/3},&Z,N\ \text{lẻ},\\
0,&A\ \text{lẻ}.
\end{cases}
$$

Tổng năng lượng liên kết ước tính là tổng tường minh của năm đóng góp. Để giữ công thức gọn, đặt:

$$
\begin{aligned}
&G_1=E_V+E_S,\\
&G_2=E_C+E_A+E_P,\\
&E_B\approx G_1+G_2.
\end{aligned}
$$

Bộ hệ số dùng ở đây có đơn vị MeV:

$$
\begin{aligned}
&C_1=15{,}75,\\
&C_2=17{,}80,\\
&C_3=0{,}7100,\\
&C_4=23{,}69,\\
&C_5=39.
\end{aligned}
$$

Các hệ số được xác định bằng thực nghiệm. Phải dùng đồng bộ hệ số và số mũ của cùng một bộ tham số.

Khối lượng nguyên tử trung hòa có thể được ước lượng từ năng lượng liên kết mô hình. Với $M_H$ là khối lượng nguyên tử hydro trung hòa, mₙ là khối lượng neutron và F là tổng khối lượng tham chiếu chứa Z electron:

$$
\begin{aligned}
&F=ZM_H+Nm_n,\\
&M_{\rm est}\approx F-\frac{E_B}{c^2}.
\end{aligned}
$$

Đây là công thức khối lượng bán thực nghiệm trong gần đúng bỏ qua chênh lệch liên kết electron. Mô hình giải thích xu hướng tổng quát của khối lượng và năng lượng liên kết, còn cấu trúc spin và các mức kích thích cần mô hình vỏ để khảo sát chi tiết.

## Ví dụ

Nucleon ở bề mặt có ít láng giềng hơn trong lòng hạt nhân, làm giảm năng lượng liên kết so với đóng góp thể tích thuần túy.

## Khi nào cần dùng?

Ước lượng khối lượng, năng lượng liên kết và xu hướng phân hạch.

## Câu hỏi ôn lại

Số hạng Coulomb mang dấu âm trong năng lượng liên kết có nghĩa lực điện là lực hút không?

<details><summary>Xem đáp án</summary>

Không. Lực đẩy giữa các proton làm hạt nhân liên kết kém hơn, nên làm giảm năng lượng liên kết dương cần để tách hệ.

</details>

## Thuật ngữ liên quan

- [Bán kính hạt nhân](./ban-kinh-hat-nhan.md)
- [Năng lượng liên kết hạt nhân](./nang-luong-lien-ket-hat-nhan.md)
- [Mô hình vỏ hạt nhân](./mo-hinh-vo-hat-nhan.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 43, trang 1442–1474.
