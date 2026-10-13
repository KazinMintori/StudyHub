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
    },
    {
      "note": "06-mach-dien-mot-chieu",
      "title": "Nối tiếp giữ dòng, song song giữ điện áp",
      "bullets": [
        "Nối tiếp không có nhánh rẽ giữa các điện trở nên các dòng bằng nhau.",
        "Song song nối vào cùng hai nút nên các hiệu điện thế bằng nhau.",
        "Điện trở tương đương giữ nguyên quan hệ dòng và điện áp nhìn từ hai đầu tổ hợp."
      ],
      "formula": "$$\n\\begin{aligned}\nR_s&=R_1+R_2,\\\\\n\\frac1{R_p}&=\\frac1{R_1}+\\frac1{R_2},\\\\\nR_p&=\\frac{R_1R_2}{R_1+R_2}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nI_1+I_2-I_3&=0,\\\\\nI_1+I_2&=I_3.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n\\Delta V_1+\\Delta V_2+\\Delta V_3&=0,\\\\\n\\mathcal E-IR_1-IR_2&=0.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nR_{\\mathrm{sh}}&=\\frac{I_GR_G}{I-I_G},\\\\\nR_s&=\\frac{V}{I_G}-R_G.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nR_A&\\to0,\\\\\nR_V&\\to\\infty,\\\\\nI_G&=0\\quad\\text{(cân bằng)}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n\\tau&=RC,\\\\\nq(t)&=C\\mathcal E(1-e^{-t/\\tau}),\\\\\ni(t)&=\\frac{\\mathcal E}{R}e^{-t/\\tau}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nq(t)&=Q_0e^{-t/\\tau},\\\\\ni(t)&=-\\frac{Q_0}{\\tau}e^{-t/\\tau},\\\\\nU(t)&=\\frac{Q_0^2}{2C}e^{-2t/\\tau}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nI&=I_1+I_2\\\\\n&\\quad+\\cdots+I_n,\\\\\nP&=VI,\\\\\n1\\,\\mathrm{kW\\cdot h}&=3.60\\,\\mathrm{MJ},\\\\\n1\\,\\mathrm{MJ}&=10^6\\,\\mathrm J.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n\\vec F&=q\\vec v\\times\\vec B,\\\\\nF&=|q|vB\\sin\\phi,\\\\\n\\vec F\\cdot\\vec v&=0.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n\\Phi_B&=\\int\\vec B\\cdot d\\vec A,\\\\\n\\Phi_B&=BA\\cos\\phi,\\\\\n1\\,\\mathrm{Wb}&=1\\,\\mathrm{T\\cdot m^2}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nR&=\\frac{mv_\\perp}{|q|B},\\\\\n\\omega&=\\frac{|q|B}{m},\\\\\nT&=\\frac{2\\pi m}{|q|B},\\\\\np&=v_\\parallel T.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nq\\vec E+q\\vec v\\times\\vec B&=0,\\\\\nv&=E/B.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nR&=\\frac{mv}{|q|B'},\\\\\n\\frac m{|q|}&=\\frac{BB'R}{E}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n\\vec F&=I\\vec l\\times\\vec B,\\\\\nd\\vec F&=I\\,d\\vec l\\times\\vec B.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\n\\vec\\mu&=NI\\vec A,\\\\\n\\vec\\tau&=\\vec\\mu\\times\\vec B.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nU&=-\\vec\\mu\\cdot\\vec B,\\\\\nU&=-\\mu B\\cos\\phi.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nV_{ab}&=\\mathcal E+Ir,\\\\\nP_{\\mathrm{in}}&=V_{ab}I,\\\\\nP_{\\mathrm{mech}}&=\\mathcal EI,\\\\\nP_r&=I^2r.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}\nE_z&=-v_xB_y,\\\\\nJ_x&=nqv_x,\\\\\nnq&=-\\frac{J_xB_y}{E_z}.\n\\end{aligned}\n$$",
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
      "formula": "$$\n\\begin{aligned}&B(r) = \\frac{\\mu_0 I r}{2\\pi R^2},\\quad r<R\\\\&B(r) = \\frac{\\mu_0 I}{2\\pi r},\\quad r\\ge R.\\end{aligned}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Ống dây dài và xuyến tập trung trường nhờ đối xứng",
      "bullets": [
        "Ở vùng giữa ống dây dài, trường gần đều và bên ngoài nhỏ.",
        "Trong lõi xuyến, trường phụ thuộc bán kính tính từ trục xuyến.",
        "Các kết quả là gần đúng hình học và giả thiết môi trường không từ tính."
      ],
      "formula": "$$\n\\begin{aligned}&B_{\\text{ống dây}} \\approx \\mu_0 nI\\\\&B_{\\text{xuyến}}(r) = \\frac{\\mu_0 NI}{2\\pi r}.\\end{aligned}\n$$"
    },
    {
      "note": "08-nguon-tu-truong",
      "title": "Độ từ hóa bổ sung vào trường do dòng ngoài",
      "bullets": [
        "Độ từ hóa là mômen từ trên một đơn vị thể tích.",
        "Trong vật liệu tuyến tính đẳng hướng, độ từ thẩm tương đối liên hệ với độ cảm từ.",
        "Không dùng quan hệ tuyến tính như hằng số vật liệu sắt từ khi vật liệu bão hòa hoặc có từ trễ."
      ],
      "formula": "$$\n\\begin{aligned}&\\vec B = \\vec B_0+\\mu_0\\vec M\\\\&\\mu = K_m\\mu_0\\\\&\\chi_m = K_m-1.\\end{aligned}\n$$"
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
    }
  ],
  "illustration": "field",
  "contentPolicy": "full-source-translation"
}
