export const slides = [
  {
    "note": "bai-12-mo-hinh-hoa",
    "title": "Từ DataFrame đến ma trận thiết kế",
    "bullets": [
      "Kiểm cột, dtype, thiếu dữ liệu và thứ tự trước khi đưa vào mô hình.",
      "Mã hóa biến phân loại phải phù hợp với mô hình và quy tắc tham chiếu."
    ],
    "formula": "",
    "example": "Một mô hình tuyến tính có intercept cần chú ý phụ thuộc giữa các cột biến giả."
  },
  {
    "note": "bai-12-mo-hinh-hoa",
    "title": "Patsy mô tả cấu trúc mô hình",
    "bullets": [
      "Công thức có thể thêm intercept, biến đổi số và biến phân loại.",
      "Khi dự đoán, dùng lại quy tắc tạo đặc trưng đã học trên dữ liệu huấn luyện."
    ],
    "formula": "",
    "example": "I(x0 + x1) bảo vệ phép cộng số học trong công thức."
  },
  {
    "note": "bai-12-mo-hinh-hoa",
    "title": "Hệ số, phần dư và suy diễn có điều kiện",
    "bullets": [
      "Tính nghiệm hồi quy và suy diễn về hệ số là hai việc khác nhau.",
      "Đọc sai số chuẩn và giá trị p cùng các giả thiết, đơn vị và mức độ phụ thuộc của dữ liệu."
    ],
    "formula": "",
    "example": "Hệ số có ý nghĩa thống kê chưa tự chứng minh tác động nhân quả."
  },
  {
    "note": "bai-12-mo-hinh-hoa",
    "title": "Đánh giá phải tách khỏi việc học",
    "bullets": [
      "Fit tiền xử lý trên tập huấn luyện, rồi dùng cùng phép biến đổi cho tập kiểm tra.",
      "Pipeline giúp tổ chức quy trình nhưng không tự phát hiện mọi nguồn rò rỉ."
    ],
    "formula": "",
    "example": "Dữ liệu thời gian hoặc nhiều hàng của cùng thực thể cần cách chia phù hợp."
  }
]
