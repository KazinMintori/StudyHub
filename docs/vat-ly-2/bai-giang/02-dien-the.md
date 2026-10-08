---
course: vat-ly-2
lecture: 02-dien-the
section: lecture
title: "Điện thế, công & gradient"
prerequisites: ["cong-nang-luong","dien-the","dao-ham","gradient","tich-phan"]
lessonStatus: ready
---


## 1. Điện thế là năng lượng trên một đơn vị điện tích

Trong tĩnh điện, thế năng U của điện tích thử q liên hệ với điện thế bằng $U=qV$ theo mốc đã chọn. Hiệu điện thế từ A đến B:

$$V_B-V_A=-\int_A^B\mathbf E\cdot d\mathbf l.$$

Với một điện tích q, $\Delta U=q\Delta V$ và công của lực điện $W=-\Delta U$. Hiệu điện thế có đơn vị volt, tương đương $J/C$.

## 2. Vì sao điện trường có dấu trừ?

Gradient của điện thế chỉ hướng V tăng nhanh nhất. Điện trường đi theo hướng V giảm nhanh nhất:

$$\mathbf E=-\nabla V.$$

Theo một trục: $E_x=-dV/dx$. Với nhiều biến: $E_x=-\partial V/\partial x$, tương tự với y và z. Dấu trừ mô tả hướng. Không có nghĩa độ lớn điện trường âm.

## 3. Ví dụ đạo hàm

Cho điện thế dọc trục x là $V(x)=2x^2-3x$ với x đo bằng mét và các hệ số mang đơn vị phù hợp để V tính bằng volt:

$$E_x=-(4x-3).$$

Tại $x=2 m$, $E_x=-5\ \mathrm{V/m}$. Điện trường hướng chiều âm trục x. Một điện tích thử dương chịu lực theo chiều âm. Một điện tích âm chịu lực chiều dương.

## 4. Mặt đẳng thế

Trên mặt đẳng thế, V không đổi. Di chuyển dọc mặt cho $dV=0$ nên $\mathbf E\cdot d\mathbf l=0$. Vì thế điện trường vuông góc mặt đẳng thế ở nơi trường khác 0. Khi điện trường bằng 0, không có hướng trường để nói vuông góc.

Trong lòng vật dẫn ở trạng thái cân bằng tĩnh điện, điện trường bằng 0 và điện thế không đổi trên mỗi phần vật dẫn liên thông. Đây là kết luận về cân bằng tĩnh điện, không áp dụng tùy tiện cho vật dẫn có dòng điện đang chạy.

## 5. Đừng nhầm điện thế với điện trường

| Đại lượng | Loại | Đơn vị | Dùng để |
|---|---|---|---|
| V | Vô hướng | V | Tính thay đổi thế năng |
| E | Vector | $V/m$ hoặc $N/C$ | Tính lực và hướng tương tác |

V có thể bằng 0 tại một điểm theo mốc chọn, nhưng E tại đó chưa chắc bằng 0. E phụ thuộc biến thiên không gian của V, không chỉ giá trị V.

<details><summary>Tự kiểm tra: V không đổi trong một miền thì E trong miền đó là gì?</summary>

$E=0$ vì mọi đạo hàm riêng của V trong miền bằng 0.

</details>

[Tiếp: Thông lượng & Gauss](/vat-ly-2/bai-giang/03-dinh-luat-gauss.md)
