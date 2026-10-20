export const slides = [
  {
    "note": "23-tac-dong-nhan-qua-nghien-cuu-quan-sat",
    "title": "Thách thức biến gây nhiễu trong nghiên cứu quan sát",
    "bullets": [
      "Người tham gia tự lựa chọn việc nhận can thiệp chứ không được phân bổ ngẫu nhiên.",
      "Biến gây nhiễu đồng thời ảnh hưởng lên quyết định can thiệp và kết quả đầu ra.",
      "So sánh trung bình thô phản ánh hỗn hợp giữa tác động nhân quả và sai lệch chọn lựa."
    ],
    "formula": "",
    "example": "Người chọn học đại học vốn có điều kiện kinh tế và động lực cao hơn người không học đại học."
  },
  {
    "note": "23-tac-dong-nhan-qua-nghien-cuu-quan-sat",
    "title": "Giả định khả gán mạnh Conditional Ignorability",
    "bullets": [
      "Giả định rằng khi đã kiểm soát tập biến quan sát X, việc can thiệp độc lập với kết quả tiềm năng.",
      "Đòi hỏi điều kiện bao phủ: Mọi cá thể đều có xác suất dương nhận can thiệp hoặc đối chứng.",
      "Không thể kiểm tra thực nghiệm giả định này vì kết quả phản thực tế không quan sát được."
    ],
    "formula": "$$\nD \\perp \\{Y(0), Y(1)\\} \\mid X\n$$",
    "example": "So sánh bệnh nhân có cùng độ tuổi, giới tính và tình trạng bệnh nền để ước lượng tác động điều trị."
  },
  {
    "note": "23-tac-dong-nhan-qua-nghien-cuu-quan-sat",
    "title": "Phương pháp ghép cặp và Điểm xu hướng",
    "bullets": [
      "Ghép cặp mỗi cá thể can thiệp với một hoặc nhiều cá thể đối chứng có đặc tính X tương đồng.",
      "Điểm xu hướng rút gọn không gian đa biến X về xác suất một chiều nhận can thiệp.",
      "Giúp cân bằng phân phối của các biến gây nhiễu giữa hai nhóm so sánh."
    ],
    "formula": "$$\ne(X) = P(D = 1 \\mid X)\n$$",
    "example": "Ghép cặp các trường học có cùng ngân sách và tỷ lệ học sinh nghèo để đánh giá hiệu quả chương trình giáo dục."
  }
]
