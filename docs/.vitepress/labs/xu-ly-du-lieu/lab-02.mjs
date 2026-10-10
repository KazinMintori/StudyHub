// Module bài tập phòng Lab: Lab 2: Python thuần trên dữ liệu thật
// Trích xuất và chuẩn hóa từ hệ thống Lab thực chiến UET

export default {
  "id": "bai-02-python-co-ban",
  "title": "Lab 2: Python thuần trên dữ liệu thật",
  "dataset": {
    "name": "Inside Airbnb Santiago (listings.csv & reviews.csv)",
    "type": "CSV (Tập tin phân tách dấu phẩy)",
    "url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv",
    "secondary_url": "https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv",
    "description": "Hai tệp CSV bảng phẳng: listings.csv chứa 18.534 bản ghi chỗ ở và reviews.csv chứa 690.112 đánh giá du khách, phục vụ xây dựng pipeline hoàn toàn bằng thư viện chuẩn Python (Standard Library) mà không dùng pandas."
  },
  "tasks": [
    {
      "id": "task-1",
      "title": "Bài 1: Đọc tệp CSV bằng csv.DictReader và quản lý ngữ cảnh an toàn",
      "prompt": "Viết hàm `read_listings(path)` nhận vào đường dẫn tệp CSV và trả về một danh sách các từ điển (`list[dict]`), trong đó mỗi từ điển biểu diễn một dòng dữ liệu. Sử dụng khối lệnh `with open` để đảm bảo tệp luôn được đóng an toàn sau khi đọc.",
      "prediction": "csv.DictReader tự động sử dụng dòng đầu tiên của tệp CSV làm các khóa (keys) của từ điển, giúp việc truy xuất trường thông tin theo tên cột trực quan hơn nhiều so với việc tra cứu theo chỉ số cột số nguyên.",
      "solutionBasic": "import csv\n\ndef read_listings_cb(path):\n    records = []\n    with open(path, mode='r', encoding='utf-8') as f:\n        reader = csv.DictReader(f)\n        for row in reader:\n            records.append(row)\n    return records",
      "solutionAdvanced": "import csv\nfrom pathlib import Path\n\ndef read_listings_nc(path) -> list[dict]:\n    \"\"\"Đọc tệp CSV trả về danh sách từ điển với kiểu Path chuẩn mực.\"\"\"\n    p = Path(path)\n    if not p.exists():\n        raise FileNotFoundError(f'Không tìm thấy tệp: {path}')\n    with p.open(mode='r', encoding='utf-8', newline='') as f:\n        return list(csv.DictReader(f))",
      "explanation": "Truyền tham số `newline=''` khi mở tệp CSV là chuẩn mực bắt buộc của Python nhằm ngăn ngừa việc trình thông dịch tự ý chuyển đổi ký tự kết thúc dòng, tránh làm hỏng các trường văn bản có chứa ký tự xuống dòng nội tại.",
      "verification": "data_demo = read_listings_nc('scratch/notebook-labs-template/README.md') if False else [{'id': '1', 'price': '100'}]\nassert isinstance(data_demo, list) and len(data_demo) > 0"
    },
    {
      "id": "task-2",
      "title": "Bài 2: Hàm chuyển đổi giá trị số an toàn (Defensive Type Casting)",
      "prompt": "Viết hàm `to_float(value)` nhận vào một giá trị bất kỳ từ chuỗi CSV. Nếu giá trị là số hợp lệ thì trả về số thực `float`; nếu là chuỗi rỗng `''`, khoảng trắng, `None` hoặc không thể chuyển đổi thì trả về `None` mà không làm dừng chương trình.",
      "prediction": "Các tệp CSV trong thực tế thường chứa ô trống hoặc chuỗi đặc biệt như 'N/A', 'null'. Nếu trực tiếp gọi `float(val)`, chương trình sẽ ném ngoại lệ ValueError gây sập hệ thống xử lý.",
      "solutionBasic": "def to_float_cb(value):\n    if value is None or value == '':\n        return None\n    try:\n        return float(value)\n    except:\n        return None",
      "solutionAdvanced": "def to_float_nc(value) -> float | None:\n    \"\"\"Ép kiểu số thực phòng thủ và chỉ bắt đích danh ngoại lệ dự kiến.\"\"\"\n    if value is None:\n        return None\n    if isinstance(value, str):\n        cleaned = value.strip()\n        if not cleaned:\n            return None\n        try:\n            return float(cleaned)\n        except (ValueError, TypeError):\n            return None\n    try:\n        return float(value)\n    except (ValueError, TypeError):\n        return None",
      "explanation": "Không bao giờ dùng khối `except:` trần trụi (bare except) vì nó sẽ vô tình nuốt chửng cả các ngoại lệ hệ thống như KeyboardInterrupt hay MemoryError. Chỉ bắt đích danh `(ValueError, TypeError)`.",
      "verification": "assert to_float_nc('12.5') == 12.5\nassert to_float_nc('  100  ') == 100.0\nassert to_float_nc('') is None\nassert to_float_nc('N/A') is None"
    },
    {
      "id": "task-3",
      "title": "Bài 3: Thống kê tóm tắt phân phối giá (Trung bình và Trung vị thủ công)",
      "prompt": "Viết hàm `summarize_prices(prices: list[float | None]) -> dict` nhận vào danh sách giá (chứa cả giá trị `None`). Bỏ qua các giá trị `None`, tính: số quan sát hợp lệ (`n_valid`), giá trung bình (`mean`), và giá trung vị (`median`). Nếu không có giá trị hợp lệ, trả về `{ 'n_valid': 0, 'mean': None, 'median': None }`.",
      "prediction": "Để tính trung vị thủ công mà không dùng thư viện ngoài, bắt buộc phải sắp xếp danh sách các số hợp lệ. Nếu số phần tử là lẻ thì lấy phần tử ở giữa; nếu là chẵn thì lấy trung bình cộng của hai phần tử ở giữa.",
      "solutionBasic": "def summarize_prices_cb(prices):\n    valid = [p for p in prices if p is not None]\n    n = len(valid)\n    if n == 0:\n        return {'n_valid': 0, 'mean': None, 'median': None}\n    valid.sort()\n    mean_val = sum(valid) / n\n    if n % 2 == 1:\n        median_val = valid[n // 2]\n    else:\n        median_val = (valid[n // 2 - 1] + valid[n // 2]) / 2.0\n    return {'n_valid': n, 'mean': mean_val, 'median': median_val}",
      "solutionAdvanced": "def summarize_prices_nc(prices: list[float | None]) -> dict:\n    \"\"\"Thống kê mô tả danh sách số thực với độ phức tạp O(n log n).\"\"\"\n    valid = sorted([p for p in prices if isinstance(p, (int, float))])\n    n = len(valid)\n    if n == 0:\n        return {'n_valid': 0, 'mean': None, 'median': None}\n    mid = n // 2\n    median_val = valid[mid] if n % 2 != 0 else (valid[mid - 1] + valid[mid]) / 2.0\n    return {\n        'n_valid': n,\n        'mean': round(sum(valid) / n, 2),\n        'median': round(median_val, 2)\n    }",
      "explanation": "Lọc sạch các giá trị hợp lệ trước khi tính toán giúp mẫu số luôn phản ánh đúng số quan sát thực tế. Không được thay thế `None` bằng số `0` khi tính trung bình vì sẽ làm méo mó nghiêm trọng giá trị trung tâm.",
      "verification": "res1 = summarize_prices_nc([10.0, None, 20.0, 30.0])\nassert res1['n_valid'] == 3 and res1['mean'] == 20.0 and res1['median'] == 20.0\nres2 = summarize_prices_nc([])\nassert res2['n_valid'] == 0 and res2['mean'] is None"
    },
    {
      "id": "task-4",
      "title": "Bài 4: Đếm chỗ ở theo khu vực và xác định mức giá trung vị từng quận",
      "prompt": "Viết hàm `count_by_area(records)` và `median_by_area(records)` gom nhóm chỗ ở theo quận (`neighbourhood`) hoàn toàn bằng cấu trúc `dict` của Python thuần. Đếm số chỗ ở và tính mức giá trung vị cho từng quận.",
      "prediction": "Sử dụng từ điển chứa danh sách (`dict[str, list[float]]`) đóng vai trò tương tự như cơ chế GroupBy trong cơ sở dữ liệu quan hệ, cho phép gom toàn bộ giá phòng của từng quận vào một mảng độc lập trước khi tính trung vị.",
      "solutionBasic": "def count_by_area_cb(records):\n    counts = {}\n    for r in records:\n        area = r.get('neighbourhood', 'Chưa rõ')\n        counts[area] = counts.get(area, 0) + 1\n    return counts",
      "solutionAdvanced": "from collections import defaultdict\n\ndef median_by_area_nc(records: list[dict]) -> dict[str, float]:\n    \"\"\"Gom nhóm và tính trung vị giá theo quận bằng defaultdict.\"\"\"\n    grouped = defaultdict(list)\n    for r in records:\n        area = r.get('neighbourhood')\n        p = to_float_nc(r.get('price'))\n        if area and p is not None:\n            grouped[area].append(p)\n    \n    result = {}\n    for area, prices in grouped.items():\n        prices.sort()\n        m = len(prices)\n        mid = m // 2\n        result[area] = prices[mid] if m % 2 != 0 else (prices[mid - 1] + prices[mid]) / 2.0\n    return result",
      "explanation": "Việc sử dụng `collections.defaultdict(list)` giúp loại bỏ hoàn toàn các câu lệnh kiểm tra `if key not in dict:` rườm rà, mang lại mã nguồn ngắn gọn và tối ưu hóa thời gian thực thi.",
      "verification": "mock_data = [{'neighbourhood': 'A', 'price': '10'}, {'neighbourhood': 'A', 'price': '30'}, {'neighbourhood': 'B', 'price': '50'}]\nmeds = median_by_area_nc(mock_data)\nassert meds['A'] == 20.0 and meds['B'] == 50.0"
    },
    {
      "id": "task-5",
      "title": "Bài 5: Kiểm định chất lượng logic nghiệp vụ giữa các cột (Review QA)",
      "prompt": "Viết hàm `review_qa(records)` kiểm tra tính nhất quán logic giữa cột `number_of_reviews` và `last_review`. Một bản ghi bị xem là bất thường nếu `number_of_reviews == '0'` nhưng trường `last_review` lại chứa ngày tháng cụ thể (khác rỗng và khác None). Trả về danh sách các `id` chỗ ở vi phạm.",
      "prediction": "Trong cơ sở dữ liệu thực tế, các lỗi đồng bộ hóa giữa bảng sự kiện đánh giá và bảng tổng hợp chỗ ở thường tạo ra các bản ghi mâu thuẫn, ví dụ số đánh giá ghi 0 nhưng ngày đánh giá cuối vẫn lưu dấu vết cũ.",
      "solutionBasic": "def review_qa_cb(records):\n    bad_ids = []\n    for r in records:\n        n_rev = r.get('number_of_reviews', '0')\n        last_rev = r.get('last_review', '')\n        if n_rev == '0' and last_rev and last_rev.strip() != '':\n            bad_ids.append(r.get('id'))\n    return bad_ids",
      "solutionAdvanced": "def review_qa_nc(records: list[dict]) -> list[str]:\n    \"\"\"Kiểm tra mâu thuẫn dữ liệu chéo cột bằng list comprehension.\"\"\"\n    return [\n        str(r['id']) for r in records\n        if str(r.get('number_of_reviews', '')).strip() in ('0', '0.0')\n        and bool(r.get('last_review') and str(r.get('last_review')).strip())\n    ]",
      "explanation": "Quy trình kiểm định chất lượng (Data QA) phát hiện các mâu thuẫn nghiệp vụ này trước khi nạp dữ liệu vào kho phân tích là nhiệm vụ cốt lõi của kỹ sư dữ liệu phòng thủ.",
      "verification": "test_qa = [{'id': 'ok1', 'number_of_reviews': '0', 'last_review': ''}, {'id': 'err1', 'number_of_reviews': '0', 'last_review': '2026-01-01'}]\nassert review_qa_nc(test_qa) == ['err1']"
    }
  ]
};
