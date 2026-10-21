# Bài 6 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai6_72_cau_hoi.md). Đủ 72 câu: 48 trắc nghiệm, 24 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B6-001 | B |
| B6-002 | A |
| B6-003 | C |
| B6-004 | B |
| B6-005 | C |
| B6-006 | C |
| B6-007 | D |
| B6-MR01 | C |
| B6-MR02 | C |
| B6-011 | D |
| B6-012 | A |
| B6-013 | D |
| B6-014 | A |
| B6-015 | C |
| B6-016 | B |
| B6-017 | D |
| B6-MR03 | D |
| B6-021 | C |
| B6-022 | B |
| B6-023 | C |
| B6-024 | D |
| B6-025 | A |
| B6-026 | B |
| B6-027 | B |
| B6-MR05 | D |
| B6-MR06 | B |
| B6-031 | D |
| B6-032 | B |
| B6-033 | A |
| B6-034 | C |
| B6-035 | B |
| B6-036 | C |
| B6-037 | C |
| B6-MR07 | A |
| B6-041 | A |
| B6-042 | C |
| B6-043 | A |
| B6-044 | A |
| B6-045 | A |
| B6-046 | D |
| B6-MR09 | A |
| B6-051 | B |
| B6-052 | A |
| B6-053 | D |
| B6-054 | D |
| B6-055 | B |
| B6-056 | D |
| B6-MR11 | B |

## Tự luận

### B6-008

(a) B:(2,80); (b) A:(2,60), B:(2,80), bỏ WHERE và đổi cả COUNT(*) thành COUNT(gia).
AVG chia số giá biết; C không có giá, COUNT(*) sẽ đếm nhầm hai hàng thiếu.

```sql
SELECT khu, COUNT(*) AS n, AVG(gia) AS tb FROM d
WHERE gia>=60 GROUP BY khu HAVING COUNT(*)>=2 ORDER BY khu;
```

### B6-009

Mean NA=10, TB=15, -=NaN; có 3 giá thiếu, id đầu "001", giữ giá 0.
NA chung làm mất mã khu hợp lệ; chỉ khai thiếu cho cột gia:

```python
d = pd.read_csv('gia.csv', keep_default_na=False,
    dtype={'id':'str','khu':'str','gia':'float64'}, na_values={'gia':['?','-','']})
```

### B6-010

id đầu = 1, price đầu = '$12.00'; Parquet giữ dữ liệu đã đọc, không phục hồi "001" hay tự chuyển tiền thành số.
Đọc lại raw với `dtype={'id':'str'}`, xử lý giá theo schema rồi lưu; kiểm mã, kiểu và giá trị sau đọc lại.

### B6-018

503 là HTTP lỗi; JSON đọc được nhưng không có daily nên code cũ gây KeyError.
Kiểm HTTP trước; với 200 vẫn kiểm đơn vị và ngày/địa điểm/timezone:

```python
r.raise_for_status()
x = r.json()
d = pd.DataFrame(x['daily'])
```

### B6-019

(a) A:2, B:2; (b) chỉ B:2 khi đổi cả COUNT(*) thành COUNT(diem), giữ WHERE năm.
A năm 2025 chỉ có 1 điểm biết; review 2024 không thuộc phạm vi.

```sql
SELECT listing_id,COUNT(*) AS n FROM rv
WHERE year(date)=2025 GROUP BY listing_id
HAVING COUNT(*)>=2 ORDER BY listing_id;
```

### B6-020

Khu của 101/104 bị thành thiếu; dtype chuỗi không ngăn nhận diện NA chung.
Kiểm khu = `['?','NA','TB','?']`, một gia thiếu và giá cuối 0:

```python
d = pd.read_csv('d.csv', keep_default_na=False, na_values={'gia':['?']},
    dtype={'id':'str','khu':'str','gia':'float64'})
```

### B6-MR04

32.5

```python
s, n = 0.0, 0
for c in pd.read_csv('gia.csv', usecols=['gia'], chunksize=3):
    s += c['gia'].sum()
    n += c['gia'].count()
tb = s/n if n else np.nan
```

### B6-028

A:(2,2,0,15), B:(2,1,1,30), C:(2,0,2,NULL); thêm `HAVING COUNT(*)-COUNT(gia)>=1` để giữ B/C.
WHERE gia IS NULL bỏ giá biết và mất A, làm sai số hàng/mean của báo cáo.

```sql
SELECT khu,COUNT(*) AS n_hang,COUNT(gia) AS n_biet,
       COUNT(*)-COUNT(gia) AS n_thieu,AVG(gia) AS tb
FROM d GROUP BY khu ORDER BY khu;
```

### B6-029

Giữ raw để xử lý lại từ đầu; kiểm round-trip, mã "001", shape (4,2), một giá thiếu và giá 0.
Kết quả này không bảo đảm mọi backend biểu diễn dtype chuỗi giống hệt.

```python
d = pd.read_csv('raw/gia.csv', dtype={'id':'str','gia':'float64'})
d.to_parquet('processed/gia.parquet', index=False)
r = pd.read_parquet('processed/gia.parquet')
pd.testing.assert_frame_equal(d, r)
```

### B6-030

Mất A vì đã khớp phí 20, không có hàng đệm NULL để OR giữ lại; chuyển điều kiện phí vào ON.
Kết quả A:NULL, B:NULL, C:5, D:8; A không có đối ứng đạt ngưỡng, C có phí hợp lệ.

```sql
SELECT l.id,t.phi FROM l
LEFT JOIN t ON l.id=t.id AND t.phi<10 ORDER BY l.id;
```

### B6-038

Cùng nguồn/tên cột chưa chắc cùng schema; usecols không chuyển tiền tệ thành số.
Kiểm shape (4,2), id "001", price '$12.00'; làm rõ đơn vị/thiếu và cùng snapshot trước so mean.

```python
d = pd.read_csv('ban_day_du.csv.gz', usecols=['id','price'], dtype={'id':'str','price':'str'})
```

### B6-039

(a) phong:2; (b) nguyen_can:3, phong:3 khi đổi cả COUNT(first_review) thành COUNT(*), không lọc ngày thiếu.
Nguồn mỗi hàng một listing; có ngày first_review không cho biết tổng số review.

```sql
SELECT loai,COUNT(first_review) AS n FROM 'l.parquet'
GROUP BY loai HAVING COUNT(first_review)>=2 ORDER BY loai;
```

### B6-040

400 là lỗi tham số ngày đã nhận, không chứng minh Timeout; tăng timeout không sửa ngày.
timeout=20 không phải hạn cứng cho toàn yêu cầu; 400 khiến raise_for_status phát HTTPError:

```python
r.raise_for_status()
x = r.json()
```

### B6-MR08

Không: hai phép đọc khác số cột, chưa tách tác động định dạng; RAM khác kích thước file.
So cùng dữ liệu/cột/schema, kiểm kết quả bằng nhau, đo lặp cùng môi trường/cache; báo riêng file/RAM/thời gian.

### B6-047

Kiểm ngày là datetime, ngày đầu 2025-01-01, 4 hàng, mã đầu "001", một điểm thiếu.
Đọc thành công chưa đủ xác nhận schema hay nội dung:

```python
d = pd.read_csv('reviews.csv.gz', usecols=['listing_id','date','diem'],
    dtype={'listing_id':'str','diem':'float64'}, na_values={'diem':['?']}, parse_dates=['date'])
assert pd.api.types.is_datetime64_any_dtype(d['date'])
assert len(d)==4 and d.loc[0,'listing_id']=='001'
assert d.loc[0,'date']==pd.Timestamp('2025-01-01') and d['diem'].isna().sum()==1
```

### B6-048

Đang so °F với 35°C; HTTP/số hàng không kiểm đơn vị. t_c = `[35,30,40]`, giữ 01/02 và 03/02.
Kiểm daily_units và tính tay 95°F = 35°C, giữ đúng biên:

```python
d['t_c'] = (d['temperature_2m_max']-32)*5/9
hot = d.loc[d['t_c'] >= 35]
```

### B6-049

SQL có 3 nhóm, pandas mặc định 2 vì bỏ khu thiếu; sửa `d.groupby('khu',dropna=False).agg(n=('gia','size'),tb=('gia','mean'))`.
A:(2,10), B:(1,30), thiếu khu:(1,20); kết quả khớp chưa chứng minh đúng đối tượng, đơn vị hay mục tiêu.

### B6-050

Lưu r.content để giữ cả đơn vị/timezone; ghép ngày review theo cùng quy ước địa phương.
Timestamp theo giây có thể trùng; dùng tên duy nhất, đọc lại kiểm ngày/đơn vị/địa điểm và metadata.

```python
Path(raw_path).write_bytes(r.content)
meta = {'url':r.url, 'downloaded_at':downloaded_at}
Path(meta_path).write_text(json.dumps(meta), encoding='utf-8')
```

### B6-MR10

Mean 65, tổng 260 trên 4 giá đạt ngưỡng; chia 7 tính cả giá thiếu/ngoài ngưỡng, mean khối không cân số giá.

```python
s, n = 0.0, 0
for c in pd.read_csv('gia.csv', usecols=['gia'], chunksize=3):
    v = c.loc[c['gia'] >= 30, 'gia']
    s += v.sum()
    n += v.count()
tb = s/n if n else np.nan
```

### B6-057

Đọc mặc định có thể mất 0 đầu mã, biến khu NA thành thiếu, giữ date dạng chuỗi; CSV không lưu schema.
Kiểm round-trip: (4,4), mã/khu, ngày datetime, một diem thiếu và giá 0:

```python
r = pd.read_csv('review.csv', keep_default_na=False,
    dtype={'listing_id':'str','khu':'str','diem':'float64'},
    na_values={'diem':['']}, parse_dates=['date'])
pd.testing.assert_frame_equal(d, r)
```

### B6-058

Kiểm đủ ngày 01–03/07, đúng đại lượng/độ dài dãy, đơn vị °C và timezone/địa điểm yêu cầu.
Lưu raw cùng URL/thời điểm tải; phân tích lại bản đã lưu để giữ đúng dữ liệu từng dùng.

```python
params = dict(latitude=-33.45, longitude=-70.67, start_date='2025-07-01',
    end_date='2025-07-03', daily='temperature_2m_max', timezone='America/Santiago')
```

### B6-059

A:(1,NULL), B:(2,4.5), C/D:(0,NULL); COUNT(*) đếm hàng đệm, COUNT(diem) bỏ review thiếu điểm.
len=4 chưa kiểm số review/năm; đối chiếu từng id với r2/r3/r4:

```sql
SELECT l.id,COUNT(rv.rid) AS n_review,AVG(rv.diem) AS tb
FROM l LEFT JOIN rv ON l.id=rv.listing_id AND year(rv.date)=2025
GROUP BY l.id ORDER BY l.id;
```

### B6-060

Làm rõ hai số đo trùng 01/01, thống nhất khóa/ngày địa phương; không tự chọn 30 hay 31.
Đúng: 01/01:(30,2), 02/01:(32,2), 03/01:(33,NaN); so SQL cùng phạm vi/thiếu; str(1) chưa là "001".

```python
n = rv.assign(time=rv['date'].dt.strftime('%Y-%m-%d')).groupby('time').size().rename('n_review')
assert w_ok['time'].is_unique
kq = w_ok.merge(n.reset_index(), on='time', how='left', validate='one_to_one')
```

### B6-MR12

`l = l.assign(id=l['id'].astype('str'))`; quy ước không đệm 0 cho phép đổi này.
Kết quả `('1','An',2), ('2','Binh',2)`; lọc năm 2025 và ưu tiên mã tăng khi đồng hạng.

```sql
SELECT rv.listing_id,l.name,COUNT(*) AS n FROM rv
LEFT JOIN l ON rv.listing_id=l.id WHERE year(rv.date)=2025
GROUP BY rv.listing_id,l.name ORDER BY n DESC,rv.listing_id ASC LIMIT 2;
```
