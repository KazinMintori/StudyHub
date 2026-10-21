# Bài 5 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai5_72_cau_hoi.md). Đủ 72 câu: 48 trắc nghiệm, 24 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B5-001 | A |
| B5-002 | B |
| B5-003 | D |
| B5-004 | D |
| B5-005 | A |
| B5-006 | C |
| B5-007 | B |
| B5-MR01 | B |
| B5-MR02 | C |
| B5-011 | C |
| B5-012 | D |
| B5-013 | A |
| B5-014 | B |
| B5-015 | D |
| B5-016 | D |
| B5-017 | B |
| B5-MR03 | D |
| B5-021 | B |
| B5-022 | B |
| B5-023 | A |
| B5-024 | B |
| B5-025 | C |
| B5-026 | A |
| B5-027 | C |
| B5-MR05 | B |
| B5-MR06 | C |
| B5-031 | C |
| B5-032 | A |
| B5-033 | B |
| B5-034 | B |
| B5-035 | D |
| B5-036 | C |
| B5-037 | C |
| B5-MR07 | D |
| B5-041 | C |
| B5-042 | D |
| B5-043 | A |
| B5-044 | C |
| B5-045 | D |
| B5-046 | A |
| B5-MR09 | A |
| B5-051 | A |
| B5-052 | A |
| B5-053 | C |
| B5-054 | B |
| B5-055 | D |
| B5-056 | D |
| B5-MR11 | A |

## Tự luận

### B5-008

Mean chung 80 USD/đêm, cân theo count 2/4; size tính cả thiếu, mean hai mean cho trọng số khu bằng nhau.
Không thể gộp median tương tự vì median/count không đủ tái tạo phân bố giá gốc.

### B5-009

6 hàng, tổng giá 140: P tạo 2×2 cặp, Q/R mỗi mã 1 cặp.
ignore_index chỉ đặt lại nhãn hàng; id P vẫn lặp giữa hai snapshot.

### B5-010

Sau chạy lại: `[0.04,0.08]`, không còn giá CLP/đêm gốc vì chia lặp.
`moi = goc.assign(gia_nghin=goc['price']/1000)`; chạy hai lần từ goc, so bằng nhau và goc vẫn `[40000,80000]`.

### B5-018

Không lỗi độ dài; lech sai theo A/B/C = `[30,10,10]` vì to_numpy bỏ nhãn.
Sửa `d['lech'] = moi-d['gia']` → `[10,30,10]`; đảo thứ tự hai đầu vào rồi đối chiếu lại theo mã.

### B5-019

Mask A/B không khớp index hàng gây IndexingError; dùng transform để lọc đúng hàng.
Giữ index `[10,20,30]`, lech `[-10,10,0]`; đếm id khác nhau theo khu, trừ mean theo listing.

```python
du = d.loc[d.groupby('khu')['id'].transform('nunique') >= 2].copy()
du['lech'] = du['gia'] - du.groupby('id')['gia'].transform('mean')
```

### B5-020

n_host theo P/R/S = `[2,2,1]`; chạy lại ổn định nhưng H có 3 listing trong nguồn, gồm Q thiếu giá.
Đếm trước lọc để được `[3,3,1]`:

```python
day_du = goc.assign(n_host=lambda d: d.groupby('host')['id'].transform('size'))
co = day_du.loc[day_du['gia'].notna()]
```

### B5-MR04

`d['tb_khu'] = d['khu'].map(tb)` → `[30,20,30,20]` theo index `[7,2,9,5]`.
Gán tb trực tiếp căn nhãn A/B vào index số nên toàn NaN; hàng 5 vẫn nhận mean khu A = 20.

### B5-028

Inner cho 5 hàng, mất S; sửa `m = d.merge(phi,on='khu',how='left',indicator=True)` được 6 hàng.
3 phí thiếu nhưng chỉ 1 left_only: P/R khớp A có phí thiếu, S không có khóa đối ứng.

### B5-029

Lệch cũ `[-40,40,0]`; sửa `x['lech'] = x['gia']-x.groupby('khu')['gia'].transform('mean')`.
Đúng `[-10,0,10]`; lệch dương chỉ là cao hơn mean khu, chưa chứng minh đắt không hợp lý.

### B5-030

r: 5 nhãn A–E, 4 thiếu; d vẫn 3 hàng, tong theo A/B/C = `[NaN,21,NaN]`.
Không tự thay thiếu bằng 0: chưa biết phí không đồng nghĩa miễn phí.

### B5-038

Cũ `[re,trung,cao,cao]` sai tại NaN; thêm đầu hàm `if pd.isna(x): return None`, rồi map lại.
Kiểm 50→trung, 100→cao, NaN→thiếu; tương đương `pd.cut(s,[0,50,100,np.inf],labels=['re','trung','cao'],right=False)`.

### B5-039

Cũ n_host `[2,2,2,2]`, chưa chứng minh nguồn sai; sau đếm toàn nguồn là `[3,3,2,2]`.
Tỷ lệ listing thuộc host chuyên nghiệp đúng 2/4 = 50%, cũ 0%; đếm trước lọc:

```python
day_du = goc.assign(n_host=lambda d: d.groupby('host')['id'].transform('size'))
x = day_du.loc[day_du['loai'] == 'can'].copy()
```

### B5-040

5 hàng, tổng 180, chuyen = 4/5; P/Q bị lặp gấp đôi, đúng một hàng/host thì tổng 140 và tỷ lệ 2/3.
Thêm `validate='m:1'` vào merge để phát MergeError; nó không tự sửa h.

### B5-MR08

Mặc định cao A/B = 1/2, 2/3, mẫu số 2/3 nhãn biết; thêm `dropna=False` cho 1/3, 2/3 trên mọi listing.
`d.groupby('khu')['phan'].value_counts(normalize=True,dropna=False)`; toàn bảng là 3/6, khác tỷ lệ từng khu.

### B5-047

tong A/B/C/D = `[65,140,NaN,NaN]`; C thiếu giá, D thiếu phí; kiểm A = 6×10+5, B đúng biên 7 đêm = 140.

```python
phi_tinh = d['phi'].copy()
phi_tinh.loc[d['so_dem'] >= 7] = 0
tong = d['gia'] * d['so_dem'] + phi_tinh
```

### B5-048

Assert qua nhưng có 6 hàng; thêm `validate='m:1'` gây MergeError vì H lặp phí 2/5.
Không tự chọn một phí; làm rõ nguồn rồi kiểm khóa, số hàng/id, left_only và thiếu phí riêng.

### B5-049

r có 6 nhãn, 6 NaN do căn index hàng với nhãn khu; sửa được `[-20,-20,20,20]`.
Lọc mean khu ≥40 giữ index `[7,12]`:

```python
r = d['gia'] - d.groupby('khu')['gia'].transform('mean')
du = d.groupby('khu').filter(lambda nhom: nhom['gia'].mean() >= 40)
```

### B5-050

ValueError do 4 giá trị/3 hàng; cắt còn 3 gán sai theo B/C/A = `[9,5,7]`.
Sửa `d['phi'] = s` → `[3,7,5]`, không thêm D; đảo thứ tự đầu vào rồi kiểm phí từng mã.

### B5-MR10

File thiếu host vì xuất t với index=False; sửa `u.to_csv('host.csv',index=False)`.
Đúng hai cột host/tb: H–30, K–80; reset_index tạo u mới, không sửa t.

### B5-057

cut cũ `[re,re,trung,trung]`, mới `[trung,trung,cao,cao]`; qcut giữ P/Q thấp, R/S cao, mốc 50000→110000.
Đổi sang nghìn CLP thì bins = `[0,50,100,np.inf]`; đổi tập, thiếu hay quy tắc chia có thể đổi nhóm qcut.

### B5-058

Pivot re: False=2/True=8; cao: False=2/True=6, ô cao/True chỉ dùng 1 giá biết; mặc định aggfunc vẫn mean.
Mỗi hàng là phân khúc; review chưa là booking hay bằng chứng nhân quả:

```python
pv = d.pivot_table(index='phan', columns='chuyen', values='review', aggfunc='mean')
```

### B5-059

Các kiểm tra đều qua nhưng P/Q sai phí vì khu bị thay bằng host; phí đúng P/Q/R/S = `[20,10,10,20]`.
Bỏ assign, dùng `d.merge(v,on='khu',how='left',validate='m:1',indicator=True)`; kiểm từng mã với khu gốc.

### B5-060

Lần đầu goc.price = `[40,80]`, assert luôn qua vì or True; chạy lại gia_nghin = `[0.04,0.08]`.
Khôi phục nguồn, bỏ or True; tạo hai kết quả bằng nhau và kiểm nguồn nguyên vẹn, gia_nghin `[40,80]`:

```python
def nghin(d):
    return d['price']/1000
moi = goc.assign(gia_nghin=nghin)
```

### B5-MR12

Sai theo B/A/C/D = `[60,20,NaN,NaN]` vì nhãn listing trùng mã khu; sửa `d['tb_khu'] = d['khu'].map(tb)`.
Đúng `[20,60,20,60]`; u gồm khu/gia, reset_index không tự sửa cột đã gán trong d.
