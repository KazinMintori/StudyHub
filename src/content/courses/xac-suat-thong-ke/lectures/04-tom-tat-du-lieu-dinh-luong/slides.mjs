export const slides = [
  {
    "note": "04-tom-tat-du-lieu-dinh-luong",
    "title": "Thước đo vị trí trung tâm",
    "bullets": [
      "Trung bình cộng nhạy cảm với các giá trị ngoại lai cực đoan.",
      "Trung vị là điểm chia đôi tập dữ liệu, có tính bền vững cao.",
      "Với phân phối lệch phải, trung bình thường lớn hơn trung vị."
    ],
    "formula": "$$\n\\bar{x} = \\frac{1}{n} \\sum_{i=1}^n x_i\n$$",
    "example": "Thu nhập trung bình bị kéo cao bởi các tỷ phú, trong khi thu nhập trung vị phản ánh mức sống phổ biến."
  },
  {
    "note": "04-tom-tat-du-lieu-dinh-luong",
    "title": "Thước đo độ phân tán",
    "bullets": [
      "Phương sai mẫu chia cho n - 1 để đảm bảo tính không chệch.",
      "Độ lệch chuẩn s có cùng đơn vị đo với biến gốc.",
      "Khoảng tứ phân vị IQR bằng Q3 trừ Q1, bền vững trước ngoại lai."
    ],
    "formula": "$$\ns = \\sqrt{\\frac{1}{n-1} \\sum_{i=1}^n (x_i - \\bar{x})^2}\n$$",
    "example": "Tập dữ liệu điểm số có trung bình 75 điểm và độ lệch chuẩn 10 điểm."
  },
  {
    "note": "04-tom-tat-du-lieu-dinh-luong",
    "title": "Biểu đồ hộp và phát hiện ngoại lai",
    "bullets": [
      "Hộp biểu diễn 50% dữ liệu trung tâm từ Q1 đến Q3.",
      "Đường bên trong hộp đánh dấu trung vị của phân phối.",
      "Điểm nằm ngoài khoảng [Q1 - 1,5 IQR, Q3 + 1,5 IQR] được xem là ngoại lai tiềm năng."
    ],
    "formula": "$$\n\\text{IQR} = Q_3 - Q_1\n$$",
    "example": "Khoảng tứ phân vị IQR = 20, điểm nằm cách ranh giới quá 30 đơn vị là ngoại lai."
  }
]
