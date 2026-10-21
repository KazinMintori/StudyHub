# Bài 3 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai3_72_cau_hoi.md). Đủ 72 câu: 48 trắc nghiệm, 24 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B3-001 | B |
| B3-002 | D |
| B3-003 | A |
| B3-004 | C |
| B3-005 | B |
| B3-006 | D |
| B3-007 | A |
| B3-MR01 | C |
| B3-MR02 | A |
| B3-011 | C |
| B3-012 | A |
| B3-013 | D |
| B3-014 | B |
| B3-015 | C |
| B3-016 | A |
| B3-017 | D |
| B3-MR03 | B |
| B3-021 | B |
| B3-022 | C |
| B3-023 | A |
| B3-024 | D |
| B3-025 | B |
| B3-026 | A |
| B3-027 | C |
| B3-MR05 | D |
| B3-MR06 | A |
| B3-031 | D |
| B3-032 | B |
| B3-033 | C |
| B3-034 | A |
| B3-035 | D |
| B3-036 | B |
| B3-037 | C |
| B3-MR07 | C |
| B3-041 | A |
| B3-042 | D |
| B3-043 | B |
| B3-044 | C |
| B3-045 | A |
| B3-046 | D |
| B3-MR09 | D |
| B3-051 | B |
| B3-052 | A |
| B3-053 | C |
| B3-054 | D |
| B3-055 | B |
| B3-056 | C |
| B3-MR11 | B |

## Tự luận

### B3-008

V: shape (2,2), strides (32,8) byte, offset đầu 20 byte; `A[3,1] = 90`, offset 52 byte.
32 chỉ là độ lệch từ đầu V, phải cộng thêm offset đầu V là 20.

### B3-009

`C[0,1] = 77`; C = `[[16,77],[4,6]]`; A = `[[2,4,6],[8,10,12],[14,16,18]]`.
Chỉ C/W dùng chung: chỉ mục nâng cao tạo C riêng, W là view của C.

### B3-010

ValueError vì (2,3) không broadcast với (2,); sửa `lech = P - P.mean(axis=1, keepdims=True)`.
Kết quả `[[-6,0,6],[-6,0,6]]`, shape (2,3); kiểm `np.allclose(lech.mean(axis=1), 0)` và hàng đầu tính tay.

### B3-018

P = `[0,2,4,6,8,10]`, Q = `[1,2,5,6,9,10]`; dùng chung A lần lượt True/False.
P bước đều 8 byte, Q xen kẽ 4/12 byte; không C-contiguous chưa đủ kết luận reshape luôn copy.

### B3-019

A không đổi vì `T[[1],:]` tạo bản sao; sửa `T[1,[0,2]] = 0`.
A = `[[2,0,6],[8,10,12],[14,0,18]]`; đối chiếu toàn A với kết quả này để kiểm đúng hai ô.

### B3-020

u = `[5,7,9]`, shape (3,), mean theo ngày; v = `[[12],[30]]`, shape (2,1), tổng theo cửa hàng; t = 7, shape ().
u[1] dùng D[0,1] và D[1,1], mẫu số 2; t dùng cả 6 ô.

### B3-MR04

Strides (0,4), nbytes 48; dùng chung b, offset V[3,1] = 4 byte, không cấp phát 48 byte phần tử mới.
V là view chỉ đọc; gán `V[0,0] = 9` gây ValueError.

### B3-028

shape (2,2); strides (8,32) byte; nbytes 16; offset ô đầu/cuối 4/44 byte.
Đoạn bao trùm [4,48) dài 44 byte; dữ liệu phần tử mới: 0 byte.

### B3-029

idx: (2,1)/(1,2); B = `[[-1,-1],[-1,-1]]`; A = `[[0,50,2,60],[4,5,6,7],[8,50,10,60]]`.
B là copy, gán A[idx] sửa A; RHS lặp [50,60] qua các hàng, còn [50,60,70] gây ValueError.

### B3-030

Không lỗi; P sai = `[[1/4,1/2],[3/8,3/4]]`, chia hai cột cho 8/12.
Sửa `P = D/D.sum(axis=1, keepdims=True)` → `[[1/4,3/4],[1/4,3/4]]`; kiểm tổng từng hàng bằng 1.

### B3-038

R = `[[1,99,4],[5,7,8]]`, A = `[[1,4,7],[2,5,8]]`; W[0,0] sửa R[0,1].
Dùng chung theo thứ tự: True/False/True/False; reshape C-order của T đã tách dữ liệu khỏi A.

### B3-039

m = `[True,False,True]`; v = `[6,20,7]`; x = `[4,6,20,7]`; cộng 5 vào x[1], x[3].
Mask không tự tính lại nên 20 không được cộng; RHS đọc copy, LHS gán vào view v của x.

### B3-040

Code chạy vì (2,) khớp chiều cột; lech sai = `[[-1,-8],[7,2]]`.
Sửa `lech = P-P.mean(axis=1, keepdims=True)` → `[[-1,1],[-2,2]]`; kiểm mean từng hàng bằng 0.

### B3-MR08

ddof=0: var = 8/3 USD², std = √(8/3) ≈ 1,632993 USD; ddof=1: var = 4 USD², std = 2 USD.
Không mâu thuẫn vì mẫu số lần lượt là 3 và 2.

### B3-047

c tái lập a; b dùng trạng thái tiếp theo của rng, không khởi tạo lại.
b có thể tình cờ bằng a; seed không bảo đảm mẫu đại diện hay mean bằng toàn bộ.

### B3-048

Hàng cuối A = `[50,9,10,11]`; R[1,1] ánh xạ A[2,0]; R dùng chung A, S không dùng chung.
R có bước đều 8 byte; S xen kẽ 4/12 byte nên reshape này phải copy.

### B3-049

A = `[20,4,6,8]`; C = `[2,40,6,8]`; A/B cùng đối tượng, A/C độc lập, C/V dùng chung.
Ngay khi copy, A và C bằng giá trị nhưng không chung dữ liệu; kiểm riêng bằng shares_memory.

### B3-050

Code/assert đều qua; P cũ = `[[1/4,3/4],[1/2,1/2]]`, là tỷ trọng theo hàng.
Sửa `P = D/D.sum(axis=0)` → `[[1/4,1/2],[3/4,1/2]]`; kiểm tổng từng cột bằng 1, tổng chung 2 chưa đủ.

### B3-MR10

W: shape (2,2), strides (8,16) byte, offset đầu 20; sửa A[2,1] = 99 ở offset 36 byte.
Stride âm là bước dịch ngược từ đầu view, không phải địa chỉ vật lý âm.

### B3-057

Mean toàn bộ 50, mẫu 15 USD/đêm; báo `gia.mean()`; chọn seed theo kết quả thấp gây thiên lệch.
Đọc mẫu giúp kiểm bản ghi; 140 đã hợp lệ nên không được tự xóa vì lớn.

### B3-058

Không thể là view: offset đầu hàng 0,16,36 cho bước 16/20 byte, không có stride hàng cố định.
`B = A.reshape(-1, order='C')[[0,2,4,6,9,11]].reshape(3,2, order='C')` → `[[0,2],[4,6],[9,11]]`.

### B3-059

x = `[3,1,5,1]`; y = `[1,1]`; tổng x/y = 10/2.
y dùng chung x, ánh xạ x[1], x[3]; mask `[False,True,False,True]` không tự tính lại.

### B3-060

Assert qua nhưng sai thứ tự cột; bỏ bước đảo, dùng `Z = P-P.mean(axis=1, keepdims=True)`.
Z = `[[-2,2],[-2,2]]`; đối chiếu toàn ma trận hoặc Z[0,0] = -2, vì mean hàng không phát hiện đảo cột.

### B3-MR12

R = `[[2,3,4],[2,3,4]]`, shape (2,3), int32, 24 byte; dùng chung theo thứ tự True/False/False.
V.nbytes=24 nhưng dùng lại 12 byte của b; R cấp phát riêng, không mâu thuẫn; kiểm bằng np.shares_memory.
