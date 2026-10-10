---
course: "dsa"
section: "notes"
prerequisites: ["mang","con-tro","de-quy"]
lessonStatus: "reference"
---

# Cấu trúc Dữ liệu & Giải thuật (DSA) 

Chào mừng bạn đến với chuyên đề **Cấu trúc dữ liệu và Giải thuật** — một trong những môn học nền tảng quan trọng nhất của sinh viên Công nghệ Thông tin UET.

::: tip Triết lý học tại Hub
Môn DSA không nhằm mục đích bắt bạn "học thuộc lòng" từng dòng code C/C++. Mục tiêu tối thượng là **hiểu bản chất tư duy giải quyết vấn đề**:
1. Tại sao cấu trúc dữ liệu / thuật toán này lại ra đời?
2. Nó giải quyết bài toán gì tốt hơn cách thông thường?
3. Khi nào nên dùng và khi nào không nên dùng?
:::

---

##  Lộ trình Ôn tập Trọng tâm

Dưới đây là các chuyên đề cốt lõi được chia nhỏ theo từng học phần:

```mermaid
flowchart TD
    A["1. Phân tích Độ phức tạp<br/>(Big O, Time, Space)"] --> B["2. Thuật toán Sắp xếp<br/>(QuickSort, MergeSort)"]
    B --> C["3. Tìm kiếm & Kỹ thuật mảng<br/>(Binary Search, Two Pointers)"]
    C --> D["4. Cấu trúc Dữ liệu Cây<br/>(Binary Tree, BST, Heap)"]
    D --> E["5. Lý thuyết Đồ thị<br/>(BFS, DFS, Dijkstra, MST)"]
```

### 1. [Phân tích Độ phức tạp Thuật toán (Big-O)](./complexity.md)
- Hiểu bản chất ký hiệu $\mathcal{O}(1), \mathcal{O}(\log n), \mathcal{O}(n), \mathcal{O}(n \log n), \mathcal{O}(n^2)$.
- Cách tính nhanh thời gian chạy của vòng lặp và đệ quy mà không cần toán cao cấp.

### 2. [Thuật toán Sắp xếp (Sorting Algorithms)](./sorting.md)
- Phân tích chi tiết: **MergeSort** (Chia để trị) và **QuickSort** (Phân hoạch Hoare/Lomuto).
- Bảng mô phỏng từng bước (dry run) với mảng số thực tế.
- So sánh tính ổn định (Stability) và bộ nhớ phụ.

### 3. [Thuật toán Tìm kiếm (Searching)](./searching.md)
- Tìm kiếm nhị phân (Binary Search) và các biến thể tìm vị trí đầu/cuối.
- Kỹ thuật Hai con trỏ (Two Pointers) & Cửa sổ trượt (Sliding Window).

### 4. [Cấu trúc Cây & Cây nhị phân (Trees)](./trees.md)
- Cây nhị phân tìm kiếm (Binary Search Tree - BST): Thêm, xóa, tìm kiếm.
- Duyệt cây: Tiền thứ tự (Preorder), Trung thứ tự (Inorder), Hậu thứ tự (Postorder).
- Giới thiệu Cây cân bằng (AVL Tree) và Heap.

### 5. [Đồ thị & Các thuật toán duyệt (Graphs)](./graphs.md)
- Biểu diễn đồ thị: Ma trận kề vs Danh sách kề.
- Thuật toán duyệt: BFS (Hàng đợi) và DFS (Ngăn xếp/Đệ quy).
- Tìm đường đi ngắn nhất: Thuật toán Dijkstra.

---

## 📖 Giáo trình & Nguồn Tham khảo Chuẩn Quốc tế

### 1. Giáo trình Chuẩn mực Toàn cầu

1. **Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, & Clifford Stein (CLRS)**, [*Introduction to Algorithms (4th Edition)*](https://mitpress.mit.edu/9780262046305/introduction-to-algorithms/), MIT Press. Giáo trình "kinh thánh" của ngành Khoa học Máy tính: Phân tích tiệm cận (Big-O, Master Theorem), thuật toán chia để trị, sắp xếp (MergeSort, QuickSort, HeapSort), cây nhị phân tìm kiếm, cây đỏ-đen, quy hoạch động và các thuật toán đồ thị cơ bản.
2. **Robert Sedgewick & Kevin Wayne**, [*Algorithms (4th Edition)*](https://algs4.cs.princeton.edu/home/), Addison-Wesley. Trang tài nguyên khóa học trực tuyến chính thức của Đại học Princeton: [algs4.cs.princeton.edu](https://algs4.cs.princeton.edu/home/). Hệ thống bài giảng và mã nguồn cài đặt mẫu mực, trực quan.
3. **Steven S. Skiena**, [*The Algorithm Design Manual (3rd Edition)*](https://www.algorist.com/), Springer. Trang tài nguyên: [algorist.com](https://www.algorist.com/). Cẩm nang tra cứu và thiết kế thuật toán giải quyết các bài toán thực tế.
4. **Giáo trình Cấu trúc dữ liệu và Giải thuật**, Khoa Công nghệ Thông tin, Trường Đại học Công nghệ (ĐHQGHN).

### 2. Công cụ Trực quan hóa & Luyện tập Trực tuyến

- [VisuAlgo.net](https://visualgo.net/en) — Công cụ trực quan hóa hoạt họa từng bước của TS. Steven Halim (Đại học Quốc gia Singapore - NUS).
- [MIT OpenCourseWare 6.006: Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/) — Khóa học nhập môn giải thuật kinh điển của MIT.
- [NeetCode.io](https://neetcode.io/) — Lộ trình luyện tập thuật toán và cấu trúc dữ liệu theo chủ đề.
- [GeeksforGeeks - Data Structures](https://www.geeksforgeeks.org/data-structures/) — Bách khoa tra cứu nhanh ví dụ mã nguồn C++/Java/Python.
