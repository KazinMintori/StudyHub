<!-- Source: Section24.2, printed786–789/PDF806–809. -->

## Tụ mắc nối tiếp và song song

Linh kiện được chế tạo với một số điện dung và điện áp làm việc tiêu chuẩn. Giá trị có sẵn có thể khác giá trị cần cho một mạch. Ghép nhiều tụ cho phép tạo điện dung tương đương phù hợp. Hai cách ghép cơ bản là nối tiếp và song song.

![Hình 24.7: Nhiều kiểu tụ linh kiện có điện dung và điện áp làm việc khác nhau](../img/young-24/hinh-24-7.png)

### Nối tiếp giữ cùng độ lớn điện tích

Hai tụ C₁,C₂ nối tiếp từ a qua nút c đến b. Ban đầu cả hai chưa tích điện. Đặt điện áp dương V_ab vào hai đầu. Bản đầu của C₁ nhận +Q. Điện trường hút electron đến bản còn lại của C₁, làm bản ấy có −Q. Electron này đến từ bản nối cùng nút của C₂, nên bản ấy có +Q. Bản cuối C₂ nhận −Q từ đầu b.

Hai bản ở nút c chỉ nối với nhau và tổng điện tích của nút ban đầu bằng không. Không có đường dẫn đưa điện tích ra, vào nút, nên tổng ấy vẫn bằng không. Bởi vậy các bản tụ trong chuỗi này có cùng độ lớn điện tích Q.

![Hình 24.8: Hai tụ nối tiếp và tụ tương đương có cùng điện tích ở cùng điện áp hai đầu](../img/young-24/hinh-24-8.png)

Đặt V₁ = V_ac, V₂ = V_cb và V = V_ab. Khi đó V₁ = Q/C₁, V₂ = Q/C₂, còn điện áp hai đầu là tổng hai điện áp:

$$
\begin{aligned}
&V = V_1+V_2\\
&\quad =Q(1/C_1+1/C_2).
\end{aligned}
$$

Chia hai vế cho cùng điện tích Q khác không:

$$
\begin{aligned}
&V/Q = 1/C_1\\
&\quad+1/C_2.
\end{aligned}
\tag{24.3}
$$

**Điện dung tương đương** là điện dung của một tụ có cùng điện tích đầu cực Q khi đặt cùng điện áp V với cả mạng:

$$
\begin{aligned}
&C_{\mathrm{eq}} = Q/V,\\
&1/C_{\mathrm{eq}} = V/Q.
\end{aligned}
\tag{24.4}
$$

Thay (24.3) vào (24.4), rồi mở rộng cho n tụ nối tiếp:

$$
\begin{aligned}
&\frac1{C_{\mathrm{eq}}} = \frac1{C_1}+\frac1{C_2}\\
&\quad+\cdots+\frac1{C_n}.
\end{aligned}
\tag{24.5}
$$

Nếu dùng tổng, đó là $\sum_{i=1}^{n}1/C_i$, với i chạy qua n tụ. Khi có ít nhất hai tụ có điện dung dương hữu hạn, C_eq nhỏ hơn mọi Cᵢ.

Các tụ nối tiếp có cùng Q trong cấu hình ban đầu chưa nạp này. Điện áp mỗi tụ lại tỷ lệ nghịch điện dung, nên chỉ bằng nhau khi các điện dung bằng nhau. Các điện áp cộng lại thành điện áp toàn chuỗi. Nếu nút giữa có điện tích dư ban đầu, phải bảo toàn điện tích riêng của nút và không tự áp đặt hai điện tích bằng nhau.

### Song song giữ cùng điện áp

Nối hai bản trên vào cùng nút a và hai bản dưới vào cùng nút b. Các bản cùng nút tạo thành một miền đẳng thế. Vì vậy mỗi tụ có cùng điện áp V = V_ab. Điện tích đi vào mỗi nhánh độc lập nên điện tích hai tụ có thể khác nhau:

$$
\begin{aligned}
&Q_1 = C_1V,\\
&Q_2 = C_2V,\\
&Q = Q_1+Q_2,\\
&Q/V = C_1+C_2.
\end{aligned}
\tag{24.6}
$$

![Hình 24.9: Hai tụ song song cùng điện áp, điện tích đầu cực của mạng bằng tổng điện tích từng nhánh](../img/young-24/hinh-24-9.png)

Tụ tương đương có cùng V và cùng tổng điện tích Q. Với n nhánh:

$$
\begin{aligned}
&C_{\mathrm{eq}} = C_1+C_2\\
&\quad+\cdots+C_n\\
&\quad =\sum_{i=1}^{n}C_i.
\end{aligned}
\tag{24.7}
$$

i chạy từ 1 đến n qua các tụ song song. Với ít nhất hai tụ dương hữu hạn, C_eq lớn hơn từng điện dung riêng. Điện áp giống nhau nhưng Q chỉ giống nhau nếu C giống nhau. Tổng điện tích mỗi phía là Q₁ + Q₂ + ⋯ + Qₙ.

### Ứng dụng: Màn hình cảm ứng

Phía sau màn hình điện thoại, máy tính bảng hoặc thiết bị y tế có hai tầng dải dẫn mỏng, trong suốt, chẳng hạn indium tin oxide. Hai tầng được giữ ở một điện áp. Các dải của tầng này vuông góc các dải tầng kia, tạo lưới các tụ tại vị trí chồng lên nhau.

Đưa ngón tay, vốn dẫn điện, đến một điểm trên màn hình tạo thêm ảnh hưởng điện dung giữa ngón tay và tầng dẫn phía trước. Trong mô hình đang xét, ảnh hưởng ấy tương ứng thêm một tụ nối tiếp tại vị trí đó. Mạch nhận biết nơi điện dung thay đổi để xác định điểm được chạm.

![Màn hình cảm ứng nhận vị trí ngón tay qua thay đổi điện dung](../img/young-24/ung-dung-man-hinh.png)

### Cách phân tích điện dung tương đương

Trước hết vẽ lại các **nút dẫn nối thông**, rồi nhận từng nhóm nối tiếp hoặc song song. Hai tụ nằm liên tiếp trên hình chưa đủ để kết luận nối tiếp. Cần nút chung của chúng không có nhánh khác trong cách rút gọn ấy. Hai tụ có chung cả hai nút mới song song.

Với nhóm nối tiếp chưa nạp ban đầu, các điện tích cùng độ lớn, còn điện áp cộng. Với nhóm song song, điện áp giống nhau, còn điện tích cộng. Thay nhóm bằng một tụ tương đương rồi tiếp tục tìm nhóm mới lộ ra. Nếu cần điện tích hoặc điện áp của từng tụ ban đầu, quay lại các bước rút gọn theo thứ tự ngược.

Sau mỗi bước, điện dung nối tiếp phải nhỏ hơn từng thành phần, điện dung song song phải lớn hơn từng thành phần khi có ít nhất hai tụ dương. Những quan hệ ấy giúp nhận một cách ghép bị đọc sai.

### Ví dụ 24.5: Cùng hai tụ, hai cách mắc

Cho C₁ = 6,0 µF, C₂ = 3,0 µF và điện áp hai đầu 18 V. Tìm điện dung tương đương, điện tích và điện áp mỗi tụ khi (a) nối tiếp, (b) song song.

::: solution Chi tiết
**Xác định và thiết lập.** Dùng (24.5) cho chuỗi và (24.7) cho các nhánh. Sau đó dùng Q = CV với đúng điện áp của từng nhóm.

(a) Nối tiếp:

$$
\begin{aligned}
&1/C_{\mathrm{eq}} = 1/(6.0\,\mathrm{\mu F})\\
&\quad+1/(3.0\,\mathrm{\mu F}),\\
&C_{\mathrm{eq}} = 2.0\,\mathrm{\mu F},\\
&Q = C_{\mathrm{eq}}V\\
&\quad =36\,\mathrm{\mu C},\\
&V_1 = Q/C_1=6.0\,\mathrm V,\\
&V_2 = Q/C_2=12.0\,\mathrm V.
\end{aligned}
$$

Điện tích mỗi tụ có cùng độ lớn 36 µC. Tụ điện dung nhỏ hơn chịu điện áp lớn hơn.

(b) Song song:

$$
\begin{aligned}
&C_{\mathrm{eq}} = 6.0+3.0\\
&\quad =9.0\,\mathrm{\mu F},\\
&V_1 = V_2=18\,\mathrm V,\\
&Q_1 = 108\,\mathrm{\mu C},\\
&Q_2 = 54\,\mathrm{\mu C}.
\end{aligned}
$$

**Đánh giá.** Điện dung chuỗi nhỏ hơn 3 µF, còn điện dung song song lớn hơn 6 µF. Ở chuỗi, 6 V + 12 V = 18 V. Ở song song, 108 µC + 54 µC = 162 µC, bằng điện tích của tụ 9 µF khi đặt 18 V. Bản có dấu dương, âm được xác định theo nút cao thế, thấp thế của từng tụ.
:::

::: exercise Câu hỏi sau Ví dụ 24.5
Chứng tỏ tổng Q₁ + Q₂ trong cách mắc song song bằng điện tích của tụ tương đương khi đặt cùng điện áp.
:::

::: solution Giải thích
Vì Q₁ = C₁V và Q₂ = C₂V, tổng bằng (C₁ + C₂)V = C_eqV. Quan hệ dùng cùng điện áp V trên hai nhánh.
:::

### Ví dụ 24.6: Mạng năm tụ

Tìm điện dung tương đương giữa a,b trong Hình 24.10. Mạng có tụ 9 µF nối tiếp với một nhóm song song gồm nhánh 3 µF, nhánh 11 µF và nhánh hai tụ 12 µF, 6 µF nối tiếp.

![Hình 24.10: Các bước rút gọn mạng năm tụ thành một tụ tương đương](../img/young-24/hinh-24-10.png)

::: solution Chi tiết
**Xác định và thiết lập.** Không thể gộp cả năm bằng một công thức nối tiếp hoặc song song. Rút từ nhóm trong ra ngoài:

$$
\begin{aligned}
&C' = (1/12+1/6)^{-1}\\
&\quad =4\,\mathrm{\mu F},\\
&C'' = 3+11+4\\
&\quad =18\,\mathrm{\mu F},\\
&C_{\mathrm{eq}} = (1/18+1/9)^{-1}\\
&\quad =6\,\mathrm{\mu F}.
\end{aligned}
$$

Các giá trị số trong phép nghịch đảo cùng dùng đơn vị µF. Nếu V_ab = 9,0 V, điện tích đầu cực mạng là 54 µC.

Nhánh 18 µF chịu 54/18 = 3,0 V, còn tụ 9 µF chịu 6,0 V. Trong nhóm song song, các tụ 3 µF, 11 µF có điện tích lần lượt 9 µC, 33 µC. Nhánh 4 µF có điện tích 12 µC. Đó cũng là độ lớn điện tích mỗi tụ 12 µF, 6 µF ban đầu, với điện áp 1,0 V, 2,0 V.

**Đánh giá.** Ba điện tích nhánh 9 + 33 + 12 = 54 µC cộng lại bằng điện tích nhóm. Trong nhánh nối tiếp, 1 V + 2 V = 3 V. Điện áp nhóm ngoài 3 V + 6 V = 9 V. Những tổng này cùng mô tả một mạng, không phải các điện tích được thêm độc lập.
:::

::: exercise Câu hỏi sau Ví dụ 24.6
Khi V_ab = 9,0 V, hãy tự tìm điện tích và điện áp từng tụ trong Hình 24.10 trước khi mở lời giải.
:::

::: solution Kết quả
| Điện dung | Điện áp | Độ lớn điện tích |
| --- | --- | --- |
| 3 µF | 3,0 V | 9 µC |
| 11 µF | 3,0 V | 33 µC |
| 12 µF | 1,0 V | 12 µC |
| 6 µF | 2,0 V | 12 µC |
| 9 µF | 6,0 V | 54 µC |
:::

::: exercise Câu hỏi ôn lại mục 24.2
Có hai tụ 4 µF và 8 µF, ban đầu chưa nạp. (a) Mắc thế nào để tụ 4 µF có điện áp lớn hơn tụ 8 µF? (b) Mắc thế nào để tụ 4 µF có điện tích lớn hơn tụ 8 µF? Với mỗi câu chọn (i) nối tiếp, (ii) song song, (iii) cả hai cách, hoặc (iv) không cách nào trong hai cách ấy.
:::

::: solution Giải thích
(a) Chọn (i). Nối tiếp giữ cùng Q, nên V = Q/C lớn hơn ở tụ 4 µF. (b) Chọn (iv). Nối tiếp cho Q bằng nhau, song song cho Q ở tụ 8 µF lớn hơn vì cùng V. Hai cách ấy không làm tụ 4 µF có điện tích lớn hơn tụ 8 µF trong điều kiện đã cho.
:::
