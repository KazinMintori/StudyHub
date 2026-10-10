---
course: "bieu-dien-tri-thuc"
section: "notes"
prerequisites: ["tap-hop","menh-de","luong-tu"]
lessonStatus: "reference"
---

# Lộ trình học tập · AIT2004 Cơ sở Trí tuệ Nhân tạo

Môn học **Cơ sở Trí tuệ Nhân tạo** (AIT2004) trang bị tư duy giải quyết vấn đề bằng mô hình hóa không gian trạng thái, các chiến lược tìm kiếm từ cơ bản đến nâng cao, lý thuyết trò chơi đối kháng, và các phương pháp biểu diễn tri thức phục vụ suy luận tự động.

Toàn bộ hệ thống bài giảng được xây dựng bám sát cấu trúc sư phạm hiện đại, kết hợp chặt chẽ giữa toán học lý thuyết và lập trình ứng dụng.

---

## 1. Không gian trạng thái và Tìm kiếm

| Bài giảng | Nội dung chủ đạo | Liên kết |
|:---|:---|:---:|
| **Bài 1: Giới thiệu & Tác tử thông minh** | Đặc tả PEAS, phân loại môi trường, kiến trúc tác tử | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/01-gioi-thieu-tac-tu.md) |
| **Bài 2: Tìm kiếm mù** | BFS, DFS, UCS (Dijkstra), giải thuật IDS tối ưu bộ nhớ | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.md) |
| **Bài 3: Tìm kiếm kinh nghiệm** | Hàm Heuristic, Greedy Best-First, A\*, tính Admissible/Consistent, IDA\* | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/03-tim-kiem-kinh-nghiem.md) |
| **Bài 4: Tìm kiếm đối kháng** | Cây trò chơi, thuật toán Minimax, kỹ thuật cắt tỉa Alpha–Beta | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/04-tim-kiem-doi-khang.md) |
| **Bài 5: Bài toán thỏa mãn ràng buộc (CSP)** | Lan truyền AC-3, quay lui Backtracking, heuristic MRV, Degree, LCV | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/05-csp.md) |

---

## 2. Biểu diễn tri thức và Suy luận

| Bài giảng | Nội dung chủ đạo | Liên kết |
|:---|:---|:---:|
| **Bài 14: Logic & Biểu diễn tri thức** | Logic vị từ bậc nhất (FOL), lượng từ, hợp nhất hóa Unification, GMP, Ontology | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/14-logic-bieu-dien-tri-thuc.md) |
| **Bài 16: Mạng Bayes & Suy luận** | Đồ thị DAG, tính độc lập có điều kiện, cấu trúc D-separation, thuật toán khử biến | [Xem bài giảng](/bieu-dien-tri-thuc/bai-giang/16-mang-bayes.md) |

---

## 3. Hệ thống bài tập và Ôn luyện

Để củng cố năng lực thực hành giải thuật và suy luận toán học, học viên tiếp tục rèn luyện với hệ thống bài tập tự luận và tính toán chi tiết tại [Tuyển tập Bài tập ôn luyện](/bieu-dien-tri-thuc/bai-tap.md).

---

## 4. Giáo trình & Tài liệu Tham khảo Chuẩn Quốc tế

Khóa học được xây dựng theo chuẩn mực học thuật quốc tế của các trường đại học hàng đầu (UC Berkeley, Stanford, MIT):

1. **Stuart Russell & Peter Norvig**, [*Artificial Intelligence: A Modern Approach (4th Edition - AIMA)*](https://aima.cs.berkeley.edu/), Pearson. Giáo trình chuẩn mực toàn cầu về tác tử thông minh, tìm kiếm không gian trạng thái, A\*, Minimax, CSP và suy luận logic. Mã nguồn giải thuật mẫu: [aimacode/aima-python](https://github.com/aimacode/aima-python).
2. **Daphne Koller & Nir Friedman**, [*Probabilistic Graphical Models: Principles and Techniques*](https://pgm.stanford.edu/), MIT Press. Tài liệu toàn diện hàng đầu về mạng Bayes, đồ thị vô hướng Markov, suy luận chính xác và xấp xỉ trên mô hình đồ thị xác suất.
3. **UC Berkeley CS188: Introduction to Artificial Intelligence** (Dan Klein & Pieter Abbeel), tài liệu tại [inst.eecs.berkeley.edu/~cs188](https://inst.eecs.berkeley.edu/~cs188/). Hệ thống slide bài giảng, video và đồ án thực hành Pacman kinh điển về Search, CSP, Games và Bayes.
4. **Stanford CS221: Artificial Intelligence: Principles and Techniques** (Percy Liang), tài liệu tại [stanford-cs221.github.io](https://stanford-cs221.github.io/). Khóa học AI của Đại học Stanford về mô hình trạng thái, biến ngẫu nhiên và logic.
5. **Đề cương bài giảng AIT2004 · Cơ sở Trí tuệ Nhân tạo**, Khoa Công nghệ Thông tin, Trường Đại học Công nghệ (ĐHQGHN).
