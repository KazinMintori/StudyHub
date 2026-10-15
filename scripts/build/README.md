# Build trên GitHub

Lệnh `npm run ci:build` chỉ chạy khi `GITHUB_ACTIONS=true`. Trên máy cá nhân, dùng trình kiểm tra bài giảng và máy chủ dev khi cần xem giao diện.

VitePress biên dịch cả phía trình duyệt và phía máy chủ trong cùng một tiến trình. Với nhiều trang chứa SVG toán học, một lần build toàn bộ đã vượt giới hạn heap 12 GiB trên runner 15 GiB. Trình điều phối chia danh sách trang thành các đợt tuần tự, mỗi đợt chạy trong một tiến trình Node riêng với heap tối đa 8 GiB. Tiến trình kết thúc trước khi bắt đầu đợt tiếp theo.

Mỗi đợt nhận tối đa 100 trang và khoảng 768 KiB Markdown, kể cả nội dung được chèn bằng `@include`. Một trang lớn hơn ngưỡng được giữ nguyên và xử lý riêng. Đây là ngưỡng phân chia đầu vào, không phải cam kết về lượng RAM. Log ghi lại mức RSS cao nhất của từng tiến trình để theo dõi.

Kết quả được ghép trong thư mục tạm. Tệp có cùng đường dẫn phải có nội dung giống nhau, ngoại trừ trang 404 được giữ từ đợt đầu và các quy tắc biểu tượng được hợp nhất. Mọi trang HTML do VitePress tạo nhận cùng một bản đồ đường dẫn hoàn chỉnh. Tài liệu HTML trong `public` được giữ nguyên. Trình ghép kiểm tra đủ trang và đủ cả hai dạng chunk trước khi chuyển kết quả sang `dist` để tải lên GitHub Pages.

Các chế độ MPA, metadata tách riêng, sitemap và tìm kiếm cục bộ cần cơ chế hợp nhất riêng. Nếu được bật trong cấu hình, bước lập kế hoạch sẽ dừng rõ lỗi để tránh tạo đầu ra thiếu dữ liệu.

Kiểm tra nhẹ tại máy cá nhân: `node --test scripts/tests/batch-build.test.mjs`. GitHub còn chạy một website mẫu bốn trang, chia thành hai đợt, để kiểm tra chuyển trang SPA giữa các đợt, hydration, SVG toán học, ảnh và hộp lời giải. Toàn bộ website chỉ được build sau khi mẫu này đạt.
