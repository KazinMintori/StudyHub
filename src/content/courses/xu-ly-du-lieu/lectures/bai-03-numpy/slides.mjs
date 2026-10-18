export const slides = [
  {
    "note": "bai-03-numpy",
    "title": "Đọc shape, dtype và số byte",
    "bullets": [
      "shape nêu kích thước các trục, ndim nêu số trục.",
      "nbytes bằng size nhân itemsize, không tính siêu dữ liệu hoặc lượng cấp phát mới của một view."
    ],
    "formula": "",
    "example": "A có shape (4, 3), dtype int64 nên có nbytes bằng 96."
  },
  {
    "note": "bai-03-numpy",
    "title": "Chọn dữ liệu và kiểm tra dùng chung bộ nhớ",
    "bullets": [
      "Lát cắt cơ bản thường tạo view, còn đọc bằng mảng chỉ mục tạo bản sao dữ liệu.",
      "reshape có thể dùng lại bộ nhớ hoặc phải sao chép tùy strides và thứ tự được yêu cầu."
    ],
    "formula": "",
    "example": "Dùng np.shares_memory để kiểm tra hai mảng cụ thể, thay vì chỉ nhìn thuộc tính base."
  },
  {
    "note": "bai-03-numpy",
    "title": "Broadcasting phải khớp đúng trục",
    "bullets": [
      "So các trục từ phải sang trái, mỗi cặp cần bằng nhau hoặc có một trục dài 1.",
      "Trung bình theo hàng cần giữ trục phù hợp trước khi trừ khỏi từng hàng."
    ],
    "formula": "",
    "example": "A + b + d[:, None] cộng b theo cột và d theo hàng khi shape phù hợp."
  },
  {
    "note": "bai-03-numpy",
    "title": "Tính trên mảng và mô phỏng có điều kiện",
    "bullets": [
      "Các phép toán số thường giảm công việc lặp ở tầng Python, nhưng hiệu năng cần được đo.",
      "Dùng generator ngẫu nhiên và kiểm tra điều kiện chạm ngưỡng trước khi lấy argmax."
    ],
    "formula": "",
    "example": "Một đường đi chưa chạm ngưỡng vẫn có argmax bằng 0 trên mask toàn False."
  }
]
