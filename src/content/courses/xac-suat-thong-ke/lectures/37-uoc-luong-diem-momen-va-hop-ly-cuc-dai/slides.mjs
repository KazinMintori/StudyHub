export const slides = [
  {
    "title": "MSE kết hợp độ chệch và phương sai",
    "bullets": [
      "Độ chệch là kỳ vọng của ước lượng trừ tham số cần ước lượng.",
      "Ước lượng không chệch vẫn có thể có phương sai lớn.",
      "MSE tiến về không là điều kiện đủ cho nhất quán."
    ],
    "formula": "$$\n\\mathrm{MSE}=\\mathrm{Var}+\\mathrm{Bias}^2\n$$",
    "example": "Với $n=9$ và $\\mu=2$, MSE của $\\bar X$ là $1/9$, còn MSE của $0{,}9\\bar X$ là $0{,}13$.",
    "note": "37-uoc-luong-diem-momen-va-hop-ly-cuc-dai"
  },
  {
    "title": "Phương pháp momen dùng mẫu số n",
    "bullets": [
      "Cân bằng các momen lý thuyết với momen mẫu tương ứng.",
      "Momen trung tâm mẫu bậc hai chia cho $n$, khác phương sai hiệu chỉnh chia cho $n-1$.",
      "Nghiệm còn phải thuộc miền tham số và cần đủ momen hữu hạn."
    ],
    "formula": "$$\nm_2=\\frac{1}{n}\\sum_{i=1}^n(X_i-\\bar X)^2\n$$",
    "example": "Gamma với $\\bar x=6$, $m_2=12$ cho tham số hình dạng $3$ và tốc độ $0{,}5$.",
    "note": "37-uoc-luong-diem-momen-va-hop-ly-cuc-dai"
  },
  {
    "title": "MLE cực đại hóa hàm hợp lý trên miền tham số",
    "bullets": [
      "Cố định dữ liệu và xét hàm hợp lý theo tham số.",
      "Với dữ liệu liên tục, dùng mật độ, không dùng xác suất tại đúng một điểm.",
      "Logarit bảo toàn điểm cực đại khi hàm hợp lý dương."
    ],
    "formula": "$$\n\\hat\\theta\\in\\arg\\max_{\\theta\\in\\Theta}L(\\theta)\n$$",
    "example": "Với mẫu mũ có tổng bằng $4$ và cỡ mẫu $4$, ước lượng tốc độ bằng $1\\,\\mathrm{s}^{-1}$.",
    "note": "37-uoc-luong-diem-momen-va-hop-ly-cuc-dai"
  },
  {
    "title": "Kiểm tra điểm biên trước khi dùng đạo hàm",
    "bullets": [
      "Với phân phối đều trên $[0,\\theta]$, miền giá trị phụ thuộc tham số.",
      "Hàm hợp lý giảm theo $\\theta$ trên miền khả thi, nên cực đại đạt tại quan sát lớn nhất.",
      "MLE có thể chệch. Hiệu quả tiệm cận còn cần điều kiện chính quy."
    ],
    "formula": "$$\n\\hat\\theta_{\\mathrm{MLE}}=X_{(n)}\n$$",
    "example": "Mẫu có cực đại $8{,}9$ cho MLE $8{,}9$, trong khi momen cho $12{,}65$.",
    "note": "37-uoc-luong-diem-momen-va-hop-ly-cuc-dai"
  }
]
