export const slides = [
  {
    "title": "Độ tin cậy thuộc về thủ tục lấy mẫu",
    "bullets": [
      "Tham số tổng thể cố định, còn hai đầu mút khoảng thay đổi theo mẫu.",
      "Khoảng chính xác bao phủ đúng mức danh định. Khoảng bảo thủ có thể bao phủ nhiều hơn.",
      "Pivot có phân phối không phụ thuộc tham số chưa biết."
    ],
    "formula": "$$\nP_\\theta(L\\le\\theta\\le U)\\ge1-\\alpha\n$$",
    "example": "Một khoảng đã quan sát hoặc chứa tham số hoặc không chứa, không gán xác suất hậu nghiệm cho tham số.",
    "note": "39-khoang-tin-cay-tham-so"
  },
  {
    "title": "Khoảng Student chính xác cần mẫu chuẩn",
    "bullets": [
      "Mẫu chuẩn độc lập, phương sai chưa biết dùng phân vị Student.",
      "Với dữ liệu bắt cặp, cần các hiệu số độc lập và phân phối chuẩn.",
      "Hai mẫu độc lập khác phương sai dùng Welch, một phép xấp xỉ ngay cả khi hai tổng thể chuẩn."
    ],
    "formula": "$$\n\\bar X\\pm t_{\\alpha/2,n-1}\\frac{S}{\\sqrt n}\n$$",
    "example": "Với $n=16$, $\\bar x=22{,}5$ và $s=4$, khoảng $95\\%$ là $[20{,}37,24{,}63]$.",
    "note": "39-khoang-tin-cay-tham-so"
  },
  {
    "title": "Wilson tránh thoái hóa ở biên nhưng vẫn xấp xỉ",
    "bullets": [
      "Wald dùng phương sai ước tính từ tỷ lệ mẫu, có thể thoái hóa khi không có thành công.",
      "Wilson đảo kiểm định điểm số và cho hai đầu mút trong $[0,1]$.",
      "Clopper–Pearson bảo đảm bao phủ ít nhất mức danh định trong mô hình nhị thức."
    ],
    "formula": "$$\n(\\hat p-p)^2\\le\\frac{z^2p(1-p)}{n}\n$$",
    "example": "Với $6$ thành công trên $40$ phép thử, khoảng Wilson $95\\%$ là $[0{,}0706,0{,}2907]$.",
    "note": "39-khoang-tin-cay-tham-so"
  },
  {
    "title": "Khoảng phương sai và quy hoạch cỡ mẫu",
    "bullets": [
      "Mẫu chuẩn cho Pivot Chi bình phương của phương sai. Hai mẫu chuẩn độc lập cho Pivot Fisher.",
      "Giá trị tới hạn đuôi phải mức $\\alpha$ là phân vị tích lũy mức $1-\\alpha$.",
      "Cỡ mẫu từ công thức chuẩn được làm tròn lên, với các giả thiết lập kế hoạch đã nêu."
    ],
    "formula": "$$\nn\\ge\\left(\\frac{z_{\\alpha/2}\\sigma}{E}\\right)^2\n$$",
    "example": "Sai số tỷ lệ $0{,}03$ là ba điểm phần trăm. Hai tỷ lệ chênh $0{,}09$ là chín điểm phần trăm.",
    "note": "39-khoang-tin-cay-tham-so"
  }
]
