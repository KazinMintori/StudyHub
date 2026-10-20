export const slides = [
  {
    "note": "24-phuong-phap-binh-phuong-be-nhat",
    "title": "Nguyên lý bình phương tối thiểu OLS",
    "bullets": [
      "Tìm đường thẳng hồi quy sao cho tổng bình phương của các phần dư là nhỏ nhất.",
      "Hàm mục tiêu lồi bậc hai đảm bảo tồn tại nghiệm tối ưu duy nhất.",
      "Phạt nặng hơn đối với các sai số lớn do cơ chế bình phương khoảng cách."
    ],
    "formula": "$$\n\\begin{aligned}e_i&=y_i-b_0-b_1x_i,\\\\\\mathrm{RSS}&=e_1^2+\\dots+e_n^2,\\\\\\hat{\\mathbf b}&=\\arg\\min_{\\mathbf b}\\mathrm{RSS}(\\mathbf b).\\end{aligned}\n$$",
    "example": "Tối ưu hóa vị trí đường hồi quy trên tập dữ liệu gồm 5 điểm quan sát."
  },
  {
    "note": "24-phuong-phap-binh-phuong-be-nhat",
    "title": "Hệ phương trình chuẩn tắc và nghiệm OLS",
    "bullets": [
      "Lấy đạo hàm riêng theo các hệ số và cho bằng 0 để thiết lập hệ phương trình chuẩn tắc.",
      "Đường hồi quy tối ưu luôn luôn đi qua điểm trọng tâm trung bình của mẫu dữ liệu.",
      "Hệ số độ dốc tỷ lệ với tỷ số giữa hiệp phương sai mẫu và phương sai mẫu của x.",
      "Cần Sxx > 0. Hai tổng chạy từ i = 1 đến n và là tổng tích độ lệch hoặc tổng bình phương độ lệch."
    ],
    "formula": "$$\n\\begin{aligned}S_{xy}&=\\sum_{i=1}^n(x_i-\\bar x)(y_i-\\bar y),\\\\S_{xx}&=\\sum_{i=1}^n(x_i-\\bar x)^2,\\\\b_1&=S_{xy}/S_{xx},\\\\b_0&=\\bar y-b_1\\bar x.\\end{aligned}\n$$",
    "example": "Tính toán độ dốc b1 = 1,2 và hệ số chặn b0 = 0,4 từ số liệu tóm tắt mẫu."
  },
  {
    "note": "24-phuong-phap-binh-phuong-be-nhat",
    "title": "Các tính chất đại số của phần dư tối ưu",
    "bullets": [
      "Tổng và giá trị trung bình của toàn bộ các phần dư luôn luôn bằng đúng 0.",
      "Tích vô hướng giữa phần dư và biến giải thích x luôn bằng 0 (tính trực giao).",
      "Trung bình của các giá trị dự báo luôn bằng đúng trung bình của dữ liệu thực tế.",
      "Khai triển tổng thứ hai: x₁e₁ + x₂e₂ + ⋯ + xₙeₙ = 0. Các đẳng thức áp dụng cho nghiệm OLS có hệ số chặn."
    ],
    "formula": "$$\n\\begin{aligned}&\\sum_{i=1}^n e_i=0,\\\\&\\sum_{i=1}^n x_ie_i=0.\\end{aligned}\n$$",
    "example": "Kiểm tra tính đúng đắn của phép tính hồi quy bằng cách xác minh tổng 5 phần dư bằng 0."
  }
]
