# Trạng thái Vật lý đại cương1, ngày23/10/2026

Bảy chương ưu tiên đã hoàn tất biên tập nội dung và rà soát cục bộ:9,10,11 về quay và cân bằng vật rắn, cùng17–20 về nhiệt học và nhiệt động lực học. Trạng thái xuất bản vẫn phải xác nhận bằng lượt GitHub Actions của chính commit được push.

| Chương | Mục lý thuyết | Ví dụ | Luyện tập | Thảo luận | Bài đánh số | Cầu nối | Lời giải gập |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 9 | 6 | 11 | 12 | 22 | 95 | 1 | 130 |
| 10 | 7 | 13 | 12 | 30 | 97 | 1 | 140 |
| 11 | 5 | 7 | 12 | 25 | 95 | 1 | 133 |
| 17 | 7 | 15 | 12 | 28 | 119 | 1 | 160 |
| 18 | 6 | 8 | 12 | 30 | 87 | 1 | 130 |
| 19 | 8 | 7 | 12 | 24 | 66 | 1 | 103 |
| 20 | 8 | 11 | 12 | 23 | 62 | 1 | 98 |

Tổng có47 mục, 82 ví dụ và894 đề cuối chương với lời giải gập, chia162 nhóm. Các ví dụ và câu tự kiểm xuất hiện trong mạch giảng vẫn ở Notes. Bài tập cuối chương có đề, hình tương ứng, tóm tắt, hướng đi giải thích cách chọn công thức và các bước giải.

Các bản nghiệm thu chi tiết ởchapter-09-review.json, chapter-10-review.json, chapter-11-review.json, chapter-17-review.json, chapter-18-review.json, chapter-19-review.json vàchapter-20-review.json trong thư mục cha. Những sai khác dữ kiện, cách đọc hình và giả thiết mô hình có hồ sơ riêng.

Đã chạy kiểm tra cấu trúc từng chương và đo độ rộng toàn bộ công thức. Rà trình duyệt ở320,360,375,1440 px gồm Notes, các chủ đề, Slides, Cheatsheet và nhóm bài tập. Chương17 và20 có thêm phép kiểm HTML nhóm xuất bản trong bộ xem thử tĩnh dùng CSS và phông chữ dự án. Phép kiểm bổ sung đó không thay cho việc kiểm chứng vật lý hoặc kiểm lại toàn bộ điều hướngVue.

Bộ kiểm thử dự án146 ca, công cụ bài giảng39 ca và tính năng112 ca đã đạt sau khi tích hợp các cập nhật giao diện từmain. Kết quả cuối trước push cần ghi ở hồ sơ xuất bản của đợt này. Không có build toàn cục nào chạy trên máy người dùng.

Hai deploy giao diện cũ39910661772 và39908565361 thất bại ở kiểm tra mã màu. Đã sửa13 dòng bằng biến thiết kế và push riêng commit40a8a0f5. Lượt39922770906 đang được theo dõi. Không sửa lịch sử để biến các lượt cũ thành thành công.

Dọn tệp đã qua một tác vụAntigravity riêng. Hai hồ sơ cũ được chuyển vàoarchive, công cụ đo công thức được lưu chính thức ởscripts/verification/measure-physics-math.mjs, hai verifier bỏ phụ thuộc đường dẫn worktree riêng. Tư liệu nguồn, ảnh, lời giải, công cụ tái lập và bằng chứng rà soát đều được giữ.

Báo cáo củaAntigravity là đầu vào thẩm định. Các kết luận sai về hình10.1, đường dẫn ảnh và dữ kiện20.44 đã được đối chiếu lại, không áp dụng máy móc. Lỗi đọc hình11.10 được xác nhận và sửa. Không cam kết một phần trăm độ chính xác tuyệt đối.
