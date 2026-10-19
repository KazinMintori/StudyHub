# Công cụ đã dùng

Codex điều phối, viết, kiểm tra và sửa mã. Antigravity được giao tạo bản nháp mô-đun, sau đó đọc lại bản sửa và xây các trường hợp kiểm thử. Không dùng công cụ này để tạo nhãn người hoặc khai accuracy/F1chưa đo.

## Các yêu cầu quan trọng

1. Giữ nguyên nguồn và snapshot, không tự thay dữ liệu thiếu bằng fixture.
2. Dùng giao listingIDcó seed và giải thích thiên lệch của mẫu.
3. Đọc calendar theo luồng với cửa sổ ngày tường minh.
4. Review duy nhất được phân biệt với lần xuất hiện theo snapshot.
5. Mỗi KPIcó điều kiện dùng dòng và mẫu số.
6. Không dùng lịch không sẵn có để khẳng định giao dịch hay doanh thu.
7. Tệp nhãn người bắt đầu trống và không bị ghi đè khi chạy lại.
8. Cache mô hình phụ thuộc nội dung và tham số, lỗi không coi là thành công.
9. Hình phải được sinh từ dữ liệu thật của lần chạy.

## Những lỗi trong bản nháp đã được sửa

Bản nháp ban đầu tự sinh dữ liệu giả nếu nguồn không có và dùng hình học thay thế khi thiếu GeoJSON. Hai cơ chế này bị loại bỏ. Các phép tự điền giá trị thiếu và chuẩn hóa trạng thái lịch không hợp lệ thành `false` cũng bị loại bỏ.

Bản tính ban đầu ngoại suy số ngày sẵn có từ lịch chưa đầy đủ và dùng0khi không quan sát được. Bản sửa giữ mẫu số ngày hợp lệ và báo độ phủ riêng. Mẫu review duy nhất không được nhân thành bốn tập ý kiến khi tính KPI.

Một số lời mô tả QAquá chắc chắn hoặc chưa có bằng chứng không được giữ. Các số liệu trên trang kết quả được đối chiếu độc lập bằng Python.

## Cách kiểm chứng

Kiểm thử dữ liệu giả định chỉ để xác minh biên ngày, khóa, số tiền, mẫu số, cache và phép chấm nhãn. Lần chạy công khai đọc đủ nguồn thật, lưu manifest, tính lại bằng chương trình độc lập và xem từng hình. Các nhận xét của tác tử được đọc lại, không nhận tự động vì có báo cáo thành công.
