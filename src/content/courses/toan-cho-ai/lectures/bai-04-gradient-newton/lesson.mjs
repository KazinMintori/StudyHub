export const lesson = {
  "number": 4,
  "slug": "bai-04-gradient-newton",
  "title": "Tối ưu không ràng buộc và ràng buộc đẳng thức",
  "prerequisites": [
    "gradient",
    "hessian",
    "ma-tran-psd",
    "he-phuong-trinh",
    "kkt"
  ],
  "supportingConcepts": [
    "tham-so-toan-hoc",
    "chuan",
    "dao-ham",
    "tim-kiem-duong",
    "tu-tuong-hop",
    "mien-kha-thi"
  ],
  "status": "ready",
  "description": "Theo dõi từng bước của phương pháp gradient, backtracking và Newton. Giải hệ Newton–KKT khi có ràng buộc đẳng thức.",
  "topicGroups": [
    {
      "title": "I. Phương pháp điểm trong nâng cao",
      "description": "Khởi tạo khả thi qua Pha I, độ phức tạp trên nón chính quy và thuật toán Primal-Dual.",
      "topics": [
        {
          "slug": "phuong-phap-pha-1-va-khoi-tao",
          "title": "Phương pháp Pha I và tìm điểm khả thi khởi đầu",
          "question": "Khi không có sẵn điểm xuất phát khả thi nghiêm ngặt, làm sao bắt đầu phương pháp điểm trong?",
          "source": "§11.4"
        },
        {
          "slug": "do-phuc-tap-va-bat-dang-thuc-tong-quat",
          "title": "Độ phức tạp và điểm trong trên nón chính quy",
          "question": "Phương pháp điểm trong cần chính xác bao nhiêu bước lặp Newton và mở rộng cho nón Lorentz/PSD thế nào?",
          "source": "§11.5–11.6"
        },
        {
          "slug": "phuong-phap-primal-dual",
          "title": "Phương pháp Điểm trong Primal-Dual",
          "question": "Vì sao cập nhật đồng thời biến nguyên thủy và đối ngẫu lại vượt trội hơn phương pháp hàm chắn truyền thống?",
          "source": "§11.7–11.8"
        }
      ]
    }
  ]
}
