# Sổ đối chiếu nguồn chương 30: Từ mục 30.4 đến hết chương

## Phạm vi và tệp đã đọc

Đã đọc `.agents/skills/studyhub-lecture/SKILL.md` và `.agents/skills/studyhub-lecture/references/repo-format.md`. Đối chiếu trực tiếp *University Physics with Modern Physics*, ấn bản 15, chương 30, trang in 998–1017, tức PDF trang 1018–1037. Chỉ số PyMuPDF zero-based tương ứng là 1017–1036, theo quy tắc `trang in + 19`.

Đã đọc bản văn nguồn `qa/physics/full-source/pdf-1018.txt` đến `pdf-1037.txt`, đồng thời render và xem lại toàn bộ 20 trang thành contact sheet. Các trang có công thức, đơn vị vi mô và ví dụ được phóng lớn kiểm tra trực tiếp gồm PDF 1025, 1026, 1028 và 1030 (trang in 1005, 1006, 1008 và 1010). Phần ANSWERS cuối chương nằm ở PDF 1037, trang in 1017.

## Nội dung lý thuyết, ví dụ, câu tự kiểm và hình

| Mục nguồn | Nội dung phải giữ | Ví dụ / tự kiểm | Hình và phương trình |
| --- | --- | --- | --- |
| 30.4, R-L circuit, tr. 998–1002 | Quy tắc Kirchhoff áp dụng tại từng thời điểm; suất điện động tự cảm chống lại biến thiên dòng; dòng tăng từ 0 đến $E/R$ và dòng giảm theo hàm mũ; hằng số thời gian $\tau=L/R$; năng lượng nguồn cấp tách thành nhiệt Joule và năng lượng từ trường. Dòng qua cuộn cảm liên tục, còn $di/dt$ có thể đổi đột ngột. | Example 30.6, chọn $E$ và $L$ để giới hạn dòng ban đầu; Example 30.7, năng lượng tiêu tán trong quá trình dòng suy giảm. Test Your Understanding 30.4 hỏi dấu của $v_{ab}$ và $v_{bc}$ ở hai trạng thái đóng/ngắt công tắc. | Fig. 30.11: mạch R-L hai công tắc; Fig. 30.12: dòng tăng; Fig. 30.13: dòng giảm. Eq. (30.12)–(30.19). |
| 30.5, L-C circuit, tr. 1002–1006 | Điện tích tụ và dòng cuộn cảm dao động điều hòa; năng lượng qua lại giữa điện trường tụ và từ trường cuộn cảm, tổng năng lượng không đổi. Quy ước dấu $i=dq/dt$ trong hình 30.15 cần gắn với điện tích ở bản trái. Nêu tương tự cơ học lò xo–vật nặng và bảng đối chiếu. | Example 30.8, tìm $f,T,q,i$ tại một thời điểm; Example 30.9, phân chia năng lượng điện và từ tại hai thời điểm. Test Your Understanding 30.5 hỏi dấu công và loại lực của tụ, cuộn cảm trong một phần tư chu kỳ. | Fig. 30.14: bốn trạng thái trong một chu kỳ; Fig. 30.15: chiều vòng, dấu $q,i$. Table 30.1: tương tự cơ học–điện. Eq. (30.20)–(30.26). |
| 30.6, L-R-C series circuit, tr. 1007–1009 | Điện trở tiêu tán năng lượng; phân biệt dao động tắt dần, tắt dần tới hạn và quá tắt dần. Đưa phương trình vi phân, nghiệm dưới tắt dần, điều kiện $R^2<4L/C$, tần số góc riêng và ngưỡng tới hạn $R^2=4L/C$. Nghiệm quá tắt dần là tổng hai hàm mũ suy giảm. | Example 30.10, chọn $R$ để tần số giảm còn một nửa tần số riêng. Test Your Understanding 30.6 so sánh ba bộ $(L,C)$ để phân loại có/không dao động. | Fig. 30.16: đồ thị điện tích theo thời gian cho ba chế độ; Fig. 30.17: mạch nạp rồi phóng RLC. Eq. (30.27)–(30.29). |

Chi tiết phương trình được đánh số trong ba mục:

- 30.4: (30.12) phương trình vòng; (30.13) phương trình cho $di/dt$; (30.14) dòng tăng; (30.15) tốc độ tăng; (30.16) $\tau=L/R$; (30.17) cân bằng công suất; (30.18) dòng suy giảm; (30.19) cân bằng công suất khi suy giảm.
- 30.5: (30.20) phương trình dao động điện tích; (30.21) $q(t)$; (30.22) tần số góc riêng; (30.23) $i(t)$; (30.24) vận tốc của dao động cơ dùng trong phép tương tự; (30.25) bảo toàn năng lượng; (30.26) dòng theo điện tích.
- 30.6: (30.27) phương trình RLC; (30.28) nghiệm dưới tắt dần; (30.29) tần số góc dao động tắt dần.

Đầu phạm vi ở trang in 998 còn có Test Your Understanding 30.3, câu hỏi đảo chiều dòng trong solenoid nhưng giữ nguyên độ lớn, hỏi hướng từ trường và mật độ năng lượng. Đáp án in ngay sau câu hỏi: hướng từ trường đổi, mật độ năng lượng giữ nguyên.

## Tóm tắt và bài tập hướng dẫn cuối chương

Summary ở trang in 1009 có sáu thẻ ý chính: hỗ cảm; tự cảm; năng lượng từ trường; mạch R-L; mạch L-C; mạch L-R-C. Summary lặp lại các phương trình chủ lực (30.4)–(30.11), (30.16), (30.22), (30.29), kèm sơ đồ nhỏ.

Guided Practice có **12 câu**, chia thành ba cụm, mỗi cụm bốn câu:

- VP30.4.1–VP30.4.4: Hỗ cảm và tự cảm, ôn Examples 30.1–30.4.
- VP30.7.1–VP30.7.4: Dòng tăng/giảm trong mạch R-L, ôn Examples 30.6–30.7.
- VP30.10.1–VP30.10.4: Dao động L-C, năng lượng và mạch RLC, ôn Examples 30.8–30.10.

Bridging Problem là **Analyzing an L-C Circuit**, với $L=60.0\,\mathrm{mH}$, $C=250\,\mu\mathrm F$, điện tích ban đầu $6.00\,\mu\mathrm C$ và dòng ban đầu $0.400\,\mathrm{mA}$. Bài có 4 phần tính đại lượng cực đại và trạng thái khi dòng bằng nửa cực đại. Solution Guide có 8 bước, từ nhận diện hệ bảo toàn năng lượng đến đánh giá tỉ phần năng lượng ban đầu trong cuộn cảm. Hình được dẫn là Fig. 30.14. Đáp án cầu nối in ở trang 1017: (a) $7.68\times10^{-8}\,\mathrm J$; (b) $1.60\,\mathrm{mA}$; (c) $24.8\,\mathrm{mV}$; (d) $1.92\times10^{-8}\,\mathrm J$ và $21.5\,\mathrm{mV}$.

## Câu hỏi và bài tập cuối chương

| Phần | Dãy / số lượng | Nội dung |
| --- | --- | --- |
| Discussion Questions | Q30.1–Q30.16, **16 câu** | Tia lửa ở tiếp điểm xe điện; tính tương đương đơn vị henry; hỗ cảm; cấu tạo và cách giảm tự cảm; năng lượng từ trường; so sánh R-C với R-L; mạch vi phân; dấu của $di/dt$; quy ước $i=dq/dt$; tính liên tục của dòng; điều kiện tắt dần. Q30.10 có đồ thị dòng theo thời gian và yêu cầu phác dạng hiển thị trên oscilloscope. |
| Exercises | 30.1–30.40, **40 câu** | 30.1–4 hỗ cảm; 30.5–12 tự cảm; 30.13–20 năng lượng từ trường; 30.21–31 mạch R-L; 30.32–37 mạch L-C; 30.38–40 mạch L-R-C. |
| Problems | 30.41–30.68, **28 câu** | Ước lượng cuộn cảm; thực nghiệm, phân tích mạch quá độ, dao động điện, mạch đo và dữ liệu. Một số câu mang nhãn CP, CALC hoặc DATA. |
| Challenge Problems | 30.69–30.71, **3 câu** | Hai solenoid đồng trục nối ngược chiều; đồng hồ đo mức chất lỏng bằng độ từ thẩm; mạch có nhánh cảm kháng và dung kháng.
| MCAT-Style Passage Problems | Đoạn BIO “Quenching an MRI Magnet”, câu 30.72–30.75, **4 câu trắc nghiệm** | Tính số vòng dây; thời gian dòng giảm còn một nửa; ảnh hưởng khi điện trở tăng dần; khối lượng helium hóa hơi nếu toàn bộ năng lượng từ trường chuyển thành nhiệt. |

Lựa chọn MCAT in đầy đủ:

- 30.72: (a) 1100; (b) 3000; (c) 4000; (d) 22,000 vòng.
- 30.73: (a) 4.7 min; (b) 10 min; (c) 15 min; (d) 30 min.
- 30.74: (a) thời gian ngắn hơn do điện trở tăng; (b) thời gian dài hơn do điện trở tăng; (c) không đổi; (d) không đủ dữ kiện.
- 30.75: (a) 27 kg; (b) 38 kg; (c) 60 kg; (d) 110 kg.

Các bài yêu cầu tự dựng/đồ thị hóa rõ ràng: Q30.10 phác dạng điện áp; 30.59 vẽ $1/t_{1/2}$ theo $R_{ext}$; 30.63(c) vẽ ba đại lượng $i_0,v_{ac},v_{cb}$ theo thời gian; 30.64(c) vẽ ba dòng theo thời gian. 30.16(e) yêu cầu đối chiếu mật độ năng lượng từ tổng năng lượng chia thể tích. Bài 30.67 và 30.68 dùng dữ liệu đọc từ các đồ thị đo được ở hình P30.67 và P30.68.

Các hình riêng được gắn vào câu hỏi cuối chương gồm **17 hình**: Q30.10; E30.9; P30.50, P30.51, P30.52; P30.57, P30.58, P30.60, P30.61, P30.63, P30.65, P30.66, P30.67, P30.68, P30.69, P30.70 và P30.71. Phần lý thuyết có bảy hình Fig. 30.11–30.17. Cộng cả lý thuyết và bài tập, dải trang này có **24 hình đánh số**, chưa tính sơ đồ nhỏ trong Summary.

## ANSWERS và cách dùng đáp số

Trang in 1017 có phần ANSWERS cho câu mở đầu chương, tất cả 12 Guided Practice và Bridging Problem. Mỗi Test Your Understanding ở cuối các mục 30.3–30.6 cũng có đáp án ngay dưới câu hỏi. Trong các trang cuối chương 998–1017 đã đối chiếu, không có đáp số chung cho Exercises, Problems, Challenge Problems hoặc MCAT. Không suy diễn đáp số những phần này từ ANSWERS của Guided Practice.

Đáp số Guided Practice được in như sau:

| Câu | Đáp số nguồn |
| --- | --- |
| VP30.4.1 | (a) $6.50\times10^{-5}\,\mathrm H$; (b) $1.56\times10^{-3}\,\mathrm{T\,m^2}$ |
| VP30.4.2 | (a) $3.36\times10^{-4}\,\mathrm V$; (b) $0$; (c) $1.44\times10^{-4}\,\mathrm V$ |
| VP30.4.3 | (a) $1.96\times10^{-6}\,\mathrm{T\,m^2}$; (b) $4.18\times10^{-3}\,\mathrm V$ |
| VP30.4.4 | (a) $25.5\,\mathrm{mH}$; (b) $23.0\,\mathrm{mV}$, ngược chiều dòng điện |
| VP30.7.1 | (a) $84.9\,\Omega$; (b) $0.212\,\mathrm A$ |
| VP30.7.2 | (a) $0.190\,\mathrm A$; (b) $+229\,\mathrm{A/s}$; (c) $6.79\times10^{-4}\,\mathrm J$ |
| VP30.7.3 | (a) $0.476\,\mathrm A$; (b) $-229\,\mathrm{A/s}$; (c) $4.26\times10^{-3}\,\mathrm J$ |
| VP30.7.4 | (a) $(L/R)\ln2=0.693(L/R)$; (b) $E/(2R)$; (c) $E/(2L)$ |
| VP30.10.1 | (a) $5.12\times10^{-3}\,\mathrm F$; (b) $14.0\,\mathrm A$ |
| VP30.10.2 | (a) $2.20\times10^{-4}\,\mathrm s$; (b) $2.85\,\mathrm A$ |
| VP30.10.3 | (a) $35.1\,\mu\mathrm F$; (b) $0.0125\,\mathrm H$; (c) $1.51\times10^3\,\mathrm{rad/s}$ |
| VP30.10.4 | (a) $61.1\,\mu\mathrm F$; (b) $49.4\,\Omega$ |

## Ký hiệu, số mũ và đơn vị cần soát khi biên soạn

- Rà bổ sung tại Codex ngày 2026-10-14: Đã xem trực tiếp trang in 1010 và tính lại 12 bài biến thể cùng bài cầu nối bằng Python. Điện tích trong VP30.10.3 là 5,30 mC, nhưng điện dung suy ra là 35,1 µF. Điện dung trong VP30.10.4 là 61,1 µF. Hai đơn vị mF ở bảng đáp số nháp trước đã được sửa. Bản inventory đã chép vào worktree B trước lần sửa này cần được đối chiếu với ghi chú hiện tại khi giao lại tác vụ.

- Bản OCR thường làm mất dấu căn, số mũ và phân số. Các dạng chuẩn ở trang 1008 đã kiểm trực tiếp: $q=Ae^{-(R/2L)t}\cos\!\left(\sqrt{1/(LC)-R^2/(4L^2)}\,t+\phi\right)$; $\omega'=\sqrt{1/(LC)-R^2/(4L^2)}$; điều kiện tới hạn $R^2=4L/C$; trong Example 30.10, $R=\sqrt{3L/C}$.
- Trang 1005–1006 xác nhận Example 30.8 dùng $25\,\mu\mathrm F$, $10\,\mathrm{mH}$, $Q=7.5\,\mathrm{mC}$; các đáp số là $\omega=2.0\times10^3\,\mathrm{rad/s}$, $f=320\,\mathrm{Hz}$, $T=3.1\,\mathrm{ms}$, $q(1.2\,\mathrm{ms})=-5.5\,\mathrm{mC}$, $i=-10\,\mathrm A$. Example 30.9 cho $U_B=0.5\,\mathrm J$, $U_E=0.6\,\mathrm J$ tại $1.2\,\mathrm{ms}$, tổng $1.1\,\mathrm J$.
- Trang 1010 xác nhận các tiền tố micro: VP30.4.2 ghi $48.0\,\mu\mathrm H$; VP30.4.3 ghi $76.0\,\mu\mathrm H$; VP30.10.1 ghi $25.0\,\mu\mathrm H$; VP30.10.2 ghi $30.0\,\mu\mathrm H$ và $655\,\mu\mathrm F$. Bridging Problem ghi $250\,\mu\mathrm F$ và $6.00\,\mu\mathrm C$.
- Example 30.6 dùng thời gian $58\,\mu\mathrm s$, $L=69\,\mathrm{mH}$ và $\tau=390\,\mu\mathrm s$. Không đọc các đơn vị thời gian này thành ms.
- 30.6 dùng $\mu\mathrm F$ cho cả ba phương án: $6.0\,\mu\mathrm F$, $3.0\,\mu\mathrm F$ và $3.0\,\mu\mathrm F$. OCR đã làm một số trong đó thành `mF`.
- Không nhập nhằng $m$ (khối lượng), tiền tố milli, tiền tố micro $\mu$, hay ký hiệu tần số góc $\omega$. Dấu âm của $i$ trong L-C là hệ quả của quy ước chiều hình 30.15, không đồng nghĩa tốc độ điện tích giảm theo quy ước tùy ý khác.
