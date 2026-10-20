export const slides = [
  {
    "note": "16-khoang-tin-cay",
    "title": "Bản chất tần suất của khoảng tin cậy",
    "bullets": [
      "Khoảng tin cậy là một khoảng ngẫu nhiên với hai đầu mút biến thiên theo từng mẫu.",
      "Độ tin cậy 95% nghĩa là 95% các khoảng tạo ra sẽ bao phủ tham số cố định.",
      "Không được phát biểu rằng có xác suất 95% tham số rơi vào một khoảng số cụ thể đã tính.",
      "Hai đầu mút L và U ngẫu nhiên. Mức bao phủ đúng hay xấp xỉ phụ thuộc phương pháp và giả thiết, không tự động đúng cho mọi khoảng dạng ước lượng ± sai số."
    ],
    "formula": "$$\nP_\\theta(L\\le\\theta\\le U)\\ge1-\\alpha.\n$$",
    "example": "Thực hiện lấy 100 mẫu độc lập, trung bình sẽ có khoảng 95 khoảng tin cậy bao trùm đúng tham số thực."
  },
  {
    "note": "16-khoang-tin-cay",
    "title": "Khoảng tin cậy cho tỷ lệ tổng thể",
    "bullets": [
      "Dựa trên xấp xỉ chuẩn cho biến nhị thức khi thỏa mãn điều kiện thành công thất bại.",
      "Giá trị tới hạn z* lấy từ phân phối chuẩn chuẩn hóa (z* = 1,96 cho mức 95%).",
      "Sai số chuẩn được ước lượng từ tỷ lệ mẫu quan sát."
    ],
    "formula": "$$\n\\hat{p} \\pm z^* \\sqrt{\\frac{\\hat{p}(1-\\hat{p})}{n}}\n$$",
    "example": "Khảo sát n = 100 cử tri có 36 người ủng hộ, khoảng tin cậy 95% cho tỷ lệ ủng hộ là [26,6%, 45,4%]."
  },
  {
    "note": "16-khoang-tin-cay",
    "title": "Khoảng tin cậy cho trung bình tổng thể",
    "bullets": [
      "Khi chưa biết phương sai tổng thể, sử dụng độ lệch chuẩn mẫu s để ước lượng SE.",
      "Sử dụng phân phối Student t với n - 1 bậc tự do cho cỡ mẫu nhỏ.",
      "Khi cỡ mẫu n đủ lớn, phân phối t tiệm cận về phân phối chuẩn chuẩn hóa."
    ],
    "formula": "$$\n\\bar{x} \\pm t_{n-1}^* \\frac{s}{\\sqrt{n}}\n$$",
    "example": "Mẫu n = 50 có trung bình 86,27 và độ lệch chuẩn mẫu 7,0, khoảng tin cậy 95% là [84,33, 88,21]."
  }
]
