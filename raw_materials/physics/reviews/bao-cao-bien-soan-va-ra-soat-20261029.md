# Báo cáo biên soạn và rà soát Vật lý đại cương 1, 2

Cập nhật ngày 29/10/2026. Đây là báo cáo đang hoàn thiện. Đã có đủ bản soạn của 20 chương Vật lý đại cương 1 và 24 chương Vật lý đại cương 2. Việc nghiệm thu toàn bộ nội dung theo từng yêu cầu và việc dọn dẹp cuối cùng vẫn chưa kết thúc.

## Kết quả có bằng chứng

| Hạng mục | Kết quả đã kiểm tra | Giới hạn của kết luận |
| --- | --- | --- |
| Phạm vi môn học | Vật lý 1 gồm chương 1–20. Vật lý 2 gồm chương 21–44, có vật lý hiện đại. | Trạng thái sẵn sàng trong danh mục không tự chứng minh nội dung đầy đủ. |
| Cấu trúc nội dung đang sử dụng | 44 bài, các trang chủ đề, nguồn được chèn vào bài, ảnh, Cheatsheet và liên kết khái niệm đều được kiểm kê. Không phát hiện đường dẫn ảnh, khái niệm hoặc trang Wiki bị thiếu trong lượt này. | Tệp tồn tại chưa chứng minh nội dung tệp chính xác. |
| Mục lý thuyết và ví dụ | Đã tìm được nơi hiển thị của 290 mục lý thuyết và 492 ví dụ có số hiệu. | Chưa dùng kết quả này để xác nhận từng câu, giả thiết và bước suy luận. |
| Câu hỏi khi giảng | 280 câu tự kiểm tra có nơi đến trong Notes. Những tiêu đề không ghi số đã được phân biệt với trường hợp thiếu câu hỏi. | Việc đối chiếu toàn bộ lựa chọn và lời giải của từng câu cần bằng chứng riêng. |
| Bài tập cuối chương | Đối chiếu số thứ tự với bản PDF gốc cho cả 44 chương, gồm 3.590 bài có số. Tổng đơn vị cuối chương quan sát được là 5.102, có thêm câu thảo luận, luyện tập hướng dẫn và bài cầu nối. | Không cộng các loại này rồi gọi tất cả là bài đánh số. Số lượng đúng chưa chứng minh các ý nhỏ và mọi lời giải đều đúng. |
| Hình có số hiệu | Đã tìm được dấu vết sử dụng của 1.952 hình trong nội dung đang hiển thị. | Chưa đủ để kết luận mọi khung ảnh đều trọn vẹn, hay mọi hình không đánh số đều được kiểm tra. |
| Chương 2 Vật lý 1 | Đã hoàn thiện 127 đơn vị cuối chương, kiểm tra 125 trường hợp hiển thị trên trang thực tế và chạy lại 681 phép kiểm tra Python của chương. | Đây là bằng chứng của chương 2, không đại diện cho toàn bộ 44 chương. |
| Các chương trình kiểm chứng hiện có | Đã sàng lọc và chạy 124 chương trình có phép khẳng định kiểm tra. Ban đầu 121 chương trình đạt, ba trường hợp lỗi đã được điều tra và chạy lại đạt. | Các chương trình có phạm vi khác nhau. Không dùng số chương trình đạt để suy ra tỷ lệ đúng của mọi phép tính. |
| Bản sửa xuất bản gần nhất | Commit `72ea66e2b3fb6f8d44a6ff7e5d6d0e11f6d7040d` đã build và deploy thành công, lượt GitHub Actions `40750654800`. Hai Cheatsheet nhiệt đã qua 10 trường hợp trên web. Toàn bộ 22 dòng công thức chương 19 được đối chiếu MathML với dữ liệu đang dùng. | Đây là kiểm tra các sửa đổi được nêu, không phải chứng nhận mọi trang công khai. |

Hồ sơ đối chiếu nằm cùng thư mục với báo cáo này, gồm `all44-formal-section-example-presence-20261029.json`, `all44-selfcheck-destinations-20261029.json`, `all44-exercise-numbering-20261028.json`, `container-and-decay-figure-repair-20261029.json`, `screened-verifier-reruns-20261028.json` và `latest-content-public-20261029.json`.

## Kết quả rà giao diện bài tập toàn môn Vật lý 2

Đã mở toàn bộ lời giải trên tab Bài tập của cả 24 chương và kiểm tra tại năm chiều rộng màn hình. Tổng cộng có 120 trường hợp quan sát trên bản web. Lượt này còn ghi nhận vấn đề hiển thị ở 17 chương, với 206 quan sát khác nhau sau khi loại bản lặp giữa các kích thước màn hình. Một quan sát có thể là tràn trang, không nhất thiết tương ứng với một công thức độc lập.

Không dùng các kiểm tra Notes trước đây để suy ra tab Bài tập cũng đạt. Đợt sửa tiếp theo hiện đã qua 195 trường hợp hiển thị của 39 phần nội dung bằng trình xử lý Markdown và CSS thực tế. Trong đó, 57 chuỗi công thức được bẻ tại dấu quan hệ và giữ nguyên thứ tự các ký hiệu trong MathML. Những biểu thức cần đặt đại lượng trung gian được kiểm tra riêng bằng Python. Đã giữ nguyên chuỗi khai báo ảnh ở cả 39 phần.

Đây vẫn là bằng chứng cục bộ của những phần đã sửa. Sau khi xuất bản cần đo lại bản web để xác định các lỗi còn lại. Chương 31 được xử lý riêng vì đề xuất của agent còn 11 chỗ tràn khi chạy kiểm tra thực tế, dù báo cáo của agent nói đã sửa hết.

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
