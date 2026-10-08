---
course: vat-ly-2
lecture: 01-dien-truong-coulomb
section: lecture
title: "Điện trường & định luật Coulomb"
prerequisites: ["vector","chuan","dien-tich","luc","don-vi"]
lessonStatus: ready
---


## 1. Phân biệt nguồn trường với điện tích thử

Điện tích nguồn Q tạo điện trường quanh nó. Điện tích thử q đặt tại một điểm chịu lực $\mathbf F=q\mathbf E$. Định nghĩa điện trường dùng điện tích thử dương đủ nhỏ để không làm thay đổi phân bố nguồn trong mô hình xét.

Nếu q âm, lực ngược hướng điện trường. Thay điện tích thử không làm đổi điện trường vốn do nguồn tạo ra.

## 2. Điện trường của điện tích điểm

Trong chân không, mô hình tĩnh điện của nguồn điểm Q:

$$\mathbf E(\mathbf r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\hat{\mathbf r},\qquad r>0.$$

$\hat{\mathbf r}$ là vector đơn vị hướng từ nguồn tới điểm đang xét. Với Q dương, trường hướng ra. Q âm, trường hướng vào. Hằng số $k=1/(4\pi\varepsilon_0)\approx9\times10^9\ \mathrm{N\,m^2/C^2}$.

Định luật Coulomb cho độ lớn lực giữa hai điện tích điểm: $F=k|Qq|/r^2$. Công thức không dùng tại $r=0$ và không thay một phân bố mở rộng bằng nguồn điểm khi điều kiện mô hình chưa phù hợp.

## 3. Ví dụ có dấu và đơn vị

Nguồn $Q=+2\,\mu C$, điểm xét cách nguồn $r=0.3\,m$:

$$E=\frac{9\times10^9\times2\times10^{-6}}{0.3^2}=2\times10^5\ \mathrm{N/C}.$$

Hướng điện trường ra xa nguồn. Đặt $q=-1\,\mu C$ tại đó: lực có độ lớn 0.2 N và hướng về nguồn. Dấu âm của q đảo chiều vector lực, không biến độ lớn lực thành một số âm.

## 4. Nguyên lý chồng chất

Với $n$ nguồn, gọi $\mathbf E_i$ là vector điện trường do nguồn thứ $i$ gây ra tại **cùng điểm đang xét**. Cộng từng vector:

$$
\mathbf E_{\text{tổng}}
=\mathbf E_1+\cdots+\mathbf E_n
=\sum_{i=1}^n\mathbf E_i.
$$

Chỉ số $i$ chọn nguồn điện tích. Với hai nguồn, $\mathbf E_{\text{tổng}}=\mathbf E_1+\mathbf E_2$. Phải cộng các thành phần theo cùng hệ trục, không cộng độ lớn khi hai hướng khác nhau.

Hai trường bằng độ lớn có thể triệt tiêu nếu ngược chiều hoặc tăng gấp đôi nếu cùng chiều. Hãy vẽ hướng trước khi cộng số.

<CodeIllustration type="field" />

## 5. Kiểm tra lời giải

1. Đổi microcoulomb thành coulomb và khoảng cách thành mét.
2. Xác định hướng từ dấu nguồn.
3. Tính thành phần vector rồi cộng.
4. Nếu cần lực, nhân điện trường với điện tích thử có dấu.

<details><summary>Tự kiểm tra: khoảng cách tới một nguồn điểm tăng gấp đôi thì độ lớn điện trường thay đổi thế nào?</summary>

Giảm 4 lần vì E tỷ lệ nghịch với bình phương khoảng cách.

</details>

[Tiếp: Điện thế, công & gradient](/vat-ly-2/bai-giang/02-dien-the.md)
