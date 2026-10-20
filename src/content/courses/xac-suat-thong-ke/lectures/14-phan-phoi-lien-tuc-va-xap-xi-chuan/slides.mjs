export const slides = [
  {
    "note": "14-phan-phoi-lien-tuc-va-xap-xi-chuan",
    "title": "Biến ngẫu nhiên liên tục và hàm mật độ PDF",
    "bullets": [
      "Xác suất tại một điểm chính xác đơn lẻ của biến liên tục luôn bằng 0.",
      "Xác suất trên một khoảng bằng diện tích dưới đường cong hàm mật độ f(x).",
      "Tích phân toàn phần của hàm mật độ trên toàn trục số luôn bằng 1."
    ],
    "formula": "$$\n\\begin{aligned}P(a\\le X\\le b)&=\\int_a^bf(x)\\,dx,\\\\\\int_{-\\infty}^{\\infty}f(x)\\,dx&=1.\\end{aligned}\n$$",
    "example": "Phân phối đều trên đoạn [0, 1] có hàm mật độ f(x) = 1 và diện tích toàn phần bằng 1."
  },
  {
    "note": "14-phan-phoi-lien-tuc-va-xap-xi-chuan",
    "title": "Phân phối chuẩn và quy tắc 68-95-99,7",
    "bullets": [
      "Phân phối chuẩn có dạng hình chuông đối xứng đặc trưng quanh kỳ vọng mu.",
      "Phép chuẩn hóa z-score chuyển biến chuẩn về phân phối chuẩn chuẩn hóa N(0, 1).",
      "Khoảng 1 SD chứa xấp xỉ 68%, 2 SD chứa 95% và 3 SD chứa 99,7% diện tích."
    ],
    "formula": "$$\nZ = \\frac{X - \\mu}{\\sigma} \\sim \\mathcal{N}(0, 1)\n$$",
    "example": "Điểm số chuẩn hóa Z = 1,96 tương ứng với phân vị 97,5% của phân phối chuẩn chuẩn hóa."
  },
  {
    "note": "14-phan-phoi-lien-tuc-va-xap-xi-chuan",
    "title": "Định lý giới hạn trung tâm và hiệu chỉnh liên tục",
    "bullets": [
      "Tổng hoặc trung bình của n biến độc lập cùng phân phối tiến về chuẩn khi n lớn.",
      "Cần hiệu chỉnh liên tục khi dùng phân phối liên tục để xấp xỉ biến rời rạc dạng lưới.",
      "Cỡ mẫu hữu hạn là phép xấp xỉ, không biến biến rời rạc thành biến liên tục hoàn hảo."
    ],
    "formula": "$$\n\\begin{aligned}P(S_{30}\\ge6)&\\approx1-\\Phi(5/\\sqrt{30})\\\\&\\approx0{,}180655.\\end{aligned}\n$$",
    "example": "Bước đi ngẫu nhiên n = 30: Xác suất thực tế là 0,1808, xấp xỉ chuẩn có hiệu chỉnh liên tục là 0,1807."
  }
]
