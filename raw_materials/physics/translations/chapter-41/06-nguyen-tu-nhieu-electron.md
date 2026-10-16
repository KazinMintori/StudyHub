## 41.6 Nguyên tử nhiều electron và nguyên lý loại trừ

Khi xét các nguyên tử có nhiều hơn một electron ($Z > 1$), bài toán trở nên phức tạp hơn rất nhiều so với nguyên tử hydro. Bên cạnh lực hút tĩnh điện giữa hạt nhân mang điện tích $+Ze$ và từng electron, ta còn phải tính đến **lực đẩy tĩnh điện giữa các electron** với nhau. Lực đẩy này làm cho phương trình Schrödinger không thể giải chính xác bằng giải tích. Tuy nhiên, bằng các phương pháp gần đúng kết hợp với các nguyên lý lượng tử sâu sắc, ta có thể hiểu được trọn vẹn cấu trúc bảng tuần hoàn các nguyên tố hóa học.

Nếu ta bỏ qua hoàn toàn lực tương tác giữa các electron và chỉ xét lực hút Coulomb từ hạt nhân $+Ze$, mức năng lượng của mỗi electron sẽ có dạng đơn giản:

$$
E_n = -\frac{Z^2}{n^2}(13{,}60\,\mathrm{eV}) \tag{41.43}
$$

Phép gần đúng thô sơ này chỉ chính xác đối với các ion chỉ có một electron duy nhất (như $\mathrm{He}^+$, $\mathrm{Li}^{2+}$). Trong các nguyên tử nhiều electron, lực đẩy giữa các electron có độ lớn tương đương với lực hút hạt nhân, do đó ta bắt buộc phải sử dụng các mô hình gần đúng tốt hơn.

### Gần đúng trường xuyên tâm

Để giải bài toán nguyên tử nhiều electron, phương pháp tiếp cận phổ biến nhất là **gần đúng trường xuyên tâm** (central-field approximation).

Trong phép gần đúng này:
1. Ta giả định mỗi electron chuyển động độc lập trong một điện trường có tính đối xứng cầu hiệu dụng.
2. Điện trường này là tổng hợp của lực hút từ hạt nhân $+Ze$ và lực đẩy trung bình từ đám mây của tất cả các electron còn lại.
3. Thế năng hiệu dụng $U(r)$ chỉ phụ thuộc vào khoảng cách xuyên tâm $r$ từ electron đến hạt nhân, chứ không phụ thuộc vào các góc định hướng $\theta$ và $\phi$.

Vì thế năng có tính đối xứng cầu, hàm sóng của mỗi electron vẫn phân tách được thành phần góc và phần bán kính. Các hàm góc giống hệt như trong nguyên tử hydro (các hàm cầu điều hòa). Các giới hạn của bốn số lượng tử đối với hàm sóng một electron trong mô hình trường xuyên tâm hoàn toàn tương tự như nguyên tử hydro:

$$
\begin{aligned}
&n \ge 1, \quad 0 \le l \le n - 1, \\
&|m_l| \le l, \quad m_s = \pm \frac{1}{2}
\end{aligned}
\tag{41.44}
$$

Tuy nhiên, do điện trường hiệu dụng không còn là trường Coulomb thuần túy $1/r$, năng lượng của các trạng thái dừng không chỉ phụ thuộc vào số lượng tử chính $n$ mà còn **phụ thuộc mạnh mẽ vào số lượng tử obitan** $l$.

### Nguyên lý loại trừ Pauli

Năm 1925, nhà vật lý người Áo Wolfgang Pauli đã phát biểu một nguyên lý cơ bản chi phối toàn bộ cấu trúc của vật chất:

> [!IMPORTANT] Nguyên lý loại trừ Pauli
> Trong một hệ nguyên tử, không thể có hai electron bất kỳ cùng chiếm một trạng thái lượng tử giống nhau. Nói cách khác, không có hai electron nào có thể có cùng một bộ bốn số lượng tử $(n, l, m_l, m_s)$.

Nguyên lý này là hệ quả của một định luật cơ bản hơn về các hạt đồng nhất: Electron là các **fermion** (hạt có spin bán nguyên $s = 1/2$). Hàm sóng của một hệ nhiều fermion bắt buộc phải **phản đối xứng** đối với phép hoán vị vị trí và spin của hai hạt bất kỳ. Nếu hai electron có cùng trạng thái lượng tử, việc hoán vị chúng sẽ làm hàm sóng triệt tiêu đồng nhất bằng không, nghĩa là trạng thái đó không thể tồn tại trong tự nhiên.

![Hình 41.20: Wolfgang Pauli và Niels Bohr quan sát một con quay. Nguyên lý loại trừ gắn với tên Pauli giải thích sự lấp đầy các trạng thái electron.](../img/young-41/hinh-41-20.png)

### Vỏ và phân lớp electron

Các trạng thái lượng tử trong nguyên tử được nhóm thành các **vỏ** (shells) và **phân lớp** (subshells):
- **Vỏ electron**: Tập hợp tất cả các trạng thái có cùng số lượng tử chính $n$. Các vỏ được ký hiệu bằng các chữ cái in hoa: $K$ ($n=1$), $L$ ($n=2$), $M$ ($n=3$), $N$ ($n=4$), v.v.
- **Phân lớp electron**: Tập hợp tất cả các trạng thái trong cùng một vỏ có cùng số lượng tử obitan $l$. Các phân lớp được ký hiệu bằng chữ cái thường: $s$ ($l=0$), $p$ ($l=1$), $d$ ($l=2$), $f$ ($l=3$), v.v.

Số trạng thái lượng tử tối đa trong một phân lớp có số lượng tử $l$:
- Với mỗi giá trị $l$, số lượng tử từ $m_l$ nhận $2l + 1$ giá trị nguyên: $-l, \dots, +l$.
- Với mỗi cặp $(n, l, m_l)$, số lượng tử từ spin $m_s$ nhận 2 giá trị khả dĩ: $+1/2$ và $-1/2$.
- Do đó, số electron tối đa mà một phân lớp có thể chứa là:

$$
N_{\mathrm{subshell}} = 2(2l + 1)
$$

Với $n=2$, hai phân lớp có sức chứa $2+6=8$. Với $n=3$, tổng là $2+6+10=18$. Tổng quát, các phân lớp đóng góp lần lượt 2, 6, 10 cho đến $2(2n-1)$ trạng thái. Viết bằng ký hiệu tổng:

$$
\begin{aligned}
N_{\mathrm{shell}} &= \sum_{l=0}^{n-1} 2(2l + 1) \\
&= 2n^2
\end{aligned}
$$

Bảng sau liệt kê đầy đủ các trạng thái lượng tử khả dĩ trong bốn vỏ đầu tiên của nguyên tử:

Bảng 41.2 được trình bày theo từng vỏ dưới đây. Mỗi dòng giữ số lượng tử quỹ đạo, các hình chiếu từ và số trạng thái có kể spin.

#### Vỏ K

Vỏ có $n=1$ và tổng cộng 2 trạng thái kể spin.
- Phân lớp $1s$ có $\ell=0$, $m_\ell=0$ và 2 trạng thái.

#### Vỏ L

Vỏ có $n=2$ và tổng cộng 8 trạng thái kể spin.
- Phân lớp $2s$ có $\ell=0$, $m_\ell=0$ và 2 trạng thái.
- Phân lớp $2p$ có $\ell=1$, $m_\ell=0,\pm1$ và 6 trạng thái.

#### Vỏ M

Vỏ có $n=3$ và tổng cộng 18 trạng thái kể spin.
- Phân lớp $3s$ có $\ell=0$, $m_\ell=0$ và 2 trạng thái.
- Phân lớp $3p$ có $\ell=1$, $m_\ell=0,\pm1$ và 6 trạng thái.
- Phân lớp $3d$ có $\ell=2$, $m_\ell=0,\pm1,\pm2$ và 10 trạng thái.

#### Vỏ N

Vỏ có $n=4$ và tổng cộng 32 trạng thái kể spin.
- Phân lớp $4s$ có $\ell=0$, $m_\ell=0$ và 2 trạng thái.
- Phân lớp $4p$ có $\ell=1$, $m_\ell=0,\pm1$ và 6 trạng thái.
- Phân lớp $4d$ có $\ell=2$, $m_\ell=0,\pm1,\pm2$ và 10 trạng thái.
- Phân lớp $4f$ có $\ell=3$, $m_\ell=0,\pm1,\pm2,\pm3$ và 14 trạng thái.

### Hiện tượng che chắn và mức độ thâm nhập

Để hiểu tại sao các phân lớp có cùng $n$ lại có năng lượng khác nhau, ta xét hiện tượng **che chắn điện tích** (screening hay shielding).

Các electron ở gần hạt nhân che chắn một phần điện tích dương $+Ze$, khiến các electron ở xa hơn chỉ cảm nhận được một **điện tích hạt nhân hiệu dụng**:

$$
Z_{\mathrm{eff}} e < Z e
$$

Mức năng lượng của electron khi chịu tác dụng che chắn được mô tả xấp xỉ bởi biểu thức:

$$
E_n = -\frac{Z_{\mathrm{eff}}^2}{n^2}(13{,}60\,\mathrm{eV}) \tag{41.45}
$$

> [!CAUTION] Phân biệt các công thức tính năng lượng
> Ba phương trình sau đều có dạng liên quan đến hệ số $(13{,}60\,\mathrm{eV})/n^2$ nhưng áp dụng cho các đối tượng vật lý khác nhau:
> - Năng lượng nguyên tử hydro thuần túy: $E_n = -(13{,}60\,\mathrm{eV})/n^2$.
> - Năng lượng ion một electron với hạt nhân $+Ze$: $E_n = -Z^2 (13{,}60\,\mathrm{eV})/n^2$ theo PT (41.43).
> - Năng lượng electron trong nguyên tử nhiều electron có tính đến hiệu ứng che chắn: $E_n = -Z_{\mathrm{eff}}^2 (13{,}60\,\mathrm{eV})/n^2$ theo PT (41.45).

Mức độ che chắn phụ thuộc chặt chẽ vào số lượng tử obitan $l$:
- **Phân lớp $s$ ($l=0$)**: Mật độ xác suất tìm thấy electron tại gốc tọa độ $r = 0$ là khác không. Hàm sóng bán kính $R_{ns}(r)$ có các đỉnh phụ nằm rất gần hạt nhân, nghĩa là electron $s$ có **mức độ thâm nhập** (penetration) sâu vào vùng lân cận hạt nhân. Khi thâm nhập qua lớp vỏ chắn bên trong, nó cảm nhận điện tích hạt nhân gần bằng $+Ze$, do đó lực hút tĩnh điện mạnh hơn và mức năng lượng sâu hơn (âm hơn).
- **Phân lớp $p, d, f$ ($l \ge 1$)**: Do rào thế ly tâm $\hbar^2 l(l+1)/(2mr^2)$, mật độ xác suất tại $r \to 0$ triệt tiêu hoàn toàn. So với trạng thái s cùng n, các trạng thái có mômen lớn thường ít thâm nhập vào vùng electron bên trong hơn. Chúng chịu che chắn mạnh hơn, nên thường có năng lượng cao hơn trong những ví dụ đang xét. Mức độ che chắn không nhất thiết hoàn toàn.

Đối với các trạng thái hóa trị của nguyên tử kim loại kiềm đang xét, mức độ thâm nhập thường dẫn đến thứ tự:

$$
E_{ns} < E_{np} < E_{nd} < E_{nf}
$$

![Hình 41.21: Sơ đồ phân bố điện tích trong nguyên tử liti minh họa hiệu ứng che chắn của hai electron 1s đối với electron hóa trị 2s.](../img/young-41/hinh-41-21.png)

![Hình 41.22: Muối ăn tan trong nước làm nước biển có vị mặn. Natri dễ nhường một electron, còn clo dễ nhận một electron. Các ion được giữ trong dung dịch nhờ lực hút với những đầu phân cực của phân tử nước.](../img/young-41/hinh-41-22.png)

![Ứng dụng: Cấu hình electron và xạ trị ung thư xương bằng đồng vị stronti-89.](../img/young-41/ung-dung-b-2.png)

> [!NOTE] Ứng dụng y sinh: Cấu hình electron và xạ trị ung thư xương
> Các đốm màu cam trên ảnh X-quang màu là các khối u ung thư xương. Một phương pháp điều trị ung thư xương là tiêm đồng vị phóng xạ của stronti ($^{89}\mathrm{Sr}$) vào tĩnh mạch bệnh nhân. Stronti có tính chất hóa học tương tự như canxi vì ở cả hai nguyên tử, hai electron ngoài cùng đều ở trạng thái $s$ (cấu hình electron đầy đủ là $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^{10}$ $4p^6$ $5s^2$ đối với stronti và $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ đối với canxi). Do đó, stronti dễ dàng được các khối u hấp thụ, nơi quá trình luân chuyển canxi diễn ra nhanh hơn so với mô xương khỏe mạnh. Bức xạ phát ra từ stronti giúp tiêu diệt các tế bào khối u.

### Cấu hình electron ở trạng thái cơ bản

Trạng thái cơ bản của nguyên tử được hình thành bằng cách sắp xếp các electron vào các mức năng lượng từ thấp đến cao, tuân thủ nguyên lý loại trừ Pauli và **quy tắc Hund**:

> [!TIP] Quy tắc Hund
> Khi điền các electron vào một phân lớp chưa bão hòa, các electron có xu hướng chiếm các obitan khác nhau với chiều spin song song tối đa, nhằm cực tiểu hóa lực đẩy tĩnh điện giữa chúng.

Bảng sau biểu diễn cấu hình electron trạng thái cơ bản của 30 nguyên tố đầu tiên trong bảng tuần hoàn (Bảng 41.3):

Bảng 41.3 liệt kê đủ 30 cấu hình. Mỗi ký hiệu phân lớp đi kèm số electron ở số mũ, với số mũ 1 được lược bỏ.

1. Hydro ($\mathrm{H}$), $Z=1$. Cấu hình: $1s$.
2. Heli ($\mathrm{He}$), $Z=2$. Cấu hình: $1s^2$.
3. Liti ($\mathrm{Li}$), $Z=3$. Cấu hình: $1s^2$ $2s$.
4. Beri ($\mathrm{Be}$), $Z=4$. Cấu hình: $1s^2$ $2s^2$.
5. Bo ($\mathrm{B}$), $Z=5$. Cấu hình: $1s^2$ $2s^2$ $2p$.
6. Carbon ($\mathrm{C}$), $Z=6$. Cấu hình: $1s^2$ $2s^2$ $2p^2$.
7. Nitơ ($\mathrm{N}$), $Z=7$. Cấu hình: $1s^2$ $2s^2$ $2p^3$.
8. Oxy ($\mathrm{O}$), $Z=8$. Cấu hình: $1s^2$ $2s^2$ $2p^4$.
9. Flo ($\mathrm{F}$), $Z=9$. Cấu hình: $1s^2$ $2s^2$ $2p^5$.
10. Neon ($\mathrm{Ne}$), $Z=10$. Cấu hình: $1s^2$ $2s^2$ $2p^6$.
11. Natri ($\mathrm{Na}$), $Z=11$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s$.
12. Magie ($\mathrm{Mg}$), $Z=12$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$.
13. Nhôm ($\mathrm{Al}$), $Z=13$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p$.
14. Silic ($\mathrm{Si}$), $Z=14$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^2$.
15. Photpho ($\mathrm{P}$), $Z=15$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^3$.
16. Lưu huỳnh ($\mathrm{S}$), $Z=16$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^4$.
17. Clo ($\mathrm{Cl}$), $Z=17$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^5$.
18. Argon ($\mathrm{Ar}$), $Z=18$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$.
19. Kali ($\mathrm{K}$), $Z=19$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s$.
20. Canxi ($\mathrm{Ca}$), $Z=20$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$.
21. Scandi ($\mathrm{Sc}$), $Z=21$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d$.
22. Titan ($\mathrm{Ti}$), $Z=22$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^2$.
23. Vanadi ($\mathrm{V}$), $Z=23$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^3$.
24. Crom ($\mathrm{Cr}$), $Z=24$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s$ $3d^5$.
25. Mangan ($\mathrm{Mn}$), $Z=25$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^5$.
26. Sắt ($\mathrm{Fe}$), $Z=26$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^6$.
27. Coban ($\mathrm{Co}$), $Z=27$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^7$.
28. Niken ($\mathrm{Ni}$), $Z=28$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^8$.
29. Đồng ($\mathrm{Cu}$), $Z=29$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s$ $3d^{10}$.
30. Kẽm ($\mathrm{Zn}$), $Z=30$. Cấu hình: $1s^2$ $2s^2$ $2p^6$ $3s^2$ $3p^6$ $4s^2$ $3d^{10}$.

Ở crom ($Z=24$) và đồng ($Z=29$), cấu hình thực nghiệm có dạng đặc biệt: Một electron từ phân lớp $4s$ chuyển sang phân lớp $3d$ để tạo thành phân lớp $3d$ nửa bão hòa ($3d^5$) hoặc bão hòa hoàn toàn ($3d^{10}$). Cấu trúc đối xứng của các phân lớp này làm giảm lực đẩy Coulomb giữa các electron, mang lại độ bền nhiệt động học cao hơn.

### Cấu hình electron và các nhóm nguyên tố

Các nguyên tố cùng cột trong bảng tuần hoàn có cấu hình electron ngoài cùng tương tự. Khí hiếm gồm heli, neon, argon, krypton, xenon và radon có vỏ đầy hoặc cấu hình kết thúc bằng phân lớp $p$ đầy.

Các kim loại kiềm liti, natri, kali, rubiđi, xesi và franxi có thêm một electron so với cấu hình khí hiếm tương ứng. Các kim loại kiềm thổ beri, magiê, canxi, stronti, bari và radi có thêm hai electron. Các halogen flo, clo, brom, iốt và astatin thiếu một electron để đạt cấu hình khí hiếm kế tiếp.

Argon có các phân lớp từ $1s$ đến $3p$ đầy. Ở kali, electron tiếp theo chiếm $4s$ thay vì $3d$, vì mức $4s$ có năng lượng thấp hơn trong nguyên tử này. Các mức gần nhau làm thứ tự điền electron không chỉ phụ thuộc số lượng tử chính.

Từ scandi, $Z=21$, đến kẽm, $Z=30$, số electron trong phân lớp $3d$ tăng, trong khi phân lớp $4s$ có một hoặc hai electron. Những nguyên tố này tạo dãy chuyển tiếp thứ nhất với nhiều tính chất hóa học và vật lý gần nhau.

Tình huống tương tự xuất hiện từ $Z=57$ đến $Z=71$. Những nguyên tố này có một hoặc hai electron $6s$, còn các phân lớp $4f$ và $5d$ đang được lấp. Các nguyên tố đất hiếm vì thế có nhiều tính chất gần nhau. Dãy actini với việc lấp các phân lớp bên trong cũng được nhận diện theo cấu trúc electron, với phần dãy đang xét bắt đầu từ $Z=91$.

Trong mô hình trường xuyên tâm, mức năng lượng phụ thuộc vào cả $l$ lẫn $n$. Xét ví dụ nguyên tử natri ($Z=11$): Khi 10 electron lấp đầy các vỏ $K$ và $L$, năng lượng đo được bằng thực nghiệm của electron còn lại ở các trạng thái khác nhau là:
- Trạng thái $3s$: $-5{,}138\,\mathrm{eV}$
- Trạng thái $3p$: $-3{,}035\,\mathrm{eV}$
- Trạng thái $3d$: $-1{,}521\,\mathrm{eV}$
- Trạng thái $4s$: $-1{,}947\,\mathrm{eV}$

Trạng thái $3s$ có năng lượng thấp nhất (liên kết chặt nhất) vì electron $s$ thâm nhập sâu vào các lớp vỏ $K$ và $L$, tiếp cận gần hạt nhân $+11e$ và cảm nhận điện tích hiệu dụng lớn hơn. Trạng thái $3d$ hầu như hoàn toàn nằm ở bên ngoài các lớp vỏ trong, nên $Z_{\mathrm{eff}} \approx 1{,}00$ và có năng lượng cao hơn nhiều.

### Ví dụ 41.9: Xác định Zeff bằng thực nghiệm

Năng lượng đo được của trạng thái $3s$ trong nguyên tử natri là $-5{,}138\,\mathrm{eV}$. Hãy tính giá trị của $Z_{\mathrm{eff}}$.

**Nhận dạng bài toán**: Natri có duy nhất một electron ở vỏ $M$ bên ngoài các vỏ $K$ và $L$ đã lấp đầy. Mười electron ở vỏ $K$ và $L$ che chắn một phần điện tích $+11e$ của hạt nhân đối với electron vỏ $M$. Mục tiêu của ta là xác định mức độ che chắn này. Đề bài cho $n = 3$ và $E_n = -5{,}138\,\mathrm{eV}$, vì vậy ta có thể sử dụng PT (41.45) để xác định $Z_{\mathrm{eff}}$.

**Chuẩn bị**: Giải PT (41.45) để tìm $Z_{\mathrm{eff}}^2$:

$$
Z_{\mathrm{eff}}^2 = -\frac{n^2 E_n}{13{,}60\,\mathrm{eV}}
$$

**Thực hiện**:
Thay số với $n = 3$ và $E_n = -5{,}138\,\mathrm{eV}$:

$$
\begin{aligned}
Z_{\mathrm{eff}}^2 &= -\frac{3^2 (-5{,}138)}{13{,}60} \\
&= 3{,}40
\end{aligned}
$$

Suy ra $Z_{\mathrm{eff}} = \sqrt{3{,}40} \approx 1{,}84$.

**Đánh giá**: Điện tích hiệu dụng hút electron $3s$ là $1{,}84e$. Như vậy 11 proton của natri bị che chắn bởi trung bình $11 - 1{,}84 = 9{,}16$ electron thay vì 10 electron, do electron $3s$ dành một phần thời gian thâm nhập vào các lớp vỏ bên trong ($K$ và $L$).

Mỗi kim loại kiềm (liti, natri, kali, rubiđi và xesi) đều có nhiều hơn một electron so với khí hiếm tương ứng (heli, neon, argon, krypton và xenon). Electron dư này hầu như nằm ở bên ngoài các electron khác trong các vỏ và phân lớp đã lấp đầy. Do đó, tất cả các kim loại kiềm đều có tính chất hóa học rất giống với natri.

**Khái niệm cần nhớ**: Khi có một electron hóa trị bên ngoài các vỏ kín, có thể ước lượng năng lượng của nó bằng mô hình một electron với điện tích hiệu dụng. Ta thay $Z$ bằng $Z_{\mathrm{eff}}$ trong công thức năng lượng. Sự che chắn của các electron lõi làm $Z_{\mathrm{eff}}$ nhỏ hơn $Z$.

### Ví dụ 41.10: Năng lượng của electron hóa trị

Electron hóa trị trong kali có trạng thái cơ bản $4s$. Hãy tính năng lượng xấp xỉ của trạng thái $n = 4$ có $Z_{\mathrm{eff}}$ nhỏ nhất, và thảo luận về năng lượng tương đối của các trạng thái $4s, 4p, 4d$ và $4f$.

**Nhận dạng và chuẩn bị**: Trạng thái có $Z_{\mathrm{eff}}$ nhỏ nhất là trạng thái mà electron hóa trị dành nhiều thời gian nhất ở bên ngoài các vỏ và phân lớp đầy bên trong, sao cho nó được che chắn hiệu quả nhất khỏi điện tích của hạt nhân. Khi xác định được trạng thái có $Z_{\mathrm{eff}}$ nhỏ nhất, ta dùng PT (41.45) để tính năng lượng của trạng thái đó.

**Thực hiện**:
Trạng thái $4f$ có $n = 4$ và $l = 3 = 4 - 1$. Do đó, đây là trạng thái có mômen động lượng obitan lớn nhất đối với $n = 4$, và là trạng thái mà electron dành phần lớn thời gian ở bên ngoài đám mây điện tích electron của các vỏ và phân lớp đầy bên trong. Điều này làm cho $Z_{\mathrm{eff}}$ đối với trạng thái $4f$ rất gần bằng 1. PT (41.45) cho:

$$
\begin{aligned}
E_4 &= -\frac{1^2}{4^2}(13{,}60\,\mathrm{eV}) \\
&= -0{,}85\,\mathrm{eV}
\end{aligned}
$$

Giá trị $-0{,}85\,\mathrm{eV}$ phù hợp với năng lượng trạng thái $4f$ của kali ở độ chính xác đang xét.

Một electron ở trạng thái $4d$ dành thêm một chút thời gian bên trong các vỏ trong, và năng lượng của nó do đó âm hơn một chút (đo được là $-0{,}94\,\mathrm{eV}$). Cùng lý do đó, trạng thái $4p$ có năng lượng còn thấp hơn (đo được là $-2{,}73\,\mathrm{eV}$) và trạng thái $4s$ có năng lượng thấp nhất (đo được là $-4{,}339\,\mathrm{eV}$).

**Đánh giá:** Phân tích này còn áp dụng gần đúng cho các ion $\mathrm{Be}^+$, $\mathrm{Mg}^+$, $\mathrm{Ca}^+$, $\mathrm{Sr}^+$ và $\mathrm{Ba}^+$. Chúng có một electron bên ngoài các vỏ kín. Khi electron ấy ở trạng thái có $\ell=n-1$, điện tích ion lõi gần bằng $+2e$, nên $Z_{\rm eff}\approx2$. Với $\mathrm{Mg}^+$ ở trạng thái $3d$, ta được:

$$
\begin{aligned}
E &\approx -\frac{2^2}{3^2}(13{,}60\,\mathrm{eV}) \\
&\approx -6{,}0\,\mathrm{eV}
\end{aligned}
$$

Năng lượng xấp xỉ $-6{,}0\,\mathrm{eV}$ phản ánh điện tích lõi lớn hơn so với trường hợp kim loại kiềm trung hòa.

**Khái niệm cần nhớ**: Trong mô hình một electron hóa trị ngoài các vỏ kín, trạng thái có $l=n-1$ ít xuyên vào vùng electron lõi. Khi sự che chắn gần như hoàn toàn, điện tích hiệu dụng xấp xỉ bằng điện tích ion lõi.

### Câu tự kiểm tra 41.6

Nếu các electron không tuân theo nguyên lý loại trừ, việc bứt electron đầu tiên ra khỏi nguyên tử natri sẽ dễ dàng hơn hay khó khăn hơn?

::: details Lời giải chi tiết
**Đáp án:** Khó khăn hơn.

**Lập luận**:
Nếu không có nguyên lý loại trừ Pauli, toàn bộ 11 electron trong nguyên tử natri sẽ cùng chiếm mức năng lượng thấp nhất (mức $1s$) và cấu hình electron sẽ là $1s^{11}$.

Trong giả thiết này, electron không bị buộc phải chiếm trạng thái hóa trị $3s$ có năng lượng cao và chịu che chắn mạnh như trong natri thực tế. Việc bứt electron đầu tiên vì thế khó hơn. Không nên hiểu cấu hình giả định $1s^{11}$ là không còn lực đẩy hay che chắn giữa các electron.

(Trong nguyên tử natri thực tế, do tuân thủ nguyên lý loại trừ Pauli, chỉ có 2 electron được phép chiếm mức $1s$, 8 electron chiếm mức $n=2$, và electron hóa trị thứ 11 bắt buộc phải nằm ở mức $3s$. Electron $3s$ này bị 10 electron bên trong che chắn hiệu quả nên liên kết rất lỏng lẻo với năng lượng ion hóa chỉ là $5{,}138\,\mathrm{eV}$, khiến natri là một kim loại kiềm hoạt động hóa học rất mạnh).
:::
