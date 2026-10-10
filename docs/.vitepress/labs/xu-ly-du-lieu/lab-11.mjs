// Module bài tập phòng Lab: Lab 11: Kỷ luật đo lường cho LLM: schema, nhãn tay & hậu kiểm
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-11-llm-du-lieu-phi-cau-truc",
  "title": "Lab 11: Kỷ luật đo lường cho LLM: schema, nhãn tay & hậu kiểm",
  "dataset": {
    "name": "Mẫu đánh giá gán nhãn thủ công (Gold Standard Santiago)",
    "type": "CSV & JSON Văn bản phi cấu trúc",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/reviews.csv.gz",
    "description": "Bộ dữ liệu chuẩn mực gồm các đoạn đánh giá của du khách kèm nhãn cảm xúc và phân loại sự cố (vệ sinh, ồn ào, địa điểm) do chuyên gia gán nhãn, phục vụ thẩm định trích xuất thông tin qua mô hình ngôn ngữ lớn (LLM) và Pydantic."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Chọn mẫu ngẫu nhiên tái lập được và ước tính chi phí token",
      "prompt": "Khi làm việc với các API mô hình ngôn ngữ lớn (LLM) có thu phí, việc thử nghiệm trên toàn bộ 690 nghìn dòng là bất khả thi. Hãy rút một mẫu ngẫu nhiên 100 đánh giá có cố định hạt giống ngẫu nhiên `random_state=42`. Sau đó, viết hàm ước tính số lượng token văn bản và tính toán chi phí trước khi gọi API.",
      "prediction": "Quy tắc kinh nghiệm trong xử lý ngôn ngữ tự nhiên: trung bình 1 từ tiếng Anh hoặc tiếng Tây Ban Nha tương ứng khoảng 1.3 token, hoặc 100 từ tương đương khoảng 130 token. Ước tính trước giúp kỹ sư kiểm soát ngân sách điện toán đám mây.",
      "solutionBasic": "import pandas as pd\n\n# Rút mẫu 100 dòng tái lập được\nmau_100 = rv['comments'].dropna().sample(n=100, random_state=42)\n\n# Ước tính token thô dựa trên số từ\ntong_so_tu = mau_100.astype(str).str.split().str.len().sum()\nuoc_tinh_tokens = int(tong_so_tu * 1.3)\ngia_moi_1k_tokens = 0.0005 # 0.0005 USD\nuoc_tinh_chi_phi = (uoc_tinh_tokens / 1000) * gia_moi_1k_tokens\n\nprint(f'Tổng số từ: {tong_so_tu:,} -> Ước tính tokens: {uoc_tinh_tokens:,}')\nprint(f'Chi phí dự kiến cho 100 bình luận: ${uoc_tinh_chi_phi:.4f} USD')",
      "solutionAdvanced": "def uoc_tinh_chi_phi_llm(series_text: pd.Series, don_gia_1k_token: float = 0.0005) -> dict:\n    \"\"\"Ước tính token và chi phí API trước khi gửi yêu cầu.\"\"\"\n    n_samples = len(series_text)\n    # Đếm ký tự trung bình (1 token ~ 4 ký tự)\n    total_chars = series_text.astype(str).str.len().sum()\n    est_tokens = int(total_chars / 4)\n    cost = (est_tokens / 1000) * don_gia_1k_token\n    return {\n        'so_mau': n_samples,\n        'tong_ky_tu': int(total_chars),\n        'uoc_tinh_tokens': est_tokens,\n        'chi_phi_usd': round(cost, 4)\n    }\n\nprint(uoc_tinh_chi_phi_llm(mau_100))",
      "explanation": "Kỷ luật hàng đầu khi ứng dụng AI tạo sinh vào kỹ thuật dữ liệu: Không bao giờ chạy một kịch bản gọi API tự động nếu chưa có bước ước tính trần chi phí tối đa (Cost Cap).",
      "verification": "assert len(mau_100) == 100\nassert uoc_tinh_tokens > 0"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Thiết kế Schema Pydantic có Enum để ép cấu trúc phản hồi của LLM",
      "prompt": "Định nghĩa một lớp Schema dữ liệu bằng thư viện Pydantic mang tên `DanhGiaChuyenSau`. Yêu cầu đầu ra gồm: (1) `cam_xuc` thuộc Enum ['TICH_CUC', 'TRUNG_TINH', 'TIEU_CUC']; (2) `diem_so` là số nguyên từ 1 đến 5; (3) `van_de_chinh` thuộc Enum ['VE_SINH', 'TIENG_ON', 'VI_TRI', 'KHONG_CO']; (4) `trich_dan_chung_cu` là chuỗi trích dẫn nguyên văn từ bình luận làm bằng chứng.",
      "prediction": "Schema Pydantic đóng vai trò là tầng phòng thủ đầu tiên: mọi phản hồi từ mô hình nếu thiếu trường, sai kiểu dữ liệu hoặc bịa đặt giá trị ngoài Enum sẽ lập tức bị ném ngoại lệ ValidationError ngay tại thời điểm nhận.",
      "solutionBasic": "from pydantic import BaseModel, Field, ValidationError\nfrom enum import Enum\n\nclass CamXucEnum(str, Enum):\n    TICH_CUC = 'TICH_CUC'\n    TRUNG_TINH = 'TRUNG_TINH'\n    TIEU_CUC = 'TIEU_CUC'\n\nclass DanhGiaChuyenSau(BaseModel):\n    cam_xuc: CamXucEnum\n    diem_so: int = Field(ge=1, le=5)\n    trich_dan_chung_cu: str",
      "solutionAdvanced": "class VanDeEnum(str, Enum):\n    VE_SINH = 'VE_SINH'\n    TIENG_ON = 'TIENG_ON'\n    VI_TRI = 'VI_TRI'\n    KHONG_CO = 'KHONG_CO'\n\nclass HoSoDanhGiaLLM(BaseModel):\n    \"\"\"Schema Pydantic nghiêm ngặt kiểm soát đầu ra của LLM.\"\"\"\n    cam_xuc: CamXucEnum\n    diem_so: int = Field(..., ge=1, le=5, description='Điểm đánh giá từ 1 đến 5')\n    van_de: VanDeEnum\n    trich_dan_chung_cu: str = Field(..., min_length=3, description='Trích dẫn nguyên văn bằng chứng')\n\n# Thử nghiệm kiểm tra tính hợp lệ\ndata_dung = {'cam_xuc': 'TICH_CUC', 'diem_so': 5, 'van_de': 'KHONG_CO', 'trich_dan_chung_cu': 'Rất sạch sẽ'}\nobj = HoSoDanhGiaLLM(**data_dung)\nprint('Thẩm định Schema thành công:', obj.model_dump())",
      "explanation": "Bằng cách sử dụng Pydantic kết hợp với tính năng Structured Outputs của các API hiện đại, mô hình bị ràng buộc toán học để luôn sinh ra cú pháp JSON hợp lệ 100% tuân thủ chặt chẽ Schema đã khai báo.",
      "verification": "try:\n    HoSoDanhGiaLLM(cam_xuc='KHONG_HOP_LE', diem_so=10, van_de='KHONG_CO', trich_dan_chung_cu='abc')\n    assert False, 'Phải ném ValidationError với dữ liệu sai!'\nexcept ValidationError:\n    assert True"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Đo lường độ chính xác (Accuracy, Precision, Recall) trên tập nhãn chuẩn",
      "prompt": "Cho một tập chuẩn mực (Gold Standard) gồm 20 đánh giá đã được con người gán nhãn thủ công và kết quả dự đoán của LLM tương ứng. Hãy viết hàm tính toán ma trận nhầm lẫn (Confusion Matrix) và các độ đo: Độ chính xác tổng thể (Accuracy), Độ chuẩn xác (Precision) và Độ thu hồi (Recall) cho nhãn 'TIEU_CUC'.",
      "prediction": "Đối với các bài toán phát hiện sự cố hoặc khiếu nại của khách hàng, độ thu hồi (Recall) của nhãn Tiêu cực là quan trọng nhất, vì bỏ sót một lời phàn nàn nghiêm trọng sẽ gây tổn thất lớn hơn việc kiểm tra nhầm một bình luận trung tính.",
      "solutionBasic": "nhan_that = ['TICH_CUC', 'TIEU_CUC', 'TICH_CUC', 'TIEU_CUC', 'TRUNG_TINH']\nnhan_llm  = ['TICH_CUC', 'TIEU_CUC', 'TRUNG_TINH', 'TICH_CUC', 'TRUNG_TINH']\n\n# Tính Accuracy\ndung = sum(1 for t, p in zip(nhan_that, nhan_llm) if t == p)\naccuracy = dung / len(nhan_that)\nprint(f'Độ chính xác Accuracy: {accuracy:.1%}')",
      "solutionAdvanced": "def danh_gia_hieu_nang_llm(y_true: list[str], y_pred: list[str], nhan_target: str = 'TIEU_CUC') -> dict:\n    \"\"\"Đo lường chi tiết hiệu năng phân loại văn bản của AI.\"\"\"\n    tp = sum(1 for t, p in zip(y_true, y_pred) if t == nhan_target and p == nhan_target)\n    fp = sum(1 for t, p in zip(y_true, y_pred) if t != nhan_target and p == nhan_target)\n    fn = sum(1 for t, p in zip(y_true, y_pred) if t == nhan_target and p != nhan_target)\n    tn = sum(1 for t, p in zip(y_true, y_pred) if t != nhan_target and p != nhan_target)\n    \n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0\n    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0\n    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0\n    \n    return {\n        'TP': tp, 'FP': fp, 'FN': fn, 'TN': tn,\n        'Precision': round(precision, 3),\n        'Recall': round(recall, 3),\n        'F1_Score': round(f1, 3)\n    }\n\nmetrics = danh_gia_hieu_nang_llm(nhan_that, nhan_llm, 'TIEU_CUC')\nprint('Chỉ số kiểm thử LLM:\\n', metrics)",
      "explanation": "Đánh giá LLM không được dựa vào 'cảm giác' đọc thử vài ví dụ ngẫu nhiên. Bắt buộc phải xây dựng bộ dữ liệu vàng (Gold Standard) từ 100 đến 200 mẫu gán nhãn thủ công để đo lường bằng các con số toán học khách quan.",
      "verification": "assert 0.0 <= metrics['Precision'] <= 1.0\nassert 0.0 <= metrics['Recall'] <= 1.0"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Hậu kiểm tự động chống ảo giác (Automatic Hallucination Guardrail)",
      "prompt": "Viết hàm hậu kiểm `kiem_tra_ao_giac(van_ban_goc: str, trich_dan_chung_cu: str) -> bool` kiểm tra xem đoạn văn bản trích dẫn làm bằng chứng do LLM trả về có thực sự xuất hiện nguyên văn trong bình luận gốc của du khách hay không. Nếu LLM tự bịa ra bằng chứng, gắn cờ cảnh báo 'ẢO_GIÁC'.",
      "prediction": "Ảo giác trích dẫn (Citation Hallucination) là hiện tượng mô hình tự sáng tác ra một câu văn nghe có vẻ hợp lý nhưng không hề có trong ngữ cảnh nguồn. Phép kiểm tra chuỗi đơn giản `evidence in raw_text` là chốt chặn hiệu quả nhất để ngăn ngừa lỗi này.",
      "solutionBasic": "def kiem_tra_ao_giac_cb(goc: str, trich_dan: str) -> bool:\n    if not trich_dan or len(trich_dan.strip()) == 0:\n        return False\n    return trich_dan.strip().lower() in goc.strip().lower()",
      "solutionAdvanced": "def hau_kiem_an_toan_llm(van_ban_goc: str, ket_qua_llm: dict) -> dict:\n    \"\"\"Chốt chặn hậu kiểm tự động phát hiện ảo giác.\"\"\"\n    raw_lower = van_ban_goc.lower()\n    quote = ket_qua_llm.get('trich_dan_chung_cu', '').strip().lower()\n    \n    co_trong_nguon = quote in raw_lower\n    return {\n        'hop_le': co_trong_nguon,\n        'ket_qua': ket_qua_llm,\n        'canh_bao': None if co_trong_nguon else 'PHÁT HIỆN ẢO GIÁC: Trích dẫn không có trong văn bản gốc!'\n    }",
      "explanation": "Kỹ thuật neo trích dẫn (Grounded Extraction): Bắt buộc Schema phải có trường trích dẫn bằng chứng và hậu kiểm sự tồn tại của nó giúp tăng độ tin cậy của đường ống dữ liệu tự động lên mức sản xuất.",
      "verification": "assert kiem_tra_ao_giac_cb('Phòng rất sạch và đẹp', 'rất sạch') == True\nassert kiem_tra_ao_giac_cb('Phòng rất sạch và đẹp', 'nhà vệ sinh bẩn') == False"
    }
  ]
};
