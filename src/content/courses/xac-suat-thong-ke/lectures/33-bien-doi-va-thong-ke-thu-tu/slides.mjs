export const slides = [
  {
    "note": "33-bien-doi-va-thong-ke-thu-tu",
    "title": "Tìm CDF trước khi lấy đạo hàm",
    "bullets": [
      "Với $Y=g(X)$, trước hết đưa biến cố $Y\\le y$ về miền giá trị của $X$.",
      "Với $y>0$, công thức dưới đây áp dụng cho bình phương biến Chuẩn chuẩn tắc. Với $y\\le0$, CDF bằng 0.",
      "Khi $g$ không một đối một, cần xét đầy đủ các nhánh của miền nghịch ảnh."
    ],
    "formula": "$$\nF_{X^2}(y)=2\\Phi(\\sqrt y)-1\n$$",
    "example": "Nếu $X$ Chuẩn chuẩn tắc thì $X^2$ có phân phối Chi bình phương một bậc tự do."
  },
  {
    "note": "33-bien-doi-va-thong-ke-thu-tu",
    "title": "Jacobian đo hệ số đổi diện tích",
    "bullets": [
      "Phép đổi biến phải là song ánh khả vi liên tục, có định thức Jacobi khác 0 và nghịch đảo khả vi.",
      "Ma trận $J$ là Jacobi của phép biến đổi ngược. Mật độ mới bằng mật độ cũ tại nghịch ảnh nhân với $|\\det J|$.",
      "Cần đổi cả miền giá trị và đặt mật độ bằng 0 ngoài miền mới."
    ],
    "formula": "$$\nf_{\\rm mới}=f_{\\rm cũ}\\,|\\det J|\n$$",
    "example": "Từ hai biến $\\mathrm{Exp}(1)$ độc lập, tổng $U=X+Y$ và tỷ lệ $V=X/(X+Y)$ có $|\\det J|=u$, và $U,V$ độc lập."
  },
  {
    "note": "33-bien-doi-va-thong-ke-thu-tu",
    "title": "Tổng hai biến có mật độ được tính bằng tích chập",
    "bullets": [
      "Giả sử $X,Y$ độc lập và có mật độ.",
      "Mỗi giá trị $x$ của biến thứ nhất được ghép với giá trị $z-x$ của biến thứ hai.",
      "Tích phân cộng các đóng góp trên toàn bộ $x$. Miền giá trị của từng biến quyết định phần tích phân khác 0."
    ],
    "formula": "$$\nf_Z=f_X*f_Y\n$$",
    "example": "Tổng hai biến $U(0,1)$ độc lập có mật độ tam giác trên $[0,2]$."
  },
  {
    "note": "33-bien-doi-va-thong-ke-thu-tu",
    "title": "Thống kê thứ tự mô tả cực trị và trung vị",
    "bullets": [
      "Mẫu gồm $n$ biến độc lập cùng phân phối, có mật độ $f$ và CDF $F$.",
      "Cực đại không vượt $x$ khi mọi quan sát đều không vượt $x$.",
      "Cực tiểu vượt $x$ khi mọi quan sát đều vượt $x$. Các công thức được lấy đạo hàm để tìm mật độ."
    ],
    "formula": "$$\nP(X_{(n)}\\le x)=[F(x)]^n\n$$",
    "example": "Trung vị của ba biến $U(0,1)$ độc lập có phân phối $\\mathrm{Beta}(2,2)$ và kỳ vọng $0{,}5$."
  }
]
