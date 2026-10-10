# Hướng dẫn chạy và kiểm thử mã `pagerank.py`

Tệp `pagerank.py` cài đặt thuật toán PageRank theo đúng mô hình của Bài giảng 03 (Học phần Giải thuật nền tảng của Khoa học dữ liệu).

## 1. Yêu cầu môi trường

- Python 3.8+ (chỉ dùng thư viện chuẩn `argparse`, `json`, `math`, `sys` — không cần cài thư viện bên ngoài qua pip).

## 2. Các lệnh chạy cơ bản

### Chạy đồ thị gốc (Hình 5.1 MMDS, $n=4, m=8$)

```bash
python materials/lec-03/code/pagerank.py --variant base --beta 0.8 --tol 1e-8 --max-iter 100
```

Kết quả kỳ vọng:
- Đạt hội tụ sau 20 vòng lặp.
- $r_A \approx 0.32142857$ ($\frac{9}{28}$).
- $r_B = r_C = r_D \approx 0.22619048$ ($\frac{19}{84}$).
- Tổng điểm $\sum r_i = 1.0$.

### Chạy biến thể Nút cụt (Dead End: Xóa cạnh C → A)

```bash
python materials/lec-03/code/pagerank.py --variant dead --beta 0.8 --tol 1e-8 --max-iter 100
```

Kết quả: Hội tụ sau 12 vòng, điểm nút cụt C được bù đều lại cho cả 4 nút qua phần bù $\beta\delta/n$.

### Chạy biến thể Bẫy liên kết (Spider Trap: Thay C → A bằng C → C)

```bash
python materials/lec-03/code/pagerank.py --variant trap --beta 0.8 --tol 1e-8 --max-iter 100
```

Kết quả: Hội tụ sau 34 vòng. Nút C hút nhiều điểm nhất ($r_C \approx 0.642$), nhưng nhờ xác suất dịch chuyển tức thời $1-\beta = 0.2$, các nút A, B, D vẫn giữ được điểm khác 0.
