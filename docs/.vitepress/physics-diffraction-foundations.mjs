export const diffractionConcepts={
  "nhieu-xa-fresnel": {
    "name": "Nhiễu xạ Fresnel",
    "aliases": [
      "Nhiễu xạ Fresnel",
      "nhiễu xạ Fresnel",
      "nhiễu xạ trường gần"
    ],
    "definition": "Nhiễu xạ Fresnel là miền nhiễu xạ trong đó độ cong của mặt sóng còn ảnh hưởng đáng kể tới pha. Nguồn hoặc điểm quan sát tương đối gần khẩu độ hoặc vật cản.",
    "example": "Bóng mép dao được chiếu bằng nguồn điểm gần không có ranh giới sáng–tối hoàn toàn sắc nét.",
    "use": "Chọn mô hình truyền sóng trước khi tính hệ vân.",
    "question": "Chỉ biết khoảng cách hữu hạn có đủ kết luận là Fresnel không?",
    "answer": "Không. Mọi khoảng cách thực đều hữu hạn. Cần xét khoảng cách so với thang kích thước khẩu độ và bước sóng để biết độ cong mặt sóng có thể bỏ qua hay không."
  },
  "nhieu-xa-fraunhofer": {
    "name": "Nhiễu xạ Fraunhofer",
    "aliases": [
      "Nhiễu xạ Fraunhofer",
      "nhiễu xạ Fraunhofer",
      "nhiễu xạ trường xa"
    ],
    "definition": "Nhiễu xạ Fraunhofer dùng sóng tới gần phẳng và các đường từ khẩu độ tới một điểm quan sát gần song song. Pha truyền được mô tả theo hướng quan sát.",
    "example": "Đặt màn trong tiêu diện một thấu kính cho phép ghi các hướng nhiễu xạ khác nhau tại các vị trí khác nhau trên màn.",
    "use": "Áp dụng công thức khe đơn, cách tử và khẩu độ tròn của quang học sóng miền xa.",
    "question": "Màn ở gần khẩu độ có luôn loại trừ Fraunhofer không?",
    "answer": "Không. Hệ thấu kính thích hợp có thể tạo điều kiện tương đương miền xa tại tiêu diện."
  },
  "nhieu-xa-khe-don": {
    "name": "Nhiễu xạ một khe",
    "aliases": [
      "Nhiễu xạ một khe",
      "nhiễu xạ một khe",
      "nhiễu xạ khe đơn"
    ],
    "definition": "Sóng từ các phần khác nhau của cùng một khe chồng chất và tạo hệ vân. Trong miền Fraunhofer, các cực tiểu thỏa $a\\sin\\theta=m\\lambda$ với m nguyên khác không.",
    "example": "Ở cực tiểu đầu, mỗi dải trong nửa trên khe có một dải ở nửa dưới cách nó nửa bề rộng khe và tới ngược pha.",
    "use": "Suy bề rộng khe, bước sóng hoặc vị trí những miền tối.",
    "question": "Bậc m bằng không có là vân tối không?",
    "answer": "Không. Tại trục trung tâm các phần khe cùng pha, tạo cực đại trung tâm."
  },
  "ham-sinc-nhieu-xa": {
    "name": "Hàm sinc trong nhiễu xạ",
    "aliases": [
      "Hàm sinc trong nhiễu xạ",
      "hàm sinc nhiễu xạ",
      "sinc"
    ],
    "definition": "Trong quy ước radian, hàm sinc là sin x chia x khi x khác không, và nhận giá trị liên tục bằng một tại không. Bình phương hàm này mô tả cường độ khe đơn chiếu đều.",
    "example": "Điểm ở giữa góc từ tâm tới cực tiểu đầu không có cường độ bằng nửa đỉnh, vì bình phương sinc không tuyến tính.",
    "use": "Tính cường độ, tìm cực tiểu và cực đại phụ của một khe.",
    "question": "Thấy tử số bằng không ở đối số không có được kết luận cường độ bằng không không?",
    "answer": "Không. Mẫu cũng bằng không. Giới hạn của sin x chia x là một."
  },
  "bao-nhieu-xa": {
    "name": "Bao nhiễu xạ",
    "aliases": [
      "Bao nhiễu xạ",
      "bao nhiễu xạ",
      "đường bao nhiễu xạ"
    ],
    "definition": "Bao nhiễu xạ mô tả sự biến thiên cường độ theo góc do bề rộng hữu hạn của từng khe, bên cạnh các vân do pha giữa những khe khác nhau.",
    "example": "Hai khe rộng tạo nhiều vân giao thoa hẹp nằm trong một miền trung tâm rộng của bao khe đơn.",
    "use": "Tính cường độ khi không thể coi khe là nguồn điểm và giải thích bậc bị khuyết.",
    "question": "Giữ khoảng tâm khe nhưng giảm bề rộng khe làm nhịp vân giao thoa đổi hay bao đổi?",
    "answer": "Bao nhiễu xạ rộng ra. Điều kiện pha giữa hai tâm vẫn dùng cùng khoảng tâm, nên vị trí các bậc giao thoa danh nghĩa giữ nguyên."
  },
  "bac-khuyet": {
    "name": "Bậc giao thoa bị khuyết",
    "aliases": [
      "Bậc giao thoa bị khuyết",
      "bậc khuyết",
      "cực đại bị khuyết"
    ],
    "definition": "Bậc khuyết xuất hiện khi một cực đại giao thoa giữa các khe trùng một cực tiểu nhiễu xạ của từng khe, làm cường độ tại hướng ấy bằng không.",
    "example": "Nếu khoảng tâm khe gấp bốn bề rộng khe, các bậc giao thoa là bội khác không của bốn bị khuyết khi hướng tương ứng tồn tại.",
    "use": "Suy tỉ số khoảng khe và bề rộng từ các bậc vắng mặt.",
    "question": "Biết một bậc bị khuyết có luôn xác định duy nhất bề rộng khe không?",
    "answer": "Không. Một cực đại có thể trùng cực tiểu nhiễu xạ bậc một hoặc bậc cao hơn. Cần xác định bậc bao hoặc thêm dữ kiện."
  },
  "cach-tu-nhieu-xa": {
    "name": "Cách tử nhiễu xạ",
    "aliases": [
      "Cách tử nhiễu xạ",
      "cách tử nhiễu xạ",
      "cách tử truyền qua",
      "cách tử phản xạ"
    ],
    "definition": "Cách tử có nhiều khe hoặc rãnh song song cách đều. Khi chúng được chiếu kết hợp, tổng trường tạo những cực đại chính hẹp phụ thuộc bước sóng.",
    "example": "Các rãnh trên đĩa quang có thể phân tách ánh sáng trắng thành các màu ở những hướng khác nhau.",
    "use": "Đo bước sóng và tạo phổ để khảo sát ánh sáng.",
    "question": "Tăng số khe nhưng giữ khoảng khe có làm góc cực đại chính đổi không?",
    "answer": "Không trong mô hình khe giống nhau. Các đỉnh hẹp hơn, nhưng điều kiện góc vẫn do khoảng khe và bước sóng quyết định."
  },
  "nang-suat-phan-giai-pho": {
    "name": "Năng suất phân giải phổ",
    "aliases": [
      "Năng suất phân giải phổ",
      "năng suất phân giải phổ",
      "độ phân giải phổ",
      "chromatic resolving power"
    ],
    "definition": "Năng suất phân giải phổ là tỉ số bước sóng với khoảng chênh bước sóng nhỏ nhất vừa phân biệt được theo tiêu chuẩn đang dùng. Với cách tử lý tưởng, nó bằng tích bậc phổ và số khe được chiếu.",
    "example": "Hai vạch rất gần nhau cần nhiều khe được chiếu hoặc bậc phổ cao hơn để tách được hai đỉnh.",
    "use": "Chọn số khe và bậc quan sát khi đo các vạch phổ gần nhau.",
    "question": "Có thể dùng bậc cao tùy ý để phân giải phổ không?",
    "answer": "Không. Bậc phải tồn tại về góc, và các bậc khác có thể chồng phổ. Thiết bị còn có các giới hạn thực tế."
  },
  "dieu-kien-bragg": {
    "name": "Điều kiện Bragg",
    "aliases": [
      "Điều kiện Bragg",
      "điều kiện Bragg",
      "phản xạ Bragg",
      "nhiễu xạ tia X"
    ],
    "definition": "Điều kiện Bragg cho tăng cường tán xạ từ một họ mặt mạng cách nhau d. Nó có dạng $2d\\sin\\theta=m\\lambda$, với m nguyên dương và góc đo với mặt mạng.",
    "example": "Đo góc cực đại với bước sóng tia X đã biết cho phép suy khoảng giữa hai mặt nguyên tử.",
    "use": "Khảo sát cấu trúc tinh thể hoặc đo bước sóng bức xạ.",
    "question": "Góc Bragg có phải góc với pháp tuyến mặt mạng không?",
    "answer": "Không. Trong công thức này, góc được đo với mặt mạng. Góc với pháp tuyến là góc phụ."
  },
  "dia-airy": {
    "name": "Đĩa Airy",
    "aliases": [
      "Đĩa Airy",
      "đĩa Airy",
      "Airy disk"
    ],
    "definition": "Đĩa Airy là đốm sáng trung tâm trong hệ vân nhiễu xạ của khẩu độ tròn. Biên đĩa là vòng tối đầu, có bán kính góc thỏa $\\sin\\theta_1=1{,}22\\lambda/D$.",
    "example": "Một ngôi sao được coi như nguồn điểm vẫn cho một ảnh có bề rộng hữu hạn qua khẩu độ tròn.",
    "use": "Tính kích thước vệt hội tụ và giới hạn phân giải ảnh.",
    "question": "Hệ số 1,22 cho bán kính hay đường kính đĩa theo góc?",
    "answer": "Cho bán kính góc từ tâm tới vòng tối đầu. Đường kính góc nhỏ của đĩa gấp đôi giá trị ấy."
  },
  "tieu-chuan-rayleigh": {
    "name": "Tiêu chuẩn Rayleigh",
    "aliases": [
      "Tiêu chuẩn Rayleigh",
      "tiêu chuẩn Rayleigh",
      "giới hạn phân giải"
    ],
    "definition": "Hai nguồn điểm vừa được phân giải theo Rayleigh khi tâm ảnh nhiễu xạ của nguồn này trùng cực tiểu đầu của nguồn kia. Với khẩu độ tròn, độ tách góc giới hạn thỏa $\\sin\\theta_R=1{,}22\\lambda/D$.",
    "example": "Tăng đường kính vật kính làm hai ảnh điểm gần nhau dễ được phân biệt hơn về giới hạn nhiễu xạ.",
    "use": "So các dụng cụ quan sát, tính chi tiết nhỏ nhất hoặc chọn đường kính khẩu độ.",
    "question": "Phóng to một ảnh chưa phân giải có làm hai chi tiết tự tách ra không?",
    "answer": "Không. Ảnh lớn hơn nhưng thông tin phân biệt đã bị giới hạn bởi sự chồng các ảnh nhiễu xạ."
  },
  "anh-toan-ky": {
    "name": "Ảnh toàn ký",
    "aliases": [
      "Ảnh toàn ký",
      "ảnh toàn ký",
      "holography",
      "hologram"
    ],
    "definition": "Ảnh toàn ký ghi hệ vân giao thoa giữa chùm chuẩn và ánh sáng từ vật, rồi dùng nhiễu xạ để tái tạo mặt sóng. Người quan sát có thể thấy thị sai của hình ảnh ba chiều.",
    "example": "Một điểm vật ghi các vành giao thoa với sóng chuẩn phẳng. Khi chiếu lại, các sóng nhiễu xạ có thể tạo cả ảnh thật và ảnh ảo.",
    "use": "Phân tích sự ghi và tái tạo thông tin pha của một vật.",
    "question": "Chỉ chiếu sáng vật và chụp cường độ như ảnh thường có đủ để ghi ảnh toàn ký không?",
    "answer": "Không. Cần quan hệ pha với chùm chuẩn để biến thông tin mặt sóng thành cấu trúc vân."
  }
}

export const diffractionWikiDetails={
  "nhieu-xa-fresnel": "Mỗi phần mặt sóng truyền qua khẩu độ đóng góp một sóng thứ cấp. Trong miền gần, khoảng truyền từ các phần khác nhau tới điểm xét phải giữ đủ sự biến thiên pha do độ cong. Chồng chất tạo các vân và làm ánh sáng đi vào một phần miền bóng hình học.\n\nFresnel và Fraunhofer mô tả hai miền gần đúng của cùng sự truyền sóng. Việc dùng tên khác không tạo hai cơ chế vật lý khác nhau. Trong miền xa hoặc khi hệ thấu kính tạo điều kiện tương đương, có thể chuyển sang mô hình Fraunhofer đơn giản hơn.",
  "nhieu-xa-fraunhofer": "Với khe hẹp, chênh đường từ hai điểm cách nhau một đoạn y tới cùng một hướng là gần bằng $y\\sin\\theta$. Chính quan hệ tuyến tính này làm pha tăng đều theo tọa độ trong khe.\n\nGần đúng miền xa khác gần đúng góc nhỏ. Fraunhofer vẫn có thể xét góc lớn bằng sin của góc. Chỉ khi đổi vị trí trên màn thành công thức tuyến tính mới cần thêm $\\tan\\theta\\approx\\sin\\theta\\approx\\theta$.",
  "nhieu-xa-khe-don": "Chia khe thành hai nửa. Khi $(a/2)\\sin\\theta=\\lambda/2$, các đóng góp được ghép theo cặp ngược pha và toàn trường bằng không. Chia thành nhiều phần phù hợp cho các cực tiểu tiếp theo. Miền bậc là $m=\\pm1,\\pm2,\\ldots$ và phải giữ $|m\\lambda/a|\\le1$.\n\nTọa độ màn phẳng là $y_m=R\\tan\\theta_m$. Chỉ ở góc nhỏ mới có $y_m\\approx Rm\\lambda/a$. Bề rộng trung tâm giữa hai cực tiểu đầu khi ấy xấp xỉ $2R\\lambda/a$.",
  "ham-sinc-nhieu-xa": "Đặt $\\gamma=\\pi a\\sin\\theta/\\lambda$. Khi đó:\n\n$$\nI=I_0\\left(\\frac{\\sin\\gamma}{\\gamma}\\right)^2.\n$$\n\nCực tiểu nằm ở các bội nguyên khác không của pi. Các cực đại phụ thỏa $\\tan\\gamma=\\gamma$. Thừa số sinc có thể âm, biểu thị sự đổi pha của trường. Độ lớn biên độ vẫn không âm và cường độ dùng bình phương thừa số.",
  "bao-nhieu-xa": "Với hai khe giống nhau kết hợp đồng pha, cường độ là tích của thừa số giao thoa và bình phương sinc của từng khe. Khoảng tâm d xuất hiện trong pha giữa hai khe, còn bề rộng a xuất hiện trong pha giữa hai mép một khe.\n\nTại góc mà bao bằng không, toàn hệ tối dù các tâm khe đang đồng pha. Khi bao biến thiên mạnh, vị trí cực đại của tích có thể lệch so với cực đại của riêng thừa số giao thoa. Cần phân biệt hướng bậc giao thoa danh nghĩa với đỉnh thật của tích.",
  "bac-khuyet": "Hai điều kiện đồng thời là:\n\n$$\n\\begin{aligned}d\\sin\\theta&=m_i\\lambda\\\\a\\sin\\theta&=m_d\\lambda\\\\m_i&=(d/a)m_d.\\end{aligned}\n$$\n\nBậc $m_d$ nguyên khác không. Bậc $m_i$ cũng nguyên và phải nằm trong miền góc có thể có. Bậc trung tâm không bị khuyết bởi điều kiện này. Đếm số vân trong một miền bao cần nêu cách xử lý các bậc nằm đúng tại biên cực tiểu.",
  "cach-tu-nhieu-xa": "Ở tới vuông góc, $d\\sin\\theta_m=m\\lambda$, với $m=0,\\pm1,\\pm2,\\ldots$. Mật độ vạch là nghịch đảo khoảng cách d, nên phải đổi đúng đơn vị khi chuyển từ vạch trên milimet sang mét.\n\nCực đại chính được tạo khi tất cả các khe đồng pha. Có N trừ một cực tiểu giữa hai đỉnh chính. Bề rộng pha của đỉnh giữa hai cực tiểu sát nó là $4\\pi/N$, nên tăng số khe làm đỉnh hẹp đi. Công thức tới vuông góc cần điều chỉnh khi chùm tới xiên.",
  "nang-suat-phan-giai-pho": "Tiêu chuẩn xét đỉnh của một vạch trùng cực tiểu đầu của vạch kia. Trong gần đúng chênh bước sóng nhỏ:\n\n$$\n\\mathcal R=\\frac{\\lambda}{\\Delta\\lambda}=mN.\n$$\n\nN là số khe thật sự được chiếu sáng. Đây là khả năng phân biệt bước sóng, khác năng suất phân giải ảnh mô tả sự tách hai vật gần nhau theo góc. Các tiêu chuẩn là quy ước làm việc và không thay thế việc xét nhiễu, hình dạng vạch và sai số cách tử.",
  "dieu-kien-bragg": "Sóng từ hai mặt liên tiếp đi thêm một đoạn khi tới và một đoạn khi ra, tổng là $2d\\sin\\theta$. Khi tổng ấy bằng một số nguyên bước sóng, các đóng góp tăng cường theo hướng phản xạ.\n\nMỗi họ mặt mạng có một d riêng. Tinh thể ba chiều có nhiều họ mặt, nên có nhiều tập hướng cực đại. Chỉ giữ các bậc thỏa $m\\lambda\\le2d$. Trong tinh thể keo đặt trong chất lỏng, phải dùng bước sóng trong chất lỏng. Không được thay nó bằng bước sóng chân không mà bỏ chiết suất.",
  "dia-airy": "Với nguồn ở xa, bán kính đĩa trên tiêu diện gần bằng $1{,}22\\lambda f/D$. Các vòng sáng và tối tiếp theo nằm quanh đĩa. Cường độ và năng lượng tập trung chủ yếu ở miền trung tâm, nhưng không có một điểm hội tụ hình học có kích thước bằng không.\n\nGiảm D làm vệt ảnh trải rộng. Vì vậy, khép khẩu có thể giảm một số quang sai và tăng độ sâu trường ảnh nhưng đồng thời làm nhiễu xạ rõ hơn. Khả năng phân giải phải xét các tác dụng ấy với nhau.",
  "tieu-chuan-rayleigh": "Ở góc nhỏ, hai điểm cách ngang s và ở xa R có độ tách góc gần bằng $s/R$. Kết hợp với tiêu chuẩn Rayleigh cho $s_{\\min}\\approx1{,}22\\lambda R/D$.\n\nTiêu chuẩn là một cách xác định mức vừa phân biệt được. Các điều kiện phát sáng, độ tương phản và nhiễu còn ảnh hưởng quan sát thực. Phân giải hai vật theo góc khác phân giải hai vạch theo bước sóng. Không dùng cùng một ký hiệu độ phân giải mà bỏ ý nghĩa đại lượng đang so.",
  "anh-toan-ky": "Với sóng chuẩn phẳng tới vuông góc và điểm vật cách phim $b_0$, các vành sáng thỏa $b_m-b_0=m\\lambda$. Hình học cho:\n\n$$\nr_m^2=2m\\lambda b_0+m^2\\lambda^2.\n$$\n\nKhi $m\\lambda\\ll b_0$, có $r_m\\approx\\sqrt{2m\\lambda b_0}$. Bản ghi tái tạo sóng hội tụ tới ảnh thật và sóng phân kỳ có vẻ phát ra từ ảnh ảo. Trong lúc ghi, cần tính kết hợp đủ dài và độ ổn định cơ học ở thang nhỏ hơn bước sóng."
}

export const diffractionWikiConnections={
  "nhieu-xa-fresnel": [
    "nguyen-ly-huygens",
    "nhieu-xa-fraunhofer",
    "mat-song"
  ],
  "nhieu-xa-fraunhofer": [
    "nhieu-xa-fresnel",
    "nhieu-xa-khe-don",
    "cach-tu-nhieu-xa"
  ],
  "nhieu-xa-khe-don": [
    "nhieu-xa-fraunhofer",
    "ham-sinc-nhieu-xa",
    "hieu-duong-di"
  ],
  "ham-sinc-nhieu-xa": [
    "nhieu-xa-khe-don",
    "vector-pha",
    "cuong-do-buc-xa"
  ],
  "bao-nhieu-xa": [
    "ham-sinc-nhieu-xa",
    "bac-khuyet",
    "giao-thoa-hai-khe"
  ],
  "bac-khuyet": [
    "bao-nhieu-xa",
    "cach-tu-nhieu-xa",
    "nhieu-xa-khe-don"
  ],
  "cach-tu-nhieu-xa": [
    "nguon-ket-hop",
    "nang-suat-phan-giai-pho",
    "bac-khuyet"
  ],
  "nang-suat-phan-giai-pho": [
    "cach-tu-nhieu-xa",
    "tieu-chuan-rayleigh",
    "tan-sac"
  ],
  "dieu-kien-bragg": [
    "hieu-duong-di",
    "cach-tu-nhieu-xa",
    "chiet-suat"
  ],
  "dia-airy": [
    "tieu-chuan-rayleigh",
    "thau-kinh-mong",
    "nhieu-xa-anh-sang"
  ],
  "tieu-chuan-rayleigh": [
    "dia-airy",
    "nang-suat-phan-giai-pho",
    "cuong-do-buc-xa"
  ],
  "anh-toan-ky": [
    "nguon-ket-hop",
    "giao-thoa-song",
    "nhieu-xa-fraunhofer"
  ]
}
