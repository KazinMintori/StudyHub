export const knowledgeLabs = {
  "bieu-dien-tri-thuc/02-tim-kiem-mu": {
    "id": "02-tim-kiem-mu",
    "title": "Thực hành Thuật toán Tìm kiếm Mù: BFS, DFS, UCS",
    "dataset": {
      "name": "Đồ thị bài toán bản đồ Romania",
      "type": "Đồ thị có trọng số dương (Adjacency Map)",
      "url": "https://raw.githubusercontent.com/uet-iai-notebook-labs-2026/notebook-labs-template/main/README.md",
      "description": "Đồ thị chuẩn mực gồm 20 thành phố của Romania kèm khoảng cách giữa các thành phố để kiểm tra tính tối ưu và chi phí đường đi của BFS và UCS."
    },
    "tasks": [
      {
        "id": "task-1",
        "title": "Bài 1: Cài đặt Uniform Cost Search (UCS) bằng hàng đợi ưu tiên",
        "prompt": "Sử dụng module `heapq` của Python để cài đặt thuật toán UCS tìm đường đi ngắn nhất từ Arad đến Bucharest. Kiểm tra tính tối ưu khi các cạnh có trọng số khác nhau.",
        "prediction": "UCS luôn lấy trạng thái có chi phí tích lũy g(n) nhỏ nhất ra khỏi hàng đợi ưu tiên, bảo đảm tìm được đường đi có tổng chi phí nhỏ nhất khi trọng số bước có chặn dưới dương.",
        "solutionBasic": "import heapq\n\ndef ucs_cb(graph, start, goal):\n    pq = [(0, start, [start])]\n    visited = set()\n    while pq:\n        cost, node, path = heapq.heappop(pq)\n        if node == goal: return cost, path\n        if node in visited: continue\n        visited.add(node)\n        for neighbor, weight in graph.get(node, []):\n            if neighbor not in visited:\n                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))\n    return float('inf'), []",
        "solutionAdvanced": "def ucs_nc(graph: dict, start: str, goal: str) -> tuple[float, list[str]]:\n    \"\"\"UCS với quản lý bảng chi phí tốt nhất frontier tracking.\"\"\"\n    best_g = {start: 0.0}\n    pq = [(0.0, start, [start])]\n    while pq:\n        g, curr, path = heapq.heappop(pq)\n        if curr == goal: return g, path\n        if g > best_g.get(curr, float('inf')): continue\n        for nxt, w in graph.get(curr, []):\n            new_g = g + w\n            if new_g < best_g.get(nxt, float('inf')):\n                best_g[nxt] = new_g\n                heapq.heappush(pq, (new_g, nxt, path + [nxt]))\n    return float('inf'), []",
        "explanation": "Bảng `best_g` giúp loại bỏ sớm các nhánh đắt tiền hơn đã có trên frontier trước khi lấy ra khỏi hàng đợi.",
        "verification": "assert True"
      }
    ]
  }
};
