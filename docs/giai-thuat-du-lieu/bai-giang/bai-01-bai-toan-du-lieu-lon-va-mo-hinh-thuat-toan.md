---
course: giai-thuat-du-lieu
lecture: bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan
section: lecture
title: "Dữ liệu lớn & mô hình thuật toán"
prerequisites: ["do-phuc-tap","phan-tan","bam"]
lessonStatus: ready
description: "Khảo sát các bài toán dữ liệu lớn Bài 02–15, giới hạn tài nguyên và mô hình thuật toán. Bài toán tìm cặp tài liệu gần trùng, độ đo Jaccard, tiêu chí đánh giá và nguyên lý Bonferroni về giới hạn suy luận."
---

## Nội dung và kết quả buổi học

Bài học khảo sát các bài toán dữ liệu của Bài 02–15, từ đó xác định giới hạn tài nguyên và yêu cầu đối với thuật toán. Bài toán tìm cặp tài liệu gần trùng được phân tích qua biểu diễn, đặc tả, thuật toán xét mọi cặp và các tiêu chí đánh giá. Phần cuối giới thiệu nội dung học phần, sự chuẩn bị cần có và các giả thiết khi suy luận từ dữ liệu.

Sau buổi học, sinh viên có thể:

1. Nêu đầu vào, đầu ra và trở ngại của một bài toán dữ liệu.
2. Giải thích tính đúng của thuật toán xét mọi cặp và phân biệt các khía cạnh đánh giá lời giải.
3. Phân biệt kết quả tính toán với kết luận rút ra về dữ liệu. Tính kỳ vọng trùng dưới các giả thiết đã cho.

[Bộ trang chiếu Bài 01](#slides) dùng cùng dữ kiện và ký hiệu. Ghi chú mở rộng đặc tả, chứng minh, điều kiện chi phí và lời giải bài tập.

---

## Tổng hợp và tìm kiếm trên kho web

### Tính tổng kích thước trang web theo máy chủ

Kho thu thập web lưu các bản ghi gồm địa chỉ trang, kích thước và ngày thu thập. Máy chủ được xác định từ địa chỉ trang. Bài toán yêu cầu cộng kích thước các trang có trong kho thuộc cùng máy chủ, rồi trả một tổng cho mỗi máy chủ. Tổng này không phải lưu lượng truy cập hoặc dung lượng toàn bộ máy chủ.

Bốn bản ghi minh họa đầu ra có dạng rút gọn:

| Máy chủ | Kích thước trang (byte) |
|---|---:|
| a.vn | 40 |
| b.vn | 25 |
| a.vn | 15 |
| c.vn | 0 |

Kết quả là a.vn có $40+15=55$ byte, b.vn có 25 byte và c.vn có 0 byte. Đây chỉ là ví dụ nhỏ để kiểm tra phép tính, vì vậy không thể dùng nó để mô tả quy mô thật của một kho web.

Gọi $D$ là số byte của tệp bản ghi và $M$ là dung lượng bộ nhớ chính khả dụng. Khi $D>M$, cách nạp trọn tệp để xử lý không khả thi. $D$ đo dung lượng tệp đầu vào, không đồng nhất với tổng kích thước nội dung các trang được ghi trong tệp.

![Tệp bản ghi lớn trên đĩa không thể nạp trọn vào bộ nhớ chính hữu hạn](img/lec-01/kho-nhat-ky-bo-nho.svg)

Một hướng xử lý là đọc tuần tự và chỉ giữ tổng đang chạy theo máy chủ. Bảng tổng cũng phải vừa bộ nhớ vì số máy chủ phân biệt quyết định kích thước của bảng. Phần phân tích thuật toán sẽ dùng lại bốn bản ghi trên để kiểm tra cách cập nhật và chứng minh tính đúng. Nguồn bài toán: Stanford CS246 01-intro, trang chiếu 62 và bối cảnh truy cập ngoài bộ nhớ: MMDS 1.3.4, tr. 13 và BHK trang PDF 10.

### Đếm số lần xuất hiện của từng từ

Khi kho tài liệu được chia trên nhiều máy, thống kê toàn kho cần kết hợp dữ liệu ở nhiều nơi. Bài toán đếm từ nhận các tài liệu và trả một bảng từ–số lần xuất hiện. Nếu một từ xuất hiện nhiều lần trong một tài liệu, phải tính đủ các lần đó. Đầu ra khác với số tài liệu chứa từ.

![Từ w xuất hiện ở hai phần kho. Gom mọi tài liệu về một máy sẽ tập trung đường truyền và công việc tại máy đó](img/lec-01/ung-dung-tong-hop-phan-tan.svg)

Hình lấy một từ $w$ để biểu diễn một khóa có mặt ở nhiều phần kho, không gán số đếm cụ thể. Gom toàn bộ tài liệu về một máy phải truyền cả dữ liệu và dồn việc vào máy nhận. Nếu máy hoặc tác vụ lỗi, chạy lại phải tránh bỏ sót và đếm trùng.

Tính đóng góp tại nơi lưu dữ liệu rồi gom theo từ là hướng xử lý của Bài 02. Lượng dữ liệu trung gian, phân bố tải và cơ chế xử lý kết quả tác vụ chạy lại đều ảnh hưởng đến lời giải. Nguồn: MMDS 2.1–2.2.6 và slide Chương 2, trang 8–13 và 20.

### Tính điểm quan trọng của trang web

Thống kê từ mô tả nội dung kho. Khi một truy vấn khớp nhiều trang, hệ thống tìm kiếm còn phải sắp xếp các kết quả. Bài toán ở đây dùng cấu trúc liên kết để tính một điểm quan trọng cho mỗi trang, làm một tín hiệu hỗ trợ việc sắp xếp.

Đầu vào là đồ thị có hướng: đỉnh biểu diễn trang, cạnh biểu diễn liên kết. Đồ thị trong hình có ba đỉnh $y,a,m$: $y$ trỏ tới $y,a$. $a$ trỏ tới $y,m$. $m$ trỏ tới $a$. Khuyên tại $y$ biểu diễn liên kết từ trang đó về chính nó.

![Ba trang liên kết có hướng, trong đó phép đọc liên kết và cập nhật điểm được lặp lại để hỗ trợ sắp xếp kết quả](img/lec-01/ung-dung-xep-hang-web.svg)

Trong PageRank, điểm của một trang phụ thuộc điểm của các trang trỏ tới nó. Mỗi vòng cập nhật vì thế phải đọc liên kết và tính đóng góp cho nhiều trang. Một ma trận đặc cho mọi cặp trang còn có thể lãng phí bộ nhớ khi đồ thị thưa. Bài 03 phân tích biểu diễn, chi phí mỗi vòng, hội tụ và điều kiện dừng.

Điểm quan trọng theo liên kết không đo đầy đủ độ liên quan với một truy vấn. Hình chỉ nêu đầu ra cần tính, không gán trước các điểm hay thứ hạng. Nguồn: MMDS 5.1–5.2 và Link Analysis 1, trang 18–21, 48 và 53.

### Ưu tiên kết quả tìm kiếm theo chủ đề

Một điểm quan trọng dùng chung cho mỗi trang chưa phân biệt các chủ đề của truy vấn. “Jaguar” có thể chỉ loài báo, ô tô, hệ điều hành hoặc máy chơi trò chơi. Với chủ đề đã xác định là ô tô, yêu cầu là ưu tiên các trang về xe trong kết quả tìm kiếm.

![Truy vấn jaguar có bốn nghĩa. Với chủ đề ô tô đã biết, mục tiêu là ưu tiên các trang về xe](img/lec-01/ung-dung-truy-van-theo-chu-de.svg)

Đầu vào bổ sung là chủ đề cần ưu tiên, còn đầu ra là điểm và thứ tự đã xét đến chủ đề đó. Xác định chủ đề từ truy vấn hoặc ngữ cảnh là công việc riêng. Hình biểu diễn yêu cầu, không phải thứ hạng đã tính.

Lưu một bộ điểm cho toàn bộ trang web riêng với từng người dùng sẽ tốn quá nhiều bộ nhớ ở quy mô web. MMDS đề xuất dùng một số bộ điểm theo chủ đề thay vì một bộ đầy đủ cho mỗi người. Bài 04 học cách đưa chủ đề vào xếp hạng. Phương pháp không bảo đảm suy đoán đúng ý định của mọi người dùng. Nguồn: MMDS 5.3.1, tr. 195–196.

### Hạn chế liên kết rác trong xếp hạng

Điểm dựa trên liên kết còn có thể bị đẩy lên bởi một bên cố ý tạo nhiều trang hỗ trợ. Bài toán là hạn chế ảnh hưởng của các liên kết rác lên điểm hạng và kết quả tìm kiếm.

![Ba nhóm trang theo Hình 5.16, trong đó cụm cùng bên kiểm soát chứa đích t và các trang hỗ trợ liên kết qua lại](img/lec-01/ung-dung-lien-ket-thao-tung.svg)

Hình phân biệt trang ngoài tầm tác động, trang cho phép bên tạo rác đặt liên kết, và trang do bên đó sở hữu. Các trang có thể tác động trỏ đến đích $t$. $t$ trỏ đến từng trang hỗ trợ và mỗi trang hỗ trợ trỏ lại $t$. Đích và các trang hỗ trợ nằm trong cùng cụm kiểm soát.

Nhiều liên kết không nhất thiết đến từ nhiều nguồn độc lập. Chỉ xét số liên kết hoặc điểm truyền tới một trang chưa đủ để đánh giá độ tin cậy. Một hướng là dùng tập trang tin cậy ban đầu để điều chỉnh điểm, như TrustRank. Việc chọn tập tin cậy là yêu cầu riêng. Phương pháp không bảo đảm loại hết liên kết rác. Sơ đồ cũng không đủ chứng minh danh tính hoặc ý định của một người ngoài đời. Nguồn: MMDS 5.4.1–5.4.4, Hình 5.16 và Bài 04.

### Tìm các cặp tài liệu gần trùng

Ngay cả khi đã xử lý điểm hạng, kết quả tìm kiếm vẫn có thể chứa các bản sao chỉ khác một phần văn bản. Bài toán gần trùng nhận một kho tài liệu làm đầu vào và trả về các cặp có độ tương đồng đạt ngưỡng đã chọn.

“Gần trùng” ở đây xét phần văn bản chung, không chỉ việc hai tài liệu nói về cùng chủ đề. Biểu diễn tài liệu, độ đo tương đồng và ngưỡng phải được xác định trước khi đánh giá kết quả.

![Hai tài liệu có nhiều đoạn chung và một phần được sửa đổi. Trong toàn kho, cách so sánh trực tiếp phải xét mọi cặp tài liệu](img/lec-01/ung-dung-tai-lieu-gan-trung.svg)

Nét trong hai trang chỉ minh họa phần chung và phần sửa, không biểu diễn một số đo. Với $N$ tài liệu, so sánh tất cả cần xét $N(N-1)/2$ cặp không thứ tự. Khi $N=10^6$:

$$
\binom{10^6}{2}=499\,999\,500\,000\approx5\times10^{11}.
$$

Gần 500 tỷ là số cặp, không phải kết quả đo thời gian. Biểu diễn gọn giúp giảm chi phí mỗi lần so sánh, còn chọn ứng viên giúp giảm số cặp phải đối chiếu. Kiểm tra lại dữ liệu gốc có thể loại ứng viên sai, nhưng không khôi phục cặp đã bị bỏ sót. Bài 05–06 phân tích các phương pháp và xác suất này. Nguồn: MMDS 3.1–3.4 và Stanford CS246 03-lsh, trang chiếu 14.

### Tìm đoạn tài liệu bằng véc-tơ truy vấn

Tìm mọi cặp gần trùng xét cả kho. Một nhu cầu khác là cho một truy vấn rồi tìm các đoạn tài liệu gần truy vấn ấy. Mỗi đoạn tài liệu và truy vấn được mã hóa thành một dãy số, gọi là véc-tơ. Cùng một phép mã hóa được dùng cho cả đoạn và truy vấn, tạo các véc-tơ cùng số chiều.

Cho một quy tắc tính khoảng cách và số lượng $k$, đầu ra chính xác gồm $k$ đoạn có véc-tơ gần truy vấn nhất. Điều kiện là $1\le k\le N$, với $N$ là số đoạn. Cần chốt cách xử lý khi nhiều đoạn bằng khoảng cách. Độ gần theo véc-tơ không tự bảo đảm đúng về ngữ nghĩa.

![Một truy vấn dạng véc-tơ được đối chiếu với các đoạn tài liệu đã mã hóa để trả k đoạn gần nhất](img/lec-01/ung-dung-truy-hoi-vec-to.svg)

BIODS 271 dùng tình huống 10 tỷ véc-tơ, 3072 chiều, mỗi thành phần 32 bit. Quét hết kho cho mỗi truy vấn cần tính 10 tỷ khoảng cách. Mỗi khoảng cách còn sử dụng nhiều thành phần. Truy vấn mới phải thực hiện lại công việc này. Quy mô trên lấy từ nguồn, không phải số đo của học phần.

Bài 07 học tổ chức và nén véc-tơ để giảm chi phí truy vấn. Khi cho phép gần đúng, phải đánh giá chất lượng: độ thu hồi tại $k$ là tỷ lệ hàng xóm gần thật xuất hiện trong $k$ kết quả trả về, với tập chuẩn và quy ước hòa đã chốt. Các chi phí khác gồm độ trễ, bộ nhớ, xây dựng và cập nhật chỉ mục. Nguồn: BIODS 271 L12, trang PDF 16 cho bài toán truy hồi đoạn tài liệu, 17–18 cho quy mô và Princeton lớp 8, trang 2–5.

::: tip Tự kiểm tra
Tìm mọi cặp gần trùng và tìm $k$ mục gần một truy vấn khác nhau về đầu ra và số đối tượng phải xét như thế nào?
:::

---

## Xử lý dòng dữ liệu, lưu trữ và truy vấn

Các yêu cầu tìm kiếm tạo ra nhật ký cần phân tích. Nội dung văn bản và ảnh cần được lưu để đọc lại. Dữ liệu nằm trên đĩa còn phải được sắp xếp, tra cứu hoặc ghép từ nhiều bảng. Ba nhóm công việc này có các đầu ra khác nhau, lần lượt là mẫu và thống kê, dữ liệu được khôi phục và kết quả truy vấn. Chúng không nhất thiết là các bước nối tiếp của cùng một hệ thống.

### Giữ mẫu truy vấn và lọc thư đến

Máy tìm kiếm muốn nghiên cứu mức lặp truy vấn của người dùng. Mỗi bản ghi gồm người dùng, truy vấn và thời điểm. Nếu không thể lưu hết nhật ký, hệ thống cần chọn một mẫu vẫn cho phép nghiên cứu hành vi ấy. Lấy mẫu từng bản ghi riêng lẻ có thể làm mất những lần lặp cần đo. Chọn người dùng rồi giữ lịch sử truy vấn của họ là đơn vị lấy mẫu phù hợp với ví dụ này.

Bài toán lọc thư có đầu vào khác: một dòng thư kèm địa chỉ gửi và danh sách địa chỉ cho phép. Đầu ra phải nhận thư từ địa chỉ trong danh sách, bỏ thư ngoài danh sách. Nếu danh sách vượt bộ nhớ, mỗi thư có thể cần một lần tra cứu trên đĩa.

![Nhật ký truy vấn được lấy mẫu theo người dùng, còn thư đến được kiểm địa chỉ theo danh sách cho phép](img/lec-01/ung-dung-dong-truy-van.svg)

Giữ một tỷ lệ người dùng cố định không bảo đảm mẫu luôn vừa bộ nhớ khi lịch sử tăng. MMDS mục 4.2.4 xét điều chỉnh tỷ lệ để đáp ứng ngân sách. Với lọc thư, bộ lọc Bloom có thể loại nhanh địa chỉ chắc chắn không có trong danh sách. Trường hợp “có thể có” vẫn phải tra danh sách chính xác nếu yêu cầu chỉ nhận thành viên. Bảo đảm không loại nhầm phần tử đã chèn áp dụng cho bộ lọc chuẩn chỉ chèn và tra cứu, không xóa, với băm và trạng thái nhất quán. Thuộc danh sách cho phép không phải bằng chứng rằng mọi thư đều không phải thư rác. Nguồn: MMDS mục 4.2–4.3, trang 136–142 và Bài 08.

### Đếm người dùng và lượt truy cập gần đây

Nhật ký truy cập gồm mã người dùng và thời điểm của mỗi lượt. Hai đầu ra thường gặp là số người dùng khác nhau trong phạm vi đã chọn và số lượt truy cập trong một khoảng thời gian gần nhất. Một người quay lại tạo thêm lượt, nhưng không tạo thêm người dùng khác nhau.

![Mốc thời gian giúp tách lượt quá cũ khỏi cửa sổ gần đây. Hình cũng phân biệt việc đếm người khác nhau với đếm lượt](img/lec-01/ung-dung-thong-ke-cua-so.svg)

Lưu mọi mã đã gặp có thể vượt bộ nhớ khi số người dùng tăng. Truy vấn cửa sổ còn phải loại ảnh hưởng của bản ghi hết hạn. Chỉ lưu tổng số lượt từ đầu là chưa đủ để trả số lượt gần đây. Tuy nhiên, đếm tổng lượt từ đầu chỉ cần một bộ đếm. Không phải mọi thống kê trên dòng đều cần thuật toán xấp xỉ.

Bài 09 còn xét tần suất $f_j$ của khóa $j$ và mômen thứ hai $\sum_j f_j^2$, khác tổng số sự kiện $\sum_j f_j$. Đại lượng cần ước lượng và phạm vi thời gian quyết định trạng thái cần giữ. Các phương pháp có bảo đảm sai số khác nhau. Chẳng hạn, DGIM có cận xác định. Nguồn: MMDS mục 4.1.3, 4.4–4.7, trang 134–135, 142–159 và UMass CS514 Lecture 10 cho Count-Min.

Nếu có $k$ khóa phân biệt, ký hiệu $\sum_j f_j$ là cách viết gọn của $f_1+\cdots+f_k$, còn $\sum_j f_j^2$ là $f_1^2+\cdots+f_k^2$. Chỉ số $j$ chạy qua các khóa. Chẳng hạn hai khóa có tần suất 2 và 3 cho tổng 5, nhưng mômen thứ hai là $2^2+3^2=13$. Ta thực hiện phép bình phương trước rồi mới cộng.

### Lưu văn bản với ít dung lượng hơn

Một số đếm không đủ để tái tạo nhật ký. Nén văn bản đặt bài toán lưu một biểu diễn có thể giải mã thành đúng chuỗi đầu vào. Trong nén không mất thông tin, mọi ký hiệu và thứ tự đều phải được bảo toàn.

Chuỗi `aabaacabcabcb` trong ví dụ LZ của CMU có các cụm lặp như `ab` và `abc`. Sự lặp lại có thể được khai thác khi mã hóa, nhưng không được tùy ý bỏ phần lặp nếu bộ giải mã không biết phải khôi phục nó ở đâu.

![Dữ liệu mã cùng thông tin giải mã phải khôi phục đúng chuỗi aabaacabcabcb](img/lec-01/ung-dung-nen-van-ban.svg)

Dung lượng phải tính cả dữ liệu mã và thông tin phụ trợ cần giải mã. Không thể hứa mọi chuỗi đều ngắn hơn sau nén. Hình chỉ nêu yêu cầu khôi phục, không cho tỷ lệ nén hoặc bộ mã cụ thể. Nguồn: Nelson–Gailly Chương 3 và 9, CMU LZ, trang logic 11–14 và Bài 10–11.

### Giảm dung lượng ảnh với sai số cho phép

Đầu vào là ảnh cần lưu hoặc truyền. Với nén có mất thông tin, đầu ra sau giải mã được phép khác ảnh gốc nhưng phải đáp ứng tiêu chí chất lượng của ứng dụng. Các ứng dụng cần khôi phục nguyên vẹn ảnh phải dùng đặc tả khác.

![Minh họa định tính: nhiều mức sáng gần nhau được gộp thành ít mức đại diện hơn, làm mất phân biệt giữa các mức ban đầu](img/lec-01/ung-dung-nen-anh.svg)

Thay các mức sáng gần nhau bằng một mức đại diện làm mất thông tin. Đây là lượng tử hóa, một bước khác với phép biến đổi trong tuyến nén JPEG. Không thể suy ra tỷ lệ nén hoặc chất lượng từ hình định tính. Cần đo dung lượng và đánh giá ảnh khôi phục bằng tiêu chí đã chọn. Nguồn: Nelson–Gailly Chương 11, CMU lossy, trang logic 2–16, đặc biệt trang 3 và Bài 11.

### Sắp xếp tệp lớn theo khóa

Đĩa trao đổi dữ liệu với bộ nhớ theo khối và mỗi khối có thể chứa nhiều bản ghi. Nén giảm dung lượng nhưng chưa xác định các khối cần đọc để xử lý. Các bài toán tiếp theo áp dụng cho tệp trên đĩa, không đòi tệp nhất thiết đã nén.

Sắp xếp nhận một tệp bản ghi chưa có thứ tự và tạo tệp chứa đủ các bản ghi ấy theo khóa tăng dần. Khóa là thuộc tính xác định thứ tự. Phải giữ cả những bản ghi có khóa lặp. Sắp xếp không đồng nghĩa với loại trùng.

![Các vạch biểu diễn thứ tự tương đối của khóa trước và sau sắp xếp, trong khi bộ nhớ chỉ giữ được một phần tệp](img/lec-01/ung-dung-sap-xep-ngoai.svg)

Khi tệp vượt bộ nhớ, không thể sắp nó như một mảng nằm trọn trong bộ nhớ. Có thể sắp từng phần vừa bộ nhớ, rồi trộn các dãy đã có thứ tự. Chi phí cần tính cả đọc và ghi khối, không chỉ số so sánh. Nguồn: Database System Concepts, ấn bản 7 (viết tắt DSC), Chương 15, trang chiếu 17–23 và Bài 12.

### Tìm hồ sơ giảng viên theo mã hoặc lương

Với bảng hồ sơ giảng viên `instructor`, truy vấn theo mã `ID` trả hồ sơ đúng mã. Truy vấn theo khoảng lương `salary` trả tất cả hồ sơ có lương trong khoảng. Phải xác định có lấy hai đầu mút hay không. Hình dùng đoạn kín và không gán mức lương cụ thể.

![Tra một mã trả hồ sơ tương ứng, còn tra đoạn lương kín trả đủ hồ sơ có lương trong đoạn](img/lec-01/ung-dung-tra-cuu-khoa.svg)

Quét cả bảng cho mỗi yêu cầu đọc nhiều dữ liệu không thuộc kết quả. Chỉ mục phù hợp giúp chọn khối cần đọc nhưng phải được xây dựng và cập nhật khi dữ liệu thay đổi. Nếu nhiều hồ sơ cùng mức lương thỏa điều kiện, phải trả đủ. Băm và cây có thứ tự không có cùng khả năng hỗ trợ truy vấn khoảng. Nguồn: DSC Chương 14, trang chiếu 4, 6, 10–16 và Bài 13.

### Tìm tài liệu chứa đồng thời hai từ khóa

Bài toán nhận một kho tài liệu cùng hai từ khóa và trả về tập tài liệu chứa cả hai từ. Một tài liệu chỉ chứa một từ không thỏa điều kiện. Bài toán này chọn tập tài liệu, chưa sắp xếp theo độ liên quan.

![Hai từ khóa phải cùng xuất hiện trong mỗi tài liệu kết quả](img/lec-01/ung-dung-tim-tu-khoa.svg)

Đọc lại toàn bộ kho cho mỗi yêu cầu tốn công. Chỉ mục đảo lưu ánh xạ từ mỗi từ khóa đến danh sách tài liệu chứa nó. Giao hai danh sách cho điều kiện chứa cả hai từ, còn hợp hai danh sách cho điều kiện chứa ít nhất một từ. Nguồn: DSC Chương 31, trang 13–16 và trang chiếu 14 và Bài 14.

### Tìm đối tượng giao vùng trên bản đồ

Đầu vào gồm các đối tượng hình học và vùng truy vấn $Q$. Đầu ra là các đối tượng có phần giao với $Q$, kể cả nằm hoàn toàn trong $Q$. Kiểm trực tiếp mọi hình trên bản đồ có thể tốn nhiều công.

![Q giao hộp bao A và B của hai nhóm đối tượng, vì vậy cả hai nhóm cần được kiểm tra tiếp](img/lec-01/ung-dung-truy-van-khong-gian.svg)

Hộp bao là hình chữ nhật chứa các đối tượng của một nhóm. Trong sơ đồ, $A$ và $B$ là hộp bao, không phải các đối tượng kết quả. Vì $Q$ giao cả hai, chỉ đi một nhánh có thể bỏ sót ứng viên. Ngược lại, hộp bao giao $Q$ chưa chứng minh đối tượng thật giao $Q$. Hình không vẽ đối tượng thật nên chưa thể liệt kê kết quả cuối cùng. Nguồn: DSC Chương 24, trang chiếu 17, 21–24, Auburn, trang PDF 10–13 và Bài 14.

### Ghép sinh viên với các môn đã đăng ký

Bảng `student` lưu thông tin sinh viên, còn `takes` lưu các lượt đăng ký học. Ghép theo mã sinh viên `ID` tạo thông tin sinh viên kèm từng môn đã đăng ký. Đầu ra phải gồm mọi cặp bản ghi trùng mã. Một sinh viên đăng ký nhiều môn có thể tạo nhiều kết quả.

![Hồ sơ sinh viên ghép với từng lượt đăng ký cùng mã để trả sinh viên kèm môn đã đăng ký](img/lec-01/ung-dung-noi-bang.svg)

Trong nguồn, `student` có 5000 bản ghi trong 100 khối và `takes` có 10.000 bản ghi trong 400 khối. Ví dụ ở Bài 15 dùng bộ nhớ $M_{\rm khối}=20$ khối. Cả hai bảng đều vượt bộ nhớ. Quét bảng đăng ký lại cho từng sinh viên sẽ đọc nhiều lần cùng dữ liệu. Các phương pháp nối cần tái sử dụng khối mà vẫn trả đủ các cặp. Nguồn: DSC Chương 15, trang chiếu 24 cho quy mô, 28 cho nối theo khối và 40 cho ví dụ bộ nhớ và kịch bản bộ nhớ của Bài 15.

::: tip Tự kiểm tra
Phân biệt điều phải giữ khi lấy mẫu theo người dùng, khôi phục văn bản, lọc ứng viên vùng và trả các cặp trùng mã. Mỗi đầu ra đặt một điều kiện đúng khác nhau.
:::

---

## Phân tích thuật toán xử lý dữ liệu lớn

Các bài toán trên đĩa cho thấy hai yêu cầu khác nhau: trả đúng kết quả và thực hiện được trong ngân sách tài nguyên. Tìm cặp tài liệu gần trùng còn buộc ta phân biệt một cặp được tìm thấy với toàn bộ các cặp cần tìm.

### Bài toán và cách biểu diễn

Các bản sao của một trang web thường giữ nội dung chính nhưng thay tên máy chủ hoặc liên kết. So sánh bằng nhau từng ký tự không nhận ra đủ những cặp này. Bài toán tìm gần trùng xét phần văn bản được chia sẻ. Nó không kết luận hai tài liệu cùng ý nghĩa hay có hành vi sao chép trái phép.

Mỗi tài liệu được biểu diễn bằng tập các đoạn ký tự liên tiếp cùng độ dài. Cả kho dùng cùng quy tắc chuẩn hóa. Một đoạn chỉ xuất hiện một lần trong tập dù lặp nhiều lần trong văn bản. Trong phần này, các tập đã được tạo và đều không rỗng. Bài 05 phân tích cách tạo chúng.

Độ tương đồng Jaccard của hai tập hữu hạn có hợp không rỗng là

$$J(S,T)=\frac{|S\cap T|}{|S\cup T|}.$$

Tỷ lệ nằm trong $[0,1]$. Nó bằng $1$ khi hai tập không rỗng bằng nhau, bằng $0$ khi chúng rời nhau.

::: example MMDS Ví dụ 3.1
Hình 3.1 cho hai phần tử chỉ thuộc $S$, ba phần tử chung và ba phần tử chỉ thuộc $T$. Do đó

$$J(S,T)=\frac{3}{2+3+3}=\frac38.$$

Với ngưỡng $\tau$ đã cho, cặp này đạt yêu cầu khi và chỉ khi $\tau\le3/8$. Không chọn ngưỡng bằng cách nhìn riêng cặp ví dụ này.
:::

![Hai tập có ba phần tử chung trong tám phần tử của hợp.](img/lec-01/danh-gia-jaccard.svg)

Nguồn: MMDS §3.1.1–3.1.2, tr. 74–75 và §3.2.1. MMDS slide Chương 3, trang 15–17 và Stanford CS246 03-lsh, trang 14–18 thống nhất về nhu cầu biểu diễn và giảm số cặp.

### Đặc tả đầu vào và đầu ra

Đầu vào gồm số nguyên $N\ge0$, các tập hữu hạn không rỗng $C_1,\ldots,C_N$ và ngưỡng $\tau\in[0,1]$. Tập $C_i$ biểu diễn tài liệu thứ $i$. Đầu ra phải là

$$R=\{(i,j):1\le i<j\le N,\ J(C_i,C_j)\ge\tau\},$$

với mỗi cặp xuất hiện đúng một lần. Điều kiện $i<j$ loại so sánh một tài liệu với chính nó và tránh trả cả hai thứ tự của cùng cặp. Khi $N<2$, kết quả rỗng.

Chỉ trả các cặp đạt ngưỡng là chưa đủ nếu còn bỏ sót cặp khác cũng đạt ngưỡng. Nếu cho phép gần đúng, phải nêu sai lệch nào được chấp nhận. Tập rỗng nằm ngoài miền đầu vào đang xét. Không tự gán giá trị cho $\frac{0}{0}$.

| Thành phần | Nội dung trong bài toán |
|---|---|
| Đặc tả | Trả đúng tập $R$ theo Jaccard và ngưỡng đã cho |
| Biểu diễn | Tập đoạn ký tự, có thể lưu thành danh sách đã sắp, không lặp |
| Thuật toán | Duyệt các cặp, kiểm tương đồng, xuất cặp đạt ngưỡng |
| Cài đặt | Kiểu phần tử, phép so sánh, cách đọc tệp, cách kiểm ngưỡng |
| Kết quả thực nghiệm | Các cặp cụ thể và số đo trong thiết lập chạy đã công bố |

Một lần chạy đúng không chứng minh mọi đầu vào, và một lần chạy nhanh không chứng minh một cận tiệm cận.

### Thuật toán xét mọi cặp và tính đúng

Giả sử phép kiểm Jaccard cho kết quả chính xác. Có thể duyệt hai danh sách đã sắp để đếm giao và hợp bằng hai con trỏ. Bài 05 phân tích thao tác đó.

```text
nếu N < 2:
    kết thúc với kết quả rỗng
cho i = 1,...,N−1:
    cho j = i+1,...,N:
        tính chính xác J(Cᵢ, Cⱼ)
        nếu J(Cᵢ, Cⱼ) ≥ τ:
            xuất cặp (i, j)
```

Với $N=2$, $C_1=S$, $C_2=T$ trong ví dụ, hai vòng chỉ xét $(1,2)$. Phép kiểm cho $J(C_1,C_2)=\frac{3}{8}$. Nếu $\tau\le3/8$, thuật toán xuất $(1,2)$ rồi dừng. Nếu $\tau>\frac{3}{8}$, nó kết thúc với kết quả rỗng. Như vậy đầu ra là $\{(1,2)\}$ hoặc $\varnothing$ theo yêu cầu ngưỡng.

Kết quả được xuất dần, không bắt buộc lưu mọi cặp đã xét hoặc toàn bộ đầu ra trong bộ nhớ. Chi phí ghi đầu ra vẫn tồn tại.

::: proof Tính đúng và điều kiện dừng
Mệnh đề: với đầu vào hợp lệ và phép kiểm tương đồng chính xác, thuật toán xuất đúng $R$, mỗi cặp một lần.

Bất biến: sau mỗi bước, các cặp đã xuất gồm đúng các cặp đạt ngưỡng trong phần đã xét.

Ban đầu chưa xét và chưa xuất cặp nào nên bất biến đúng. Giả sử nó đúng trước một bước. Cặp mới chưa được xét trước đó. Nếu đạt ngưỡng, thuật toán xuất cặp ấy. Nếu không, nó không xuất. Kết quả trước giữ nguyên nên bất biến tiếp tục đúng và không có cặp trùng lặp.

Hai vòng xét mỗi cặp $i<j$ đúng một lần rồi dừng sau $N(N-1)/2$ cặp. Khi kết thúc, phần đã xét là toàn bộ miền cặp. Bất biến cho kết quả bằng $R$. Với $N<2$, miền cặp và kết quả đều rỗng.
:::

![Ba trong sáu cặp đã được xét và kết quả hiện tại đúng với phần đã xét.](img/lec-01/danh-gia-tinh-dung.svg)

Chứng minh giả định phép kiểm ngưỡng chính xác. Cài đặt dấu phẩy động phải được kiểm tra ở gần ngưỡng. Không suy từ giả mã rằng mọi cách tính số đều giữ nguyên quyết định.

::: exercise Tự kiểm đặc tả
Nếu vòng trong bắt đầu từ $j=1$ thay vì $j=i+1$, thuật toán vi phạm phần nào của đặc tả?
:::

::: solution
Nó có thể trả cặp tự so sánh $(i,i)$ và cả hai thứ tự $(i,j),(j,i)$ khi đạt ngưỡng. Chúng không thỏa điều kiện $i<j$.
:::

Nguồn bài toán và cách xét mọi cặp: MMDS Chương 3, tr. 73. Giả mã và chứng minh là cách hình thức hóa trực tiếp phép duyệt hữu hạn đó.

---

## Đánh giá lời giải theo từng khía cạnh

Tính đúng đã được chứng minh cho thuật toán xét mọi cặp. Tính khả thi còn phụ thuộc tài nguyên và cách phục vụ công việc.

| Nhóm | Tiêu chí | Đại lượng hoặc điều kiện |
|---|---|---|
| Kết quả | Tính đúng | Đáp ứng đặc tả trên mọi đầu vào hợp lệ |
| Kết quả | Chất lượng gần đúng | Thước đo sai lệch và điều kiện bảo đảm |
| Tài nguyên | Khối lượng tính toán | Số thao tác theo kích thước đầu vào |
| Tài nguyên | Bộ nhớ làm việc | Dung lượng lớn nhất cần giữ đồng thời |
| Tài nguyên | Đọc ghi và lượt quét | Khối chuyển giữa đĩa–bộ nhớ, số lần đọc toàn dữ liệu |
| Tài nguyên | Dữ liệu mạng | Lượng dữ liệu trao đổi giữa máy |
| Tài nguyên | Dung lượng lưu trữ | Dữ liệu đã lưu cùng phần phụ trợ |
| Vận hành | Độ trễ truy vấn | Thời gian từ nhận đến trả kết quả |
| Vận hành | Xây dựng | Thời gian, bộ nhớ để tạo cấu trúc trước truy vấn |
| Vận hành | Cập nhật | Công việc phản ánh một thay đổi dữ liệu |

Không cộng trực tiếp số phép toán, dung lượng và sai số thành một giá trị nếu chưa định nghĩa mục tiêu tối ưu.

### Khối lượng tính toán

Với $N\ge2$ tài liệu, số lần kiểm là $\binom N2=N(N-1)/2$. Với $N=10^6$, có $499\,999\,500\,000$ cặp. Đây là phép đếm, không phải số đo tốc độ. Khi số tài liệu tăng gấp đôi, số cặp tăng gần bốn lần.

Giả sử mỗi tập được lưu thành danh sách tăng dần không lặp, có không quá $L$ phần tử, và so sánh hai phần tử có chi phí đơn vị. Hai con trỏ duyệt một cặp trong $O(|C_i|+|C_j|)\subseteq O(L)$. Phần xét toàn kho có cận trên trường hợp xấu $O(N^2L)$, chưa tính tạo và sắp các tập.

![Bốn tài liệu tạo sáu cặp. Khi số tài liệu tăng, số cặp tăng theo bậc hai.](img/lec-01/ung-dung-tai-lieu-gan-trung.svg)

Coi một lần kiểm là hằng số che mất tác động của độ dài tài liệu. Giảm số cặp kiểm cũng chưa xác định toàn bộ chi phí: còn tạo ứng viên và xuất kết quả. Nếu $R$ chứa bậc hai cặp, riêng xuất đầy đủ từng cặp đã cần bậc hai thao tác. Nguồn: MMDS Chương 3, tr. 73, Stanford 03-lsh, trang 14 và Bài 05.

### Bộ nhớ làm việc

Bộ nhớ làm việc là dung lượng lớn nhất phải giữ đồng thời, gồm trạng thái, dữ liệu đang dùng và bộ đệm. Nó khác kích thước toàn bộ đầu vào và đầu ra đã ghi.

Để ghép hồ sơ sinh viên với lượt đăng ký theo mã sinh viên, hai bảng chiếm 100 và 400 khối, còn ngân sách ví dụ chỉ có 20 khối bộ nhớ. Không bảng nào nạp trọn được. Xử lý từng phần phải chừa chỗ cho các bộ đệm và đầu ra.

![Hai bảng 100 và 400 khối vượt ngân sách 20 khối bộ nhớ.](img/lec-01/danh-gia-bo-nho.svg)

Nguồn quy mô: DSC Chương 15, trang chiếu 24 và ngân sách 20 khối từ Bài 15. Chia phần không đổi yêu cầu trả mọi cặp trùng mã, nhưng có thể làm tăng số lần đọc lại.

### Đọc ghi và số lượt quét

Chi phí đọc ghi đếm khối chuyển giữa đĩa và bộ nhớ. Một lượt quét đọc hết dữ liệu một lần. Với tệp $F$ khối chưa có trong bộ đệm, một lượt đọc cần $F$ lần chuyển khối. Nếu cũng ghi ra $F$ khối, phần chuyển dữ liệu của lượt đó là $2F$.

Sắp ngoài tạo các dãy đã sắp rồi trộn. Các lượt trộn đọc ghi lại cùng dữ liệu. Số bộ đệm giới hạn số dãy trộn đồng thời.

![Sắp ngoài đọc tệp, xử lý trong bộ đệm, ghi dãy và tiếp tục đọc ghi ở lượt trộn sau.](img/lec-01/danh-gia-doc-ghi.svg)

Hai phương pháp có số so sánh gần nhau vẫn có thể khác số khối đọc ghi. Truy cập tuần tự và ngẫu nhiên cũng có chi phí thực khác nhau. Số khối chưa phải số giây. Nguồn: DSC Chương 15, trang chiếu 17–23 và MMDS §1.3.4.

### Dữ liệu truyền qua mạng

Chi phí mạng ở đây đo lượng dữ liệu trao đổi giữa máy. Với đếm từ, mỗi máy đếm tại nơi giữ phần kho rồi gửi số đếm theo từ để cộng lại. Khi từ lặp nhiều, cách này có thể gửi ít dữ liệu hơn chuyển toàn bộ văn bản.

![Hai máy đếm từ w tại chỗ rồi gửi số đếm để tổng hợp toàn kho.](img/lec-01/danh-gia-truyen-mang.svg)

Đếm đúng đòi hỏi mỗi đóng góp được tính đúng một lần, kể cả khi tác vụ chạy lại. Tổng lượng truyền không tự quyết định thời gian hoàn thành: lệch tải, máy chậm và các vòng đồng bộ còn gây chờ. Lượng dữ liệu mạng chỉ đếm chuyển giữa máy, còn chi phí truyền thông trong MMDS §2.5 có thể tính cả dữ liệu vào ra của tác vụ. Nguồn: MMDS §2.2.4–2.2.6, §2.5 và Stanford 01-intro, trang 67–69.

### Độ trễ truy vấn

Độ trễ là khoảng từ lúc nhận truy vấn đến lúc trả kết quả, gồm chờ, truy cập, tính toán và trả lời. Với tìm $k$ đoạn tài liệu gần véc-tơ truy vấn, chỉ đếm phép tính khoảng cách chưa mô tả đủ thời gian chờ.

![Độ trễ trải từ nhận truy vấn qua các công đoạn đến trả kết quả.](img/lec-01/danh-gia-do-tre.svg)

Thông lượng là số truy vấn hoàn tất trong một đơn vị thời gian, không phải độ trễ từng truy vấn. Khi đo cần công bố tập truy vấn, phần cứng, số luồng, tải và chất lượng. Độ rộng các công đoạn trong hình không biểu diễn số đo. Nguồn: Bài 07, mục 1 và BIODS 271 và Princeton lớp 8–9.

### Chi phí xây dựng chỉ mục

Xây chỉ mục tổ chức kho thành cấu trúc phục vụ các truy vấn về sau. Cần tính thời gian và bộ nhớ lớn nhất lúc xây, không chỉ dung lượng chỉ mục hoàn tất.

![Kho véc-tơ được dùng để xây chỉ mục, sau đó nhiều truy vấn dùng lại chỉ mục này.](img/lec-01/danh-gia-xay-dung.svg)

Với tìm véc-tơ, phương pháp có thể cần tạo đồ thị hoặc học bộ mã. Báo cáo phải nói công việc nào được tính. Trả truy vấn nhanh vẫn có thể tốn nhiều thời gian chuẩn bị. Lợi ích còn phụ thuộc cách dùng lại. Nguồn: Bài 07, mục 1 và các trục đánh giá từ Princeton lớp 8–9.

### Chi phí cập nhật

Chi phí cập nhật gồm sửa dữ liệu và cấu trúc phụ thuộc. Khi lương của giảng viên thay đổi, phải sửa bản ghi gốc lẫn mục chỉ dẫn theo lương để truy vấn khoảng dùng giá trị mới.

![Thay đổi lương tác động tới cả bản ghi và chỉ mục, vì vậy tra cứu cần hai cấu trúc nhất quán.](img/lec-01/danh-gia-cap-nhat.svg)

Nếu chỉ sửa bản ghi, truy vấn có thể bỏ sót mục đã chuyển vào khoảng hoặc lấy mục đã chuyển ra. Sơ đồ mô tả trạng thái sau cập nhật hoàn tất, không quy định giao thức giao dịch. Có thể đo thao tác, khối đọc ghi hay thời gian cho mỗi cập nhật. Với dòng còn xét khả năng theo kịp tốc độ đến. Nguồn duy trì chỉ mục: DSC Chương 14, trang chiếu 4, 10–11 và các mục chèn/xóa. Nguồn yêu cầu theo kịp dòng: MMDS §4.1.

### Dung lượng lưu trữ

Dung lượng lưu trữ gồm dữ liệu đã lưu và phần phụ trợ. Với văn bản nén không mất thông tin, phải tính dòng mã và mọi thông tin giải mã thực sự cần lưu. Bản khôi phục phải bằng nguyên văn bản ban đầu.

![Bản lưu gồm mã và thông tin giải mã cần thiết để khôi phục đúng văn bản.](img/lec-01/danh-gia-luu-tru.svg)

Thông tin phụ tùy phương pháp: có từ điển được tái dựng, không cần lưu toàn bộ cạnh mã. Nếu có chỉ mục truy cập, phải tính cả nó. Dung lượng bản lưu khác bộ nhớ làm việc khi nén/giải nén. Không phải mọi đầu vào đều nén ngắn hơn. Với ảnh cho phép mất thông tin, báo dung lượng cùng sai số tái tạo. Nguồn: Nelson–Gailly Chương 3, 8–9, 11, CMU về nén LZ và Bài 10–11.

### Chất lượng kết quả gần đúng

Với véc-tơ truy vấn $q$, gọi $N_k(q)$ là tập $k$ hàng xóm gần nhất theo khoảng cách đã chọn và quy tắc phá hòa cố định. Giả sử $1\le k\le N$ và kết quả $\widehat N_k(q)$ cũng gồm $k$ định danh phân biệt. Độ thu hồi tại $k$ là

$$\operatorname{recall@}k(q)=\frac{|\widehat N_k(q)\cap N_k(q)|}{k}.$$

::: example Ba trong năm hàng xóm thật
Tập đúng $\{a,b,c,d,e\}$ và tập trả về $\{c,d,e,f,g\}$ có ba phần tử chung. Độ thu hồi tại năm là $\frac{3}{5}$. Hai mục $f,g$ không bù được hai hàng xóm thật $a,b$ bị thiếu.
:::

![Hai tập năm phần tử có ba phần tử chung, còn a,b bị thiếu và f,g nằm ngoài tập đúng.](img/lec-01/danh-gia-do-thu-hoi.svg)

Đây là ví dụ chạy tay từ Bài 07, không phải đo hiệu năng. Chất lượng đo trên tập truy vấn không tự là bảo đảm xác suất cho mọi đầu vào. Các bài toán dùng sai số khác nhau: độ thu hồi, sai số tái tạo, cận xác định hoặc cận xác suất với giả thiết tương ứng. Nguồn: Bài 07, mục 1 và hình độ thu hồi và Princeton lớp 8–9.

### Giảm ứng viên và nguy cơ bỏ sót

Một hướng giảm đối chiếu là chọn cặp ứng viên rồi tính Jaccard chính xác chỉ trên các cặp ấy. Gọi $A$ là tập ứng viên, $R$ là tập cặp đúng theo đặc tả. Sau hậu kiểm chính xác, đầu ra là

$$\widehat R=A\cap R.$$

Suy ra $\widehat R\subseteq R$: mọi cặp trả ra đều đạt ngưỡng. Muốn có $\widehat R=R$, còn cần $R\subseteq A$, tức không bỏ sót cặp đúng khi chọn ứng viên.

![Cặp được chọn đi qua kiểm tra chính xác, còn cặp bị bỏ qua sẽ không xuất hiện lại ở hậu kiểm.](img/lec-01/danh-gia-ung-vien.svg)

Băm nhạy cảm cục bộ (LSH) ở Bài 06 xây cơ chế chọn ứng viên với bảo đảm xác suất dưới giả thiết cụ thể. Không gọi hậu kiểm là đầy đủ chỉ vì các phép kiểm đã thực hiện đều chính xác. Chi phí tạo ứng viên và kích thước đầu ra cũng phải được tính. Nguồn: MMDS Chương 3, tr. 73 và §3.4.

::: exercise Tự kiểm đánh giá
Bộ lọc chưa bảo đảm không bỏ sót, nhưng bước sau kiểm Jaccard chính xác cho mọi ứng viên. Có thể cam kết trả đúng tập $R$ không?
:::

::: solution
Chưa thể. Hậu kiểm loại ứng viên không đạt ngưỡng nhưng không xét cặp ngoài $A$. Cần bảo đảm $R\subseteq A$ để giữ đặc tả chính xác, hoặc công bố yêu cầu chất lượng gần đúng được chấp nhận.
:::

Các nhóm phương pháp của học phần xử lý những giới hạn này. Mỗi phương pháp phải gắn với đầu ra, điều kiện áp dụng và mô hình chi phí cụ thể.

---

## Nội dung học phần và phương pháp sẽ học

Các yêu cầu vừa phân tích dẫn tới năm nhóm phương pháp: xử lý phân tán, tìm tương đồng, duy trì trạng thái dòng, nén dữ liệu, tổ chức lưu trữ và truy vấn.

Học phần Giải thuật nền tảng của Khoa học dữ liệu, mã UET.DSE2053, có 3 tín chỉ. Đề cương quy định bốn chuẩn đầu ra học phần (CLO): giải thích nguyên lý và giải thuật. Phân tích để lựa chọn. Thiết kế, triển khai và đánh giá. Tự học và xử lý dữ liệu có trách nhiệm.

![Bài 01 là nền chung cho năm nhóm bài: phân tán và xếp hạng, tương đồng và tìm gần, dòng và cửa sổ, nén, cùng lưu trữ và truy vấn](img/lec-01/ban-do-hoc-phan.svg)

Năm nhóm được học liền nhau theo thứ tự dưới đây. Mỗi bài gắn phương pháp với một đầu ra và các thuộc tính cần đánh giá.

| Bài | Phương pháp và cấu trúc sẽ học | Ứng dụng và thuộc tính cần đánh giá |
|---:|---|---|
| 02 | MapReduce, ánh xạ, nhóm, rút gọn, bộ kết hợp và phân vùng | Tổng hợp kho phân tán, bảo toàn đóng góp, truyền thông và phối hợp khôi phục tác vụ |
| 03 | PageRank, phép lặp, xử lý nút cụt và bẫy nhện | Xếp hạng web, điều kiện hội tụ, tiêu chuẩn dừng và chi phí mỗi vòng |
| 04 | PageRank theo chủ đề, TrustRank, khối lượng rác, HITS | Chủ đề và liên kết thao túng, giả thiết tín hiệu, phạm vi đồ thị, giới hạn diễn giải |
| 05 | Shingling, độ đo Jaccard, MinHash | Gần trùng, dưới hoán vị đều, xác suất trùng MinHash bằng độ tương đồng Jaccard |
| 06 | Băm nhạy cảm cục bộ (LSH), phân dải và khuếch đại | Tạo ứng viên, xác suất ứng viên, bỏ sót và chi phí đối chiếu |
| 07 | HNSW, lượng tử hóa tích (PQ), IVF-PQ | Truy vấn véc-tơ, độ thu hồi, độ trễ, bộ nhớ, xây dựng, phân biệt phép đo với bảo đảm lý thuyết |
| 08 | Lấy mẫu theo khóa, lấy mẫu hồ chứa, bộ lọc Bloom | Dòng truy vấn, đơn vị và phân phối mẫu, cập nhật, sai số một phía có điều kiện |
| 09 | Flajolet–Martin, phác thảo Count-Min, AMS, DGIM, suy giảm mũ | Thống kê dòng, đại lượng, cửa sổ, loại sai số và trạng thái, DGIM có cận xác định |
| 10 | Huffman tĩnh, Huffman thích nghi, mã hóa số học | Nén không mất thông tin, độ dài mã, dữ liệu phụ trợ, khôi phục đúng |
| 11 | LZ77, LZ78, LZW, JPEG dựa trên biến đổi cô-sin rời rạc (DCT) | Mẫu lặp và ảnh, đồng bộ từ điển, trạng thái, phân biệt LZ không mất thông tin với lượng tử hóa ảnh |
| 12 | Sắp xếp trộn ngoài bộ nhớ, chọn thay thế | Sắp tệp lớn, dãy có thứ tự, số lượt đọc/ghi và bộ đệm |
| 13 | B-Tree, B+-Tree, băm tĩnh, chỉ mục bitmap | Tra khóa/khoảng, loại truy vấn, dung lượng, xây dựng và cập nhật |
| 14 | Chỉ mục đảo, R-tree, kd-tree, ball tree, Z-order | Từ khóa và không gian, cắt nhánh, độ đầy đủ của lọc và tinh lọc |
| 15 | Nối vòng lặp theo bản ghi/khối/chỉ mục, nối sắp xếp–trộn, nối băm và Grace Hash | Kết nối bảng, đúng mọi cặp khớp, ngân sách bộ nhớ, lệch phân hoạch, đọc/ghi |

MapReduce là mô hình xử lý, Jaccard là độ đo, còn chỉ mục là cấu trúc dữ liệu. Spark và Faiss là phần mềm hỗ trợ khi bài tương ứng sử dụng, có vai trò khác với các thuật toán và cấu trúc dữ liệu. IVF-PQ kết hợp chỉ mục phân vùng với mã lượng tử hóa tích.

Năm nhóm theo thứ tự học là Bài 02–04, 05–07, 08–09, 10–11 và 12–15. Tiên quyết có các nhánh: Bài 01 đến 02–03–04. Đến 05–06–07. Đến 08–09. Đến 10–11. Đến 12–13–14. Bài 12–13 hỗ trợ Bài 15, còn Bài 02 cung cấp cách tính phân tán khi cần. Nhóm sau không mặc nhiên cần toàn bộ nhóm trước.

### Ý tưởng của các nhóm phương pháp

**Phân tán và xếp hạng.** Với kho văn bản trên nhiều máy, MapReduce tạo cặp khóa–giá trị, gom cùng khóa rồi kết hợp các giá trị. Trong đếm từ, khóa là từ và giá trị là số lần xuất hiện, vì vậy có thể cộng cục bộ các giá trị cùng khóa trước khi truyền. Mỗi đóng góp phải được tính đúng một lần, kể cả khi tác vụ chạy lại. PageRank giải bài toán khác: cập nhật điểm trang qua liên kết và một phân phối dịch chuyển. Dịch chuyển giúp xác định mô hình hội tụ khi xử lý đúng nút cụt. Bài 04 dùng trang mẫu theo chủ đề để ưu tiên kết quả, hoặc trang tin cậy làm nguồn tín hiệu TrustRank. HITS tách điểm trang trung tâm dẫn tới nguồn tốt và điểm trang thẩm quyền được trang trung tâm tốt dẫn tới. Khối lượng rác là tín hiệu so sánh hạng thông thường với tín hiệu tin cậy. Điểm liên kết không tự chứng minh chất lượng nội dung. Nguồn: MMDS 2.2 và 5.1–5.5.

**Tương đồng và truy vấn véc-tơ.** Tập các đoạn ký tự liên tiếp biểu diễn một tài liệu. MinHash lấy giá trị nhỏ nhất của tập sau một hoán vị. Nhiều hoán vị cho chữ ký gọn. Với hoán vị đều, xác suất hai giá trị MinHash bằng nhau bằng Jaccard. Băm nhạy cảm cục bộ (LSH) dùng các phần của chữ ký để chọn cặp ứng viên. Với hai tập có Jaccard $\frac{3}{8}$ đã xét, cặp chỉ được hậu kiểm nếu bộ lọc đã chọn nó. Tính Jaccard chính xác sau lọc không bảo đảm không bỏ sót.

![Tập đoạn ký tự tạo chữ ký MinHash, LSH chọn cặp ứng viên rồi hậu kiểm bằng Jaccard](img/lec-01/chuong-trinh-cap-ung-vien.svg)

Khi đầu vào là một véc-tơ truy vấn, HNSW tổ chức đồ thị lân cận nhiều tầng để tìm từ tầng thưa xuống tầng chi tiết. Lượng tử hóa tích (PQ) chia véc-tơ thành các đoạn, lưu mã tâm đại diện cho từng đoạn để giảm dung lượng và tính khoảng cách qua mã. IVF-PQ kết hợp phân vùng với PQ. Chỉ tìm một số vùng có thể bỏ sót hàng xóm thật. Hai hướng này giảm những khoản chi phí khác nhau: PQ quét đầy đủ vẫn chấm điểm mọi mã. Độ thu hồi $\frac{3}{5}$ ở ví dụ trước phải được báo cùng độ trễ và bộ nhớ. Nguồn: MMDS 3.1–3.4 và Bài 07, Princeton 8–9, BIODS 271 L12.

![HNSW chọn các véc-tơ cần chấm điểm qua liên kết, còn PQ biểu diễn từng véc-tơ bằng mã đại diện để giảm dung lượng](img/lec-01/chuong-trinh-vec-to.svg)

**Dòng dữ liệu.** Lấy mẫu theo khóa chọn một nhóm người dùng rồi giữ các truy vấn của họ, còn lấy mẫu hồ chứa giữ mẫu đều theo vị trí bản ghi. Đơn vị mẫu quyết định kết quả đại diện cho cái gì. Bộ lọc Bloom biểu diễn tập đã chèn bằng mảng bit và các hàm băm. Bloom chuẩn, không xóa bit và dùng cùng các hàm băm, không báo vắng nhầm phần tử đã chèn. Kết quả có thể có vẫn cần tra danh sách gốc để xác minh.

![Mẫu giữ các truy vấn được chọn, còn Bloom trả chắc chắn không có hoặc cần xác minh](img/lec-01/chuong-trinh-mau-loc.svg)

Flajolet–Martin theo dõi dấu hiệu hiếm ở giá trị băm để ước lượng số khóa khác nhau, chẳng hạn số người dùng. Count-Min chia sẻ nhiều hàng bộ đếm qua băm để ước lượng tần suất một khóa. AMS ước lượng tổng bình phương tần suất, phản ánh mức tập trung của dòng. DGIM gom bit 1 thành các nhóm có kích thước và mốc thời gian để trả lời truy vấn trong cửa sổ gần đây. Suy giảm mũ giảm dần trọng số sự kiện cũ thay vì loại chúng ngay tại một ranh giới. Đây là các đại lượng khác nhau, có giả thiết và sai số khác nhau. Vì thế, một cấu trúc gọn chưa chắc trả lời được mọi loại truy vấn. Nguồn: MMDS 4.2–4.7 và UMass Count-Min và Bài 08–09.

**Nén.** Với chuỗi `aabaacabcabcb` đã xét, có thể khai thác phân phối ký hiệu hoặc các đoạn lặp. Huffman tạo mã tiền tố: không từ mã nào là tiền tố của từ mã khác. Mô hình tĩnh cố định thống kê, còn mô hình thích nghi cập nhật theo ký hiệu đã đọc. Mã hóa số học thu hẹp một khoảng để biểu diễn cả chuỗi. LZ77 tham chiếu đoạn đã xuất hiện trong cửa sổ, còn LZ78 mở rộng từ điển các cụm. Với LZW, hai phía cùng xây từ điển để sử dụng mã của các mục từ. Những cách nén không mất thông tin phải khôi phục nguyên chuỗi, kể cả thứ tự ký hiệu. JPEG được học dùng biến đổi cô-sin rời rạc (DCT) và lượng tử hóa, tức làm tròn hệ số về các mức đại diện. Do đó, bước lượng tử hóa có thể làm mất chi tiết ảnh. Không thể kết luận lợi ích lưu trữ chỉ từ độ dài mã mà bỏ dữ liệu phụ trợ. Nguồn: Nelson–Gailly 3–5, 8–11 và CMU nén.

**Lưu trữ và truy vấn.** Sắp xếp trộn ngoài bộ nhớ tạo các dãy có thứ tự vừa bộ nhớ rồi trộn chúng. Chọn thay thế dùng hàng đợi để tạo dãy ban đầu. Cây B/B+ phân chia miền khóa theo thứ tự để hỗ trợ tìm khóa và khoảng. Băm tĩnh định vị nhóm cho khóa bằng nhau. Bitmap dùng dãy bit đánh dấu bản ghi thuộc một giá trị. Chỉ mục đảo ánh xạ từ sang các tài liệu chứa từ. R-tree nhóm các hộp bao. Kd-tree chia không gian theo tọa độ. Ball tree nhóm các điểm trong vùng cầu. Z-order mã hóa vị trí thành một thứ tự một chiều. Các biểu diễn ấy phù hợp những phép lọc khác nhau, không mặc nhiên thay thế nhau.

Với hai bảng sinh viên và đăng ký đã xét, nối vòng lặp dò bản ghi hoặc khối của bảng kia. Nối theo chỉ mục dùng khóa để tra. Nối trộn đi qua hai đầu vào có thứ tự. Nối băm gom khóa vào nhóm rồi kiểm các cặp khớp. Grace Hash phân hoạch cả hai bảng ra ngoài bộ nhớ trước khi nối từng cặp phần, cần xét phần lớn và lệch phân bố. Cả hai bảng không vừa bộ nhớ không có nghĩa chỉ dùng một lần quét là đủ. Nguồn: DSC 14–15, 24, 31 và Bài 12–15.

Các mô tả trên dùng để nhận diện vai trò của phương pháp. Điều kiện áp dụng, giả mã, chứng minh và ví dụ chạy đầy đủ được học ở bài tương ứng. Chương trình không yêu cầu thuộc danh sách tên trước khi bắt đầu.

---

## Kiến thức, kỹ năng và cách học

Năm nhóm thuật toán dùng các phần kiến thức nền khác nhau. Việc chuẩn bị gồm xác định nội dung cần ôn, vận dụng nó vào một bài toán và tạo sản phẩm có thể kiểm tra. Đề cương yêu cầu cả tự học, hợp tác và trách nhiệm dữ liệu. Những năng lực này thể hiện trong cách trình bày lời giải và báo cáo.

### Kiến thức đầu vào và phần cần ôn

Tiên quyết chính thức là UET.CS1058. Nền chung gồm lập trình, đọc giả mã, dùng cấu trúc dữ liệu và phân tích độ phức tạp. Toán rời rạc, xác suất, đại số tuyến tính và cơ sở dữ liệu được ôn theo nhóm bài.

| Nhóm bài | Kiến thức và cách dùng |
|---|---|
| Phân tán và xếp hạng | Khóa–giá trị để gom đóng góp, đồ thị và ma trận để truyền điểm |
| Tương đồng và tìm gần | Tập hợp để tính Jaccard, véc-tơ và khoảng cách để tìm đoạn tài liệu gần truy vấn |
| Dòng dữ liệu | Xác suất để lấy mẫu, kỳ vọng để phân tích thống kê |
| Nén | Cây và phân phối ký hiệu để tạo mã, chuỗi và từ điển để biểu diễn đoạn lặp |
| Lưu trữ và truy vấn | Bản ghi, khối, cây và băm để tổ chức nơi cần đọc |

Không yêu cầu biết sẵn các thuật toán sẽ học. Chẳng hạn, để hiểu điều kiện chọn cặp gần trùng, trước hết cần giải thích phép đếm giao và hợp của hai tập.

![Hai tập đoạn ký tự có phần giao gồm ba phần tử, phần hợp gồm tám phần tử](img/lec-01/danh-gia-jaccard.svg)

Với hai tập không rỗng $S,T$ của ví dụ MMDS 3.1, $|S\cap T|=3$, $|S\cup T|=8$, nên $J(S,T)=\frac{3}{8}$. Giao đếm các đoạn có trong cả hai tài liệu. Hợp đếm mỗi đoạn xuất hiện ở ít nhất một tài liệu đúng một lần. Điều kiện chọn là $J(S,T)\ge\tau$, nên cặp này được chọn khi $\tau\le3/8$. Nếu chưa lý giải được hai phép đếm, phần cần ôn là tập hợp, chưa phải cơ chế MinHash.

### Kỹ năng cần tạo thành sản phẩm

Đặc tả nêu miền đầu vào, kết quả và bảo đảm. Chạy tay theo dõi trạng thái ở một đầu vào cụ thể. Chứng minh giải thích đúng và đủ cho mọi đầu vào hợp lệ. Phân tích chi phí xác định phép toán, dữ liệu phải giữ hoặc khối cần đọc trong mô hình đã chọn.

![Đặc tả cặp đạt ngưỡng dẫn tới vết chạy và lập luận, sau đó kiểm mã và phân tích chi phí](img/lec-01/hoc-tap-san-pham.svg)

Với $N=2$, $C_1=S$, $C_2=T$, thuật toán xét mọi cặp chỉ thăm $(1,2)$ một lần. Trạng thái kết quả ban đầu là $R=\varnothing$. Nếu $\frac{3}{8}\ge\tau$ thì thêm $(1,2)$, nếu không thì giữ rỗng. Vết này giúp đối chiếu giả mã với đặc tả. Để kết luận cho mọi $N$, vẫn cần bất biến trên các cặp đã xét như ở phần phân tích. Kiểm thử còn cần $N<2$ và các ngưỡng biên hợp lệ. Trường hợp $J=\tau$ phải được chọn vì đặc tả dùng dấu $\ge$.

Nền thực hành gồm Python hoặc C++, đọc tài liệu chuyên ngành tiếng Anh và làm việc với giả mã. Mã chạy đúng trên một ví dụ chưa thay thế chứng minh. Một lần chạy nhanh chưa chứng minh cận tiệm cận. Các sản phẩm này cụ thể hóa CLO1–CLO3.

### Báo cáo chất lượng và hiệu năng

Ở ví dụ truy vấn véc-tơ, chuẩn đúng là $\{a,b,c,d,e\}$ còn kết quả trả về là $\{c,d,e,f,g\}$. Giao gồm ba phần tử, nên độ thu hồi tại 5 là $\frac{3}{5}$. Đây là ví dụ khác với hai tập đoạn ký tự dùng tính Jaccard.

![Chuẩn đúng và tập hàng xóm trả về đều có năm phần tử, giao ba phần tử nên độ thu hồi bằng ba phần năm](img/lec-01/danh-gia-do-thu-hoi.svg)

Một báo cáo thực nghiệm phải nêu dữ liệu, tập truy vấn, chuẩn đúng, tham số, thiết bị và cách đo. Độ thu hồi cần đi cùng độ trễ và bộ nhớ khi so các cách tìm gần. Ví dụ $\frac{3}{5}$ minh họa cách đọc kết quả, không phải số đo hiệu năng của hệ thống nào. Phương pháp có độ trễ nhỏ hơn nhưng bỏ sót nhiều hơn chưa thể được coi là phù hợp hơn nếu chưa nêu yêu cầu chất lượng. Nguồn: Bài 07 và CLO3.

### Tự học, hợp tác và trách nhiệm

Tự học bắt đầu từ điểm chưa giải thích được. Ví dụ, khi đọc quy trình chọn ứng viên, cần nêu được vì sao hậu kiểm không cứu cặp đạt ngưỡng nhưng không được chọn: cặp đó không xuất hiện trong đầu vào của bước hậu kiểm. Một phản ví dụ như vậy cụ thể hơn việc chỉ ghi chưa hiểu bộ lọc.

Khi làm nhóm, ghi nguồn thuật toán, dữ liệu và phần đóng góp của từng người. Báo cáo cả trường hợp bỏ sót, sai số và kết quả không như dự kiến. Chỉ chia sẻ dữ liệu được phép dùng trong bài học. Những hành vi này thực hiện chuẩn đầu ra CLO4 về tự học, phản biện, hợp tác và trách nhiệm.

Jaccard chỉ đo độ tương đồng theo biểu diễn đã chọn. Tìm đúng cặp đạt ngưỡng chưa đủ chứng minh có hành vi sao chép. Với dữ liệu lớn, nhiều mẫu trùng còn có thể phát sinh ngẫu nhiên. Mô hình hồ sơ lưu trú tiếp theo cho một phép tính cụ thể về hiện tượng ấy.

---

## Mô hình ngẫu nhiên và giới hạn suy luận

Trách nhiệm khi phân tích dữ liệu còn nằm ở cách diễn giải đầu ra. Liệt kê đúng mọi mẫu trùng chưa cho biết chúng có bất thường hay có thể xuất hiện ngẫu nhiên. Phần này đặt bài toán lưu trú, xác định cách dữ liệu phát sinh, tính xác suất và số trùng trung bình rồi giới hạn kết luận.

### Bài toán tìm mẫu lưu trú trùng

MMDS mục 1.2.3, trang 7–8 xét việc tìm dấu hiệu hoạt động phối hợp từ hồ sơ khách sạn. Đầu vào gồm các bản ghi người, ngày và khách sạn. Mẫu tìm kiếm là hai người cùng ở một khách sạn trong hai ngày khác nhau. Khách sạn có thể khác giữa hai ngày vì điều kiện trùng được xét riêng trong từng ngày.

![Cặp người u,v trùng khách sạn trong ngày s và ngày t, nhưng khách sạn giữa hai ngày có thể khác nhau](img/lec-01/suy-luan-mau-luu-tru.svg)

Hình chỉ ký hiệu một mẫu cần tìm, không tạo hồ sơ quan sát mới. Khó khăn nằm ở số cặp người và bộ ngày rất lớn: một mẫu hiếm trong mỗi phép thử vẫn có thể xuất hiện nhiều khi xét mọi khả năng. Đầu ra tìm kiếm cần được phân biệt với kết luận về ý định của một người.

### Mô hình lưu trú không phối hợp

Mô hình nền giả sử không có phối hợp, với các tham số nguồn:

| Ký hiệu | Ý nghĩa | Giá trị |
|---|---|---:|
| $P$ | Số người | $10^9$ |
| $T$ | Số ngày quan sát | $1000$ |
| $H$ | Số khách sạn | $10^5$ |
| $q$ | Xác suất một người lưu trú trong một ngày | $0{,}01$ |

Mỗi người quyết định lưu trú độc lập giữa mọi người và mọi ngày. Nếu đi, người đó chọn đều một trong $H$ khách sạn: mỗi khách sạn có xác suất $1/H$ khi đã lưu trú. Độc lập nghĩa lựa chọn của một người/ngày không làm thay đổi phân phối lựa chọn của người/ngày khác.

Các điều kiện ấy là giả thiết mô hình, chưa phải kết quả được xác nhận từ hồ sơ thật. Nguồn dùng 100 chỗ mỗi khách sạn để đặt quy mô $H$. Phép tính không áp thêm sức chứa cứng làm các lựa chọn phụ thuộc.

### Xác suất trùng trong một phép thử

Cố định một cặp người và một ngày. Hai người đều lưu trú với xác suất $q^2$, nhờ độc lập giữa người. Khi cả hai đã đi, cố định khách sạn của người thứ nhất. Người thứ hai chọn trùng với xác suất $1/H$.

::: derivation
Xác suất trùng trong một ngày là:

$$
p=q^2\frac1H=\frac{(0{,}01)^2}{10^5}=10^{-9}.
$$

Cố định thêm một ngày khác. Nhờ độc lập giữa ngày, xác suất trùng trong cả hai ngày là:

$$
p^2=10^{-18}.
$$
:::

![Cặp người phải trùng trong ngày s và cả ngày t. Nhờ giả thiết độc lập giữa các ngày, ta có thể nhân hai xác suất](img/lec-01/suy-luan-hai-ngay.svg)

Hai khách sạn ở hai ngày không phải trùng nhau. Xác suất $1/H$ nói về hai người trong cùng một ngày, không phải cùng người trong hai ngày.

### Đơn vị đếm và số phép thử

Một phép thử chọn một cặp người không thứ tự và một cặp ngày không thứ tự. Có $\binom P2$ cách chọn người và $\binom T2$ cách chọn ngày, nên tổng số phép thử là tích $\binom P2\binom T2$.

![Một cặp người và một cặp ngày xác định một phép thử trùng khách sạn trong từng ngày](img/lec-01/phep-thu-va-duong-tinh-gia.svg)

Với mỗi phép thử, đặt biến chỉ báo bằng 1 nếu mẫu trùng xảy ra và bằng 0 nếu không. Gọi $X$ là tổng các chỉ báo. $X$ đếm các biến cố **cặp người–cặp ngày**, không đếm cặp người phân biệt. Nếu một cặp người trùng trong ba ngày, họ đóng góp $\binom32=3$ biến cố vào $X$.

### Kỳ vọng số trùng

Kỳ vọng là giá trị trung bình theo mô hình qua các lần sinh dữ liệu, không phải số đếm quan sát được trên một kho cụ thể. Mỗi chỉ báo bằng 1 với xác suất $p^2$, nên có kỳ vọng $p^2$.

::: derivation
Tính tuyến tính kỳ vọng cho:

$$
\mathbb E[X]=\binom P2\binom T2p^2
=\binom{10^9}{2}\binom{1000}{2}10^{-18}
=249\,749{,}99975025.
$$

Làm tròn được $249\,750$. MMDS dùng $\binom n2\approx \frac{n^2}{2}$ và được khoảng $250\,000$.
:::

Các phép thử có thể chia sẻ người hoặc ngày. Tuyến tính kỳ vọng không đòi hỏi chúng độc lập. Giả thiết độc lập được dùng khi tính $q^2$ và $p^2$, không phải khi cộng kỳ vọng.

Nguồn diễn giải kết quả bằng số cặp người, còn công thức trên đếm biến cố cặp người–cặp ngày. Để đếm cặp người phân biệt phải gộp các bộ ngày của cùng một cặp. Đây là vấn đề đơn vị đếm. Chênh lệch giữa $250\,000$ và $249\,750$ ở phép tính lại do xấp xỉ số tổ hợp.

### Diễn giải có điều kiện

MMDS gọi cảnh báo về số mẫu trùng ngẫu nhiên là nguyên lý Bonferroni phi hình thức. Cần ước lượng mức trùng trong dữ liệu ngẫu nhiên trước khi coi kết quả tìm được là bằng chứng. Phần này không trình bày định lý hiệu chỉnh nhiều kiểm định.

| Kết quả | Điều có thể kết luận |
|---|---|
| Thuật toán liệt kê đủ mẫu trùng | Đầu ra đáp ứng điều kiện tìm kiếm |
| Mô hình không phối hợp cho kỳ vọng khoảng $249\,750$ | Mẫu trùng ngẫu nhiên có thể tạo nhiều kết quả cần xem xét |
| Một cặp có tên trong đầu ra | Chưa xác định xác suất họ có phối hợp từ kỳ vọng nền |

Kết luận về hoạt động phối hợp còn phụ thuộc mô hình thay thế, tỷ lệ nền và tính phù hợp của giả thiết. Thuật toán chạy đúng không xác nhận giả thiết độc lập. Tương tự, Jaccard đạt ngưỡng chưa đủ chứng minh có hành vi sao chép.

::: tip Tự kiểm tra
Giải thích nơi dùng độc lập và nơi dùng tuyến tính kỳ vọng. Phân biệt $X$ với số cặp người phân biệt. Trường hợp ba ngày ở trên cho một cách kiểm tra đơn vị đếm.
:::

---

## Đặc tả, chi phí và chuẩn bị Bài 02

Với cặp tài liệu gần trùng, đặc tả yêu cầu đúng, đủ và không lặp. Mô hình chi phí đếm số cặp và chi phí mỗi lần đối chiếu. Mô hình dữ liệu giới hạn ý nghĩa suy ra từ độ tương đồng. Năm nhóm bài của học phần phát triển phương pháp theo các giới hạn đã nhận diện.

Bài 02 dùng đếm từ trên kho phân tán. Kết quả phải chứa đúng số lần xuất hiện của từng từ trong toàn kho. Đếm cục bộ rồi gom theo khóa phải bảo toàn mọi đóng góp và tránh tính lặp, kể cả khi tác vụ chạy lại.

Để chuẩn bị, đọc MMDS Chương 2. Ôn khóa–giá trị, phép nhóm, tính kết hợp và giao hoán. Phép cộng số nguyên không tràn cho phép đổi cách nhóm nếu mỗi đóng góp được tính đúng một lần. Bản thân tính kết hợp không loại đóng góp trùng. Các bài tập ngay sau đây quay lại mô hình lưu trú để thay đổi quy mô và tiêu chuẩn trùng, rồi chuyển sang tập mặt hàng.

---

## Bài tập từ MMDS

Hai bài từ MMDS, mục 1.2.4, trang 8 dùng mô hình ngẫu nhiên để xét số mẫu trùng. Bài 1.2.1 thay riêng từng điều kiện của hồ sơ lưu trú. Bài 1.2.2 chuyển từ ngày lưu trú sang lượt mua và tập mặt hàng. Mỗi bài yêu cầu tính số mẫu trùng rồi xác định điều có thể suy ra từ kết quả.

| Thành phần lời giải | Nội dung phải xác định |
|---|---|
| Đơn vị và số phép thử | Một phép thử chọn những người, ngày hoặc lượt nào |
| Xác suất trùng | Điều kiện trùng và giả thiết để tính xác suất |
| Kỳ vọng số trùng | Cộng đóng góp của các phép thử, phân biệt biến cố với cặp người |
| Diễn giải | Kết luận trong mô hình và điều chưa suy ra từ mẫu trùng |

### Bài 1.2.1: thay đổi quy mô quan sát

::: exercise
Dùng mô hình hồ sơ lưu trú ở mục 1.2.3 của nguồn. Số cặp bị báo nghi vấn thay đổi thế nào nếu áp dụng **từng thay đổi riêng**, các số khác giữ nguyên?

(a) Tăng số ngày quan sát lên $2000$.

(b) Tăng số người được quan sát lên $2$ tỷ. Do đó có $200\,000$ khách sạn.

(c) Chỉ báo một cặp nếu họ cùng ở một khách sạn vào cùng thời điểm trong ba ngày khác nhau. Khách sạn có thể khác giữa các ngày vì điều kiện trùng được xét riêng trong từng ngày.

Sản phẩm: với mỗi phần, ghi số phép thử, xác suất một phép thử, kỳ vọng và diễn giải theo mô hình.
:::

::: hint
Nếu cần trùng trong $k$ ngày khác nhau, đơn vị đếm gồm cặp người và **bộ $k$ ngày**. Kỳ vọng số biến cố là:

$$
\binom P2\binom Tk\left(\frac{q^2}{H}\right)^k.
$$

Dùng $k=2$ cho (a), (b). $k=3$ cho (c). Với (b), cả $P$ và $H$ đều thay đổi. Phân biệt giá trị dùng tổ hợp với xấp xỉ của sách.
:::

::: solution
Cơ sở là $249\,749{,}99975025$ biến cố. Sách làm tròn bằng xấp xỉ lũy thừa thành khoảng $250\,000$.

**(a)** Chỉ thay $T=2000$:

$$
\mathbb E[X_a]=\binom{10^9}{2}\binom{2000}{2}10^{-18}
=999\,499{,}9990005\approx999\,500.
$$

Tỷ lệ so cơ sở là $\binom{2000}{2}/\binom{1000}{2}=\frac{3998}{999}$, gần 4 nhưng không đúng bằng 4. Xấp xỉ $\binom T2\approx \frac{T^2}{2}$ của sách cho khoảng $1\,000\,000$.

**(b)** Thay $P=2\times10^9$, $H=2\times10^5$:

$$
\mathbb E[X_b]=\binom{2\times10^9}{2}\binom{1000}{2}
\left(5\times10^{-10}\right)^2
=249\,749{,}999875125\approx249\,750.
$$

Số cặp người gần gấp 4, còn xác suất trùng trong hai ngày giảm đúng 4 lần. Kỳ vọng gần như không đổi. Xấp xỉ của sách cho khoảng $250\,000$. Giá trị dùng tổ hợp không hoàn toàn bằng cơ sở.

**(c)** Giữ quy mô gốc, chọn bộ ba ngày:

$$
\mathbb E[X_c]=\binom{10^9}{2}\binom{1000}{3}10^{-27}
=0{,}0830834999169165\approx0{,}0831.
$$

Yêu cầu ba ngày làm kỳ vọng trùng ngẫu nhiên xuống dưới 1 trong mô hình. Điều đó không có nghĩa không thể xuất hiện trùng và không chứng minh danh tính của một cặp. Xấp xỉ $\binom T3\approx \frac{T^3}{6}$ cho khoảng $0{,}0833$.
:::

### Đổi quy mô và đổi tiêu chuẩn trùng

Hai thay đổi (a), (b) đều bắt đầu từ mô hình gốc. Với (a), số người và khách sạn không đổi. Với (b), số người và khách sạn cùng tăng, còn thời gian quan sát không đổi. Vì vậy phải tách ảnh hưởng lên số phép thử khỏi ảnh hưởng lên xác suất mỗi phép thử.

![Hai nhánh bắt đầu từ mô hình gốc: tăng thời gian lên 2000 ngày hoặc tăng lên 2 tỷ người và 200 000 khách sạn](img/lec-01/bai-tap-quy-mo.svg)

Phần (c) giữ quy mô gốc nhưng yêu cầu trùng trong cả ba ngày. Theo mô hình MMDS mục 1.2.3, trang 7, khách sạn có thể khác giữa các ngày. Trong mỗi ngày, hai người phải ở cùng khách sạn. Đơn vị đếm chuyển từ cặp ngày sang bộ ba ngày, và điều kiện xảy ra của một phép thử cũng thay đổi.

![Một cặp người được kiểm trên bộ ba ngày khác nhau, cần trùng khách sạn trong từng ngày](img/lec-01/bai-tap-ba-ngay.svg)

### Bài 1.2.2: trùng tập mặt hàng

Bài lưu trú chọn một cặp ngày, còn bài mua hàng chọn một lượt của mỗi người. Hai lượt không buộc có cùng số thứ tự.

| Thành phần | Hồ sơ lưu trú | Tập mặt hàng |
|---|---|---|
| Đối tượng | Cặp người | Cặp người |
| Quan sát được chọn | Cặp ngày | Một lượt của mỗi người |
| Điều kiện trùng | Cùng khách sạn trong từng ngày | Hai tập 10 mặt hàng bằng nhau |

Một giỏ là một tập: đổi thứ tự mua không tạo thêm tập mới. Mô hình nền giả sử các lượt độc lập và chọn đều tập 10 mặt hàng. Đây là điều kiện tính toán, không phải mô tả đã được xác nhận cho hành vi mua hàng thực.

::: exercise
Có thông tin mua sắm của $100$ triệu người. Mỗi người đi siêu thị $100$ lần trong một năm và mua $10$ trong $1000$ mặt hàng được bán.

Đề đặt giả thuyết rằng một cặp khủng bố sẽ mua đúng cùng một tập $10$ mặt hàng vào một thời điểm trong năm. Nếu tìm các cặp người đã mua cùng một tập mặt hàng, có thể kỳ vọng những người tìm được thực sự là khủng bố không?

Chú thích 3 của nguồn yêu cầu chấp nhận giả thuyết làm việc ấy, không bàn việc khủng bố có nhất thiết mua như vậy. Đây là giả thuyết của bài tập, không phải căn cứ gán nhãn người trong dữ liệu thực.

Sản phẩm: đơn vị đếm, mô hình nền, xác suất, kỳ vọng và câu trả lời có điều kiện.
:::

![Một lượt mua của người thứ nhất và một lượt mua của người thứ hai được so sánh theo tập mười mặt hàng](img/lec-01/ung-dung-trung-gio-hang.svg)

::: hint
Trong mô hình nền, mỗi lượt chọn đều một tập 10 phần tử trong 1000 mặt hàng, độc lập với các lượt khác. Với hai người khác nhau, có bao nhiêu cách chọn một lượt của người thứ nhất và một lượt của người thứ hai? Các mặt hàng trong một giỏ là một tập, không phải dãy có thứ tự.
:::

::: solution
Đặt $Y$ là số cặp lượt mua của hai người khác nhau có cùng tập mặt hàng. Có $\binom{10^8}{2}$ cặp người và $100^2$ cặp lượt cho mỗi cặp người. Không chỉ so lượt cùng số thứ tự giữa hai người.

Có $\binom{1000}{10}$ tập mặt hàng. Sau khi cố định tập của lượt thứ nhất, xác suất lượt thứ hai chọn đúng tập ấy là $1/\binom{1000}{10}$. Theo tuyến tính kỳ vọng:

$$
\mathbb E[Y]=\frac{\binom{10^8}{2}\,100^2}{\binom{1000}{10}}
\approx0{,}000189818469
\approx1{,}90\times10^{-4}.
$$

Kỳ vọng trùng ngẫu nhiên rất nhỏ dưới mô hình chọn đều, độc lập. Theo tiêu chí Bonferroni phi hình thức và giả thuyết làm việc của đề, việc tìm mẫu trùng này không bị ngập bởi các trùng ngẫu nhiên như ví dụ khách sạn.

Có thể làm rõ ý nghĩa “ít trùng” mà không suy danh tính: vì $Y$ là số nguyên không âm, chỉ báo $\mathbf1_{\{Y\ge1\}}\le Y$. Lấy kỳ vọng hai vế được $\Pr(Y\ge1)\le\mathbb E[Y]$. Xác suất xuất hiện ít nhất một trùng ngẫu nhiên trong mô hình vì thế không vượt khoảng $1{,}90\times10^{-4}$.

Tuy nhiên, xác suất có điều kiện một cặp là khủng bố sau khi quan sát trùng không được xác định chỉ từ $\mathbb E[Y]$ và giả thuyết nguồn. Còn cần tỷ lệ nền và mô hình cho nhóm cần tìm. Lượt mua thực cũng không nhất thiết độc lập hay chọn đều. Đó là giới hạn khi chuyển câu trả lời của bài tập sang kết luận thực tế.
:::

---

## Đọc thêm và tài liệu nguồn

MMDS mục 1.1 phân biệt mô hình thống kê với bản tóm tắt phục vụ truy vấn. BHK Chương 1–2 trình bày nền tảng về dữ liệu cao chiều.

- **Đề cương học phần:** nguồn xác định mã UET.DSE2053, chuẩn đầu ra, tiên quyết và thứ tự 15 bài. Xem [chỉ mục học phần](/giai-thuat-du-lieu/).
- **Mining of Massive Datasets, ấn bản 3:** Chương 1 cho chi phí và bài tập. Chương 2, 5, 3, 4 cho phân tán, xếp hạng, tương đồng và dòng. Nội dung và các sơ đồ tương ứng được StudyHub hệ thống hóa và biên soạn độc lập. Tham khảo tác giả tại [MMDS](http://www.mmds.org).
- **Stanford CS246:** bài mở đầu trang chiếu 62 cho tổng kích thước. 03-lsh trang 14 cho quy mô so cặp.
- **Blum–Hopcroft–Kannan, Foundations of Data Science:** Chương 1–2, đặc biệt trang PDF 9–12, cho giới hạn mô hình bộ nhớ và định hướng đọc thêm.
- **BIODS 271 và Princeton COS 597A:** các trang đã dẫn trong ứng dụng véc-tơ. Tài liệu và bài báo HNSW/PQ theo Bài 07 dùng để học cơ chế chi tiết.
- **Nelson–Gailly, The Data Compression Book:** Chương 3–5, 8–9, 11. Slide CMU LZ và lossy theo Bài 10–11.
- **Database System Concepts, ấn bản 7:** slide Chương 14–15, 24 và nội dung Chương 31 theo Bài 12–15. UMass CS514 Lecture 10 bổ sung Count-Min trong Bài 09.

[Quay về bộ trang chiếu](#slides).
