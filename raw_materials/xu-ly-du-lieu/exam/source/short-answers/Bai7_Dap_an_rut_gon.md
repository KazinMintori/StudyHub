# Bài 7 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai7_80_cau_hoi.md). Đủ 80 câu: 52 trắc nghiệm, 28 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B7-001 | A |
| B7-002 | B |
| B7-003 | A |
| B7-004 | A |
| B7-005 | D |
| B7-006 | B |
| B7-007 | A |
| B7-011 | B |
| B7-012 | D |
| B7-013 | D |
| B7-014 | B |
| B7-015 | D |
| B7-016 | A |
| B7-017 | D |
| B7-021 | B |
| B7-022 | C |
| B7-023 | D |
| B7-024 | A |
| B7-025 | B |
| B7-026 | A |
| B7-027 | B |
| B7-031 | D |
| B7-032 | C |
| B7-033 | A |
| B7-034 | D |
| B7-035 | A |
| B7-036 | B |
| B7-037 | C |
| B7-041 | C |
| B7-042 | C |
| B7-043 | C |
| B7-044 | C |
| B7-045 | C |
| B7-046 | A |
| B7-051 | D |
| B7-052 | B |
| B7-053 | C |
| B7-054 | B |
| B7-055 | C |
| B7-056 | D |
| B7-R01 | C |
| B7-R02 | D |
| B7-R03 | A |
| B7-R05 | A |
| B7-R07 | C |
| B7-R09 | B |
| B7-R11 | C |
| B7-R13 | D |
| B7-R15 | A |
| B7-R18 | B |
| B7-R19 | D |
| B7-R20 | B |

## Tự luận

### B7-008

parsed A/B/C/D/E = `[2000,NaN,NaN,NaN,0]`; lỗi C/D, thiếu nguồn B.
Không fillna(0) vì sẽ lẫn thiếu/lỗi với E có giá 0 thật; giữ raw:

```python
clean = raw.str.strip().str.replace(r'[$,]', '', regex=True)
parsed = pd.to_numeric(clean, errors='coerce')
loi = raw.notna() & parsed.isna()
```

### B7-009

Nhãn 20→'3', 50→'5', kiểu chuỗi; 10/30/40 thiếu.
`_`, số 2 sau BR và x trước 4 đều cản ranh giới từ; không khớp chưa chứng minh 0 phòng.

### B7-010

2/4 = 0,5: A/E có wifi, B rỗng vẫn được tính, C chưa biết bị loại.
Đếm mục sau explode/dropna cho 3/4, trước dropna cho 3/5, đều khác tỷ lệ listing:

```python
ds = raw.dropna().map(json.loads)
co = ds.map(lambda xs: any(x.strip().lower() == 'wifi' for x in xs))
ty_le = co.mean()
```

### B7-018

m theo 8/2/9/5 = `[True,False,True,False]`, mean 2/4; `m[s.notna()].mean()` = 2/3.
Chứa “metro” chỉ là nhắc từ, có thể là “metros” hoặc phủ định, chưa xác minh gần metro.

### B7-019

A→'2', B→'3', C/D/E thiếu; C thiếu ranh giới trước 4, D thiếu ranh giới sau bath vì dấu _.
Kết quả còn là chuỗi, không khớp không thay bằng 0:

```python
p = r'\b([0-9]+)\s*(?:WC|bathrooms?|baths?)\b'
x = s.str.extract(p, flags=re.I, expand=False)
```

### B7-020

stove, gas:1; wifi:2; tv:1; tỷ lệ wifi 2/4, C rỗng vẫn trong mẫu số.
split(',') làm vỡ tên tiện nghi; value_counts đếm lặp wifi của B:

```python
ds = raw.map(json.loads)
muc = ds.explode().dropna().str.strip().str.lower()
bang = muc.to_frame('nhan').reset_index(names='id')
dem = bang.groupby('nhan')['id'].nunique()
ty_le = dem.get('wifi', 0)/len(ds)
```

### B7-028

tv:2, wifi:2; TV đúng 2/4, cách sai 2/3 vì bỏ B rỗng khỏi mẫu số; A chỉ đếm một listing.
Giữ ds gốc để đếm đủ listing:

```python
m = ds.explode().dropna().str.strip().str.lower()
t = m.to_frame('nhan').reset_index(names='id')
n = t.groupby('nhan')['id'].nunique()
ty_le_tv = n['tv']/len(ds)
```

### B7-029

Đo cùng dữ liệu/backend, cùng thao tác và phạm vi chuyển kiểu; đối chiếu giá trị, index, vị trí thiếu trước đo.
Đo lặp, ghi môi trường; một phép đo không chứng minh apply hay .str luôn nhanh hơn.

### B7-030

`ok = raw.str.strip().str.fullmatch(p, na=False)`; chỉ hàng 1/3 hợp lệ.
contains chỉ tìm đoạn; bỏ phẩy rồi chuyển số có thể che tiền tố hoặc phân cách nghìn sai.

### B7-038

`s_chuan = s.str.strip().str.lower()` → wifi:2, wifi!:1, wi-fi:1, café:1, cafe:1.
Index `[9,4,8,1,7,3]` và s gốc giữ nguyên; xóa dấu câu/dấu tiếng vượt quy tắc.

### B7-039

A/B/C = 46.5/32.5/80 m², D/E thiếu; “80 M2” khớp, “30m2x” thiếu ranh giới cuối.

```python
p = r'\b([0-9]+(?:[.,][0-9]+)?)\s*m(?:2|²)\b'
x = s.str.extract(p, flags=re.I, expand=False)
area = pd.to_numeric(x.str.replace(',', '.', regex=False), errors='coerce')
```

### B7-040

e có 5 hàng, B/D là placeholder; dropna còn 3. Mean eq('Wifi') trước/sau = 2/5 và 2/3.
Tỷ lệ listing đúng `ds.map(lambda xs: 'Wifi' in xs).mean()` = 2/4; mỗi listing chỉ một trọng số.

### B7-047

parsed = `[NaN,0,NaN,NaN,30]`; lỗi hàng 0/2, hàng 3 thiếu nguồn.
Không fillna(0) để tránh lẫn với giá 0 hợp lệ; giữ raw và chỉ chuyển chuỗi đúng toàn định dạng:

```python
c = raw.str.strip()
ok = c.str.fullmatch(p, na=False)
parsed = pd.to_numeric(c.where(ok).str.replace(r'[$,]', '', regex=True), errors='coerce')
loi = raw.notna() & ~ok
```

### B7-048

Đã biết: 2/4 = 0,5; quan sát liệt kê trên mọi listing: 2/5 = 0,4, chưa xác minh trạng thái C.
Kiểm co có 4 nhãn, A/E True, B/D False, tổng 2 để bắt bỏ [] hoặc đếm lặp:

```python
co = ds.dropna().map(lambda xs: 'Wifi' in xs)
ty_le_biet, ty_le_quan_sat = co.mean(), co.sum()/len(ds)
```

### B7-049

x = `['Central','todo','Museo',NaN]`; mẫu chỉ lấy một từ, không xác định đầy đủ tên địa điểm.
Đặt cột tu_sau_gan, đọc nguyên câu khớp/không khớp; nhắc metro/wifi chưa xác minh khoảng cách/hài lòng.

### B7-050

a: A='1', B thiếu, C='3'; b shape (3,1): (A,0)='1', (A,1)='2', (C,0)='3'.
len(b)=3 đếm cụm khớp, chỉ có 2 listing khớp A/C; không chứng minh số listing thật sự có phòng.

### B7-057

`lo = s.str.lower()` → `['straße','strasse','café','cafe']`, 4 nhãn; `fold = s.str.casefold()` → 3 nhãn.
fold = `['strasse','strasse','café','cafe']`; cả hai giữ index `[3,8,2,6]` và s gốc, không xóa dấu café.

### B7-058

home dùng 100/300, median 200; room dùng 20/1000/40, median 40; mean hoặc điền 0 làm đổi đại lượng/tập giá.
Kiểm raw có 1 thiếu, không lỗi chuyển đổi; d/raw vẫn nguyên:

```python
t = d.assign(loai_chuan=d['loai'].str.strip().str.lower(),
    gia=pd.to_numeric(d['raw'].str.replace(r'[$,]', '', regex=True), errors='coerce'))
kq = t.groupby('loai_chuan')['gia'].median()
```

### B7-059

`t = s.str.replace('<br/>',' ',regex=False)` → `['A B C','<br> X','<BR/>Y','<b>Z</b>']`.
1 review bị tác động, 2 lần thay, giảm 8 ký tự; bỏ qua hoa thường hoặc gọi là xóa mọi HTML vượt quy tắc.

### B7-060

Trong cấu hình đã cho, contains trên Arrow dùng ranh giới ASCII, extract và storage Python dùng Python re.
Không khái quát mọi backend; ghi phiên bản/storage/flags/phương thức, thử ca Unicode/ASCII/thiếu và đối chiếu re.

### B7-R04

`False, True, False, False, False`; fullmatch kiểm toàn chuỗi, vẫn strip sẽ nhận nhầm ' Apa'.

```python
def hop_le(text):
    return False if text is None else re.fullmatch(r'[A-C][n-p][a-c]', text) is not None
```

### B7-R06

Mẫu cũ bỏ 'aac', nhận nhầm 'ab'; a{2,}: ít nhất 2 a, b*: có thể vắng, c+: ít nhất 1 c.

```python
def hop_le(text):
    return False if text is None else re.fullmatch(r'a{2,}b*c+', text) is not None
```

### B7-R08

`False, True, True, False, False`; đổi * thành + để bắt buộc ít nhất một ký tự trắng, gồm tab/newline.

```python
def hop_le(text):
    return False if text is None else re.fullmatch(r'[0-9]+\.\s+abc', text) is not None
```

### B7-R10

`None, '0', None, '2'`; gom hai đơn vị để cùng bắt buộc số và ranh giới từ.
2BR2BA vẫn không khớp ranh giới cuối; đúng mẫu chưa bao phủ mọi cách viết thực tế.

```python
p = r'\b([0-9]+)\s*(?:BR|bedrooms?)\b'
def lay_so(text):
    m = None if text is None else re.search(p, text, flags=re.I)
    return m.group(1) if m is not None else None
```

### B7-R12

`True, False, False, True, False`; sau mỗi phẩy cần 3 số, có e/E thì bắt buộc số mũ.

```python
I = r'(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)'
E = r'(?:[eE][+-]?[0-9]+)?'
p = r'[+-]?' + I + r'(?:\.[0-9]+)?' + E
def hop_le(text):
    return False if text is None else re.fullmatch(p, text) is not None
```

### B7-R14

`'Lan.01', None, None, None`; filter đặt ngoài nhóm bắt tên gốc nhưng vẫn trong mẫu kiểm email.
Regex chỉ kiểm hình thức giản lược, không xác minh hộp thư tồn tại.

```python
p = '(' + BASE + ')' + FILTER + '@' + DOMAIN
def ten_goc(text):
    m = None if text is None else re.fullmatch(p, text)
    return m.group(1) if m is not None else None
```

### B7-R16

`('scene.02-night','png'), None, None, None`; đổi nhóm lặp sang không bắt để chỉ trả hai trường.
fullmatch loại đuôi .jpg.tmp vì không kết thúc bằng mở rộng cho phép.

```python
p = r'([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)'
def lay_anh(text):
    m = None if text is None else re.fullmatch(p, text)
    return m.groups() if m is not None else None
```

### B7-R17

`'A  B', '', '', None, '\u00a0X\u00a0'`; chỉ cắt dấu cách/tab, giữ NBSP và khoảng trắng giữa chuỗi.
`if result:` làm mất chuỗi rỗng hợp lệ; đổi thành `if result is not None:`.

```python
def cat_dau_cuoi(text):
    if text is None: return None
    return re.fullmatch(r'[ \t]*(.*?)[ \t]*', text).group(1)
```
