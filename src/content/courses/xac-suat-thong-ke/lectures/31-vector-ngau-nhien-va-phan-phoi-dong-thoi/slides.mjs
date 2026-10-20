export const slides = [
  {
    "note": "31-vector-ngau-nhien-va-phan-phoi-dong-thoi",
    "title": "Lấy tổng hoặc tích phân để tìm phân phối lề",
    "bullets": [
      "Phân phối đồng thời mô tả các giá trị mà hai biến cùng nhận.",
      "Trong bảng rời rạc, cộng các ô theo biến còn lại để tìm phân phối lề.",
      "Nếu cặp biến có mật độ đồng thời $f$, lấy tích phân theo biến còn lại."
    ],
    "formula": "$$\nf_X(x)=\\int_{\\mathbb R}f(x,y)\\,dy\n$$",
    "example": "Trong bảng sự cố, cộng hàng $X=0$ được $0{,}4+0{,}2+0{,}1=0{,}7$."
  },
  {
    "note": "31-vector-ngau-nhien-va-phan-phoi-dong-thoi",
    "title": "Chuẩn hóa lát cắt để tìm mật độ có điều kiện",
    "bullets": [
      "Với $0<f_X(x)<\\infty$, chia mật độ đồng thời cho mật độ lề của giá trị đang quan sát.",
      "Công thức được hiểu như một phiên bản mật độ có điều kiện với hầu hết các giá trị $x$ theo phân phối của $X$.",
      "Điều kiện hóa có thể làm thay đổi cả hình dạng mật độ lẫn miền giá trị của biến còn lại."
    ],
    "formula": "$$\nf_{Y\\mid X}(y\\mid x)=\\frac{f(x,y)}{f_X(x)}\n$$",
    "example": "Với mật độ $6(x+2y)/5$ trên tam giác $0\\le x\\le y\\le1$, ta có $\\mathbb E[X\\mid Y=y]=8y/15$ khi $0<y\\le1$."
  },
  {
    "note": "31-vector-ngau-nhien-va-phan-phoi-dong-thoi",
    "title": "Đổi thứ tự tích phân trên miền tam giác",
    "bullets": [
      "Miền không phải hình chữ nhật thường làm cận trong phụ thuộc biến ngoài.",
      "Tonelli cho phép đổi thứ tự tích phân của hàm không âm. Fubini áp dụng cho hàm khả tích tuyệt đối.",
      "Đổi lát cắt có thể đưa một tích phân khó về dạng có phép đổi biến đơn giản."
    ],
    "formula": "$$\nI=\\int_0^1x e^{x^2}\\,dx=\\frac{e-1}2\n$$",
    "example": "Với miền $0\\le y\\le x\\le1$, tích phân $e^{x^2}$ theo $y$ trước làm xuất hiện thừa số $x$."
  },
  {
    "note": "31-vector-ngau-nhien-va-phan-phoi-dong-thoi",
    "title": "Độc lập đòi hỏi phân tích mật độ trên toàn miền",
    "bullets": [
      "Với cặp có mật độ, độc lập tương đương với đẳng thức mật độ tích hầu khắp nơi trên toàn mặt phẳng.",
      "Phải kiểm tra cả phần mật độ bằng 0 ngoài miền đã cho. Tách biểu thức đại số riêng bên trong miền chưa đủ.",
      "Tích Descartes của hai tập giá trị có thể gồm nhiều miền rời nhau, không nhất thiết là một hình chữ nhật liền khối."
    ],
    "formula": "$$\nf_{X,Y}(x,y)=f_X(x)f_Y(y)\n$$",
    "example": "Mật độ $4xy$ trên hình vuông đơn vị cho hai biến độc lập, còn mật độ đều trên tam giác $x+y\\le1$ với $x,y\\ge0$ thì không."
  }
]
