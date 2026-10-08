---
course: vat-ly-2
lecture: 03-dinh-luat-gauss
section: lecture
title: "Thông lượng & định luật Gauss"
prerequisites: ["tich-vo-huong","thong-luong","tich-phan","dien-tich"]
lessonStatus: ready
---


## 1. Đếm phần trường đi qua mặt

Thông lượng điện trường qua một mặt S là $\Phi_E=\int_S\mathbf E\cdot d\mathbf A$. Vector diện tích có hướng pháp tuyến của mặt. Với trường đều qua mặt phẳng diện tích A:

$$\Phi_E=EA\cos\theta.$$

Góc $\theta$ là giữa điện trường và pháp tuyến. Trường song song mặt thì thông lượng bằng 0, chứ không phải lớn nhất.

## 2. Mặt kín và điện tích bên trong

Trong chân không, định luật Gauss:

$$\oint_S\mathbf E\cdot d\mathbf A=\frac{Q_{\text{bên trong}}}{\varepsilon_0}.$$

Mặt kín dùng pháp tuyến hướng ra ngoài. $Q_{\text{bên trong}}$ là tổng đại số điện tích nằm trong mặt. Điện tích ngoài mặt có thể tạo trường tại các điểm trên mặt nhưng đóng góp thông lượng tổng qua mặt kín bằng 0.

## 3. Tại sao cần đối xứng?

Gauss luôn liên hệ thông lượng với điện tích, nhưng không tự cho E ở mọi điểm. Muốn kéo E ra ngoài tích phân, cần biết trường có độ lớn không đổi trên phần mặt phù hợp và biết góc với pháp tuyến. Các đối xứng cầu, trụ, phẳng là những trường hợp thường dùng.

Với điện tích điểm Q ở tâm mặt cầu bán kính r, E hướng xuyên tâm và có cùng độ lớn trên mặt:

$$E\,4\pi r^2=\frac{Q}{\varepsilon_0},\qquad E=\frac{Q}{4\pi\varepsilon_0r^2}.$$

Ở đây E là thành phần xuyên tâm có dấu. Với Q âm, vector trường hướng vào tâm. Công thức phù hợp với kết quả Coulomb.

## 4. Ví dụ và kiểm tra bẫy

Nguồn điểm $Q=+1\,\mu C$ đặt ở tâm. Tại $r=0.2 m$, độ lớn trường xấp xỉ $9\times10^9\times10^{-6}/0.2^2=2.25\times10^5\ \mathrm{N/C}$, hướng ra ngoài.

Nếu tổng điện tích bên trong một mặt kín bằng 0, chỉ kết luận **thông lượng tổng bằng 0**. Không kết luận E bằng 0 tại từng điểm: một điện trường đều không bằng 0 qua một hộp kín vẫn có tổng thông lượng bằng 0 vì các mặt có đóng góp bù nhau.

<details><summary>Tự kiểm tra: điện tích ngoài mặt kín có bắt buộc tạo $E=0$ trên mặt không?</summary>

Không. Nó có thể tạo E khác 0 trên mặt, nhưng thông lượng tổng do nó qua toàn mặt kín bằng 0.

</details>
