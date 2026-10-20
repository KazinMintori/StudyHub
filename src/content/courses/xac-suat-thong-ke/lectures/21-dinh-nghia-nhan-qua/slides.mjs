export const slides = [
  {
    "note": "21-dinh-nghia-nhan-qua",
    "title": "Khung kết quả tiềm năng Neyman-Rubin",
    "bullets": [
      "Mỗi đơn vị quan sát có hai kết quả tiềm năng: Y(1) khi can thiệp và Y(0) khi không can thiệp.",
      "Tác động can thiệp cá thể là hiệu số trực tiếp giữa hai kết quả tiềm năng đó.",
      "Kết quả quan sát thực tế phụ thuộc vào việc cá thể có thực sự nhận can thiệp hay không."
    ],
    "formula": "$$\nY_i=\\begin{cases}Y_i(1)&D_i=1,\\\\Y_i(0)&D_i=0.\\end{cases}\n$$",
    "example": "Bệnh nhân i nếu uống thuốc sẽ có huyết áp Y_i(1), nếu không uống thuốc sẽ có huyết áp Y_i(0)."
  },
  {
    "note": "21-dinh-nghia-nhan-qua",
    "title": "Vấn đề cơ bản của suy luận nhân quả",
    "bullets": [
      "Với mỗi cá thể cụ thể, ta chỉ có thể quan sát được tối đa một trong hai kết quả tiềm năng.",
      "Kết quả tiềm năng còn lại vĩnh viễn là một biến cố phản thực tế không thể quan sát.",
      "Không bao giờ có thể tính toán trực tiếp tác động nhân quả cho từng cá nhân riêng lẻ."
    ],
    "formula": "$$\n\\mathrm{ITE}_i=Y_i(1)-Y_i(0).\n$$",
    "example": "Một người đã uống thuốc thì ta không thể biết chính xác sức khỏe của họ sẽ ra sao nếu không uống."
  },
  {
    "note": "21-dinh-nghia-nhan-qua",
    "title": "Tác động can thiệp bình quân ATE",
    "bullets": [
      "Chuyển mục tiêu từ suy luận cá thể sang suy luận trung bình trên toàn bộ quần thể.",
      "ATE là kỳ vọng của hiệu số giữa hai kết quả tiềm năng trên toàn quần thể.",
      "So sánh ngây thơ giữa hai nhóm quan sát thường bị sai lệch do khác biệt xuất phát điểm.",
      "Kỳ vọng đòi hỏi các kết quả tiềm năng có kỳ vọng hữu hạn."
    ],
    "formula": "$$\n\\begin{aligned}\\mu_1&=E[Y(1)],\\\\\\mu_0&=E[Y(0)],\\\\\\mathrm{ATE}&=\\mu_1-\\mu_0.\\end{aligned}\n$$",
    "example": "Đánh giá mức tăng thu nhập bình quân của người lao động khi tham gia một chương trình đào tạo nghề."
  }
]
