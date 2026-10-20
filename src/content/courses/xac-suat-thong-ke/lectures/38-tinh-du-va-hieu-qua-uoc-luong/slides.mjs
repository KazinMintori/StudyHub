export const slides = [
  {
    "title": "Tính đủ được xác định cho tham số đang xét",
    "bullets": [
      "Thống kê đủ làm phân phối có điều kiện của mẫu không còn phụ thuộc tham số.",
      "Phân tích nhân tử tách phần dữ liệu chứa tham số khỏi phần còn lại.",
      "Trong mẫu chuẩn, thống kê đủ phụ thuộc việc kỳ vọng hay phương sai đã biết."
    ],
    "formula": "$$\nf(x;\\theta)=g(T(x),\\theta)h(x)\n$$",
    "example": "Khi cả kỳ vọng và phương sai chuẩn chưa biết, cần cặp $(\\bar X,S^2)$.",
    "note": "38-tinh-du-va-hieu-qua-uoc-luong"
  },
  {
    "title": "Rao–Blackwell loại bỏ dao động không cần thiết",
    "bullets": [
      "Bắt đầu từ ước lượng không chệch $W$ có phương sai hữu hạn.",
      "Lấy kỳ vọng có điều kiện theo thống kê đủ $T$.",
      "Ước lượng mới giữ kỳ vọng và không tăng phương sai."
    ],
    "formula": "$$\nW^*=\\mathbb E[W\\mid T]\n$$",
    "example": "Với Bernoulli, điều kiện hóa $X_1$ theo tổng mẫu tạo $\\bar X$ và giảm phương sai $n$ lần.",
    "note": "38-tinh-du-va-hieu-qua-uoc-luong"
  },
  {
    "title": "Chặn Cramér–Rao cần điều kiện chính quy",
    "bullets": [
      "Miền giá trị không phụ thuộc tham số và phải được đổi đạo hàm với kỳ vọng.",
      "Thông tin Fisher phải hữu hạn, dương. Ước lượng có phương sai hữu hạn.",
      "Công thức một tham số dưới đây không áp dụng trực tiếp cho phân phối đều có cận chưa biết."
    ],
    "formula": "$$\n\\mathrm{Var}(\\hat\\theta)\\ge\\frac{1}{nI(\\theta)}\n$$",
    "example": "Với Poisson, $I(\\lambda)=1/\\lambda$ và $\\bar X$ đạt chặn $\\lambda/n$.",
    "note": "38-tinh-du-va-hieu-qua-uoc-luong"
  },
  {
    "title": "Đủ và đầy đủ giúp nhận diện UMVU",
    "bullets": [
      "Tính đầy đủ yêu cầu một kỳ vọng bằng không với mọi giá trị tham số chỉ có thể đến từ hàm bằng không hầu chắc chắn.",
      "Hàm không chệch, phương sai hữu hạn của thống kê đủ và đầy đủ là UMVU.",
      "Tính duy nhất được hiểu đến sai khác trên tập xác suất không."
    ],
    "formula": "$$\n\\mathbb E_\\theta[g(T)]=0\\quad\\forall\\theta\n$$",
    "example": "Tổng Bernoulli đủ và đầy đủ với $0<p<1$, nên $\\bar X$ là UMVU của $p$.",
    "note": "38-tinh-du-va-hieu-qua-uoc-luong"
  }
]
