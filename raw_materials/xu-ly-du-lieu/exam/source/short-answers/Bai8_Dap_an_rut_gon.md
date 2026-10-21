# Bài 8 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai8_72_cau_hoi.md). Đủ 72 câu: 48 trắc nghiệm, 24 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B8-001 | B |
| B8-002 | D |
| B8-003 | C |
| B8-004 | A |
| B8-005 | B |
| B8-006 | C |
| B8-007 | D |
| B8-MR01 | D |
| B8-011 | C |
| B8-012 | A |
| B8-013 | D |
| B8-014 | B |
| B8-015 | A |
| B8-016 | D |
| B8-017 | C |
| B8-MR03 | A |
| B8-MR04 | C |
| B8-021 | A |
| B8-022 | C |
| B8-023 | B |
| B8-024 | D |
| B8-025 | C |
| B8-026 | B |
| B8-MR05 | C |
| B8-031 | D |
| B8-032 | B |
| B8-033 | A |
| B8-034 | C |
| B8-035 | D |
| B8-036 | A |
| B8-037 | B |
| B8-MR07 | B |
| B8-MR08 | D |
| B8-041 | B |
| B8-042 | D |
| B8-043 | C |
| B8-044 | A |
| B8-045 | D |
| B8-046 | B |
| B8-047 | A |
| B8-MR09 | B |
| B8-051 | C |
| B8-052 | A |
| B8-053 | B |
| B8-054 | D |
| B8-055 | A |
| B8-056 | C |
| B8-MR11 | A |

## Tự luận

### B8-008

Số đêm D1/D2/D3/D4 = `[2,3,NaN,NaN]`; lỗi vào chỉ D3, D4 thiếu nguồn.
Thiếu ngày làm hiệu chưa biết, không đồng nghĩa 0 đêm:

```python
vao = pd.to_datetime(dat['vao'], format='%d/%m/%Y', errors='coerce')
ra = pd.to_datetime(dat['ra'], format='%d/%m/%Y', errors='coerce')
so_dem = (ra-vao).dt.days
loi_vao = dat['vao'].notna() & vao.isna()
```

### B8-009

`(238/200-1)*100` = 19,0%; mẫu số 200 review, trọng số tháng theo 20/200 và 180/200, không ngang nhau.
55% là mean tỷ lệ tháng; chưa đủ kết luận nguyên nhân quảng cáo.

### B8-010

Bỏ format có thể đảo ngày/tháng; dùng ME thay M. Tháng 6 mới 12 ngày so với cả tháng 5, chưa kết luận tháng trọn.
Số đếm `[2,2,2]`; loại tháng 6 khỏi so sánh tháng trọn, không gán ngày chưa thu bằng 0:

```python
rv['ngay'] = pd.to_datetime(rv['ngay'], format='%d/%m/%Y')
thang = rv.set_index('ngay').sort_index().resample('ME').size()
tron = thang.loc[thang.index <= pd.Timestamp('2026-05-31')]
tang_tron = tron.pct_change(fill_method=None)
```

### B8-MR02

Giữ hàng 1/2, được 2 review; giờ Việt Nam tương ứng 01/07 00:00 và 17:00.
Gắn trực tiếp timezone Việt Nam cho đồng hồ UTC sẽ đổi sai thời điểm thực:

```python
v = pd.to_datetime(raw, format='%Y-%m-%d %H:%M', utc=True).dt.tz_convert('Asia/Ho_Chi_Minh')
dau = pd.Timestamp('2026-07-01', tz='Asia/Ho_Chi_Minh')
cuoi = pd.Timestamp('2026-07-02', tz='Asia/Ho_Chi_Minh')
giu = (v >= dau) & (v < cuoi)
so = int(giu.sum())
```

### B8-018

Giữ 3 hàng id 2/1/3; ngoài phạm vi 1 (id4), lỗi 1 (id6), thiếu nguồn 1 (id5).
Không xóa review trùng ngày; ngoài mốc chưa chắc lỗi nhập:

```python
d = pd.to_datetime(raw['date'], format='%Y-%m-%d', errors='coerce')
loi = raw['date'].notna() & d.isna()
ngoai = d.notna() & ((d < '2026-06-01') | (d > '2026-06-29'))
giu = d.notna() & (d >= '2026-06-01') & (d <= '2026-06-29')
r = raw.assign(ngay=d).loc[giu].set_index('ngay').sort_index()
```

### B8-019

Bỏ format có thể đảo ngày/tháng, Q đổi QE; số đếm `[3,3]`, tổng 6, chỉ quý I trọn.
Đã quan sát 90/90 ngày nhưng quý II cần 91; hai số bằng nhau chưa chứng minh xu hướng ổn định.

```python
rv['ngay'] = pd.to_datetime(rv['ngay'], format='%d/%m/%Y')
q = rv.set_index('ngay').sort_index().resample('QE').size()
tron = q.loc[q.index <= pd.Timestamp('2026-06-29')]
assert q.sum() == len(rv)
```

### B8-020

Chỉ dùng 2024–2025: tổng tháng 1/2 đều 60, mean 12 tổng là 60, hai chỉ số đều 100.
.month bỏ năm; thêm 2026 làm lệch số năm đóng góp; chỉ số chưa loại xu hướng hay độ dài tháng.

### B8-027

Ngày thực `[1.50,1.25,NaN]`; .dt.days cho `[1,1,NaN]` vì chỉ lấy phần ngày nguyên.

```python
vao = pd.to_datetime(dat['vao'], format='%Y-%m-%d %H:%M', errors='coerce')
ra = pd.to_datetime(dat['ra'], format='%Y-%m-%d %H:%M', errors='coerce')
khoang = ra-vao
ngay_thuc = khoang.dt.total_seconds()/86400
ngay_nguyen = khoang.dt.days
```

### B8-028

`du = s.reindex(lich,fill_value=0)` → `[0,2,0,4,0]`; `du.mean()` = 1,2 review/ngày trên 5 ngày.
resample/asfreq chỉ phủ 02–04/06, thiếu hai đầu; 06/06 chưa biết nên không tự điền 0.

### B8-029

Sáu kết quả đầu NaN; cực đại rolling 07/11, cửa sổ 01–07/11 `[14,0,0,3,4,5,6]`, mean 32/7.
Cực đại gốc 01/11 = 14; trễ 6 ngày chỉ của ví dụ, rolling không tự dự báo hay giải thích nguyên nhân.

```python
tb7 = s.rolling(7, min_periods=7, center=False).mean()
ngay = tb7.idxmax()
w = s.loc[ngay-pd.Timedelta(days=6):ngay]
assert len(w)==7 and abs(w.mean()-tb7.loc[ngay]) < 1e-9
```

### B8-030

`doi = q/q.shift(4)-1`; quý I/2026 so quý I/2025: 50/40−1 = 0,25 = 25%.
shift(12) là 3 năm, chuỗi này không đủ; kiểm gốc bằng đếm review từ 01/01/2025 đến trước 01/04/2025.

### B8-MR06

Cuối chuỗi: 3 hàng lấy `[0,NaN,8]` → 4; 3D loại biên trái 02/06 09:00, còn `[NaN,8]` → NaN.
min_periods đếm giá trị biết, có tính 0; không suy 03/06 bằng 0:

```python
a = s.rolling(3, min_periods=2, center=False).mean()
b = s.rolling('3D', min_periods=2, center=False, closed='right').mean()
```

### B8-038

Cũ đọc 08/04→08/07, ra 91 ngày; đúng 04/08→07/08, 3 đêm.
Hiển thị ISO không chứng minh đọc đúng nguồn; cần format DD/MM/YYYY:

```python
vao = pd.to_datetime(vao_raw, format='%d/%m/%Y')
ra = pd.to_datetime(ra_raw, format='%d/%m/%Y')
so_dem = (ra-vao).days
```

### B8-039

Sửa format/ME; giữ tháng 6 vì đã thu đủ, số đếm `[2,2,2]`, dem6=2, tổng 6; khớp số chưa chứng minh xu hướng/nhân quả.
Khai báo AI: ChatGPT hỗ trợ theo định dạng/phạm vi đề, tôi tự kiểm tháng 6 bằng mask và tổng review.

```python
rv['date'] = pd.to_datetime(rv['date'], format='%d/%m/%Y')
m = rv.set_index('date').sort_index().resample('ME').size()
m = m.loc[m.index <= pd.Timestamp('2026-06-30')]
dem6 = ((rv['date'] >= '2026-06-01') & (rv['date'] < '2026-07-01')).sum()
assert dem6 == m.loc['2026-06-30'] and m.sum() == len(rv)
```

### B8-040

Cũ 30%, trọng số mỗi tháng bằng nhau; sửa `bao_cao = nay.sum()/goc.sum()-1` → 5,0%, gốc 400 review quý I/2025.
Tháng 3 giảm 10% so tháng 3/2025 không mâu thuẫn tổng quý tăng; in `f'{bao_cao:.1%}'`.

### B8-048

Cũ giữ 3, đúng giữ hàng 0–3 gồm 4 review; mốc 30/06 00:00 bỏ sót buổi chiều, không chứng minh nguồn thiếu.
Tháng 6 đã trọn; sự kiện 01/07 không chứng minh tháng 7 trọn:

```python
giu = (t >= pd.Timestamp('2026-06-01')) & (t < pd.Timestamp('2026-07-01'))
so = int(giu.sum())
```

### B8-049

`tb = s.rolling(7,min_periods=7,center=False).mean()`; 07/06 và 08/06 đều NaN, không điền 0.
Cửa sổ 02–08/06 `[2,NaN,4,0,6,8,10]`; min_periods=6 cho 5 trên 6 giá biết, chưa là mean đủ 7 ngày.

### B8-050

Tháng 1: 930/62 = 15/ngày; tháng 2: 860/57 ≈ 15,087719/ngày; tổng giảm 7,5% nhưng mức/ngày tăng 0,6%.
Gộp tổng review/tổng ngày; mean các mức năm không cân số ngày, kỳ gốc phải cùng đại lượng tháng 1.

```python
ngay = pd.Series(m.index.days_in_month, index=m.index)
tong = m.groupby(m.index.month).sum()
tb = tong/ngay.groupby(ngay.index.month).sum()
p_tong, p_ngay = tong.loc[2]/tong.loc[1]-1, tb.loc[2]/tb.loc[1]-1
```

### B8-MR10

Giữ hàng 1/2; báo 01/01:2, 02/01:NaN; phạm vi đầy đủ cho 2 review/ngày.
Sự kiện 02/01 00:00 không xác nhận trọn ngày, không dùng làm tổng ngày hoặc tự điền 0.

```python
v = pd.to_datetime(raw, format='%Y-%m-%d %H:%M', utc=True).dt.tz_convert('Asia/Ho_Chi_Minh')
dau = pd.Timestamp('2027-01-01', tz='Asia/Ho_Chi_Minh')
cuoi = pd.Timestamp('2027-01-02', tz='Asia/Ho_Chi_Minh')
giu = (v >= dau) & (v < cuoi)
dem = pd.Series(1, index=pd.DatetimeIndex(v[giu])).resample('D').size()
bao_cao = dem.reindex(lich)
```

### B8-057

Sai format/M và size đếm hàng thay review; đúng tổng 20/10, tổng chung 30; mức/ngày 20/31 và 10/5 = 2.
Tháng 2 mới 5 ngày, chưa được gọi tổng giảm 50% là biến động tháng trọn; có thể so 01–05 của hai tháng.

```python
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
m = df.set_index('date')['n'].resample('ME').sum()
tb1, tb2 = m.loc['2024-01-31']/31, m.loc['2024-02-29']/5
```

### B8-058

Lọc năm trước rolling; 01–06/01 là NaN, 07/01 dùng `[1,1,1,1,1,1,7]`, mean 13/7.
Rolling trước rồi lọc vẫn dùng 31/12/2024 cho 06/01, sai phạm vi chỉ dùng 2025.

```python
nam = s.loc['2025']
tb7 = nam.rolling(7, min_periods=7, center=False).mean()
w = nam.loc['2025-01-01':'2025-01-07']
assert abs(tb7.loc['2025-01-07']-w.mean()) < 1e-9
```

### B8-059

Chỉ số 150: cao hơn mean 12 tổng tháng 50%, mốc 100 là mean; điều chỉnh 180/120=1,5 và 264/240=1,1.
Tháng 8 tổng cao hơn nhưng tỷ số thấp hơn; chưa loại hết xu hướng/số ngày/mùa hay chứng minh nguyên nhân.

### B8-060

Giữ hàng 1/2/3, được 3 review/ngày; hàng 2 là 01/01/2027 thứ Sáu, dayofweek=4.
Không tự gán UTC cho ngày thuần khi nguồn chưa quy định thời điểm/múi giờ.

```python
v = pd.to_datetime(raw, format='%Y-%m-%d %H:%M', utc=True).dt.tz_convert('Asia/Ho_Chi_Minh')
dau = pd.Timestamp('2027-01-01', tz='Asia/Ho_Chi_Minh')
cuoi = pd.Timestamp('2027-01-02', tz='Asia/Ho_Chi_Minh')
giu = (v >= dau) & (v < cuoi)
so = int(giu.sum())
```

### B8-MR12

(a) 3 sự kiện: 30/06 01:00, 01/07 01:00, 03/07 00:00; (b) ngày 01–03/07: `[1,0,1]`, tổng 2.
Hai cửa sổ khác biên: (30/06 00:00,03/07 00:00] và [01/07 00:00,04/07 00:00), nên không mâu thuẫn.

```python
v = pd.to_datetime(raw, format='%Y-%m-%d %H:%M', utc=True).tz_convert('Asia/Ho_Chi_Minh')
ev = pd.Series(1, index=v).sort_index()
t = pd.Timestamp('2026-07-03', tz='Asia/Ho_Chi_Minh')
a = ev.rolling('3D', min_periods=1, closed='right').sum().loc[t]
d = ev.resample('D').size().reindex(lich, fill_value=0)
b = d.rolling(3, min_periods=3, center=False).sum().loc[t]
```
