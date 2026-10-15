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
        "dien-the",
        "suat-dien-dong",
        "dien-dung",
        "cong-nang-luong",
        "dao-ham",
        "tich-phan"
      ],
      "supportingConcepts": [
        "dien-tro-tuong-duong",
        "quy-tac-kirchhoff",
        "dien-ke",
        "ampe-ke",
        "von-ke",
        "chiet-ap-can-bang",
        "mach-rc",
        "hang-so-thoi-gian",
        "dien-tro-trong"
      ],
      "status": "ready",
      "number": 6,
      "sourceChapter": 26,
      "topicGroups": [
        {
          "title": "Tổ hợp điện trở và mạch nhiều nhánh",
          "topics": [
            {
              "slug": "noi-tiep-song-song",
              "title": "Điện trở nối tiếp và song song",
              "question": "Dòng và điện áp được phân chia thế nào trong từng kiểu mắc?",
              "source": "26.1"
            },
            {
              "slug": "kirchhoff",
              "title": "Quy tắc Kirchhoff",
              "question": "Lập phương trình cho mạch không thu gọn được bằng nối tiếp và song song ra sao?",
              "source": "26.2"
            }
          ]
        },
        {
          "title": "Đo điện, quá trình chuyển tiếp và phân phối điện",
          "topics": [
            {
              "slug": "dung-cu-do",
              "title": "Dụng cụ đo điện",
              "question": "Dụng cụ đo ảnh hưởng đến mạch như thế nào?",
              "source": "26.3"
            },
            {
              "slug": "mach-rc",
              "title": "Mạch điện trở và tụ điện",
              "question": "Vì sao điện tích và dòng thay đổi theo hàm mũ khi nạp hoặc phóng tụ?",
              "source": "26.4"
            },
            {
              "slug": "phan-phoi-dien",
              "title": "Hệ thống phân phối điện",
              "question": "Mạch nhánh, bảo vệ quá dòng và dây bảo vệ thực hiện những chức năng gì?",
              "source": "26.5"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "07-tu-truong-luc-tu",
      "title": "Từ trường và lực từ",
      "prerequisites": [
        "vector",
        "tich-co-huong",
        "dien-tich",
        "dong-dien",
        "luc",
        "momen-luc",
        "momen-quan-tinh",
        "cong-nang-luong",
        "dao-ham",
        "tich-phan"
      ],
      "supportingConcepts": [
        "tu-truong",
        "luc-tu-tren-dien-tich",
        "duong-suc-tu",
        "tu-thong",
        "chuyen-dong-hat-trong-tu-truong",
        "bo-chon-van-toc",
        "khoi-pho",
        "momen-tu",
        "luong-cuc-tu",
        "suat-phan-dien-dong",
        "hieu-ung-hall"
      ],
      "status": "ready",
      "number": 7,
      "sourceChapter": 27,
      "topicGroups": [
        {
          "title": "Từ trường và cách biểu diễn",
          "topics": [
            {
              "slug": "tu-tinh",
              "title": "Từ tính",
              "question": "Vì sao nam châm có hai cực và tương tác từ gắn với điện tích chuyển động?",
              "source": "27.1"
            },
            {
              "slug": "tu-truong",
              "title": "Từ trường",
              "question": "Vận tốc và dấu điện tích quyết định lực từ như thế nào?",
              "source": "27.2"
            },
            {
              "slug": "duong-suc-tu-thong",
              "title": "Đường sức từ và từ thông",
              "question": "Bản đồ đường sức và từ thông cho biết những gì về từ trường?",
              "source": "27.3"
            }
          ]
        },
        {
          "title": "Chuyển động của hạt mang điện",
          "topics": [
            {
              "slug": "chuyen-dong-hat",
              "title": "Chuyển động trong từ trường",
              "question": "Khi nào hạt đi theo đường tròn hoặc đường xoắn ốc?",
              "source": "27.4"
            },
            {
              "slug": "ung-dung-hat",
              "title": "Ứng dụng chuyển động của hạt",
              "question": "Trường chéo nhau chọn vận tốc và phân biệt khối lượng hạt ra sao?",
              "source": "27.5"
            }
          ]
        },
        {
          "title": "Dòng điện, vòng dây và thiết bị",
          "topics": [
            {
              "slug": "luc-len-day",
              "title": "Lực từ lên dây dẫn",
              "question": "Lực vi mô lên hạt tải trở thành lực lên cả dây như thế nào?",
              "source": "27.6"
            },
            {
              "slug": "vong-day-mo-men",
              "title": "Lực và mômen lên vòng dây",
              "question": "Vì sao tổng lực có thể bằng không nhưng vòng vẫn quay?",
              "source": "27.7"
            },
            {
              "slug": "dong-co-dien",
              "title": "Động cơ điện một chiều",
              "question": "Cổ góp và suất phản điện động quyết định chiều quay và công suất ra sao?",
              "source": "27.8"
            },
            {
              "slug": "hall",
              "title": "Hiệu ứng Hall",
              "question": "Điện áp ngang giúp suy dấu và mật độ hạt tải như thế nào?",
              "source": "27.9"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "08-nguon-tu-truong",
      "title": "Nguồn của từ trường",
      "prerequisites": [
        "vector",
        "tich-co-huong",
        "dien-tich",
        "dong-dien",
        "dien-truong",
        "dinh-luat-gauss",
        "tu-truong",
        "luc-tu-tren-dien-tich",
        "momen-tu",
        "momen-dong-luong",
        "tich-phan"
      ],
      "supportingConcepts": [
        "dinh-luat-biot-savart",
        "dinh-luat-ampere",
        "do-tu-hoa",
        "do-tu-tham",
        "do-cam-tu",
        "thuan-tu",
        "nghich-tu",
        "sat-tu",
        "bao-hoa-tu",
        "tu-tre",
        "tu-hoa-du",
        "luc-khu-tu",
        "hien-tuong-curie",
        "ong-day-dien",
        "ong-day-hinh-xuyen"
      ],
      "status": "ready",
      "number": 8,
      "sourceChapter": 28,
      "topicGroups": [
        {
          "title": "Từ trường do dòng điện tạo ra",
          "topics": [
            {
              "slug": "dien-tich-chuyen-dong-tu-truong",
              "title": "Từ trường do điện tích chuyển động",
              "question": "Một điện tích chuyển động tạo từ trường phụ thuộc vận tốc và vị trí ra sao?",
              "source": "28.1"
            },
            {
              "slug": "tu-truong-biot-savart",
              "title": "Định luật Biot–Savart",
              "question": "Mỗi phần tử dòng điện đóng góp vào từ trường tại điểm khảo sát như thế nào?",
              "source": "28.2"
            },
            {
              "slug": "tu-truong-day-thang",
              "title": "Từ trường của dây dẫn thẳng",
              "question": "Đối xứng trụ cho biết độ lớn và chiều trường quanh dây ra sao?",
              "source": "28.3"
            },
            {
              "slug": "luc-tu-hai-day",
              "title": "Lực giữa hai dây dẫn song song",
              "question": "Vì sao hai dòng cùng chiều hút nhau còn hai dòng ngược chiều đẩy nhau?",
              "source": "28.4"
            },
            {
              "slug": "tu-truong-vong-day",
              "title": "Từ trường trên trục vòng dây",
              "question": "Các phần tử đối xứng của vòng dây tổng hợp trường trên trục thế nào?",
              "source": "28.5"
            },
            {
              "slug": "dinh-luat-ampere",
              "title": "Định luật Ampere",
              "question": "Tích phân đường kín liên hệ với dòng điện bao quanh như thế nào?",
              "source": "28.6"
            },
            {
              "slug": "ung-dung-ampere",
              "title": "Ứng dụng định luật Ampere",
              "question": "Đối xứng nào cho phép tìm trường trong dây trụ, ống dây và xuyến?",
              "source": "28.7"
            },
            {
              "slug": "vat-lieu-tu",
              "title": "Vật liệu từ",
              "question": "Từ hóa, độ cảm từ và từ trễ mô tả phản ứng của vật liệu ra sao?",
              "source": "28.8"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "09-cam-ung-dien-tu",
      "title": "Cảm ứng điện từ",
      "prerequisites": [
        "vector",
        "tich-vo-huong",
        "tich-co-huong",
        "dao-ham",
        "tich-phan",
        "dien-truong-bao-toan",
        "suat-dien-dong",
        "luc-tu-tren-dien-tich",
        "momen-tu",
        "dien-dung",
        "ong-day-dien",
        "dinh-luat-ampere"
      ],
      "supportingConcepts": [
        "tu-thong",
        "cam-ung-dien-tu",
        "dinh-luat-faraday",
        "dinh-luat-lenz",
        "suat-dien-dong-chuyen-dong",
        "dien-truong-cam-ung",
        "dong-dien-foucault",
        "dong-dien-dich",
        "phuong-trinh-maxwell",
        "sieu-dan",
        "nhiet-do-toi-han-sieu-dan",
        "tu-truong-toi-han-sieu-dan",
        "hieu-ung-meissner",
        "sieu-dan-loai-i",
        "sieu-dan-loai-ii",
        "dao-dong-tat-dan"
      ],
      "status": "ready",
      "number": 9,
      "sourceChapter": 29,
      "topicGroups": [
        {
          "title": "Cảm ứng, trường biến thiên và vật liệu siêu dẫn",
          "topics": [
            {
              "slug": "thi-nghiem-cam-ung",
              "title": "Thí nghiệm cảm ứng",
              "question": "Những thay đổi nào làm cuộn dây xuất hiện dòng điện?",
              "source": "29.1"
            },
            {
              "slug": "dinh-luat-faraday",
              "title": "Định luật Faraday",
              "question": "Tốc độ biến thiên từ thông quyết định suất điện động ra sao?",
              "source": "29.2"
            },
            {
              "slug": "dinh-luat-lenz",
              "title": "Định luật Lenz",
              "question": "Dòng cảm ứng chống lại sự thay đổi nào?",
              "source": "29.3"
            },
            {
              "slug": "suat-dien-dong-chuyen-dong",
              "title": "Suất điện động do chuyển động",
              "question": "Lực từ phân bố lại điện tích trong vật dẫn chuyển động thế nào?",
              "source": "29.4"
            },
            {
              "slug": "dien-truong-cam-ung",
              "title": "Điện trường cảm ứng",
              "question": "Điều gì đẩy điện tích trong vòng dây đứng yên khi từ thông biến thiên?",
              "source": "29.5"
            },
            {
              "slug": "dong-dien-foucault",
              "title": "Dòng điện Fu-cô",
              "question": "Dòng điện khép kín trong khối kim loại tạo lực hãm và nhiệt thế nào?",
              "source": "29.6"
            },
            {
              "slug": "dong-dien-dich-maxwell",
              "title": "Dòng điện dịch và phương trình Maxwell",
              "question": "Điện trường biến thiên bổ sung nguồn từ trường như thế nào?",
              "source": "29.7"
            },
            {
              "slug": "sieu-dan",
              "title": "Siêu dẫn",
              "question": "Trạng thái không điện trở còn có những tính chất từ nào?",
              "source": "29.8"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "10-tu-cam",
      "title": "Điện cảm",
      "prerequisites": [
        "dao-ham",
        "tich-phan",
        "dao-dong-dieu-hoa",
        "dao-dong-tat-dan",
        "dien-dung",
        "mat-do-nang-luong-dien-truong",
        "quy-tac-kirchhoff",
        "ong-day-dien",
        "do-tu-tham",
        "dinh-luat-faraday",
        "dinh-luat-lenz",
        "dien-truong-bao-toan"
      ],
      "supportingConcepts": [
        "tu-thong-moc-vong",
        "ho-cam",
        "tu-cam",
        "cuon-cam",
        "nang-luong-tu-truong",
        "mat-do-nang-luong-tu-truong",
        "mach-rl",
        "hang-so-thoi-gian-rl",
        "mach-lc",
        "mach-rlc",
        "tat-dan-toi-han",
        "qua-tat-dan"
      ],
      "status": "ready",
      "number": 10,
      "sourceChapter": 30,
      "topicGroups": [
        {
          "title": "Điện cảm, năng lượng và quá trình chuyển tiếp",
          "topics": [
            {
              "slug": "ho-cam",
              "title": "Hỗ cảm",
              "question": "Dòng ở một cuộn tạo suất điện động trong cuộn khác như thế nào?",
              "source": "30.1"
            },
            {
              "slug": "tu-cam-cuon-cam",
              "title": "Tự cảm và cuộn cảm",
              "question": "Vì sao điện áp cuộn phụ thuộc tốc độ biến thiên dòng?",
              "source": "30.2"
            },
            {
              "slug": "nang-luong-tu-truong",
              "title": "Năng lượng từ trường",
              "question": "Công để thiết lập dòng được tích trữ ở đâu?",
              "source": "30.3"
            },
            {
              "slug": "mach-rl",
              "title": "Mạch RL",
              "question": "Dòng tăng và giảm theo quy luật nào khi chuyển công tắc?",
              "source": "30.4"
            },
            {
              "slug": "mach-lc",
              "title": "Mạch LC",
              "question": "Vì sao tụ và cuộn tạo dao động điện?",
              "source": "30.5"
            },
            {
              "slug": "mach-rlc",
              "title": "Mạch RLC nối tiếp",
              "question": "Điện trở quyết định dao động hay suy giảm không dao động ra sao?",
              "source": "30.6"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
        "slug": "11-dong-dien-xoay-chieu",
        "title": "Dòng điện xoay chiều",
        "prerequisites": [
          "dao-ham",
          "tich-phan",
          "dao-dong-dieu-hoa",
          "dien-tro",
          "dien-dung",
          "cuon-cam",
          "quy-tac-kirchhoff",
          "dinh-luat-faraday",
          "ho-cam",
          "dong-dien-dich",
          "dien-ke",
          "tu-tre"
        ],
        "supportingConcepts": [
          "dong-dien-xoay-chieu",
          "vector-pha",
          "gia-tri-hieu-dung",
          "cam-khang",
          "dung-khang",
          "tro-khang",
          "goc-pha-mach-dien",
          "he-so-cong-suat",
          "cong-huong-dien",
          "may-bien-ap"
        ],
        "status": "ready",
        "number": 11,
        "sourceChapter": 31,
        "topicGroups": [
          {
            "title": "Pha, đáp ứng và năng lượng của mạch xoay chiều",
            "topics": [
              {
                "slug": "gian-do-pha-hieu-dung",
                "title": "Giản đồ pha và giá trị hiệu dụng",
                "question": "Một vector quay biểu diễn dòng hình sin và giá trị hiệu dụng ra sao?",
                "source": "31.1"
              },
              {
                "slug": "dien-tro-dien-khang",
                "title": "Điện trở và điện kháng",
                "question": "Vì sao điện trở, cuộn cảm và tụ có quan hệ pha khác nhau?",
                "source": "31.2"
              },
              {
                "slug": "mach-rlc-noi-tiep",
                "title": "Mạch RLC nối tiếp có nguồn",
                "question": "Cộng các điện áp lệch pha để tìm trở kháng như thế nào?",
                "source": "31.3"
              },
              {
                "slug": "cong-suat-xoay-chieu",
                "title": "Công suất và hệ số công suất",
                "question": "Điện áp và dòng lệch pha làm công suất trung bình thay đổi ra sao?",
                "source": "31.4"
              },
              {
                "slug": "cong-huong",
                "title": "Cộng hưởng trong mạch xoay chiều",
                "question": "Tần số nào cho dòng lớn nhất và điện trở làm đổi đỉnh thế nào?",
                "source": "31.5"
              },
              {
                "slug": "may-bien-ap",
                "title": "Máy biến áp",
                "question": "Hai cuộn ghép từ đổi điện áp, dòng và điện trở nhìn từ nguồn ra sao?",
                "source": "31.6"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
        "slug": "12-song-dien-tu",
        "title": "Sóng điện từ",
        "prerequisites": [
          "dao-ham",
          "dao-ham-rieng",
          "tich-phan",
          "tich-co-huong",
          "dao-dong-dieu-hoa",
          "song",
          "pha-song",
          "dong-luong-vat-ly",
          "cong-nang-luong",
          "dien-truong",
          "tu-truong",
          "thong-luong",
          "dinh-luat-faraday",
          "dong-dien-dich"
        ],
        "supportingConcepts": [
          "song-dien-tu",
          "song-dien-tu-phang",
          "phan-cuc-thang",
          "vector-poynting",
          "cuong-do-buc-xa",
          "ap-suat-buc-xa",
          "dong-luong-dien-tu",
          "song-dung-dien-tu",
          "hoc-cong-huong-dien-tu",
          "pho-dien-tu"
        ],
        "status": "ready",
        "number": 12,
        "sourceChapter": 32,
        "topicGroups": [
          {
            "title": "Trường, năng lượng và sự phản xạ của sóng điện từ",
            "topics": [
              {
                "slug": "maxwell-song-dien-tu",
                "title": "Maxwell và nguồn sóng điện từ",
                "question": "Vì sao hai trường biến thiên có thể truyền trong chân không?",
                "source": "32.1"
              },
              {
                "slug": "song-phang-van-toc-anh-sang",
                "title": "Sóng phẳng và tốc độ ánh sáng",
                "question": "Các phương trình trường quyết định tốc độ và hướng truyền như thế nào?",
                "source": "32.2"
              },
              {
                "slug": "song-hinh-sin",
                "title": "Sóng hình sin và môi trường vật chất",
                "question": "Biên độ, pha, bước sóng và vật liệu liên hệ ra sao?",
                "source": "32.3"
              },
              {
                "slug": "nang-luong-dong-luong",
                "title": "Năng lượng, động lượng và áp suất bức xạ",
                "question": "Sóng mang công suất và tạo lực lên vật nhận như thế nào?",
                "source": "32.4"
              },
              {
                "slug": "song-dung-dien-tu",
                "title": "Sóng đứng và hốc cộng hưởng",
                "question": "Phản xạ tạo nút, bụng và các tần số riêng nào?",
                "source": "32.5"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
        "slug": "13-truyen-anh-sang",
        "title": "Bản chất và sự truyền ánh sáng",
        "prerequisites": [
          "song",
          "pha-song",
          "vector",
          "dao-ham",
          "dao-dong-dieu-hoa",
          "song-dien-tu",
          "cuong-do-buc-xa"
        ],
        "supportingConcepts": [
          "chiet-suat",
          "dinh-luat-snell",
          "phan-cuc-thang",
          "mat-song",
          "tia-sang",
          "phan-xa-guong",
          "phan-xa-toan-phan",
          "tan-sac",
          "anh-sang-khong-phan-cuc",
          "dinh-luat-malus",
          "goc-brewster",
          "phan-cuc-tron",
          "phan-cuc-elip",
          "luong-chiet",
          "ban-phan-tu-buoc-song",
          "tan-xa-rayleigh",
          "nguyen-ly-huygens"
        ],
        "status": "ready",
        "number": 13,
        "sourceChapter": 33,
        "topicGroups": [
          {
            "title": "Bản chất, đường truyền và trạng thái phân cực của ánh sáng",
            "topics": [
              {
                "slug": "ban-chat-anh-sang",
                "title": "Bản chất ánh sáng, mặt sóng và tia",
                "question": "Khi nào dùng mô hình sóng, hạt hay tia để mô tả ánh sáng?",
                "source": "33.1"
              },
              {
                "slug": "phan-xa-khuc-xa",
                "title": "Phản xạ, khúc xạ và bước sóng",
                "question": "Tia đổi hướng như thế nào khi gặp một mặt phân cách?",
                "source": "33.2"
              },
              {
                "slug": "phan-xa-toan-phan",
                "title": "Phản xạ toàn phần và dẫn sáng",
                "question": "Điều kiện nào giữ ánh sáng trong lăng kính hoặc sợi quang?",
                "source": "33.3"
              },
              {
                "slug": "tan-sac",
                "title": "Tán sắc, lăng kính và cầu vồng",
                "question": "Vì sao các màu đi theo những hướng khác nhau?",
                "source": "33.4"
              },
              {
                "slug": "phan-cuc",
                "title": "Phân cực và tương tác với vật liệu",
                "question": "Phương dao động điện trường quyết định ánh sáng truyền qua và phản xạ ra sao?",
                "source": "33.5"
              },
              {
                "slug": "tan-xa-anh-sang",
                "title": "Tán xạ và màu sắc bầu trời",
                "question": "Vì sao trời xanh, mây trắng và Mặt Trời đỏ lúc gần chân trời?",
                "source": "33.6"
              },
              {
                "slug": "nguyen-ly-huygens",
                "title": "Nguyên lý Huygens",
                "question": "Có thể suy đường tia từ sự tiến của mặt sóng như thế nào?",
                "source": "33.7"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
        "slug": "14-quang-hinh-hoc",
        "title": "Quang hình học",
        "prerequisites": [
          "tia-sang",
          "phan-xa-guong",
          "chiet-suat",
          "dinh-luat-snell",
          "don-vi"
        ],
        "supportingConcepts": [
          "vat-anh-quang-hoc",
          "quy-uoc-dau-quang-hoc",
          "tia-can-truc",
          "guong-cau",
          "tieu-diem-quang-hoc",
          "phong-dai-ngang",
          "khuc-xa-mat-cau",
          "thau-kinh-mong",
          "cong-thuc-che-tao-thau-kinh",
          "quang-sai-cau",
          "chi-so-f",
          "do-tu-thau-kinh",
          "dieu-tiet-mat",
          "tat-khuc-xa",
          "boi-giac-goc",
          "kinh-hien-vi",
          "kinh-thien-van"
        ],
        "status": "ready",
        "number": 14,
        "sourceChapter": 34,
        "topicGroups": [
          {
            "title": "Tạo ảnh và dụng cụ quang học",
            "topics": [
              {
                "slug": "guong-phang",
                "title": "Vật, ảnh và gương phẳng",
                "question": "Ảnh nằm ở đâu khi các tia phản xạ chỉ có vẻ xuất phát từ một điểm?",
                "source": "34.1"
              },
              {
                "slug": "guong-cau",
                "title": "Gương cầu và phép dựng ảnh",
                "question": "Độ cong của gương quyết định vị trí, chiều và kích thước ảnh như thế nào?",
                "source": "34.2"
              },
              {
                "slug": "khuc-xa-mat-cau",
                "title": "Khúc xạ tại mặt cầu và độ sâu biểu kiến",
                "question": "Vì sao một mặt khúc xạ có thể hội tụ tia hoặc làm vật có vẻ ở gần hơn?",
                "source": "34.3"
              },
              {
                "slug": "thau-kinh-mong",
                "title": "Thấu kính mỏng và hệ nhiều kính",
                "question": "Hai mặt khúc xạ phối hợp tạo ảnh ra sao, và khi nào ảnh trước trở thành vật ảo?",
                "source": "34.4"
              },
              {
                "slug": "may-anh",
                "title": "Máy ảnh, khẩu độ và ống kính zoom",
                "question": "Tiêu cự, khẩu độ và màn trập điều khiển khung hình cùng độ phơi sáng như thế nào?",
                "source": "34.5"
              },
              {
                "slug": "mat",
                "title": "Mắt, điều tiết và kính hiệu chỉnh",
                "question": "Vì sao ảnh phải nằm trên võng mạc và kính bổ trợ tạo ảnh ở đâu?",
                "source": "34.6"
              },
              {
                "slug": "kinh-lup",
                "title": "Kính lúp và bội giác góc",
                "question": "Ảnh ở vô cực vẫn có góc trông hữu hạn như thế nào?",
                "source": "34.7"
              },
              {
                "slug": "kinh-hien-vi-thien-van",
                "title": "Kính hiển vi và kính thiên văn",
                "question": "Vì sao vật kính hiển vi cần tiêu cự ngắn, còn vật kính thiên văn cần tiêu cự dài?",
                "source": "34.8"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
        "slug": "15-giao-thoa",
        "title": "Giao thoa",
        "prerequisites": [
          "song",
          "pha-song",
          "vector-pha",
          "chiet-suat",
          "phan-cuc-thang",
          "cuong-do-buc-xa",
          "don-vi"
        ],
        "supportingConcepts": [
          "nguon-ket-hop",
          "hieu-duong-di",
          "giao-thoa-hai-khe",
          "van-giao-thoa",
          "doi-pha-phan-xa",
          "quang-trinh",
          "giao-thoa-mang-mong",
          "nem-khong-khi",
          "van-tron-newton",
          "lop-phu-chong-phan-xa",
          "giao-thoa-ke-michelson"
        ],
        "status": "ready",
        "number": 15,
        "sourceChapter": 35,
        "topicGroups": [
          {
            "title": "Giao thoa từ nguồn kết hợp đến phép đo",
            "topics": [
              {
                "slug": "giao-thoa-nguon-ket-hop",
                "title": "Giao thoa và nguồn kết hợp",
                "question": "Vì sao cùng tần số chưa đủ để giữ một hệ vân ổn định?",
                "source": "35.1"
              },
              {
                "slug": "giao-thoa-hai-nguon",
                "title": "Giao thoa ánh sáng từ hai nguồn",
                "question": "Hiệu đường đi quyết định hướng sáng và tối như thế nào?",
                "source": "35.2"
              },
              {
                "slug": "cuong-do-giao-thoa",
                "title": "Cường độ trong hệ vân",
                "question": "Cộng điện trường như thế nào để tính cường độ ở mọi điểm?",
                "source": "35.3"
              },
              {
                "slug": "giao-thoa-mang-mong",
                "title": "Giao thoa ở màng mỏng",
                "question": "Dấu pha phản xạ và đường đi trong màng phối hợp tạo màu ra sao?",
                "source": "35.4"
              },
              {
                "slug": "giao-thoa-ke-michelson",
                "title": "Giao thoa kế Michelson",
                "question": "Vì sao đếm vân có thể đo được dịch chuyển rất nhỏ?",
                "source": "35.5"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
        "slug": "16-nhieu-xa",
        "title": "Nhiễu xạ",
        "prerequisites": [
          "mat-song",
          "nguyen-ly-huygens",
          "nguon-ket-hop",
          "hieu-duong-di",
          "vector-pha",
          "thau-kinh-mong",
          "chiet-suat",
          "tan-sac"
        ],
        "supportingConcepts": [
          "nhieu-xa-fresnel",
          "nhieu-xa-fraunhofer",
          "nhieu-xa-khe-don",
          "ham-sinc-nhieu-xa",
          "bao-nhieu-xa",
          "bac-khuyet",
          "cach-tu-nhieu-xa",
          "nang-suat-phan-giai-pho",
          "dieu-kien-bragg",
          "dia-airy",
          "tieu-chuan-rayleigh",
          "anh-toan-ky"
        ],
        "status": "ready",
        "number": 16,
        "sourceChapter": 36,
        "topicGroups": [
          {
            "title": "Từ khẩu độ tới cấu trúc và hình ảnh",
            "topics": [
              {
                "slug": "nhieu-xa-fresnel-fraunhofer",
                "title": "Nhiễu xạ Fresnel và Fraunhofer",
                "question": "Khi nào cần xét độ cong mặt sóng?",
                "source": "36.1"
              },
              {
                "slug": "nhieu-xa-mot-khe",
                "title": "Nhiễu xạ qua một khe",
                "question": "Vì sao một khe vẫn tạo được các vân tối?",
                "source": "36.2"
              },
              {
                "slug": "cuong-do-nhieu-xa-mot-khe",
                "title": "Cường độ nhiễu xạ một khe",
                "question": "Tổng các sóng từ toàn khe cho phân bố cường độ nào?",
                "source": "36.3"
              },
              {
                "slug": "nhieu-khe",
                "title": "Hệ nhiều khe",
                "question": "Bao nhiễu xạ và pha giữa các khe phối hợp thế nào?",
                "source": "36.4"
              },
              {
                "slug": "cach-tu-nhieu-xa",
                "title": "Cách tử nhiễu xạ",
                "question": "Vì sao nhiều khe giúp đo và phân giải bước sóng?",
                "source": "36.5"
              },
              {
                "slug": "nhieu-xa-tia-x",
                "title": "Nhiễu xạ tia X",
                "question": "Góc Bragg cho biết khoảng mặt mạng ra sao?",
                "source": "36.6"
              },
              {
                "slug": "khau-do-tron-phan-giai",
                "title": "Khẩu độ tròn và phân giải",
                "question": "Vì sao phóng to ảnh chưa chắc thấy thêm chi tiết?",
                "source": "36.7"
              },
              {
                "slug": "anh-toan-ky",
                "title": "Ảnh toàn ký",
                "question": "Ghi hệ vân như thế nào để tái tạo mặt sóng ba chiều?",
                "source": "36.8"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
        "slug": "17-thuyet-tuong-doi",
        "title": "Thuyết tương đối",
        "prerequisites": [
          "vector",
          "van-toc-vat-ly",
          "dong-luong-vat-ly",
          "cong-nang-luong",
          "song"
        ],
        "supportingConcepts": [
          "he-quy-chieu-quan-tinh",
          "su-kien-khong-thoi-gian",
          "dong-thoi-tuong-doi",
          "he-so-lorentz",
          "thoi-gian-rieng",
          "gian-thoi-gian",
          "do-dai-rieng",
          "co-chieu-dai-lorentz",
          "bien-doi-lorentz",
          "doppler-dien-tu",
          "dong-luong-tuong-doi",
          "nang-luong-nghi",
          "nguyen-ly-tuong-ung",
          "nguyen-ly-tuong-duong"
        ],
        "status": "ready",
        "number": 17,
        "sourceChapter": 37,
        "topicGroups": [
          {
            "title": "Không gian, thời gian và phép đo",
            "topics": [
              {
                "slug": "bat-bien-dinh-luat",
                "title": "Tính bất biến của định luật vật lý",
                "question": "Hai hệ quán tính có thể dùng những định luật khác nhau không?",
                "source": "37.1"
              },
              {
                "slug": "tinh-tuong-doi-dong-thoi",
                "title": "Tính tương đối của đồng thời",
                "question": "Vì sao hai sự kiện đồng thời trong một hệ lại không đồng thời trong hệ khác?",
                "source": "37.2"
              },
              {
                "slug": "gian-thoi-gian",
                "title": "Giãn thời gian và thời gian riêng",
                "question": "Đồng hồ chuyển động chạy chậm được xác định bằng phép đo nào?",
                "source": "37.3"
              },
              {
                "slug": "co-chieu-dai",
                "title": "Co chiều dài và hình dạng quan sát",
                "question": "Đo đồng thời hai đầu vật khác với chụp ảnh vật như thế nào?",
                "source": "37.4"
              },
              {
                "slug": "bien-doi-lorentz",
                "title": "Biến đổi Lorentz",
                "question": "Cùng một sự kiện và cùng một chuyển động có tọa độ nào trong hai hệ?",
                "source": "37.5"
              },
              {
                "slug": "doppler-dien-tu",
                "title": "Doppler của sóng điện từ",
                "question": "Tần số đổi thế nào trong khi tốc độ ánh sáng vẫn bằng c?",
                "source": "37.6"
              }
            ]
          },
          {
            "title": "Động lực học, năng lượng và hấp dẫn",
            "topics": [
              {
                "slug": "dong-luong-tuong-doi",
                "title": "Động lượng và lực tương đối tính",
                "question": "Vì sao lực dọc và lực ngang cho các hệ số gia tốc khác nhau?",
                "source": "37.7"
              },
              {
                "slug": "cong-nang-luong-tuong-doi",
                "title": "Công và năng lượng tương đối tính",
                "question": "Động năng, năng lượng nghỉ và năng lượng toàn phần liên hệ thế nào?",
                "source": "37.8"
              },
              {
                "slug": "newton-va-tuong-doi-rong",
                "title": "Cơ học Newton và thuyết tương đối rộng",
                "question": "Nguyên lý tương ứng và nguyên lý tương đương nói gì?",
                "source": "37.9"
              }
            ]
          }
        ],
        "hasChapterExercises": true
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
      "formula": "$$\n\\begin{aligned}\n&\\vec F_0 =q_0\\vec E,\\\\\n&\\vec E =\\frac{kq}{r^2}\\hat{\\mathbf r}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\vec E = \\vec E_1+\\vec E_2+\\cdots+\\vec E_n,\\\\\n&\\vec E = \\sum_{i=1}^{n}\\vec E_i.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&p =qd,\\\\\n&\\vec\\tau =\\vec p\\times\\vec E,\\\\\n&U =-\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\Phi_E = \\oint\\vec E\\cdot d\\vec A,\\\\\n&\\Phi_E = \\frac{Q_{\\mathrm{trong}}}{\\varepsilon_0}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&E_{\\mathrm{trong}} =\\frac{k|Q|r}{R^3},\\quad r<R,\\\\\n&E_{\\mathrm{ngoai}} =\\frac{k|Q|}{r^2},\\quad r>R.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&Q_{\\mathrm{trong}} =-q,\\\\\n&Q_{\\mathrm{ngoai}} =q_C+q,\\\\\n&E_\\perp =\\frac{\\sigma}{\\varepsilon_0}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&W_{a\\to b} =U_a-U_b,\\\\\n&K_a+U_a =K_b+U_b.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&U_{123} =\\frac{kq_1q_2}{r_{12}}\\\\\n&\\quad+\\frac{kq_1q_3}{r_{13}}\\\\\n&\\quad+\\frac{kq_2q_3}{r_{23}},\\\\\n&U =k\\sum_{i=1}^{n-1}\\sum_{j=i+1}^{n}\\frac{q_iq_j}{r_{ij}}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&V =\\frac{U}{q_0},\\\\\n&W_{a\\to b} =q_0(V_a-V_b),\\\\\n&1\\,\\mathrm V =1\\,\\mathrm{J/C}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&V =k\\int \\frac{dq}{r},\\\\\n&V_a-V_b =\\int_a^b\\vec E\\cdot d\\vec\\ell.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&E_x =-\\frac{\\partial V}{\\partial x},\\\\\n&E_y =-\\frac{\\partial V}{\\partial y},\\\\\n&E_z =-\\frac{\\partial V}{\\partial z},\\\\\n&\\vec E =-\\nabla V.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&C =\\frac{Q}{V_{ab}},\\\\\n&1\\,\\mathrm F =1\\,\\mathrm{C/V}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&V_{ab} =\\int_a^b\\vec E\\cdot d\\vec\\ell,\\\\\n&C_0 =\\frac{\\varepsilon_0 A}{d}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\frac1{C_s} =\\frac1{C_1}+\\frac1{C_2}+\\frac1{C_3},\\\\\n&C_p =C_1+C_2+C_3.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&U =\\frac{Q^2}{2C}=\\frac12 CV^2,\\\\\n&U =\\frac12 QV,\\\\\n&u_0 =\\frac12\\varepsilon_0 E^2.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\varepsilon =K\\varepsilon_0,\\\\\n&C =KC_0,\\\\\n&E =E_0/K,\\quad Q=Q_0.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\vec\\tau =\\vec p\\times\\vec E,\\\\\n&U_{\\mathrm{dipole}} =-\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&U_Q =U_0/K,\\quad Q=Q_0,\\\\\n&U_V =KU_0,\\quad V=V_0.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\oint_S K\\vec E\\cdot d\\vec A =\\frac{Q_{\\mathrm{free}}}{\\varepsilon_0},\\\\\n&u =\\frac12\\varepsilon E^2.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&I =\\frac{dQ}{dt},\\\\\n&1\\,\\mathrm A =1\\,\\mathrm{C/s}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&I =n|q|v_dA,\\\\\n&J =I/A,\\\\\n&\\vec J =nq\\vec v_d.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\rho =E/J,\\\\\n&\\sigma =1/\\rho,\\\\\n&\\rho(T) \\approx\\rho_0[1+\\alpha(T-T_0)].\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&R =\\frac{\\rho L}{A},\\\\\n&V =IR,\\\\\n&1\\,\\Omega =1\\,\\mathrm{V/A}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&V_{ab} =\\mathcal E-Ir,\\\\\n&I =\\frac{\\mathcal E}{R+r}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&I_{\\mathrm{oc}} =0,\\\\\n&V_{\\mathrm{oc}} =\\mathcal E,\\\\\n&I_{\\mathrm{sc}} =\\mathcal E/r,\\\\\n&V_{\\mathrm{sc}} =0.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&P =V_{ab}I,\\\\\n&P_R =I^2R,\\\\\n&P_{\\mathrm{ra}} =\\mathcal EI-I^2r.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n&\\vec v_d =\\frac{q\\tau}{m}\\vec E,\\\\\n&\\rho =\\frac{m}{ne^2\\tau}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Nối tiếp giữ dòng, song song giữ điện áp",
      "bullets": [
        "Nối tiếp không có nhánh rẽ giữa các điện trở nên các dòng bằng nhau.",
        "Song song nối vào cùng hai nút nên các hiệu điện thế bằng nhau.",
        "Điện trở tương đương giữ nguyên quan hệ dòng và điện áp nhìn từ hai đầu tổ hợp."
      ],
      "formula": "$$\n\\begin{aligned}\n&R_s =R_1+R_2,\\\\\n&\\frac1{R_p} =\\frac1{R_1}+\\frac1{R_2},\\\\\n&R_p =\\frac{R_1R_2}{R_1+R_2}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Quy tắc nút biểu diễn bảo toàn điện tích",
      "bullets": [
        "Ở trạng thái ổn định, điện tích không tích tụ liên tục tại nút.",
        "Dòng vào và dòng ra được gán dấu trái nhau trong phương trình nút.",
        "Kết quả dòng âm chỉ ra chiều thực ngược với chiều giả định."
      ],
      "formula": "$$\n\\begin{aligned}\n&I_1+I_2-I_3 =0,\\\\\n&I_1+I_2 =I_3.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Quy tắc vòng giữ nhất quán các biến thiên điện thế",
      "bullets": [
        "Đi dọc chiều dòng qua điện trở cho biến thiên −IR. Đi ngược chiều cho +IR.",
        "Qua nguồn từ cực âm đến cực dương cho +ℰ, ngược lại cho −ℰ.",
        "Chiều duyệt vòng do người giải chọn và không buộc trùng chiều dòng."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\Delta V_1+\\Delta V_2+\\Delta V_3 =0,\\\\\n&\\mathcal E-IR_1-IR_2 =0.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Dòng toàn thang quyết định điện trở bổ sung của dụng cụ",
      "bullets": [
        "Điện kế d’Arsonval có góc lệch tỉ lệ dòng trong miền hiệu chuẩn.",
        "Điện trở rẽ song song cho phép đo dòng lớn hơn dòng toàn thang của cuộn.",
        "Điện trở nối tiếp cho phép đo điện áp lớn hơn điện áp toàn thang của cuộn."
      ],
      "formula": "$$\n\\begin{aligned}\n&R_{\\mathrm{sh}} =\\frac{I_GR_G}{I-I_G},\\\\\n&R_s =\\frac{V}{I_G}-R_G.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Dụng cụ thực làm thay đổi đại lượng đang đo",
      "bullets": [
        "Ampe kế mắc nối tiếp và có điện trở nhỏ.",
        "Vôn kế mắc song song và có điện trở lớn.",
        "Chiết áp cân bằng đo suất điện động mà không lấy dòng từ nguồn cần đo ở điểm cân bằng."
      ],
      "formula": "$$\n\\begin{aligned}\n&R_A \\to0,\\\\\n&R_V \\to\\infty,\\\\\n&I_G = 0.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Nạp tụ qua điện trở là quá trình tiến dần đến cân bằng",
      "bullets": [
        "Tụ ban đầu chưa tích điện, nguồn và điện trở không đổi.",
        "Điện tích liên tục nên tụ chưa có điện áp ngay khi đóng công tắc.",
        "Khi thời gian đủ dài, dòng bằng không và điện áp tụ bằng suất điện động nguồn."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\tau =RC,\\\\\n&q(t) =C\\mathcal E(1-e^{-t/\\tau}),\\\\\n&i(t) =\\frac{\\mathcal E}{R}e^{-t/\\tau}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Phóng tụ chuyển năng lượng điện trường thành nhiệt",
      "bullets": [
        "Nguồn được ngắt, tụ có điện tích đầu Q₀ và phóng qua điện trở R.",
        "Dấu âm của dòng dùng chiều nạp làm chiều dương.",
        "Năng lượng giảm với thời gian đặc trưng RC/2, khác thời gian giảm điện tích RC."
      ],
      "formula": "$$\n\\begin{aligned}\n&q(t) =Q_0e^{-t/\\tau},\\\\\n&i(t) =-\\frac{Q_0}{\\tau}e^{-t/\\tau},\\\\\n&U(t) =\\frac{Q_0^2}{2C}e^{-2t/\\tau}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Mạch nhánh dùng chung điện áp và cộng dòng ở nguồn",
      "bullets": [
        "Các thiết bị được mắc song song để nhận cùng điện áp cấp trong mô hình.",
        "Cầu chì và bộ ngắt bảo vệ mạch trước dòng quá mức.",
        "Dây bảo vệ và thiết bị ngắt do chênh dòng có chức năng khác bảo vệ quá dòng."
      ],
      "formula": "$$\n\\begin{aligned}\n&I =I_1+I_2\\\\\n&\\quad+\\cdots+I_n,\\\\\n&P =VI,\\\\\n&1\\,\\mathrm{kW\\cdot h} =3.60\\,\\mathrm{MJ},\\\\\n&1\\,\\mathrm{MJ} =10^6\\,\\mathrm J.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Từ tính gắn với các điện tích chuyển động",
      "bullets": [
        "Hai cực cùng tên đẩy nhau, hai cực khác tên hút nhau.",
        "Chia một nam châm thành các phần tạo các nam châm nhỏ có hai cực.",
        "Dòng điện tạo từ trường, còn từ trường tác dụng lên điện tích đang chuyển động."
      ],
      "formula": "",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Lực từ có hướng vuông góc vận tốc và trường",
      "bullets": [
        "Dấu điện tích quyết định chiều lực so với tích có hướng.",
        "Vận tốc song song hoặc ngược song song trường cho lực bằng không.",
        "Lực từ không sinh công lên hạt vì vuông góc vận tốc tức thời."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\vec F =q\\vec v\\times\\vec B,\\\\\n&F =|q|vB\\sin\\phi,\\\\\n&\\vec F\\cdot\\vec v =0.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Đường sức từ biểu diễn trường và không chỉ hướng lực",
      "bullets": [
        "Tiếp tuyến của đường sức cho hướng từ trường tại điểm ấy.",
        "Mật độ đường trong cùng bản đồ biểu thị tương đối độ mạnh của trường.",
        "Đường sức không có nguồn hoặc điểm tận cùng. Các bản đồ nam châm khép qua cả bên trong nam châm."
      ],
      "formula": "$$\n\\oint\\vec B\\cdot d\\vec A=0\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Dấu từ thông phụ thuộc pháp tuyến đã chọn",
      "bullets": [
        "Thành phần vuông góc mặt đóng góp vào từ thông.",
        "Mặt kín dùng pháp tuyến hướng ra ngoài, mặt hở cần chọn một hướng nhất quán.",
        "Công thức BA cosφ dùng mặt phẳng và từ trường đều trên mặt."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\Phi_B =\\int\\vec B\\cdot d\\vec A,\\\\\n&\\Phi_B =BA\\cos\\phi,\\\\\n&1\\,\\mathrm{Wb} =1\\,\\mathrm{T\\cdot m^2}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Từ trường đều bẻ hướng hạt mà không đổi tốc độ",
      "bullets": [
        "Vận tốc vuông góc trường cho quỹ đạo tròn.",
        "Thành phần song song trường giữ không đổi và tạo bước xoắn.",
        "Các công thức dùng khối lượng không đổi trong mô hình không tương đối tính."
      ],
      "formula": "$$\n\\begin{aligned}\n&R =\\frac{mv_\\perp}{|q|B},\\\\\n&\\omega =\\frac{|q|B}{m},\\\\\n&T =\\frac{2\\pi m}{|q|B},\\\\\n&p =v_\\parallel T.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Bộ chọn vận tốc cân bằng hai lực",
      "bullets": [
        "Điện trường và từ trường được bố trí chéo nhau.",
        "Chỉ vận tốc có hướng và độ lớn phù hợp mới đi thẳng qua vùng chọn.",
        "Hạt nhanh hơn hoặc chậm hơn bị lệch theo các chiều khác nhau."
      ],
      "formula": "$$\n\\begin{aligned}\n&q\\vec E+q\\vec v\\times\\vec B =0,\\\\\n&v =E/B.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Khối phổ dùng bán kính quỹ đạo để phân biệt hạt",
      "bullets": [
        "Sau bộ chọn vận tốc, các hạt có cùng tốc độ.",
        "Trường phân tích bẻ quỹ đạo, bán kính phụ thuộc khối lượng trên độ lớn điện tích.",
        "Hai bán kính khác nhau đưa các đồng vị đến các vị trí khác nhau."
      ],
      "formula": "$$\n\\begin{aligned}\n&R =\\frac{mv}{|q|B'},\\\\\n&\\frac m{|q|} =\\frac{BB'R}{E}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Dòng điện trong dây chịu tổng lực của các hạt tải",
      "bullets": [
        "Vector chiều dài của dây hướng theo dòng quy ước.",
        "Dây thẳng trong trường đều có thể dùng lực của cả đoạn.",
        "Dây cong hoặc trường không đều cần cộng vector lực từng phần tử."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\vec F =I\\vec l\\times\\vec B,\\\\\n&d\\vec F =I\\,d\\vec l\\times\\vec B.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Vòng dây trong trường đều có thể chịu mômen",
      "bullets": [
        "Các lực trên vòng kín triệt tiêu tổng, nhưng các đường tác dụng khác nhau có thể tạo mômen.",
        "Quy tắc bàn tay phải cho hướng mômen từ theo chiều dòng.",
        "Cuộn N vòng cùng hình học và hướng làm mômen từ tăng N lần."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\vec\\mu =NI\\vec A,\\\\\n&\\vec\\tau =\\vec\\mu\\times\\vec B.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Năng lượng thấp nhất khi mômen từ cùng hướng trường",
      "bullets": [
        "Góc được tính giữa mômen từ và từ trường.",
        "Cùng chiều là cân bằng bền, ngược chiều là cân bằng không bền.",
        "Trong trường không đều, vòng còn có thể chịu lực tổng hướng về hoặc ra xa vùng trường mạnh."
      ],
      "formula": "$$\n\\begin{aligned}\n&U =-\\vec\\mu\\cdot\\vec B,\\\\\n&U =-\\mu B\\cos\\phi.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Động cơ chuyển điện năng thành cơ năng",
      "bullets": [
        "Cổ góp đổi chiều dòng trong vòng sau nửa vòng quay để duy trì chiều mômen.",
        "Suất phản điện động tăng theo tốc độ khi cấu hình và từ trường giữ nguyên.",
        "Rôto dừng làm suất phản điện động mất đi, nên dòng tăng mạnh trong mô hình nguồn và điện trở cố định."
      ],
      "formula": "$$\n\\begin{aligned}\n&V_{ab} =\\mathcal E+Ir,\\\\\n&P_{\\mathrm{in}} =V_{ab}I,\\\\\n&P_{\\mathrm{mech}} =\\mathcal EI,\\\\\n&P_r =I^2r.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "07-tu-truong-luc-tu",
      "title": "Hiệu ứng Hall tách điện tích theo phương ngang",
      "bullets": [
        "Lực từ dồn hạt tải về một mép và tạo điện trường ngang.",
        "Ở cân bằng, lực điện ngang chống lại lực từ.",
        "Cực tính Hall cho dấu hạt tải, còn độ lớn giúp suy mật độ trong mô hình thích hợp."
      ],
      "formula": "$$\n\\begin{aligned}\n&E_z =-v_xB_y,\\\\\n&J_x =nqv_x,\\\\\n&nq =-\\frac{J_xB_y}{E_z}.\n\\end{aligned}\n$$",
      "example": ""
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Điện tích chuyển động tạo từ trường",
      "bullets": [
        "Từ trường tại điểm khảo sát phụ thuộc vị trí tương đối đến điện tích.",
        "Biểu thức dùng điện tích chuyển động đều với tốc độ nhỏ so với tốc độ ánh sáng.",
        "Chiều vuông góc với vận tốc và phương nối đến điểm."
      ],
      "formula": "$$\n\\vec B=\\frac{\\mu_0}{4\\pi}\\frac{q\\vec v\\times\\hat r}{r^2}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Biot–Savart cộng trường của các phần tử dòng",
      "bullets": [
        "Mỗi phần tử dòng đóng góp một vector từ trường tại điểm khảo sát.",
        "Độ lớn giảm theo bình phương khoảng cách và phụ thuộc góc giữa phần tử dòng với phương nối đến điểm.",
        "Chiều xác định bằng tích có hướng theo quy tắc bàn tay phải."
      ],
      "formula": "$$\nd\\vec B=\\frac{\\mu_0}{4\\pi}\\frac{I\\,d\\vec l\\times\\hat r}{r^2}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Dây thẳng dài có trường giảm theo khoảng cách",
      "bullets": [
        "Đối xứng trụ làm đường sức là các đường tròn đồng tâm.",
        "Chiều trường xác định bởi chiều dòng điện.",
        "Kết quả áp dụng cho dây thẳng đủ dài so với khoảng cách đang xét."
      ],
      "formula": "$$\nB=\\frac{\\mu_0 I}{2\\pi r}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Hai dây song song hút hoặc đẩy tùy chiều dòng",
      "bullets": [
        "Mỗi dây nằm trong trường do dây kia tạo ra.",
        "Dòng cùng chiều gây lực hút, dòng ngược chiều gây lực đẩy.",
        "Lực trên một đơn vị chiều dài tỉ lệ tích hai dòng và nghịch với khoảng cách."
      ],
      "formula": "$$\n\\frac{F}{L}=\\frac{\\mu_0 I_1 I_2}{2\\pi d}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Trường trên trục vòng dây có hai thành phần đối xứng",
      "bullets": [
        "Các thành phần ngang triệt tiêu từng cặp.",
        "Các thành phần dọc trục cùng chiều và cộng lại.",
        "Tại tâm một vòng bán kính a, biểu thức rút gọn tương ứng."
      ],
      "formula": "$$\nB_x=\\frac{\\mu_0 I a^2}{2(a^2+x^2)^{3/2}}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Đoạn dây hữu hạn cho trường theo hai góc đầu mút",
      "bullets": [
        "Biot–Savart tích phân dọc đoạn dây thẳng hữu hạn.",
        "Các góc được đo từ phương vuông góc với dây qua điểm quan sát.",
        "Giới hạn dây rất dài khôi phục biểu thức dây thẳng vô hạn."
      ],
      "formula": "$$\nB=\\frac{\\mu_0 I}{4\\pi a}(\\sin\\theta_1+\\sin\\theta_2)\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Định luật Ampere tính tích phân theo dòng bao",
      "bullets": [
        "Dòng xuyên qua mặt được giới hạn bởi đường kín được cộng đại số.",
        "Chiều dương gắn với chiều đi trên đường bằng quy tắc bàn tay phải.",
        "Định luật dạng này dùng cho từ tĩnh, không bao gồm số hạng điện trường biến thiên."
      ],
      "formula": "$$\n\\oint\\vec B\\cdot d\\vec l=\\mu_0 I_{\\mathrm{encl}}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Dây trụ có dòng đều cho trường tuyến tính bên trong",
      "bullets": [
        "Bên trong, dòng bao tỉ lệ diện tích tiết diện được bao.",
        "Bên ngoài, đường tích phân bao toàn bộ dòng.",
        "Độ lớn trường liên tục tại mặt trụ trong mô hình phân bố đều."
      ],
      "formula": "$$\n\\begin{aligned}\n&B(r) = \\frac{\\mu_0 I r}{2\\pi R^2},\\quad r<R\\\\\n&B(r) = \\frac{\\mu_0 I}{2\\pi r},\\quad r\\ge R.\n\\end{aligned}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Ống dây dài và xuyến tập trung trường nhờ đối xứng",
      "bullets": [
        "Ở vùng giữa ống dây dài, trường gần đều và bên ngoài nhỏ.",
        "Trong lõi xuyến, trường phụ thuộc bán kính tính từ trục xuyến.",
        "Các kết quả là gần đúng hình học và giả thiết môi trường không từ tính."
      ],
      "formula": "$$\n\\begin{aligned}\n&B_{\\mathrm{solenoid}} \\approx \\mu_0 nI\\\\\n&B_{\\mathrm{toroid}}(r) = \\frac{\\mu_0 NI}{2\\pi r}.\n\\end{aligned}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Độ từ hóa bổ sung vào trường do dòng ngoài",
      "bullets": [
        "Độ từ hóa là mômen từ trên một đơn vị thể tích.",
        "Trong vật liệu tuyến tính đẳng hướng, độ từ thẩm tương đối liên hệ với độ cảm từ.",
        "Không dùng quan hệ tuyến tính như hằng số vật liệu sắt từ khi vật liệu bão hòa hoặc có từ trễ."
      ],
      "formula": "$$\n\\begin{aligned}\n&\\vec B = \\vec B_0+\\mu_0\\vec M\\\\\n&\\mu = K_m\\mu_0\\\\\n&\\chi_m = K_m-1.\n\\end{aligned}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Vật liệu sắt từ có bão hòa và từ trễ",
      "bullets": [
        "Các miền từ có thể đổi kích thước và hướng khi tăng trường ngoài.",
        "Sau khi bỏ trường, từ hóa dư có thể còn lại.",
        "Vòng trễ phụ thuộc lịch sử từ hóa nên không mô tả bằng một độ từ thẩm cố định."
      ],
      "formula": ""
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Biến thiên từ thông là điều kiện gây cảm ứng",
      "bullets": [
        "Nam châm đứng yên gần cuộn dây không gây dòng cảm ứng ổn định.",
        "Chuyển động tương đối, biến đổi dòng nguồn hoặc đổi hình dạng cuộn đều có thể làm từ thông biến thiên.",
        "Suất điện động phụ thuộc tốc độ thay đổi, không phụ thuộc riêng giá trị từ thông."
      ],
      "formula": "$$\n\\Phi_B=\\int_S\\vec B\\cdot d\\vec A\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Faraday gắn suất điện động với đạo hàm từ thông",
      "bullets": [
        "Chiều dương quanh vòng được gắn với pháp tuyến bằng quy tắc bàn tay phải.",
        "N vòng nối tiếp có cùng từ thông cho suất điện động gấp N lần.",
        "Mạch hở có thể có suất điện động dù không có dòng vòng."
      ],
      "formula": "$$\n\\mathcal E=-N\\frac{d\\Phi_B}{dt}\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Dấu của Faraday phải đi cùng pháp tuyến đã chọn",
      "bullets": [
        "Từ thông dương tăng cho suất điện động âm.",
        "Từ thông dương giảm cho suất điện động dương.",
        "Chỉ sau khi chọn pháp tuyến mới đổi dấu thành chiều chạy quanh vòng."
      ],
      "formula": "$$\n\\Phi_B=BA\\cos\\phi\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Cuộn quay tạo suất điện động hình sin",
      "bullets": [
        "Pháp tuyến quay đều làm góc với trường thay đổi tuyến tính theo thời gian.",
        "Suất điện động cực đại khi từ thông đi qua không.",
        "Cổ góp đổi nối điện mỗi nửa vòng để đầu ra giữ cùng dấu."
      ],
      "formula": "$$\n\\begin{aligned}&\\Phi_B=BA\\cos\\omega t\\\\&\\mathcal E=N\\omega BA\\sin\\omega t.\\end{aligned}\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Lenz chống biến thiên từ thông",
      "bullets": [
        "Trường ngoài tăng thì dòng cảm ứng tạo trường ngược chiều trong vùng xét.",
        "Trường ngoài giảm thì dòng cảm ứng có thể tạo trường cùng chiều.",
        "Lực từ cản chuyển động sinh dòng, phù hợp bảo toàn năng lượng."
      ],
      "formula": ""
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Thanh chuyển động tách điện tích bằng lực từ",
      "bullets": [
        "Điện tích dương chịu lực theo tích có hướng của vận tốc với từ trường.",
        "Trong thanh cô lập, điện trường tăng đến khi cân bằng lực từ.",
        "Công thức tích vBL cần thanh, vận tốc và trường vuông góc từng đôi."
      ],
      "formula": "$$\n\\begin{aligned}&\\vec E=-\\vec v\\times\\vec B\\\\&|\\mathcal E|=vBL.\\end{aligned}\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Suất điện động chuyển động cần tích phân theo từng phần tử",
      "bullets": [
        "Vận tốc và trường được lấy tại mỗi phần tử của vật dẫn.",
        "Biểu thức này mô tả phần suất điện động do vật dẫn chuyển động.",
        "Dây đứng yên trong từ trường biến thiên cần xét điện trường cảm ứng."
      ],
      "formula": "$$\n\\mathcal E=\\oint(\\vec v\\times\\vec B)\\cdot d\\vec\\ell\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Điện trường cảm ứng có tuần hoàn khác không",
      "bullets": [
        "Đường tích phân được giữ cố định trong dạng Faraday cho điện trường.",
        "Điện trường này không bảo toàn và tồn tại cả khi không có dây dẫn.",
        "Đối xứng trụ làm điện trường tiếp tuyến với các đường tròn đồng tâm."
      ],
      "formula": "$$\n\\oint\\vec E\\cdot d\\vec\\ell=-\\frac{d\\Phi_B}{dt}\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Dòng Fu-cô có thể hãm, nung nóng và tạo tín hiệu dò",
      "bullets": [
        "Các đường dòng khép kín trong chính khối vật dẫn.",
        "Lực hãm chuyển cơ năng thành nhiệt.",
        "Dòng Fu-cô trong lõi biến áp gây tổn hao cần giảm bằng cấu tạo lõi."
      ],
      "formula": ""
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Dòng điện dịch làm Ampere nhất quán khi nạp tụ",
      "bullets": [
        "Hai mặt cùng đường biên phải cho cùng tích phân từ trường.",
        "Dòng dẫn trong dây bằng dòng dịch tổng trong khe của tụ lý tưởng đang nạp.",
        "Dòng dịch không đồng nhất với dòng dẫn xuyên điện môi."
      ],
      "formula": "$$\n\\begin{aligned}&i_D=\\varepsilon\\frac{d\\Phi_E}{dt}\\\\&\\oint\\vec B\\cdot d\\vec\\ell\\\\&\\quad=\\mu_0(i_C+i_D)_{\\mathrm{encl}}.\\end{aligned}\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Maxwell liên hệ điện trường, từ trường và nguồn",
      "bullets": [
        "Hai định luật Gauss liên hệ thông lượng qua mặt kín với các nguồn.",
        "Faraday và Ampere–Maxwell liên hệ tuần hoàn với các trường biến thiên.",
        "Kết hợp lực Lorentz cho biết tác dụng của trường lên điện tích."
      ],
      "formula": "$$\n\\vec F=q(\\vec E+\\vec v\\times\\vec B)\n$$"
    },
    {
      "note": "09-cam-ung-dien-tu",
      "title": "Siêu dẫn bao gồm cả điện trở bằng không và hiệu ứng Meissner",
      "bullets": [
        "Chuyển pha cần nhiệt độ và trường ngoài phù hợp.",
        "Meissner đẩy từ thông khỏi khối vật liệu trong trạng thái được xét.",
        "Loại II có hai trường tới hạn, với miền hỗn hợp giữa hai ngưỡng."
      ],
      "formula": "$$\nB_{c1}<B_0<B_{c2}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Hỗ cảm liên hệ hai mạch qua từ thông",
      "bullets": [
        "Dòng biến thiên ở cuộn nguồn làm từ thông qua cuộn nhận thay đổi.",
        "Từ thông trong định nghĩa là trung bình một vòng, còn từ thông móc vòng có tính số vòng.",
        "Hỗ cảm không đổi cần hình học cố định và môi trường từ tuyến tính."
      ],
      "formula": "$$\n\\begin{aligned}&N_2\\Phi_{B2}=Mi_1\\\\&\\mathcal E_2=-M\\frac{di_1}{dt}.\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Đổi vai hai cuộn vẫn cho cùng hỗ cảm",
      "bullets": [
        "Trong mô hình môi trường từ tuyến tính thuận nghịch, M12 bằng M21.",
        "Từ thông một vòng ở hai cuộn không nhất thiết bằng nhau.",
        "Dòng không đổi không tạo suất điện động hỗ cảm trong cấu hình cố định."
      ],
      "formula": "$$\n\\begin{aligned}&M=\\frac{N_2\\Phi_{B2}}{i_1}\\\\&\\quad=\\frac{N_1\\Phi_{B1}}{i_2}.\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Tự cảm chống sự thay đổi dòng",
      "bullets": [
        "Mạch mang dòng biến thiên tạo suất điện động qua biến thiên từ thông của chính nó.",
        "Dấu Lenz chống biến thiên dòng, không nhất thiết chống chiều dòng.",
        "Hệ số L là hằng trong mô hình cuộn tuyến tính, hình học cố định."
      ],
      "formula": "$$\n\\begin{aligned}&L=\\frac{N\\Phi_B}{i}\\\\&\\mathcal E_L=-L\\frac{di}{dt}.\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Dấu điện áp cuộn phải đi với chiều dòng",
      "bullets": [
        "Điện áp thụ động là điện thế đầu dòng đi vào trừ điện thế đầu dòng đi ra.",
        "Dòng dương tăng làm cuộn nhận năng lượng, còn dòng dương giảm làm cuộn nhả năng lượng.",
        "Với điện áp hữu hạn và L khác không, dòng cuộn liên tục khi chuyển mạch."
      ],
      "formula": "$$\nv_L=L\\frac{di}{dt}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Năng lượng cuộn nằm trong từ trường",
      "bullets": [
        "Tích phân công suất nạp cuộn cho năng lượng tỷ lệ bình phương dòng.",
        "Công thức mật độ trong vật liệu cần độ từ thẩm không đổi.",
        "Dòng đổi dấu nhưng giữ độ lớn không làm năng lượng từ trường đổi."
      ],
      "formula": "$$\n\\begin{aligned}&U_B=\\frac12Li^2\\\\&u_B=\\frac{B^2}{2\\mu}.\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Dòng RL tăng về giá trị do điện trở quyết định",
      "bullets": [
        "Cuộn ban đầu không dòng nhận toàn bộ điện áp nguồn ngay sau đóng.",
        "Hằng số thời gian quyết định tốc độ tăng, còn dòng cuối không phụ thuộc L.",
        "Sau một hằng số thời gian, dòng đạt khoảng 63,2% giá trị cuối."
      ],
      "formula": "$$\n\\begin{aligned}&\\tau=\\frac LR\\\\&I_\\infty=\\frac{\\mathcal E}{R}\\\\&i=I_\\infty(1-e^{-t/\\tau}).\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Tách nguồn làm dòng giảm liên tục",
      "bullets": [
        "Dòng ngay sau chuyển bằng dòng ngay trước chuyển.",
        "Cuộn cấp năng lượng từ trường cho điện trở trong vòng kín.",
        "Năng lượng giảm với hệ số mũ gấp đôi hệ số của dòng."
      ],
      "formula": "$$\n\\begin{aligned}&i=I_0e^{-t/\\tau}\\\\&U_B=U_0e^{-2t/\\tau}.\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "LC trao đổi năng lượng giữa tụ và cuộn",
      "bullets": [
        "Dòng không dừng khi tụ vừa hết điện tích, nên tụ tiếp tục được nạp với cực tính ngược.",
        "Trong mạch lý tưởng, tổng năng lượng không đổi.",
        "Quy ước i bằng đạo hàm q đòi hỏi dòng dương đi vào bản có điện tích q."
      ],
      "formula": "$$\n\\begin{aligned}&Lq''+\\frac qC=0\\\\&\\omega_0=\\frac1{\\sqrt{LC}}.\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Dòng và điện tích LC lệch pha một phần tư chu kỳ",
      "bullets": [
        "Biên độ và pha được xác định bởi điện tích và dòng ban đầu.",
        "Tại cực đại điện tích, dòng bằng không. Khi điện tích bằng không, độ lớn dòng cực đại.",
        "Điện tích âm cho biết bản tụ đã chọn có cực tính ngược với ban đầu."
      ],
      "formula": "$$\n\\begin{aligned}&q=Q\\cos(\\omega_0t+\\phi)\\\\&i=-\\omega_0Q\\sin(\\omega_0t+\\phi).\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "RLC cần đồng thời xét pha và suy giảm biên độ",
      "bullets": [
        "Điện trở tiêu tán năng lượng và làm tần số dưới tắt dần giảm.",
        "Dòng đầu bằng không không cho phép tự đặt pha cosin bằng không khi R khác không.",
        "Hệ số suy giảm biên độ là R trên 2L."
      ],
      "formula": "$$\n\\begin{aligned}&\\alpha=\\frac{R}{2L}\\\\&\\omega_d=\\sqrt{\\frac1{LC}-\\alpha^2}\\\\&q=Ae^{-\\alpha t}\\cos(\\omega_dt+\\phi).\\end{aligned}\n$$"
    },
    {
      "note": "10-tu-cam",
      "title": "Ngưỡng điện trở phân biệt ba chế độ",
      "bullets": [
        "Dưới ngưỡng tới hạn, hệ có dao động tắt dần.",
        "Tại ngưỡng, nghiệm tới hạn không còn phần dao động hình sin.",
        "Trên ngưỡng, nghiệm là tổng hai hàm mũ thực suy giảm."
      ],
      "formula": "$$\n\\begin{aligned}&R_{\\mathrm{th}}=2\\sqrt{\\frac LC}\\\\&R<R_{\\mathrm{th}}\\\\&R=R_{\\mathrm{th}}\\\\&R>R_{\\mathrm{th}}.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Vector pha biến dao động hình sin thành hình chiếu",
      "bullets": [
        "Độ dài vector bằng biên độ và tốc độ quay bằng tần số góc.",
        "Hình chiếu ngang cho giá trị tức thời khi dùng cosin.",
        "Vector pha biểu diễn biên độ và pha, không chỉ một hướng vật lý trong không gian."
      ],
      "formula": "$$\n\\begin{aligned}&i=I\\cos\\omega t\\\\&\\omega=2\\pi f.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Trung bình, trung bình chỉnh lưu và hiệu dụng khác nhau",
      "bullets": [
        "Dòng hình sin có trung bình bằng không qua một số nguyên chu kỳ.",
        "Chỉnh lưu toàn sóng giữ dấu dòng qua điện kế cùng chiều.",
        "Giá trị hiệu dụng được lấy bằng căn của trung bình bình phương."
      ],
      "formula": "$$\n\\begin{aligned}&I_{\\mathrm{rav}}=\\frac2\\pi I\\\\&I_{\\mathrm{rms}}=\\frac I{\\sqrt2}\\\\&V_{\\mathrm{rms}}=\\frac V{\\sqrt2}.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Điện trở giữ điện áp và dòng cùng pha",
      "bullets": [
        "Định luật Ohm liên hệ các giá trị tức thời trên điện trở thuần.",
        "Các cực đại, cực tiểu và điểm bằng không xuất hiện cùng lúc.",
        "Tỉ số biên độ cũng bằng điện trở."
      ],
      "formula": "$$\n\\begin{aligned}&v_R=iR\\\\&V_R=IR.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Cuộn cảm làm điện áp sớm dòng một phần tư chu kỳ",
      "bullets": [
        "Điện áp cuộn theo quy ước thụ động phụ thuộc đạo hàm dòng.",
        "Cảm kháng tăng theo tần số và điện cảm.",
        "Quan hệ giữa biên độ không thay thế được quan hệ tức thời."
      ],
      "formula": "$$\n\\begin{aligned}&v_L=L\\frac{di}{dt}\\\\&X_L=\\omega L\\\\&V_L=IX_L.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Tụ làm điện áp trễ dòng một phần tư chu kỳ",
      "bullets": [
        "Dòng là điện dung nhân tốc độ thay đổi điện áp.",
        "Dung kháng giảm khi tần số hoặc điện dung tăng.",
        "Dòng dẫn không xuyên qua điện môi, nhưng dòng điện dịch duy trì sự liên tục."
      ],
      "formula": "$$\n\\begin{aligned}&i=C\\frac{dv_C}{dt}\\\\&X_C=\\frac1{\\omega C}\\\\&V_C=IX_C.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "RLC nối tiếp cần cộng vector điện áp",
      "bullets": [
        "Dòng tức thời như nhau trên mọi phần tử nối tiếp.",
        "Điện áp cuộn cảm và tụ ngược pha, nên điện kháng tổng là hiệu hai điện kháng.",
        "Biên độ nguồn là độ lớn tổng vector, còn các điện áp tức thời cộng đại số."
      ],
      "formula": "$$\n\\begin{aligned}&X=X_L-X_C\\\\&Z=\\sqrt{R^2+X^2}\\\\&V=IZ.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Góc pha phụ thuộc dấu điện kháng tổng",
      "bullets": [
        "Chọn dòng làm mốc, góc pha dương nghĩa điện áp nguồn sớm dòng.",
        "Cảm kháng lớn hơn dung kháng cho góc dương, còn dung kháng lớn hơn cho góc âm.",
        "Các tỉ số điện áp và dòng giữ nguyên khi đồng loạt dùng hiệu dụng."
      ],
      "formula": "$$\n\\begin{aligned}&\\tan\\phi=\\frac{X_L-X_C}{R}\\\\&v=V\\cos(\\omega t+\\phi)\\\\&V_{\\mathrm{rms}}=I_{\\mathrm{rms}}Z.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Công suất trung bình nhận thành phần điện áp cùng pha",
      "bullets": [
        "Điện trở tiêu tán năng lượng theo cả hai chiều dòng.",
        "Cuộn cảm và tụ lý tưởng nhận rồi trả năng lượng, với công suất trung bình bằng không.",
        "Trong RLC nối tiếp, toàn bộ công suất nhận ròng được tiêu tán trên điện trở."
      ],
      "formula": "$$\n\\begin{aligned}&p=vi\\\\&P_{\\mathrm{av}}=\\frac12VI\\cos\\phi\\\\&\\quad=V_{\\mathrm{rms}}I_{\\mathrm{rms}}\\cos\\phi.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Hệ số công suất thấp làm dòng đường dây lớn hơn",
      "bullets": [
        "Với cùng điện áp và công suất trung bình, hệ số công suất nhỏ đòi hỏi dòng lớn.",
        "Dòng lớn tăng tổn hao nhiệt trên đường dây.",
        "Tụ song song có thể bù thành phần dòng trễ của tải cảm."
      ],
      "formula": "$$\n\\begin{aligned}&\\cos\\phi=\\frac RZ\\\\&I_{\\mathrm{rms}}=\\frac{P_{\\mathrm{av}}}{V_{\\mathrm{rms}}\\cos\\phi}.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Cộng hưởng dòng xảy ra khi hai điện kháng bằng nhau",
      "bullets": [
        "Giữ biên độ nguồn cố định và R dương, dòng lớn nhất khi trở kháng nhỏ nhất.",
        "Tại cộng hưởng, điện áp cuộn và tụ triệt tiêu tức thời, còn nguồn cùng pha dòng.",
        "Điện trở nhỏ tạo đỉnh cao và hẹp hơn, còn vị trí đỉnh do L,C quyết định."
      ],
      "formula": "$$\n\\begin{aligned}&\\omega_0=\\frac1{\\sqrt{LC}}\\\\&X_L=X_C\\\\&Z_{\\min}=R\\\\&I_{\\max}=\\frac VR.\\end{aligned}\n$$"
    },
    {
      "note": "11-dong-dien-xoay-chieu",
      "title": "Máy biến áp đổi điện áp và dòng, giữ công suất lý tưởng",
      "bullets": [
        "Hai cuộn cùng nhận từ thông biến thiên trong lõi.",
        "Tỉ số điện áp bằng tỉ số số vòng khi bỏ qua sụt áp và từ thông rò.",
        "Với tải thuần trở và dòng từ hóa được bỏ qua, tăng áp đi kèm giảm dòng."
      ],
      "formula": "$$\n\\begin{aligned}&\\frac{V_2}{V_1}=\\frac{N_2}{N_1}\\\\&V_1I_1=V_2I_2\\\\&R_{\\mathrm{eq}}=R\\left(\\frac{N_1}{N_2}\\right)^2.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Trường biến thiên liên hệ hai phía của điện từ",
      "bullets": [
        "Faraday liên hệ từ thông biến thiên với điện trường có lưu thông.",
        "Ampère–Maxwell kể cả dòng điện dịch khi điện trường biến thiên.",
        "Điện tích chuyển động có gia tốc có thể phát bức xạ. Sóng truyền được qua chân không."
      ],
      "formula": "$$\n\\begin{aligned}&\\oint\\vec E\\cdot d\\vec l=-\\frac{d\\Phi_B}{dt}\\\\&\\oint\\vec B\\cdot d\\vec l\\\\&=\\mu_0\\left(i_C+\\varepsilon_0\\frac{d\\Phi_E}{dt}\\right).\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Một sóng phẳng chạy có hai trường ngang",
      "bullets": [
        "Các trường đồng đều trên mỗi mặt phẳng vuông góc hướng truyền.",
        "Điện trường, từ trường và hướng truyền tạo bộ ba vuông góc.",
        "Tích có hướng của hai trường xác định hướng dòng năng lượng."
      ],
      "formula": "$$\n\\begin{aligned}&\\vec E\\cdot\\vec B=0\\\\&E=cB\\\\&\\vec S=\\frac1{\\mu_0}\\vec E\\times\\vec B.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Tốc độ ánh sáng xuất hiện từ hằng số điện và từ",
      "bullets": [
        "Faraday và Ampère–Maxwell cùng phải thỏa cho một mặt sóng.",
        "Hai quan hệ biên độ quyết định tốc độ trong chân không.",
        "Trường biến thiên không truyền tức thời."
      ],
      "formula": "$$\n\\begin{aligned}&E=cB\\\\&B=\\varepsilon_0\\mu_0cE\\\\&c=\\frac1{\\sqrt{\\varepsilon_0\\mu_0}}.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Hàm sóng giữ cả dấu pha và hướng trường",
      "bullets": [
        "Pha kx−ωt truyền theo+x, còn kx+ωt truyền theo−x.",
        "Khi đổi hướng truyền, phải đổi quan hệ hướng giữa E và B.",
        "Trong sóng chạy hình sin, hai trường cùng pha."
      ],
      "formula": "$$\n\\begin{aligned}&\\omega=ck\\\\&k=2\\pi/\\lambda\\\\&f=c/\\lambda\\\\&E_{\\max}=cB_{\\max}.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Phổ điện từ là một họ sóng với nhiều thang bước sóng",
      "bullets": [
        "Radio, vi ba, hồng ngoại, ánh sáng nhìn thấy, tử ngoại, tia X và gamma cùng có bản chất điện từ.",
        "Tần số và bước sóng thay đổi, nhưng tốc độ chân không là c.",
        "Phân cực mô tả hướng dao động ngang của điện trường."
      ],
      "formula": "$$\nf\\lambda=c.\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Vật liệu đổi tốc độ và bước sóng",
      "bullets": [
        "Tại mặt phân cách đứng yên, tần số được giữ.",
        "Hằng số vật liệu phải xét ở tần số của sóng.",
        "Công thức dưới dùng mô hình tuyến tính, đồng nhất, đẳng hướng, không tán sắc và không tổn hao."
      ],
      "formula": "$$\n\\begin{aligned}&v=\\frac c{\\sqrt{\\varepsilon_r\\mu_r}}\\\\&\\lambda=v/f\\\\&n=c/v\\\\&E_{\\max}=vB_{\\max}.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Cường độ liên hệ công suất với biên độ trường",
      "bullets": [
        "Vector Poynting cho dòng năng lượng tức thời theo hướng.",
        "Cường độ sóng chạy là độ lớn vector Poynting sau khi lấy trung bình.",
        "Biên độ phải bình phương. Giá trị hiệu dụng đã chứa hệ số trung bình của sóng hình sin."
      ],
      "formula": "$$\n\\begin{aligned}&I=|\\langle\\vec S\\rangle|\\\\&I=\\frac12\\varepsilon_0cE_{\\max}^2\\\\&I=\\frac c{2\\mu_0}B_{\\max}^2.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Động lượng của ánh sáng tạo áp suất",
      "bullets": [
        "Hấp thụ nhận động lượng tới, còn phản xạ ngược chiều nhận gấp đôi.",
        "Các công thức áp suất này xét sóng tới vuông góc.",
        "Công suất có thể đáng kể trong khi lực rất nhỏ vì chia cho tốc độ ánh sáng."
      ],
      "formula": "$$\n\\begin{aligned}&\\vec g=\\vec S/c^2\\\\&p_{\\mathrm a}=I/c\\\\&p_{\\mathrm r}=2I/c\\\\&F=pA.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Sóng đứng vẫn chứa năng lượng dù dòng trung bình triệt tiêu",
      "bullets": [
        "Hai sóng chạy bằng nhau đi ngược chiều tạo sóng đứng.",
        "Hai trường vuông pha theo thời gian, nút điện là bụng từ và ngược lại.",
        "Trung bình vector Poynting bằng không. Trung bình độ lớn của nó có thể khác không."
      ],
      "formula": "$$\n\\begin{aligned}&S_x=S_0\\sin(2kx)\\sin(2\\omega t)\\\\&\\langle S_x\\rangle=0\\\\&S_0=E_{\\max}B_{\\max}/\\mu_0.\\end{aligned}\n$$"
    },
    {
      "note": "12-song-dien-tu",
      "title": "Hai tường dẫn chọn các mode của hốc",
      "bullets": [
        "Hai tường là nút điện trường tiếp tuyến trong mô hình dẫn lý tưởng.",
        "Mỗi nửa bước sóng chứa một bụng điện trường.",
        "Đo khoảng cách bụng và biết tần số cho phép suy tốc độ."
      ],
      "formula": "$$\n\\begin{aligned}&L=n\\lambda_n/2\\\\&\\lambda_n=2L/n\\\\&f_n=nc/(2L)\\\\&n=1,2,3,\\ldots.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Mô hình của ánh sáng phụ thuộc hiện tượng",
      "bullets": [
        "Ánh sáng là sóng điện từ. Sự truyền được mô tả bằng mô hình sóng.",
        "Phát xạ và hấp thụ bộc lộ tính chất hạt. Mô hình tia dùng trong quang hình học.",
        "Mặt sóng có cùng pha. Trong môi trường đồng nhất đẳng hướng, tia thẳng và vuông góc mặt sóng."
      ],
      "formula": "$$\n\\begin{aligned}&c=299\\,792\\,458\\,\\mathrm{m/s}\\\\&v=c/n\\\\&\\lambda=\\lambda_0/n.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Phản xạ và khúc xạ dùng góc với pháp tuyến",
      "bullets": [
        "Tia tới, phản xạ, khúc xạ và pháp tuyến cùng nằm trong mặt phẳng tới.",
        "Mặt nhẵn tạo phản xạ gương, còn mặt nhám phân bố ánh sáng ra nhiều hướng.",
        "Tại mặt phân cách đứng yên, tần số không đổi. Đi vào chiết suất lớn hơn làm góc khúc xạ nhỏ hơn nếu tới xiên."
      ],
      "formula": "$$\n\\begin{aligned}&\\theta_r=\\theta_a\\\\&n_a\\sin\\theta_a=n_b\\sin\\theta_b\\\\&f_a=f_b.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Phản xạ toàn phần cần đúng cả môi trường và góc",
      "bullets": [
        "Chỉ có ngưỡng khi ánh sáng đi từ chiết suất lớn sang chiết suất nhỏ.",
        "Tại ngưỡng, tia khúc xạ có hướng dọc mặt phân cách.",
        "Lăng kính và sợi quang dẫn sáng nhờ các lần phản xạ thỏa điều kiện. Uốn quá gắt có thể làm tia rò ra."
      ],
      "formula": "$$\n\\begin{aligned}&n_a>n_b\\\\&\\sin\\theta_c=n_b/n_a\\\\&\\theta_a>\\theta_c.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Tán sắc biến ánh sáng trắng thành các hướng màu",
      "bullets": [
        "Trong vật liệu, chiết suất có thể phụ thuộc bước sóng chân không.",
        "Ở miền tán sắc chuẩn, tia tím thường có chiết suất lớn hơn tia đỏ.",
        "Qua lăng kính, hai lần khúc xạ tách các màu vì góc lệch phụ thuộc chiết suất."
      ],
      "formula": "$$\n\\begin{aligned}&n=n(\\lambda_0)\\\\&n_{\\mathrm{violet}}>n_{\\mathrm{red}}\\\\&v_{\\mathrm{violet}}<v_{\\mathrm{red}}.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Cầu vồng là vành tập trung tia quanh điểm đối nhật",
      "bullets": [
        "Cầu vồng bậc một có hai lần khúc xạ và một lần phản xạ nội.",
        "Đỏ ở vòng ngoài khoảng 42,5 độ, tím ở vòng trong khoảng 40,8 độ.",
        "Bậc hai có hai phản xạ nội, mờ hơn và đảo thứ tự màu. Bán kính góc đỏ khoảng 50,1 độ, tím khoảng 53,2 độ."
      ],
      "formula": "$$\n\\begin{aligned}&\\Delta_1=\\pi+2i-4r\\\\&\\Delta_2=2\\pi+2i-6r\\\\&\\sin i=n\\sin r.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Kính phân cực truyền một phép chiếu điện trường",
      "bullets": [
        "Phương phân cực được định nghĩa bằng điện trường, vuông góc hướng truyền.",
        "Kính lý tưởng truyền thành phần dọc trục và chặn thành phần vuông góc.",
        "Malus áp dụng cho ánh sáng tới đã phân cực thẳng. Ánh sáng chưa phân cực qua kính đầu còn một nửa cường độ."
      ],
      "formula": "$$\n\\begin{aligned}&E_{\\rm out}=E_{\\rm in}\\cos\\phi\\\\&I_{\\rm out}=I_{\\rm in}\\cos^2\\phi.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Brewster gắn phân cực với hình học phản xạ",
      "bullets": [
        "Ở góc Brewster, tia phản xạ và tia khúc xạ vuông góc.",
        "Thành phần p nằm trong mặt phẳng tới không phản xạ. Thành phần s vẫn có thể phản xạ.",
        "Với chùm tự nhiên, ánh sáng phản xạ vì thế phân cực s. Dùng mô hình điện môi trong suốt không từ tính."
      ],
      "formula": "$$\n\\begin{aligned}&\\tan\\theta_p=n_b/n_a\\\\&\\theta_p+\\theta_b=90^\\circ.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Pha tương đối phân biệt thẳng, tròn và elip",
      "bullets": [
        "Hai thành phần vuông góc cùng pha hoặc ngược pha tạo phân cực thẳng.",
        "Bằng biên độ và lệch pha một phần tư chu kỳ tạo phân cực tròn.",
        "Các trường hợp không suy biến còn lại tạo elip. Lưỡng chiết làm hai thành phần tích lũy pha khác nhau."
      ],
      "formula": "$$\n\\begin{aligned}&E_y=A\\cos\\psi\\\\&E_z=B\\cos(\\psi+\\delta)\\\\&|\\delta|=\\pi/2,\\quad A=B.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Bản trễ pha cần cả chiều dày và hướng trục",
      "bullets": [
        "Hai phương riêng có hai chiết suất, nên độ trễ pha phụ thuộc chiều dày.",
        "Bản phần tư sóng đổi thẳng thành tròn khi hai thành phần tới bằng biên độ.",
        "Quang đàn hồi dùng lưỡng chiết do ứng suất. Kính ba chiều và màn hình tinh thể lỏng điều khiển trạng thái phân cực."
      ],
      "formula": "$$\n\\begin{aligned}&\\Delta\\phi=\\frac{2\\pi(n_1-n_2)d}{\\lambda_0}\\\\&d_{\\min}=\\frac{\\lambda_0}{4|n_1-n_2|}.\\end{aligned}\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Tán xạ làm đổi màu và trạng thái phân cực",
      "bullets": [
        "Điện trường tới làm điện tích phân tử dao động rồi bức xạ theo các hướng khác.",
        "Bước sóng ngắn bị tán xạ mạnh hơn trong mô hình Rayleigh. Chùm trực tiếp đi xa vì thế thiên về đỏ.",
        "Ở góc 90 độ, tán xạ một lần lý tưởng có thể phân cực hoàn toàn. Tán xạ nhiều lần trong mây không giữ kết luận đơn giản ấy."
      ],
      "formula": "$$\nI_{\\rm sc}\\propto1/\\lambda^4.\n$$"
    },
    {
      "note": "13-truyen-anh-sang",
      "title": "Huygens dựng mặt sóng trước khi suy đường tia",
      "bullets": [
        "Mỗi điểm trên mặt sóng là nguồn sóng thứ cấp. Dùng cùng một khoảng thời gian để dựng mặt mới.",
        "Các bán kính bằng nhau trong cùng môi trường cho góc phản xạ bằng góc tới.",
        "Hai tốc độ khác nhau tại mặt phân cách làm mặt sóng quay, dẫn đến Snell. Biến đổi tốc độ theo độ cao tạo đường tia cong và ảo ảnh."
      ],
      "formula": "$$\n\\begin{aligned}&r_a=v_at,\\quad r_b=v_bt\\\\&\\frac{\\sin\\theta_a}{\\sin\\theta_b}=\\frac{v_a}{v_b}\\\\&n_a\\sin\\theta_a=n_b\\sin\\theta_b.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Ảnh thật và ảnh ảo được phân biệt bằng đường tia",
      "bullets": [
        "Ảnh thật là nơi các tia đi ra hội tụ. Ảnh ảo là giao điểm của các đường kéo dài ngược chiều.",
        "Khoảng vật dương ở phía ánh sáng tới, khoảng ảnh dương ở phía ánh sáng ra.",
        "Gương phẳng tạo ảnh ảo đối xứng qua mặt gương của một vật thật."
      ],
      "formula": "$$\n\\begin{aligned}s^\\prime&=-s\\\\m&=y^\\prime/y=1.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Gần đúng cận trục cho một ảnh điểm xác định",
      "bullets": [
        "Các tia gần trục tạo góc nhỏ. Có thể thay sin và tan bằng góc tính bằng radian.",
        "Các tia biên của gương cầu không cùng hội tụ với tia cận trục, gây quang sai cầu.",
        "Gương parabol hội tụ chính xác chùm song song trục tại một tiêu điểm."
      ],
      "formula": "$$\n\\sin\\theta\\approx\\tan\\theta\\approx\\theta.\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Gương cầu dùng bán kính và tiêu cự có dấu",
      "bullets": [
        "Gương lõm có tiêu cự dương, còn gương lồi có tiêu cự âm.",
        "Vật thật trong tiêu cự gương lõm tạo ảnh ảo phóng đại cùng chiều.",
        "Gương lồi tạo ảnh ảo cùng chiều và thu nhỏ của vật thật."
      ],
      "formula": "$$\n\\begin{aligned}f&=R/2\\\\\\frac1s+\\frac1{s^\\prime}&=\\frac1f\\\\m&=-s^\\prime/s.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Mặt khúc xạ phụ thuộc độ chênh chiết suất",
      "bullets": [
        "Tâm cong ở phía ánh sáng đi ra cho bán kính dương.",
        "Khoảng ảnh dương biểu thị hội tụ thật trong môi trường sau mặt phân cách.",
        "Mặt phẳng là giới hạn bán kính vô cực và giữ nguyên kích thước ngang của ảnh cận trục."
      ],
      "formula": "$$\n\\begin{aligned}\\frac{n_a}s+\\frac{n_b}{s^\\prime}&=\\frac{n_b-n_a}R\\\\m&=-\\frac{n_as^\\prime}{n_bs}.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Hai mặt thấu kính phối hợp thành một tiêu cự",
      "bullets": [
        "Kính mỏng cho phép bỏ qua bề dày so với khoảng vật và ảnh.",
        "Kính trong không khí có tiêu cự xác định bởi chiết suất và hai bán kính có dấu.",
        "Hai tiêu cự ở hai phía bằng nhau khi hai môi trường ngoài giống nhau."
      ],
      "formula": "$$\n\\begin{aligned}&\\frac1f=(n-1)\\\\&\\quad\\times\\left(\\frac1{R_1}-\\frac1{R_2}\\right)\\\\&\\frac1s+\\frac1{s^\\prime}=\\frac1f.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Hệ nhiều phần tử cần đổi mốc ở từng bước",
      "bullets": [
        "Tìm ảnh của phần tử đầu trước khi xét phần tử sau.",
        "Ảnh dự kiến nằm sau kính thứ hai là vật ảo của kính đó.",
        "Phóng đại toàn hệ là tích các phóng đại có dấu, nên hai lần đảo chiều có thể cho ảnh cuối cùng chiều."
      ],
      "formula": "$$\n\\begin{aligned}s_2&=d-s^\\prime_1\\\\m&=m_1m_2.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Tiêu cự máy ảnh quyết định kích thước ảnh và góc trông",
      "bullets": [
        "Tiêu cự dài cho ảnh lớn và góc trông hẹp trên cùng bề mặt ghi nhận.",
        "Vật ở gần hơn cần khoảng kính–cảm biến lớn hơn để ảnh nét.",
        "Ống kính zoom thay đổi tiêu cự bằng chuyển động tương đối của các nhóm kính."
      ],
      "formula": "$$\n\\begin{aligned}s^\\prime&=\\frac{fs}{s-f}\\\\m&=-s^\\prime/s.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Chỉ số f nối khẩu độ với độ phơi sáng",
      "bullets": [
        "Chỉ số f bằng tiêu cự chia đường kính khẩu độ.",
        "Cùng cảnh và điều kiện quang học, cường độ ảnh tỉ lệ nghịch bình phương chỉ số f.",
        "Mỗi nấc khẩu danh định đổi cường độ khoảng hai lần. Giữ độ phơi sáng cần bù bằng thời gian."
      ],
      "formula": "$$\n\\begin{aligned}N&=f/D\\\\I&\\propto1/N^2\\\\H&\\propto\\Delta t/N^2.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Mắt điều tiết tiêu cự để giữ ảnh trên võng mạc",
      "bullets": [
        "Giác mạc gây phần lớn khúc xạ vì độ chênh chiết suất với không khí lớn.",
        "Cơ thể mi co làm thể thủy tinh cong hơn, giảm tiêu cự khi nhìn gần.",
        "Kính phân kỳ hiệu chỉnh nhìn xa của mắt cận, kính hội tụ hỗ trợ nhìn gần khi cần ảnh ảo xa hơn."
      ],
      "formula": "$$\nP=1/f.\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Bội giác góc khác độ phóng đại ngang",
      "bullets": [
        "Kích thước góc quyết định kích thước ảnh trên võng mạc.",
        "Kính lúp cho vật ở tiêu điểm để ảnh ở vô cực và mắt không cần điều tiết.",
        "So với nhìn trực tiếp ở khoảng quy ước 25cm, bội giác tăng khi tiêu cự kính lúp giảm."
      ],
      "formula": "$$\n\\begin{aligned}M&=\\theta^\\prime/\\theta\\\\M&=\\frac{25\\,\\mathrm{cm}}f.\\end{aligned}\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Kính hiển vi phóng đại qua hai giai đoạn",
      "bullets": [
        "Vật kính tiêu cự ngắn tạo ảnh thật phóng đại và ngược chiều.",
        "Thị kính dùng ảnh trung gian làm vật cho kính lúp. Ảnh cuối vẫn ngược chiều vật đầu.",
        "Công thức gần đúng dùng vật gần tiêu điểm vật kính và ảnh cuối ở vô cực."
      ],
      "formula": "$$\n|M|\\approx\\frac{(25\\,\\mathrm{cm})s^\\prime_1}{f_1f_2}.\n$$"
    },
    {
      "note": "14-quang-hinh-hoc",
      "title": "Kính thiên văn tăng góc trông của vật rất xa",
      "bullets": [
        "Vật kính tạo ảnh thật thu nhỏ của thiên thể, rồi thị kính phóng đại góc của ảnh đó.",
        "Hai kính hội tụ ngắm chừng ở vô cực cách nhau tổng hai tiêu cự.",
        "Gương lõm làm vật kính tránh quang sai sắc. Các gương phụ đưa ảnh tới thiết bị quan sát hoặc cảm biến."
      ],
      "formula": "$$\n\\begin{aligned}M&=-f_1/f_2\\\\L&=f_1+f_2.\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Chồng chất cộng trường trước khi tính cường độ",
      "bullets": [
        "Mỗi điểm nhận tổng các đóng góp tức thời của những sóng chồng lên nhau.",
        "Với ánh sáng, cộng các thành phần điện trường theo cùng phương.",
        "Cường độ là trung bình của bình phương trường, nên có số hạng phụ thuộc pha."
      ],
      "formula": "$$\nE_{\\rm net}(t)=E_1(t)+E_2(t).\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Nguồn kết hợp giữ quan hệ pha ổn định",
      "bullets": [
        "Hai nguồn đơn sắc cùng tần số có pha tương đối không đổi là nguồn kết hợp.",
        "Nguồn kết hợp có thể lệch pha ban đầu. Đồng pha là một trường hợp riêng.",
        "Chia một nguồn thành hai đường giúp các thay đổi pha chung không phá pha tương đối."
      ],
      "formula": "$$\n\\phi=\\frac{2\\pi\\Delta r}{\\lambda}+\\phi_0.\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Hiệu đường đi chọn các đường cực trị",
      "bullets": [
        "Với hai nguồn đồng pha, hiệu đường đi nguyên bước sóng cho tăng cường.",
        "Hiệu đường đi bán nguyên bước sóng cho triệt giảm.",
        "Triệt tiêu hoàn toàn còn cần hai biên độ tại điểm xét bằng nhau."
      ],
      "formula": "$$\n\\begin{aligned}\\Delta r_{\\max}&=m\\lambda\\\\\\Delta r_{\\min}&=(m+1/2)\\lambda\\\\m&\\in\\mathbb Z.\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Màn xa cho hiệu đường đi theo sin góc",
      "bullets": [
        "Khi khoảng quan sát lớn hơn nhiều khoảng nguồn, hai đường tia gần song song.",
        "Góc đo với đường trung trực hai nguồn.",
        "Miền của sin giới hạn những bậc sáng và tối có thể xuất hiện."
      ],
      "formula": "$$\n\\begin{aligned}\\Delta r&\\approx d\\sin\\theta\\\\|\\sin\\theta|&\\le1.\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Khoảng vân đều là gần đúng ở góc nhỏ",
      "bullets": [
        "Gần tâm có thể lấy sin và tang gần bằng góc theo radian.",
        "Vị trí vân sáng tỉ lệ bậc, bước sóng và khoảng tới màn.",
        "Ra xa tâm cần giữ riêng sin trong điều kiện pha và tang trong tọa độ màn."
      ],
      "formula": "$$\n\\begin{aligned}y_m&\\approx m\\lambda R/d\\\\\\Delta y&\\approx\\lambda R/d\\\\y&=R\\tan\\theta.\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Giản đồ pha cho biên độ tổng",
      "bullets": [
        "Hai vectơ pha cùng quay, có góc cố định bằng pha tương đối.",
        "Biên độ tổng của hai sóng bằng nhau phụ thuộc cos của nửa pha.",
        "Cường độ cực đại của cả hai nguồn bằng bốn lần cường độ một nguồn riêng."
      ],
      "formula": "$$\n\\begin{aligned}E_P&=2E|\\cos(\\phi/2)|\\\\I&=I_0\\cos^2(\\phi/2).\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Pha phản xạ cần xét ở từng mặt",
      "bullets": [
        "Phản xạ từ chiết suất nhỏ sang lớn đổi pha nửa chu kỳ.",
        "Phản xạ theo chiều ngược lại không có lần đổi pha ấy trong mô hình tới vuông góc.",
        "Hai lần đổi pha giống nhau không gây chênh pha tương đối."
      ],
      "formula": "$$\nr=\\frac{n_a-n_b}{n_a+n_b}.\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Màng mỏng phối hợp pha truyền và pha phản xạ",
      "bullets": [
        "Tia từ mặt dưới đi thêm hai lần bề dày màng ở gần pháp tuyến.",
        "Dùng bước sóng chân không thì quang lộ thêm là hai lần chiết suất nhân bề dày.",
        "Một lần đảo pha phản xạ tương đối làm các điều kiện sáng và tối đổi vai trò."
      ],
      "formula": "$$\n\\begin{aligned}\\phi&=4\\pi nt/\\lambda_0+\\phi_r\\\\\\phi_{\\max}&=2m\\pi\\\\\\phi_{\\min}&=(2m+1)\\pi.\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Bề dày biến thiên tạo các dạng vân",
      "bullets": [
        "Màng nêm có bề dày gần tuyến tính theo vị trí và tạo các vân thẳng.",
        "Mặt cầu gần tiếp xúc mặt phẳng tạo các vòng Newton.",
        "Các lớp phủ điều khiển phản xạ bằng quan hệ pha giữa các đường truyền."
      ],
      "formula": "$$\n\\begin{aligned}t(x)&\\approx\\alpha x\\\\t(r)&\\approx r^2/(2R_c).\\end{aligned}\n$$"
    },
    {
      "note": "15-giao-thoa",
      "title": "Michelson biến độ dời gương thành số vân",
      "bullets": [
        "Bộ chia chùm tạo hai đường rồi tái hợp. Bản bù cân bằng bề dày kính hai đường.",
        "Gương dịch làm đường đi hai lượt thay đổi gấp đôi độ dời trong không khí.",
        "Biết bước sóng có thể đo khoảng cách bằng đếm vân, hoặc dùng độ dời đã biết để suy bước sóng."
      ],
      "formula": "$$\n\\begin{aligned}2y&=N\\lambda\\\\\\lambda&=2y/N.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Nhiễu xạ là chồng chất các phần mặt sóng",
      "bullets": [
        "Mỗi phần của khẩu độ đóng góp một sóng thứ cấp.",
        "Fraunhofer dùng các hướng gần song song ở miền xa hoặc tiêu diện.",
        "Fresnel cần giữ độ cong mặt sóng khi hình học còn ở miền gần."
      ],
      "formula": "$$\nE_P=E_1+E_2.\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Cực tiểu khe đơn cần triệt tiêu toàn khe",
      "bullets": [
        "Hai nửa khe có thể ghép thành các cặp ngược pha ở cực tiểu đầu.",
        "Bậc không khác không phân biệt cực tiểu với tâm cực đại.",
        "Khe càng hẹp, góc mở trung tâm càng lớn."
      ],
      "formula": "$$\n\\begin{aligned}a\\sin\\theta_m&=m\\lambda\\\\m&=\\pm1,\\pm2,\\ldots.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Cường độ khe đơn không giảm tuyến tính",
      "bullets": [
        "Đối số là nửa độ lệch pha giữa hai mép khe.",
        "Tại tâm, dùng giới hạn để được cường độ cực đại.",
        "Các cực đại phụ được tìm từ phương trình tang bằng đối số."
      ],
      "formula": "$$\n\\begin{aligned}\\gamma&=\\pi a\\sin\\theta/\\lambda\\\\I&=I_0(\\sin\\gamma/\\gamma)^2.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Vị trí trên màn cần phân biệt sin và tang",
      "bullets": [
        "Điều kiện pha dùng sin của góc.",
        "Tọa độ trên màn phẳng dùng tang của góc.",
        "Công thức bề rộng tỉ lệ nghịch khe cần góc nhỏ."
      ],
      "formula": "$$\n\\begin{aligned}y_m&=R\\tan\\theta_m\\\\y_m&\\approx Rm\\lambda/a.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Vân giao thoa nằm trong bao nhiễu xạ",
      "bullets": [
        "Khoảng tâm khe quyết định nhịp của thừa số giao thoa.",
        "Bề rộng mỗi khe quyết định bao nhiễu xạ.",
        "Một bậc bị khuyết khi cực đại giao thoa trùng cực tiểu của bao."
      ],
      "formula": "$$\n\\begin{aligned}d\\sin\\theta&=m_i\\lambda\\\\a\\sin\\theta&=m_d\\lambda\\\\m_i&=(d/a)m_d.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Nhiều khe cho cực đại chính hẹp",
      "bullets": [
        "Vị trí cực đại chính giữ cùng điều kiện pha giữa các khe kề nhau.",
        "Có N trừ một cực tiểu giữa hai cực đại chính.",
        "Bề rộng theo pha tỉ lệ nghịch số khe khi các đóng góp cùng biên độ."
      ],
      "formula": "$$\n\\begin{aligned}I_{\\max}&=N^2I_s\\\\\\Delta\\phi&=4\\pi/N.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Cách tử tách bước sóng theo góc",
      "bullets": [
        "Ở tới vuông góc, cực đại có hiệu đường đi nguyên bước sóng.",
        "Bước sóng dài hơn lệch nhiều hơn trên cùng phía và cùng bậc.",
        "Bậc cao có thể chồng phổ với những bậc khác."
      ],
      "formula": "$$\nd\\sin\\theta_m=m\\lambda.\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Năng suất phân giải phổ phụ thuộc số khe",
      "bullets": [
        "Hai vạch vừa phân giải khi đỉnh một vạch trùng cực tiểu đầu của vạch kia.",
        "Số khe được chiếu sáng và bậc phổ cùng làm tăng độ phân giải.",
        "Điều kiện góc tồn tại vẫn giới hạn các bậc dùng được."
      ],
      "formula": "$$\n\\mathcal R=\\lambda/\\Delta\\lambda=mN.\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Bragg dùng góc với mặt mạng",
      "bullets": [
        "Các nguyên tử trong mỗi mặt tán xạ kết hợp theo hướng phản xạ.",
        "Hai mặt mạng liên tiếp tạo thêm cả đường vào và đường ra.",
        "Dùng bước sóng trong môi trường của mạng tán xạ."
      ],
      "formula": "$$\n\\begin{aligned}2d\\sin\\theta&=m\\lambda\\\\m&=1,2,3,\\ldots.\\end{aligned}\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Khẩu độ tròn tạo đĩa Airy và giới hạn chi tiết",
      "bullets": [
        "Một vật điểm cho ảnh có bề rộng hữu hạn.",
        "Tiêu chuẩn Rayleigh so độ tách hai ảnh với vòng tối đầu.",
        "Khẩu độ lớn hơn và bước sóng ngắn hơn giảm giới hạn góc."
      ],
      "formula": "$$\n\\sin\\theta_R=1{,}22\\lambda/D.\n$$"
    },
    {
      "note": "16-nhieu-xa",
      "title": "Ảnh toàn ký tái tạo sóng hội tụ và phân kỳ",
      "bullets": [
        "Chùm vật và chùm chuẩn cùng ghi hệ vân trên phim.",
        "Chiếu chùm thích hợp lên bản ghi có thể tạo ảnh thật và ảnh ảo.",
        "Quan hệ pha và độ ổn định cơ học phải được giữ trong lúc ghi."
      ],
      "formula": "$$\n\\begin{aligned}b_m-b_0&=m\\lambda\\\\r_m^2&=2m\\lambda b_0+m^2\\lambda^2.\\end{aligned}\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Hai tiên đề đặt giới hạn cho mô tả chuyển động",
      "bullets": [
        "Các định luật vật lý có cùng dạng trong mọi hệ quán tính.",
        "Ánh sáng trong chân không có cùng tốc độ trong các hệ ấy.",
        "Vận tốc nguồn không được cộng theo Galileo vào tốc độ ánh sáng."
      ],
      "formula": "$$\nc=299\\,792\\,458\\,\\mathrm{m/s}.\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Đồng thời phụ thuộc hệ ở những vị trí khác nhau",
      "bullets": [
        "Hai hệ phải gán tọa độ cho cùng những sự kiện.",
        "Đồng hồ được đồng bộ riêng trong từng hệ quán tính.",
        "Hai sự kiện trùng cả vị trí và thời điểm vẫn trùng nhau trong mọi hệ."
      ],
      "formula": "$$\n\\begin{aligned}\\Delta t&=0\\\\\\Delta t'&=-\\gamma u\\Delta x/c^2.\\end{aligned}\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Thời gian riêng gắn với hai sự kiện cùng vị trí",
      "bullets": [
        "Đồng hồ có mặt ở cả hai sự kiện đo thời gian riêng.",
        "Trong hệ mà đồng hồ chuyển động, khoảng thời gian giữa cùng hai sự kiện dài hơn.",
        "Thời gian sự kiện đã phân biệt với thời gian ánh sáng đến mắt."
      ],
      "formula": "$$\n\\begin{aligned}\\gamma&=1/\\sqrt{1-u^2/c^2}\\\\\\Delta t&=\\gamma\\Delta t_0.\\end{aligned}\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Chiều dài cần đo hai đầu đồng thời trong hệ đang xét",
      "bullets": [
        "Độ dài riêng thuộc hệ nghỉ của vật.",
        "Chỉ kích thước dọc vận tốc tương đối bị co.",
        "Ảnh nhìn thấy còn phụ thuộc thời gian truyền ánh sáng."
      ],
      "formula": "$$\nl=l_0/\\gamma.\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Lorentz trộn tọa độ không gian với thời gian",
      "bullets": [
        "Hệ có dấu phẩy chuyển động theo chiều dương với tốc độ u.",
        "Hai gốc trùng nhau tại thời điểm cả hai đồng hồ bằng không.",
        "Đổi hệ ngược bằng cách đổi dấu u và hoán đổi dấu phẩy."
      ],
      "formula": "$$\n\\begin{aligned}x'&=\\gamma(x-ut)\\\\t'&=\\gamma(t-ux/c^2).\\end{aligned}\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Phép cộng vận tốc giữ ánh sáng ở tốc độ c",
      "bullets": [
        "Phân biệt vận tốc vật với vận tốc tương đối của hai hệ.",
        "Chuyển động một chiều dùng cùng quy ước trục ở cả hai hệ.",
        "Vật dưới tốc độ ánh sáng trong một hệ vẫn dưới giới hạn ấy trong hệ kia."
      ],
      "formula": "$$\nv'_x=\\frac{v_x-u}{1-uv_x/c^2}.\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Doppler đổi tần số và bước sóng đồng thời",
      "bullets": [
        "Nguồn tiến lại gần cho tần số cao hơn trong cấu hình dọc đường nhìn.",
        "Rời xa dùng dấu tốc độ ngược trong hệ số Doppler.",
        "Công thức Doppler âm không thay thế công thức ánh sáng trong chân không."
      ],
      "formula": "$$\nf=f_0\\sqrt{\\frac{c+u}{c-u}}.\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Động lượng có thêm hệ số Lorentz của hạt",
      "bullets": [
        "Khối lượng trong công thức là khối lượng nghỉ.",
        "Động lượng cùng hướng vận tốc và trở về gần đúng Newton ở tốc độ nhỏ.",
        "Ở gần c, động lượng tăng mạnh trong khi tốc độ chỉ tăng ít."
      ],
      "formula": "$$\n\\vec p=\\gamma m\\vec v.\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Gia tốc không luôn cùng hướng hợp lực",
      "bullets": [
        "Lực dọc vận tốc làm đổi cả hệ số Lorentz và tốc độ.",
        "Lực ngang vận tốc đổi hướng động lượng với hệ số khác.",
        "Trong chuyển động tròn đều, lực hướng tâm không sinh công."
      ],
      "formula": "$$\n\\begin{aligned}F_\\parallel&=\\gamma^3ma_\\parallel\\\\F_\\perp&=\\gamma ma_\\perp.\\end{aligned}\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Động năng là phần năng lượng ngoài năng lượng nghỉ",
      "bullets": [
        "Không đồng nhất động năng với năng lượng toàn phần.",
        "Năng lượng nghỉ vẫn có khi hạt đứng yên.",
        "Giới hạn tốc độ nhỏ cho động năng Newton."
      ],
      "formula": "$$\n\\begin{aligned}K&=(\\gamma-1)mc^2\\\\E&=K+mc^2.\\end{aligned}\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Tạo hạt phải bảo toàn cả năng lượng và động lượng",
      "bullets": [
        "Tổng khối lượng nghỉ riêng lẻ có thể thay đổi trong phản ứng.",
        "Năng lượng toàn phần của hệ cô lập vẫn bảo toàn.",
        "Hai chùm đối đầu giảm năng lượng dành cho chuyển động khối tâm."
      ],
      "formula": "$$\nE^2=(mc^2)^2+(pc)^2.\n$$"
    },
    {
      "note": "17-thuyet-tuong-doi",
      "title": "Hấp dẫn đòi hỏi mở rộng mô tả hệ quy chiếu",
      "bullets": [
        "Cơ học Newton là giới hạn tương ứng ở tốc độ nhỏ.",
        "Nguyên lý tương đương so các phép thử cục bộ trong trọng trường và hệ gia tốc.",
        "Định vị vệ tinh cần hiệu chỉnh cả chuyển động lẫn hấp dẫn."
      ],
      "formula": "$$\nE_0=mc^2.\n$$"
    }
  ],
  "illustration": "field",
  "contentPolicy": "full-source-translation"
}
