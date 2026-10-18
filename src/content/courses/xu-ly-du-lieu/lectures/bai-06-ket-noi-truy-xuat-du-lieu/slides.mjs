export const slides = [
  {
    "note": "bai-06-ket-noi-truy-xuat-du-lieu",
    "title": "Đọc đúng trước khi tổng hợp",
    "bullets": [
      "Khai báo cột mã, ngày, dấu phân cách và quy ước giá thiếu khi cần.",
      "Đọc theo khối phải giữ các thống kê đủ để gộp đúng kết quả."
    ],
    "formula": "",
    "example": "Trung bình gộp cần tổng và số giá hợp lệ, không chỉ trung bình của từng khối."
  },
  {
    "note": "bai-06-ket-noi-truy-xuat-du-lieu",
    "title": "Chọn định dạng theo cách sử dụng",
    "bullets": [
      "CSV cần quy ước đọc lại, Parquet hỗ trợ schema và đọc chọn cột.",
      "JSON, XML, HTML và Excel có cấu trúc cần được kiểm tra trước khi tạo bảng."
    ],
    "formula": "",
    "example": "Không giải tuần tự hóa pickle từ nguồn không đáng tin."
  },
  {
    "note": "bai-06-ket-noi-truy-xuat-du-lieu",
    "title": "API cần kiểm phản hồi và giữ dữ liệu gốc",
    "bullets": [
      "Đặt timeout và kiểm trạng thái HTTP trước khi đọc JSON.",
      "Ghi byte phản hồi cùng tham số, thời điểm lấy để đối chiếu về sau."
    ],
    "formula": "",
    "example": "Một bảng ngày chỉ ghép đúng khi hai nguồn thống nhất lịch và múi giờ."
  },
  {
    "note": "bai-06-ket-noi-truy-xuat-du-lieu",
    "title": "SQL lọc hàng và lọc nhóm ở hai bước",
    "bullets": [
      "WHERE chọn hàng trước tổng hợp, HAVING chọn nhóm sau tổng hợp.",
      "COUNT(*) đếm hàng, còn COUNT(cột) không đếm ô NULL."
    ],
    "formula": "",
    "example": "Kiểm số dòng và khóa trước, sau LEFT JOIN để phát hiện nhân dòng."
  }
]
