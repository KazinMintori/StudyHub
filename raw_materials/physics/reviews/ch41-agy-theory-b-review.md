# Chương 41, lý thuyết B: Hồ sơ rà của tác vụ chính

Trạng thái: Bản tích hợp đã được đọc đối chiếu và sửa riêng. Đây không phải xác nhận tác vụ Antigravity thành công. Lượt thứ ba trả lỗi cầu nối NoneType. Ba bản chụp được giữ trong qa/physics/chapter41/worker-b-call1..3-snapshot. Không có lượt thứ tư. Báo cáo ban đầu mô tả sai một số ảnh và thay dữ kiện ví dụ, nên đã được thay bằng hồ sơ này.

Phạm vi: Mục 41.5–41.8, sáu ví dụ 41.6–41.11, bốn câu tự kiểm 41.5–41.8, các công thức 41.36–41.52. Mười tám PNG do nhóm B phụ trách gồm hình 41.13–41.27 và ba ảnh ứng dụng. Hình 41.13–41.15 đặt ở mục Zeeman để đúng mạch giảng.

Các sửa quan trọng:

- Ví dụ 41.7 giữ 588,995 nm và 589,592 nm. Tính lại cho 18,3902 T, làm tròn 18,4 T. Đáp số in 18,0 T không khớp các dữ kiện ấy.
- Ví dụ 41.8 giữ đủ năng lượng các mức, hai photon, độ tách bước sóng và so sánh hai bước sóng đo 121,567364 nm và 121,566824 nm ở phần đánh giá. Các giá trị đo thực sự có trong phần tiếp của nguồn.
- Ví dụ 41.9 dùng natri 3s với năng lượng −5,138 eV. Ví dụ 41.10 dùng kali 4f, so với 4d −0,94 eV, 4p −2,73 eV và 4s −4,339 eV. Giữ mở rộng Mg+ ở 3d, khoảng −6,0 eV.
- Khôi phục đủ mười hàng dung lượng phân lớp, ba mươi cấu hình electron và phần nhóm nguyên tố, dãy chuyển tiếp, đất hiếm. Chuyển bảng rộng sang danh sách có thể xuống dòng, không bỏ ô dữ liệu.
- Ứng dụng giữ men răng trong ESR, stronti-89 trong xương và các nguyên tố chì, antimon, bari của cặn thuốc súng. Loại những trường hợp khác đã bị thay vào bản đầu.
- Phân biệt mômen từ spin với spin, hệ số g không thứ nguyên với tỉ số từ cơ có đơn vị. Giữ cấu trúc tinh vi, siêu tinh vi, hai ảnh thiên văn 21 cm và ứng dụng phổ tia X.
- Phần rối nêu rõ phản đối xứng của trạng thái đầy đủ gồm cả spin. Trạng thái tích electron–proton ở câu tự kiểm không rối. Không coi mọi phép đo trên một cặp rối là tương quan hoàn hảo ở mọi cơ sở hoặc cho phép truyền tin nhanh hơn ánh sáng.
- Mở rộng vùng cắt hình 41.16, 41.19 và 41.24 để giữ nhãn. Đã nhìn lại hình và đối chiếu RGB mới. Không sửa chữ hoặc nét trong ảnh.

Kiểm tra thực tế: verify_chapter41_theory_b.py, verify_chapter41_parent.py, đo toàn bộ biểu thức bằng MathJax và kiểm giao diện theo các hồ sơ chương. Các tập lệnh chỉ chứng minh những trường hợp đã lập trình. Hồ sơ tổng kết chương ghi riêng kiểm kê, trình duyệt và các giới hạn.
