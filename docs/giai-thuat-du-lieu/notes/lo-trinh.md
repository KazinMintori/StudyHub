---
course: "giai-thuat-du-lieu"
section: "notes"
prerequisites: ["do-phuc-tap","ham-lap-trinh","dictionary"]
lessonStatus: "reference"
---

# Giải Thuật Nền Tảng Cho Khoa Học Dữ Liệu 

Môn học **Giải thuật nền tảng cho Khoa học dữ liệu** (Foundations of Data Science / Algorithmic Foundations of Data Science) trình bày cách mô hình hóa và giải các bài toán dữ liệu quy mô lớn. Các chủ đề gồm tính toán phân tán Map-Reduce, phân tích liên kết (PageRank), tìm kiếm tương đồng (MinHash, LSH) và chỉ mục véc-tơ. Phần sau xét thuật toán dòng dữ liệu (Streaming), nén dữ liệu và cấu trúc dữ liệu ngoài bộ nhớ chính.

---

##  Lộ trình Môn học Trọng tâm

```mermaid
flowchart LR
    A["1. Mô hình Thuật toán<br/>(Đặc tả, Giới hạn, Bonferroni)"] --> B["2. Phân tán Map-Reduce<br/>(Map, Shuffle, Reduce, Hadoop)"]
    B --> C["3. Phân tích Đồ thị<br/>(PageRank, Random Walk, Spam)"]
    C --> D["4. Tìm kiếm Tương đồng<br/>(Jaccard, MinHash, LSH)"]
    D --> E["5. Dòng Dữ liệu & Nén<br/>(Bloom Filter, Sketch, Huffman)"]
```

---

##  Danh mục Bài học

| Bài | Tên chuyên đề | Trạng thái |
|---|---|---|
| **Bài 01** | [**Bài toán dữ liệu lớn và mô hình thuật toán**](./bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan.md) *(Đặc tả, độ đo tương đồng Jaccard, tiêu chí đánh giá thuật toán và nguyên lý Bonferroni)* |  **Đã hoàn thành** |
| **Bài 02** | [**Mô hình tính toán Map-Reduce**](./bai-02-mapreduce-va-xu-ly-du-lieu-lon.md) *(Mô hình lập trình Map/Reduce/Combine, nhân ma trận, mô hình chi phí và thực hành Hadoop)* |  **Đã hoàn thành** |
| **Bài 03** | [**PageRank: Mô hình và tính toán**](./bai-03-pagerank-mo-hinh-va-tinh-toan.md) *(Random Surfer, Power Iteration, xử lý Dead Ends và Spider Traps)* |  Đang biên soạn |
| **Bài 04** | PageRank theo chủ đề và chống spam liên kết (Topic-Sensitive & TrustRank) |  Chờ nạp bài |
| **Bài 05** | Tìm tập tương đồng & Kỹ thuật Shingling / MinHash |  Chờ nạp bài |
| **Bài 06** | Tìm kiếm lân cận cục bộ (Locality-Sensitive Hashing - LSH) |  Chờ nạp bài |
| **Bài 07** | Tìm kiếm véc-tơ quy mô lớn (Vector Search, HNSW, PQ) |  Chờ nạp bài |
| **Bài 08** | Khai phá dòng dữ liệu I: Lấy mẫu và Bộ lọc Bloom (Bloom Filter) |  Chờ nạp bài |
| **Bài 09** | Khai phá dòng dữ liệu II: Đếm phân biệt (Flajolet-Martin) và Count-Min Sketch |  Chờ nạp bài |
| **Bài 10** | Nén dữ liệu không mất mát: Mã hoá Huffman và Lempel-Ziv |  Chờ nạp bài |
| **Bài 11** | Nén dữ liệu có mất mát: Biến đổi Cosin rời rạc (DCT) và JPEG |  Chờ nạp bài |
| **Bài 12** | Thuật toán ngoài bộ nhớ chính (External Memory) & Sắp xếp ngoài (Merge Sort) |  Chờ nạp bài |
| **Bài 13** | Cấu trúc dữ liệu cây ngoài bộ nhớ: B-Tree và các biến thể |  Chờ nạp bài |
| **Bài 14** | Chỉ mục không gian: R-Tree và truy vấn phạm vi đa chiều |  Chờ nạp bài |
| **Bài 15** | Phân cụm dữ liệu quy mô lớn (BFR, CURE) và Tổng kết học phần |  Chờ nạp bài |

---

##  Giáo trình & Nguồn Tham khảo Chuẩn Quốc tế

1. **"Mining of Massive Datasets" (MMDS)** — *Jure Leskovec, Anand Rajaraman, Jeffrey D. Ullman* (Stanford University / Cambridge University Press).
2. **"Foundations of Data Science"** — *Avrim Blum, John Hopcroft, Ravindran Kannan* (Cambridge University Press).
3. **Dean & Ghemawat:** *"MapReduce: Simplified Data Processing on Large Clusters"* (Google / OSDI 2004).
4. **Slide bài giảng:** Khoa Công nghệ Thông tin — Trường Đại học Công nghệ (ĐHQGHN).
