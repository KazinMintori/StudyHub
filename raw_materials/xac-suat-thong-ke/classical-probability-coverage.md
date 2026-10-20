# Phạm vi bộ bổ trợ xác suất cổ điển

Bộ bổ trợ gồm tám bài độc lập, số 28–35. Bộ này nối tiếp kiến thức xác suất nhập môn và cung cấp nền toán cho các bài thống kê tham số. Mỗi bài có Notes, bốn thẻ ôn tập, kiến thức liên quan và năm bài tập với lời giải gập.

## Bản đồ nội dung

| Bài | Nội dung đã triển khai | Ví dụ và bài tập đại diện |
| --- | --- | --- |
| 28 | Quy tắc đếm, hoán vị, chỉnh hợp, tổ hợp, vách ngăn, bù trừ, xác suất hình học, cộng tính đếm được, tính liên tục đơn điệu | Phân chia tài nguyên, ba nhóm ngôn ngữ, cuộc hẹn, bẻ que, dãy khoảng giảm |
| 29 | Hai quy ước Geometric, tính không nhớ, Nhị thức âm, Đa thức, hiệp phương sai số đếm, thu thập phiếu | Kiểm thử, kiểm soát chất lượng, ba nhóm văn bản, thu đủ ba loại phiếu |
| 30 | Mật độ và CDF, Exponential, Gamma/Erlang, Beta, Weibull, Lognormal | Chờ giao dịch, chờ gói tin, tỷ lệ nhấp chuột, tốc độ hỏng, mômen Chuẩn bậc bốn |
| 31 | PMF/PDF đồng thời, lề, có điều kiện, Tonelli/Fubini, miền tam giác, tiêu chuẩn độc lập | Bảng sáu ô, mật độ tam giác tuyến tính, đổi cận, kiểm tra tích mật độ trên toàn miền |
| 32 | Hiệp phương sai, tương quan, phương sai tổng, không tương quan và phụ thuộc, kỳ vọng và phương sai toàn phần, MMSE | Tổng Poisson, số lần tung xu ngẫu nhiên, bình phương biến đều, biến Chuẩn đổi dấu |
| 33 | CDF của biến đổi, Jacobi một và hai chiều, tích chập, cực trị, thống kê thứ tự | Bình phương Chuẩn, tổng/tỷ lệ Exponential, tổng hai biến đều, trung vị, CDF đồng thời min/max |
| 34 | Mômen, độ lệch và độ nhọn, MGF hữu hạn quanh 0, PGF, Markov, Chebyshev, Cauchy–Schwarz, Jensen, Cantelli | MGF Chuẩn/Exponential, cộng Poisson, điểm thi, nghịch đảo biến dương, thiếu MGF ở Cauchy/Lognormal |
| 35 | Hội tụ theo phân phối/xác suất/hầu chắc chắn, WLLN/SLLN, CLT i.i.d., De Moivre–Laplace, hiệu chỉnh liên tục, Poisson, Slutsky | Cỡ mẫu Chebyshev, tung xu, lỗi gói tin, mô hình phí bảo hiểm, khoảng trượt, Cauchy |

## Nguồn tham chiếu

- [Penn State STAT 414: Danh mục học liệu](https://online.stat.psu.edu/stat414/index) xác nhận các chủ đề Counting Techniques, Geometric and Negative Binomial Distributions, Exponential/Gamma, phân phối hai biến, đổi biến, MGF và CLT. Các mục chưa xác minh được URL bài cụ thể được dẫn tới danh mục, không gán số bài phỏng đoán.
- [Penn State STAT 414: Counting Techniques](https://online.stat.psu.edu/stat414/Lesson03).
- [Penn State STAT 414: Moment Generating Functions](https://online.stat.psu.edu/stat414/Lesson09).
- [Penn State STAT 414: Distributions of Two Discrete Random Variables](https://online.stat.psu.edu/stat414/Lesson17).
- [Penn State STAT 504: Introduction to Discrete Data](https://online.stat.psu.edu/stat504/Lesson01), các mục Nhị thức âm và Đa thức.
- [MIT 18.05 Spring 2022: Calendar](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/pages/calendar/) xác nhận Class 6b về LLN/CLT và Class 7 về phân phối đồng thời, độc lập, hiệp phương sai và tương quan.
- [Harvard STAT 110](https://stat110.hsites.harvard.edu/) xác nhận bản điện tử của *Introduction to Probability*, Joseph K. Blitzstein và Jessica Hwang, tại [probabilitybook.net](https://probabilitybook.net/).

## Các điều kiện đã rà

- Độc lập của cặp có mật độ được kiểm tra bằng phân tích thành tích hầu khắp nơi trên toàn miền, kể cả phần mật độ bằng 0. Tập giá trị lề có thể rời thành nhiều khoảng, nên không đòi hỏi một hình chữ nhật liền khối.
- Geometric phân biệt số lần thử với số thất bại, tránh lệch một đơn vị ở xác suất đuôi.
- Diễn giải Gamma thành thời gian chờ số sự kiện chỉ dùng cho hình dạng nguyên dương. Weibull phân biệt tham số thang đo với tốc độ Exponential.
- Tương quan cần hai phương sai dương hữu hạn. Luật kỳ vọng toàn phần cần khả tích, còn phương sai toàn phần và MMSE dùng mômen bậc hai hữu hạn.
- MGF dùng trong định lý duy nhất và sinh mômen phải hữu hạn trên một khoảng mở quanh 0. Độ lệch bằng 0 chưa suy ra đối xứng, độ nhọn không xếp hạng xác suất đuôi ở mọi ngưỡng.
- CLT i.i.d. yêu cầu phương sai dương hữu hạn. Thang dao động của trung bình khác với tốc độ sai số xấp xỉ. Các tính toán phí bảo hiểm và cỡ mẫu bằng Chuẩn được ghi rõ là xấp xỉ.

## Kiểm chứng tái lập

Script scripts/qa/xstk-classical-probability.py kiểm lại các ví dụ và bài tập bằng số hữu tỉ, SciPy, tích phân số, tổng PMF và công thức phân phối chuẩn. Kiểm tra bao gồm CDF bình phương Chuẩn, Jacobi tổng/tỷ lệ, CDF min/max trên và ngoài miền, phản ví dụ phụ thuộc, các mômen và kỳ vọng nghịch đảo, cận Cantelli, hiệu chỉnh liên tục và phân vị bảo hiểm.

Script cũng dùng MathJax kiểm cú pháp, dấu phân cách, giới hạn 38ex nội dòng và 34ex hiển thị. Lỗi chạy kiểm tra MathJax làm verifier thất bại, không bị bỏ qua. Kiểm tra trình duyệt chung chịu trách nhiệm xác nhận chiều rộng thực tế trong hộp lồng và thẻ ôn tập.

## Ranh giới

Không triển khai xác suất có điều kiện theo độ đo đầy đủ, kỳ vọng có điều kiện theo Radon–Nikodym, CLT cho dãy không cùng phân phối, chứng minh SLLN tổng quát hoặc lý thuyết quá trình ngẫu nhiên. Bản giới thiệu hàm đặc trưng chỉ phục vụ phản ví dụ Cauchy. Các bài 36–45 tiếp tục suy luận thống kê và Bayes.
