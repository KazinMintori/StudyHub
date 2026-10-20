export const slides = [
  {
    "title": "Mức ý nghĩa chặn trên sai lầm loại I",
    "bullets": [
      "Bác bỏ khi thống kê vào miền $C$. Ngoài miền đó, kết luận là chưa bác bỏ.",
      "Xác suất sai lầm loại I không vượt mức $\\alpha$, kích thước thực tế có thể nhỏ hơn.",
      "Công suất tại mỗi đối thuyết bằng một trừ xác suất sai lầm loại II."
    ],
    "formula": "$$\n\\pi(\\theta)=1-\\beta(\\theta)\n$$",
    "example": "Thay thiết kế, giảm nhiễu đo hoặc chọn kiểm định phù hợp đều có thể tăng công suất.",
    "note": "40-kiem-dinh-tham-so-va-cong-suat"
  },
  {
    "title": "Neyman–Pearson khác với xấp xỉ Wilks",
    "bullets": [
      "Neyman–Pearson cho kiểm định mạnh nhất giữa hai giả thuyết đơn.",
      "Tỷ số hợp lý nhỏ ủng hộ đối thuyết. Có thể cần ngẫu nhiên hóa ở biên.",
      "GLRT dùng tối ưu trên hai miền tham số. Wilks là kết quả tiệm cận với các điều kiện chính quy."
    ],
    "formula": "$$\n\\Lambda(x)=\\frac{L(\\theta_0;x)}{L(\\theta_1;x)}\n$$",
    "example": "Quan sát chuẩn phương sai $1$, kiểm định kỳ vọng $0$ với $2$ có miền bác bỏ $X\\ge1{,}6449$ ở mức $5\\%$.",
    "note": "40-kiem-dinh-tham-so-va-cong-suat"
  },
  {
    "title": "Phân phối kiểm định đi cùng giả thiết lấy mẫu",
    "bullets": [
      "Mẫu chuẩn độc lập dùng $z$ khi biết độ lệch chuẩn và Student khi chưa biết.",
      "Hai tỷ lệ Bernoulli độc lập dùng sai số chuẩn gộp dưới giả thuyết bằng nhau, với xấp xỉ chuẩn.",
      "Phép thử phương sai Chi bình phương và Fisher chính xác cần dữ liệu chuẩn độc lập."
    ],
    "formula": "$$\nT=\\frac{\\bar X-\\mu_0}{S/\\sqrt n}\n$$",
    "example": "Hiệu số bắt cặp chuẩn có $t=2{,}9093$ và $9$ bậc tự do cho giá trị $p$ một phía $0{,}0087$.",
    "note": "40-kiem-dinh-tham-so-va-cong-suat"
  },
  {
    "title": "Giá trị p cần quy tắc cực đoan định trước",
    "bullets": [
      "Giá trị $p$ được tính dưới giả thuyết không, không phải xác suất giả thuyết không đúng.",
      "Cách tính hai phía phụ thuộc thống kê và quy tắc đuôi. Không có một công thức chung cho mọi phân phối.",
      "Quy hoạch công suất một mẫu chuẩn, biết phương sai, cần xác định mức lệch mục tiêu trước khi lấy mẫu."
    ],
    "formula": "$$\nn\\ge\\frac{(z_\\alpha+z_\\beta)^2\\sigma^2}{\\Delta^2}\n$$",
    "example": "Để phát hiện mức lệch $3$ với $\\sigma=6$, mức một phía $5\\%$ và công suất ít nhất $80\\%$, cần $n=25$.",
    "note": "40-kiem-dinh-tham-so-va-cong-suat"
  }
]
