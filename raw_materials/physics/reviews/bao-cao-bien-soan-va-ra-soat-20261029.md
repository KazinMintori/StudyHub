# Báo cáo chốt biên soạn Vật lý đại cương 1 và 2

Ngày chốt: 1/11/2026. Các thay đổi nội dung được đẩy lên GitHub và build toàn bộ trên GitHub Actions.

## 1. Phạm vi bàn giao

Nội dung gồm 20 chương Vật lý đại cương 1, từ đo lường và cơ học đến hết nhiệt học, cùng 24 chương Vật lý đại cương 2 tương ứng chương 21–44 của Young & Freedman, gồm điện từ, quang học và vật lý hiện đại.

Notes giữ lý thuyết, lập luận, ví dụ và câu hỏi ngay tại phần giảng tương ứng. Bài tập cuối chương nằm trong tab Bài tập. Mỗi lời giải dùng khung đóng mở, có tóm tắt và phần Hướng đi nêu công thức cùng lý do sử dụng. Cheatsheet dành cho định nghĩa, tính chất, công thức và điều kiện áp dụng. Kiến thức nền và Wiki phục vụ việc tra cứu trong Notebook.

Hình minh họa được trích từ PDF gốc. Phần giải nghĩa tiếng Việt đặt dưới ảnh và tránh lặp cùng một nhãn tiếng Anh. Các bản sửa khung lấy lại phần bị cắt từ chính PDF, không thay bằng hình vẽ lại.

## 2. Những sửa đổi thực chất trong đợt chốt

- Khôi phục chú thích và nhãn từng không xuất hiện dù đã có trong nguồn Markdown. Nguyên nhân là ảnh và đoạn văn liền sau bị trình dựng trang coi là cùng một đoạn. Đã xử lý tại nguồn và cập nhật các mốc dòng liên quan.
- Khôi phục chữ, tiểu hình, đầu trục, mũi tên và dây nối bị cắt. Ảnh sau sửa được xem cạnh ngữ cảnh PDF, rồi đối chiếu lại vùng nguồn.
- Sửa chú thích sai đối tượng, chiều chuyển mức hoặc ký hiệu. Các lỗi gồm nhầm bán kính lớn và nhỏ, nhầm lực với gia tốc, mất số mũ, mất ký hiệu Hy Lạp và đảo chú thích hai ảnh kính phân cực.
- Bổ sung điều kiện áp dụng còn thiếu. Chẳng hạn, công thức trường của trụ cần đối xứng trụ dài vô hạn hoặc gần đúng xa hai đầu. Kết luận điện trường ngoài hai bản bằng không cần điện tích bằng nhau về độ lớn, trái dấu và không có trường ngoài.
- Phân biệt thế năng điện với tổng thế năng của mọi lực thế. Khi dùng riêng thế năng điện, bảo toàn động năng cộng thế năng điện phải loại công của các lực khác.
- Sửa công thức dài trong các khung hẹp bằng cách ngắt tại dấu quan hệ hoặc đặt tên cho từng phần. Không dùng việc cắt nội dung hay thu nhỏ chữ để che lỗi tràn.

Lượt sửa cuối xử lý 184 tệp nội dung, trong đó có 159 ảnh gốc được khôi phục khung. Giao diện đọc của 192 hình cùng các biến thể chú thích liên quan đạt 1.000 trường hợp ở năm chiều rộng. Hai Cheatsheet được bổ sung điều kiện áp dụng đạt thêm 10 trường hợp kiểm tra bố cục.

## 3. Cách kiểm chứng và giới hạn của kết quả

Các ví dụ, phép đổi đơn vị, quan hệ dấu và phản ví dụ đã được kiểm bằng Python trong phạm vi từng biên bản. Kiểm tra cấu trúc bài giảng được tách khỏi kiểm tra ý nghĩa vật lý. Số lượng bài, hình hoặc công thức chỉ chứng minh sự hiện diện, không tự chứng minh đúng nội dung.

Các trang sửa được kiểm ở các chiều rộng 320, 360, 375, 768 và 1440 px. Có hai loại bằng chứng riêng: Kiểm tra nguồn mới bằng trình dựng và CSS thực tế, và kiểm tra trang đã xuất bản. Kết quả của loại thứ nhất không được dùng thay cho loại thứ hai.

Build toàn bộ và deploy chạy trên GitHub. Checkout rút gọn trên máy thiếu một số module riêng tư, vì vậy lần chạy verify:math cục bộ có 12 kiểm thử đạt và ba kiểm thử không nạp được module. Kết quả ấy không được ghi thành đạt toàn dự án. Lượt CI đã lắp đủ học phần mới là căn cứ cho kiểm tra toàn bộ.

Các báo cáo đọc nhầm module cũ, chỉ kiểm mã băm hoặc chỉ kiểm ảnh khớp vùng cắt đã bị loại khỏi bằng chứng nghiệm thu ý nghĩa. Những trường hợp biên chưa đủ căn cứ không được đổi thành đạt chỉ để đóng bảng theo dõi. Báo cáo này không đưa ra tỷ lệ chính xác tuyệt đối vì không có phép đo độc lập cho một tỷ lệ như vậy.

Phần tra cứu chương 33–44 đã được đọc theo phiên bản hiện hành, gồm 353 mục Cheatsheet và 227 Wiki riêng biệt cùng ghi chú nhanh. Ba nhóm kiểm đã chạy 138 phép kiểm Python trong phạm vi các nhận định được ghi rõ. Các lỗi xác nhận được sửa theo yêu cầu chốt, rồi dừng tìm lỗi mới. Kết quả này không được suy rộng thành chứng nhận độc lập cho mọi phép tính của toàn bộ 44 chương.

## 4. Đánh giá cách thực hiện

Điểm hữu ích là việc giữ nguồn, mã băm và phép tính có thể chạy lại, cùng khả năng tách nội dung khỏi giao diện để kiểm tra trên điện thoại. Nhờ vậy, nhiều lỗi nằm ngoài phạm vi một bài kiểm thử đơn giản đã được sửa đúng chỗ.

Điểm chưa tốt là tiến độ kéo dài và số worktree, bản rà cùng tệp trung gian tăng quá nhiều. Có giai đoạn kết quả của agent bị nhận quá gần với kết luận nghiệm thu, trong khi bản nguồn hoặc phạm vi kiểm chưa đúng. Việc kiểm tra hình cũng từng chỉ xác nhận vùng cắt tái lập được, bỏ sót câu hỏi quan trọng hơn là vùng cắt đã chứa đủ hình hay chưa.

Một sai sót khác là kiểm các bản sao khác thời điểm. Một báo cáo có thể đọc đúng tệp của nó nhưng vẫn sai đối với phiên bản đang xuất bản. Các trường hợp này làm phát sinh việc làm lại và gây khó theo dõi tiến độ.

## 5. Kinh nghiệm khi chuyển một giáo trình thành bài học

1. Khóa phiên bản nguồn và lập bản đồ từng mục, ví dụ, câu tự kiểm, bài tập, hình và bảng trước khi viết. Mỗi đơn vị cần có nơi xuất hiện cụ thể.
2. Tách soạn nội dung, tính lại, kiểm hình và kiểm hiển thị thành các bước rõ ràng. Một bước đạt không thay thế các bước còn lại.
3. Trích hình cùng vùng ngữ cảnh rộng hơn ngay từ đầu. Xem cả đầu trục, dấu âm, chỉ số, nhãn và dây nối trước khi chốt tọa độ.
4. Khóa dữ liệu đang được giao diện dùng. Không rà một bản catalog hoặc Cheatsheet cũ chỉ vì tên tệp trông phù hợp.
5. Giữ điều kiện vật lý đi cùng công thức. Việc rút gọn câu không được bỏ giả thiết, quy ước dấu hoặc miền gần đúng.
6. Viết tiếng Việt từ ý nghĩa của toàn câu và kiểm lại đối tượng được nói tới. Không để OCR quyết định ký hiệu hoặc dịch từng từ khiến lực biến thành gia tốc.
7. Kiểm sớm ở khung hẹp nhất thực tế, gồm cả popover và hộp lời giải. Một biểu thức vừa trang Notes vẫn có thể tràn trong ghi chú nhanh.
8. Lưu bằng chứng gắn với đúng tệp và phiên bản, nhưng chỉ giữ một bộ đầu vào dùng chung. Không nhân bản phụ thuộc hoặc trình duyệt cho từng agent.

## 6. Đề xuất cải thiện quy trình

Dùng một danh sách giao việc cố định cho từng chương và chỉ một bảng chốt phiên bản. Agent phải trả về tệp đã đọc, thay đổi chính xác, phép kiểm đã chạy và giới hạn còn lại. Người điều phối kiểm các khác biệt quan trọng trước khi nhập.

Tọa độ ảnh, nhãn và chú thích nên được quản lý từ cùng một nguồn dữ liệu để tránh sửa ảnh mà quên phần giải nghĩa. Công cụ kiểm cần báo riêng lỗi nguồn, lỗi trình dựng và lỗi công cụ kiểm. Một lỗi của công cụ không nên dẫn đến sửa nội dung vốn đúng.

Mỗi đợt nên gom các thay đổi liên quan thành một commit đủ lớn, chạy CI một lần và kiểm đúng các trang bị ảnh hưởng. Sau khi bản ấy xuất bản thành công, lưu một gói bằng chứng có mục lục rồi đóng worktree đã xong. Cách này giảm số lượt build, dung lượng và việc đọc lại cùng một vấn đề.

## 7. Quyết định chốt và dọn dẹp

Theo yêu cầu cuối của người dùng, không mở thêm vòng rà mới hoặc thêm tính năng. Đợt chốt xử lý các lỗi đã xác nhận, lưu các giới hạn kiểm chứng và theo dõi build, deploy của phiên bản bàn giao.

Chỉ dọn tệp tạm có thể tạo lại và worktree đã xác nhận không còn nội dung riêng chưa xuất bản. Giữ PDF gốc, nội dung đã soạn, thay đổi chưa xuất bản, trạng thái của các tác vụ khác và bằng chứng cần truy nguyên. Nhật ký dọn dẹp ghi rõ đường dẫn, căn cứ và dung lượng thực tế, không suy đoán mức giảm lag.


## 8. Sửa nốt các lỗi đang xử lý và kết thúc rà

Theo yêu cầu cuối, chỉ xử lý các lỗi đã xác nhận trong lượt đang làm. Không tiếp tục mở vòng tìm lỗi, thêm tính năng hoặc sửa giao diện.

Các thay đổi gồm bổ sung điều kiện tới gần vuông góc cho giao thoa màng mỏng, điều kiện hàng rào đủ dày cho xấp xỉ xuyên hầm và điều kiện công lực điện. Định nghĩa quang trình phân biệt chiều dài tương đương trong chân không với phần chênh quang trình. Ví dụ hai gương vuông góc và công thức ảnh toàn ký giữ đầy đủ điều kiện hình học, pha.

Các khối toán Wiki bị mất môi trường căn dòng hoặc mất ký hiệu Hy Lạp được khôi phục. Các vế dài được viết qua đại lượng trung gian khi cần, không bẻ ở dấu cộng hoặc nhân. Phần tra cứu được bổ sung hai định nghĩa còn thiếu đã xác nhận: Liên kết kim loại và đầu dò hạt dựa trên ion hóa. Nội dung chỉ gồm định nghĩa, tính chất và công thức.

Lượt sửa này thay đổi 15 module nội dung riêng tư và 42 tệp công khai, gồm 41 Wiki và dữ liệu khái niệm chung. Kiểm hiển thị đúng phần sửa đạt 280 trường hợp tại 320, 360, 375, 768 và 1440 px, không có lỗi trong phạm vi ấy. 39 kiểm thử công cụ đều đạt. Kiểm toán toàn dự án cục bộ bị giới hạn bởi module riêng tư thiếu và thư mục tạm sandbox, nên không ghi thành đạt toàn bộ. CI đầy đủ được chạy trên GitHub sau khi push.

Bản phát hành trước lượt sửa này, commit abebe25f, đã build và deploy thành công. Kiểm web trước đó xác nhận 159 ảnh cập nhật, 317 lần xuất hiện chú thích và 325 trường hợp bố cục. Lượt sửa tra cứu giữ nguyên toàn bộ ảnh.

Đã xóa 935 bản sao ảnh QA đã có bản lưu trữ trùng mã băm và hồ sơ Chrome tạm của phiên kiểm trước, tổng dung lượng logic 212.886.843 byte. Đã bảo toàn 698 tệp bằng chứng bị Git bỏ qua trước khi thử lưu trữ 12 worktree. Ứng dụng từ chối vì chat khác vẫn dùng các worktree ấy, nên chúng được giữ nguyên. PDF gốc, nội dung riêng chưa xuất bản và dữ liệu của người dùng không bị xóa. Dung lượng logic tệp đã xóa không phải phép đo mức giảm lag của máy.
