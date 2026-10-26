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
    "thanh-phan-vector",
    "tich-vo-huong",
    "tich-co-huong"
  ],
  "status": "ready",
  "number": 1,
  "sourceChapter": 1,
  "topicGroups": [
    {
      "title": "Đơn vị, đại lượng vật lý và vector",
      "topics": [
        {
          "slug": "ban-chat-vat-ly",
          "title": "Bản chất của vật lý",
          "question": "Lý thuyết vật lý được hình thành và kiểm chứng qua thực nghiệm như thế nào?",
          "source": "1.1"
        },
        {
          "slug": "giai-bai-toan-vat-ly",
          "title": "Giải bài toán vật lý",
          "question": "Quy trình bốn bước I SEE và phương pháp mô hình lý tưởng hóa vận hành ra sao?",
          "source": "1.2"
        },
        {
          "slug": "chuan-va-don-vi",
          "title": "Chuẩn đo lường và hệ đơn vị SI",
          "question": "Giây, mét, kilôgam và các tiền tố đơn vị được xác định, sử dụng như thế nào?",
          "source": "1.3"
        },
        {
          "slug": "su-dung-doi-don-vi",
          "title": "Sử dụng và đổi đơn vị",
          "question": "Tính nhất quán thứ nguyên và phương pháp hệ số đổi đơn vị được áp dụng ra sao?",
          "source": "1.4"
        },
        {
          "slug": "do-bat-dinh-chu-so",
          "title": "Độ bất định và chữ số có nghĩa",
          "question": "Quy tắc xác định chữ số có nghĩa trong phép tính nhân, chia, cộng, trừ là gì?",
          "source": "1.5"
        },
        {
          "slug": "uoc-luong-bac-do-lon",
          "title": "Ước lượng và bậc độ lớn",
          "question": "Làm thế nào để ước lượng gần đúng theo bậc độ lớn khi thiếu dữ liệu chính xác?",
          "source": "1.6"
        },
        {
          "slug": "vector-va-phep-cong-vector",
          "title": "Vector và phép cộng vector",
          "question": "Phép cộng và trừ vector theo phương pháp hình học tuân theo những định luật nào?",
          "source": "1.7"
        },
        {
          "slug": "thanh-phan-vector",
          "title": "Thành phần của vector",
          "question": "Làm thế nào xác định, cộng và nhân các thành phần của vector?",
          "source": "1.8"
        },
        {
          "slug": "vector-don-vi",
          "title": "Vector đơn vị",
          "question": "Hệ vector đơn vị trực chuẩn biểu diễn các vector trong không gian như thế nào?",
          "source": "1.9"
        },
        {
          "slug": "cac-phep-nhan-vector",
          "title": "Các phép nhân vector",
          "question": "Sự khác biệt về định nghĩa và ý nghĩa hình học giữa tích vô hướng và tích có hướng là gì?",
          "source": "1.10"
        }
      ]
    }
  ],
  "hasChapterExercises": true
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
    "thanh-phan-vector",
    "dao-ham",
    "gia-toc"
  ],
  "supportingConcepts": [
    "vector-vi-tri",
    "gia-toc-huong-tam",
    "chuyen-dong-nem",
    "van-toc-tuong-doi",
    "van-toc-vat-ly",
    "toc-do-chuyen-dong"
  ],
  "status": "ready",
  "number": 3,
  "sourceChapter": 3,
  "topicGroups": [
    {
      "title": "Chuyển động trong hai hoặc ba chiều",
      "topics": [
        {
          "slug": "vector-vi-tri-va-van-toc",
          "title": "Vector vị trí và vector vận tốc",
          "question": "Làm thế nào xác định vị trí và chiều chuyển động của chất điểm trong không gian?",
          "source": "3.1"
        },
        {
          "slug": "vector-gia-toc",
          "title": "Vector gia tốc",
          "question": "Vì sao vật chuyển động với tốc độ không đổi trên đường cong vẫn có gia tốc?",
          "source": "3.2"
        },
        {
          "slug": "chuyen-dong-nem",
          "title": "Chuyển động ném",
          "question": "Các chuyển động theo phương ngang và phương thẳng đứng độc lập với nhau thế nào?",
          "source": "3.3"
        },
        {
          "slug": "chuyen-dong-tron",
          "title": "Chuyển động tròn",
          "question": "Điều gì quyết định độ lớn và phương hướng của gia tốc trong chuyển động tròn?",
          "source": "3.4"
        },
        {
          "slug": "van-toc-tuong-doi",
          "title": "Vận tốc tương đối",
          "question": "Làm thế nào liên hệ kết quả đo vận tốc giữa các hệ quy chiếu chuyển động đối với nhau?",
          "source": "3.5"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "04-dinh-luat-newton",
  "title": "Các định luật chuyển động của Newton",
  "prerequisites": [
    "vector",
    "thanh-phan-vector",
    "gia-toc"
  ],
  "supportingConcepts": [
    "luc",
    "he-quy-chieu-quan-tinh",
    "luc-phap-tuyen",
    "ma-sat-nghi",
    "ma-sat-truot",
    "don-vi",
    "dao-ham",
    "tich-phan"
  ],
  "status": "ready",
  "number": 4,
  "sourceChapter": 4,
  "topicGroups": [
    {
      "title": "Các định luật chuyển động của Newton",
      "topics": [
        {
          "slug": "luc-va-tuong-tac",
          "title": "Lực và tương tác",
          "question": "Làm thế nào mô tả và tổng hợp các lực tác dụng lên một vật?",
          "source": "4.1"
        },
        {
          "slug": "dinh-luat-thu-nhat-newton",
          "title": "Định luật thứ nhất của Newton",
          "question": "Khi tổng ngoại lực bằng không, vật có thể chuyển động như thế nào?",
          "source": "4.2"
        },
        {
          "slug": "dinh-luat-thu-hai-newton",
          "title": "Định luật thứ hai của Newton",
          "question": "Tổng ngoại lực và khối lượng xác định gia tốc ra sao?",
          "source": "4.3"
        },
        {
          "slug": "khoi-luong-va-trong-luong",
          "title": "Khối lượng và trọng lượng",
          "question": "Vì sao khối lượng không đổi khi chuyển nơi nhưng trọng lượng có thể đổi?",
          "source": "4.4"
        },
        {
          "slug": "dinh-luat-thu-ba-newton",
          "title": "Định luật thứ ba của Newton",
          "question": "Hai lực tương tác bằng nhau có làm hợp lực lên mỗi vật bằng không không?",
          "source": "4.5"
        },
        {
          "slug": "so-do-luc",
          "title": "Sơ đồ lực",
          "question": "Những lực nào được đưa vào sơ đồ của vật đã chọn?",
          "source": "4.6"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "05-ung-dung-newton",
  "title": "Áp dụng các định luật Newton",
  "prerequisites": [
    "vector",
    "thanh-phan-vector",
    "luc",
    "he-quy-chieu-quan-tinh",
    "gia-toc",
    "gia-toc-huong-tam"
  ],
  "supportingConcepts": [
    "luc-phap-tuyen",
    "ma-sat-nghi",
    "ma-sat-truot",
    "can-bang-co-hoc",
    "dao-ham",
    "tich-phan"
  ],
  "status": "draft",
  "number": 5,
  "sourceChapter": 5,
  "topicGroups": [
    {
      "title": "Áp dụng các định luật Newton",
      "topics": [
        {
          "slug": "can-bang-chat-diem-dinh-luat-1",
          "title": "Sử dụng định luật I Newton: Chất điểm cân bằng",
          "question": "Làm thế nào xác định lực khi vật đứng yên hoặc chuyển động thẳng đều?",
          "source": "5.1"
        },
        {
          "slug": "dong-luc-hoc-chat-diem-dinh-luat-2",
          "title": "Sử dụng định luật II Newton: Động lực học chất điểm",
          "question": "Phân tích lực và gia tốc của một hoặc nhiều vật bằng cách nào?",
          "source": "5.2"
        },
        {
          "slug": "luc-ma-sat-va-luc-can",
          "title": "Lực ma sát và lực cản chất lưu",
          "question": "Điều kiện tiếp xúc và vận tốc tương đối quyết định ma sát, lực cản ra sao?",
          "source": "5.3"
        },
        {
          "slug": "dong-luc-hoc-chuyen-dong-tron",
          "title": "Động lực học chuyển động tròn",
          "question": "Các lực thực tế tạo thành phần hướng tâm như thế nào?",
          "source": "5.4"
        },
        {
          "slug": "cac-luc-co-ban-trong-tu-nhien",
          "title": "Các tương tác cơ bản của tự nhiên",
          "question": "Bốn tương tác cơ bản có những tính chất chủ yếu gì?",
          "source": "5.5"
        }
      ]
    }
  ]
},
    {
  "slug": "06-cong-dong-nang",
  "title": "Công và động năng",
  "prerequisites": [
    "vector",
    "luc",
    "tich-vo-huong",
    "dao-ham",
    "tich-phan"
  ],
  "supportingConcepts": [
    "cong-nang-luong"
  ],
  "status": "ready",
  "number": 6,
  "sourceChapter": 6,
  "topicGroups": [
    {
      "title": "Công và động năng",
      "topics": [
        {
          "slug": "cong-co-hoc",
          "title": "Công cơ học",
          "question": "Làm thế nào để đo lường tác dụng truyền năng lượng của một lực khi làm vật dịch chuyển?",
          "source": "6.1"
        },
        {
          "slug": "dong-nang-va-dinh-ly-cong-dong-nang",
          "title": "Động năng và định lý công–động năng",
          "question": "Công toàn phần tác dụng lên chất điểm làm thay đổi trạng thái chuyển động của nó như thế nào?",
          "source": "6.2"
        },
        {
          "slug": "cong-va-nang-luong-voi-luc-bien-doi",
          "title": "Công và năng lượng với lực biến đổi",
          "question": "Tính công thế nào khi lực thay đổi theo tọa độ hoặc tác dụng dọc theo một quỹ đạo cong?",
          "source": "6.3"
        },
        {
          "slug": "cong-suat",
          "title": "Công suất",
          "question": "Tốc độ sinh công hoặc tiêu thụ năng lượng theo thời gian được định lượng ra sao?",
          "source": "6.4"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "07-the-nang-bao-toan-co-nang",
  "title": "Thế năng và bảo toàn năng lượng",
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "dao-ham",
    "tich-phan"
  ],
  "supportingConcepts": [
    "can-bang-co-hoc",
    "gia-toc",
    "vector"
  ],
  "status": "ready",
  "number": 7,
  "sourceChapter": 7,
  "topicGroups": [
    {
      "title": "Thế năng và bảo toàn năng lượng",
      "topics": [
        {
          "slug": "the-nang-trong-truong",
          "title": "Thế năng trọng trường",
          "question": "Thế năng trọng trường được định nghĩa thế nào và khi nào cơ năng được bảo toàn trong chuyển động thẳng đứng?",
          "source": "7.1"
        },
        {
          "slug": "the-nang-dan-hoi",
          "title": "Thế năng đàn hồi",
          "question": "Năng lượng tích trữ trong lò xo biến dạng phụ thuộc vào độ biến dạng ra sao?",
          "source": "7.2"
        },
        {
          "slug": "luc-bao-toan-va-khong-bao-toan",
          "title": "Lực bảo toàn và lực không bảo toàn",
          "question": "Dấu hiệu phân biệt lực bảo toàn với lực không bảo toàn và định luật bảo toàn năng lượng tổng quát là gì?",
          "source": "7.3"
        },
        {
          "slug": "luc-va-the-nang",
          "title": "Lực và thế năng",
          "question": "Làm thế nào xác định lực tác dụng khi biết hàm thế năng của hệ?",
          "source": "7.4"
        },
        {
          "slug": "do-thi-nang-luong",
          "title": "Đồ thị năng lượng",
          "question": "Đồ thị thế năng cho biết gì về giới hạn chuyển động và các vị trí cân bằng bền, không bền?",
          "source": "7.5"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "08-dong-luong-va-cham",
  "title": "Động lượng, xung lượng và va chạm",
  "prerequisites": [
    "vector",
    "luc",
    "he-quy-chieu-quan-tinh",
    "van-toc-tuong-doi",
    "cong-nang-luong"
  ],
  "supportingConcepts": [
    "dong-luong-vat-ly",
    "khoi-tam",
    "va-cham-dan-hoi"
  ],
  "status": "draft",
  "number": 8,
  "sourceChapter": 8,
  "topicGroups": [
    {
      "title": "Động lượng, xung lượng và va chạm",
      "topics": [
        {
          "slug": "dong-luong-va-xung-luong",
          "title": "Động lượng và xung lượng",
          "question": "Động lượng của một chất điểm được định nghĩa như thế nào và xung lượng của hợp lực tác dụng làm thay đổi động lượng ra sao?",
          "source": "8.1"
        },
        {
          "slug": "dinh-luat-bao-toan-dong-luong",
          "title": "Định luật bảo toàn động lượng",
          "question": "Trong những điều kiện nào thì tổng động lượng của một hệ chất điểm được bảo toàn và nguyên lý này áp dụng ra sao cho chuyển động nhiều chiều?",
          "source": "8.2"
        },
        {
          "slug": "bao-toan-dong-luong-va-va-cham",
          "title": "Bảo toàn động lượng và va chạm",
          "question": "Sự khác biệt về mặt cơ chế và năng lượng giữa va chạm đàn hồi, va chạm không đàn hồi và va chạm hoàn toàn mềm là gì?",
          "source": "8.3"
        },
        {
          "slug": "va-cham-dan-hoi",
          "title": "Va chạm đàn hồi",
          "question": "Trong va chạm đàn hồi một chiều và hai chiều, các phương trình bảo toàn động lượng và bảo toàn động năng liên hệ với nhau như thế nào?",
          "source": "8.4"
        },
        {
          "slug": "khoi-tam",
          "title": "Khối tâm",
          "question": "Khối tâm của một hệ chất điểm được xác định ra sao và hợp ngoại lực chi phối gia tốc của khối tâm theo quy luật nào?",
          "source": "8.5"
        },
        {
          "slug": "chuyen-dong-phan-luc-ten-lua",
          "title": "Chuyển động phản lực của tên lửa",
          "question": "Phương trình chuyển động phản lực của tên lửa được thiết lập như thế nào khi khối lượng của tên lửa liên tục giảm theo thời gian?",
          "source": "8.6"
        }
      ]
    }
  ]
},
    {
  "slug": "09-dong-hoc-vat-ran",
  "title": "Chuyển động quay của vật rắn",
  "prerequisites": [
    "dao-ham",
    "tich-phan",
    "vector",
    "cong-nang-luong"
  ],
  "supportingConcepts": [
    "toa-do-goc",
    "van-toc-goc",
    "gia-toc-goc",
    "momen-quan-tinh",
    "dinh-ly-truc-song-song",
    "ban-kinh-quan-tinh"
  ],
  "status": "ready",
  "number": 9,
  "sourceChapter": 9,
  "topicGroups": [
    {
      "title": "Chuyển động quay và vật rắn",
      "topics": [
        {
          "slug": "van-toc-va-gia-toc-goc",
          "title": "Vận tốc góc và gia tốc góc",
          "question": "Làm thế nào mô tả vị trí và chiều quay của toàn bộ vật rắn?",
          "source": "9.1"
        },
        {
          "slug": "quay-gia-toc-goc-khong-doi",
          "title": "Quay với gia tốc góc không đổi",
          "question": "Khi nào dùng được các phương trình quay tương tự chuyển động thẳng?",
          "source": "9.2"
        },
        {
          "slug": "lien-he-dai-luong-dai-va-goc",
          "title": "Liên hệ đại lượng dài và đại lượng góc",
          "question": "Vì sao các điểm trên cùng vật có cùng vận tốc góc nhưng khác tốc độ dài?",
          "source": "9.3"
        },
        {
          "slug": "dong-nang-va-momen-quan-tinh",
          "title": "Động năng quay và mômen quán tính",
          "question": "Sự phân bố khối lượng quanh trục quyết định động năng quay thế nào?",
          "source": "9.4"
        },
        {
          "slug": "dinh-ly-truc-song-song",
          "title": "Định lý trục song song",
          "question": "Đổi trục quay song song làm mômen quán tính thay đổi ra sao?",
          "source": "9.5"
        },
        {
          "slug": "tinh-momen-quan-tinh",
          "title": "Tính mômen quán tính bằng tích phân",
          "question": "Chọn phần tử khối lượng nào để tính mômen quán tính của một vật liên tục?",
          "source": "9.6"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "10-dong-luc-hoc-quay",
  "title": "Động lực học chuyển động quay",
  "prerequisites": [
    "vector",
    "luc",
    "momen-quan-tinh",
    "cong-nang-luong",
    "dong-luong-vat-ly"
  ],
  "supportingConcepts": [
    "momen-luc",
    "momen-dong-luong",
    "lan-khong-truot",
    "con-quay-tien-dong"
  ],
  "status": "ready",
  "number": 10,
  "sourceChapter": 10,
  "topicGroups": [
    {
      "title": "Chuyển động quay và vật rắn",
      "topics": [
        {
          "slug": "momen-luc",
          "title": "Mômen lực",
          "question": "Lực tác dụng ở đâu và theo hướng nào tạo ra tác dụng quay?",
          "source": "10.1"
        },
        {
          "slug": "momen-luc-va-gia-toc-goc",
          "title": "Mômen lực và gia tốc góc",
          "question": "Tổng mômen lực quyết định gia tốc quay quanh trục cố định thế nào?",
          "source": "10.2"
        },
        {
          "slug": "quay-quanh-truc-chuyen-dong",
          "title": "Vật rắn quay quanh trục chuyển động",
          "question": "Kết hợp chuyển động khối tâm và chuyển động quay trong bài toán lăn ra sao?",
          "source": "10.3"
        },
        {
          "slug": "cong-va-cong-suat-quay",
          "title": "Công và công suất trong chuyển động quay",
          "question": "Lực làm vật quay truyền năng lượng với tốc độ nào?",
          "source": "10.4"
        },
        {
          "slug": "momen-dong-luong",
          "title": "Mômen động lượng",
          "question": "Mômen động lượng phụ thuộc gốc và phân bố vận tốc như thế nào?",
          "source": "10.5"
        },
        {
          "slug": "bao-toan-momen-dong-luong",
          "title": "Bảo toàn mômen động lượng",
          "question": "Khi nào thay đổi cấu hình làm vận tốc quay thay đổi mà mômen động lượng vẫn giữ nguyên?",
          "source": "10.6"
        },
        {
          "slug": "con-quay-va-tien-dong",
          "title": "Con quay và tiến động",
          "question": "Vì sao mômen trọng lực có thể đổi hướng trục quay thay vì làm con quay đổ ngay?",
          "source": "10.7"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "11-can-bang-dan-hoi",
  "title": "Cân bằng và đàn hồi",
  "prerequisites": [
    "luc",
    "momen-luc",
    "don-vi"
  ],
  "supportingConcepts": [
    "can-bang-co-hoc",
    "trong-tam-vat-ran",
    "ung-suat",
    "bien-dang-tuong-doi",
    "modun-young",
    "modun-khoi",
    "modun-truot",
    "gioi-han-dan-hoi"
  ],
  "status": "ready",
  "number": 11,
  "sourceChapter": 11,
  "topicGroups": [
    {
      "title": "Chuyển động quay và vật rắn",
      "topics": [
        {
          "slug": "dieu-kien-can-bang",
          "title": "Điều kiện cân bằng",
          "question": "Vì sao cân bằng lực chưa đủ để giữ vật rắn đứng yên?",
          "source": "11.1"
        },
        {
          "slug": "trong-tam",
          "title": "Trọng tâm",
          "question": "Khi nào có thể thay trọng lực phân bố bằng một lực đặt tại trọng tâm?",
          "source": "11.2"
        },
        {
          "slug": "giai-bai-toan-can-bang-vat-ran",
          "title": "Giải bài toán cân bằng vật rắn",
          "question": "Chọn vật, điểm tính mômen và lực liên kết như thế nào?",
          "source": "11.3"
        },
        {
          "slug": "ung-suat-bien-dang-modun",
          "title": "Ứng suất, biến dạng và môđun đàn hồi",
          "question": "Lực phân bố trên diện tích và sự biến dạng liên hệ ra sao?",
          "source": "11.4"
        },
        {
          "slug": "dan-hoi-va-deo",
          "title": "Đàn hồi và dẻo",
          "question": "Giới hạn tỉ lệ khác giới hạn đàn hồi thế nào?",
          "source": "11.5"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "12-co-hoc-chat-luu",
  "title": "Cơ học chất lưu",
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "don-vi",
    "dao-ham"
  ],
  "supportingConcepts": [
    "khoi-luong-rieng",
    "ty-khoi",
    "ap-suat-chat-luu",
    "nguyen-ly-pascal",
    "ap-suat-tuyet-doi-va-ap-suat-du",
    "luc-day-archimedes",
    "suc-cang-be-mat",
    "chat-luu-ly-tuong",
    "duong-dong-chat-luu",
    "phuong-trinh-lien-tuc",
    "phuong-trinh-bernoulli",
    "do-nhot-chat-luu",
    "chay-tang-va-chay-roi",
    "dong-nhot-trong-ong-tru",
    "ong-dong-chat-luu",
    "duong-di-phan-tu-chat-luu",
    "luu-luong-chat-luu"
  ],
  "status": "ready",
  "number": 12,
  "sourceChapter": 12,
  "topicGroups": [
    {
      "title": "Cơ học chất lưu",
      "topics": [
        {
          "slug": "chat-khi-chat-long-va-khoi-luong-rieng",
          "title": "Chất khí, chất lỏng và khối lượng riêng",
          "question": "Vì sao cùng một thể tích nhưng chất khí, chất lỏng và chất rắn có khối lượng khác nhau?",
          "source": "12.1"
        },
        {
          "slug": "ap-suat-trong-chat-luu",
          "title": "Áp suất trong chất lưu",
          "question": "Áp suất thay đổi theo độ sâu như thế nào và các dụng cụ đo áp suất hoạt động ra sao?",
          "source": "12.2"
        },
        {
          "slug": "luc-day-archimedes-va-suc-cang-be-mat",
          "title": "Lực đẩy Archimedes và sức căng bề mặt",
          "question": "Lực nào giữ vật nổi trong chất lưu, và vì sao một vật đặc hơn nước vẫn có thể nằm trên mặt nước?",
          "source": "12.3"
        },
        {
          "slug": "dong-chay-chat-luu",
          "title": "Dòng chảy chất lưu",
          "question": "Bảo toàn khối lượng liên hệ tiết diện, khối lượng riêng và tốc độ của dòng chảy như thế nào?",
          "source": "12.4"
        },
        {
          "slug": "phuong-trinh-bernoulli",
          "title": "Phương trình Bernoulli",
          "question": "Công của áp lực làm thay đổi tốc độ và độ cao của chất lưu như thế nào?",
          "source": "12.5"
        },
        {
          "slug": "do-nhot-va-chay-roi",
          "title": "Độ nhớt và chảy rối",
          "question": "Khi ma sát bên trong chất lưu và những nhiễu loạn dòng chảy trở nên đáng kể, mô hình lý tưởng thay đổi ra sao?",
          "source": "12.6"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "13-hap-dan",
  "title": "Hấp dẫn",
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "vector",
    "gia-toc-huong-tam",
    "momen-luc",
    "momen-dong-luong",
    "khoi-tam",
    "dao-ham",
    "tich-phan"
  ],
  "supportingConcepts": [
    "dinh-luat-van-vat-hap-dan",
    "the-nang-hap-dan",
    "toc-do-thoat",
    "quy-dao-ve-tinh",
    "dinh-luat-kepler",
    "luc-xuyen-tam",
    "dinh-ly-vo-cau",
    "trong-luong-bieu-kien",
    "ban-kinh-schwarzschild",
    "chan-troi-su-kien",
    "ho-den"
  ],
  "status": "ready",
  "number": 13,
  "sourceChapter": 13,
  "topicGroups": [
    {
      "title": "Hấp dẫn",
      "topics": [
        {
          "slug": "dinh-luat-van-vat-hap-dan",
          "title": "Định luật vạn vật hấp dẫn Newton",
          "question": "Hai vật có khối lượng hút nhau như thế nào và lực tổng hợp được tính ra sao?",
          "source": "13.1"
        },
        {
          "slug": "trong-luong",
          "title": "Trọng lượng",
          "question": "Trọng lượng và gia tốc trọng trường thay đổi theo thiên thể và độ cao như thế nào?",
          "source": "13.2"
        },
        {
          "slug": "the-nang-hap-dan",
          "title": "Thế năng hấp dẫn",
          "question": "Tính công, cơ năng và tốc độ thoát thế nào khi lực hấp dẫn thay đổi theo khoảng cách?",
          "source": "13.3"
        },
        {
          "slug": "chuyen-dong-ve-tinh",
          "title": "Chuyển động vệ tinh",
          "question": "Lực hấp dẫn xác định tốc độ, chu kỳ và cơ năng của vệ tinh trên quỹ đạo tròn ra sao?",
          "source": "13.4"
        },
        {
          "slug": "cac-dinh-luat-kepler-va-chuyen-dong-hanh-tinh",
          "title": "Các định luật Kepler và chuyển động hành tinh",
          "question": "Hình học quỹ đạo, diện tích quét và chu kỳ liên hệ với các định luật Newton như thế nào?",
          "source": "13.5"
        },
        {
          "slug": "phan-bo-khoi-luong-doi-xung-cau",
          "title": "Phân bố khối lượng đối xứng cầu",
          "question": "Vì sao vật đối xứng cầu có thể được thay bằng khối lượng ở tâm, và điều gì xảy ra bên trong vỏ cầu?",
          "source": "13.6"
        },
        {
          "slug": "trong-luong-bieu-kien-va-su-quay-trai-dat",
          "title": "Trọng lượng biểu kiến và sự quay của Trái Đất",
          "question": "Vì sao số chỉ của cân khác lực hấp dẫn thật khi vật cùng quay với Trái Đất?",
          "source": "13.7"
        },
        {
          "slug": "ho-den",
          "title": "Hố đen",
          "question": "Chân trời sự kiện có ý nghĩa gì và làm thế nào nhận biết hố đen qua chuyển động của vật lân cận?",
          "source": "13.8"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "14-dao-dong",
  "title": "Chuyển động tuần hoàn",
  "prerequisites": [
    "luc",
    "cong-nang-luong",
    "bao-toan-co-nang",
    "gia-toc-huong-tam",
    "momen-luc",
    "momen-quan-tinh",
    "dao-ham",
    "dong-luong-vat-ly"
  ],
  "supportingConcepts": [
    "dao-dong-dieu-hoa",
    "dao-dong-tat-dan",
    "cong-huong-co-hoc",
    "can-bang-co-hoc",
    "luc-can-tuyen-tinh",
    "khoi-luong-rut-gon",
    "chu-ky-va-tan-so-dao-dong",
    "tan-so-goc-dao-dong",
    "pha-dao-dong-co-hoc",
    "dao-dong-dieu-hoa-goc",
    "con-lac-don",
    "con-lac-vat-ly",
    "dao-dong-cuong-buc",
    "tat-dan-toi-han"
  ],
  "status": "ready",
  "number": 14,
  "sourceChapter": 14,
  "topicGroups": [
    {
      "title": "Chuyển động tuần hoàn",
      "topics": [
        {
          "slug": "mo-ta-dao-dong",
          "title": "Mô tả dao động",
          "question": "Biên độ, chu kỳ và tần số mô tả một dao động như thế nào?",
          "source": "14.1"
        },
        {
          "slug": "dao-dong-dieu-hoa",
          "title": "Dao động điều hòa",
          "question": "Lực phục hồi tuyến tính xác định li độ, vận tốc và gia tốc ra sao?",
          "source": "14.2"
        },
        {
          "slug": "co-nang-dao-dong-dieu-hoa",
          "title": "Cơ năng trong dao động điều hòa",
          "question": "Cơ năng và li độ liên hệ với tốc độ, biên độ như thế nào?",
          "source": "14.3"
        },
        {
          "slug": "ung-dung-dao-dong-dieu-hoa",
          "title": "Các ứng dụng của dao động điều hòa",
          "question": "Lò xo đứng, dao động xoắn và tương tác phân tử cùng dẫn tới mô hình điều hòa ra sao?",
          "source": "14.4"
        },
        {
          "slug": "con-lac-don",
          "title": "Con lắc đơn",
          "question": "Khi nào con lắc đơn gần điều hòa và chu kỳ thay đổi theo biên độ thế nào?",
          "source": "14.5"
        },
        {
          "slug": "con-lac-vat-ly",
          "title": "Con lắc vật lý",
          "question": "Phân bố khối lượng và trục treo quyết định chu kỳ của vật quay ra sao?",
          "source": "14.6"
        },
        {
          "slug": "dao-dong-tat-dan",
          "title": "Dao động tắt dần",
          "question": "Lực cản làm giảm cơ năng và phân chia các chế độ chuyển động thế nào?",
          "source": "14.7"
        },
        {
          "slug": "dao-dong-cuong-buc-va-cong-huong",
          "title": "Dao động cưỡng bức và cộng hưởng",
          "question": "Ngoại lực tuần hoàn và độ cản quyết định biên độ đáp ứng ra sao?",
          "source": "14.8"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "15-song-co",
  "title": "Sóng cơ",
  "prerequisites": [
    "dao-dong-dieu-hoa",
    "luc",
    "cong-nang-luong",
    "dao-ham",
    "dong-luong-vat-ly"
  ],
  "supportingConcepts": [
    "song-co-hoc",
    "buoc-song-co-hoc",
    "so-song",
    "ham-song-co-hoc",
    "toc-do-song-ngang-tren-day",
    "cong-suat-song-co",
    "cuong-do-song-co",
    "chong-chat-song-tuyen-tinh",
    "dieu-kien-bien-cua-day",
    "song-dung-co-hoc",
    "nut-va-bung-song",
    "dang-dao-dong-rieng-cua-day",
    "hoa-am-va-am-boi",
    "phan-tich-hoa-am-cua-day",
    "pha-song",
    "giao-thoa-song",
    "dao-ham-rieng"
  ],
  "status": "ready",
  "number": 15,
  "sourceChapter": 15,
  "topicGroups": [
    {
      "title": "Sóng cơ",
      "topics": [
        {
          "slug": "cac-loai-song-co",
          "title": "Các loại sóng cơ",
          "question": "Sóng truyền đi trong khi từng phần tử môi trường chuyển động như thế nào?",
          "source": "15.1"
        },
        {
          "slug": "song-tuan-hoan",
          "title": "Sóng tuần hoàn",
          "question": "Bước sóng, chu kỳ và tần số xác định tốc độ truyền ra sao?",
          "source": "15.2"
        },
        {
          "slug": "ham-song",
          "title": "Hàm sóng",
          "question": "Làm thế nào mô tả dạng sóng và dao động của từng phần tử bằng một hàm?",
          "source": "15.3"
        },
        {
          "slug": "toc-do-song-tren-day",
          "title": "Tốc độ sóng ngang trên dây",
          "question": "Lực căng và quán tính của dây quyết định tốc độ truyền thế nào?",
          "source": "15.4"
        },
        {
          "slug": "nang-luong-trong-chuyen-dong-song",
          "title": "Năng lượng trong chuyển động sóng",
          "question": "Biên độ, tần số và khoảng cách ảnh hưởng công suất và cường độ ra sao?",
          "source": "15.5"
        },
        {
          "slug": "giao-thoa-dieu-kien-bien-va-chong-chat",
          "title": "Giao thoa, điều kiện biên và chồng chất",
          "question": "Vì sao sóng phản xạ có thể đảo dấu, và hai sóng chồng nhau được cộng thế nào?",
          "source": "15.6"
        },
        {
          "slug": "song-dung-tren-day",
          "title": "Sóng dừng trên dây",
          "question": "Hai sóng chạy ngược chiều tạo nút, bụng và chuyển động tại chỗ ra sao?",
          "source": "15.7"
        },
        {
          "slug": "cac-dang-dao-dong-rieng-cua-day",
          "title": "Các dạng dao động riêng của dây",
          "question": "Hai đầu cố định chọn những tần số nào và vì sao dây đàn tạo nhiều họa âm?",
          "source": "15.8"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "16-am-hoc",
  "title": "Âm thanh và sự nghe",
  "prerequisites": [
    "cong-suat-co-hoc",
    "dong-luong-vat-ly",
    "modun-khoi",
    "modun-young",
    "ap-suat-tuyet-doi-va-ap-suat-du",
    "dao-dong-cuong-buc",
    "cong-huong-co-hoc",
    "song-co-hoc",
    "ham-song-co-hoc",
    "buoc-song-co-hoc",
    "so-song",
    "chong-chat-song-tuyen-tinh",
    "cuong-do-song-co",
    "dao-ham-rieng"
  ],
  "supportingConcepts": [
    "song-am",
    "ap-suat-am",
    "toc-do-truyen-am",
    "cuong-do-am",
    "muc-cuong-do-am",
    "cao-do-am",
    "am-sac",
    "song-dung-trong-cot-khi",
    "cong-huong-am",
    "phach",
    "hieu-ung-doppler-am",
    "doppler-dien-tu",
    "song-xung-kich",
    "so-mach",
    "tieng-no-vuot-am",
    "nut-va-bung-song",
    "hoa-am-va-am-boi"
  ],
  "status": "ready",
  "number": 16,
  "sourceChapter": 16,
  "topicGroups": [
    {
      "title": "Âm thanh và sự nghe",
      "topics": [
        {
          "slug": "song-am",
          "title": "Sóng âm",
          "question": "Li độ phần tử và biến thiên áp suất mô tả cùng một sóng âm như thế nào?",
          "source": "16.1"
        },
        {
          "slug": "toc-do-truyen-am",
          "title": "Tốc độ truyền âm",
          "question": "Cơ tính, khối lượng riêng và nhiệt độ quyết định tốc độ truyền ra sao?",
          "source": "16.2"
        },
        {
          "slug": "cuong-do-va-muc-cuong-do-am",
          "title": "Cường độ và mức cường độ âm",
          "question": "Biên độ áp suất, biên độ li độ và decibel liên hệ như thế nào?",
          "source": "16.3"
        },
        {
          "slug": "song-am-dung-va-cac-dang-rieng",
          "title": "Sóng âm dừng và các dạng dao động riêng",
          "question": "Điều kiện đầu ống chọn tần số và các nút, bụng của đại lượng nào?",
          "source": "16.4"
        },
        {
          "slug": "cong-huong-am",
          "title": "Cộng hưởng âm",
          "question": "Vì sao một cột khí hoặc dây đàn có thể rung mạnh do nguồn âm bên ngoài?",
          "source": "16.5"
        },
        {
          "slug": "giao-thoa-song-am",
          "title": "Giao thoa sóng âm",
          "question": "Pha và hiệu đường đi tạo các vùng âm mạnh, yếu như thế nào?",
          "source": "16.6"
        },
        {
          "slug": "phach",
          "title": "Phách",
          "question": "Hai tần số gần nhau tạo nhịp lớn nhỏ với tần số nào?",
          "source": "16.7"
        },
        {
          "slug": "hieu-ung-doppler",
          "title": "Hiệu ứng Doppler",
          "question": "Chuyển động của nguồn, người nghe và môi trường làm đổi tần số nhận thế nào?",
          "source": "16.8"
        },
        {
          "slug": "song-xung-kich",
          "title": "Sóng xung kích",
          "question": "Nguồn vượt âm tạo mặt nón và tiếng nổ tại người nghe như thế nào?",
          "source": "16.9"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "17-nhiet-do-nhiet-luong",
  "title": "Nhiệt độ và nhiệt",
  "prerequisites": [
    "don-vi",
    "cong-nang-luong",
    "luc"
  ],
  "supportingConcepts": [
    "can-bang-nhiet",
    "nguyen-ly-khong-nhiet-dong",
    "nhiet-do-tuyet-doi",
    "su-no-vi-nhiet",
    "nhiet-luong",
    "nhiet-dung-rieng",
    "nhiet-an-chuyen-pha",
    "dan-nhiet",
    "nhiet-tro",
    "doi-luu-nhiet",
    "buc-xa-nhiet"
  ],
  "status": "ready",
  "number": 17,
  "sourceChapter": 17,
  "topicGroups": [
    {
      "title": "Nhiệt học và nhiệt động lực học",
      "topics": [
        {
          "slug": "nhiet-do-va-can-bang-nhiet",
          "title": "Nhiệt độ và cân bằng nhiệt",
          "question": "Nhiệt kế đo đại lượng nào khi đạt cân bằng với vật?",
          "source": "17.1"
        },
        {
          "slug": "nhiet-ke-va-thang-nhiet-do",
          "title": "Nhiệt kế và các thang nhiệt độ",
          "question": "Các tính chất vật lý được dùng để xây dựng thang nhiệt độ thế nào?",
          "source": "17.2"
        },
        {
          "slug": "nhiet-ke-khi-va-thang-kelvin",
          "title": "Nhiệt kế khí và thang Kelvin",
          "question": "Giới hạn khí loãng dẫn tới thang nhiệt độ tuyệt đối ra sao?",
          "source": "17.3"
        },
        {
          "slug": "su-no-vi-nhiet",
          "title": "Sự nở vì nhiệt",
          "question": "Vì sao thay đổi nhiệt độ làm thay đổi kích thước và tạo ứng suất?",
          "source": "17.4"
        },
        {
          "slug": "nhiet-luong",
          "title": "Nhiệt lượng và nhiệt dung",
          "question": "Nhiệt lượng khác nhiệt độ và năng lượng chứa trong vật như thế nào?",
          "source": "17.5"
        },
        {
          "slug": "nhiet-luong-ke-va-chuyen-pha",
          "title": "Nhiệt lượng kế và chuyển pha",
          "question": "Cân bằng năng lượng thế nào khi các vật đổi nhiệt độ hoặc đổi pha?",
          "source": "17.6"
        },
        {
          "slug": "cac-co-che-truyen-nhiet",
          "title": "Các cơ chế truyền nhiệt",
          "question": "Dẫn nhiệt, đối lưu và bức xạ truyền năng lượng bằng cơ chế nào?",
          "source": "17.7"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "18-thuyet-dong-hoc-chat-khi",
  "title": "Tính chất nhiệt của vật chất",
  "prerequisites": [
    "nhiet-do-tuyet-doi",
    "cong-nang-luong",
    "dong-luong-vat-ly"
  ],
  "supportingConcepts": [
    "khi-ly-tuong",
    "phuong-trinh-van-der-waals",
    "phan-bo-maxwell",
    "nguyen-ly-phan-bo-deu-nang-luong",
    "quang-duong-tu-do-trung-binh",
    "diem-ba",
    "diem-toi-han-chat"
  ],
  "status": "ready",
  "number": 18,
  "sourceChapter": 18,
  "topicGroups": [
    {
      "title": "Nhiệt học và nhiệt động lực học",
      "topics": [
        {
          "slug": "phuong-trinh-trang-thai",
          "title": "Phương trình trạng thái",
          "question": "Áp suất, thể tích và nhiệt độ của chất khí được ràng buộc ra sao?",
          "source": "18.1"
        },
        {
          "slug": "tinh-chat-phan-tu-vat-chat",
          "title": "Tính chất phân tử của vật chất",
          "question": "Kích thước, tương tác và lượng chất liên hệ với đại lượng vĩ mô thế nào?",
          "source": "18.2"
        },
        {
          "slug": "mo-hinh-dong-hoc-khi-ly-tuong",
          "title": "Mô hình động học phân tử của khí lý tưởng",
          "question": "Va chạm phân tử tạo áp suất và nối nhiệt độ với động năng ra sao?",
          "source": "18.3"
        },
        {
          "slug": "nhiet-dung",
          "title": "Nhiệt dung và các bậc tự do",
          "question": "Vì sao nhiệt dung khí phụ thuộc cấu trúc phân tử và nhiệt độ?",
          "source": "18.4"
        },
        {
          "slug": "toc-do-phan-tu",
          "title": "Tốc độ phân tử",
          "question": "Tốc độ trung bình, hiệu dụng và có xác suất lớn nhất khác nhau thế nào?",
          "source": "18.5"
        },
        {
          "slug": "cac-pha-cua-vat-chat",
          "title": "Các pha của vật chất",
          "question": "Giản đồ pha cho biết gì về điểm ba và điểm tới hạn?",
          "source": "18.6"
        }
      ]
    }
  ],
  "hasChapterExercises": true
},
    {
  "slug": "19-nguyen-ly-thu-nhat",
  "title": "Nguyên lý thứ nhất của nhiệt động lực học",
  "prerequisites": [
    "khi-ly-tuong",
    "tich-phan",
    "nhiet-do-tuyet-doi",
    "cong-nang-luong"
  ],
  "supportingConcepts": [
    "he-nhiet-dong",
    "noi-nang",
    "cong-nhiet-dong",
    "qua-trinh-dang-nhiet",
    "qua-trinh-doan-nhiet",
    "nhiet-dung-dang-tich-dang-ap"
  ],
  "status": "ready",
  "number": 19,
  "sourceChapter": 19,
  "topicGroups": [
    {
      "title": "Nhiệt học và nhiệt động lực học",
      "topics": [
        {
          "slug": "he-nhiet-dong",
          "title": "Hệ nhiệt động",
          "question": "Chọn hệ và quy ước dấu cho năng lượng trao đổi thế nào?",
          "source": "19.1"
        },
        {
          "slug": "cong-khi-the-tich-thay-doi",
          "title": "Công khi thể tích thay đổi",
          "question": "Diện tích dưới đường quá trình trên đồ thị p–V biểu diễn đại lượng gì?",
          "source": "19.2"
        },
        {
          "slug": "duong-di-giua-cac-trang-thai",
          "title": "Đường đi giữa các trạng thái",
          "question": "Vì sao cùng hai trạng thái đầu cuối có thể cho công và nhiệt lượng khác nhau?",
          "source": "19.3"
        },
        {
          "slug": "noi-nang-va-nguyen-ly-thu-nhat",
          "title": "Nội năng và nguyên lý thứ nhất",
          "question": "Bảo toàn năng lượng được viết thế nào theo nội năng, nhiệt lượng và công?",
          "source": "19.4"
        },
        {
          "slug": "cac-qua-trinh-nhiet-dong",
          "title": "Các quá trình nhiệt động",
          "question": "Đẳng tích, đẳng áp, đẳng nhiệt và đoạn nhiệt khác nhau ở điều kiện nào?",
          "source": "19.5"
        },
        {
          "slug": "noi-nang-khi-ly-tuong",
          "title": "Nội năng của khí lý tưởng",
          "question": "Vì sao nội năng khí lý tưởng chỉ phụ thuộc nhiệt độ?",
          "source": "19.6"
        },
        {
          "slug": "nhiet-dung-khi-ly-tuong",
          "title": "Nhiệt dung của khí lý tưởng",
          "question": "Vì sao đun đẳng áp cần nhiều nhiệt lượng hơn đun đẳng tích?",
          "source": "19.7"
        },
        {
          "slug": "qua-trinh-doan-nhiet-khi-ly-tuong",
          "title": "Quá trình đoạn nhiệt của khí lý tưởng",
          "question": "Trong điều kiện nào áp suất và thể tích tuân theo định luật lũy thừa?",
          "source": "19.8"
        }
      ]
    }
  ],
  "hasChapterExercises": true
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
    "dong-co-nhiet",
    "hieu-suat-nhiet",
    "he-so-lam-lanh",
    "chu-trinh-carnot",
    "entropy-nhiet-dong",
    "qua-trinh-thuan-nghich",
    "so-trang-thai-vi-mo"
  ],
  "status": "ready",
  "number": 20,
  "sourceChapter": 20,
  "topicGroups": [
    {
      "title": "Nhiệt học và nhiệt động lực học",
      "topics": [
        {
          "slug": "chieu-cua-qua-trinh-nhiet-dong",
          "title": "Chiều của quá trình nhiệt động",
          "question": "Vì sao bảo toàn năng lượng chưa xác định được chiều diễn biến?",
          "source": "20.1"
        },
        {
          "slug": "dong-co-nhiet",
          "title": "Động cơ nhiệt",
          "question": "Động cơ nhận nhiệt, sinh công và thải nhiệt trong một chu trình ra sao?",
          "source": "20.2"
        },
        {
          "slug": "dong-co-dot-trong",
          "title": "Động cơ đốt trong",
          "question": "Mô hình Otto và Diesel liên hệ các quá trình nhiệt động như thế nào?",
          "source": "20.3"
        },
        {
          "slug": "may-lanh",
          "title": "Máy lạnh và bơm nhiệt",
          "question": "Công cấp vào giúp chuyển nhiệt từ nguồn lạnh lên nguồn nóng thế nào?",
          "source": "20.4"
        },
        {
          "slug": "nguyen-ly-thu-hai",
          "title": "Nguyên lý thứ hai",
          "question": "Các phát biểu Kelvin–Planck và Clausius tương đương về giới hạn nào?",
          "source": "20.5"
        },
        {
          "slug": "chu-trinh-carnot",
          "title": "Chu trình Carnot",
          "question": "Vì sao nhiệt độ hai nguồn đặt giới hạn cho hiệu suất?",
          "source": "20.6"
        },
        {
          "slug": "entropy",
          "title": "Entropy",
          "question": "Làm thế nào tính độ biến thiên entropy của một quá trình không thuận nghịch?",
          "source": "20.7"
        },
        {
          "slug": "giai-thich-vi-mo-entropy",
          "title": "Giải thích vi mô của entropy",
          "question": "Số trạng thái vi mô liên hệ với entropy và chiều diễn biến thế nào?",
          "source": "20.8"
        }
      ]
    }
  ],
  "hasChapterExercises": true
}
  ],
  "slides": [
  {
    "note": "02-chuyen-dong-thang",
    "title": "Vận tốc biểu diễn sự thay đổi vị trí",
    "bullets": [
      "Độ dời có dấu, phụ thuộc vị trí đầu và vị trí cuối.",
      "Vận tốc tức thời là đạo hàm của tọa độ theo thời gian.",
      "Tốc độ tức thời là độ lớn vận tốc."
    ],
    "formula": "$$\nv_x=\\frac{dx}{dt}\n$$"
  },
  {
    "note": "02-chuyen-dong-thang",
    "title": "Gia tốc không đổi cho các hệ thức động học",
    "bullets": [
      "Gia tốc là đạo hàm của vận tốc theo thời gian.",
      "Dùng hệ thức dưới đây khi gia tốc không đổi trong toàn bộ khoảng xét, với thời điểm đầu bằng không.",
      "Đối với rơi tự do, phải chọn chiều trục và dấu gia tốc trọng trường nhất quán."
    ],
    "formula": "$$\nx=x_0+v_{0x}t+\\tfrac12a_xt^2\n$$"
  },
  {
    "note": "02-chuyen-dong-thang",
    "title": "Tích phân khôi phục độ dời từ vận tốc",
    "bullets": [
      "Độ dời bằng tích phân có dấu của vận tốc theo thời gian.",
      "Diện tích dưới đồ thị vận tốc có thể dương hoặc âm.",
      "Khi gia tốc thay đổi, tích phân gia tốc để tìm độ biến thiên vận tốc trước khi tìm vị trí."
    ],
    "formula": "$$\nx_2-x_1=\\int_{t_1}^{t_2}v_x(t)\\,dt\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Tọa độ góc và độ dời góc",
    "bullets": [
      "Góc tính bằng radian.",
      "Độ dời góc là đại lượng có dấu, còn quãng đường trên cung tròn không âm."
    ],
    "formula": "$$\n\\Delta\\theta=\\theta_2-\\theta_1\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Vận tốc góc",
    "bullets": [
      "Chọn chiều dương quanh trục trước khi xác định dấu.",
      "Tốc độ góc là độ lớn vận tốc góc."
    ],
    "formula": "$$\n\\omega_{\\mathrm{av},z}=\\Delta\\theta/\\Delta t\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Gia tốc góc",
    "bullets": [
      "Gia tốc góc biểu diễn sự thay đổi vận tốc góc.",
      "Đơn vị là rad/s²."
    ],
    "formula": "$$\n\\alpha_z=d\\omega_z/dt\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Gia tốc góc không đổi",
    "bullets": [
      "Các hệ thức sau áp dụng trong cùng một khoảng có gia tốc góc không đổi.",
      "Thời điểm đầu lấy bằng không."
    ],
    "formula": "$$\n\\omega_z=\\omega_{0z}+\\alpha_zt\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Vận tốc và gia tốc",
    "bullets": [
      "Khoảng r là khoảng cách vuông góc từ điểm đến trục cố định.",
      "Hai thành phần gia tốc tiếp tuyến và hướng tâm vuông góc nhau."
    ],
    "formula": "$$\nv=r|\\omega_z|\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Mômen quán tính",
    "bullets": [
      "Mômen quán tính phụ thuộc vật và trục.",
      "Các rᵢ là khoảng cách đến trục, không nhất thiết là khoảng cách đến gốc."
    ],
    "formula": "$$\nI=m_1r_1^2+m_2r_2^2+m_3r_3^2\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Động năng quay",
    "bullets": [
      "Vật rắn quay quanh trục cố định, với mọi điểm có cùng vận tốc góc.",
      "Bán kính quán tính:\n\n$$\nk=\\sqrt{I/M}\n$$"
    ],
    "formula": "$$\nK=\\tfrac12I\\omega_z^2\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Định lý trục song song",
    "bullets": [
      "Một trục phải đi qua khối tâm.",
      "Trục thứ hai song song và cách nó một khoảng d."
    ],
    "formula": "$$\nI=I_{\\mathrm{cm}}+Md^2\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Thanh mảnh đồng chất",
    "bullets": [
      "Trục vuông góc chiều dài L.",
      "M là khối lượng thanh."
    ],
    "formula": "$$\nI_{\\mathrm{cm}}=ML^2/12\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Các vật tròn đối xứng",
    "bullets": [
      "Trục qua tâm và là trục đối xứng tương ứng.",
      "Các vật đồng chất."
    ],
    "formula": "$$\nI=MR^2\n$$"
  },
  {
    "note": "09-dong-hoc-vat-ran",
    "title": "Tấm chữ nhật đồng chất",
    "bullets": [
      "Trục qua tâm, vuông góc mặt tấm cạnh a và b.",
      "Nếu đổi vị trí hoặc hướng của trục, phải tính lại mômen quán tính theo trục mới."
    ],
    "formula": "$$\nI=M(a^2+b^2)/12\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Khí lý tưởng",
    "bullets": [
      "Các phân tử có thể coi là chất điểm, tương tác giữa các va chạm được bỏ qua. n là số mol, N là số phân tử.",
      "Liên hệ lượng chất:\n\n$$\nN=nN_A\n$$"
    ],
    "formula": "$$\npV=nRT\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Khí thực theo van der Waals",
    "bullets": [
      "a và b là các hằng số đặc trưng cho chất khí trong mô hình hiệu dụng. p* là áp suất đã hiệu chỉnh lực hút, V* là thể tích đã hiệu chỉnh kích thước phân tử.",
      "Phương trình trạng thái:\n\n$$\np_*V_*=nRT\n$$"
    ],
    "formula": "$$\np_*=p+an^2/V^2\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Động năng tịnh tiến",
    "bullets": [
      "Cân bằng nhiệt, khí cổ điển lý tưởng và chuyển động đẳng hướng. m là khối lượng một phân tử.",
      "Áp suất động học:\n\n$$\npV=\\tfrac13Nm\\langle v^2\\rangle\n$$"
    ],
    "formula": "$$\n\\langle K_{\\mathrm{tr}}\\rangle=\\tfrac32k_BT\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Phân bố đều năng lượng",
    "bullets": [
      "Mỗi số hạng bậc hai độc lập đang hoạt động trong giới hạn cổ điển đóng góp năng lượng trung bình bằng một nửa kBT trên mỗi phân tử.",
      "Lượng tử hóa có thể làm một số bậc tự do quay hoặc dao động chưa đóng góp theo giá trị cổ điển."
    ],
    "formula": "$$\nC_V=fR/2\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Quãng đường tự do trung bình",
    "bullets": [
      "Mô hình các phân tử cầu cứng đường kính d, khí loãng có mật độ số nN.",
      "Quãng đường tự do:\n\n$$\n\\ell=1/(\\sqrt2\\pi d^2n_N)\n$$"
    ],
    "formula": "$$\nn_N=N/V\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Các tốc độ đặc trưng",
    "bullets": [
      "Khí lý tưởng có phân bố Maxwell ở cân bằng nhiệt.",
      "Khối lượng m là của một phân tử."
    ],
    "formula": "$$\nv_{\\mathrm{mp}}=\\sqrt{2k_BT/m}\n$$"
  },
  {
    "note": "18-thuyet-dong-hoc-chat-khi",
    "title": "Phân bố Maxwell",
    "bullets": [
      "f(v)dv là phần phân tử có tốc độ trong khoảng từ v đến v+dv, với v không âm.",
      "Các ký hiệu C và b được định nghĩa trong các dòng dưới."
    ],
    "formula": "$$\nC=4\\pi[m/(2\\pi k_BT)]^{3/2}\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Quy ước dấu",
    "bullets": [
      "Q dương khi hệ nhận nhiệt.",
      "W dương khi hệ thực hiện công lên môi trường."
    ],
    "formula": "$$\n\\Delta U=Q-W\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Công biến đổi thể tích",
    "bullets": [
      "Quá trình đủ chậm để dùng áp suất cân bằng p của hệ cho công biên.",
      "Khi giãn nở không cân bằng, phải xét áp suất ngoài phù hợp."
    ],
    "formula": "$$\nW=\\int_{V_1}^{V_2}p\\,dV\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Điều kiện quá trình",
    "bullets": [
      "Đẳng tích giữ V không đổi.",
      "Đẳng áp giữ p không đổi.",
      "Đẳng nhiệt giữ T không đổi.",
      "Đoạn nhiệt không trao đổi nhiệt."
    ],
    "formula": "$$\nW=0\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Nội năng khí lý tưởng",
    "bullets": [
      "Lượng khí và thành phần không đổi.",
      "CV có thể coi không đổi trên khoảng nhiệt độ đang xét."
    ],
    "formula": "$$\n\\Delta U=nC_V\\Delta T\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Nhiệt dung mol",
    "bullets": [
      "Khí lý tưởng có cùng thành phần, trong cùng miền nhiệt độ xét.",
      "Tỉ số nhiệt dung:\n\n$$\n\\gamma=C_p/C_V\n$$"
    ],
    "formula": "$$\nC_p-C_V=R\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Giãn nở đẳng nhiệt khí lý tưởng",
    "bullets": [
      "Quá trình thuận nghịch hoặc gần tĩnh, T không đổi và lượng khí không đổi.",
      "Biến thiên nội năng:\n\n$$\n\\Delta U=0\n$$"
    ],
    "formula": "$$\nW=nRT\\ln(V_2/V_1)\n$$"
  },
  {
    "note": "19-nguyen-ly-thu-nhat",
    "title": "Định luật đoạn nhiệt",
    "bullets": [
      "Chỉ áp dụng cho khí lý tưởng, quá trình đoạn nhiệt thuận nghịch hoặc gần tĩnh phù hợp, với nhiệt dung và gamma coi không đổi.",
      "Công do khí thực hiện:\n\n$$\nW=\\frac{p_1V_1-p_2V_2}{\\gamma-1}\n$$"
    ],
    "formula": "$$\npV^\\gamma=\\mathrm{const}\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Mômen lực",
    "bullets": [
      "Vector vị trí tính từ gốc đã chọn đến điểm đặt lực.",
      "Cánh tay đòn là khoảng cách từ gốc đến giá lực."
    ],
    "formula": "$$\n\\vec\\tau=\\vec r\\times\\vec F\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Vật rắn quay quanh trục cố định",
    "bullets": [
      "Dùng thành phần mômen ngoại lực và mômen quán tính đối với cùng trục cố định trong hệ quán tính.",
      "Dấu của gia tốc góc theo trục được quyết định bởi tổng mômen lực có dấu theo chính trục đó."
    ],
    "formula": "$$\n\\sum\\tau_z=I_z\\alpha_z\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Động năng vật rắn",
    "bullets": [
      "Tách động năng chuyển động của khối tâm và động năng quay quanh trục qua khối tâm.",
      "Vận tốc khối tâm và vận tốc góc mô tả hai phần của cùng chuyển động vật rắn."
    ],
    "formula": "$$\nK=\\tfrac12Mv_{\\mathrm{cm}}^2+\\tfrac12I_{\\mathrm{cm}}\\omega^2\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Lăn không trượt",
    "bullets": [
      "Quan hệ độ lớn này áp dụng tại tiếp xúc với mặt phẳng đứng yên.",
      "Dấu các thành phần phụ thuộc quy ước trục."
    ],
    "formula": "$$\nv_{\\mathrm{cm}}=R\\omega\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Lăn xuống mặt nghiêng",
    "bullets": [
      "Vật tròn lăn không trượt dưới trọng lực, không có lực hay mômen ngoài bổ sung.",
      "Ma sát phải đủ giữ điều kiện lăn."
    ],
    "formula": "$$\na_{\\mathrm{cm}}=\\frac{g\\sin\\beta}{1+I_{\\mathrm{cm}}/(MR^2)}\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Công và công suất quay",
    "bullets": [
      "Trục cố định.",
      "Công phụ thuộc góc và mômen lực tác dụng trong suốt quá trình."
    ],
    "formula": "$$\nW=\\int_{\\theta_1}^{\\theta_2}\\tau_z\\,d\\theta\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Mômen động lượng",
    "bullets": [
      "Gốc tính mômen phải được xác định.",
      "Với gốc cố định trong hệ quán tính, tổng mômen ngoại lực bằng tốc độ đổi mômen động lượng."
    ],
    "formula": "$$\n\\vec L=\\vec r\\times\\vec p\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Bảo toàn mômen động lượng",
    "bullets": [
      "Tổng mômen ngoại lực đối với gốc xét bằng không.",
      "Bảo toàn mômen động lượng không kéo theo bảo toàn động năng."
    ],
    "formula": "$$\n\\vec L_i=\\vec L_f\n$$"
  },
  {
    "note": "10-dong-luc-hoc-quay",
    "title": "Tiến động đều chậm",
    "bullets": [
      "Con quay đối xứng quay nhanh, trục nghiêng và đầu tựa cố định.",
      "Hệ thức là gần đúng khi mômen động lượng chủ yếu do quay quanh trục đối xứng."
    ],
    "formula": "$$\n\\Omega=Mgr/(I\\omega)\n$$"
  },
  {
    "note": "11-can-bang-dan-hoi",
    "title": "Điều kiện cân bằng tĩnh",
    "bullets": [
      "Vật ban đầu đứng yên trong hệ quán tính.",
      "Hợp lực và tổng mômen ngoại lực cùng bằng không."
    ],
    "formula": "$$\n\\sum\\vec F=\\vec0\n$$"
  },
  {
    "note": "11-can-bang-dan-hoi",
    "title": "Trọng tâm trong trường đều",
    "bullets": [
      "Khi gia tốc trọng trường cùng hướng và cùng độ lớn trong toàn vật, trọng tâm trùng khối tâm.",
      "Trong trường không đều, cần phân biệt khối tâm với điểm đặt tương đương của trọng lực."
    ],
    "formula": "$$\nx_{\\mathrm{cm}}=\\frac{\\sum_{i=1}^{n}m_ix_i}{M}\n$$"
  },
  {
    "note": "11-can-bang-dan-hoi",
    "title": "Ma sát nghỉ",
    "bullets": [
      "Lực ma sát tự điều chỉnh trong giới hạn.",
      "Chỉ đạt dấu bằng ở ngưỡng trượt."
    ],
    "formula": "$$\nf_s\\le\\mu_sN\n$$"
  },
  {
    "note": "11-can-bang-dan-hoi",
    "title": "Kéo và nén",
    "bullets": [
      "F⊥ là độ lớn lực pháp tuyến trên tiết diện A.",
      "Công thức môđun áp dụng trong miền tỉ lệ tuyến tính."
    ],
    "formula": "$$\n\\sigma=F_\\perp/A\n$$"
  },
  {
    "note": "11-can-bang-dan-hoi",
    "title": "Nén thể tích",
    "bullets": [
      "Áp suất tăng làm thể tích giảm đối với vật liệu ổn định thông thường.",
      "Dấu trừ làm môđun khối dương."
    ],
    "formula": "$$\nB=-\\Delta p/(\\Delta V/V_0)\n$$"
  },
  {
    "note": "11-can-bang-dan-hoi",
    "title": "Trượt",
    "bullets": [
      "Lực tiếp tuyến phân bố trên diện tích A làm hai mặt lệch nhau. x/h là biến dạng trượt góc nhỏ.",
      "Biến dạng trượt mô tả thay đổi hình dạng, còn nén đều từ mọi phía mô tả biến đổi thể tích."
    ],
    "formula": "$$\nS=\\frac{F_\\parallel/A}{x/h}\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Nguyên lý không",
    "bullets": [
      "Nếu hai hệ cùng cân bằng nhiệt với một hệ thứ ba thì chúng cân bằng nhiệt với nhau.",
      "Nhiệt độ là đại lượng xác định điều kiện cân bằng nhiệt."
    ],
    "formula": ""
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Đổi thang nhiệt độ",
    "bullets": [
      "Trong các công thức sau, tF và tC là các số đo theo độ Fahrenheit và độ Celsius.",
      "T là số đo theo kelvin."
    ],
    "formula": "$$\nt_F=\\tfrac95t_C+32\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Thang Kelvin",
    "bullets": [
      "Kelvin là đơn vị nhiệt độ nhiệt động lực học.",
      "Nhiệt kế khí thể tích không đổi trong giới hạn khí loãng cho quan hệ áp suất tỉ lệ nhiệt độ tuyệt đối."
    ],
    "formula": "$$\nT_2/T_1=p_2/p_1\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Nở dài và nở thể tích",
    "bullets": [
      "Biến thiên nhiệt độ đủ nhỏ để hệ số nở có thể coi không đổi.",
      "Vật nở tự do, không chịu cản trở cơ học."
    ],
    "formula": "$$\n\\Delta L=\\alpha L_0\\Delta T\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Ứng suất nhiệt",
    "bullets": [
      "Thanh bị giữ không đổi chiều dài trong miền đàn hồi tuyến tính.",
      "Dấu ứng suất theo quy ước kéo dương."
    ],
    "formula": "$$\n\\sigma=-Y\\alpha\\Delta T\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Nhiệt lượng khi đổi nhiệt độ",
    "bullets": [
      "Không chuyển pha. c hoặc C có thể coi không đổi trong khoảng khảo sát.",
      "Nhiệt lượng dương khi hệ nhận năng lượng bằng truyền nhiệt."
    ],
    "formula": "$$\nQ=mc\\Delta T\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Ẩn nhiệt",
    "bullets": [
      "Chuyển pha ở điều kiện xác định.",
      "L là ẩn nhiệt trên một đơn vị khối lượng.",
      "Dấu Q phụ thuộc chiều chuyển pha."
    ],
    "formula": "$$\n|Q|=mL\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Nhiệt lượng kế cách nhiệt",
    "bullets": [
      "Chọn toàn bộ các vật trao đổi nhiệt làm hệ.",
      "Không có công ngoài đáng kể và không thất thoát nhiệt ra môi trường."
    ],
    "formula": "$$\nQ_1+Q_2+\\cdots+Q_n=0\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Dẫn nhiệt ổn định qua bản phẳng",
    "bullets": [
      "Vật đồng nhất, tiết diện A, chiều dài dẫn L.",
      "Hai đầu giữ ở nhiệt độ Th lớn hơn Tc.",
      "H là độ lớn dòng nhiệt."
    ],
    "formula": "$$\nH=kA(T_h-T_c)/L\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Các lớp nối tiếp",
    "bullets": [
      "Dòng nhiệt ổn định đi qua lần lượt các lớp, không có nguồn nhiệt ở nút nối và không thất thoát ngang.",
      "Chênh lệch nhiệt độ của từng lớp tỉ lệ nhiệt trở của lớp khi các lớp truyền cùng dòng nhiệt."
    ],
    "formula": "$$\nR=R_1+R_2+\\cdots+R_n\n$$"
  },
  {
    "note": "17-nhiet-do-nhiet-luong",
    "title": "Bức xạ nhiệt",
    "bullets": [
      "Nhiệt độ tính bằng kelvin. e là hệ số phát xạ.",
      "Hệ thức trao đổi ròng xét vật nhỏ trong môi trường bao quanh lớn ở nhiệt độ Ts."
    ],
    "formula": "$$\nP=e\\sigma AT^4\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Cân bằng một chu trình động cơ",
    "bullets": [
      "Qh là nhiệt nhận từ nguồn nóng, Qc là độ lớn nhiệt thải cho nguồn lạnh.",
      "W là công có ích trong một chu trình."
    ],
    "formula": "$$\nW=Q_h-Q_c\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Máy lạnh",
    "bullets": [
      "Qc là nhiệt lấy từ nguồn lạnh, W là công cấp vào, Qh là nhiệt tỏa cho nguồn nóng.",
      "Hệ số bơm nhiệt:\n\n$$\nK_h=Q_h/W\n$$"
    ],
    "formula": "$$\nQ_h=Q_c+W\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Chu trình Otto lý tưởng",
    "bullets": [
      "Khí lý tưởng với gamma không đổi. r là tỉ số thể tích lớn nhất trên thể tích nhỏ nhất.",
      "Tỉ số nén là một tham số của mô hình chu trình, còn gamma phụ thuộc mô hình nhiệt dung của môi chất."
    ],
    "formula": "$$\ne=1-r^{1-\\gamma}\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Nguyên lý thứ hai",
    "bullets": [
      "Không có động cơ tuần hoàn chỉ nhận nhiệt từ một nguồn rồi biến toàn bộ thành công.",
      "Không có quá trình mà kết quả duy nhất là chuyển nhiệt từ vật lạnh sang vật nóng."
    ],
    "formula": ""
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Động cơ thuận nghịch hai nguồn",
    "bullets": [
      "Th lớn hơn Tc và cả hai là nhiệt độ tuyệt đối.",
      "Nguồn có nhiệt độ không đổi."
    ],
    "formula": "$$\nQ_c/Q_h=T_c/T_h\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Máy lạnh Carnot",
    "bullets": [
      "Máy lạnh thuận nghịch làm việc giữa đúng hai nguồn ở nhiệt độ tuyệt đối Th và Tc.",
      "Chênh lệch nhiệt độ hai nguồn càng nhỏ thì hệ số làm lạnh thuận nghịch càng lớn."
    ],
    "formula": "$$\nK_C=T_c/(T_h-T_c)\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Độ biến thiên entropy",
    "bullets": [
      "Tính theo một đường thuận nghịch nối cùng hai trạng thái cân bằng.",
      "Không thay nhiệt thực của một đường không thuận nghịch vào công thức này."
    ],
    "formula": "$$\n\\Delta S=\\int_i^f\\frac{\\delta Q_{\\mathrm{rev}}}{T}\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Hệ cô lập và toàn thể",
    "bullets": [
      "Tổng entropy của hệ cô lập không giảm.",
      "Dấu bằng ứng với quá trình thuận nghịch trong mô hình xét."
    ],
    "formula": "$$\n\\Delta S_{\\mathrm{tot}}\\ge0\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Khí lý tưởng",
    "bullets": [
      "Lượng khí không đổi, CV có thể coi không đổi.",
      "Hai dòng đóng góp cộng lại thành độ biến thiên entropy."
    ],
    "formula": "$$\n\\Delta S_T=nC_V\\ln(T_2/T_1)\n$$"
  },
  {
    "note": "20-nguyen-ly-thu-hai-entropy",
    "title": "Diễn giải thống kê",
    "bullets": [
      "Omega là số trạng thái vi mô tương thích với trạng thái vĩ mô trong mô hình các trạng thái vi mô đồng xác suất.",
      "Entropy cộng được khi số trạng thái vi mô của hai hệ độc lập nhân với nhau."
    ],
    "formula": "$$\nS=k_B\\ln\\Omega\n$$"
  },
  {
    "note": "04-dinh-luat-newton",
    "title": "Lực và hợp lực",
    "bullets": [
      "Đại lượng vector định lượng tương tác. Lực pháp tuyến vuông góc mặt tiếp xúc, ma sát song song mặt tiếp xúc, lực căng kéo dọc dây. Trọng lực có thể tác dụng không qua tiếp xúc.",
      "Tổng vector của mọi ngoại lực tác dụng lên cùng vật. Tổng thành phần theo mỗi trục được tính đại số, giữ đúng dấu."
    ],
    "formula": "$$\n\\vec R=\\vec F_1+\\vec F_2+\\vec F_3\n$$"
  },
  {
    "note": "04-dinh-luat-newton",
    "title": "Hệ quán tính và định luật thứ nhất",
    "bullets": [
      "Hệ mà định luật thứ nhất đúng. Một hệ chuyển động tịnh tiến với vận tốc không đổi so với một hệ quán tính cũng là hệ quán tính.",
      "Vận tốc không đổi, có thể bằng không, khi tổng ngoại lực bằng không. Điều kiện này không tự thay thế điều kiện cân bằng quay của vật rắn."
    ],
    "formula": "$$\n\\sum_{i=1}^{n}\\vec F_i=\\vec0\n$$"
  },
  {
    "note": "04-dinh-luat-newton",
    "title": "Khối lượng và định luật thứ hai",
    "bullets": [
      "Đại lượng đo quán tính, có tính cộng trong cơ học Newton. Cùng một hợp lực tạo gia tốc tỉ lệ nghịch khối lượng.",
      "Dạng dưới đây áp dụng trong hệ quán tính khi khối lượng vật hoặc hệ không đổi. Chỉ ngoại lực lên hệ đã chọn được đưa vào tổng.",
      "Trong hệ SI, khối lượng dùng kilôgam và gia tốc dùng mét trên giây bình phương."
    ],
    "formula": "$$\nm_2/m_1=a_1/a_2\n$$"
  },
  {
    "note": "04-dinh-luat-newton",
    "title": "Trọng lượng",
    "bullets": [
      "Lực hấp dẫn tác dụng lên vật. Giá trị phụ thuộc trường trọng lực tại vị trí vật, còn khối lượng không đổi khi chỉ chuyển vật đến nơi khác."
    ],
    "formula": "$$\nw=mg\n$$"
  },
  {
    "note": "04-dinh-luat-newton",
    "title": "Cặp lực tương tác và sơ đồ lực",
    "bullets": [
      "Hai lực của cùng tương tác có cùng độ lớn, ngược hướng và tác dụng lên hai vật khác nhau. Ký hiệu A/B chỉ lực do A tác dụng lên B.",
      "Trong mô hình dây thẳng không khối lượng, chỉ chịu các lực dọc dây ở hai đầu, lực căng ở hai đầu bằng nhau. Kết quả cũng đúng cho dây cân bằng khi không có lực phân bố dọc dây.",
      "Biểu diễn riêng mọi ngoại lực tác dụng lên vật đã chọn. Không đưa lực vật tác dụng lên môi trường vào sơ đồ ấy. Các vật khác nhau có sơ đồ riêng."
    ],
    "formula": "$$\n\\vec F_{A/B}=-\\vec F_{B/A}\n$$"
  },
  {
    "note": "07-the-nang-bao-toan-co-nang",
    "title": "Thế năng trọng trường",
    "bullets": [
      "Trong miền gia tốc trọng trường không đổi, trục y hướng lên. Thế năng của hệ vật–Trái Đất phụ thuộc mốc, còn hiệu thế năng không phụ thuộc hằng số cộng.",
      "Động năng và thế năng phải được tính trong cùng hệ quy chiếu và theo cùng quy ước mốc."
    ],
    "formula": "$$\nU_g=mgy\n$$"
  },
  {
    "note": "07-the-nang-bao-toan-co-nang",
    "title": "Thế năng đàn hồi",
    "bullets": [
      "Định luật Hooke trong miền tuyến tính, x tính từ chiều dài tự nhiên. Chọn thế năng bằng không khi lò xo không biến dạng.",
      "Bỏ qua động năng lò xo khi khối lượng lò xo nhỏ so với vật. Công của lực khác bằng độ biến thiên cơ năng."
    ],
    "formula": "$$\nF_x=-kx\n$$"
  },
  {
    "note": "07-the-nang-bao-toan-co-nang",
    "title": "Lực bảo toàn và nội năng",
    "bullets": [
      "Công giữa hai điểm không phụ thuộc đường đi, tương đương công trên mọi đường kín trong miền xét bằng không. Có thể biểu diễn công bằng độ giảm thế năng.",
      "Với lực ma sát có độ lớn không đổi, công ma sát trên vật là âm. Khi hệ chỉ chuyển hóa cơ năng thành nội năng và không trao đổi năng lượng ra ngoài, tổng các dạng năng lượng được bảo toàn."
    ],
    "formula": "$$\n\\oint\\vec F\\cdot d\\vec l=0\n$$"
  },
  {
    "note": "07-the-nang-bao-toan-co-nang",
    "title": "Lực và thế năng",
    "bullets": [
      "Lực phụ thuộc độ dốc thế năng, không phụ thuộc dấu hoặc hằng số cộng của thế năng.",
      "Mỗi đạo hàm riêng giữ các tọa độ còn lại cố định. Gradient hướng tăng thế năng nhanh nhất tại điểm xét, lực bảo toàn hướng ngược lại."
    ],
    "formula": "$$\nF_x=-\\frac{dU}{dx}\n$$"
  },
  {
    "note": "07-the-nang-bao-toan-co-nang",
    "title": "Đồ thị năng lượng và cân bằng",
    "bullets": [
      "Với cơ năng bảo toàn, chuyển động chỉ xảy ra trong miền động năng không âm. Tại một biên miền có lực khác không, vận tốc bằng không rồi đổi chiều.",
      "Trong một chiều, cân bằng bền ở cực tiểu địa phương và không bền ở cực đại. Dấu đạo hàm bậc hai là điều kiện đủ tại điểm dừng không suy biến. Khi đạo hàm bậc hai bằng không, phải xét thêm hình dạng của thế năng."
    ],
    "formula": "$$\nK=E-U(x)\n$$"
  },
  {
    "note": "06-cong-dong-nang",
    "title": "Công của lực không đổi",
    "bullets": [
      "Áp dụng cho lực không đổi tác dụng lên chất điểm chuyển động thẳng với độ dời xác định.",
      "Với lực không đổi có độ lớn dương và độ dời khác không, dấu của công bằng dấu cosin góc giữa lực và độ dời.",
      "Tổng công bằng tổng đại số công của các lực. Với các lực không đổi trên cùng độ dời thẳng, có thể tính bằng hợp lực.",
      "Trong SI, công và động năng cùng đo bằng joule."
    ],
    "formula": "$$\nW = \\vec F \\cdot \\vec s = Fs\\cos\\phi\n$$"
  },
  {
    "note": "06-cong-dong-nang",
    "title": "Động năng và định lý công–động năng",
    "bullets": [
      "Năng lượng chuyển động của chất điểm khối lượng dương, không đổi trong cơ học Newton. Động năng không âm và phụ thuộc hệ quy chiếu.",
      "Độ biến thiên động năng của chất điểm bằng tổng công của tất cả các ngoại lực tác dụng lên nó trong hệ quy chiếu quán tính."
    ],
    "formula": "$$\nK = \\frac{1}{2}mv^2\n$$"
  },
  {
    "note": "06-cong-dong-nang",
    "title": "Công của lực biến đổi và chuyển động cong",
    "bullets": [
      "Chất điểm chuyển động thẳng dọc theo trục x từ vị trí x1 đến x2 dưới tác dụng của lực biến đổi Fx(x).",
      "Định luật Hooke trong miền biến dạng tuyến tính. Độ biến dạng x tính từ chiều dài tự nhiên. Lực ngoài kx giữ cân bằng đầu lò xo hoặc kéo, nén chậm.",
      "Công của lực ngoài khi biến dạng chậm lò xo lý tưởng. Công của lò xo lên vật chuyển động có dấu ngược lại.",
      "Công trên một đường đi xác định là tích phân của thành phần lực theo tiếp tuyến, lấy theo chiều chuyển động."
    ],
    "formula": "$$\nW = \\int_{x_1}^{x_2} F_x\\,dx\n$$"
  },
  {
    "note": "06-cong-dong-nang",
    "title": "Công suất",
    "bullets": [
      "Đại lượng vô hướng đặc trưng cho tốc độ thực hiện công hoặc tốc độ truyền năng lượng theo thời gian.",
      "Watt là đơn vị công suất, mã lực là đơn vị công suất ngoài SI. Kilowatt-giờ là đơn vị năng lượng."
    ],
    "formula": "$$\nP_{\\mathrm{av}} = \\frac{\\Delta W}{\\Delta t}\n$$"
  },
  {
    "note": "12-co-hoc-chat-luu",
    "title": "Chất khí, chất lỏng và khối lượng riêng",
    "bullets": [
      "Chất lưu có thể chảy và thay đổi hình dạng. Chất khí và chất lỏng đều là chất lưu. Chất lỏng có lực liên kết phân tử đủ mạnh để giữ thể tích gần như không đổi trong những điều kiện thông thường.",
      "Vật liệu đồng nhất có cùng khối lượng riêng tại mọi điểm. Với vật không đồng nhất, tỉ số khối lượng toàn vật và thể tích toàn vật là khối lượng riêng trung bình.",
      "Đơn vị SI là kilogram trên mét khối. Giá trị bằng gram trên centimet khối được đổi sang SI bằng hệ số một nghìn.",
      "Tỉ khối là tỉ số khối lượng riêng của vật liệu và khối lượng riêng của nước ở 4,0 °C. Đại lượng này không có đơn vị."
    ],
    "formula": "$$\n\\rho=\\frac mV\n$$"
  },
  {
    "note": "12-co-hoc-chat-luu",
    "title": "Áp suất và cân bằng chất lưu",
    "bullets": [
      "Áp suất là đại lượng vô hướng. Trong chất lưu đứng yên, áp lực tác dụng vuông góc với mặt tiếp xúc. Hai phía của một mặt nhỏ trong chất lưu cân bằng chịu lực bằng nhau về độ lớn và ngược chiều.",
      "Khi áp suất bằng nhau trên toàn bộ mặt phẳng đang xét, độ lớn áp lực ở một phía bằng tích áp suất và diện tích.",
      "Pascal là đơn vị SI. Atmosphere tiêu chuẩn được định nghĩa bằng 101325 Pa. Bar và millibar là các đơn vị áp suất.",
      "Chất lưu đứng yên trong trường trọng lực. Trục y hướng lên và g là độ lớn gia tốc trọng trường. Công thức hiệu áp suất dưới đây dùng khối lượng riêng và g không đổi trên đoạn xét."
    ],
    "formula": "$$\np=\\frac{dF_\\perp}{dA}\n$$"
  },
  {
    "note": "12-co-hoc-chat-luu",
    "title": "Lực nổi và sức căng bề mặt",
    "bullets": [
      "Lực đẩy hướng lên bằng trọng lượng phần chất lưu bị vật chiếm chỗ. Với chất lưu có khối lượng riêng không đổi trong trường trọng lực đều, đường tác dụng đi qua trọng tâm phần chất lưu bị chiếm chỗ.",
      "Khi chỉ trọng lực và lực đẩy tác dụng lên vật, lực đẩy bằng trọng lượng. Tỉ lệ thể tích chìm dưới đây bỏ qua lực nổi của không khí và dùng khối lượng riêng trung bình của toàn vật.",
      "Với dây căng kéo thẳng lên và vật cân bằng, lực căng bằng trọng lượng trừ lực đẩy. Biểu thức áp dụng khi lực căng không âm. Nếu lực đẩy lớn hơn trọng lượng, dây phía trên không thể giữ vật bằng lực căng.",
      "Phù kế tự nổi cân bằng. Cùng một phù kế chiếm chỗ thể tích chất lỏng lớn hơn khi khối lượng riêng chất lỏng nhỏ hơn."
    ],
    "formula": "$$\nB=\\rho_{\\mathrm f}gV_{\\mathrm d}\n$$"
  },
  {
    "note": "12-co-hoc-chat-luu",
    "title": "Dòng chảy và phương trình liên tục",
    "bullets": [
      "Mô hình chất lưu không nén được và không có ma sát bên trong. Bỏ qua ứng suất nhớt khi tác dụng của chúng nhỏ so với lực áp suất và trọng lực.",
      "Trong dòng ổn định, trường vận tốc tại mỗi vị trí cố định không đổi theo thời gian. Tiếp tuyến đường dòng cùng hướng vận tốc tức thời. Đường đi của phần tử trùng đường dòng trong dòng ổn định. Chất lưu không đi xuyên qua thành bên của ống dòng.",
      "Dòng ổn định, cùng một ống dòng không có nguồn cấp hoặc nhánh hút qua thành bên. Khối lượng riêng không đổi. Các tốc độ là đều trên tiết diện hoặc được hiểu là giá trị trung bình phù hợp.",
      "Lưu lượng thể tích là thể tích đi qua một tiết diện trong một đơn vị thời gian. Công thức Av dùng tốc độ trung bình theo tiết diện nếu vận tốc không đều."
    ],
    "formula": "$$\nA_1v_1=A_2v_2\n$$"
  },
  {
    "note": "12-co-hoc-chat-luu",
    "title": "Phương trình Bernoulli",
    "bullets": [
      "Dòng ổn định, chất lưu không nén được, bỏ qua nhớt và tổn hao cơ năng. Hai điểm thuộc cùng một đường dòng hoặc ống dòng được mô hình hóa. Không có công bơm hay tuabin giữa hai điểm trong dạng phương trình đang xét.",
      "Tổng áp suất, thế năng trọng trường trên thể tích và động năng trên thể tích không đổi dọc đường dòng dưới các điều kiện Bernoulli. Mỗi số hạng có đơn vị Pa.",
      "Trong cùng thời gian, thể tích dV đi vào và đi ra ống dòng không nén được bằng nhau. Công áp suất ở đầu vào dương, ở đầu ra âm theo chiều dòng.",
      "Trong phép so sánh hai trạng thái của dòng ổn định, phần thể tích chung không đổi cơ năng. Với phần chất lưu được thay thế có khối lượng ρdV, công áp suất bằng biến thiên động năng và thế năng."
    ],
    "formula": "$$\n\\begin{aligned}\n&p_1+\\rho gy_1+\\frac12\\rho v_1^2=C,\\\\\n&p_2+\\rho gy_2+\\frac12\\rho v_2^2=C.\n\\end{aligned}\n$$"
  },
  {
    "note": "12-co-hoc-chat-luu",
    "title": "Độ nhớt và chảy rối",
    "bullets": [
      "Độ nhớt đặc trưng ma sát bên trong chất lưu. Lực nhớt chống lại chuyển động tương đối giữa những phần chất lưu. Ở các chất được xét, độ nhớt tăng theo nhiệt độ đối với khí và giảm theo nhiệt độ đối với chất lỏng.",
      "Chất lưu nhớt có xu hướng bám bề mặt rắn. Gần bề mặt, tốc độ tương đối của chất lưu so với bề mặt nhỏ. Trong mô hình không trượt ở thành ống, tốc độ tương đối bằng không.",
      "Trong ống trụ dài, dòng tầng có độ lớn vận tốc theo bán kính dạng parabol. Tốc độ lớn nhất trên trục ống và bằng không tại thành. Cần chênh áp theo chiều dòng để duy trì lưu lượng.",
      "Với cùng chất lưu, trạng thái nhiệt độ và lưu lượng thể tích trong dòng tầng qua ống trụ dài, chênh áp tỉ lệ chiều dài ống và nghịch đảo lũy thừa bậc bốn bán kính trong."
    ],
    "formula": "$$\nv(R)=0\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Lực hấp dẫn",
    "bullets": [
      "Hai chất điểm có khối lượng dương hút nhau theo đường nối chúng. Với hai phân bố đối xứng cầu không chồng lấn, r là khoảng cách giữa hai tâm.",
      "Hai lực đặt lên hai vật khác nhau, bằng nhau về độ lớn và ngược chiều.",
      "Lực tổng hợp là tổng vector từng lực. Viết tường minh cho ba vật gây lực.",
      "G không phải gia tốc trọng trường g. Giá trị dùng trong các phép tính là xấp xỉ ba chữ số có nghĩa."
    ],
    "formula": "$$\nF_g=\\frac{Gm_1m_2}{r^2}\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Trọng lượng và gia tốc trọng trường",
    "bullets": [
      "Trọng lượng là tổng lực hấp dẫn tác dụng lên vật. Gần một thiên thể, dùng lực hút của thiên thể đó khi các ảnh hưởng khác không đáng kể.",
      "Thiên thể trung tâm có khối lượng M. r đo từ tâm và nằm ngoài vật. g là độ lớn gia tốc hấp dẫn do thiên thể đó.",
      "Thiên thể đối xứng cầu có bán kính R.",
      "Vị trí nằm ở độ cao h trên bề mặt, nên r=R+h. Khối lượng của vật thử không thay đổi."
    ],
    "formula": "$$\nw=mg\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Thế năng và tốc độ thoát",
    "bullets": [
      "Chiều dương bán kính hướng ra ngoài thiên thể đối xứng cầu.",
      "Thế năng của hệ hai vật, với mốc bằng không ở vô cực. Công thức dùng cho chất điểm hoặc tương tác bên ngoài phù hợp của phân bố đối xứng cầu.",
      "Hai trạng thái nằm ngoài thiên thể. Công hấp dẫn không phụ thuộc đường đi.",
      "Động năng K của vật được phóng được tính trong hệ thiên thể trung tâm đứng yên. Vật nhẹ hơn nhiều thiên thể. Chỉ lực hấp dẫn thực hiện công trong mô hình đang xét."
    ],
    "formula": "$$\nF_r=-\\frac{GMm}{r^2}\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Quỹ đạo tròn",
    "bullets": [
      "Chỉ lực hút của thiên thể khối lượng M chi phối chuyển động. Vật trung tâm được coi đứng yên và quỹ đạo có bán kính r.",
      "T là thời gian đi hết một vòng trên quỹ đạo tròn.",
      "Thế năng dùng mốc vô cực. Các quan hệ K,U,E dưới đây dành riêng cho quỹ đạo tròn.",
      "Coi thiên thể trung tâm đứng yên và vật được phóng có khối lượng nhỏ hơn nhiều khối lượng thiên thể. So sánh tại cùng khoảng cách r quanh cùng thiên thể."
    ],
    "formula": "$$\nv=\\sqrt{\\frac{GM}{r}}\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Các định luật Kepler",
    "bullets": [
      "Mặt Trời nằm tại một tiêu điểm. a là bán trục lớn, e là độ lệch tâm. e=0 cho đường tròn, 0<e<1 cho ellipse không tròn.",
      "Đường nối từ thiên thể trung tâm tới vật quét các diện tích bằng nhau trong những khoảng thời gian bằng nhau. Áp dụng khi mômen động lượng quanh tâm bảo toàn.",
      "Lực luôn dọc đường nối chất điểm với một điểm cố định. Mômen lực quanh điểm đó bằng không, nên vector mômen động lượng bảo toàn.",
      "Quỹ đạo liên kết quanh thiên thể trung tâm có khối lượng M lớn hơn nhiều khối lượng vật quay. Chu kỳ phụ thuộc bán trục lớn, không phụ thuộc riêng độ lệch tâm."
    ],
    "formula": "$$\n0\\le e<1\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Đối xứng cầu và vỏ cầu",
    "bullets": [
      "Chất điểm ở bên ngoài vật đối xứng cầu tổng khối lượng M. r tính từ tâm.",
      "Vỏ bán kính R, khối lượng M phân bố đều trên mặt. Chất điểm ở r<R. Thế năng dùng mốc vô cực.",
      "M(r) là khối lượng nằm trong bán kính r. Các vỏ ngoài r không gây hợp lực lên vật thử bên trong.",
      "Vật cầu bán kính R, tổng khối lượng M. Biểu thức áp dụng r≤R, và lực tại tâm bằng không theo đối xứng."
    ],
    "formula": "$$\nU=-\\frac{GMm}{r}\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Trọng lượng biểu kiến và sự quay",
    "bullets": [
      "F là lực do cân tác dụng lên vật. Trọng lượng biểu kiến có độ lớn bằng số chỉ cân và vector ngược hướng lực cân.",
      "Trái Đất được coi hình cầu, quay đều. w0 là trọng lượng hấp dẫn thật và v là tốc độ xích đạo.",
      "Gia tốc hướng tâm arad hướng về trục quay. Hệ thức là vector, không thay bằng hiệu hai độ lớn khi các vector không cùng phương.",
      "Trong mô hình hình cầu, bán kính chuyển động quanh trục bằng không ở hai cực, nên số chỉ cân bằng trọng lượng thật."
    ],
    "formula": "$$\n\\vec w=-\\vec F\n$$"
  },
  {
    "note": "13-hap-dan",
    "title": "Hố đen và chân trời sự kiện",
    "bullets": [
      "Coi thiên thể trung tâm đứng yên và vật được phóng có khối lượng nhỏ hơn nhiều khối lượng thiên thể. Trong mô hình Newton bên ngoài một thiên thể hình cầu, với khối lượng riêng trung bình rho và bán kính R.",
      "Mô hình hố đen đối xứng cầu, không quay và không tích điện. Đây là kết quả của thuyết tương đối rộng.",
      "Ranh giới nhân quả bao quanh vùng không thể truyền tín hiệu ra ngoài. Với mô hình Schwarzschild, chân trời là mặt cầu bán kính RS. Ánh sáng quan sát từ đĩa bồi tụ phát ra trước khi vật chất đi vào chân trời.",
      "Trong mô hình Kepler chi phối bởi một vật trung tâm, chu kỳ T và bán trục lớn a của sao lân cận xác định khối lượng trung tâm."
    ],
    "formula": "$$\nM=\\frac{4\\pi}{3}\\bar\\rho R^3\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Mô tả dao động",
    "bullets": [
      "Chuyển động lặp lại sau chu kỳ $T$. Các hệ dao động phục hồi đang xét có cân bằng bền và chuyển động qua lại quanh vị trí cân bằng.",
      "Tần số góc bằng hai pi lần tần số, có đơn vị rad/s. Tần số có đơn vị Hz.",
      "Biên độ $A$ là độ lớn li độ cực đại. Trong dao động qua lại đối xứng, hành trình giữa hai biên dài $2A$ và mất nửa chu kỳ."
    ],
    "formula": "$$\nf=\\frac1T,\\qquad T=\\frac1f\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Dao động điều hòa",
    "bullets": [
      "Hợp lực theo trục dao động bằng $-kx$, với $m>0$, $k>0$ và không có tiêu tán.",
      "Lò xo lý tưởng có khối lượng bỏ qua. Với cùng $m,k$, tần số và chu kỳ không phụ thuộc biên độ.",
      "Biên độ $A$ và pha ban đầu $\\phi$ do điều kiện đầu xác định. Pha tại thời điểm $t$ là $\\omega t+\\phi$.",
      "Vận tốc và gia tốc là các đạo hàm theo thời gian của li độ."
    ],
    "formula": "$$\nF_x=-kx\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Cơ năng dao động điều hòa",
    "bullets": [
      "Lò xo lý tưởng, không có công của lực tiêu tán, với mốc thế năng tại cân bằng.",
      "Ký hiệu $K,U$ lần lượt là động năng và thế năng đàn hồi. Miền chuyển động là $|x|\\le A$.",
      "Dấu của vận tốc phụ thuộc chiều chuyển động tại li độ đang xét."
    ],
    "formula": "$$\nE=\\frac12mv_x^2+\\frac12kx^2\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Các mô hình điều hòa",
    "bullets": [
      "Li độ $x$ đo từ vị trí cân bằng có trọng lực. Độ dãn tĩnh là $\\Delta l$. Trọng lực dịch vị trí cân bằng nhưng không đổi tần số khi $m,k$ giữ nguyên.",
      "Góc tính bằng radian, $\\kappa>0$ là hằng số xoắn và $I$ là mômen quán tính quanh trục dao động.",
      "Mô hình van der Waals có $U_0>0$, khoảng cách cân bằng $R_0$. Biến $u$ là tỷ số khoảng cách không thứ nguyên.",
      "Độ lệch $x=r-R_0$ thỏa $|x|\\ll R_0$. Độ cứng hiệu dụng là độ cong thế năng tại cân bằng. Khi cả hai hạt tự do, tần số tương đối dùng khối lượng rút gọn $\\mu$."
    ],
    "formula": "$$\nk\\Delta l=mg\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Con lắc đơn",
    "bullets": [
      "Chất điểm treo bằng dây không khối lượng, không dãn, dài $L$. Dây còn căng và góc $\\theta$ đo từ phương thẳng đứng xuống.",
      "Với góc nhỏ tính bằng radian, $\\sin\\theta\\approx\\theta$ và chuyển động gần điều hòa.",
      "Biên độ góc thỏa $0\\le\\Theta<\\pi$. Ký hiệu $T_0$ là chu kỳ góc nhỏ. Chuỗi dưới đây biểu diễn chu kỳ với hai hệ số hiệu chỉnh đầu."
    ],
    "formula": "$$\nx=L\\theta\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Con lắc vật lý",
    "bullets": [
      "Vật rắn quay quanh trục không ma sát. Ở cân bằng bền, trọng tâm ở dưới trục một đoạn $d>0$. Mômen quán tính $I$ lấy quanh trục treo.",
      "Góc nhỏ tính bằng radian, trường trọng lực gần đều và mômen quán tính quanh trục không đổi.",
      "Thanh dài $L$, khối lượng $m$, dao động góc nhỏ quanh trục qua đầu, vuông góc thanh."
    ],
    "formula": "$$\n\\tau_z=-mgd\\sin\\theta\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Tắt dần do lực cản tuyến tính",
    "bullets": [
      "Khối lượng và độ cứng dương, hệ số cản không âm. Lực cản tuyến tính ngược chiều vận tốc.",
      "Hệ số cản thỏa $0<b<2\\sqrt{km}$. Đặt $\\omega_0=\\sqrt{k/m}$. Các hằng số $A,\\phi$ do điều kiện đầu xác định.",
      "Tới hạn khi $b=b_c$, quá tới hạn khi $b>b_c$. Vật bị lệch rồi thả từ nghỉ trở về mà không dao động qua lại trong hai chế độ này.",
      "Tốc độ biến thiên cơ năng bằng công suất lực cản và không dương. Cơ năng tức thời không giảm với tốc độ đều."
    ],
    "formula": "$$\nF_d=-bv_x\n$$"
  },
  {
    "note": "14-dao-dong",
    "title": "Dao động cưỡng bức và cộng hưởng",
    "bullets": [
      "Ngoại lực hình sin tác dụng lên hệ tuyến tính có $b>0$. Sau khi quá độ tắt, tần số góc đáp ứng bằng $\\omega_d$.",
      "Công thức cho trạng thái ổn định của hệ tuyến tính có cản, với biên độ lực $F_{\\max}$ và tần số góc cưỡng bức $\\omega_d$.",
      "Đỉnh tại tần số dương chỉ tồn tại khi $b<\\sqrt{2km}$. Tần số đỉnh gần tần số riêng không cản khi cản yếu.",
      "Đặt $\\omega_0=\\sqrt{k/m}$. Tại tần số cưỡng bức không, lực là hằng số và đáp ứng cuối là độ lệch cân bằng tĩnh."
    ],
    "formula": "$$\nF(t)=F_{\\max}\\cos\\omega_dt\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Các loại sóng cơ",
    "bullets": [
      "Nhiễu loạn truyền trong môi trường vật chất. Tốc độ truyền nhiễu loạn khác vận tốc dao động của từng phần tử môi trường.",
      "Sóng ngang có phương dao động vuông góc chiều truyền. Sóng dọc có phương dao động cùng phương chiều truyền. Một chuyển động sóng có thể chứa cả hai thành phần.",
      "Sóng cơ truyền năng lượng nhờ tương tác giữa các phần môi trường. Trong mô hình dao động tuyến tính đang xét, phần tử dao động quanh vị trí cân bằng, còn hình dạng nhiễu loạn truyền đi."
    ],
    "formula": ""
  },
  {
    "note": "15-song-co",
    "title": "Sóng tuần hoàn",
    "bullets": [
      "Chu kỳ là thời gian chuyển động lặp lại, còn tần số là số chu kỳ trong một đơn vị thời gian.",
      "Khoảng cách giữa hai điểm liên tiếp cùng pha của sóng tuần hoàn, chẳng hạn hai đỉnh kề nhau. Trong một chu kỳ, dạng sóng chạy một bước sóng.",
      "Khi tốc độ truyền chỉ do các tính chất cơ học cố định của môi trường quyết định, tăng tần số làm giảm bước sóng theo cùng tỷ lệ nghịch. Tính độc lập với tần số này là giả thiết của các mô hình trong chương."
    ],
    "formula": "$$\nf=\\frac1T,\\qquad \\omega=2\\pi f\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Hàm sóng hình sin",
    "bullets": [
      "Chọn gốc thời gian khi nguồn có li độ dương cực đại.",
      "Với hàm $y(x,t)$, pha $kx-\\omega t$ không đổi trên các vị trí chuyển về phía x tăng. Ba cách viết dưới đây tương đương, với y là cùng hàm li độ.",
      "Số sóng là tốc độ biến thiên pha theo vị trí. Tần số góc là độ biến thiên pha theo thời gian tại một vị trí.",
      "Dấu cộng giữa $kx$ và $\\omega t$ ứng với chiều truyền âm khi k và tần số góc đều dương."
    ],
    "formula": "$$\ny(0,t)=A\\cos\\omega t\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Tốc độ sóng trên dây",
    "bullets": [
      "Khối lượng trên một đơn vị chiều dài. Với dây đồng nhất, tổng khối lượng bằng $\\mu L$.",
      "Với phần dây ban đầu đứng yên được cuốn vào chuyển động ngang trong thời gian t, khối lượng tham gia là $\\mu vt$.",
      "Dây mềm đồng nhất, lực căng gần đều, độ dốc và dao động ngang nhỏ. Khối lượng riêng dài giữ vai trò quán tính, còn lực căng giữ vai trò phục hồi.",
      "Với $\\mu$ không đổi, tốc độ tỉ lệ căn lực căng. Với lực căng không đổi, tốc độ tỉ lệ nghịch căn khối lượng riêng dài."
    ],
    "formula": "$$\n\\mu=\\frac mL\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Năng lượng và cường độ",
    "bullets": [
      "Xét lực của phần dây bên trái lên phần bên phải. Công suất dương quy ước năng lượng truyền theo chiều x tăng.",
      "Với sóng chạy theo chiều dương, đặt $\\theta=kx-\\omega t$ và viết P cho $P(x,t)$. Công suất tức thời không âm trong trường hợp một sóng chạy này.",
      "Trung bình trên một số nguyên chu kỳ. Với cùng dây và cùng lực căng, công suất trung bình tỉ lệ $A^2f^2$, trong đó A là biên độ li độ.",
      "Công suất trung bình truyền qua một đơn vị diện tích S vuông góc chiều truyền. Công thức thương dưới đây áp dụng khi cường độ đều trên S."
    ],
    "formula": "$$\nF_y=-F\\frac{\\partial y}{\\partial x}\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Phản xạ và chồng chất",
    "bullets": [
      "Li độ đầu dây bằng không ở mọi thời điểm. Sóng phản xạ lý tưởng đảo dấu li độ so với sóng tới.",
      "Vòng nhẹ không ma sát không nhận lực theo phương dao động từ giá đỡ. Độ dốc tại đầu tự do bằng không, và sóng phản xạ không đảo dấu.",
      "Li độ tổng tại cùng vị trí và thời điểm bằng tổng đại số các li độ thành phần. Cần phương trình sóng và điều kiện biên tuyến tính.",
      "Cộng hai li độ cùng dấu làm tăng độ lớn li độ tổng. Hai li độ trái dấu bù nhau một phần hoặc toàn phần. Sau khi hai xung vượt qua nhau trong môi trường tuyến tính lý tưởng, từng xung tiếp tục truyền với dạng riêng."
    ],
    "formula": "$$\ny(0,t)=0\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Sóng dừng",
    "bullets": [
      "Hai sóng cùng $A,\\omega,k$, với quan hệ pha thỏa đầu cố định ở gốc.",
      "Viết y cho li độ y(x,t). Biên độ tại một điểm là độ lớn thừa số không gian. Các điểm trong cùng một bó dao động cùng pha.",
      "Nút luôn đứng yên. Bụng có biên độ lớn nhất và nằm giữa hai nút. Nút đếm bằng n=0,1,2,... từ đầu cố định.",
      "Có trao đổi năng lượng cục bộ theo thời gian, nhưng không có truyền năng lượng trung bình qua một điểm. Công suất tức thời không bắt buộc bằng không ở mọi điểm."
    ],
    "formula": "$$\ny_1=-A\\cos(kx+\\omega t)\n$$"
  },
  {
    "note": "15-song-co",
    "title": "Dạng riêng và họa âm",
    "bullets": [
      "Chiều dài chứa một, hai, ba,... nửa bước sóng. Chỉ số n chạy qua các số nguyên dương.",
      "Tần số riêng của dây mềm lý tưởng là $f_1$, $2f_1$, $3f_1$, v.v. với $n=1,2,3,\\ldots$. Mỗi dạng có cùng tần số tại mọi điểm, nhưng biên độ có thể khác nhau.",
      "Viết y_n cho y_n(x,t). Hai đầu x=0 và x=L đều là nút. Pha thời gian có thể thay đổi theo điều kiện đầu.",
      "Họa âm thứ nhất là âm cơ bản. Họa âm thứ hai là âm bồi thứ nhất. Âm bồi thứ hai là họa âm thứ ba."
    ],
    "formula": "$$\nL=n\\frac\\lambda2\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Sóng âm và áp suất",
    "bullets": [
      "Trong chất lưu, dao động phần tử song song phương truyền. x là tọa độ cân bằng, y là li độ dọc, A là biên độ li độ.",
      "p là áp suất dư so với cân bằng, B>0 là môđun khối. Biến dạng thể tích nhỏ và chuyển động dọc một chiều.",
      "Với sóng hình sin, p và y lệch pha một phần tư chu kỳ tại cùng vị trí. Biên độ áp suất không phải li độ phần tử.",
      "Cao độ liên hệ chủ yếu với tần số. Âm sắc phụ thuộc thành phần họa âm và sự hình thành, suy giảm âm. Độ to không đồng nghĩa cao độ. Hạ âm dưới khoảng 20 Hz, miền nghe thường khoảng 20–20000 Hz, siêu âm trên miền ấy."
    ],
    "formula": "$$\ny=A\\cos(kx-\\omega t)\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Tốc độ truyền âm",
    "bullets": [
      "Mô hình biến dạng nhỏ, môi trường gần đồng nhất, rho>0. Độ phục hồi thể tích so với quán tính quyết định tốc độ.",
      "Thanh đàn hồi tuyến tính, biến dạng ngang tự do. Y là môđun Young. Không phải công thức chung cho mọi sóng trong khối rắn.",
      "Nén giãn âm gần đoạn nhiệt. Nhiệt độ tuyệt đối T, khối lượng mol M và tỷ số nhiệt dung gamma xác định tốc độ. Với cùng loại khí, không coi áp suất là yếu tố độc lập khi lấy B/rho.",
      "f>0 và tốc độ pha v trong môi trường đang xét. Khi qua mặt phân cách đứng yên, tần số giữ nguyên còn bước sóng có thể đổi."
    ],
    "formula": "$$\nv=\\sqrt{\\frac B\\rho}\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Cường độ và mức cường độ âm",
    "bullets": [
      "Công suất trung bình trên diện tích vuông góc phương truyền. Công thức theo A hoặc pmax dùng cho sóng hình sin chạy trong chất lưu.",
      "Cùng môi trường và cùng tần số, cường độ tỷ lệ bình phương biên độ li độ hoặc áp suất. Với I cố định, biên độ li độ tỷ lệ nghịch tần số.",
      "Công suất trung bình P không bị hấp thụ. Nguồn tỏa toàn mặt cầu dùng diện tích $4\\pi r^2$. Tỏa đều trên bán cầu dùng $2\\pi r^2$.",
      "Cường độ tham chiếu $I_0=10^{-12}\\,\\mathrm{W/m^2}$. Logarit cơ số 10, đối số là tỷ số không thứ nguyên. Đơn vị mức là dB."
    ],
    "formula": "$$\nI=\\frac12\\rho v\\omega^2A^2\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Sóng âm dừng và các dạng riêng",
    "bullets": [
      "Đầu kín là nút li độ, bụng áp suất. Đầu hở gần là bụng li độ, nút áp suất. Nút/bụng phải chỉ rõ đại lượng.",
      "Trong sóng dừng một chiều hình sin, hai nút kế tiếp hoặc hai bụng kế tiếp cách $\\lambda/2$. Nút và bụng kề nhau cách $\\lambda/4$.",
      "Cột khí đều dài hiệu dụng L, bỏ hiệu chỉnh đầu ống. n=1,2,3,… là mọi số nguyên dương.",
      "Cột khí đều dài hiệu dụng L, một đầu kín và đầu kia hở. n=1,3,5,… chỉ nhận số nguyên dương lẻ."
    ],
    "formula": "$$\nd_{NN}=\\frac\\lambda2\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Cộng hưởng âm",
    "bullets": [
      "Đáp ứng tăng mạnh khi tần số kích thích gần một tần số riêng. Đỉnh phụ thuộc hình học, độ cản và đại lượng đáp ứng. Cản yếu cho đỉnh gần tần số riêng không cản.",
      "Hai hệ ghép cộng hưởng có thể cùng tần số nhưng khác bước sóng vì tốc độ truyền khác nhau.",
      "Ở trạng thái ổn định có cản, công suất trung bình nhận cân bằng công suất tiêu tán. Hệ lý tưởng không cản kích thích đúng tần số riêng không có biên độ ổn định hữu hạn."
    ],
    "formula": "$$\nf_a=f_b\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Giao thoa sóng âm",
    "bullets": [
      "Hai nguồn cùng tần số, cùng pha ban đầu. Pha tới phụ thuộc chênh đường truyền. Nguồn lệch pha ban đầu cần tính thêm độ lệch ấy.",
      "Hai nguồn cùng pha và cùng tần số. n=0,1,2,… là số nguyên không âm.",
      "Hai nguồn cùng pha và cùng tần số. n=1,3,5,… là số nguyên dương lẻ. Triệt tiêu áp suất hoàn toàn còn cần biên độ tới bằng nhau.",
      "Năng lượng được phân bố lại, không biến mất. Với hai sóng tới không song song, tổng áp suất bằng không không tự làm tổng vector li độ bằng không."
    ],
    "formula": "$$\nd=|r_2-r_1|\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Phách",
    "bullets": [
      "Hai âm gần tần số tạo nhịp lớn nhỏ. Pha ban đầu không đổi khoảng cách giữa hai cực đại bao liên tiếp.",
      "Hai dao động có cùng biên độ A. Đặt $\\Delta f=f_a-f_b$ và $\\bar f=(f_a+f_b)/2$. Với pha đầu đối nhau, $h=\\pi\\Delta f\\,t$ và $g=2\\pi\\bar f\\,t$.",
      "Biết một tần số và tần số phách chỉ cho hai khả năng cao hơn hoặc thấp hơn. Phách khác âm hiệu có thể xuất hiện do đáp ứng phi tuyến."
    ],
    "formula": "$$\nf_{\\mathrm{ph}}=|f_a-f_b|\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Hiệu ứng Doppler",
    "bullets": [
      "Nguồn S và người nghe L chuyển động dọc đường nối, vận tốc đo so với môi trường. Chiều dương từ L tới S. Xét miền dưới tốc độ âm, v>0.",
      "Nguồn đứng yên đối với môi trường. Người nghe tiến về nguồn có $v_L>0$, ra xa có $v_L<0$.",
      "u>0 là tốc độ nguồn đối với môi trường, u<v. Phía trước và phía sau được xác định theo chiều nguồn chuyển động.",
      "Bề mặt nhận sóng ở lượt tới, rồi là nguồn ở lượt phản xạ. Tần số phát lại trong hệ bề mặt bằng tần số bề mặt nhận. Cần hai lần đổi vai nguồn/người nghe."
    ],
    "formula": "$$\nf_L=\\frac{v+v_L}{v+v_S}f_S\n$$"
  },
  {
    "note": "16-am-hoc",
    "title": "Sóng xung kích và số Mach",
    "bullets": [
      "Tốc độ vật $v_S$ đo so với môi trường, tốc độ âm $v>0$. Vượt âm ứng với $M>1$.",
      "Nguồn chuyển động đều vượt âm trong môi trường đồng nhất. Góc $\\alpha$ giữa một đường sinh nón và phương vận tốc là nửa góc mở nón.",
      "Tiếng nổ xuất hiện khi mặt xung kích đi qua người nghe. Vật tạo xung kích liên tục khi còn vượt âm, không chỉ lúc vừa vượt Mach 1 hoặc chỉ khi động cơ phát tiếng. Công thức Doppler phía trước nguồn dưới âm không được kéo dài sang nguồn vượt âm."
    ],
    "formula": "$$\nM=\\frac{v_S}{v}\n$$"
  },
  {
    "note": "01-don-vi-vector",
    "title": "Đại lượng vật lý và đơn vị",
    "bullets": [
      "Một giá trị đo gồm con số và đơn vị. Đơn vị dẫn xuất được lập từ các đơn vị cơ bản. Trong cơ học, các đơn vị cơ bản là mét, kilôgam và giây.",
      "Giây dựa trên bức xạ của nguyên tử cesium-133. Mét được xác định từ tốc độ ánh sáng. Kilôgam dựa trên hằng số Planck.",
      "Các hệ số thập phân là chính xác.",
      "Nhân giá trị với một hệ số đổi đơn vị bằng một. Đơn vị cũng được nhân, chia và khử như các thừa số đại số."
    ],
    "formula": "$$\nf_{\\mathrm{Cs}}=9\\,192\\,631\\,770\\,\\mathrm{Hz}\n$$"
  },
  {
    "note": "01-don-vi-vector",
    "title": "Độ bất định, chữ số có nghĩa và ước lượng",
    "bullets": [
      "Với giá trị đo khác không, độ bất định tương đối bằng độ bất định tuyệt đối chia độ lớn giá trị đo.",
      "Kết quả giữ số chữ số có nghĩa bằng số chữ số có nghĩa ít nhất trong các dữ kiện đo tham gia phép tính.",
      "Kết quả làm tròn tới hàng thập phân kém chính xác nhất của các số hạng. Đây là quy tắc về hàng thập phân, khác quy tắc cho phép nhân và chia.",
      "Hệ số đổi đơn vị chính xác không giới hạn số chữ số có nghĩa. Giữ thêm chữ số ở các bước trung gian và làm tròn kết quả cuối."
    ],
    "formula": "$$\n\\varepsilon_r=\\frac{\\Delta x}{|x|}\n$$"
  },
  {
    "note": "01-don-vi-vector",
    "title": "Vector và thành phần",
    "bullets": [
      "Đại lượng vô hướng có giá trị số. Vector có độ lớn và hướng. Vector bằng không có độ lớn bằng không và không có hướng xác định.",
      "Cộng vector theo quy tắc nối đuôi vào đầu hoặc quy tắc hình bình hành. Nhân với số âm đảo hướng, còn độ lớn được nhân với trị tuyệt đối của số ấy.",
      "Trong mặt phẳng, θ đo từ trục +x về phía +y theo chiều ngược kim đồng hồ. Các thành phần là đại lượng đại số, không phải vector.",
      "Công thức tang chỉ dùng khi Aₓ khác không. Phải chọn góc phần tư theo dấu cả hai thành phần. Nếu Aₓ=0 thì hướng nằm trên trục y. Nếu cả hai bằng không thì hướng không xác định."
    ],
    "formula": "$$\nA=\\|\\vec A\\|\\ge0\n$$"
  },
  {
    "note": "01-don-vi-vector",
    "title": "Các phép nhân vector",
    "bullets": [
      "Kết quả là một đại lượng vô hướng. Với hai vector khác không, φ là góc giữa chúng trong khoảng từ 0° đến 180°. Ký hiệu S là tích vô hướng của hai vector.",
      "Với hai vector không cùng phương và khác không, kết quả vuông góc mặt phẳng của chúng, hướng theo quy tắc bàn tay phải. Nếu cùng phương hoặc có vector không, kết quả là vector không."
    ],
    "formula": "$$\n\\vec A\\cdot\\vec B=AB\\cos\\varphi\n$$"
  },
  {
    "note": "03-chuyen-dong-khong-gian",
    "title": "Vector vị trí, vận tốc và gia tốc",
    "bullets": [
      "Định nghĩa vị trí chất điểm trong hệ tọa độ Descartes ba chiều.",
      "Vận tốc trung bình cùng hướng với độ dời. vận tốc tức thời tiếp tuyến với quỹ đạo.",
      "Phân tích vận tốc thành hai thành phần vuông góc $v_x$ và $v_y$.",
      "Gia tốc mô tả tốc độ biến thiên của vector vận tốc theo thời gian."
    ],
    "formula": "$$\n\\vec{r} = x\\hat{i} + y\\hat{j} + z\\hat{k}\n$$"
  },
  {
    "note": "03-chuyen-dong-khong-gian",
    "title": "Chuyển động ném trong mặt phẳng",
    "bullets": [
      "Bỏ qua sức cản không khí, gia tốc ngang triệt tiêu và gia tốc đứng hướng xuống với độ lớn g.",
      "Gốc tại điểm ném, vận tốc ngang khác không. Đặt b và c như dưới đây để viết phương trình quỹ đạo.",
      "Áp dụng khi điểm rơi có cùng cao độ với điểm ném ban đầu ($y = 0$)."
    ],
    "formula": "$$\na_x = 0, \\quad a_y = -g\n$$"
  },
  {
    "note": "03-chuyen-dong-khong-gian",
    "title": "Chuyển động tròn đều và không đều",
    "bullets": [
      "Chất điểm đi trên đường tròn bán kính R với tốc độ không đổi v.",
      "Tốc độ thay đổi theo thời gian, gia tốc gồm cả thành phần hướng tâm và tiếp tuyến."
    ],
    "formula": "$$\nv = \\frac{2\\pi R}{T}\n$$"
  },
  {
    "note": "03-chuyen-dong-khong-gian",
    "title": "Vận tốc tương đối (Phép biến đổi Galilei)",
    "bullets": [
      "Quy tắc cộng vận tốc dọc theo một đường thẳng.",
      "Quy tắc cộng vector vận tốc giữa các hệ quy chiếu chuyển động tịnh tiến."
    ],
    "formula": "$$\nv_{P/A}=v_{P/B}+v_{B/A}\n$$"
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
          "cong-nang-luong",
          "dong-luong-vat-ly",
          "electron-volt",
          "song",
          "song-dien-tu",
          "nhieu-xa-khe-don",
          "dong-luong-tuong-doi",
          "nang-luong-nghi"
        ],
        "supportingConcepts": [
          "photon",
          "hang-so-planck",
          "hieu-ung-quang-dien",
          "cong-thoat",
          "the-ham-quang-dien",
          "quang-dan",
          "buc-xa-ham",
          "tan-xa-compton",
          "tao-cap-electron-positron",
          "huy-cap-electron-positron",
          "luong-tinh-song-hat",
          "xac-suat-photon",
          "bat-dinh-vi-tri-dong-luong",
          "bat-dinh-nang-luong-thoi-gian"
        ],
        "status": "ready",
        "number": 18,
        "sourceChapter": 38,
        "topicGroups": [
          {
            "title": "Hấp thụ và phát photon",
            "topics": [
              {
                "slug": "quang-dien",
                "title": "Hiệu ứng quang điện và photon",
                "question": "Vì sao tăng cường độ không thay được tần số ngưỡng?",
                "source": "38.1"
              },
              {
                "slug": "phat-tia-x",
                "title": "Phát tia X và bức xạ hãm",
                "question": "Điện áp gia tốc giới hạn bước sóng tia X như thế nào?",
                "source": "38.2"
              }
            ]
          },
          {
            "title": "Tán xạ, xác suất và bất định",
            "topics": [
              {
                "slug": "compton-tao-cap",
                "title": "Compton, tạo cặp và hủy cặp",
                "question": "Photon chuyển năng lượng và động lượng cho vật chất bằng cách nào?",
                "source": "38.3"
              },
              {
                "slug": "luong-tinh-bat-dinh",
                "title": "Lưỡng tính sóng–hạt và nguyên lý bất định",
                "question": "Vì sao các sự kiện photon riêng lẻ tạo nên phân bố nhiễu xạ?",
                "source": "38.4"
              }
            ]
          }
        ],
        "hasChapterExercises": true
      },
    {
      "slug": "19-song-vat-chat",
      "title": "Tính sóng của hạt",
      "prerequisites": [
        "cong-nang-luong",
        "dong-luong-vat-ly",
        "momen-dong-luong",
        "song",
        "nhieu-xa-anh-sang",
        "electron-volt",
        "photon",
        "dong-luong-tuong-doi",
        "nang-luong-nghi",
        "nhiet-do-tuyet-doi"
      ],
      "supportingConcepts": [
        "buoc-song-de-broglie",
        "nhieu-xa-electron",
        "mo-hinh-hat-nhan-rutherford",
        "pho-vach-nguyen-tu",
        "muc-nang-luong-nguyen-tu",
        "mo-hinh-bohr",
        "so-luong-tu-chinh",
        "nang-luong-ion-hoa",
        "khoi-luong-rut-gon",
        "phat-xa-kich-thich",
        "dao-lon-mat-do",
        "trang-thai-sieu-ben",
        "vat-den",
        "suat-phat-xa-pho",
        "dinh-luat-wien",
        "dinh-luat-planck",
        "do-rong-vach-tu-nhien"
      ],
      "status": "ready",
      "number": 19,
      "sourceChapter": 39,
      "topicGroups": [
        {
          "title": "Tính sóng và cấu trúc nguyên tử",
          "topics": [
            {
              "slug": "song-electron",
              "title": "Sóng electron và kính hiển vi electron",
              "question": "Làm thế nào đo được bước sóng của một hạt?",
              "source": "39.1"
            },
            {
              "slug": "nguyen-tu-hat-nhan-pho",
              "title": "Hạt nhân nguyên tử và quang phổ",
              "question": "Tán xạ và phổ ánh sáng cho biết gì về nguyên tử?",
              "source": "39.2"
            }
          ]
        },
        {
          "title": "Mức năng lượng và laser",
          "topics": [
            {
              "slug": "muc-nang-luong-bohr",
              "title": "Mức năng lượng và mô hình Bohr",
              "question": "Vì sao chỉ có một số bước sóng được phát hoặc hấp thụ?",
              "source": "39.3"
            },
            {
              "slug": "laser",
              "title": "Laser và phát xạ kích thích",
              "question": "Làm thế nào tạo một chùm sáng kết hợp bằng nhiều nguyên tử?",
              "source": "39.4"
            }
          ]
        },
        {
          "title": "Phổ nhiệt và bất định",
          "topics": [
            {
              "slug": "pho-lien-tuc",
              "title": "Phổ liên tục và bức xạ vật đen",
              "question": "Vì sao vật nóng phát một dải bước sóng và đổi màu khi nhiệt độ tăng?",
              "source": "39.5"
            },
            {
              "slug": "bat-dinh-vat-chat",
              "title": "Nguyên lý bất định đối với vật chất",
              "question": "Tính sóng thay đổi mô tả electron trong nguyên tử như thế nào?",
              "source": "39.6"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "20-ham-song-schrodinger",
      "title": "Cơ học lượng tử I: Hàm sóng",
      "prerequisites": [
        "dao-ham",
        "dao-ham-rieng",
        "tich-phan",
        "song",
        "dao-dong-dieu-hoa",
        "cong-nang-luong",
        "dong-luong-vat-ly",
        "photon",
        "buoc-song-de-broglie"
      ],
      "supportingConcepts": [
        "ham-song-luong-tu",
        "mat-do-xac-suat-luong-tu",
        "chuan-hoa-ham-song",
        "so-phuc-trong-ham-song",
        "phuong-trinh-schrodinger",
        "chong-chap-ham-song",
        "goi-song-luong-tu",
        "trang-thai-dung-luong-tu",
        "dieu-kien-bien-ham-song",
        "hat-trong-hop-luong-tu",
        "gieng-the-huu-han",
        "trang-thai-lien-ket-luong-tu",
        "xuyen-ham-luong-tu",
        "dao-dong-tu-dieu-hoa-luong-tu",
        "nang-luong-diem-khong",
        "phep-do-luong-tu",
        "cham-luong-tu",
        "kinh-hien-vi-quet-xuyen-ham"
      ],
      "status": "ready",
      "number": 20,
      "sourceChapter": 40,
      "topicGroups": [
        {
          "title": "Hàm sóng và sự giam giữ",
          "topics": [
            {
              "slug": "ham-song-schrodinger",
              "title": "Hàm sóng và phương trình Schrödinger",
              "question": "Biên độ phức mô tả trạng thái và xác suất như thế nào?",
              "source": "40.1"
            },
            {
              "slug": "hat-trong-hop",
              "title": "Hạt trong hộp vô hạn",
              "question": "Hai vách giới hạn các bước sóng và năng lượng ra sao?",
              "source": "40.2"
            },
            {
              "slug": "gieng-the-huu-han",
              "title": "Giếng thế hữu hạn",
              "question": "Điều gì thay đổi khi hàm sóng có thể thâm nhập ra ngoài giếng?",
              "source": "40.3"
            }
          ]
        },
        {
          "title": "Xuyên hầm, dao động và phép đo",
          "topics": [
            {
              "slug": "hang-rao-xuyen-ham",
              "title": "Hàng rào thế và xuyên hầm",
              "question": "Hạt đi qua miền bị cấm cổ điển với xác suất nào?",
              "source": "40.4"
            },
            {
              "slug": "dao-dong-tu-dieu-hoa",
              "title": "Dao động tử điều hòa",
              "question": "Điều kiện ở vô cực chọn các mức dao động như thế nào?",
              "source": "40.5"
            },
            {
              "slug": "phep-do-luong-tu",
              "title": "Phép đo trong cơ học lượng tử",
              "question": "Kết quả đo liên hệ với trạng thái trước và sau phép đo ra sao?",
              "source": "40.6"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "21-cau-truc-nguyen-tu",
      "title": "Cơ học lượng tử II: Cấu trúc nguyên tử",
      "prerequisites": [
        "dao-ham-rieng",
        "tich-phan",
        "ham-song-luong-tu",
        "phuong-trinh-schrodinger",
        "hat-trong-hop-luong-tu",
        "dao-dong-tu-dieu-hoa-luong-tu",
        "phep-do-luong-tu",
        "dinh-luat-gauss",
        "luong-cuc-tu",
        "song-dung-dien-tu",
        "mo-hinh-bohr",
        "photon"
      ],
      "supportingConcepts": [
        "phuong-trinh-schrodinger-ba-chieu",
        "hat-trong-hop-ba-chieu",
        "suy-bien-muc-nang-luong",
        "so-luong-tu-nguyen-tu",
        "orbital-nguyen-tu",
        "phan-bo-xac-suat-ban-kinh",
        "momen-dong-luong-quy-dao",
        "luong-tu-hoa-khong-gian",
        "hieu-ung-zeeman",
        "magneton-bohr",
        "spin-luong-tu",
        "thi-nghiem-stern-gerlach",
        "tuong-tac-spin-quy-dao",
        "nguyen-ly-pauli",
        "cau-hinh-electron",
        "che-chan-dien-tich-hat-nhan",
        "pho-tia-x-dac-trung",
        "dinh-luat-moseley",
        "roi-luong-tu",
        "qubit"
      ],
      "status": "ready",
      "number": 21,
      "sourceChapter": 41,
      "topicGroups": [
        {
          "title": "Trạng thái ba chiều và nguyên tử hydro",
          "topics": [
            {
              "slug": "schrodinger-ba-chieu",
              "title": "Phương trình Schrödinger trong ba chiều",
              "question": "Động năng và xác suất mở rộng sang ba chiều như thế nào?",
              "source": "41.1"
            },
            {
              "slug": "hop-ba-chieu",
              "title": "Hạt trong hộp ba chiều",
              "question": "Điều kiện biên tạo các mức và suy biến ra sao?",
              "source": "41.2"
            },
            {
              "slug": "nguyen-tu-hydro",
              "title": "Nguyên tử hydro và các số lượng tử",
              "question": "Nghiệm Coulomb mô tả trạng thái nguyên tử bằng những số nào?",
              "source": "41.3"
            },
            {
              "slug": "hieu-ung-zeeman",
              "title": "Mômen từ quỹ đạo và hiệu ứng Zeeman",
              "question": "Vì sao từ trường làm tách các mức và vạch phổ?",
              "source": "41.4"
            }
          ]
        },
        {
          "title": "Spin, nhiều electron và thông tin lượng tử",
          "topics": [
            {
              "slug": "spin-electron",
              "title": "Spin electron và cấu trúc tinh tế",
              "question": "Những kết quả nào đòi hỏi mômen động lượng nội tại?",
              "source": "41.5"
            },
            {
              "slug": "nguyen-tu-nhieu-electron",
              "title": "Nguyên tử nhiều electron và Pauli",
              "question": "Các electron lấp đầy trạng thái dưới những ràng buộc nào?",
              "source": "41.6"
            },
            {
              "slug": "pho-tia-x",
              "title": "Phổ tia X đặc trưng",
              "question": "Photon tia X cho biết gì về những mức nằm sâu trong nguyên tử?",
              "source": "41.7"
            },
            {
              "slug": "roi-luong-tu",
              "title": "Rối lượng tử và qubit",
              "question": "Khi nào trạng thái hai hạt không thể tách thành hai mô tả riêng?",
              "source": "41.8"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "22-chat-ran-ban-dan",
      "title": "Phân tử và vật chất ngưng tụ",
      "prerequisites": [
        "nguyen-ly-pauli",
        "cau-hinh-electron",
        "dao-dong-tu-dieu-hoa-luong-tu",
        "ham-song-luong-tu",
        "hat-trong-hop-ba-chieu",
        "photon",
        "nhiet-do-tuyet-doi",
        "tich-phan",
        "dien-truong"
      ],
      "supportingConcepts": [
        "lien-ket-ion",
        "lien-ket-cong-hoa-tri",
        "lien-ket-van-der-waals",
        "lien-ket-hydro",
        "pho-quay-phan-tu",
        "pho-dao-dong-phan-tu",
        "mang-tinh-the",
        "o-co-so-tinh-the",
        "hang-so-madelung",
        "vung-nang-luong",
        "vung-cam-nang-luong",
        "mo-hinh-electron-tu-do",
        "mat-do-trang-thai-luong-tu",
        "phan-bo-fermi-dirac",
        "nang-luong-fermi",
        "lo-trong-ban-dan",
        "pha-tap-ban-dan",
        "tiep-giap-p-n",
        "diot-ban-dan",
        "cap-cooper"
      ],
      "status": "ready",
      "number": 22,
      "sourceChapter": 42,
      "topicGroups": [
        {
          "title": "Liên kết, phổ và cấu trúc vật chất",
          "topics": [
            {
              "slug": "lien-ket-phan-tu",
              "title": "Các loại liên kết phân tử",
              "question": "Điều gì giữ các nguyên tử thành phân tử?",
              "source": "42.1"
            },
            {
              "slug": "pho-phan-tu",
              "title": "Phổ quay và dao động phân tử",
              "question": "Photon cho biết gì về chuyển động của các hạt nhân?",
              "source": "42.2"
            },
            {
              "slug": "cau-truc-chat-ran",
              "title": "Cấu trúc và liên kết trong chất rắn",
              "question": "Mạng và nhóm cơ sở tạo cấu trúc tinh thể như thế nào?",
              "source": "42.3"
            },
            {
              "slug": "dai-nang-luong",
              "title": "Dải năng lượng trong chất rắn",
              "question": "Vì sao cùng có electron mà các vật liệu dẫn điện khác nhau?",
              "source": "42.4"
            }
          ]
        },
        {
          "title": "Electron, bán dẫn và siêu dẫn",
          "topics": [
            {
              "slug": "mo-hinh-electron-tu-do",
              "title": "Mô hình electron tự do",
              "question": "Pauli quyết định sự điền trạng thái trong kim loại ra sao?",
              "source": "42.5"
            },
            {
              "slug": "chat-ban-dan",
              "title": "Bán dẫn thuần và pha tạp",
              "question": "Electron và lỗ trống hình thành bằng những cơ chế nào?",
              "source": "42.6"
            },
            {
              "slug": "thiet-bi-ban-dan",
              "title": "Tiếp giáp và thiết bị bán dẫn",
              "question": "Rào thế nội tạo đặc tuyến và khả năng điều khiển dòng như thế nào?",
              "source": "42.7"
            },
            {
              "slug": "sieu-dan",
              "title": "Trạng thái siêu dẫn",
              "question": "Vì sao trạng thái ghép cặp có thể dẫn tới điện trở bằng không?",
              "source": "42.8"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "23-vat-ly-hat-nhan",
      "title": "Vật lý hạt nhân",
      "prerequisites": [
        "photon",
        "thuyet-tuong-doi-hep",
        "cong-nang-luong",
        "dong-luong-vat-ly",
        "spin-luong-tu",
        "nguyen-ly-pauli",
        "xuyen-ham-luong-tu",
        "dao-ham",
        "tich-phan"
      ],
      "supportingConcepts": [
        "nuclide",
        "dong-vi-hat-nhan",
        "ban-kinh-hat-nhan",
        "spin-hat-nhan",
        "magneton-hat-nhan",
        "nang-luong-lien-ket-hat-nhan",
        "mo-hinh-giot-chat-long",
        "mo-hinh-vo-hat-nhan",
        "phan-ra-alpha",
        "phan-ra-beta",
        "bat-electron",
        "phan-ra-gamma",
        "phan-ra-phong-xa",
        "hoat-do-phong-xa",
        "chu-ky-ban-ra",
        "thoi-gian-song-trung-binh",
        "lieu-hap-thu-buc-xa",
        "lieu-tuong-duong-buc-xa",
        "nang-luong-phan-ung-hat-nhan",
        "phan-hach-hat-nhan",
        "nhiet-hach-hat-nhan"
      ],
      "status": "ready",
      "number": 23,
      "sourceChapter": 43,
      "topicGroups": [
        {
          "title": "Cấu trúc, liên kết và sự phân rã",
          "topics": [
            {
              "slug": "tinh-chat-hat-nhan",
              "title": "Các tính chất của hạt nhân",
              "question": "Kích thước, khối lượng và mômen từ mô tả hạt nhân như thế nào?",
              "source": "43.1"
            },
            {
              "slug": "nang-luong-lien-ket",
              "title": "Năng lượng liên kết và cấu trúc hạt nhân",
              "question": "Độ hụt khối cho biết gì về năng lượng và độ bền liên kết?",
              "source": "43.2"
            },
            {
              "slug": "on-dinh-va-phong-xa",
              "title": "Độ bền và các dạng phóng xạ",
              "question": "Hạt nhân đổi thành phần và năng lượng qua những kênh nào?",
              "source": "43.3"
            },
            {
              "slug": "hoat-do-va-chu-ky-ban-ra",
              "title": "Hoạt độ và chu kỳ bán rã",
              "question": "Làm thế nào suy số hạt nhân và tuổi mẫu từ hoạt độ?",
              "source": "43.4"
            }
          ]
        },
        {
          "title": "Bức xạ và các phản ứng hạt nhân",
          "topics": [
            {
              "slug": "tac-dung-sinh-hoc",
              "title": "Tác dụng sinh học và ứng dụng của bức xạ",
              "question": "Vì sao hoạt độ, liều hấp thụ và liều tương đương là các đại lượng khác nhau?",
              "source": "43.5"
            },
            {
              "slug": "phan-ung-hat-nhan",
              "title": "Năng lượng và ngưỡng phản ứng hạt nhân",
              "question": "Vì sao năng lượng phản ứng chưa đủ xác định ngưỡng trong phòng thí nghiệm?",
              "source": "43.6"
            },
            {
              "slug": "phan-hach",
              "title": "Phân hạch và phản ứng dây chuyền",
              "question": "Các neutron nối nhiều phản ứng phân hạch với nhau ra sao?",
              "source": "43.7"
            },
            {
              "slug": "nhiet-hach",
              "title": "Nhiệt hạch và năng lượng của các sao",
              "question": "Hai hạt nhân mang điện dương đến gần nhau và giải phóng năng lượng bằng cách nào?",
              "source": "43.8"
            }
          ]
        }
      ],
      "hasChapterExercises": true
    },
    {
      "slug": "24-hat-co-ban-vu-tru",
      "title": "Vật lý hạt và vũ trụ học",
      "prerequisites": [
        "thuyet-tuong-doi-hep",
        "photon",
        "phan-ra-phong-xa",
        "nhiet-do-tuyet-doi",
        "dong-luong-vat-ly",
        "chuyen-dong-hat-trong-tu-truong",
        "spin-luong-tu",
        "nguyen-ly-pauli",
        "dao-ham",
        "tich-phan"
      ],
      "supportingConcepts": [
        "phan-hat",
        "hat-ao",
        "va-cham-khoi-tam",
        "lepton",
        "hadron",
        "baryon",
        "meson",
        "quark",
        "gluon",
        "so-baryon",
        "do-la",
        "mo-hinh-chuan-hat",
        "truong-higgs",
        "do-dich-chuyen-do",
        "dinh-luat-hubble",
        "mat-do-toi-han-vu-tru",
        "vat-chat-toi",
        "nang-luong-toi",
        "buc-xa-nen-vu-tru",
        "tong-hop-hat-nhan-so-khai",
        "lam-phat-vu-tru",
        "thang-planck"
      ],
      "status": "ready",
      "number": 24,
      "sourceChapter": 44,
      "topicGroups": [
        {
          "title": "Hạt, tương tác và các mô hình cấu trúc",
          "topics": [
            {
              "slug": "lich-su-hat-co-ban",
              "title": "Các hạt cơ bản và quá trình khám phá",
              "question": "Hạt mới và phản hạt đã thay đổi bức tranh về vật chất ra sao?",
              "source": "44.1"
            },
            {
              "slug": "may-gia-toc-va-detector",
              "title": "Máy gia tốc và thiết bị ghi nhận hạt",
              "question": "Năng lượng chùm tới trở thành năng lượng tạo hạt như thế nào?",
              "source": "44.2"
            },
            {
              "slug": "hat-va-tuong-tac",
              "title": "Phân loại hạt và các tương tác",
              "question": "Những đại lượng bảo toàn cho phép hoặc loại trừ một phản ứng ra sao?",
              "source": "44.3"
            },
            {
              "slug": "quark-va-gluon",
              "title": "Quark, gluon và cấu trúc hadron",
              "question": "Điện tích, số baryon và độ lạ xác định thành phần quark như thế nào?",
              "source": "44.4"
            },
            {
              "slug": "mo-hinh-chuan",
              "title": "Mô hình chuẩn và các giới hạn",
              "question": "Sự thống nhất điện yếu và trường Higgs giải thích những điều gì?",
              "source": "44.5"
            }
          ]
        },
        {
          "title": "Sự giãn nở và lịch sử vũ trụ",
          "topics": [
            {
              "slug": "vu-tru-gian-no",
              "title": "Vũ trụ giãn nở",
              "question": "Dịch chuyển đỏ và phép đo khoảng cách cho biết gì về sự giãn nở?",
              "source": "44.6"
            },
            {
              "slug": "khoi-dau-thoi-gian",
              "title": "Vũ trụ sơ khai và khởi đầu thời gian",
              "question": "Vật lý hạt nối với bức xạ nền và sự hình thành nguyên tố ra sao?",
              "source": "44.7"
            }
          ]
        }
      ],
      "hasChapterExercises": true
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
    },
    {
      "note": "18-photon",
      "title": "Tần số quyết định năng lượng từng photon",
      "bullets": [
        "Photon có năng lượng và động lượng dù khối lượng nghỉ bằng không.",
        "Cường độ cùng tần số tăng nghĩa là số photon tăng.",
        "Sóng vô tuyến và tia gamma đều tuân theo hệ thức photon."
      ],
      "formula": "$$\n\\begin{aligned}E&=hf\\\\p&=h/\\lambda.\\end{aligned}\n$$"
    },
    {
      "note": "18-photon",
      "title": "Thế hãm đo động năng cực đại",
      "bullets": [
        "Điện áp ngược làm cản electron quang điện.",
        "Tại ngưỡng tắt dòng, ngay cả electron nhanh nhất cũng không đến được anôt.",
        "V₀ là độ lớn dương của thế hãm."
      ],
      "formula": "$$\nK_{\\max}=eV_0.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Ngưỡng quang điện phụ thuộc vật liệu",
      "bullets": [
        "Một photon truyền trọn năng lượng cho một electron trong mô hình đang xét.",
        "Công thoát lớn hơn làm động năng cực đại nhỏ hơn ở cùng tần số.",
        "Tăng cường độ dưới ngưỡng không thay thế năng lượng còn thiếu của từng photon."
      ],
      "formula": "$$\n\\begin{aligned}K_{\\max}&=hf-\\phi\\\\f_0&=\\phi/h.\\end{aligned}\n$$"
    },
    {
      "note": "18-photon",
      "title": "Đường thẳng thế hãm cho công thoát và hằng số Planck",
      "bullets": [
        "Đổi bước sóng sang tần số trước khi dựng đồ thị.",
        "Độ dốc bằng h/e và tung độ gốc bằng −φ/e.",
        "Công thoát nhạy với tạp chất bề mặt."
      ],
      "formula": "$$\nV_0=(h/e)f-\\phi/e.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Bước sóng ngắn nhất của tia X do điện áp quyết định",
      "bullets": [
        "Electron được gia tốc rồi phát bức xạ hãm khi gặp bia.",
        "Photon mạnh nhất nhận toàn bộ động năng của một electron.",
        "Tăng tốc độ electron tới ở cùng điện áp làm tăng cường độ mà không đổi bước sóng cắt."
      ],
      "formula": "$$\n\\lambda_{\\min}=hc/(eV_{AC}).\n$$"
    },
    {
      "note": "18-photon",
      "title": "Compton cần bảo toàn cả năng lượng lẫn động lượng",
      "bullets": [
        "Công thức chuẩn xét electron tự do ban đầu đứng yên.",
        "Photon cuối có thể đổi hướng và truyền năng lượng cho electron.",
        "Phổ có thành phần dịch và không dịch liên quan mức liên kết của electron."
      ],
      "formula": "$$\n\\lambda'-\\lambda=\\frac h{mc}(1-\\cos\\varphi).\n$$"
    },
    {
      "note": "18-photon",
      "title": "Tạo cặp một photon cần một vật nhận giật lùi",
      "bullets": [
        "Tổng năng lượng nghỉ của cặp bằng 2mc².",
        "Một photon tự do trong chân không không thể tự tạo cặp này.",
        "Bảo toàn động lượng làm ngưỡng thực với bia hữu hạn cao hơn mốc năng lượng nghỉ."
      ],
      "formula": "$$\nE_\\gamma\\ge2mc^2.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Hủy cặp hai photon đối xứng trong hệ khối tâm",
      "bullets": [
        "Electron và positron có động lượng ban đầu đối nhau.",
        "Hai photon cuối cùng năng lượng và bay ngược chiều.",
        "Năng lượng mỗi photon gồm cả phần năng lượng nghỉ và động năng của một hạt ban đầu."
      ],
      "formula": "$$\nE_\\gamma=\\gamma mc^2.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Các photon riêng lẻ vẫn tạo phân bố nhiễu xạ",
      "bullets": [
        "Mỗi photon tạo một sự kiện phát hiện riêng lẻ.",
        "Sau nhiều sự kiện, cường độ cho phân bố xác suất.",
        "Vân tối lý tưởng có xác suất phát hiện bằng không."
      ],
      "formula": "$$\na\\sin\\theta=m\\lambda.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Giới hạn bất định không phải lỗi dụng cụ",
      "bullets": [
        "Định xứ photon qua khe làm phân bố động lượng ngang rộng ra.",
        "Quan hệ xét vị trí và động lượng liên hợp của cùng trạng thái.",
        "Tăng độ tinh vi của thiết bị không loại bỏ giới hạn này."
      ],
      "formula": "$$\n\\Delta x\\,\\Delta p_x\\ge\\hbar/2.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Sóng có động lượng xác định trải rộng trong không gian",
      "bullets": [
        "Sóng sin đơn sắc kéo dài có số sóng xác định.",
        "Chồng các thành phần khác nhau tạo miền biên độ tập trung hơn.",
        "Phân bố động lượng rộng hơn đi cùng định xứ tốt hơn."
      ],
      "formula": "$$\np_x=\\hbar k.\n$$"
    },
    {
      "note": "18-photon",
      "title": "Xung ánh sáng ngắn đòi hỏi phổ rộng",
      "bullets": [
        "Năng lượng và tần số của photon liên hệ qua h.",
        "Thời gian xung ngắn không đồng nghĩa chu kỳ sóng ngắn.",
        "Ý nghĩa của độ rộng năng lượng và thời gian phải được xác định khi dùng bất định."
      ],
      "formula": "$$\n\\Delta t\\,\\Delta E\\ge\\hbar/2.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Động lượng quyết định bước sóng vật chất",
      "bullets": [
        "Electron, neutron và những hạt khác có thể nhiễu xạ.",
        "Dùng động lượng phù hợp miền tốc độ.",
        "Không thay quan hệ năng lượng của hạt có khối lượng bằng E=pc."
      ],
      "formula": "$$\n\\lambda=h/p.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Thí nghiệm nhiễu xạ nối hai mô tả",
      "bullets": [
        "Hiệu điện thế gia tốc xác định động năng electron.",
        "Cực đại nhiễu xạ cho phép xác định bước sóng độc lập.",
        "Sự phù hợp kiểm tra giả thuyết de Broglie."
      ],
      "formula": "$$\n\\lambda=h/\\sqrt{2meV_{ba}}.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Hạt nhân tập trung khối lượng và điện tích dương",
      "bullets": [
        "Phần lớn hạt alpha qua lá vàng chỉ lệch ít.",
        "Một số lệch góc lớn đòi hỏi lực đẩy mạnh trong vùng rất nhỏ.",
        "Bài toán trực diện với bia nặng dùng bảo toàn cơ năng."
      ],
      "formula": "$$\nK_0=qQ/(4\\pi\\epsilon_0r_{\\min}).\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Phổ vạch phản ánh mức năng lượng nguyên tử",
      "bullets": [
        "Phát photon làm nguyên tử chuyển xuống mức thấp.",
        "Hấp thụ photon cần mức cuối phù hợp.",
        "Phổ hấp thụ còn phụ thuộc các mức ban đầu có nguyên tử cư trú."
      ],
      "formula": "$$\nhf=E_i-E_f.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Quỹ đạo Bohr là một mô hình lượng tử hóa bán cổ điển",
      "bullets": [
        "Chỉ một số mômen động lượng và bán kính được phép trong mô hình.",
        "Điều kiện vòng sóng cho cách diễn giải lượng tử hóa.",
        "Nguyên lý bất định đặt giới hạn cho mô tả quỹ đạo xác định."
      ],
      "formula": "$$\n\\begin{aligned}L_n&=n\\hbar\\\\2\\pi r_n&=n\\lambda_n.\\end{aligned}\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Năng lượng liên kết âm với mốc ion hóa bằng không",
      "bullets": [
        "Động năng dương, thế năng âm và cơ năng âm.",
        "Ion hóa cần cung cấp ít nhất độ lớn cơ năng ban đầu.",
        "Photon chuyển mức mang chênh lệch cơ năng."
      ],
      "formula": "$$\nE_n=-hcR/n^2.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Hạt nhân chuyển động tạo hiệu chỉnh phổ",
      "bullets": [
        "Electron và hạt nhân cùng chuyển động quanh khối tâm.",
        "Khối lượng rút gọn hiệu chỉnh các dự đoán của mô hình.",
        "Đồng vị khác khối lượng hạt nhân có các vạch hơi lệch nhau."
      ],
      "formula": "$$\n\\mu=mM/(m+M).\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Laser cần phát xạ kích thích và đảo lộn mật độ",
      "bullets": [
        "Photon tới kích thích nguyên tử đã được kích thích.",
        "Bơm giữ hệ ngoài cân bằng nhiệt.",
        "Laser bốn mức đảo lộn giữa hai mức của chuyển mức laser, không đòi mức trên đông hơn mức cơ bản."
      ],
      "formula": "$$\nn_u>n_l.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Phổ vật đen cần hai đại lượng khác nhau",
      "bullets": [
        "Cường độ toàn phần là công suất trên diện tích.",
        "Suất phát xạ phổ còn tính trên mỗi khoảng bước sóng.",
        "Lấy tích phân phổ mới thu được cường độ toàn phần."
      ],
      "formula": "$$\nI=\\int_0^\\infty I(\\lambda)\\,d\\lambda.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Nhiệt độ tăng làm đỉnh phổ cao hơn và dịch về bước sóng ngắn",
      "bullets": [
        "Tổng công suất trên diện tích tăng theo lũy thừa bốn.",
        "Vị trí đỉnh theo bước sóng tuân theo Wien.",
        "Màu tổng hợp không chỉ là màu của bước sóng đỉnh."
      ],
      "formula": "$$\n\\begin{aligned}I&=\\sigma T^4\\\\\\lambda_mT&\\approx2{,}90\\times10^{-3}\\,\\mathrm{m\\,K}.\\end{aligned}\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Lượng tử hóa khắc phục tai biến tử ngoại",
      "bullets": [
        "Rayleigh dùng năng lượng trung bình kT cho mọi mode.",
        "Khoảng năng lượng hf lớn làm trạng thái kích thích khó được cư trú.",
        "Định luật Planck trở về giới hạn cổ điển ở bước sóng dài."
      ],
      "formula": "$$\nN_1/N_0=e^{-hf/(kT)}.\n$$"
    },
    {
      "note": "19-song-vat-chat",
      "title": "Vật chất có cùng các giới hạn bất định với photon",
      "bullets": [
        "Từng electron riêng lẻ vẫn tích lũy thành vân giao thoa.",
        "Giam hạt trong vùng nhỏ hơn làm cận động lượng tăng.",
        "Thời gian sống ngắn đi cùng thang độ rộng năng lượng lớn hơn."
      ],
      "formula": "$$\n\\begin{aligned}\\Delta x\\,\\Delta p_x&\\ge\\hbar/2\\\\\\Delta t\\,\\Delta E&\\ge\\hbar/2.\\end{aligned}\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Hàm sóng cho mật độ, tích phân cho xác suất",
      "bullets": [
        "Hàm sóng có thể phức.",
        "Xác suất trên một khoảng là tích phân bình phương môđun.",
        "Một điểm đơn lẻ của phân bố liên tục có xác suất bằng không."
      ],
      "formula": "$$\n\\rho=\\Psi^*\\Psi.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Chồng biên độ trước khi tính xác suất",
      "bullets": [
        "Tính tuyến tính cho phép chồng các nghiệm của cùng phương trình.",
        "Pha tương đối tạo những số hạng giao thoa.",
        "Một gói định xứ cần một phổ số sóng thích hợp."
      ],
      "formula": "$$\n\\Psi=C\\Psi_1+D\\Psi_2.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Sóng vật chất phi tương đối tính có tán sắc",
      "bullets": [
        "Tần số góc tỉ lệ bình phương số sóng.",
        "Vận tốc pha khác vận tốc nhóm.",
        "Gói sóng tự do có thể trải rộng theo thời gian."
      ],
      "formula": "$$\n\\omega=\\frac{\\hbar k^2}{2m}.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Phương trình Schrödinger cần một mô hình cụ thể",
      "bullets": [
        "Hamiltonian chứa động năng và thế năng.",
        "Miền và điều kiện biên là một phần của bài toán.",
        "Một nghiệm phương trình vi phân chưa chắc là trạng thái vật lý."
      ],
      "formula": "$$\ni\\hbar\\frac{\\partial\\Psi}{\\partial t}=\\hat H\\Psi.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Trạng thái dừng có mật độ không đổi",
      "bullets": [
        "Thế năng không phụ thuộc thời gian.",
        "Một trạng thái riêng năng lượng chỉ nhận pha chung theo thời gian.",
        "Năng lượng xác định không bảo đảm động lượng xác định."
      ],
      "formula": "$$\n\\Psi(x,t)=\\psi(x)e^{-iEt/\\hbar}.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Hai vách tạo lượng tử hóa trong hộp",
      "bullets": [
        "Hàm sóng bằng không tại hai đầu.",
        "Số lượng tử bắt đầu từ một.",
        "Khoảng cách mức tăng theo số lượng tử."
      ],
      "formula": "$$\nE_n=\\frac{n^2\\pi^2\\hbar^2}{2mL^2}.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Chuẩn hóa bao gồm toàn miền",
      "bullets": [
        "Biên độ lượng tử được ràng buộc bởi xác suất toàn phần.",
        "Nút có mật độ bằng không.",
        "Các khoảng bằng nhau không nhất thiết đồng xác suất."
      ],
      "formula": "$$\n\\int_{-\\infty}^{\\infty}|\\psi|^2\\,dx=1.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Giếng hữu hạn có đuôi xác suất",
      "bullets": [
        "Nghiệm bên trong dao động, bên ngoài suy giảm.",
        "Nối hàm và đạo hàm tại bước thế hữu hạn.",
        "Liên kết yếu tạo đuôi dài và số mức liên kết là hữu hạn."
      ],
      "formula": "$$\n\\kappa=\\frac{\\sqrt{2m(U_0-E)}}{\\hbar}.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Xuyên hầm nhạy với độ rộng hàng rào",
      "bullets": [
        "Truyền qua không đồng nghĩa tiêu hao cơ năng trong thế tĩnh.",
        "Công thức gần đúng cần hệ số truyền rất nhỏ.",
        "Sự phụ thuộc hàm mũ giải thích độ nhạy của STM."
      ],
      "formula": "$$\nT\\approx Ge^{-2\\kappa L}.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Dao động tử có các mức cách đều",
      "bullets": [
        "Số lượng tử bắt đầu từ không.",
        "Mức cơ bản cao hơn đáy parabol.",
        "Gần cân bằng bền, một thế năng thực có thể gần parabol."
      ],
      "formula": "$$\nE_n=\\left(n+\\frac12\\right)\\hbar\\omega.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Gaussian cơ bản đạt giới hạn bất định",
      "bullets": [
        "Hàm sóng cơ bản không phải một hạt đứng yên ở tâm.",
        "Độ lệch chuẩn khác biên độ cổ điển.",
        "Hàm sóng còn kéo dài ra miền ngoài biên độ cổ điển."
      ],
      "formula": "$$\n\\Delta x\\,\\Delta p_x=\\frac{\\hbar}{2}.\n$$"
    },
    {
      "note": "20-ham-song-schrodinger",
      "title": "Kết quả từng lần khác trung bình thống kê",
      "bullets": [
        "Đo năng lượng của chồng chập cho một trong các mức được phép.",
        "Xác suất phụ thuộc hệ số đã chuẩn hóa.",
        "Một phép đo lý tưởng trên trạng thái riêng phù hợp có thể giữ nguyên trạng thái."
      ],
      "formula": "$$\n\\langle E\\rangle=|C|^2E_1+|D|^2E_2.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Ba chiều cần đủ ba phần động năng",
      "bullets": [
        "Hàm sóng phụ thuộc ba tọa độ.",
        "Điều kiện biên là một phần của bài toán.",
        "Xác suất được tính theo thể tích."
      ],
      "formula": "$$\n-\\frac{\\hbar^2}{2m}\\nabla^2\\psi+U\\psi=E\\psi.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Hộp có ba số lượng tử nguyên dương",
      "bullets": [
        "Nghiệm không gian là tích các sóng đứng.",
        "Mỗi thành hộp là một mặt nút.",
        "Số lượng tử bằng không làm toàn hàm bằng không."
      ],
      "formula": "$$\nE=E_x+E_y+E_z.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Một mức có thể chứa nhiều trạng thái",
      "bullets": [
        "Hoán đổi ba số lượng tử có thể giữ năng lượng.",
        "Đếm trạng thái độc lập, không đếm lại pha chung.",
        "Tách biệt suy biến không gian và spin."
      ],
      "formula": "$$\nN=n_x^2+n_y^2+n_z^2.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Hydro giữ phổ năng lượng nhưng đổi cách mô tả",
      "bullets": [
        "Phổ Coulomb phi tương đối tính trùng mô hình Bohr.",
        "Orbital biểu diễn trạng thái, không phải quỹ đạo.",
        "Khối lượng rút gọn kể chuyển động hạt nhân."
      ],
      "formula": "$$\nE_n=-\\frac{Z^2E_{\\rm H}}{n^2}.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Độ lớn mômen khác một hình chiếu",
      "bullets": [
        "$\\ell$ quyết định độ lớn mômen quỹ đạo.",
        "$m_\\ell$ quyết định kết quả đo theo trục z.",
        "Không gán đồng thời ba hình chiếu xác định."
      ],
      "formula": "$$\n\\begin{aligned}L&=\\sqrt{\\ell(\\ell+1)}\\,\\hbar,\\\\L_z&=m_\\ell\\hbar.\\end{aligned}\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Bán kính có thêm yếu tố thể tích",
      "bullets": [
        "Mật độ theo thể tích và theo bán kính khác nhau.",
        "Vỏ cầu sát tâm có thể tích tiến về không.",
        "Dạng 4π dùng cho hàm không phụ thuộc góc."
      ],
      "formula": "$$\nP_{1s}(r)=4\\pi r^2|\\psi_{1s}(r)|^2.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Từ trường làm dịch các mức quỹ đạo",
      "bullets": [
        "Điện tích electron âm quyết định dấu mômen từ.",
        "Mức con có độ dịch phụ thuộc $m_\\ell$.",
        "Vạch phổ còn bị ràng buộc bởi điều kiện chọn."
      ],
      "formula": "$$\nU=m_\\ell\\mu_{\\rm B}B.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Spin là mômen nội tại",
      "bullets": [
        "Stern–Gerlach cần gradient từ trường.",
        "Hai hình chiếu spin không phải hai hướng vector cổ điển duy nhất.",
        "Spin tạo đóng góp mômen từ riêng."
      ],
      "formula": "$$\nS_z=\\pm\\frac12\\hbar.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Tổng mômen phân biệt cấu trúc tinh tế",
      "bullets": [
        "Cộng mômen quỹ đạo với spin.",
        "Với $\\ell$ bằng không chỉ có một giá trị j.",
        "Tương tác spin–quỹ đạo góp phần tách mức."
      ],
      "formula": "$$\nj=\\ell\\pm\\frac12.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Pauli quyết định cách lấp đầy",
      "bullets": [
        "Electron trong cùng orbital phải khác spin.",
        "Che chắn làm năng lượng phụ thuộc phân lớp.",
        "Cấu hình electron nối cấu trúc vi mô với tính chất hóa học."
      ],
      "formula": "$$\nN_\\ell=2(2\\ell+1).\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Tia X đặc trưng khảo sát các mức sâu",
      "bullets": [
        "Cần một lỗ trống ở mức trong.",
        "Photon mang hiệu năng lượng chuyển mức.",
        "Họ vạch khác nhau có quan hệ tần số khác nhau."
      ],
      "formula": "$$\nE_\\gamma=E_i-E_f.\n$$"
    },
    {
      "note": "21-cau-truc-nguyen-tu",
      "title": "Rối liên quan đến trạng thái toàn hệ",
      "bullets": [
        "Trạng thái có thể không tách thành tích hai trạng thái riêng.",
        "Từng kết quả đo vẫn có thể ngẫu nhiên.",
        "Qubit không cho phép đọc đồng thời mọi biên độ bằng một lần đo."
      ],
      "formula": "$$\n|\\psi\\rangle=a|0\\rangle+b|1\\rangle.\n$$"
    },
    {
      "title": "Liên kết cần một cân bằng năng lượng",
      "bullets": [
        "Sự tạo ion có chi phí năng lượng, còn tương tác giữa ion trái dấu làm giảm năng lượng.",
        "Lực đẩy ở khoảng cách ngắn ngăn các hạt nhân tiến sát vô hạn và tạo khoảng cách cân bằng.",
        "Liên kết cộng hóa trị và các tương tác lưỡng cực có cơ chế phân bố electron khác nhau."
      ],
      "formula": "$$\nU(r)=\\frac{q_1q_2}{4\\pi\\varepsilon_0r}\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Phổ quay cho biết mômen quán tính",
      "bullets": [
        "Phân tử hai nguyên tử được xem như rotor cứng quanh khối tâm.",
        "Khối lượng rút gọn và độ dài liên kết quyết định mômen quán tính.",
        "Chuyển mức lưỡng cực quay có độ biến thiên số lượng tử bằng một đơn vị."
      ],
      "formula": "$$\nE_\\ell=\\frac{\\ell(\\ell+1)\\hbar^2}{2I}\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Dao động có năng lượng điểm không",
      "bullets": [
        "Gần khoảng cách cân bằng, thế năng có thể xấp xỉ bằng một parabol.",
        "Số lượng tử dao động bắt đầu từ không nhưng năng lượng thấp nhất khác không.",
        "Photon dao động–quay nhận hiệu năng lượng của cả hai dạng chuyển động."
      ],
      "formula": "$$\nE_n=(n+\\tfrac12)\\hbar\\omega\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Mạng tinh thể và nhóm cơ sở có vai trò khác nhau",
      "bullets": [
        "Mạng mô tả các phép tịnh tiến lặp lại cấu trúc.",
        "Nhóm cơ sở quy định những nguyên tử đặt ở mỗi điểm mạng.",
        "Liên kết ion, cộng hóa trị, phân tử và kim loại tạo các tính chất vật liệu khác nhau."
      ],
      "formula": "",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Trạng thái còn trống quyết định đáp ứng điện",
      "bullets": [
        "Tương tác giữa các nguyên tử tạo thành các dải mức năng lượng rất gần nhau.",
        "Electron chỉ có thể chuyển sang một trạng thái được phép còn trống.",
        "Dải điền một phần và vùng cấm phân biệt chất dẫn, bán dẫn và cách điện."
      ],
      "formula": "$$\nE_g=E_c-E_v\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Mật độ trạng thái đếm chỗ cho electron",
      "bullets": [
        "Mỗi trạng thái không gian trong hộp chứa tối đa hai electron ngược spin.",
        "Trong mô hình ba chiều, số trạng thái trong một khoảng năng lượng được mô tả bởi g(E).",
        "Phải phân biệt số trạng thái với số electron thực sự chiếm các trạng thái ấy."
      ],
      "formula": "$$\ndN=g(E)f(E)\\,dE\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Fermi–Dirac xác định xác suất chiếm",
      "bullets": [
        "Ở nhiệt độ dương, xác suất chiếm giảm liên tục theo năng lượng.",
        "Tại mức Fermi, xác suất bằng một nửa.",
        "Ở nhiệt độ thấp, các trạng thái sâu dưới mức Fermi gần như đầy và các trạng thái cao hơn gần như trống."
      ],
      "formula": "$$\nf(E)=\\frac1{e^{(E-E_F)/(kT)}+1}\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Không độ tuyệt đối vẫn còn động năng",
      "bullets": [
        "Nguyên lý Pauli buộc electron điền nhiều trạng thái không gian khác nhau.",
        "Electron không cùng dồn vào trạng thái động năng thấp nhất.",
        "Trong khí electron tự do ba chiều, động năng trung bình bằng ba phần năm năng lượng Fermi."
      ],
      "formula": "$$\n\\overline E=\\frac35E_{F0}\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Pha tạp thay đổi hạt tải chiếm ưu thế",
      "bullets": [
        "Tạp chất cho tạo electron dẫn và ion cho dương.",
        "Tạp chất nhận tạo lỗ trống và ion nhận âm.",
        "Pha tạp không đồng nghĩa toàn mẫu có điện tích tổng cộng khác không."
      ],
      "formula": "",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Tiếp giáp tạo một rào thế nội",
      "bullets": [
        "Khuếch tán và tái hợp để lại điện tích ion trong vùng nghèo.",
        "Phân cực thuận giảm rào, còn phân cực nghịch tăng rào.",
        "Đặc tuyến diode lý tưởng mô tả dòng trong miền chưa có đánh thủng."
      ],
      "formula": "$$\nI=I_s(e^{eV/(kT)}-1)\n$$",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Electron–lỗ trống nối quang học với điện học",
      "bullets": [
        "Tái hợp có thể tạo bức xạ trong diode phát quang.",
        "Hấp thụ photon có thể tạo hạt tải trong quang diode hoặc pin mặt trời.",
        "Transistor điều khiển dòng nhờ cấu trúc tiếp giáp hoặc điện trường cổng."
      ],
      "formula": "",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Siêu dẫn là một trạng thái tập thể",
      "bullets": [
        "Trạng thái siêu dẫn tồn tại dưới những điều kiện tới hạn của nhiệt độ, từ trường và dòng điện.",
        "Mô hình BCS mô tả sự ghép cặp electron nhờ tương tác hiệu dụng liên quan đến mạng.",
        "Khe năng lượng và tính tập thể phân biệt siêu dẫn với việc chỉ giảm tán xạ thông thường."
      ],
      "formula": "",
      "note": "22-chat-ran-ban-dan"
    },
    {
      "title": "Hạt nhân có mật độ gần như không đổi",
      "bullets": [
        "Hạt nhân gồm Z proton và N neutron, với số khối A = Z + N.",
        "Mô hình bán kính tỉ lệ căn bậc ba số khối dẫn đến thể tích gần tỉ lệ với số nucleon.",
        "Đồng vị có cùng Z nhưng khác N. Khối lượng nguyên tử trung hòa còn gồm electron."
      ],
      "formula": "$$\nR=R_0A^{1/3}\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Mômen từ nối spin với cộng hưởng",
      "bullets": [
        "Thành phần mômen từ theo từ trường nhận các giá trị lượng tử hóa.",
        "Hai hướng spin của proton có năng lượng khác nhau trong từ trường ngoài.",
        "Photon cộng hưởng trao đổi đúng hiệu năng lượng giữa các mức."
      ],
      "formula": "$$\nU=-\\boldsymbol\\mu\\cdot\\mathbf B\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Năng lượng liên kết là phần giảm của năng lượng nghỉ",
      "bullets": [
        "Tách hoàn toàn hạt nhân liên kết thành các nucleon tự do cần cung cấp năng lượng.",
        "Khi dùng khối lượng nguyên tử trung hòa, phải cân bằng số electron ở hai vế.",
        "Năng lượng liên kết trung bình không đồng nhất với năng lượng tách một nucleon cụ thể."
      ],
      "formula": "$$\nE_B=\\Delta M c^2\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Các mô hình nhấn mạnh những tính chất khác nhau",
      "bullets": [
        "Mô hình giọt chất lỏng kể tương tác ngắn hạn, bề mặt, lực đẩy điện và sự ghép đôi.",
        "Mô hình vỏ mô tả sự điền các trạng thái nucleon trong thế hiệu dụng.",
        "Năng lượng liên kết lớn trên mỗi nucleon không bảo đảm mọi kênh biến đổi đều bị cấm."
      ],
      "formula": "",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Các kênh phân rã có dấu hiệu bảo toàn riêng",
      "bullets": [
        "Phát alpha làm giảm số khối bốn đơn vị và số proton hai đơn vị.",
        "Beta trừ, beta cộng và bắt electron đổi một neutron hoặc proton trong hạt nhân.",
        "Phát gamma thuần túy hạ mức năng lượng mà không đổi số proton và neutron."
      ],
      "formula": "",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Khối lượng nguyên tử quyết định ngưỡng beta",
      "bullets": [
        "Beta trừ có năng lượng khả dụng từ chênh lệch khối lượng nguyên tử mẹ và con.",
        "Đặt ΔM là khối lượng nguyên tử mẹ trừ khối lượng nguyên tử con. Beta cộng còn cần ngân sách năng lượng nghỉ của hai electron.",
        "Bắt electron có thể xảy ra khi beta cộng bị cấm về năng lượng."
      ],
      "formula": "$$\nQ_+=(\\Delta M-2m_e)c^2\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Hoạt độ là số phân rã trong một đơn vị thời gian",
      "bullets": [
        "Với một đồng vị, hằng số phân rã không đổi và không có nguồn bổ sung, số hạt nhân giảm theo hàm mũ.",
        "Hoạt độ bằng hằng số phân rã nhân số hạt nhân còn lại.",
        "Becquerel đo số phân rã mỗi giây, không đo năng lượng hấp thụ trong mô."
      ],
      "formula": "$$\n\\mathcal A=\\lambda N\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Chu kỳ bán rã và tuổi mẫu có vai trò khác nhau",
      "bullets": [
        "Chu kỳ bán rã mô tả thời gian giảm một nửa trong cùng mô hình suy giảm.",
        "Thời gian sống trung bình là nghịch đảo hằng số phân rã.",
        "Định tuổi cần hoạt độ ban đầu phù hợp và giả thiết về trao đổi đồng vị của mẫu."
      ],
      "formula": "$$\nt=\\lambda^{-1}\\ln(\\mathcal A_0/\\mathcal A)\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Năng lượng và loại bức xạ cùng ảnh hưởng tác dụng sinh học",
      "bullets": [
        "Liều hấp thụ là năng lượng truyền cho vật chất trên mỗi đơn vị khối lượng.",
        "Liều tương đương còn kể hệ số hiệu quả sinh học trong mô hình đang dùng.",
        "Khả năng xuyên sâu, đường phơi nhiễm và mô nhận bức xạ là những yếu tố cần phân biệt."
      ],
      "formula": "$$\nD=E_{\\rm abs}/m\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Ngưỡng phản ứng phải kể động lượng",
      "bullets": [
        "Q dương biểu thị phần giảm của tổng năng lượng nghỉ, còn Q âm cần năng lượng cung cấp.",
        "Với bia đứng yên, một phần động năng thuộc chuyển động chung của khối tâm.",
        "Hạt mang điện còn gặp hàng rào Coulomb. Xuyên ngầm phân biệt hàng rào cổ điển với một cấm đoán tuyệt đối."
      ],
      "formula": "$$\nK_{\\rm cm}=\\frac{M}{M+m}K\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Phân hạch có thể tạo phản ứng dây chuyền",
      "bullets": [
        "Các neutron sinh ra có thể kích thích những phân hạch tiếp theo.",
        "Chất làm chậm và thanh điều khiển thực hiện các nhiệm vụ khác nhau.",
        "Sản phẩm phân hạch tiếp tục phân rã sau khi dừng dây chuyền, nên vẫn sinh nhiệt."
      ],
      "formula": "$$\nP=\\dot N_f E_f\n$$",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Nhiệt hạch phụ thuộc năng lượng liên kết và hàng rào",
      "bullets": [
        "Ghép những hạt nhân đủ nhẹ có thể làm giảm tổng khối lượng nghỉ và giải phóng năng lượng.",
        "Trong các sao, phân bố động năng và xuyên ngầm cùng tham gia quyết định xác suất phản ứng.",
        "Chuỗi proton–proton tạo heli. Ghép hai hạt nhân bất kỳ không luôn là phản ứng tỏa năng lượng."
      ],
      "formula": "",
      "note": "23-vat-ly-hat-nhan"
    },
    {
      "title": "Phản hạt mở rộng khái niệm về vật chất",
      "bullets": [
        "Hạt và phản hạt tương ứng có cùng khối lượng, còn những điện tích thích hợp có dấu đối nhau.",
        "Tạo cặp và hủy cặp phải đồng thời bảo toàn năng lượng và động lượng.",
        "Một photon tự do không thể một mình tạo một cặp hạt tự do trong chân không."
      ],
      "formula": "$$\nE_{\\rm rest}=2m_ec^2\n$$",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Hạt ảo thuộc mô tả tương tác",
      "bullets": [
        "Hạt ảo là thành phần trung gian trong phép mô tả lượng tử, không phải một hạt tự do được quan sát riêng.",
        "Bảo toàn năng lượng và động lượng vẫn được áp dụng.",
        "Thế Yukawa có thang tầm tác dụng liên hệ với khối lượng hạt truyền tương tác trong mô hình hiệu dụng."
      ],
      "formula": "$$\nr_0\\sim\\frac{\\hbar}{mc}\n$$",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Cyclotron dùng chuyển động tròn trong từ trường",
      "bullets": [
        "Trong gần đúng phi tương đối tính, độ lớn điện tích và từ trường quyết định tần số quay.",
        "Dấu điện tích quyết định chiều quay. Bán kính tăng khi động lượng tăng.",
        "Khi hiệu ứng tương đối tính đáng kể, không thể giữ nguyên công thức tần số không phụ thuộc năng lượng."
      ],
      "formula": "$$\nf=\\frac{|q|B}{2\\pi m}\n$$",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Năng lượng khối tâm quyết định khả năng tạo hạt",
      "bullets": [
        "Một phần năng lượng trong thí nghiệm bia cố định gắn với chuyển động chung của hệ.",
        "Hai chùm có động lượng bằng nhau và ngược hướng đưa hệ phòng thí nghiệm về hệ khối tâm.",
        "Tại ngưỡng tạo các hạt có khối lượng, sản phẩm không còn động năng tương đối trong hệ khối tâm."
      ],
      "formula": "$$\nE_{\\rm cm}^2=E_{\\rm tot}^2-p_{\\rm tot}^2c^2\n$$",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Các quy tắc chọn lọc phải được xét đồng thời",
      "bullets": [
        "Điện tích và năng lượng đủ chưa bảo đảm phản ứng xảy ra.",
        "Số baryon và số lepton được dùng cùng những điều kiện của mô hình phản ứng đang xét.",
        "Độ lạ được bảo toàn trong tương tác mạnh và điện từ nhưng có thể thay đổi trong tương tác yếu."
      ],
      "formula": "",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Quark giải thích điện tích của hadron",
      "bullets": [
        "Trong mô hình thành phần hóa trị thông thường, baryon gồm ba quark và meson gồm quark với phản quark.",
        "Điện tích, số baryon và các số lượng tử mùi được cộng đại số.",
        "Proton có thành phần uud, còn neutron có thành phần udd."
      ],
      "formula": "",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Gluon và màu mô tả tương tác mạnh",
      "bullets": [
        "Màu là tên một điện tích lượng tử, khác màu sắc quang học.",
        "Gluon truyền tương tác và có thể làm thay đổi trạng thái màu của quark.",
        "Hadron quan sát được có cấu trúc trạng thái trung hòa màu phù hợp mô hình."
      ],
      "formula": "",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Mô hình chuẩn có phạm vi và giới hạn",
      "bullets": [
        "Quark, lepton và các hạt truyền tương tác tổ chức các phản ứng trong mô hình chuẩn.",
        "Thống nhất điện yếu nối tương tác điện từ với tương tác yếu, còn trường Higgs có vai trò trong cơ chế tạo khối lượng.",
        "Hấp dẫn lượng tử, vật chất tối và nhiều câu hỏi về vũ trụ vẫn cần những mô tả bổ sung."
      ],
      "formula": "",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Dịch chuyển đỏ là một tỉ số bước sóng",
      "bullets": [
        "So sánh cùng một vạch phổ ở nguồn và ở phép đo để xác định độ dịch chuyển đỏ.",
        "Công thức Doppler tương đối tính thuộc mô hình chuyển động tương đối thích hợp.",
        "Dịch chuyển đỏ vũ trụ còn gắn trực tiếp với sự thay đổi hệ số tỉ lệ trong khi photon truyền đi."
      ],
      "formula": "$$\n1+z=\\frac{\\lambda_o}{\\lambda_e}\n$$",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Định luật Hubble nối vận tốc lùi với khoảng cách",
      "bullets": [
        "Quan hệ Hubble tại một thời điểm cần nêu loại khoảng cách và miền mô hình.",
        "Nghịch đảo Hubble cho một thang thời gian, không tự cho tuổi chính xác của mọi mô hình vũ trụ.",
        "Mật độ tới hạn và các tham số thành phần giúp mô tả động lực giãn nở."
      ],
      "formula": "$$\nv=H_0r\n$$",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Vũ trụ sơ khai nguội đi khi giãn nở",
      "bullets": [
        "Những thời kỳ tương tác và tạo hạt được phân biệt bằng các thang nhiệt độ, năng lượng và thời gian.",
        "Tổng hợp hạt nhân sơ khai tạo các nguyên tố nhẹ, khác với sự hình thành nguyên tử trung hòa muộn hơn.",
        "Khi mật độ electron tự do giảm, photon có thể truyền xa và lưu lại thông tin về lần tán xạ cuối."
      ],
      "formula": "",
      "note": "24-hat-co-ban-vu-tru"
    },
    {
      "title": "Bức xạ nền nối nhiệt độ với sự giãn nở",
      "bullets": [
        "Bức xạ nền có phổ gần vật đen và bước sóng tăng theo hệ số tỉ lệ của vũ trụ.",
        "Trong mô hình giãn nở đoạn nhiệt đang xét, nhiệt độ bức xạ giảm theo nghịch đảo hệ số tỉ lệ.",
        "Các giả thuyết về lạm phát và bất đối xứng vật chất cần được phân biệt với các dữ kiện quan sát."
      ],
      "formula": "$$\nT\\propto a^{-1}\n$$",
      "note": "24-hat-co-ban-vu-tru"
    }
  ],
  "illustration": "field",
  "contentPolicy": "full-source-translation"
}
