export const slides = [
  {
    "note": "08-hoi-quy-tuyen-tinh-boi",
    "title": "Mô hình hồi quy tuyến tính bội",
    "bullets": [
      "Mở rộng mô hình tuyến tính đơn cho k biến dự báo đồng thời.",
      "Cho phép dự báo kết quả dựa trên tổ hợp tuyến tính của nhiều biến giải thích.",
      "Mỗi hệ số hồi quy đo lường tác động riêng phần của biến tương ứng."
    ],
    "formula": "$$\n\\begin{aligned}u_j&=b_jx_j,\\\\\\hat y&=b_0+u_1+\\dots+u_k.\\end{aligned}\n$$",
    "example": "Dự báo giá nhà dựa trên diện tích sàn, số phòng ngủ và tuổi thọ công trình."
  },
  {
    "note": "08-hoi-quy-tuyen-tinh-boi",
    "title": "Ý nghĩa kiểm soát Ceteris Paribus",
    "bullets": [
      "Hệ số b_j phản ánh mức thay đổi kỳ vọng của y khi x_j tăng 1 đơn vị và giữ cố định các biến khác.",
      "Giúp loại bỏ ảnh hưởng gây nhiễu giữa các biến độc lập có tương quan với nhau.",
      "Tác động riêng phần có thể khác biệt hoàn toàn so với hệ số hồi quy đơn biến."
    ],
    "formula": "",
    "example": "Khi kiểm soát kích thước xe, mã lực động cơ vẫn có tác động độc lập tới mức tiêu thụ nhiên liệu."
  },
  {
    "note": "08-hoi-quy-tuyen-tinh-boi",
    "title": "Hệ số xác định đa biến và đánh giá mô hình",
    "bullets": [
      "R^2 đo tỷ lệ biến thiên của biến phụ thuộc được giải thích bởi mô hình.",
      "R^2 luôn tăng khi thêm biến mới, dễ gây đánh giá sai lầm.",
      "R^2 hiệu chỉnh áp dụng hình phạt theo số lượng tham số để tránh quá khớp."
    ],
    "formula": "$$\nR^2 = 1 - \\frac{\\text{SSE}}{\\text{SST}}\n$$",
    "example": "Mô hình đạt R^2 = 0,72 nghĩa là 72% phương sai của biến mục tiêu được giải thích."
  }
]
