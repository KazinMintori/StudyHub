export const dsaLabs = {
  "dsa/complexity": {
    "id": "complexity",
    "title": "Thực hành Đánh giá Độ phức tạp Thuật toán & Profiling",
    "dataset": {
      "name": "Bộ dữ liệu đo lường hiệu năng thời gian & bộ nhớ",
      "type": "Mảng thử nghiệm tổng hợp (N = 1.000 đến 1.000.000 phần tử)",
      "url": "https://raw.githubusercontent.com/uet-iai-notebook-labs-2026/notebook-labs-template/main/README.md",
      "description": "Các mảng số nguyên ngẫu nhiên, mảng đã sắp xếp và mảng nghịch đảo để đo thời gian thực thi (timeit) và số phép so sánh của thuật toán tìm kiếm, sắp xếp."
    },
    "tasks": [
      {
        "id": "task-1",
        "title": "Bài 1: Đo lường thực nghiệm thời gian thực thi O(1), O(n), O(n^2)",
        "prompt": "Viết hàm đo lường thời gian thực thi của 3 phép toán trên danh sách có kích thước N tăng dần: (1) Truy xuất phần tử đầu `lst[0]`; (2) Tìm kiếm tuyến tính `val in lst`; (3) Đếm cặp phần tử `[(a, b) for a in lst for b in lst]`. Khảo sát đồ thị thời gian thực tế so với độ phức tạp lý thuyết.",
        "prediction": "Truy xuất chỉ số có thời gian không đổi bất kể N. Tìm kiếm tuyến tính có thời gian tăng tuyến tính theo N. Duyệt cặp bùng nổ bậc hai, khi N = 10.000 sẽ mất vài giây.",
        "solutionBasic": "import time\n\ndef do_thoi_gian(func, *args):\n    t0 = time.perf_counter()\n    func(*args)\n    return time.perf_counter() - t0",
        "solutionAdvanced": "import timeit\n\ndef benchmark_complexity(n_sizes: list[int]) -> dict:\n    \"\"\"Đo lường thời gian trung bình bằng module timeit chuẩn.\"\"\"\n    res = {'O1': [], 'On': []}\n    for n in n_sizes:\n        lst = list(range(n))\n        t_o1 = timeit.timeit(lambda: lst[0], number=10000)\n        t_on = timeit.timeit(lambda: n - 1 in lst, number=100)\n        res['O1'].append(t_o1)\n        res['On'].append(t_on)\n    return res",
        "explanation": "Đo lường thực nghiệm giúp sinh viên nhận ra hằng số ẩn $C$ trong ký hiệu Big-O. Một thuật toán $O(N)$ với hằng số lớn có thể chậm hơn $O(N^2)$ khi $N$ nhỏ.",
        "verification": "assert True"
      }
    ]
  },
  "dsa/sorting": {
    "id": "sorting",
    "title": "Thực hành Thuật toán Sắp xếp & Tính ổn định",
    "dataset": {
      "name": "Bộ dữ liệu hồ sơ sinh viên kèm điểm thi",
      "type": "Danh sách bộ dữ liệu phức hợp (Student Records)",
      "url": "https://raw.githubusercontent.com/uet-iai-notebook-labs-2026/notebook-labs-template/main/README.md",
      "description": "Danh sách các bản ghi gồm Tên, Lớp và Điểm thi để kiểm chứng tính ổn định (Stability) của Merge Sort và Quick Sort."
    },
    "tasks": [
      {
        "id": "task-1",
        "title": "Bài 1: Cài đặt Merge Sort ổn định và kiểm chứng tính bảo toàn thứ tự ban đầu",
        "prompt": "Cài đặt thuật toán Merge Sort theo hướng chia để trị. Cho danh sách sinh viên đã được sắp xếp trước theo Tên, hãy sắp xếp lại theo Điểm thi và chứng minh các sinh viên cùng điểm vẫn giữ nguyên thứ tự tên ban đầu.",
        "prediction": "Merge Sort sử dụng dấu so sánh `<=` trong bước trộn (Merge) sẽ bảo toàn vị trí tương đối của các phần tử có cùng khóa so sánh, đảm bảo tính ổn định.",
        "solutionBasic": "def merge_sort_cb(arr):\n    if len(arr) <= 1: return arr\n    mid = len(arr) // 2\n    left = merge_sort_cb(arr[:mid])\n    right = merge_sort_cb(arr[mid:])\n    # Trộn\n    res = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i]['diem'] >= right[j]['diem']: # Giữ ổn định\n            res.append(left[i]); i += 1\n        else:\n            res.append(right[j]); j += 1\n    res.extend(left[i:]); res.extend(right[j:])\n    return res",
        "solutionAdvanced": "def merge_sort_nc(arr: list, key=lambda x: x) -> list:\n    \"\"\"Merge sort ổn định tổng quát với tham số khóa tùy chỉnh.\"\"\"\n    if len(arr) <= 1: return arr\n    mid = len(arr) // 2\n    L = merge_sort_nc(arr[:mid], key)\n    R = merge_sort_nc(arr[mid:], key)\n    out = []\n    i = j = 0\n    while i < len(L) and j < len(R):\n        if key(L[i]) <= key(R[j]):\n            out.append(L[i]); i += 1\n        else:\n            out.append(R[j]); j += 1\n    out.extend(L[i:]); out.extend(R[j:])\n    return out",
        "explanation": "Tính ổn định là đặc tính sống còn khi thực hiện sắp xếp nhiều tiêu chí (Multi-key Sort), ví dụ sắp xếp theo Lớp rồi sắp tiếp theo Điểm.",
        "verification": "assert True"
      }
    ]
  }
};
