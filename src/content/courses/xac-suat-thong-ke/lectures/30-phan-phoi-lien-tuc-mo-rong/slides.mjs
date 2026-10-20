export const slides = [
  {
    "note": "30-phan-phoi-lien-tuc-mo-rong",
    "title": "Exponential có tính chất không nhớ",
    "bullets": [
      "Khoảng chờ giữa các sự kiện của quá trình Poisson đồng nhất có phân phối $\\mathrm{Exp}(\\lambda)$.",
      "Tham số $\\lambda>0$ là tốc độ. Kỳ vọng bằng $1/\\lambda$ và phương sai bằng $1/\\lambda^2$.",
      "Khi thiết bị còn hoạt động, thời gian chờ còn lại có cùng phân phối với lúc bắt đầu."
    ],
    "formula": "$$\nP(X>x)=e^{-\\lambda x},\\quad x\\ge0\n$$",
    "example": "Thời gian phục vụ trung bình $2$ phút cho xác suất cần thêm hơn $3$ phút sau khi đã đợi $2$ phút là khoảng $22{,}31\\%$."
  },
  {
    "note": "30-phan-phoi-lien-tuc-mo-rong",
    "title": "Gamma mở rộng tổng các khoảng chờ",
    "bullets": [
      "Họ Gamma có hình dạng $\\alpha>0$ và tốc độ $\\lambda>0$.",
      "Khi $\\alpha=k$ nguyên dương, đây là tổng $k$ khoảng chờ Exponential độc lập, còn gọi là Erlang.",
      "Các biến Gamma độc lập cùng tốc độ có tổng tham số hình dạng. Với hình dạng không nguyên, không diễn giải là số sự kiện."
    ],
    "formula": "$$\n\\mathbb E[X]=\\frac{\\alpha}{\\lambda}\n$$",
    "example": "Nhận đủ $4$ gói tin với tốc độ $2$ gói/giây có thời gian chờ $\\mathrm{Gamma}(4,2)$, kỳ vọng $2$ giây và phương sai $1$ giây bình phương."
  },
  {
    "note": "30-phan-phoi-lien-tuc-mo-rong",
    "title": "Beta mô hình hóa tỷ lệ liên tục",
    "bullets": [
      "Phân phối $\\mathrm{Beta}(\\alpha,\\beta)$ có hai tham số dương và mật độ trên khoảng $(0,1)$.",
      "Trong mô hình Bernoulli, Beta là tiên nghiệm liên hợp khi các phép thử độc lập có điều kiện theo xác suất thành công.",
      "Khi $\\alpha,\\beta>1$, mật độ đạt cực đại tại $(\\alpha-1)/(\\alpha+\\beta-2)$."
    ],
    "formula": "$$\n\\mathbb E[X]=\\frac{\\alpha}{\\alpha+\\beta}\n$$",
    "example": "Với $\\mathrm{Beta}(3,7)$, kỳ vọng là $30\\%$, còn mật độ đạt cực đại tại tỷ lệ $25\\%$."
  },
  {
    "note": "30-phan-phoi-lien-tuc-mo-rong",
    "title": "Weibull và Lognormal dùng hai cơ chế khác nhau",
    "bullets": [
      "Weibull có tốc độ hỏng tăng khi $k>1$, không đổi khi $k=1$ và giảm khi $0<k<1$.",
      "Trong công thức Weibull, $\\lambda$ là thang thời gian. Tốc độ hỏng là tốc độ có điều kiện, có đơn vị nghịch đảo thời gian.",
      "Nếu $\\ln Y$ có phân phối Chuẩn với $\\sigma>0$, thì $Y$ có phân phối Lognormal, kỳ vọng lớn hơn trung vị."
    ],
    "formula": "$$\n\\mathrm{Med}(Y)=e^\\mu\n$$",
    "example": "Mô hình thu nhập Lognormal với $\\mu=3$, $\\sigma=0{,}5$ cho trung vị khoảng $20{,}09$ triệu đồng và kỳ vọng $22{,}76$ triệu đồng."
  }
]
