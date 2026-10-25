### Bài tập cầu nối: Vừa dao động vừa lăn

Hai hình trụ đặc đồng nhất, mỗi hình có bán kính $R$, có tổng khối lượng $M$. Chúng được nối dọc trục chung bằng một thanh ngắn, nhẹ và đặt trên mặt bàn ngang như Hình 14.29. Một vòng không ma sát ở giữa thanh được nối vào lò xo có độ cứng $k$, đầu kia của lò xo được giữ cố định.

Kéo các hình trụ sang trái một đoạn $x$, làm lò xo dãn, rồi thả từ nghỉ. Do có ma sát với bàn, các hình trụ lăn không trượt khi dao động. Chứng minh khối tâm của chúng dao động điều hòa và tìm chu kỳ.

![Hình 14.29: Hai trụ đặc nối cùng trục và gắn lò xo qua vòng không ma sát ở tâm thanh nối. Khi được kéo lệch rồi thả, chúng vừa tịnh tiến vừa quay.](/vat-ly-1/bai-giang/img/young-14/r-exercises-figure-14-29.png)

#### Các bước hướng dẫn

1. Điều kiện nào cần thỏa để khối tâm các hình trụ dao động điều hòa?
2. Dùng những phương trình nào để mô tả (a) chuyển động tịnh tiến và quay của các trụ, (b) điều kiện lăn không trượt? Có thể ôn Mục 10.3.
3. Vẽ tình huống, chọn hệ tọa độ, liệt kê các đại lượng chưa biết và xác định đại lượng cần tìm.
4. Vẽ sơ đồ lực của các trụ khi lệch khỏi cân bằng một đoạn $x$.
5. Giải hệ phương trình để tìm gia tốc khối tâm theo li độ. Kết quả cho biết điều gì?
6. Dùng kết quả bước 5 để tìm chu kỳ dao động khối tâm.
7. Nếu không có ma sát và các trụ không lăn, chu kỳ bằng bao nhiêu? Nó lớn hơn hay nhỏ hơn kết quả bước 6? Giải thích tính hợp lý.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai trụ có tổng khối lượng $M$, bán kính $R$, nối với lò xo ngang độ cứng $k$ qua trục. Thanh nối và vòng có khối lượng không đáng kể. Xét ma sát tĩnh đủ để duy trì lăn không trượt, không có tổn hao lăn trong mô hình.

**Hướng đi:**

- Muốn chứng minh khối tâm dao động điều hòa, cần suy gia tốc tỷ lệ và ngược dấu với li độ: $a_x=-\omega^2x$ với $\omega$ không đổi.
- Dùng đồng thời định luật II Newton cho tịnh tiến, phương trình mômen quanh khối tâm và điều kiện lăn. Bỏ phương trình quay sẽ bỏ phần động năng quay của hai trụ.
- Lực lò xo đặt qua trục nên không tạo mômen quanh khối tâm. Ma sát tại tiếp điểm mới tạo mômen quay. Tìm lực ấy cùng gia tốc, không giả sử nó luôn bằng lực ma sát giới hạn.

**Lời giải:**

#### 1. Điều kiện cần chứng minh

Nếu gia tốc khối tâm có dạng $a_x=-Cx$, với $C>0$ là một hằng số, chuyển động là dao động điều hòa và $\omega=\sqrt C$. Ta cần tìm $C$ từ các phương trình động lực học.

#### 2. Các phương trình và điều kiện lăn

Chọn chiều dương trục $x$ sang trái, phù hợp với độ kéo ban đầu trên hình. Góc quay dương được chọn ngược chiều kim đồng hồ khi nhìn vào mặt đầu trụ. Với quy ước này, lăn sang trái đi kèm góc quay dương, nên

$$
v_x=R\dot\theta,\qquad a_x=R\alpha.
$$

Gọi $f$ là thành phần có dấu của hợp lực ma sát theo chiều sang trái. Lò xo có thành phần $-kx$. Khi trụ ở $x>0$, lò xo kéo sang phải, còn ma sát cần tạo mômen quay theo chiều kim đồng hồ.

#### 3. Khối lượng và mômen quán tính

Mỗi trụ có khối lượng $M/2$. Mômen quán tính mỗi trụ quanh trục chung là $MR^2/4$. Tổng mômen quán tính của hai trụ vì vậy là

$$
I=I_1+I_2=\frac12MR^2.
$$

Các đại lượng chưa biết có thể chọn là $a_x$, $\alpha$, $f$ và chu kỳ $T$. Đích cần tìm là quan hệ $a_x(x)$ rồi chu kỳ của chuyển động.

#### 4. Sơ đồ lực

Các ngoại lực là trọng lực $Mg$, phản lực pháp tuyến $N$, lực lò xo và ma sát tĩnh tại tiếp điểm. Không có gia tốc theo phương đứng, nên $N=Mg$. Hai lực đứng không tạo mômen quanh tâm trụ vì đường tác dụng đi qua tâm.

![Sơ đồ lời giải: Phần (a) tách các lực cho phương trình tịnh tiến khi x dương sang trái. Phần (b) chỉ ra ma sát ở tiếp điểm tạo mômen quanh khối tâm, với cánh tay đòn R.](/vat-ly-1/bai-giang/img/young-14/bridge-14-free-body.svg)

Phương trình tịnh tiến là

$$
Ma_x=-kx+f.
$$

Ma sát dương sang trái tại điểm thấp nhất gây mômen theo chiều kim đồng hồ, ngược chiều góc dương đã chọn. Vì vậy

$$
I\alpha=-Rf.
$$

Lực lò xo đặt qua vòng tại trục không trực tiếp tạo mômen quanh trục. Không thêm một “lực lăn” riêng ngoài các lực vừa liệt kê.

#### 5. Gia tốc và tính điều hòa

Từ $\alpha=a_x/R$ và phương trình mômen,

$$
f=-\frac{I}{R^2}a_x.
$$

Thế vào phương trình tịnh tiến:

$$
\left(M+\frac{I}{R^2}\right)a_x=-kx.
$$

Với $I=MR^2/2$, hệ thức trở thành

$$
\frac32Ma_x=-kx.
$$

Do đó

$$
a_x=-\frac{2k}{3M}x.
$$

Gia tốc đúng là tỷ lệ li độ và ngược dấu với li độ. Hệ vì vậy dao động điều hòa quanh vị trí lò xo không dãn.

Lực ma sát có thành phần

$$
f=\frac{kx}{3}.
$$

Ở biên trái, nó hướng sang trái và tạo mômen để các trụ bắt đầu lăn sang phải. Ma sát tĩnh phải đủ lớn để cung cấp lực này. Nếu không đủ, giả thiết lăn không trượt mất hiệu lực.

#### 6. Tần số góc và chu kỳ

So sánh gia tốc với $a_x=-\omega^2x$, ta được

$$
\omega=\sqrt{\frac{2k}{3M}},
$$

$$
T=2\pi\sqrt{\frac{3M}{2k}}.
$$

Bán kính $R$ triệt tiêu vì mômen quán tính trụ đặc tỷ lệ $MR^2$, trong khi điều kiện lăn đưa vào hệ số $1/R^2$.

#### 7. So sánh với trường hợp không ma sát

Khi mặt bàn không có ma sát, lực lò xo qua trục không tạo mômen. Các trụ được thả từ nghỉ nên không bắt đầu quay. Phương trình ngang chỉ còn $Ma_x=-kx$, cho chu kỳ

$$
T_0=2\pi\sqrt{\frac Mk}.
$$

Tỷ số hai chu kỳ là

$$
\frac T{T_0}=\sqrt{\frac32}>1.
$$

Trường hợp lăn có chu kỳ dài hơn vì năng lượng đàn hồi phải chuyển thành cả động năng tịnh tiến lẫn động năng quay. Có thể kiểm điều này từ

$$
K=\frac12Mv_x^2+\frac12I\dot\theta^2.
$$

Với điều kiện lăn và mômen đã cho,

$$
K=\frac34Mv_x^2.
$$

Hệ có khối lượng hiệu dụng tịnh tiến $3M/2$. Ma sát tĩnh lý tưởng không làm mất cơ năng ở tiếp điểm đứng yên tức thời. Chu kỳ dài hơn ở đây không phải do một quá trình tiêu tán năng lượng.

</details>
