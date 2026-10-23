### Bài tập cầu nối

Một đầu thanh đồng đặc hình trụ dài $0{,}200\,\mathrm m$, bán kính $0{,}0250\,\mathrm m$ cắm vào khối hiđrô rắn lớn đang ở nhiệt độ nóng chảy $13{,}84\,\mathrm K$. Đầu kia được bôi đen, tiếp nhận bức xạ từ các vách xung quanh ở $500{,}0\,\mathrm K$. Mặt bên thanh được cách nhiệt, nên chỉ hai đầu trao đổi năng lượng.

Một số hệ làm lạnh kính thiên văn dùng ý tưởng tương tự: Chất làm lạnh rắn giữ thiết bị rất lạnh dù thiết bị nhận bức xạ từ ngoài.

(a) Khi dòng nhiệt ổn định, đầu bôi đen có nhiệt độ bao nhiêu? Dùng hệ số dẫn nhiệt của đồng gần 20 K là $1670\,\mathrm{W/(m\,K)}$.

(b) Hiđrô nóng chảy với tốc độ bao nhiêu, tính bằng kg/giờ? Nhiệt nóng chảy của hiđrô là $58{,}6\times10^3\,\mathrm{J/kg}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Thanh có chiều dài L, bán kính R như trên. Đầu lạnh giữ ở $T_c=13{,}84\,\mathrm K$, vách ở $T_w=500{,}0\,\mathrm K$. Xem đầu bôi đen có hệ số phát xạ và hấp thụ bằng 1. Dùng k không đổi theo dữ kiện.

**Hướng đi:**

1. Phác họa thanh với đầu lạnh tiếp xúc hiđrô, đầu đen nhìn ra các vách nóng, mặt bên cách nhiệt. Ghi L, R và hai nhiệt độ đã biết.
2. Ẩn là nhiệt độ đầu đen T, dòng nhiệt H và tốc độ nóng chảy. Tiết diện thanh cũng là diện tích mặt đầu nhận bức xạ.
3. Ở trạng thái ổn định, năng lượng đầu đen nhận ròng từ bức xạ bằng năng lượng dẫn dọc thanh. Phải trừ bức xạ mà chính đầu đen phát ra.
4. Dòng nhiệt tới hiđrô dùng cho chuyển pha ở nhiệt độ giữ nguyên, nên $H=L_f\,dm/dt$.
5. Do đồng dẫn nhiệt mạnh, thử T chỉ hơi lớn hơn $T_c$. Giải gần đúng rồi kiểm tra lại phương trình đầy đủ.
6. Từ T suy H và tốc độ nóng chảy.
7. Đánh giá mức chênh hai đầu để kiểm tra giả thiết ở bước 5.
8. Xét tăng bán kính hai lần: So sánh cách diện tích xuất hiện trong cả dòng bức xạ và dòng dẫn.

**Lời giải chi tiết:**

![Sơ đồ bài cầu nối: Thanh đồng nối khối hiđrô ở nhiệt độ nóng chảy với đầu bôi đen nhận bức xạ từ các vách nóng.](../img/young-17/c-bridge-radiation-conduction.svg)

Gọi $A=\pi R^2$ là diện tích mặt cắt. Đầu đen nhận công suất bức xạ ròng:

$$
H_{\mathrm{rad}}=\sigma A(T_w^4-T^4).
$$

Dòng dẫn qua thanh:

$$
H_{\mathrm{cond}}=\frac{kA}{L}(T-T_c).
$$

(a) Ở trạng thái ổn định, hai dòng bằng nhau. Rút gọn A:

$$
\frac{k}{L}(T-T_c)=\sigma(T_w^4-T^4).
$$

Phương trình có duy nhất một nghiệm trong khoảng từ $T_c$ tới $T_w$: Vế trái tăng theo T, vế phải giảm theo T.

Vì T gần nhiệt độ đầu lạnh nên $T^4$ nhỏ hơn nhiều so với $T_w^4$. Bỏ số hạng nhỏ ở lần tính đầu:

$$
T-T_c\approx\frac{\sigma LT_w^4}{k}.
$$

Được $T-T_c\approx0{,}4244\,\mathrm K$. Thay lại và giải phương trình đầy đủ cho $T=14{,}2644\,\mathrm K$, làm tròn $14{,}3\,\mathrm K$. Hiệu chỉnh do bức xạ phát ra của đầu lạnh ở mức rất nhỏ trong bài này.

(b) Tiết diện $A=1{,}9635\times10^{-3}\,\mathrm{m^2}$. Dòng nhiệt:

$$
H=\frac{kA}{L}(T-T_c)=6{,}96\,\mathrm W.
$$

Tốc độ nóng chảy theo giây là $H/L_f$. Đổi sang giờ:

$$
\begin{aligned}
\frac{dm}{dt}&=\frac{3600H}{L_f}\\
&=0{,}427\,\mathrm{kg/h}.
\end{aligned}
$$

Nhiệt độ hai đầu chỉ lệch khoảng 0,424 K, phù hợp giả thiết dẫn nhiệt mạnh ở bước 5. Khi hiđrô còn đồng thời ở pha rắn và lỏng trong mô hình, năng lượng nhận vào làm tăng phần đã nóng chảy thay vì tăng nhiệt độ khối.

Nếu bán kính thanh tăng hai lần, A tăng bốn lần. Nó triệt tiêu khỏi phương trình nhiệt độ nên T giữ nguyên. Cả dòng nhiệt và tốc độ nóng chảy tăng bốn lần. Kết luận giữ các điều kiện cách nhiệt mặt bên, nhiệt độ vách và hệ số vật liệu như trước.

</details>
