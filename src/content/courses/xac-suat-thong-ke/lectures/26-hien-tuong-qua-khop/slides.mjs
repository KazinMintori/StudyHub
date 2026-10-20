export const slides = [
  {
    "note": "26-hien-tuong-qua-khop",
    "title": "Hiện tượng quá khớp Overfitting",
    "bullets": [
      "Mô hình quá phức tạp khớp vào cả nhiễu ngẫu nhiên của tập dữ liệu huấn luyện.",
      "Sai số trên tập huấn luyện rất nhỏ nhưng sai số trên dữ liệu kiểm thử mới lại tăng vọt.",
      "Khả năng khái quát hóa và dự báo thực tế bị suy giảm nghiêm trọng."
    ],
    "formula": "",
    "example": "Đa thức bậc 9 khớp hoàn hảo 10 điểm huấn luyện nhưng dao động hỗn loạn giữa các điểm."
  },
  {
    "note": "26-hien-tuong-qua-khop",
    "title": "Phân chia tập dữ liệu Train và Test",
    "bullets": [
      "Tách dữ liệu thành hai tập độc lập: Tập huấn luyện để khớp mô hình, tập kiểm thử để đánh giá.",
      "Tỷ lệ phân chia thông dụng là 70/30 hoặc 80/20.",
      "Tuyệt đối không sử dụng tập kiểm thử trong quá trình huấn luyện hay tinh chỉnh tham số."
    ],
    "formula": "",
    "example": "Dùng 80% dữ liệu để ước lượng các hệ số hồi quy và dùng 20% còn lại để kiểm tra sai số dự báo."
  },
  {
    "note": "26-hien-tuong-qua-khop",
    "title": "Kiểm định chéo K-lần K-Fold Cross Validation",
    "bullets": [
      "Chia dữ liệu thành K phần bằng nhau, lần lượt dùng 1 phần làm kiểm thử và K - 1 phần làm huấn luyện.",
      "Trung bình hóa sai số qua K lượt để có ước lượng khách quan về hiệu năng mô hình.",
      "Giúp tận dụng tối đa dữ liệu mà không làm rò rỉ thông tin kiểm định."
    ],
    "formula": "$$\n\\text{CV}_{(K)} = \\frac{1}{K} \\sum_{k=1}^K \\text{MSE}_k\n$$",
    "example": "Kiểm định chéo 5 lần chia dữ liệu thành 5 khối, luân phiên huấn luyện và đánh giá 5 lần."
  }
]
