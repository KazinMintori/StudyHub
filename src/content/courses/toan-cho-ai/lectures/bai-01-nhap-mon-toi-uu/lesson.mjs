export const lesson = {
  "number": 1,
  "slug": "bai-01-nhap-mon-toi-uu",
  "title": "Giới thiệu tối ưu, tập lồi và hàm lồi",
  "prerequisites": [
    "vector",
    "tich-vo-huong",
    "gradient",
    "hessian",
    "ma-tran-psd"
  ],
  "supportingConcepts": [
    "tham-so-toan-hoc",
    "ham-so",
    "tap-hop",
    "to-hop-loi",
    "tap-loi",
    "ham-loi",
    "chuan",
    "ma-tran",
    "he-phuong-trinh",
    "mien-kha-thi",
    "infimum",
    "epigraph",
    "binh-phuong-toi-thieu",
    "likelihood",
    "dinh-luat-snell"
  ],
  "status": "ready",
  "description": "Lập bài toán, dùng đoạn thẳng để xét tập lồi và dây cung để xét hàm lồi. Giải thích điều kiện tối ưu toàn cục.",
  "topicGroups": [
    {
      "title": "I. Bài toán tối ưu",
      "description": "Viết đúng một bài toán trước khi nghĩ tới chuyện giải nó.",
      "topics": [
        {
          "slug": "bai-toan-toi-uu",
          "title": "Bài toán tối ưu và những gì cần viết ra",
          "question": "Muốn nói một phương án là tốt nhất, ta phải mô tả chính xác những đối tượng nào?",
          "source": "§1.1, §4.1.1"
        },
        {
          "slug": "hai-lop-bai-toan-kinh-dien",
          "title": "Bình phương tối thiểu và quy hoạch tuyến tính",
          "question": "Hai lớp bài toán quen thuộc này có điểm chung gì mà người ta giải được chúng một cách đáng tin cậy?",
          "source": "§1.2–1.3"
        }
      ]
    },
    {
      "title": "II. Hình học của tập lồi",
      "description": "Các khối hình cơ bản, cách lắp ghép chúng và những định lý hình học dùng lại suốt môn học.",
      "topics": [
        {
          "slug": "duong-thang-va-tap-affine",
          "title": "Đường thẳng, đoạn thẳng và tập affine",
          "question": "Điều kiện “các hệ số cộng lại bằng 1” mô tả loại hình học nào?",
          "source": "§2.1.1–2.1.2"
        },
        {
          "slug": "noi-tuong-doi",
          "title": "Chiều affine và nội tương đối",
          "question": "Một hình vuông nằm phẳng trong không gian ba chiều có “phần trong” hay không?",
          "source": "§2.1.3"
        },
        {
          "slug": "tap-loi-va-bao-loi",
          "title": "Tập lồi, tổ hợp lồi và bao lồi",
          "question": "Khi buộc mọi hệ số phải không âm, đường thẳng qua hai điểm còn lại phần nào?",
          "source": "§2.1.4"
        },
        {
          "slug": "non-loi",
          "title": "Nón và nón lồi",
          "question": "Bỏ điều kiện tổng bằng 1 nhưng vẫn giữ hệ số không âm thì ta thu được hình gì?",
          "source": "§2.1.5"
        },
        {
          "slug": "sieu-phang-va-nua-khong-gian",
          "title": "Siêu phẳng và nửa không gian",
          "question": "Một phương trình tuyến tính duy nhất chia không gian ra sao?",
          "source": "§2.2.1"
        },
        {
          "slug": "qua-cau-va-ellipsoid",
          "title": "Quả cầu và ellipsoid",
          "question": "Một ma trận đối xứng xác định dương vẽ ra hình gì trong không gian?",
          "source": "§2.2.2"
        },
        {
          "slug": "chuan-va-non-chuan",
          "title": "Quả cầu chuẩn và nón chuẩn",
          "question": "Vì sao quả cầu đơn vị của mọi chuẩn đều lồi, còn “quả cầu” của ‖x‖ với p = 1/2 thì không?",
          "source": "§2.2.3"
        },
        {
          "slug": "da-dien-va-don-hinh",
          "title": "Đa diện và đơn hình",
          "question": "Nên mô tả một đa giác bằng các cạnh hay bằng các đỉnh của nó?",
          "source": "§2.2.4"
        },
        {
          "slug": "non-psd",
          "title": "Nón các ma trận nửa xác định dương",
          "question": "Tập hợp các ma trận cũng có một hình dạng mà ta có thể hình dung được không?",
          "source": "§2.2.5"
        },
        {
          "slug": "phep-toan-giu-tinh-loi",
          "title": "Các phép toán giữ tính lồi của tập",
          "question": "Làm thế nào chứng minh một tập phức tạp là lồi mà không phải kiểm tra từng đoạn thẳng?",
          "source": "§2.3.1–2.3.2"
        },
        {
          "slug": "phoi-canh-va-phan-tuyen-tinh",
          "title": "Phép phối cảnh và hàm phân tuyến tính",
          "question": "Nhìn một vật lồi qua máy ảnh lỗ kim, ảnh thu được có còn lồi?",
          "source": "§2.3.3"
        },
        {
          "slug": "bat-dang-thuc-tong-quat",
          "title": "Nón chính quy và bất đẳng thức tổng quát",
          "question": "Khi so sánh hai vector, “nhỏ hơn” nên được hiểu theo nghĩa nào?",
          "source": "§2.4"
        },
        {
          "slug": "sieu-phang-phan-tach-va-tua",
          "title": "Siêu phẳng phân tách và siêu phẳng tựa",
          "question": "Hai tập lồi rời nhau có luôn ngăn được bằng một siêu phẳng không?",
          "source": "§2.5"
        },
        {
          "slug": "non-doi-ngau",
          "title": "Nón đối ngẫu và lựa chọn Pareto",
          "question": "Những hướng nào nhìn toàn bộ một nón từ cùng một phía, và điều đó giúp gì khi phải cân nhiều tiêu chí?",
          "source": "§2.6"
        }
      ]
    },
    {
      "title": "III. Hàm lồi",
      "description": "Nối hình học của tập lồi với giải tích: Dây cung, tiếp tuyến, độ cong và các quy tắc lắp ghép hàm.",
      "topics": [
        {
          "slug": "ham-loi",
          "title": "Hàm lồi và bất đẳng thức dây cung",
          "question": "Đồ thị nằm dưới mọi dây cung thì nói lên điều gì về một hàm số?",
          "source": "§3.1.1–3.1.2"
        },
        {
          "slug": "dieu-kien-bac-nhat",
          "title": "Điều kiện bậc nhất: Tiếp tuyến nằm dưới đồ thị",
          "question": "Chỉ biết giá trị và đạo hàm tại một điểm, ta suy ra được gì về toàn bộ hàm?",
          "source": "§3.1.3"
        },
        {
          "slug": "dieu-kien-bac-hai",
          "title": "Điều kiện bậc hai và độ cong",
          "question": "Hessian nửa xác định dương mang ý nghĩa hình học gì?",
          "source": "§3.1.4"
        },
        {
          "slug": "cac-ham-loi-quen-thuoc",
          "title": "Những hàm lồi thường gặp",
          "question": "Chuẩn, hàm max, log-sum-exp và log det lồi hay lõm, và ta chứng minh điều đó thế nào?",
          "source": "§3.1.5"
        },
        {
          "slug": "epigraph-tap-muc-duoi-jensen",
          "title": "Epigraph, tập mức dưới và bất đẳng thức Jensen",
          "question": "Nhìn một hàm lồi như một tập hợp thì ta được thêm những công cụ gì?",
          "source": "§3.1.6–3.1.9"
        },
        {
          "slug": "phep-toan-giu-tinh-loi-cua-ham",
          "title": "Các phép toán giữ tính lồi của hàm",
          "question": "Từ vài hàm lồi đã biết, ta lắp ghép được những hàm lồi mới nào và cần cẩn thận ở đâu?",
          "source": "§3.2"
        }
      ]
    },
    {
      "title": "IV. Tính lồi trong bài toán tối ưu",
      "description": "Ghép miền lồi với hàm mục tiêu lồi để có những bảo đảm mà tối ưu tổng quát không có.",
      "topics": [
        {
          "slug": "cuc-bo-va-toan-cuc",
          "title": "Cực tiểu cục bộ và cực tiểu toàn cục",
          "question": "Trong bài toán lồi, một điểm tốt nhất trong vùng lân cận có chắc là tốt nhất trên toàn miền?",
          "source": "§4.2.1–4.2.2"
        },
        {
          "slug": "dieu-kien-toi-uu",
          "title": "Điều kiện tối ưu bậc nhất trên miền lồi",
          "question": "Khi nghiệm nằm trên biên và gradient khác 0, ta kiểm chứng nó tối ưu bằng cách nào?",
          "source": "§4.2.3"
        },
        {
          "slug": "tinh-loi-trong-mo-hinh-hoc-may",
          "title": "Nhận diện tính lồi trong mô hình học máy",
          "question": "Hàm mất mát của hồi quy logistic là lồi, vậy còn mạng nơ-ron hai tầng thì sao?",
          "source": "§4.4, §7.1"
        }
      ]
    }
  ]
}
