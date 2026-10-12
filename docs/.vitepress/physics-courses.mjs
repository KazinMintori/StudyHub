// Physics course catalog.
export const physics1Course = {
  "id": "vat-ly-1",
  "code": "09",
  "name": "Vật lý đại cương 1",
  "short": "Vật lý 1",
  "current": true,
  "description": "Cơ học, dao động, sóng cơ và nhiệt học đại cương.",
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
      "sourceChapter": 2,
      "hasChapterExercises": true
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
  "slides": [],
  "contentPolicy": "full-source-translation"
}

export const physics2Course = {
  "id": "vat-ly-2",
  "code": "05",
  "name": "Vật lý đại cương 2",
  "short": "Vật lý 2",
  "current": true,
  "description": "Điện từ học, quang học và vật lý hiện đại, từ điện tích và điện trường đến hạt cơ bản và vũ trụ học.",
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
        "tich-vo-huong",
        "tich-co-huong",
        "luc",
        "can-bang-co-hoc",
        "duong-dong-chat-luu"
      ],
      "supportingConcepts": [
        "dien-tich",
        "dien-truong",
        "vat-dan-cach-dien",
        "phan-cuc-dien",
        "luong-cuc-dien",
        "don-vi",
        "tich-phan"
      ],
      "status": "ready",
      "number": 1,
      "sourceChapter": 21,
      "hasChapterExercises": true,
      "topicGroups": [
        {
          "title": "Điện tích và sự nhiễm điện",
          "topics": [
            {
              "slug": "dien-tich",
              "title": "Điện tích và cấu tạo vật chất",
              "question": "Điện tích được trao đổi, bảo toàn và lượng tử hóa như thế nào?",
              "source": "21.1"
            },
            {
              "slug": "vat-dan-cach-dien",
              "title": "Vật dẫn, vật cách điện và sự nhiễm điện",
              "question": "Vì sao một vật mang điện có thể hút vật trung hòa?",
              "source": "21.2"
            }
          ]
        },
        {
          "title": "Lực điện và điện trường",
          "topics": [
            {
              "slug": "dinh-luat-coulomb",
              "title": "Định luật Coulomb và chồng chất lực",
              "question": "Làm thế nào xác định đúng độ lớn và hướng tổng lực?",
              "source": "21.3"
            },
            {
              "slug": "dien-truong-luc-dien",
              "title": "Điện trường và lực điện",
              "question": "Điện trường của nguồn khác lực lên điện tích thử ở đâu?",
              "source": "21.4"
            },
            {
              "slug": "tinh-dien-truong",
              "title": "Tính trường của các phân bố điện tích",
              "question": "Đối xứng và tích phân giúp cộng trường liên tục như thế nào?",
              "source": "21.5"
            }
          ]
        },
        {
          "title": "Hướng trường và lưỡng cực",
          "topics": [
            {
              "slug": "duong-suc-dien",
              "title": "Đường sức điện",
              "question": "Đường sức cho biết hướng và độ lớn trường như thế nào?",
              "source": "21.6"
            },
            {
              "slug": "luong-cuc-dien",
              "title": "Lưỡng cực điện",
              "question": "Vì sao lưỡng cực quay trong trường đều dù hợp lực bằng không?",
              "source": "21.7"
            }
          ]
        }
      ]
    },
    {
      "slug": "03-dinh-luat-gauss",
      "title": "Định luật Gauss",
      "prerequisites": [
        "dien-truong",
        "tich-vo-huong",
        "tich-phan",
        "vat-dan-cach-dien"
      ],
      "supportingConcepts": [
        "dien-tich",
        "dien-thong",
        "dinh-luat-gauss",
        "mat-gauss",
        "che-chan-tinh-dien"
      ],
      "status": "ready",
      "number": 2,
      "sourceChapter": 22,
      "topicGroups": [
        {
          "title": "Điện tích và điện thông",
          "topics": [
            {
              "slug": "dien-tich-dien-thong",
              "title": "Điện tích và điện thông",
              "question": "Trường bên ngoài cho biết gì về điện tích bên trong?",
              "source": "22.1"
            },
            {
              "slug": "tinh-dien-thong",
              "title": "Tính điện thông",
              "question": "Diện tích, pháp tuyến và trường đi vào tích phân như thế nào?",
              "source": "22.2"
            }
          ]
        },
        {
          "title": "Định luật và các cấu hình đối xứng",
          "topics": [
            {
              "slug": "dinh-luat-gauss",
              "title": "Định luật Gauss",
              "question": "Vì sao điện thông tổng chỉ phụ thuộc điện tích được bao?",
              "source": "22.3"
            },
            {
              "slug": "ung-dung-gauss",
              "title": "Áp dụng định luật Gauss",
              "question": "Chọn mặt Gauss thế nào để tìm điện trường?",
              "source": "22.4"
            }
          ]
        },
        {
          "title": "Điện tích trên vật dẫn",
          "topics": [
            {
              "slug": "dien-tich-vat-dan",
              "title": "Điện tích và che chắn tĩnh điện trên vật dẫn",
              "question": "Điện tích mặt trong, mặt ngoài và trường trong hốc liên hệ thế nào?",
              "source": "22.5"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "02-dien-the",
      "title": "Điện thế",
      "prerequisites": [
        "cong-nang-luong",
        "dien-truong",
        "tich-phan",
        "gradient"
      ],
      "supportingConcepts": [
        "dien-the",
        "the-nang-dien",
        "electron-volt",
        "mat-dang-the",
        "dinh-luat-gauss",
        "vat-dan-cach-dien"
      ],
      "status": "ready",
      "number": 3,
      "sourceChapter": 23,
      "topicGroups": [
        {
          "title": "Thế năng và điện thế",
          "topics": [
            {
              "slug": "the-nang-dien",
              "title": "Thế năng điện",
              "question": "Công lực điện và năng lượng của hệ liên hệ như thế nào?",
              "source": "23.1"
            },
            {
              "slug": "dien-the",
              "title": "Điện thế và hiệu điện thế",
              "question": "Đại lượng nào thuộc trường và đại lượng nào còn phụ thuộc điện tích thử?",
              "source": "23.2"
            }
          ]
        },
        {
          "title": "Tính toán và hình học điện thế",
          "topics": [
            {
              "slug": "tinh-dien-the",
              "title": "Tính điện thế của các phân bố nguồn",
              "question": "Tìm điện thế của cầu, vòng, thanh và hai bản như thế nào?",
              "source": "23.3"
            },
            {
              "slug": "mat-dang-the",
              "title": "Mặt đẳng thế và vật dẫn",
              "question": "Vì sao đường sức vuông góc mặt đẳng thế?",
              "source": "23.4"
            },
            {
              "slug": "gradient-dien-the",
              "title": "Gradient điện thế",
              "question": "Từ hàm điện thế suy ra từng thành phần điện trường ra sao?",
              "source": "23.5"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "04-tu-dien-dien-moi",
      "title": "Điện dung và điện môi",
      "prerequisites": [
        "dien-the",
        "dien-truong",
        "dinh-luat-gauss",
        "tich-phan",
        "phan-cuc-dien",
        "luong-cuc-dien"
      ],
      "supportingConcepts": [
        "dien-dung",
        "dien-moi",
        "do-dien-tham",
        "do-ben-dien-moi",
        "mat-do-nang-luong-dien-truong",
        "vat-dan-cach-dien",
        "mat-dang-the",
        "cong-nang-luong"
      ],
      "status": "ready",
      "number": 4,
      "sourceChapter": 24,
      "topicGroups": [
        {
          "title": "Cấu trúc, cách mắc và năng lượng",
          "topics": [
            {
              "slug": "tu-dien-dien-dung",
              "title": "Tụ điện và điện dung",
              "question": "Hình học của hai vật dẫn quyết định điện dung như thế nào?",
              "source": "24.1"
            },
            {
              "slug": "mac-tu-dien",
              "title": "Tụ mắc nối tiếp và song song",
              "question": "Đại lượng nào được giữ chung trong mỗi cách mắc?",
              "source": "24.2"
            },
            {
              "slug": "nang-luong-tu-dien",
              "title": "Năng lượng của tụ và điện trường",
              "question": "Công nạp điện được tích trữ ở đâu?",
              "source": "24.3"
            }
          ]
        },
        {
          "title": "Điện môi và phân cực",
          "topics": [
            {
              "slug": "dien-moi",
              "title": "Điện môi",
              "question": "Vì sao thêm chất cách điện có thể làm điện dung tăng?",
              "source": "24.4"
            },
            {
              "slug": "mo-hinh-phan-tu",
              "title": "Mô hình phân tử của điện tích cảm ứng",
              "question": "Điện tích liên kết xuất hiện từ sự sắp xếp nào của các phân tử?",
              "source": "24.5"
            },
            {
              "slug": "gauss-trong-dien-moi",
              "title": "Định luật Gauss trong điện môi",
              "question": "Gauss đếm điện tích tự do và điện tích liên kết ra sao?",
              "source": "24.6"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "05-dong-dien-dien-tro",
      "title": "Dòng điện, điện trở và suất điện động",
      "prerequisites": [
        "dien-tich",
        "dien-the",
        "dien-truong",
        "cong-nang-luong",
        "dan-nhiet",
        "tich-phan"
      ],
      "supportingConcepts": [
        "dong-dien",
        "mat-do-dong-dien",
        "dien-tro-suat",
        "do-dan-dien",
        "dien-tro",
        "suat-dien-dong",
        "dien-tro-trong",
        "nhiet-do-tuyet-doi",
        "do-ben-dien-moi"
      ],
      "status": "ready",
      "number": 5,
      "sourceChapter": 25,
      "topicGroups": [
        {
          "title": "Dòng điện và tính chất vật liệu",
          "topics": [
            {
              "slug": "dong-dien",
              "title": "Dòng điện",
              "question": "Chuyển động ngẫu nhiên và vận tốc trôi tạo dòng như thế nào?",
              "source": "25.1"
            },
            {
              "slug": "dien-tro-suat",
              "title": "Điện trở suất",
              "question": "Vật liệu và nhiệt độ ảnh hưởng đến mật độ dòng ra sao?",
              "source": "25.2"
            },
            {
              "slug": "dien-tro",
              "title": "Điện trở",
              "question": "Từ điện trở suất và hình học suy điện trở của một mẫu như thế nào?",
              "source": "25.3"
            }
          ]
        },
        {
          "title": "Nguồn điện, năng lượng và mô hình vi mô",
          "topics": [
            {
              "slug": "suat-dien-dong",
              "title": "Suất điện động và mạch điện",
              "question": "Nguồn duy trì dòng và điện áp hai cực như thế nào?",
              "source": "25.4"
            },
            {
              "slug": "nang-luong-cong-suat",
              "title": "Năng lượng và công suất trong mạch",
              "question": "Dòng và điện áp cho biết phần tử nhận hay cấp năng lượng ra sao?",
              "source": "25.5"
            },
            {
              "slug": "dan-dien-kim-loai",
              "title": "Mô hình dẫn điện trong kim loại",
              "question": "Tán xạ electron liên hệ với điện trở suất như thế nào?",
              "source": "25.6"
            }
          ]
        }
      ],
      "hasChapterExercises": true
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
  "slides": [
    {
      "note": "01-dien-truong-coulomb",
      "title": "Điện tích được bảo toàn và lượng tử hóa",
      "bullets": [
        "Điện tích cùng dấu đẩy nhau, trái dấu hút nhau.",
        "Tổng đại số điện tích trong hệ kín giữ nguyên.",
        "Phân cực không bắt buộc làm tổng điện tích khác không."
      ],
      "formula": "$$\nQ=ne,\\quad n\\in\\mathbb Z\n$$",
      "example": ""
    },
    {
      "note": "01-dien-truong-coulomb",
      "title": "Lực Coulomb được cộng theo vector",
      "bullets": [
        "Nguồn điểm được dùng khi kích thước nguồn nhỏ so với khoảng cách.",
        "Trong chân không, độ lớn lực tỷ lệ tích độ lớn điện tích và nghịch đảo bình phương khoảng cách.",
        "Hai lực của một cặp bằng nhau về độ lớn và ngược chiều."
      ],
      "formula": "$$\nF=\\frac{k|q_1q_2|}{r^2}\n$$",
      "example": ""
    },
    {
      "note": "01-dien-truong-coulomb",
      "title": "Điện trường khác lực lên điện tích thử",
      "bullets": [
        "Trường của nguồn tồn tại dù không đặt điện tích thử tại điểm khảo sát.",
        "Nguồn thử dương chịu lực cùng chiều trường, nguồn thử âm chịu lực ngược chiều.",
        "Vector đơn vị trong trường nguồn điểm hướng từ nguồn đến điểm khảo sát."
      ],
      "formula": "$$\n\\begin{aligned}\n\\vec F_0&=q_0\\vec E,\\\\\n\\vec E&=\\frac{kq}{r^2}\\hat{\\mathbf r}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "01-dien-truong-coulomb",
      "title": "Đối xứng giúp cộng trường liên tục",
      "bullets": [
        "Các trường thành phần đều được tính tại cùng điểm.",
        "Chia nguồn liên tục thành phần nhỏ rồi tích phân vector trường.",
        "Cận tích phân phủ toàn nguồn và không đếm một phần nguồn hai lần."
      ],
      "formula": "$$\n\\begin{aligned}\n\\vec E&=\\vec E_1+\\vec E_2+\\cdots+\\vec E_n\\\\\n&=\\sum_{i=1}^{n}\\vec E_i.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "01-dien-truong-coulomb",
      "title": "Đường sức biểu diễn hướng điện trường",
      "bullets": [
        "Tiếp tuyến đường sức cùng hướng trường tại mỗi điểm.",
        "Các đường không cắt nhau, mật độ đường biểu diễn độ mạnh tương đối của trường.",
        "Đường sức nhìn chung khác quỹ đạo của hạt mang điện."
      ],
      "formula": "",
      "example": ""
    },
    {
      "note": "01-dien-truong-coulomb",
      "title": "Lưỡng cực có thể quay khi hợp lực bằng không",
      "bullets": [
        "Mômen lưỡng cực hướng từ âm đến dương.",
        "Trong trường đều, hai lực bù nhau nhưng có thể tạo mômen.",
        "Cùng chiều trường là cân bằng bền, ngược chiều là không bền."
      ],
      "formula": "$$\n\\begin{aligned}\np&=qd,\\\\\n\\vec\\tau&=\\vec p\\times\\vec E,\\\\\nU&=-\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "03-dinh-luat-gauss",
      "title": "Điện thông dùng thành phần trường theo pháp tuyến",
      "bullets": [
        "Với mặt phẳng trong trường đều, điện thông bằng tích vô hướng của trường và vector diện tích.",
        "Góc được đo với pháp tuyến. Trường song song mặt cho điện thông bằng không.",
        "Mặt kín luôn chọn pháp tuyến ra ngoài."
      ],
      "formula": "$$\n\\Phi_E=EA\\cos\\varphi\n$$",
      "example": ""
    },
    {
      "note": "03-dinh-luat-gauss",
      "title": "Mặt cong hoặc trường không đều cần tích phân mặt",
      "bullets": [
        "Tính trường và pháp tuyến tại từng phần mặt nhỏ.",
        "Cộng các tích vô hướng có dấu để được điện thông tổng.",
        "Chỉ đưa E ra ngoài tích phân khi độ lớn ấy không đổi trên phần mặt đang xét."
      ],
      "formula": "$$\n\\Phi_E=\\int_A\\vec E\\cdot d\\vec A\n$$",
      "example": ""
    },
    {
      "note": "03-dinh-luat-gauss",
      "title": "Gauss đếm điện tích tổng được bao",
      "bullets": [
        "Điện tích được cộng với dấu.",
        "Trường trong tích phân là trường của cả nguồn trong và ngoài.",
        "Nguồn ngoài không đóng góp điện thông tổng qua mặt kín."
      ],
      "formula": "$$\n\\begin{aligned}\n\\Phi_E&=\\oint\\vec E\\cdot d\\vec A\\\\\n&=\\frac{Q_{\\mathrm{trong}}}{\\varepsilon_0}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "03-dinh-luat-gauss",
      "title": "Đối xứng của nguồn quyết định mặt Gauss",
      "bullets": [
        "Đối xứng cầu dùng cầu đồng tâm. Đối xứng trụ dùng trụ đồng trục.",
        "Đối xứng phẳng dùng hai đáy song song mặt nguồn.",
        "Điện thông không không buộc điện trường không."
      ],
      "formula": "",
      "example": ""
    },
    {
      "note": "03-dinh-luat-gauss",
      "title": "Cầu dẫn và cầu cách điện đều có trường trong khác nhau",
      "bullets": [
        "Trong vật liệu dẫn cân bằng, trường bằng không.",
        "Trong cầu cách điện đều theo thể tích, trường tăng tuyến tính theo bán kính.",
        "Trường ngoài của hai phân bố cầu cùng tổng điện tích giống nhau."
      ],
      "formula": "$$\n\\begin{aligned}\nE_{\\mathrm{trong}}&=\\frac{k|Q|r}{R^3},\\quad r<R,\\\\\nE_{\\mathrm{ngoai}}&=\\frac{k|Q|}{r^2},\\quad r>R.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "03-dinh-luat-gauss",
      "title": "Vật dẫn che chắn nhờ điện tích tái phân bố",
      "bullets": [
        "Nguồn q trong hốc tạo tổng −q trên thành hốc.",
        "Vật dẫn cô lập có tổng qC thì mặt ngoài mang qC + q.",
        "Ngay ngoài mặt dẫn, trường vuông góc mặt."
      ],
      "formula": "$$\n\\begin{aligned}\nQ_{\\mathrm{trong}}&=-q,\\\\\nQ_{\\mathrm{ngoai}}&=q_C+q,\\\\\nE_\\perp&=\\frac{\\sigma}{\\varepsilon_0}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "02-dien-the",
      "title": "Công lực điện làm thế năng giảm",
      "bullets": [
        "Trường tĩnh điện là trường thế. Công giữa hai điểm không phụ thuộc đường đi.",
        "Thế năng thuộc hệ các điện tích và phụ thuộc mốc được chọn.",
        "Nếu chỉ lực điện sinh công thì động năng cộng thế năng được bảo toàn."
      ],
      "formula": "$$\n\\begin{aligned}\nW_{a\\to b}&=U_a-U_b,\\\\\nK_a+U_a&=K_b+U_b.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "02-dien-the",
      "title": "Thế năng nhiều nguồn đếm mỗi cặp một lần",
      "bullets": [
        "Với hai nguồn điểm, thế năng có dấu của tích điện tích.",
        "Công thêm một nguồn vào hệ chỉ tính các cặp liên quan nguồn mới.",
        "Mốc bằng không khi mọi nguồn ở xa vô hạn phù hợp hệ nguồn hữu hạn."
      ],
      "formula": "$$\n\\begin{aligned}\nU_{123}&=\\frac{kq_1q_2}{r_{12}}\\\\\n&\\quad+\\frac{kq_1q_3}{r_{13}}\\\\\n&\\quad+\\frac{kq_2q_3}{r_{23}},\\\\\nU&=k\\sum_{i=1}^{n-1}\\sum_{j=i+1}^{n}\\frac{q_iq_j}{r_{ij}}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "02-dien-the",
      "title": "Điện thế tách ảnh hưởng của điện tích thử",
      "bullets": [
        "Điện thế là thế năng trên mỗi đơn vị điện tích thử.",
        "Hiệu điện thế cho công lực điện trên mỗi coulomb.",
        "Điện thế cao không luôn tương ứng thế năng cao vì điện tích thử có thể âm."
      ],
      "formula": "$$\n\\begin{aligned}\nV&=\\frac{U}{q_0},\\\\\nW_{a\\to b}&=q_0(V_a-V_b),\\\\\n1\\,\\mathrm V&=1\\,\\mathrm{J/C}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "02-dien-the",
      "title": "Cộng điện thế bằng tổng đại số hoặc tích phân",
      "bullets": [
        "Điện thế là vô hướng, nên cộng phần đóng góp có dấu.",
        "Phân bố liên tục được chia thành các phần dq.",
        "Nguồn kéo dài vô hạn thường cần mốc hữu hạn thay cho vô hạn."
      ],
      "formula": "$$\n\\begin{aligned}\nV&=k\\int \\frac{dq}{r},\\\\\nV_a-V_b&=\\int_a^b\\vec E\\cdot d\\vec\\ell.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "02-dien-the",
      "title": "Mặt đẳng thế vuông góc điện trường",
      "bullets": [
        "Dịch chuyển trên mặt đẳng thế không làm lực điện sinh công.",
        "Tại điểm trường khác không, trường vuông góc mặt đẳng thế.",
        "Vật dẫn cân bằng và hốc kín không có nguồn riêng là miền đẳng thế."
      ],
      "formula": "$$\ndV=-\\vec E\\cdot d\\vec\\ell\n$$",
      "example": ""
    },
    {
      "note": "02-dien-the",
      "title": "Gradient cho trường từ hàm điện thế",
      "bullets": [
        "Lấy âm đạo hàm riêng theo mỗi tọa độ để có thành phần trường.",
        "Trường hướng về phía điện thế giảm nhanh nhất.",
        "Cộng một hằng số vào điện thế không thay đổi điện trường."
      ],
      "formula": "$$\n\\begin{aligned}\nE_x&=-\\frac{\\partial V}{\\partial x},\\\\\nE_y&=-\\frac{\\partial V}{\\partial y},\\\\\nE_z&=-\\frac{\\partial V}{\\partial z},\\\\\n\\vec E&=-\\nabla V.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Điện dung thuộc cấu hình của hai vật dẫn",
      "bullets": [
        "Điện tích Q là độ lớn trên từng bản. Tổng điện tích của hai bản ±Q bằng không.",
        "Hiệu điện thế được lấy từ bản dương đến bản âm.",
        "Với hình học và điện môi tuyến tính giữ nguyên, tăng Q làm V tăng cùng tỉ lệ."
      ],
      "formula": "$$\n\\begin{aligned}\nC&=\\frac{Q}{V_{ab}},\\\\\n1\\,\\mathrm F&=1\\,\\mathrm{C/V}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Tìm điện dung bằng trường và hiệu điện thế",
      "bullets": [
        "Giả sử hai vật dẫn mang ±Q, dùng đối xứng tìm điện trường.",
        "Tích phân trường từ bản dương đến bản âm để tính hiệu điện thế.",
        "Trong tụ phẳng, chỉ bỏ hiệu ứng mép khi khe nhỏ so với kích thước bản."
      ],
      "formula": "$$\n\\begin{aligned}\nV_{ab}&=\\int_a^b\\vec E\\cdot d\\vec\\ell,\\\\\nC_0&=\\frac{\\varepsilon_0 A}{d}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Nối tiếp giữ cùng điện tích, song song giữ cùng điện áp",
      "bullets": [
        "Chuỗi tụ bắt đầu chưa nạp có các nút giữa trung hòa và cô lập.",
        "Ở chuỗi ấy, độ lớn điện tích trên mọi tụ bằng nhau và các điện áp cộng.",
        "Các nhánh song song nối cùng hai nút nên có cùng điện áp."
      ],
      "formula": "$$\n\\begin{aligned}\n\\frac1{C_s}&=\\frac1{C_1}+\\frac1{C_2}+\\frac1{C_3},\\\\\nC_p&=C_1+C_2+C_3.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Công nạp tích trữ thành năng lượng điện trường",
      "bullets": [
        "Điện áp tăng dần trong quá trình nạp nên công không bằng Q nhân điện áp cuối.",
        "Ba biểu thức năng lượng là các cách viết tương đương cho tụ tuyến tính.",
        "Năng lượng điện trường và thế năng của tụ là cùng một năng lượng."
      ],
      "formula": "$$\n\\begin{aligned}\nU&=\\frac{Q^2}{2C}=\\frac12 CV^2,\\\\\nU&=\\frac12 QV,\\\\\nu_0&=\\frac12\\varepsilon_0 E^2.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Điện môi tăng điện dung nhờ sự phân cực",
      "bullets": [
        "Điện tích liên kết trên mặt điện môi tạo trường chống lại trường của các bản.",
        "Điện môi tuyến tính đồng nhất lấp toàn khe làm điện dung tăng K lần.",
        "Giữ điện tích tự do thì trường và điện áp giảm K lần."
      ],
      "formula": "$$\n\\begin{aligned}\n\\varepsilon&=K\\varepsilon_0,\\\\\nC&=KC_0,\\\\\nE&=E_0/K,\\quad Q=Q_0.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Phân cực ở mức phân tử không làm điện tích chảy tự do",
      "bullets": [
        "Phân tử không phân cực bị tách tương đối các tâm điện tích trong trường.",
        "Phân tử phân cực có lưỡng cực thường trực và chịu mômen định hướng.",
        "Trong vật liệu trung hòa, các điện tích liên kết trong thể tích có thể bù nhau, còn ở mặt ngoài thì không."
      ],
      "formula": "$$\n\\begin{aligned}\n\\vec\\tau&=\\vec p\\times\\vec E,\\\\\nU_{\\mathrm{dipole}}&=-\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Điều kiện nối nguồn quyết định năng lượng sau khi thêm điện môi",
      "bullets": [
        "Ngắt nguồn giữ điện tích tự do, vì các bản không trao đổi điện tích với nguồn.",
        "Giữ nguồn lý tưởng thì điện áp giữ nguyên và nguồn chuyển thêm điện tích.",
        "Độ bền điện môi đặt giới hạn trường mà mô hình cách điện còn dùng được."
      ],
      "formula": "$$\n\\begin{aligned}\nU_Q&=U_0/K,\\quad Q=Q_0,\\\\\nU_V&=KU_0,\\quad V=V_0.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "04-tu-dien-dien-moi",
      "title": "Gauss cải biên chỉ đếm điện tích tự do",
      "bullets": [
        "Điện trường thực đã bao gồm tác dụng của điện tích tự do và điện tích liên kết.",
        "Dạng cải biên giữ K trong tích phân nếu vật liệu thay đổi trên mặt Gauss.",
        "Mật độ năng lượng trong điện môi dùng điện trường thực và độ điện thẩm của vật liệu."
      ],
      "formula": "$$\n\\begin{aligned}\n\\oint_S K\\vec E\\cdot d\\vec A&=\\frac{Q_{\\mathrm{free}}}{\\varepsilon_0},\\\\\nu&=\\frac12\\varepsilon E^2.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Dòng điện đo điện lượng chuyển qua tiết diện",
      "bullets": [
        "Dòng là đại lượng vô hướng. Chiều quy ước theo điện tích dương.",
        "Electron trôi ngược chiều dòng quy ước trong kim loại.",
        "Dòng ổn định trong một vòng không bị bóng đèn hoặc điện trở tiêu thụ."
      ],
      "formula": "$$\n\\begin{aligned}\nI&=\\frac{dQ}{dt},\\\\\n1\\,\\mathrm A&=1\\,\\mathrm{C/s}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Mật độ dòng điện giữ thông tin về hướng",
      "bullets": [
        "Chuyển động ngẫu nhiên không tạo dòng thuần. Độ trôi nhỏ tạo dòng.",
        "Cùng một dòng qua dây to và dây nhỏ có thể cho mật độ dòng khác nhau.",
        "Điện tích âm và vận tốc trôi ngược trường vẫn cho mật độ dòng cùng chiều trường."
      ],
      "formula": "$$\n\\begin{aligned}\nI&=n|q|v_dA,\\\\\nJ&=I/A,\\\\\n\\vec J&=nq\\vec v_d.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Điện trở suất thuộc vật liệu và điều kiện khảo sát",
      "bullets": [
        "Độ dẫn điện là nghịch đảo điện trở suất.",
        "Vật liệu Ohm có điện trở suất không đổi theo độ lớn trường trong miền xét.",
        "Hệ số nhiệt cần dùng trong khoảng nhiệt độ mà gần đúng tuyến tính còn phù hợp."
      ],
      "formula": "$$\n\\begin{aligned}\n\\rho&=E/J,\\\\\n\\sigma&=1/\\rho,\\\\\n\\rho(T)&\\approx\\rho_0[1+\\alpha(T-T_0)].\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Điện trở còn phụ thuộc chiều dài và tiết diện",
      "bullets": [
        "Dây đồng nhất, tiết diện đều có điện trở tỉ lệ chiều dài và nghịch tiết diện.",
        "Định nghĩa R = V/I không tự khẳng định định luật Ohm.",
        "Muốn V tỉ lệ I phải giữ R không đổi trong điều kiện khảo sát."
      ],
      "formula": "$$\n\\begin{aligned}\nR&=\\frac{\\rho L}{A},\\\\\nV&=IR,\\\\\n1\\,\\Omega&=1\\,\\mathrm{V/A}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Suất điện động là năng lượng trên mỗi coulomb",
      "bullets": [
        "Nguồn dùng tác động không tĩnh điện đưa điện tích lên điện thế cao.",
        "Suất điện động có đơn vị volt và không phải lực cơ học.",
        "Nguồn thực có điện trở trong, nên điện áp hai cực phụ thuộc tải."
      ],
      "formula": "$$\n\\begin{aligned}\nV_{ab}&=\\mathcal E-Ir,\\\\\nI&=\\frac{\\mathcal E}{R+r}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Mắc dụng cụ đo làm thay đổi mạch nếu chọn sai vị trí",
      "bullets": [
        "Ampe kế lý tưởng có điện trở bằng không, mắc nối tiếp.",
        "Vôn kế lý tưởng có điện trở vô hạn, mắc song song giữa hai điểm cần đo.",
        "Mạch hở và ngắn mạch có điện áp, dòng điện rất khác nhau."
      ],
      "formula": "$$\n\\begin{aligned}\nI_{\\mathrm{oc}}&=0,\\\\\nV_{\\mathrm{oc}}&=\\mathcal E,\\\\\nI_{\\mathrm{sc}}&=\\mathcal E/r,\\\\\nV_{\\mathrm{sc}}&=0.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Công suất có dấu phân biệt nhận và cấp năng lượng",
      "bullets": [
        "Dòng đi vào đầu a cho công suất nhận bằng (Va − Vb)I.",
        "Điện trở nhận điện năng rồi chuyển hóa thành nhiệt hoặc các dạng khác.",
        "Nguồn phát điện có phần chuyển hóa và phần hao trong điện trở trong."
      ],
      "formula": "$$\n\\begin{aligned}\nP&=V_{ab}I,\\\\\nP_R&=I^2R,\\\\\nP_{\\mathrm{ra}}&=\\mathcal EI-I^2r.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "05-dong-dien-dien-tro",
      "title": "Tán xạ liên hệ vận tốc trôi với điện trở suất",
      "bullets": [
        "Mô hình cổ điển dùng thời gian tự do trung bình giữa các va chạm.",
        "Độ trôi có hướng rất nhỏ so với chuyển động ngẫu nhiên.",
        "Mô hình dự đoán điện trở suất không đổi theo trường khi n và τ không đổi theo trường."
      ],
      "formula": "$$\n\\begin{aligned}\n\\vec v_d&=\\frac{q\\tau}{m}\\vec E,\\\\\n\\rho&=\\frac{m}{ne^2\\tau}.\n\\end{aligned}\n$$",
      "example": ""
    }
  ],
  "illustration": "field",
  "contentPolicy": "full-source-translation"
}
