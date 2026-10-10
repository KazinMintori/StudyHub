// Bản dịch nguyên tác đang được đối chiếu. Không đánh dấu ready khi còn đơn vị nguồn chưa dịch.
export const physics1Course = {
  "id": "vat-ly-1",
  "code": "09",
  "name": "Vật lý đại cương 1",
  "short": "Vật lý 1",
  "current": true,
  "description": "Bản dịch tiếng Việt theo chương 1–20 của Young & Freedman, từ cơ học đến hết nhiệt học. Đang dịch và đối chiếu từng mục, hình, ví dụ và bài tập nguyên tác.",
  "foundations": [
    "don-vi",
    "vector",
    "tich-vo-huong",
    "dao-ham",
    "tich-phan",
    "luc",
    "cong-nang-luong",
    "dong-luong-vat-ly",
    "momen-luc",
    "momen-quan-tinh",
    "dao-dong-dieu-hoa",
    "song",
    "nhiet-do-tuyet-doi",
    "khi-ly-tuong",
    "noi-nang",
    "entropy-nhiet-dong"
  ],
  "parts": [
    {
      "title": "Phần 1. Đo lường và động học",
      "description": "Mô hình vật lý, vector và mô tả chuyển động.",
      "lessons": [
        "01-don-vi-vector",
        "02-chuyen-dong-thang",
        "03-chuyen-dong-khong-gian"
      ]
    },
    {
      "title": "Phần 2. Lực, năng lượng và động lượng",
      "description": "Newton, công, thế năng và va chạm.",
      "lessons": [
        "04-dinh-luat-newton",
        "05-ung-dung-newton",
        "06-cong-dong-nang",
        "07-the-nang-bao-toan-co-nang",
        "08-dong-luong-va-cham"
      ]
    },
    {
      "title": "Phần 3. Vật rắn, chất lưu và hấp dẫn",
      "description": "Quay, cân bằng, biến dạng, chất lưu và quỹ đạo.",
      "lessons": [
        "09-dong-hoc-vat-ran",
        "10-dong-luc-hoc-quay",
        "11-can-bang-dan-hoi",
        "12-co-hoc-chat-luu",
        "13-hap-dan"
      ]
    },
    {
      "title": "Phần 4. Dao động và sóng cơ",
      "description": "Dao động điều hòa, sóng dừng và âm học.",
      "lessons": [
        "14-dao-dong",
        "15-song-co",
        "16-am-hoc"
      ]
    },
    {
      "title": "Phần 5. Nhiệt học và nhiệt động lực học",
      "description": "Nhiệt lượng, khí lý tưởng, hai nguyên lý và entropy.",
      "lessons": [
        "17-nhiet-do-nhiet-luong",
        "18-thuyet-dong-hoc-chat-khi",
        "19-nguyen-ly-thu-nhat",
        "20-nguyen-ly-thu-hai-entropy"
      ]
    }
  ],
  "lessons": [
    {
      "slug": "01-don-vi-vector",
      "title": "Đơn vị, đại lượng vật lý và vector",
      "prerequisites": [],
      "supportingConcepts": [
        "don-vi",
        "vector",
        "tich-vo-huong"
      ],
      "status": "draft",
      "number": 1,
      "sourceChapter": 1
    },
    {
      "slug": "02-chuyen-dong-thang",
      "title": "Chuyển động trên đường thẳng",
      "prerequisites": [
        "do-doi",
        "thanh-phan-vector"
      ],
      "supportingConcepts": [
        "van-toc-vat-ly",
        "toc-do-chuyen-dong",
        "gia-toc",
        "roi-tu-do",
        "dao-ham",
        "tich-phan"
      ],
      "status": "ready",
      "number": 2,
      "sourceChapter": 2
    },
    {
      "slug": "03-chuyen-dong-khong-gian",
      "title": "Chuyển động trong hai hoặc ba chiều",
      "prerequisites": [
        "vector",
        "dao-ham",
        "don-vi"
      ],
      "supportingConcepts": [
        "luc"
      ],
      "status": "draft",
      "number": 3,
      "sourceChapter": 3
    },
    {
      "slug": "04-dinh-luat-newton",
      "title": "Các định luật chuyển động của Newton",
      "prerequisites": [
        "vector",
        "dao-ham",
        "don-vi"
      ],
      "supportingConcepts": [
        "luc"
      ],
      "status": "draft",
      "number": 4,
      "sourceChapter": 4
    },
    {
      "slug": "05-ung-dung-newton",
      "title": "Áp dụng các định luật Newton",
      "prerequisites": [
        "vector",
        "luc",
        "don-vi"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 5,
      "sourceChapter": 5
    },
    {
      "slug": "06-cong-dong-nang",
      "title": "Công và động năng",
      "prerequisites": [
        "tich-vo-huong",
        "tich-phan",
        "luc"
      ],
      "supportingConcepts": [
        "cong-nang-luong"
      ],
      "status": "draft",
      "number": 6,
      "sourceChapter": 6
    },
    {
      "slug": "07-the-nang-bao-toan-co-nang",
      "title": "Thế năng và bảo toàn năng lượng",
      "prerequisites": [
        "cong-nang-luong",
        "dao-ham"
      ],
      "supportingConcepts": [
        "luc"
      ],
      "status": "draft",
      "number": 7,
      "sourceChapter": 7
    },
    {
      "slug": "08-dong-luong-va-cham",
      "title": "Động lượng, xung lượng và va chạm",
      "prerequisites": [
        "vector",
        "tich-phan",
        "cong-nang-luong"
      ],
      "supportingConcepts": [
        "dong-luong-vat-ly"
      ],
      "status": "draft",
      "number": 8,
      "sourceChapter": 8
    },
    {
      "slug": "09-dong-hoc-vat-ran",
      "title": "Chuyển động quay của vật rắn",
      "prerequisites": [
        "dao-ham",
        "tich-phan",
        "cong-nang-luong"
      ],
      "supportingConcepts": [
        "momen-quan-tinh"
      ],
      "status": "draft",
      "number": 9,
      "sourceChapter": 9
    },
    {
      "slug": "10-dong-luc-hoc-quay",
      "title": "Động lực học chuyển động quay",
      "prerequisites": [
        "vector",
        "tich-vo-huong",
        "momen-quan-tinh",
        "cong-nang-luong"
      ],
      "supportingConcepts": [
        "momen-luc",
        "dong-luong-vat-ly"
      ],
      "status": "draft",
      "number": 10,
      "sourceChapter": 10
    },
    {
      "slug": "11-can-bang-dan-hoi",
      "title": "Cân bằng và đàn hồi",
      "prerequisites": [
        "luc",
        "momen-luc",
        "don-vi"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 11,
      "sourceChapter": 11
    },
    {
      "slug": "12-co-hoc-chat-luu",
      "title": "Cơ học chất lưu",
      "prerequisites": [
        "luc",
        "cong-nang-luong",
        "don-vi"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 12,
      "sourceChapter": 12
    },
    {
      "slug": "13-hap-dan",
      "title": "Hấp dẫn",
      "prerequisites": [
        "luc",
        "cong-nang-luong",
        "vector"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 13,
      "sourceChapter": 13
    },
    {
      "slug": "14-dao-dong",
      "title": "Chuyển động tuần hoàn",
      "prerequisites": [
        "dao-ham",
        "cong-nang-luong",
        "momen-quan-tinh"
      ],
      "supportingConcepts": [
        "dao-dong-dieu-hoa",
        "pha-song"
      ],
      "status": "draft",
      "number": 14,
      "sourceChapter": 14
    },
    {
      "slug": "15-song-co",
      "title": "Sóng cơ",
      "prerequisites": [
        "dao-dong-dieu-hoa",
        "dao-ham",
        "don-vi"
      ],
      "supportingConcepts": [
        "song",
        "pha-song",
        "giao-thoa-song"
      ],
      "status": "draft",
      "number": 15,
      "sourceChapter": 15
    },
    {
      "slug": "16-am-hoc",
      "title": "Âm thanh và sự nghe",
      "prerequisites": [
        "song",
        "pha-song",
        "dao-dong-dieu-hoa"
      ],
      "supportingConcepts": [
        "giao-thoa-song"
      ],
      "status": "draft",
      "number": 16,
      "sourceChapter": 16
    },
    {
      "slug": "17-nhiet-do-nhiet-luong",
      "title": "Nhiệt độ và nhiệt",
      "prerequisites": [
        "cong-nang-luong",
        "don-vi"
      ],
      "supportingConcepts": [
        "nhiet-do-tuyet-doi",
        "noi-nang"
      ],
      "status": "draft",
      "number": 17,
      "sourceChapter": 17
    },
    {
      "slug": "18-thuyet-dong-hoc-chat-khi",
      "title": "Tính chất nhiệt của vật chất",
      "prerequisites": [
        "nhiet-do-tuyet-doi",
        "cong-nang-luong",
        "ky-vong"
      ],
      "supportingConcepts": [
        "khi-ly-tuong",
        "noi-nang"
      ],
      "status": "draft",
      "number": 18,
      "sourceChapter": 18
    },
    {
      "slug": "19-nguyen-ly-thu-nhat",
      "title": "Nguyên lý thứ nhất của nhiệt động lực học",
      "prerequisites": [
        "khi-ly-tuong",
        "tich-phan",
        "nhiet-do-tuyet-doi"
      ],
      "supportingConcepts": [
        "noi-nang"
      ],
      "status": "draft",
      "number": 19,
      "sourceChapter": 19
    },
    {
      "slug": "20-nguyen-ly-thu-hai-entropy",
      "title": "Nguyên lý thứ hai của nhiệt động lực học",
      "prerequisites": [
        "noi-nang",
        "khi-ly-tuong",
        "nhiet-do-tuyet-doi",
        "tich-phan"
      ],
      "supportingConcepts": [
        "entropy-nhiet-dong"
      ],
      "status": "draft",
      "number": 20,
      "sourceChapter": 20
    }
  ],
  "slides": [
    {
      "note": "02-chuyen-dong-thang",
      "title": "Độ dời và vận tốc trung bình",
      "bullets": [
        "Chọn trục và chiều dương trước khi lấy tọa độ cuối trừ tọa độ đầu.",
        "Vận tốc trung bình phụ thuộc hai đầu khoảng thời gian, không mô tả mọi biến đổi ở bên trong.",
        "Trên đồ thị vị trí theo thời gian, vận tốc trung bình là độ dốc dây cung."
      ],
      "formula": "$$\\Delta x=x_2-x_1,\\qquad v_{\\mathrm{av}-x}=\\frac{x_2-x_1}{t_2-t_1},\\quad t_2>t_1$$",
      "example": "Hình 2.1: Từ 19 m lúc 1,0 s đến 277 m lúc 4,0 s cho độ dời 258 m và vận tốc trung bình 86 m/s."
    },
    {
      "note": "02-chuyen-dong-thang",
      "title": "Vận tốc tức thời và tốc độ là hai đại lượng khác nhau",
      "bullets": [
        "Vận tốc tức thời là giới hạn của vận tốc trung bình và bằng độ dốc tiếp tuyến đồ thị vị trí.",
        "Tốc độ tức thời là độ lớn vận tốc; tốc độ trung bình dùng quãng đường thay cho độ dời.",
        "Đi rồi trở về điểm đầu có thể có vận tốc trung bình bằng không dù tốc độ trung bình dương."
      ],
      "formula": "$$v_x=\\frac{dx}{dt},\\qquad v=|v_x|$$",
      "example": "Ví dụ 2.1: Báo có vận tốc trung bình 15 m/s từ 1,0 s đến 2,0 s; vận tốc tức thời tại 1,0 s là 10 m/s."
    },
    {
      "note": "02-chuyen-dong-thang",
      "title": "Dấu của gia tốc cần được xét cùng dấu vận tốc",
      "bullets": [
        "Gia tốc trung bình bằng độ biến thiên vận tốc chia khoảng thời gian.",
        "Gia tốc tức thời là độ dốc tiếp tuyến của đồ thị vận tốc theo thời gian.",
        "Trong chuyển động thẳng, cùng dấu vận tốc và gia tốc thì nhanh dần; trái dấu thì chậm dần."
      ],
      "formula": "$$a_{\\mathrm{av}-x}=\\frac{v_{2x}-v_{1x}}{t_2-t_1},\\qquad a_x=\\frac{dv_x}{dt}=\\frac{d^2x}{dt^2}$$",
      "example": "Ví dụ 2.2(c): Vận tốc giảm từ −0,4 đến −1,0 m/s trong 2,0 s; gia tốc trung bình âm nhưng tốc độ tăng."
    },
    {
      "note": "02-chuyen-dong-thang",
      "title": "Bốn phương trình dùng khi gia tốc không đổi",
      "bullets": [
        "Vị trí đầu và vận tốc đầu phải được xác định ở cùng mốc t = 0.",
        "Chọn phương trình theo đại lượng đã biết và đại lượng cần tìm; giải bằng ký hiệu trước khi thay số.",
        "Vận tốc trung bình bằng nửa tổng vận tốc đầu và cuối trong trường hợp gia tốc không đổi."
      ],
      "formula": "$$\\begin{aligned}v_x&=v_{0x}+a_xt\\\\x&=x_0+v_{0x}t+\\tfrac12a_xt^2\\\\v_x^2&=v_{0x}^2+2a_x(x-x_0)\\\\x-x_0&=\\tfrac12(v_{0x}+v_x)t\\end{aligned}$$",
      "example": "Ví dụ 2.4: Với x₀ = 5,0 m, v₀ₓ = 15 m/s, aₓ = 4,0 m/s² cho x = 43 m và vₓ = 23 m/s tại t = 2,0 s."
    },
    {
      "note": "02-chuyen-dong-thang",
      "title": "Rơi tự do gồm cả lúc đi lên và lúc đi xuống",
      "bullets": [
        "Bỏ lực cản không khí và xét gần mặt đất để coi gia tốc trọng trường không đổi.",
        "Độ lớn g dương; chọn trục thẳng đứng hướng lên thì thành phần gia tốc âm.",
        "Ở điểm cao nhất, vận tốc bằng không nhưng gia tốc vẫn hướng xuống."
      ],
      "formula": "$$a_y=-g,\\qquad y=y_0+v_{0y}t-\\tfrac12gt^2,\\qquad v_y=v_{0y}-gt$$",
      "example": "Ví dụ 2.7: Bóng rời tay với 15,0 m/s hướng lên đạt độ cao cực đại khoảng 11,5 m so với tay."
    },
    {
      "note": "02-chuyen-dong-thang",
      "title": "Tích phân nối gia tốc, vận tốc và vị trí",
      "bullets": [
        "Nếu biết gia tốc theo thời gian, tích phân một lần và dùng vận tốc đầu để tìm vận tốc.",
        "Tích phân vận tốc và dùng vị trí đầu để tìm vị trí.",
        "Diện tích có dấu dưới đồ thị gia tốc cho biến thiên vận tốc; dưới đồ thị vận tốc cho độ dời."
      ],
      "formula": "$$v_x=v_{0x}+\\int_0^t a_x\\,dt,\\qquad x=x_0+\\int_0^t v_x\\,dt$$",
      "example": "Ví dụ 2.9: Hàm gia tốc aₓ = 2,0 m/s² − (0,10 m/s³)t cho vận tốc lớn nhất 30 m/s tại t = 20 s, khi x ≈ 517 m."
    }
  ],
  "contentPolicy": "full-source-translation"
}

export const physics2Course = {
  "id": "vat-ly-2",
  "code": "05",
  "name": "Vật lý đại cương 2",
  "short": "Vật lý 2",
  "current": true,
  "description": "Bản dịch tiếng Việt theo chương 21–44 của Young & Freedman, từ điện học đến hết vật lý hiện đại. Đang dịch và đối chiếu từng mục, hình, ví dụ và bài tập nguyên tác.",
  "foundations": [
    "vector",
    "tich-vo-huong",
    "dao-ham",
    "gradient",
    "tich-phan",
    "don-vi",
    "cong-nang-luong",
    "dien-tich",
    "dien-truong",
    "dien-the",
    "thong-luong",
    "dien-dung",
    "dong-dien",
    "dien-tro",
    "tu-truong",
    "cam-ung-dien-tu",
    "tu-cam",
    "song",
    "pha-song",
    "chiet-suat",
    "photon",
    "ham-song-luong-tu"
  ],
  "parts": [
    {
      "title": "Phần 1. Tĩnh điện và tụ điện",
      "description": "Coulomb, Gauss, điện thế và điện môi.",
      "lessons": [
        "01-dien-truong-coulomb",
        "03-dinh-luat-gauss",
        "02-dien-the",
        "04-tu-dien-dien-moi"
      ]
    },
    {
      "title": "Phần 2. Dòng điện và mạch một chiều",
      "description": "Hạt tải, nguồn điện, Kirchhoff và quá trình RC.",
      "lessons": [
        "05-dong-dien-dien-tro",
        "06-mach-dien-mot-chieu"
      ]
    },
    {
      "title": "Phần 3. Từ trường và cảm ứng",
      "description": "Lực từ, nguồn từ, Faraday, tự cảm và mạch xoay chiều.",
      "lessons": [
        "07-tu-truong-luc-tu",
        "08-nguon-tu-truong",
        "09-cam-ung-dien-tu",
        "10-tu-cam",
        "11-dong-dien-xoay-chieu"
      ]
    },
    {
      "title": "Phần 4. Sóng điện từ và quang học",
      "description": "Sóng điện từ, khúc xạ, tạo ảnh, giao thoa và nhiễu xạ.",
      "lessons": [
        "12-song-dien-tu",
        "13-truyen-anh-sang",
        "14-quang-hinh-hoc",
        "15-giao-thoa",
        "16-nhieu-xa"
      ]
    },
    {
      "title": "Phần 5. Tương đối và lượng tử",
      "description": "Tương đối hẹp, photon, sóng vật chất, hàm sóng và nguyên tử.",
      "lessons": [
        "17-thuyet-tuong-doi",
        "18-photon",
        "19-song-vat-chat",
        "20-ham-song-schrodinger",
        "21-cau-truc-nguyen-tu"
      ]
    },
    {
      "title": "Phần 6. Vật chất, hạt nhân và vũ trụ",
      "description": "Vùng năng lượng, bán dẫn, phóng xạ và vật lý hạt.",
      "lessons": [
        "22-chat-ran-ban-dan",
        "23-vat-ly-hat-nhan",
        "24-hat-co-ban-vu-tru"
      ]
    }
  ],
  "lessons": [
    {
      "slug": "01-dien-truong-coulomb",
      "title": "Điện tích và điện trường",
      "prerequisites": [
        "vector",
        "chuan",
        "luc",
        "don-vi"
      ],
      "supportingConcepts": [
        "dien-tich",
        "dien-truong"
      ],
      "status": "draft",
      "number": 1,
      "sourceChapter": 21
    },
    {
      "slug": "03-dinh-luat-gauss",
      "title": "Định luật Gauss",
      "prerequisites": [
        "tich-vo-huong",
        "tich-phan",
        "dien-tich",
        "dien-truong"
      ],
      "supportingConcepts": [
        "thong-luong"
      ],
      "status": "draft",
      "number": 2,
      "sourceChapter": 22
    },
    {
      "slug": "02-dien-the",
      "title": "Điện thế",
      "prerequisites": [
        "dien-truong",
        "cong-nang-luong",
        "tich-phan",
        "gradient"
      ],
      "supportingConcepts": [
        "dien-the"
      ],
      "status": "draft",
      "number": 3,
      "sourceChapter": 23
    },
    {
      "slug": "04-tu-dien-dien-moi",
      "title": "Điện dung và điện môi",
      "prerequisites": [
        "dien-truong",
        "dien-the",
        "cong-nang-luong"
      ],
      "supportingConcepts": [
        "dien-dung"
      ],
      "status": "draft",
      "number": 4,
      "sourceChapter": 24
    },
    {
      "slug": "05-dong-dien-dien-tro",
      "title": "Dòng điện, điện trở và suất điện động",
      "prerequisites": [
        "dien-tich",
        "dien-the",
        "cong-nang-luong"
      ],
      "supportingConcepts": [
        "dong-dien",
        "dien-tro"
      ],
      "status": "draft",
      "number": 5,
      "sourceChapter": 25
    },
    {
      "slug": "06-mach-dien-mot-chieu",
      "title": "Mạch điện một chiều",
      "prerequisites": [
        "dong-dien",
        "dien-tro",
        "dien-dung",
        "dien-the"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 6,
      "sourceChapter": 26
    },
    {
      "slug": "07-tu-truong-luc-tu",
      "title": "Từ trường và lực từ",
      "prerequisites": [
        "vector",
        "dong-dien",
        "luc"
      ],
      "supportingConcepts": [
        "tu-truong",
        "momen-luc"
      ],
      "status": "draft",
      "number": 7,
      "sourceChapter": 27
    },
    {
      "slug": "08-nguon-tu-truong",
      "title": "Nguồn của từ trường",
      "prerequisites": [
        "vector",
        "tich-phan",
        "dong-dien",
        "tu-truong"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 8,
      "sourceChapter": 28
    },
    {
      "slug": "09-cam-ung-dien-tu",
      "title": "Cảm ứng điện từ",
      "prerequisites": [
        "thong-luong",
        "tu-truong",
        "dao-ham",
        "dong-dien"
      ],
      "supportingConcepts": [
        "cam-ung-dien-tu"
      ],
      "status": "draft",
      "number": 9,
      "sourceChapter": 29
    },
    {
      "slug": "10-tu-cam",
      "title": "Điện cảm",
      "prerequisites": [
        "cam-ung-dien-tu",
        "dien-dung",
        "dien-tro",
        "dao-ham"
      ],
      "supportingConcepts": [
        "tu-cam",
        "dao-dong-dieu-hoa"
      ],
      "status": "draft",
      "number": 10,
      "sourceChapter": 30
    },
    {
      "slug": "11-dong-dien-xoay-chieu",
      "title": "Dòng điện xoay chiều",
      "prerequisites": [
        "tu-cam",
        "dien-dung",
        "dien-tro",
        "pha-song"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 11,
      "sourceChapter": 31
    },
    {
      "slug": "12-song-dien-tu",
      "title": "Sóng điện từ",
      "prerequisites": [
        "dien-truong",
        "tu-truong",
        "song",
        "thong-luong"
      ],
      "supportingConcepts": [
        "pha-song"
      ],
      "status": "draft",
      "number": 12,
      "sourceChapter": 32
    },
    {
      "slug": "13-truyen-anh-sang",
      "title": "Bản chất và sự truyền ánh sáng",
      "prerequisites": [
        "song",
        "pha-song",
        "vector"
      ],
      "supportingConcepts": [
        "chiet-suat"
      ],
      "status": "draft",
      "number": 13,
      "sourceChapter": 33
    },
    {
      "slug": "14-quang-hinh-hoc",
      "title": "Quang hình học",
      "prerequisites": [
        "chiet-suat",
        "don-vi"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 14,
      "sourceChapter": 34
    },
    {
      "slug": "15-giao-thoa",
      "title": "Giao thoa",
      "prerequisites": [
        "song",
        "pha-song",
        "chiet-suat"
      ],
      "supportingConcepts": [
        "giao-thoa-song"
      ],
      "status": "draft",
      "number": 15,
      "sourceChapter": 35
    },
    {
      "slug": "16-nhieu-xa",
      "title": "Nhiễu xạ",
      "prerequisites": [
        "giao-thoa-song",
        "pha-song",
        "chiet-suat"
      ],
      "supportingConcepts": [
        "nhieu-xa-anh-sang"
      ],
      "status": "draft",
      "number": 16,
      "sourceChapter": 36
    },
    {
      "slug": "17-thuyet-tuong-doi",
      "title": "Thuyết tương đối",
      "prerequisites": [
        "vector",
        "dong-luong-vat-ly",
        "cong-nang-luong"
      ],
      "supportingConcepts": [
        "thuyet-tuong-doi-hep"
      ],
      "status": "draft",
      "number": 17,
      "sourceChapter": 37
    },
    {
      "slug": "18-photon",
      "title": "Photon: Tính hạt của sóng ánh sáng",
      "prerequisites": [
        "thuyet-tuong-doi-hep",
        "cong-nang-luong",
        "song"
      ],
      "supportingConcepts": [
        "photon"
      ],
      "status": "draft",
      "number": 18,
      "sourceChapter": 38
    },
    {
      "slug": "19-song-vat-chat",
      "title": "Tính sóng của hạt",
      "prerequisites": [
        "photon",
        "dong-luong-vat-ly",
        "thuyet-tuong-doi-hep"
      ],
      "supportingConcepts": [
        "ham-song-luong-tu"
      ],
      "status": "draft",
      "number": 19,
      "sourceChapter": 39
    },
    {
      "slug": "20-ham-song-schrodinger",
      "title": "Cơ học lượng tử I: Hàm sóng",
      "prerequisites": [
        "tich-phan",
        "dao-ham",
        "photon"
      ],
      "supportingConcepts": [
        "ham-song-luong-tu"
      ],
      "status": "draft",
      "number": 20,
      "sourceChapter": 40
    },
    {
      "slug": "21-cau-truc-nguyen-tu",
      "title": "Cơ học lượng tử II: Cấu trúc nguyên tử",
      "prerequisites": [
        "ham-song-luong-tu",
        "photon",
        "tu-truong"
      ],
      "supportingConcepts": [
        "spin-luong-tu",
        "nguyen-ly-pauli"
      ],
      "status": "draft",
      "number": 21,
      "sourceChapter": 41
    },
    {
      "slug": "22-chat-ran-ban-dan",
      "title": "Phân tử và vật chất ngưng tụ",
      "prerequisites": [
        "ham-song-luong-tu",
        "nguyen-ly-pauli",
        "nhiet-do-tuyet-doi",
        "dong-dien"
      ],
      "supportingConcepts": [
        "vung-nang-luong"
      ],
      "status": "draft",
      "number": 22,
      "sourceChapter": 42
    },
    {
      "slug": "23-vat-ly-hat-nhan",
      "title": "Vật lý hạt nhân",
      "prerequisites": [
        "photon",
        "thuyet-tuong-doi-hep",
        "cong-nang-luong",
        "dao-ham"
      ],
      "supportingConcepts": [
        "phan-ra-phong-xa"
      ],
      "status": "draft",
      "number": 23,
      "sourceChapter": 43
    },
    {
      "slug": "24-hat-co-ban-vu-tru",
      "title": "Vật lý hạt và vũ trụ học",
      "prerequisites": [
        "thuyet-tuong-doi-hep",
        "photon",
        "phan-ra-phong-xa",
        "nhiet-do-tuyet-doi"
      ],
      "supportingConcepts": [],
      "status": "draft",
      "number": 24,
      "sourceChapter": 44
    }
  ],
  "slides": [],
  "illustration": "field",
  "contentPolicy": "full-source-translation"
}
