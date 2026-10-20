export const slides = [
  {
    "note": "29-phan-phoi-roi-rac-mo-rong",
    "title": "Hai quy ước của phân phối Geometric",
    "bullets": [
      "Các phép thử Bernoulli độc lập và cùng có xác suất thành công $p\\in(0,1)$.",
      "Biến $X$ đếm số lần thử đến thành công đầu tiên, còn $Y=X-1$ đếm số thất bại.",
      "Kỳ vọng tương ứng là $1/p$ và $(1-p)/p$. Cả hai có phương sai $(1-p)/p^2$."
    ],
    "formula": "$$\nP(X=k)=(1-p)^{k-1}p\n$$",
    "example": "Khi $p=0{,}2$, trung bình cần $5$ lần thử. Sau ba lần thất bại, xác suất hai lần tiếp theo vẫn thất bại là $0{,}8^2=0{,}64$."
  },
  {
    "note": "29-phan-phoi-roi-rac-mo-rong",
    "title": "Phân phối Nhị thức âm đếm thất bại",
    "bullets": [
      "Dừng chuỗi Bernoulli độc lập cùng tham số $p$ khi có thành công thứ $r$, với $r$ nguyên dương.",
      "Biến $Y$ đếm thất bại trước thời điểm dừng và nhận các giá trị nguyên không âm.",
      "Biến $Y$ bằng tổng $r$ biến Geometric độc lập theo quy ước đếm thất bại."
    ],
    "formula": "$$\n\\mathbb E[Y]=\\frac{r(1-p)}p\n$$",
    "example": "Với xác suất lỗi $p=0{,}05$, số sản phẩm đạt chuẩn trước lỗi thứ ba có kỳ vọng $57$ và phương sai $1140$."
  },
  {
    "note": "29-phan-phoi-roi-rac-mo-rong",
    "title": "Phân phối Đa thức có các nhóm rời nhau",
    "bullets": [
      "Mỗi phép thử độc lập rơi vào đúng một nhóm trong một hệ phân loại rời nhau và vét cạn.",
      "Vector xác suất nhóm không đổi giữa các phép thử. Mỗi số đếm lề $X_i$ có phân phối $\\mathrm{Bin}(n,p_i)$.",
      "Hiệp phương sai giữa hai nhóm phân biệt không dương. Nó âm nghiêm ngặt khi $n>0$ và cả hai xác suất nhóm đều dương."
    ],
    "formula": "$$\n\\mathrm{Cov}(X_i,X_j)=-np_ip_j\n$$",
    "example": "Với $n=10$, $p_1=0{,}5$ và $p_2=0{,}3$, hiệp phương sai hai số đếm bằng $-1{,}5$."
  },
  {
    "note": "29-phan-phoi-roi-rac-mo-rong",
    "title": "Thu thập đủ ba loại phiếu thưởng",
    "bullets": [
      "Mỗi lần nhận một phiếu độc lập và đều giữa ba loại.",
      "Tách tổng thời gian thành ba khoảng chờ loại mới, có xác suất thành công lần lượt là $1$, $2/3$ và $1/3$.",
      "Các khoảng chờ độc lập nên phương sai tổng cũng bằng tổng phương sai."
    ],
    "formula": "$$\n\\mathbb E[T]=1+\\frac32+3=5{,}5\n$$",
    "example": "Phương sai tổng số lần mở bằng $0+3/4+6=6{,}75$."
  }
]
