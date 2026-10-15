# Rà soát cuối Chương 36

Phạm vi: Trang in 1185–1216, tương ứng PDF 1205–1236. Chương 37 bắt đầu ở PDF 1237. Nguồn đối chiếu là Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, SHA256 f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff.

## Kiểm kê nội dung

| Phần | Nội dung và nơi hiển thị |
| --- | --- |
| Mở đầu | Notes trang chương, mắt kép của ruồi, tám mục tiêu, các kiến thức cần ôn và đủ năm lựa chọn câu mở đầu |
| 36.1 | Chủ đề Fresnel và Fraunhofer, mép dao và lỗ kim, nhiều điểm của nguồn và nhiều bước sóng, Huygens, lịch sử được nguồn nêu, dụng cụ chỉ nhận phần mặt sóng và tự kiểm ở trang nối tiếp |
| 36.2 | Chủ đề khe đơn, hình học bốn phần, thấu kính, ghép cặp nửa khe và các bậc, cảnh báo cực tiểu với cực đại, điều kiện góc nhỏ, 85% năng lượng, ví dụ 36.1 và tự kiểm |
| 36.3 | Chủ đề cường độ, tổng vectơ pha thành cung, hệ số trường có dấu, bình phương sinc, pha hai mép, giới hạn tại tâm, cực đại phụ, hàm siêu việt, độ mở, âm, hai ví dụ và tự kiểm đủ bốn lựa chọn |
| 36.4 | Chủ đề hai khe rộng, bao nhiễu xạ, bậc khuyết, câu hỏi chứng minh, tám khe, tích lũy pha, cực tiểu, độ hẹp và năng lượng, tự kiểm |
| 36.5 | Chủ đề cách tử, truyền qua và phản xạ, DVD, ví dụ 36.4 đủ các bậc và chồng phổ, máy quang phổ, hạn chế lăng kính, bộ đôi natri, chứng minh phân giải, ứng dụng ADN và tự kiểm |
| 36.6 | Chủ đề tia X, lịch sử, bể sóng và mạng tán xạ, tổng đường nguồn–tâm–người quan sát, điều kiện góc và Bragg, các họ mặt mạng ba chiều, đo cấu trúc và bước sóng, ADN, ví dụ 36.5 và tự kiểm |
| 36.7 | Chủ đề khẩu độ tròn, ba vòng tối và ba vòng sáng, đĩa Airy, năng lượng, bốn nguồn ảnh, Rayleigh, phân giải ảnh với phổ, tử ngoại và electron, DVD/Blu-ray, VLA, mắt đại bàng, ví dụ 36.6 và tự kiểm |
| 36.8 | Chủ đề toàn ký, ghi và tái tạo, ảnh thật và ảo, hình học một điểm, cận trục, vật mở rộng, hai góc nhìn, tính kết hợp và ổn định cơ học |
| Tổng kết | Notes trang chương, năm nhóm nội dung và đủ năm hình tổng kết |
| Luyện tập | Tab Bài tập, đủ 12 bài hướng dẫn và bài cầu nối Doppler của thiên hà |
| Thảo luận | Tab Bài tập, Q36.1–Q36.19, có các giản đồ pha được đề yêu cầu |
| Bài đánh số | Tab Bài tập, 36.1–36.71, đầy đủ các phần, bảng chín và bốn cặp số đo, hình P và đoạn dẫn cùng mọi lựa chọn MCAT |
| Đáp số | Tab Bài tập, 36 hàng bài lẻ đồng bộ lời giải và điều kiện mô hình |

Mỗi đề cuối chương đứng trước một hộp lời giải gập. Mỗi hộp gồm Tóm tắt đề bài, Hướng đi với quan hệ và lý do sử dụng, rồi các bước giải. Các ví dụ và câu hỏi trong mạch giảng giữ ở Notes. Câu tự kiểm và câu hỏi đánh giá được đặt tại vị trí giảng, chỉ gập phần trả lời khi thích hợp.

## Đối chiếu và tính toán

Chín chương trình Python kiểm sáu ví dụ, bảy tự kiểm, 71 bài đánh số, 12 bài hướng dẫn, bài cầu nối và các lập luận định lượng của thảo luận. Bài 36.62 dùng đủ chín cặp số đo, bài 36.63 tính riêng bốn đường kính rồi lấy trung bình đúng yêu cầu. Bài 36.61 đếm đủ 17 đốm của ảnh nguồn, xác định bậc khuyết ở ±7. Tổng phức N khe được so với 120 tổng hữu hạn. Phép tích phân khe đơn có đối chiếu số độc lập.

Các bất nhất và giả thiết cần nói rõ được giữ trong `ch36-source-clarifications.json`. Bao gồm đáp số hướng dẫn không khớp dữ kiện, bậc khuyết không chọn duy nhất bậc cực tiểu của bao, góc lớn cần sin/tang, kích thước biển số chưa cho, vận tốc pha của electron và các phát biểu chưa nhất quán ở bài màng trượt 36.65. Câu 36.70 cần giả thiết bậc một để chọn một đáp án. Không đổi dữ kiện để ép khớp đáp số.

Một lượt rà trước chỉ đọc trang PDF 1205–1206 đã kết luận sai rằng tự kiểm 36.1 nằm ngoài nguồn. Khi xem trang nối tiếp PDF 1207, Codex xác nhận câu ấy có thật và khôi phục đúng đề cùng đáp án. Hồ sơ cuối ghi rõ việc sửa sai này. Tự kiểm 36.3 được sửa về đủ bốn lựa chọn 500 nm, 10,6 µm, 1,00 mm, 50,0 nm. Số hiệu 36.8 được trả về quan hệ góc cực tiểu.

## Hình và trình bày

Có 42 PNG giữ nguyên pixel vùng PDF, gồm 30 hình lý thuyết, ba hình bài tập, ảnh mở đầu, ba ứng dụng và năm hình tổng kết. Đã mở đủ mép phải hai phần 36.3, bỏ đường khung ví dụ thừa dưới 36.7, giữ đủ các sóng và điểm ảnh của 36.29. Có chín SVG bổ trợ lời giải, gồm bảy giản đồ pha, đồ thị nghiệm siêu việt và đồ thị đủ chín cặp số đo. Các hình nguồn không bị vẽ lại, đổi màu hay ghép bố cục.

Chú thích tiếng Việt nằm dưới hình. Mỗi nhãn tiếng Anh được giải nghĩa một lần qua module tập trung. Các màu ion NaCl và ký hiệu Hy Lạp chép từ ảnh được rà lại. Ba ảnh ứng dụng được giữ đúng vùng của ống mẫu ADN, VLA và đại bàng.

Theo AGENTS.md thay thế mới, mọi vế của công thức giữ liền mạch. Chỉ ngắt ở dấu quan hệ, không ngắt trước hoặc sau một dấu bằng bỏ trống vế, không dùng dòng tiếp với phép cộng/nhân. Công thức ngắn không bọc aligned. Các biểu thức dài dùng đại lượng trung gian có giải thích. Dữ liệu chín tích được trình bày bằng bảng thay vì một chuỗi dài.

## Tích hợp và kiểm tra

Có tám trang chủ đề, 11 Slides, bảy nhóm Cheatsheet với 18 mục chỉ gồm định nghĩa, tính chất, công thức, điều kiện và ký hiệu, cùng 12 Wiki mới. Tiên quyết được tách khỏi những khái niệm đang dạy. Tab Cheatsheet đứng ngay sau Bài tập và Vật lý 1 vẫn đứng ngay trước Vật lý 2.

151 lượt trình duyệt kiểm toàn bộ chương, 103 hộp lời giải, 11 slide, Cheatsheet và 12 Wiki ở 320, 360, 375, 1440 px, cùng bảy lần đổi bề rộng trực tiếp. Có thêm tám lượt kiểm hai trang sau bổ sung đoạn nguồn và chú thích cuối. Không phát hiện tràn công thức, TeX thô, ảnh hỏng hay lỗi JavaScript ở lượt đạt cuối.

Lượt xem thực phát hiện Slide đầu quá rộng và một khối toán bị thụt vào danh sách, khiến văn xuôi bị đọc nhầm thành công thức. Cả hai được sửa ở nội dung và ranh giới Markdown, không thu nhỏ hoặc che phần tràn. Có 39 kiểm thử skill, tám kiểm thử bộ hiển thị toán và kiểm tra cấu trúc toàn kho đã qua.

Hai tác vụ Antigravity dùng đúng ba lượt, kết thúc với lỗi bridge NoneType. Không coi báo cáo tự nhận của agent là chứng nhận thành công. Worktree cùng bản sao theo hash được giữ và Codex tự sửa, so nguồn, tính lại và kiểm giao diện. Không gọi lượt thứ tư hoặc subagent GPT.

Toàn bộ 44 bài chưa hoàn tất. Chương 37–44 và phần còn lại của Vật lý 1 vẫn được ghi riêng là còn thiếu. Build toàn bộ và triển khai chỉ chạy trên GitHub Actions sau push.
