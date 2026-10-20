export const slides = [
  {
    "note": "22-thi-nghiem-ngau-nhien",
    "title": "Thử nghiệm ngẫu nhiên có đối chứng RCT",
    "bullets": [
      "Được xem là tiêu chuẩn vàng để xác lập mối quan hệ nhân quả vững chắc.",
      "Phân bổ can thiệp ngẫu nhiên hoàn toàn độc lập với các đặc tính tiềm ẩn của đối tượng.",
      "Đảm bảo nhóm can thiệp và nhóm đối chứng có đặc tính xuất phát điểm cân bằng."
    ],
    "formula": "$$\nD \\perp \\{Y(0), Y(1)\\}\n$$",
    "example": "Thử nghiệm vắc-xin chia ngẫu nhiên người tình nguyện thành nhóm tiêm vắc-xin và nhóm tiêm giả dược."
  },
  {
    "note": "22-thi-nghiem-ngau-nhien",
    "title": "Triệt tiêu sai lệch chọn lựa",
    "bullets": [
      "Phân bổ ngẫu nhiên làm triệt tiêu sai lệch chọn lựa trong so sánh trung bình mẫu.",
      "Kỳ vọng của kết quả phản thực tế trong nhóm can thiệp bằng kỳ vọng nhóm đối chứng.",
      "Hiệu số trung bình quan sát là ước lượng không chệch cho tác động can thiệp ATE.",
      "Đặt μ₀ = E[Y(0)]. Đẳng thức được suy ra từ phép phân nhóm ngẫu nhiên và kỳ vọng hữu hạn."
    ],
    "formula": "$$\n\\begin{aligned}&E[Y(0)\\mid D=1]=\\mu_0,\\\\&E[Y(0)\\mid D=0]=\\mu_0.\\end{aligned}\n$$",
    "example": "Nhờ ngẫu nhiên hóa, nhóm can thiệp và nhóm đối chứng có cùng tỷ lệ mắc bệnh nền ban đầu như nhau."
  },
  {
    "note": "22-thi-nghiem-ngau-nhien",
    "title": "Kỹ thuật thử nghiệm mù và hiệu ứng giả dược",
    "bullets": [
      "Hiệu ứng giả dược là sự thay đổi tâm lý hoặc sức khỏe do tin rằng mình đang được điều trị.",
      "Thiết kế làm mù đơn ngăn người tham gia biết mình thuộc nhóm can thiệp hay đối chứng.",
      "Làm mù đôi ngăn cả bác sĩ điều trị lẫn người tham gia biết nhãn phân bổ điều trị."
    ],
    "formula": "",
    "example": "Cho nhóm đối chứng uống viên đường có hình thức giống hệt viên thuốc điều trị để đo lường hiệu ứng giả dược."
  }
]
