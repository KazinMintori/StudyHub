# Báo cáo biên soạn và rà soát Vật lý đại cương 1, 2

Cập nhật ngày 29/10/2026. Đây là báo cáo đang hoàn thiện. Đã có đủ bản soạn của 20 chương Vật lý đại cương 1 và 24 chương Vật lý đại cương 2. Việc nghiệm thu toàn bộ nội dung theo từng yêu cầu và việc dọn dẹp cuối cùng vẫn chưa kết thúc.

## Kết quả có bằng chứng

| Hạng mục | Kết quả đã kiểm tra | Giới hạn của kết luận |
| --- | --- | --- |
| Phạm vi môn học | Vật lý 1 gồm chương 1–20. Vật lý 2 gồm chương 21–44, có vật lý hiện đại. | Trạng thái sẵn sàng trong danh mục không tự chứng minh nội dung đầy đủ. |
| Cấu trúc nội dung đang sử dụng | 44 bài, các trang chủ đề, nguồn được chèn vào bài, ảnh, Cheatsheet và liên kết khái niệm đều được kiểm kê. Không phát hiện đường dẫn ảnh, khái niệm hoặc trang Wiki bị thiếu trong lượt này. | Tệp tồn tại chưa chứng minh nội dung tệp chính xác. |
| Mục lý thuyết và ví dụ | Đã tìm được nơi hiển thị của 290 mục lý thuyết và 492 ví dụ có số hiệu. | Chưa dùng kết quả này để xác nhận từng câu, giả thiết và bước suy luận. |
| Câu hỏi khi giảng | 280 câu tự kiểm tra có nơi đến trong Notes. Những tiêu đề không ghi số đã được phân biệt với trường hợp thiếu câu hỏi. | Việc đối chiếu toàn bộ lựa chọn và lời giải của từng câu cần bằng chứng riêng. |
| Bài tập cuối chương | Đối chiếu số thứ tự với bản PDF gốc cho cả 44 chương, gồm 3.590 bài có số. Tổng đơn vị cuối chương quan sát được là 5.111, có thêm câu thảo luận, luyện tập hướng dẫn và bài cầu nối. | Không cộng các loại này rồi gọi tất cả là bài đánh số. Số lượng đúng chưa chứng minh các ý nhỏ và mọi lời giải đều đúng. |
| Hình có số hiệu | Đã tìm được dấu vết sử dụng của 1.952 hình trong nội dung đang hiển thị. | Chưa đủ để kết luận mọi khung ảnh đều trọn vẹn, hay mọi hình không đánh số đều được kiểm tra. |
| Chương 2 Vật lý 1 | Đã hoàn thiện 127 đơn vị cuối chương, kiểm tra 125 trường hợp hiển thị trên trang thực tế và chạy lại 681 phép kiểm tra Python của chương. | Đây là bằng chứng của chương 2, không đại diện cho toàn bộ 44 chương. |
| Các chương trình kiểm chứng hiện có | Đã sàng lọc và chạy 124 chương trình có phép khẳng định kiểm tra. Ban đầu 121 chương trình đạt, ba trường hợp lỗi đã được điều tra và chạy lại đạt. | Các chương trình có phạm vi khác nhau. Không dùng số chương trình đạt để suy ra tỷ lệ đúng của mọi phép tính. |
| Bản sửa xuất bản gần nhất | Commit `72ea66e2b3fb6f8d44a6ff7e5d6d0e11f6d7040d` đã build và deploy thành công, lượt GitHub Actions `40750654800`. Hai Cheatsheet nhiệt đã qua 10 trường hợp trên web. Toàn bộ 22 dòng công thức chương 19 được đối chiếu MathML với dữ liệu đang dùng. | Đây là kiểm tra các sửa đổi được nêu, không phải chứng nhận mọi trang công khai. |

Hồ sơ đối chiếu nằm cùng thư mục với báo cáo này, gồm `all44-formal-section-example-presence-20261029.json`, `all44-selfcheck-destinations-20261029.json`, `all44-exercise-numbering-20261028.json`, `container-and-decay-figure-repair-20261029.json`, `screened-verifier-reruns-20261028.json` và `latest-content-public-20261029.json`.

## Kết quả rà giao diện bài tập toàn môn Vật lý 2

Đã mở toàn bộ lời giải trên tab Bài tập của cả 24 chương và kiểm tra tại năm chiều rộng màn hình. Tổng cộng có 120 trường hợp quan sát trên bản web. Lượt này còn ghi nhận vấn đề hiển thị ở 17 chương, với 206 quan sát khác nhau sau khi loại bản lặp giữa các kích thước màn hình. Một quan sát có thể là tràn trang, không nhất thiết tương ứng với một công thức độc lập.

Không dùng các kiểm tra Notes trước đây để suy ra tab Bài tập cũng đạt. Đợt sửa tiếp theo hiện đã qua 195 trường hợp hiển thị của 39 phần nội dung bằng trình xử lý Markdown và CSS thực tế. Trong đó, 57 chuỗi công thức được bẻ tại dấu quan hệ và giữ nguyên thứ tự các ký hiệu trong MathML. Những biểu thức cần đặt đại lượng trung gian được kiểm tra riêng bằng Python. Đã giữ nguyên chuỗi khai báo ảnh ở cả 39 phần.

Đây vẫn là bằng chứng cục bộ của những phần đã sửa. Sau khi xuất bản cần đo lại bản web để xác định các lỗi còn lại. Chương 31 được xử lý riêng vì đề xuất của agent còn 11 chỗ tràn khi chạy kiểm tra thực tế, dù báo cáo của agent nói đã sửa hết. Các chỗ này đã được sửa và đo lại, đạt 30 trường hợp hiển thị của sáu phần nội dung. Những bước khai triển đa thức và quan hệ tần số bị rút mất trong đề xuất ban đầu đã được khôi phục. Kiểm tra toán toàn dự án chạy lại đạt cả 32 kiểm thử, cùng các phép kiểm chứng Python độc lập cho mạch RLC.

Các phát hiện về bảng ở Q40.25 và bài 40.60 đã được sửa bằng cách hiển thị theo hàng trên điện thoại. Bảng số liệu truyền qua được chuyển từ hàng ngang sang năm cặp giá trị theo cột. Mọi giá trị được giữ nguyên. Ba phần bài tập giao thoa cũng đã được sửa, đạt thêm 25 trường hợp hiển thị cùng hai phần lượng tử. Các kiểm tra toán chạy lại đạt 32/32 và bộ kỹ năng đạt 39/39.

Lượt sửa chương 39 tiếp theo đạt 30 trường hợp hiển thị ở sáu phần nội dung. Các công thức dài trong câu được tách tại quan hệ suy luận hoặc chuyển sang khối toán, giữ đủ dữ kiện và đơn vị. Bài 39.44 giữ ước lượng theo bề rộng phòng nhưng phân biệt rõ thang độ đó với độ lệch chuẩn của vị trí. Một nhận xét về tốc độ bay của muỗi không được dữ kiện hỗ trợ đã được bỏ. Những phép đổi đơn vị, phổ chuyển mức và giới hạn độ lệch chuẩn được kiểm lại bằng Python.

## Những lỗi thực tế đã sửa

- Chương 2 có đề nhưng chưa đủ lời giải chi tiết. Đã bổ sung trọn bộ 127 đơn vị cuối chương, tách nhóm bài tập đúng cơ chế của trang và sửa các công thức bị tràn trong khung lời giải trên điện thoại.
- Một số hình khớp chính xác với vùng cắt đã khai báo nhưng vùng cắt lại thiếu nội dung. Đã khôi phục các khung được xác nhận, chẳng hạn hình ở chương 10, vạch đỏ của phổ Balmer và ký hiệu trạng thái trên đồ thị Otto.
- Hình 43.8 đã có tệp ảnh nhưng chưa được gắn vào bài. Đã đặt đồ thị ngay sau định luật phân rã và thêm chú thích tiếng Việt.
- Các khai báo hộp như `::: Info` và `::: Details` sai chữ hoa, khiến trình dựng không nhận đúng loại hộp. Đã sửa 39 khai báo trong 25 tệp và kiểm tra lại phần nội dung bên trong.
- Mục 11.4 có giá trị thiếu hệ số và các biểu thức TeX bị lộ thành chữ. Đã sửa dữ kiện, cách trình bày và các phát biểu về áp suất, biến dạng trượt trong phạm vi được đối chiếu.
- Mục 6.3 cần phân biệt công tác dụng lên lò xo với công do lò xo thực hiện. Đã khôi phục lưu ý về chiều lực và điều kiện kéo chậm.
- Mục 7.1 cần trình bày đầy đủ thứ tự lập luận, hệ quy chiếu thế năng và ví dụ đổi mốc độ cao. Đã sửa mà vẫn giữ các hình, ví dụ và câu hỏi của mục.
- Trang Wiki xuyên hầm có công thức dùng G và kappa nhưng chưa định nghĩa tại chỗ. Đã bổ sung ý nghĩa, đơn vị và điều kiện của công thức gần đúng.
- Một phép kiểm chứng hình chương 17 dùng vùng cắt cũ. Đã cập nhật dữ liệu kiểm tra sau khi đối chiếu trực tiếp với bản PDF, không đổi ảnh đúng để làm vừa phép kiểm tra cũ.

## Đánh giá cách thực hiện

Điểm có giá trị nhất của quy trình là giữ bản PDF làm căn cứ và tách bốn loại bằng chứng: Nội dung nguồn, phép tính, hình ảnh và hành vi của trang web. Những lỗi về dấu, điều kiện áp dụng và khung hình đã được phát hiện nhờ đối chiếu độc lập, dù trang vẫn có thể build thành công.

Tuy nhiên, tiến độ xử lý quá chậm và việc theo dõi công việc đã trở nên nặng nề. Có quá nhiều báo cáo nhỏ, nhiều worktree và nhiều lượt kiểm tra chồng nhau. Một số báo cáo tiến độ còn giữ trạng thái cũ, khiến việc xác định phần thật sự chưa xong khó hơn cần thiết. Đây là hạn chế của cách tổ chức công việc, cần nhận trách nhiệm và sửa bằng quy trình gọn hơn.

Một sai sót nghiêm trọng trong tiêu chí nghiệm thu ban đầu là coi bài có trạng thái sẵn sàng hoặc có đủ tiêu đề như bài đã hoàn tất. Trường hợp chương 2 cho thấy cách kiểm tra đó không đủ: Có đề bài nhưng chưa có lời giải chi tiết theo yêu cầu. Phải nghiệm thu sản phẩm người học thực sự đọc được.

Việc dùng nhiều agent chỉ hiệu quả khi nhiệm vụ nhỏ, ranh giới tệp rõ và kết quả có thể kiểm lại ngay. Hai agent có thể cùng đọc sai một ký tự do dùng chung kết quả trích xuất PDF. Hai lời kết luận giống nhau vì vậy không thay thế được việc xem trang gốc.

Chưa có cơ sở để cam kết độ chính xác bằng một tỷ lệ phần trăm. Muốn đưa ra tỷ lệ cần xác định đơn vị đánh giá, cách lấy mẫu, tiêu chí lỗi và kiểm tra độc lập phù hợp. Báo cáo này chỉ khẳng định những kết quả có bằng chứng trong đúng phạm vi.

## Kinh nghiệm khi chuyển một quyển sách thành bài học

1. Lập bảng nơi đến của từng đơn vị ngay từ đầu: Lời mở, định nghĩa, giả thiết, suy diễn, ví dụ, ứng dụng, hình, câu tự kiểm và bài tập. Mỗi đơn vị phải trỏ tới vị trí người học có thể đọc được.
2. Tách lý thuyết và bài tập bằng cấu trúc dữ liệu rõ ràng. Ví dụ khi giảng và câu hỏi ngay sau mục thuộc Notes. Bài tập cuối chương thuộc tab Bài tập, với lời giải đóng mặc định.
3. Kiểm tra công thức theo mô hình vật lý trước khi thay số: Chọn hệ, quy ước dấu, điều kiện biên, miền áp dụng và đơn vị. Với số rất nhỏ hoặc phép trừ hai đại lượng gần nhau, chọn thang sai số thích hợp thay vì dùng một ngưỡng tuyệt đối cho mọi bài.
4. Xem ảnh trong bối cảnh trang gốc. So sánh điểm ảnh chỉ chứng minh ảnh không bị vẽ lại trong vùng đã cắt, chưa chứng minh vùng đó chứa đủ hình. Cần kiểm cả nhãn sát mép, trục, đơn vị và các ô hình phụ.
5. Viết tiếng Việt theo ý nghĩa vật lý. Có thể rút gọn câu nhưng phải giữ giả thiết, lượng từ, quan hệ nhân quả và các bước quyết định. Không thêm phát biểu mạnh hơn nguồn chỉ để câu nghe dứt khoát.
6. Kiểm tra giao diện trong khung thực tế nhỏ nhất. Khung lời giải ở màn hình 320 px có thể chỉ còn 248 px. Một công thức vừa trong khung thử 280 px vẫn có thể tràn khi lên trang.
7. Đọc đầu ra thực tế của hệ thống. Chú thích ảnh có thể được thêm từ mô-đun toàn cục. Kết luận thiếu chú thích từ một tệp Markdown riêng lẻ có thể sai và dẫn đến lặp chú thích.
8. Phân biệt lỗi công cụ với chất lượng nội dung. Một agent mất kết nối có thể đã lưu tệp dùng được, nhưng phải kiểm tra phạm vi sửa và kết quả trước khi nhận. Ngược lại, tiến trình thoát thành công không đảm bảo kết quả có nội dung đúng.
9. Sau khi push, kiểm tra riêng ba bước: Commit đã tới GitHub, build/deploy đã thành công, bản web thật hiển thị đúng nội dung và ảnh. Không thay bước cuối bằng một dấu tích xanh của CI.

## Thích ứng với việc tách kho nguồn học phần

Trong lúc hoàn thiện lượt rà, dự án chuyển tài liệu môn học sang các kho Git riêng tư. Các bản sửa Vật lý 2 vì vậy được đưa vào `StudyHub-course-vat-ly-2`, còn kho giao diện chỉ cập nhật commit được ghim cùng báo cáo nghiệm thu. Không đưa lại nội dung môn học vào kho công khai.

Đã kiểm từng checksum trước khi ghép nguồn để kiểm tra. Những dữ liệu ví dụ và chỉ mục được cải thiện trong quá trình chuyển kho được giữ lại. Chỉ cập nhật số dòng tham chiếu bị thay đổi bởi lần biên tập này, thay vì ghi đè toàn bộ chỉ mục bằng bản cũ. Các ngày cập nhật của tệp không thay đổi cũng được giữ nguyên.

Lượt xuất đầu tiên bị chuyển LF thành CRLF trên Windows. Đã chuẩn hóa và kiểm lại checksum của bản Git được dùng để ghim. Đây là lỗi cần ngăn ngay ở công cụ xuất: Quy định kiểu xuống dòng và kiểm tệp đã stage trước khi commit, thay vì chỉ kiểm bản đang mở trong thư mục làm việc.

Sau khi ghép đủ 10 kho học phần theo commit được khóa, lệnh `npm run verify:math` đạt cả 32 kiểm thử. Bộ kiểm tra đã phân tích 1.508 trang cùng 588 lệnh chèn nguồn và kiểm tra 58.352 công thức khác nhau trên toàn bộ dữ liệu. Kết quả này chứng minh tính hợp lệ của cú pháp và bộ hiển thị trong phạm vi đã chạy, không chứng minh mọi công thức đều đúng về mặt vật lý.

## Đề xuất cải thiện

Nên dùng một bảng nghiệm thu duy nhất cho mỗi chương, có các cột về nội dung nguồn, phép tính, ảnh, câu tự kiểm, bài tập, Cheatsheet, Wiki và giao diện công khai. Mỗi kết luận cần kèm vị trí bằng chứng và commit tương ứng. Các báo cáo riêng chỉ giữ vai trò chi tiết bổ sung.

Nhiệm vụ agent nên kết thúc ở một phần có thể nhận ngay, chẳng hạn một mục hoặc một nhóm bài có đầy đủ dữ kiện và lời giải. Agent phải lưu kết quả theo từng đơn vị, thay vì dành nhiều thời gian dựng bộ khung rồi mới viết nội dung vào cuối lượt. Không giao lại một nhiệm vụ đã hết số lần sửa chỉ bằng cách đổi tên.

Nên tự động kiểm tra những bất biến có ý nghĩa: Đủ các ý của đề, số thứ tự liên tục, một lời giải đóng cho mỗi bài, đủ các giai đoạn giải, liên kết hợp lệ, loại hộp đúng và ảnh được sử dụng thật. Những kiểm tra này hỗ trợ người rà nội dung, không thay thế người rà.

Phần tính toán nên lưu dữ kiện và quan hệ vật lý có thể dùng lại. Khi công thức đổi, chạy đúng nhóm kiểm tra liên quan. Khi chỉ sửa lời văn, không chạy lặp toàn bộ các phép kiểm chứng không liên quan. Build toàn cục tiếp tục chạy trên GitHub để giảm tải máy cá nhân.

Việc lưu trữ nên tách rõ sản phẩm, bằng chứng cần giữ và tệp có thể tạo lại. Trạng thái Git sạch không đủ để xóa worktree: Các thư mục QA bị bỏ qua bởi Git vẫn có thể chứa bằng chứng chưa được bảo quản.

## Phần chưa được nghiệm thu xong

- Hoàn tất việc nhận hoặc bác bỏ các kết quả đối chiếu nội dung còn lại cho cả hai môn, đặc biệt các giả thiết, ý nhỏ của bài tập và nội dung không có số hiệu. Không coi các bảng đếm là bằng chứng thay thế.
- Hoàn tất đối chiếu ý nghĩa của Cheatsheet và Wiki theo phạm vi từng chương. Lượt rà hai chương 19–20 đã cung cấp một số đề xuất. Các hệ thức được nhận cho chương 19 đã được bổ sung và kiểm tra. Không nhận kết luận đầy đủ của agent khi trích dẫn ấn bản hoặc số trang không khớp.
- Cập nhật kết quả của đợt kiểm tra cuối, push các thay đổi đã được nhận và xác minh bản công khai tương ứng.
- Sau khi bảo quản đầy đủ bằng chứng, mới dọn những worktree, tệp và tiến trình do công việc này tạo ra mà không còn cần thiết. Chưa tiến hành xóa các worktree đang cần giữ để kiểm tra.

Báo cáo sẽ được chốt sau các bước này. Những tệp riêng của người dùng, bản PDF gốc và dữ liệu nền chưa được nhận không thuộc phạm vi tự ý xóa.

## Lượt kiểm tra bổ sung ngày 29/10/2026

Đã kiểm tra tab Bài tập của toàn bộ 20 chương Vật lý 1 trên bản công khai, gồm 2.551 đơn vị và 2.320 trường hợp hiển thị. Mỗi đơn vị được đối chiếu với danh mục đang dùng, có đúng một lời giải đóng mặc định, phần tóm tắt và hướng đi. Lượt này không ghi nhận lỗi tải tài nguyên hay hình học hiển thị. Kết quả không thay thế việc đối chiếu từng lập luận và phép tính.

Lượt sửa Vật lý 2 tiếp theo đã kiểm tra 45 trường hợp hiển thị của các phần được sửa tại chương 23, 26, 29, 30, 32 và 42. Các phép tính liên quan được kiểm lại bằng Python, giữ nguyên chuỗi khai báo hình. Chương 42 được điều chỉnh phát biểu về điện tích trong vật liệu bán dẫn để phân biệt miền trung hòa và vùng điện tích không gian. Một công thức bị agent báo dài nhưng thực tế đạt giới hạn đã được giữ nguyên.

Bản nguồn riêng tư được ghim tại commit `1b7fb77d67f468e492a46782dd2137edda8dc8b7`. Kiểm tra toán toàn dự án và build của chính bản ghim này chờ lượt GitHub Actions, không được suy ra từ kết quả của commit trước. Hồ sơ gồm `physics1-all-public-exercises-20261029.json` và `physics2-observed-formula-followup-20261029.json`.

## Giữ đúng số hiệu và kiểm tra các trang đọc

Đã rà thêm 375 trang công khai, gồm 44 trang Notes đầu chương, 287 trang lý thuyết riêng và 44 Cheatsheet. Tổng cộng 1.875 trường hợp tại năm chiều rộng không ghi nhận lỗi tràn công thức, MathML phụ bị lộ hoặc ảnh tải thất bại. Đây là lượt trên bản công khai trước khi bản `9edd8705` xuất bản, không phải chứng nhận mọi bản nguồn về sau.

Đã sửa lỗi bộ chuẩn hóa tiêu đề đổi số hiệu như `21.45` thành `21: 45` khi đi cùng ký hiệu độ khó. Bộ xử lý mới giữ nguyên số hiệu nhiều cấp và vẫn phân biệt dấu chấm kết thúc nhãn với dấu chấm trong mã bài. Kiểm tra trình xử lý đạt 62 trường hợp, bộ kỹ năng đạt 39 kiểm thử. Lượt cloud và bản web của thay đổi này cần xác nhận riêng.

Đã sửa một sai sót trong báo cáo đếm: Chín bài cầu nối có sẵn bị bỏ qua do cách đặt tiêu đề. Đối chiếu lại mục bài cầu nối trên PDF và nguồn hiệu lực cho tổng 2.560 đơn vị cuối chương Vật lý 2, thay cho số đếm cũ 2.551. Tổng hai môn là 5.111, trong khi số bài đánh số vẫn là 3.590. Việc sửa bộ đếm không được mô tả như bổ sung chín bài mới.

## Cập nhật ngày 31/10/2026

Đã xác nhận commit `4085f71365aefdf7b2f2a81cc9975eaf100c36ba` build và deploy thành công trong lượt GitHub Actions `40842075479`. Bản trước `9edd8705` cũng đã build và deploy thành công. Hai lượt này bao gồm nguồn công thức đã ghim ngày 29/10 và bản sửa số hiệu bài tập.

Đối chiếu trực tiếp hai mục 43.1–43.2 với PDF phát hiện các điểm cần sửa về dấu tương tác từ, điều kiện spin, phân biệt khối lượng nguyên tử với khối lượng hạt nhân và các phát biểu quá tuyệt đối trong mô hình liên kết. Đã sửa 19 khối nội dung, bổ sung năng lượng liên kết deuteron trên mỗi nucleon và ý nghĩa số hạng thể tích. Hai chú thích tiếng Anh được sửa ký hiệu chia và ký hiệu đồng vị. Đường dẫn hình và các tệp ảnh gốc được giữ nguyên.

Các sửa đổi được rà độc lập theo đúng phạm vi, chạy 31 phép kiểm số học, mô hình và sự hiện diện của điều kiện. Hai mục đã qua 10 trường hợp hiển thị với quy tắc Markdown, công thức, chú thích hình và CSS thực tế. Phần liên kết thuật ngữ tự động được bỏ qua trong bộ kiểm cục bộ này, nên vẫn cần CI đầy đủ và kiểm trang sau triển khai. Bộ kỹ năng chạy đạt 39 kiểm thử.

Một báo cáo agent cũ ghi sai nguyên tố của ví dụ, từ trường, nội dung ứng dụng đồng vị và một số câu hỏi. Các chi tiết đó không được dùng làm căn cứ sửa. Bài học là phải kiểm chính dữ kiện trong PDF, kể cả khi một báo cáo có vẻ đầy đủ và có nhiều con số kiểm tra. Hồ sơ nghiệm thu hiện tại là `nuclear-corrections-20261031.json`, với bằng chứng chi tiết được bảo quản trong kho nguồn riêng tư. Đợt sửa mới chưa được gọi là đã xuất bản cho đến khi CI và bản web tương ứng được xác nhận.

## Nghiệm thu tab Bài tập và khôi phục giải thích cuối môn

Lượt kiểm tra bản web ngày 31/10 đã mở toàn bộ lời giải của 24 chương Vật lý 2. Đã đối chiếu số bài, trình tự bài đánh số và 2.560 đơn vị cuối chương, với đúng một lời giải đóng mặc định, tóm tắt và hướng đi cho mỗi đơn vị. Cả 120 trường hợp ở năm chiều rộng đều đạt, không có lỗi tải tài nguyên trong lượt này. Hồ sơ là `physics2-all-public-exercises-20261031.json`. Kết quả xác nhận cấu trúc và hiển thị, không thay thế việc rà từng giả thiết và lời giải vật lý.

Đối chiếu mục 44.6–44.7 phát hiện các giải thích bị rút mất về dịch chuyển đỏ lớn, giả thiết của thời gian Hubble, photon năng lượng cao và deuteron, cơ chế ba hạt alpha, cùng giới hạn của mô hình bất đối xứng vật chất. Đã khôi phục 22 khối nội dung và làm rõ các miền áp dụng. Năm ví dụ, hai câu tự kiểm, 12 đường dẫn hình và 10 số hiệu phương trình được giữ nguyên. Hai phần Cheatsheet hạt nhân được bổ sung đủ các hệ thức và điều kiện cốt lõi. Phần kỹ thuật của năm Wiki tương ứng được cập nhật, giữ các ví dụ, câu hỏi, đáp án và liên kết cũ.

Đợt sửa đã được đối chiếu độc lập, chạy 42 phép kiểm số học và quan hệ mô hình, cùng 40 trường hợp hiển thị của các phần hiện tại. Khi kiểm giao diện, một lượt đầu bị nội dung công khai nạp lại sau khi chèn bản đề xuất. Bộ kiểm đã được sửa để bắt buộc giữ đúng nội dung và đủ công thức tại từng chiều rộng, rồi chạy lại đạt. Không dùng một trang có mất công thức làm bằng chứng không tràn.

Ảnh nguyên gốc được giữ. Một nhãn trên sơ đồ tổng hợp hạt nhân cần được đọc với lưu ý khoa học, thay vì giải thích khác biệt bằng làm tròn. Ghi chú được bổ sung và có tài liệu đối chiếu của Particle Data Group trong phần tham khảo. Chi tiết sửa và giới hạn nghiệm thu nằm trong `cosmology-and-nuclear-support-20261031.json`. Bằng chứng chi tiết được bảo quản riêng tư, các tệp văn bản gốc được nén không mất dữ liệu và có checksum. Bản ghim mới vẫn phải qua CI và kiểm tra bản triển khai tương ứng.

## Bổ sung nguyên lý II và nối các lần nghiệm thu Vật lý 1

Đã đối chiếu trực tiếp mục 20.5 tại PDF 671–673. Bản trước còn thiếu cơ chế chuyển động có tổ chức và chuyển động hỗn loạn của phân tử, lập luận nguyên lý II độc lập với nguyên lý I, cùng các ví dụ dòng khí và sự trộn lẫn không thuận nghịch. Những phần này được khôi phục. Phát biểu Clausius giữ đúng điều kiện kết quả duy nhất của quá trình. Yêu cầu cấp công cơ học được đặt trong mô hình máy lạnh dùng máy nén đang xét.

Hình 20.11, hai hướng chứng minh tương đương, câu tự kiểm và đáp án được giữ nguyên. Đã chạy 24 phép kiểm bằng Python về tích phân lực lò xo và cân bằng năng lượng. Phần hiện tại qua năm chiều rộng 320, 360, 375, 768 và 1440 px, giữ đủ 42 công thức, một hình và một chú thích, không phát hiện tràn hoặc thanh cuộn công thức. Bộ công cụ bài giảng đạt 39 kiểm thử. Phép kiểm tích hợp cục bộ không nạp được một học phần riêng tư khác trong checkout rút gọn, do đó không được tính là đạt. CI phải xác nhận bản đã lắp ghép đầy đủ.

Đã nối lại hai thay đổi sau nghiệm thu cũ. Mục 6.3 bổ sung đúng lưu ý phân biệt công lên lò xo với công do lò xo thực hiện, được đối chiếu PDF 203 và kiểm lại dấu công. Mục 9.3 chỉ bỏ khoảng trắng cuối dòng, không đổi nội dung. Hồ sơ chi tiết là `physics1-second-law-source-acceptance-20261031.json`. Bằng chứng, ảnh trang đối chiếu và ma trận nghiệm thu đã được lưu riêng tư trong gói nén không mất dữ liệu, có checksum kiểm lại từng tệp. Ba tệp chương 18 vẫn đang được rà riêng. Đây chưa phải nghiệm thu hoàn tất toàn bộ hai môn.
