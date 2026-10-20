# Phạm vi bổ sung thống kê cổ điển

Tài liệu này ghi phạm vi học thuật của chín bài 36–44, nguồn đối chiếu và kiểm chứng số. Đây là sổ biên tập, không phải nội dung hiển thị cho sinh viên. Các bài xác suất 28–35 và suy luận Bayes ở bài 45 liên kết với cụm này nhưng có phần rà soát riêng.

## Bản đồ nội dung

| Bài | Nội dung đã triển khai trong Notes và bốn thẻ Slides | Điều kiện và giới hạn được giữ | Bài tập có lời giải gập |
| --- | --- | --- | --- |
| 36. Phân phối mẫu chính xác | Mẫu i.i.d., thống kê, hàm phân phối thực nghiệm, hiệu chỉnh Bessel, tính độc lập trong mẫu chuẩn, Chi bình phương, Student, Fisher, phân vị tích lũy và tới hạn đuôi phải | Bessel chỉ cần phương sai hữu hạn. Các phân phối t, Chi bình phương của phương sai và Fisher chính xác cần mẫu chuẩn, với các thành phần độc lập. Không tương quan không suy ra độc lập | 5 |
| 37. Ước lượng điểm | Độ chệch, MSE, nhất quán, momen, hợp lý và log-hợp lý, MLE mũ/chuẩn/đều, điểm biên, tính bất biến | Momen trung tâm mẫu chia cho n. Gamma dùng tham số tốc độ. Mật độ liên tục không phải xác suất tại điểm. MLE có thể không tồn tại, không duy nhất hoặc đạt biên. MLE chuẩn phương sai dương cần mẫu không đồng nhất | 5 |
| 38. Đủ và hiệu quả | Phân tích nhân tử, tham số chuẩn đã biết/chưa biết, Rao–Blackwell, điểm số, thông tin Fisher, Cramér–Rao, tính đầy đủ, Lehmann–Scheffé, UMVU | Rao–Blackwell cần phương sai hữu hạn. Cramér–Rao cần chính quy, tham số nội, đổi đạo hàm và kỳ vọng, thông tin dương hữu hạn. Lehmann–Scheffé cần đủ và đầy đủ. Bernoulli xét 0 < p < 1 | 5 |
| 39. Khoảng tin cậy | Bao phủ, Pivot, khoảng trung bình chuẩn, cặp, gộp, Welch, Wald/Wilson/Clopper–Pearson, một phương sai và tỷ số phương sai, một phía, cỡ mẫu | Welch là xấp xỉ và có thể dùng bậc tự do không nguyên. Wilson không bảo đảm bao phủ tối thiểu mọi n,p. Tỷ lệ chênh được diễn giải bằng điểm phần trăm. Khảo sát quan sát không suy ra tác dụng nhân quả | 4 |
| 40. Kiểm định và công suất | Giả thuyết đơn/phức, mức và kích thước kiểm định, hai sai lầm, công suất, Neyman–Pearson, GLRT/Wilks, z/t, tỷ lệ gộp, phương sai, p-value, cỡ mẫu | Mức alpha là cận trên sai lầm loại I. Neyman–Pearson cho hai giả thuyết đơn và có thể cần ngẫu nhiên hóa. Wilks là tiệm cận chính quy, không tự dùng ở biên. Cách tính p hai phía phải gắn thống kê và quy tắc cực đoan | 4 |
| 41. Chi bình phương | Độ phù hợp Pearson, mất bậc tự do, bảng độc lập/đồng nhất, tần số thưa, Fisher 2×2, Phi và Cramér V | Trừ tham số phù hợp với cách khớp từ tần số nhóm và điều kiện chính quy. Tần số thưa cần gộp có căn cứ hoặc hiệu chuẩn chính xác/mô phỏng. Fisher 2×2 không thay cho độ phù hợp đa thức một chiều. Phi không âm là độ lớn của tương quan nhị phân | 4 |
| 42. ANOVA | Một nhân tố, phân rã bình phương, MSB/MSW, kiểm định F, FWER, Bonferroni, Tukey HSD, hai nhân tố và tương tác | F chính xác cần sai số chuẩn độc lập cùng phương sai. FWER=1−(1−alpha)^m chỉ khi độc lập và mọi giả thuyết không đúng. Tukey cần mô hình phù hợp. Tương tác đòi hỏi xét hiệu ứng theo từng mức, thiết kế lặp cần r≥2 để tách tương tác và sai số | 4 |
| 43. Suy luận hồi quy | Hồi quy đơn có thiết kế cố định, phân phối OLS, phương sai dư, kiểm định và khoảng hệ số, CI kỳ vọng và PI cá thể, chẩn đoán, hồi quy bội, R² hiệu chỉnh, F tổng thể, ma trận mũ | Hạng thiết kế đầy đủ và n>p. k đếm biến dự báo, p=k+1 tính cả chặn. Sai số chuẩn độc lập cùng phương sai cho suy luận chính xác. Khoảng tại từng điểm không phải dải đồng thời. Hồi quy quan sát không tự xác lập nhân quả | 4 |
| 44. Phi tham số | Dấu, Wilcoxon có dấu, hạng trùng, Mann–Whitney, Spearman, K–S một/hai mẫu | Bỏ số không cần cân bằng dấu có điều kiện. Wilcoxon cần đối xứng và hiệu chuẩn hạng trùng. Mann–Whitney cổ điển hiệu chuẩn dưới cùng phân phối, không phải mọi trung vị hay chỉ P(X>Y)=1/2. K–S thường cần null liên tục đã xác định trước, khớp tham số cần hiệu chỉnh hoặc mô phỏng lại | 4 |

Tổng cộng có 39 bài tập, mỗi đề tách khỏi lời giải. Mỗi bài có `hasChapterExercises: true`, vùng `lecture-notes-content` và vùng `lecture-exercises-content`. Mục cuối là `Tài liệu tham khảo`.

## Nguồn đã đối chiếu

- [MIT OpenCourseWare 18.05, Spring 2022](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/) cho hợp lý, kiểm định, khoảng tin cậy và hồi quy. Ghi tên cơ sở để không gán nhầm giảng viên giữa các phiên bản học phần.
- [MIT 18.655, Lecture 6, Sufficiency](https://ocw.mit.edu/courses/18-655-mathematical-statistics-spring-2016/bbbca14a2009e47add8c7ea2a49daa41_MIT18_655S16_LecNote6.pdf) và [đề cương 18.655](https://www.mit.edu/~18.655/syllabus.html) cho tính đủ, Rao–Blackwell, UMVU, Cramér–Rao và kiểm định.
- [MIT 18.655, Unbiased Estimation and Risk Inequalities](https://ocw.mit.edu/courses/18-655-mathematical-statistics-spring-2016/resources/mit18_655s16_lecnote13/) cho điều kiện chính quy của bất đẳng thức thông tin và [Gaussian Linear Models](https://ocw.mit.edu/courses/18-655-mathematical-statistics-spring-2016/resources/mit18_655s16_lecnote19/) cho phân phối hệ số, phần dư và bậc tự do dưới thiết kế cố định.
- [Penn State STAT 415](https://online.stat.psu.edu/stat415/) cho toàn bộ phạm vi thống kê toán. Không gán số bài đoán trước vì cấu trúc nguồn có thể thay đổi.
- [NIST Gallery of Distributions](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm), [ước lượng tham số](https://www.itl.nist.gov/div898/handbook/eda/section3/eda365.htm), [khoảng tin cậy](https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm), [khoảng tỷ lệ](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm) và [kiểm định](https://www.itl.nist.gov/div898/handbook/prc/section1/prc13.htm).
- [NIST Pearson goodness-of-fit](https://www.itl.nist.gov/div898/handbook/eda/section3/eda35f.htm), [ANOVA](https://www.itl.nist.gov/div898/handbook/prc/section4/prc43.htm), [Tukey](https://www.itl.nist.gov/div898/handbook/prc/section4/prc471.htm) và [chẩn đoán mô hình](https://www.itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm).
- [NIST Rank Sum](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/ranksum.htm), [Signed Rank](https://www.itl.nist.gov/div898/software/dataplot/refman1/auxillar/signrank.htm), [K–S](https://www.itl.nist.gov/div898/handbook/prc/section2/prc212.htm) và [Penn State STAT 500, phi tham số](https://online.stat.psu.edu/stat500/Lesson11).

## Kiểm chứng số và hình

Chạy `python -I scripts/qa/xstk-classical-statistics.py` để tính lại các ví dụ và bài tập. Bộ kiểm tra dùng SciPy/NumPy, có cả kiểm chứng phân phối, phân vị, CI, p-value, MSE, công suất, tổng bình phương và ma trận mũ. Các kiểm tra bổ sung bao phủ những bài tập vốn chưa được xác minh trong bản nháp.

- Wilcoxon có hạng trùng ở bài 44 xét đủ 512 cách gán dấu. Hai đuôi có 12 kết cục nên p=12/512, không dùng bảng tới hạn không trùng.
- Mann–Whitney xét đủ 126 cách chọn bốn nhãn trong chín hạng. Hai đuôi có 14 cách nên p=14/126.
- K–S ví dụ đều có D=0,20 và ngưỡng hữu hạn n=5 xấp xỉ 0,5632752. Hình chuẩn riêng có D=0,1881446014 tại mép trái x=0,8.
- Hình độ bao phủ dùng `np.random.default_rng(20261020).normal(50,1.2,20)` và nửa độ rộng cố định `stats.norm.isf(.025)*1.2`. Kết quả thực tế là 18/20, không sửa dữ liệu để ép 19/20.
- Hình Wald/Wilson dùng 2/30, khác ví dụ tính tay 6/40. Hình ANOVA phân rã dùng ba nhóm (2,3,4), (4,5,6), (6,7,8), khác ví dụ phân bón trong Notes. Chú thích xác định rõ từng bộ số.

Mỗi công thức hiển thị dùng dấu mở/đóng trên dòng riêng. Chuỗi dài được ngắt tại quan hệ hoặc thay bằng ký hiệu ngắn có định nghĩa. Không thu nhỏ công thức hay che nội dung để vượt kiểm tra giao diện. Kiểm tra trình duyệt cần mở cả lời giải gập và bốn thẻ Slides ở bề rộng 360px.
