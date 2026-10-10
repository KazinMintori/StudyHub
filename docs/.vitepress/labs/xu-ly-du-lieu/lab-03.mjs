// Module bài tập phòng Lab: Lab 3: NumPy và tư duy vector hoá
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-03-numpy",
  "title": "Lab 3: NumPy và tư duy vector hoá",
  "dataset": {
    "name": "Ma trận giá phòng & Mảng đa chiều NumPy",
    "type": "NumPy ndarray (Bộ nhớ liên tục C-order)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "description": "Mảng số thực trích xuất từ cột giá phòng, số đêm tối thiểu và số đánh giá của 18.534 chỗ ở, phục vụ huấn luyện tư duy vector hóa và tối ưu hóa bộ nhớ đệm CPU."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Khảo sát cấu trúc mảng đa chiều (shape, ndim, dtype, itemsize)",
      "prompt": "Khởi tạo một mảng 2 chiều đại diện cho bảng thuộc tính gồm 4 chỗ ở, mỗi chỗ ở gồm 3 chỉ số: [giá đêm, số đêm tối thiểu, số đánh giá]. Hãy in và phân tích ý nghĩa của các thuộc tính: `shape`, `ndim`, `dtype`, `itemsize`, `nbytes`.",
      "prediction": "Mảng NumPy lưu trữ dữ liệu đồng nhất (homogeneous) trong một vùng nhớ liên tục (contiguous buffer), mỗi phần tử chiếm số byte cố định tùy theo kiểu dữ liệu (ví dụ float64 chiếm 8 bytes), giúp CPU tải hàng loạt dữ liệu vào bộ nhớ đệm L1/L2.",
      "solutionBasic": "import numpy as np\n\ndata_list = [\n    [45000, 2, 15],\n    [32000, 1, 8],\n    [98000, 3, 42],\n    [60000, 2, 0]\n]\narr = np.array(data_list, dtype=np.float64)\nprint('Shape:', arr.shape)\nprint('Số chiều ndim:', arr.ndim)\nprint('Kiểu dữ liệu dtype:', arr.dtype)",
      "solutionAdvanced": "import numpy as np\n\ndef phan_tich_bo_nho_mang(arr: np.ndarray) -> dict:\n    \"\"\"Phân tích chi tiết mức độ tiêu thụ bộ nhớ RAM của mảng NumPy.\"\"\"\n    return {\n        'hinh_dang': arr.shape,\n        'so_chieu': arr.ndim,\n        'tong_phan_tu': arr.size,\n        'kich_thuoc_1_so_bytes': arr.itemsize,\n        'tong_dung_luong_bytes': arr.nbytes,\n        'bo_nho_lien_tuc_C': arr.flags['C_CONTIGUOUS']\n    }\n\ninfo = phan_tich_bo_nho_mang(arr)\nprint(info)",
      "explanation": "Khác với danh sách Python (chứa con trỏ trỏ đến các đối tượng rời rạc trong RAM), mảng NumPy lưu các giá trị thô kề nhau, giảm thiểu chi phí giải con trỏ (pointer chasing) và hỗ trợ tính toán song song SIMD.",
      "verification": "assert arr.shape == (4, 3)\nassert arr.ndim == 2\nassert arr.nbytes == 4 * 3 * 8"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Phân biệt bản chiếu (View) và bản sao độc lập (Copy) khi cắt lát",
      "prompt": "Thực hiện thao tác cắt lát `sub = arr[0:2, 0:2]`. Thay đổi giá trị phần tử `sub[0, 0] = 99999`. Quan sát mảng gốc `arr`. Làm lại thí nghiệm nhưng dùng `.copy()` để bảo toàn dữ liệu gốc.",
      "prediction": "Cắt lát cơ bản (Basic Slicing) trong NumPy chỉ tạo một đối tượng xem (View) chia sẻ chung con trỏ dữ liệu gốc. Mọi thay đổi trên View sẽ lập tức làm biến đổi mảng gốc. Để tạo vùng nhớ mới hoàn toàn độc lập, bắt buộc phải dùng `.copy()`.",
      "solutionBasic": "# Thí nghiệm View làm biến đổi mảng gốc\narr_goc = np.array([[10, 20], [30, 40]])\nview_arr = arr_goc[0:1]\nview_arr[0, 0] = 999\nprint('Mảng gốc bị thay đổi:', arr_goc[0, 0]) # In ra 999",
      "solutionAdvanced": "# Thí nghiệm Copy bảo toàn dữ liệu gốc\narr_an_toan = np.array([[10, 20], [30, 40]])\ncopy_arr = arr_an_toan[0:1].copy()\ncopy_arr[0, 0] = 999\nprint('Mảng gốc vẫn an toàn:', arr_an_toan[0, 0]) # Vẫn là 10\nassert arr_an_toan[0, 0] == 10",
      "explanation": "NumPy thiết kế mặc định tạo View để tiết kiệm bộ nhớ và tránh chi phí sao chép mảng hàng triệu dòng. Tuy nhiên trong quy trình làm sạch dữ liệu, sửa đổi trên View là nguồn gốc sinh ra các lỗi dữ liệu ngầm khó truy vết.",
      "verification": "assert view_arr.base is arr_goc\nassert copy_arr.base is None"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Lọc dữ liệu bằng mặt nạ Boolean (Boolean Masking) và Toán tử bitwise",
      "prompt": "Cho mảng giá phòng 1 chiều gồm các mức giá: [25000, 80000, 150000, 45000, 320000, 60000]. Hãy lọc ra các chỗ ở thỏa mãn điều kiện: giá lớn hơn hoặc bằng 50.000 và nhỏ hơn 200.000 CLP. Giải thích tại sao bắt buộc dùng toán tử `&` thay vì từ khóa `and`.",
      "prediction": "Từ khóa `and` của Python đánh giá tính đúng sai của toàn bộ đối tượng mảng (ném lỗi ValueError: The truth value of an array with more than one element is ambiguous). Bắt buộc phải dùng toán tử bitwise `&` để thực hiện phép AND logic trên từng cặp phần tử.",
      "solutionBasic": "gia = np.array([25000, 80000, 150000, 45000, 320000, 60000])\n# Đặt từng điều kiện trong ngoặc đơn\nmat_na = (gia >= 50000) & (gia < 200000)\nket_qua = gia[mat_na]\nprint('Chỗ ở tầm trung:', ket_qua)",
      "solutionAdvanced": "def loc_gia_chuan(mang_gia: np.ndarray, min_val: float, max_val: float) -> np.ndarray:\n    \"\"\"Lọc mảng vector hóa có bảo toàn dữ liệu.\"\"\"\n    c1 = (mang_gia >= min_val)\n    c2 = (mang_gia < max_val)\n    # Kết hợp hai mặt nạ Boolean C-level\n    return mang_gia[c1 & c2]\n\nloc_chuan = loc_gia_chuan(gia, 50000, 200000)\nprint('Kết quả lọc chuẩn mực:', loc_chuan)",
      "explanation": "Trong Python, toán tử bitwise `&` có độ ưu tiên cao hơn các toán tử so sánh `>=` và `<`. Vì vậy, việc bọc các biểu thức điều kiện trong ngoặc đơn `(gia >= min_val) & (gia < max_val)` là bắt buộc về mặt cú pháp.",
      "verification": "assert np.array_equal(ket_qua, np.array([80000, 150000, 60000]))\nassert len(ket_qua) == 3"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Lan truyền kích thước (Broadcasting) và Quy tắc căn chỉnh trục từ cuối",
      "prompt": "Cho ma trận giá phòng kích thước (4, 3) đại diện cho 4 chỗ ở qua 3 mùa du lịch. Giả sử chính quyền áp thuế lưu trú cố định theo từng mùa gồm 3 giá trị: `thue = np.array([1500, 2000, 1800])`. Hãy cộng thuế này vào từng chỗ ở bằng cơ chế Broadcasting và giải thích quy tắc so khớp trục.",
      "prediction": "Mảng thuế có hình dạng (3,). Khi so khớp với ma trận (4, 3), NumPy duyệt từ trục cuối sang trục đầu: trục cuối cùng đều bằng 3 nên khớp hợp lệ, mảng thuế được tự động kéo giãn dọc theo trục 0 để cộng vào cả 4 hàng mà không tốn thêm RAM.",
      "solutionBasic": "ma_tran_gia = np.array([\n    [40000, 50000, 45000],\n    [30000, 35000, 32000],\n    [80000, 95000, 90000],\n    [60000, 70000, 65000]\n])\nthue = np.array([1500, 2000, 1800])\n# Broadcasting tự động diễn ra\ngia_sau_thue = ma_tran_gia + thue\nprint('Giá sau thuế:\\n', gia_sau_thue)",
      "solutionAdvanced": "# Thí nghiệm cộng theo cột (chuẩn hóa theo từng chỗ ở)\nphi_dich_vu_phong = np.array([500, 300, 1000, 700]) # Hình dạng (4,)\n# Để cộng theo hàng, bắt buộc thêm trục mới biến thành (4, 1)\ngia_kem_phi = ma_tran_gia + phi_dich_vu_phong[:, np.newaxis]\nprint('Giá sau phí dịch vụ riêng từng phòng:\\n', gia_kem_phi)",
      "explanation": "Quy tắc Broadcasting: Hai chiều khớp nhau khi chúng bằng nhau hoặc một trong hai chiều bằng 1. Nếu muốn cộng một vector 1D theo chiều dọc (cột), bắt buộc dùng `col[:, np.newaxis]` để đổi hình dạng từ (N,) thành (N, 1).",
      "verification": "assert gia_sau_thue.shape == (4, 3)\nassert gia_sau_thue[0, 0] == 41500\nassert gia_kem_phi[0, 0] == 40500"
    },
    {
      "id": "task-5",
      "title": "Bài 5: Phép toán tổng hợp theo trục (Axis Aggregation) và Giữ nguyên số chiều",
      "prompt": "Với ma trận giá phòng kích thước (4, 3), hãy tính: (1) Giá trung bình của từng mùa trên toàn bộ các phòng (gom theo hàng, giữ kết quả theo cột); (2) Giá trung bình của từng phòng qua các mùa (gom theo cột, giữ kết quả theo hàng). Sử dụng tham số `keepdims=True` để chuẩn hóa dữ liệu.",
      "prediction": "Tham số `axis=0` sẽ thu gọn theo chiều dọc của hàng, trả về mảng 1D có 3 phần tử. Tham số `axis=1` sẽ thu gọn theo chiều ngang của cột, trả về mảng 1D có 4 phần tử. Khi bật `keepdims=True`, mảng kết quả giữ nguyên số chiều (1, 3) hoặc (4, 1), giúp thực hiện phép trừ chuẩn hóa trực tiếp mà không cần reshape.",
      "solutionBasic": "tb_theo_mua = ma_tran_gia.mean(axis=0)\ntb_theo_phong = ma_tran_gia.mean(axis=1)\nprint('Trung bình từng mùa (axis=0):', tb_theo_mua)\nprint('Trung bình từng phòng (axis=1):', tb_theo_phong)",
      "solutionAdvanced": "# Chuẩn hóa trừ đi trung bình phòng bằng keepdims=True\ntb_phong_giu_chieu = ma_tran_gia.mean(axis=1, keepdims=True)\nlech_chuan_phong = ma_tran_gia - tb_phong_giu_chieu\nprint('Độ lệch so với trung bình phòng:\\n', lech_chuan_phong)",
      "explanation": "Ghi nhớ quy tắc trục: `axis=0` là tiêu biến trục hàng (chạy dọc theo các hàng để gom về 1 dòng kết quả); `axis=1` là tiêu biến trục cột (chạy ngang qua các cột để gom về 1 cột kết quả).",
      "verification": "assert tb_theo_mua.shape == (3,)\nassert tb_phong_giu_chieu.shape == (4, 1)\nassert np.allclose(lech_chuan_phong.mean(axis=1), 0.0)"
    }
  ]
};
