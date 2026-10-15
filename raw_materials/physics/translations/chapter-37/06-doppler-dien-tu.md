## Tần số đổi thế nào nếu tốc độ ánh sáng không đổi?

Hai người có thể đo cùng tốc độ ánh sáng $c$ nhưng đo tần số khác nhau. Khi tần số đổi, bước sóng cũng đổi để tích $f\lambda$ vẫn bằng $c$ trong chân không. Ta sẽ suy ra hiệu ứng Doppler điện từ từ thời gian phát hai đỉnh sóng liên tiếp.

### 1. Nguồn tiến về người quan sát

Nguồn chuyển động với tốc độ không đổi $u$ về phía Stanley. Trong hệ nghỉ nguồn, tần số là $f_0$ và chu kỳ $T_0=1/f_0$. Gọi $T$ là khoảng thời gian giữa hai lần phát liên tiếp trong hệ Stanley.

![Hình 37.17: Trong thời gian giữa hai lần phát, đỉnh sóng đầu đi cT còn nguồn tiến uT, nên khoảng cách hai đỉnh ở phía trước nguồn là cT trừ uT.](../img/young-37/hinh-37-17.png)

Khoảng $T$ không phải khoảng thời gian hai đỉnh đến Stanley. Hai đỉnh được phát ở hai vị trí khác nhau, nên thời gian truyền của chúng khác nhau. Trong phép đo tần số thu, chính các thời điểm nhận liên tiếp quyết định chu kỳ thu.

Trong thời gian $T$, đỉnh sóng đầu đi $cT$, còn nguồn tiến $uT$. Khoảng cách hai đỉnh là $\lambda=(c-u)T$, nên

$$
f=\frac{c}{(c-u)T}.
\tag{37.24}
$$

Đến đây lập luận giống Doppler âm của nguồn chuyển động. Điểm cần sửa là không được đặt $T=T_0$. Hai lần phát xảy ra cùng vị trí trong hệ nguồn, nên $T_0$ là thời gian riêng và $T=\gamma T_0$.

Vì vậy,

$$
\frac1T=\frac{f_0}{\gamma}.
$$

Thay vào (37.24), rồi dùng $c^2-u^2=(c-u)(c+u)$ để rút gọn, ta có

$$
f=f_0\sqrt{\frac{c+u}{c-u}}.
\tag{37.25}
$$

Nguồn tiến lại gần cho $f>f_0$. Độ dịch tần là $\Delta f=f-f_0$. Nếu $u/c$ rất nhỏ, khai triển đến bậc nhất cho

$$
\frac{\Delta f}{f_0}\approx\frac uc.
$$

Ở cùng bậc gần đúng này, có thể thay mẫu $f_0$ bằng $f$ vì hai tần số chỉ khác nhau một lượng nhỏ. Không dùng gần đúng ấy khi độ dịch tần lớn.

### 2. Nguồn rời xa và radar phản xạ

Nếu nguồn rời xa, đổi dấu $u$ trong biểu thức tiến lại gần:

$$
f=f_0\sqrt{\frac{c-u}{c+u}}.
\tag{37.26}
$$

Khi ấy $f<f_0$. Với ánh sáng trong chân không, không có một môi trường truyền ưu tiên như không khí trong bài Doppler âm. Chuyển động tương đối giữa nguồn và người thu quyết định kết quả trong cấu hình dọc đường nối đang xét.

![Hình 37.18: Radar đo tốc độ xe bằng cách so tần số sóng phát và sóng phản xạ đã trải qua hai lần dịch Doppler.](../img/young-37/hinh-37-18.png)

Radar phát sóng tần số $f_0$. Xe tiến lại gần đo tần số cao hơn trong hệ của nó. Sóng phản xạ có cùng tần số ấy trong mô hình phản xạ đàn hồi ở hệ xe, rồi lại được dịch lên khi quay về radar.

Do đó, phải xét hai lần Doppler. Đo độ chênh giữa tần số phát và tần số phản xạ thu về cho phép suy tốc độ xe, như bài 37.59 triển khai.

### Ví dụ 37.8: Luồng vật chất từ tâm thiên hà

Vật chất quanh lỗ đen siêu khối lượng có thể bị nung nóng, ion hóa và tạo từ trường mạnh. Tương tác điện từ hướng một phần vật chất vào các luồng phun nhanh ra không gian liên thiên hà.

![Hình 37.19: Luồng vật chất dài khoảng 5000 năm ánh sáng phát ra từ vùng tâm thiên hà M87. Ánh sáng của luồng gắn với electron nhanh chuyển động xoắn quanh đường sức từ.](../img/young-37/hinh-37-19.png)

Xét mô hình một vạch bức xạ từ luồng có tần số chúng ta đo được $f=6{,}66\times10^{14}\,\mathrm{Hz}$, còn tần số trong hệ vật chất phát là $f_0=5{,}55\times10^{13}\,\mathrm{Hz}$. Tìm tốc độ tương đối của vật chất theo phương nhìn.

**Nhận dạng và chuẩn bị:** Vì $f>f_0$, vật chất tiến lại gần trong mô hình Doppler dọc. Đặt $r=f/f_0=12{,}0$. Tần số thu tương ứng bước sóng khoảng $450\,\mathrm{nm}$, thuộc ánh sáng nhìn thấy, còn tần số riêng tương ứng khoảng $5{,}41\,\mu\mathrm m$, thuộc hồng ngoại.

**Thực hiện:** Bình phương (37.25) rồi giải theo tốc độ:

$$
\frac uc=\frac{r^2-1}{r^2+1}\approx0{,}986.
$$

**Đánh giá:** Độ dịch tần rất lớn nên không dùng gần đúng tốc độ nhỏ. Nếu đặt sai $u/c\approx(f-f_0)/f_0$, ta sẽ thu được $u\approx11c$, không thể là tốc độ của vật chất trong mô hình này.

Tần số quan sát phụ thuộc chuyển động tương đối, nhưng tốc độ truyền ánh sáng trong chân không vẫn bằng $c$. Đó là hai phát biểu khác nhau, cùng được thỏa mãn bởi quan hệ Doppler tương đối tính.
