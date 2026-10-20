export const slides = [
  {
    "note": "17-phuong-phap-bootstrapping",
    "title": "Nguyên lý cắm mẫu Bootstrap",
    "bullets": [
      "Xem mẫu dữ liệu hiện có như một quần thể đại diện thu nhỏ.",
      "Tái lấy mẫu có hoàn lại từ dữ liệu gốc với kích thước đúng bằng cỡ mẫu ban đầu n.",
      "Lặp lại quy trình hàng nghìn lần để mô phỏng biến thiên chọn mẫu thực nghiệm."
    ],
    "formula": "",
    "example": "Từ mẫu 100 quan sát, rút ngẫu nhiên có hoàn lại 100 phần tử để tạo ra một mẫu bootstrap mới."
  },
  {
    "note": "17-phuong-phap-bootstrapping",
    "title": "Ước lượng sai số chuẩn Bootstrap",
    "bullets": [
      "Tính toán giá trị thống kê quan tâm trên từng mẫu bootstrap đã tạo ra.",
      "Sai số chuẩn bootstrap là độ lệch chuẩn thực nghiệm của các thống kê bootstrap đó.",
      "Áp dụng được cho các thống kê phức tạp không có công thức giải tích đóng."
    ],
    "formula": "$$\n\\begin{aligned}v_b&=(\\hat\\theta_b^*-\\bar\\theta^*)^2,\\\\\\widehat{\\mathrm{SE}}_{\\mathrm{boot}}&=\\sqrt{\\frac{v_1+\\dots+v_B}{B-1}}.\\end{aligned}\n$$",
    "example": "Ước lượng sai số chuẩn cho hệ số tương quan hoặc trung vị mẫu mà không cần giả định phân phối chuẩn."
  },
  {
    "note": "17-phuong-phap-bootstrapping",
    "title": "Khoảng tin cậy Bootstrap phân vị",
    "bullets": [
      "Sắp xếp các giá trị thống kê bootstrap theo thứ tự tăng dần.",
      "Lấy trực tiếp các phân vị alpha/2 và 1 - alpha/2 làm hai đầu mút của khoảng tin cậy.",
      "Không đòi hỏi phân phối của thống kê phải đối xứng hay chuẩn mực.",
      "q* là phân vị của các ước lượng bootstrap. Khoảng phân vị là xấp xỉ và không bảo đảm mức bao phủ đúng trong mọi bài toán."
    ],
    "formula": "$$\n\\mathrm{CI}_{1-\\alpha}=[q_{\\alpha/2}^*,q_{1-\\alpha/2}^*].\n$$",
    "example": "Với B = 1000 mẫu bootstrap, khoảng tin cậy 95% lấy từ giá trị thứ 25 đến giá trị thứ 975."
  }
]
