# Bài 4 — Đáp án rút gọn

Đối chiếu với [đề bài](Bai4_60_cau_hoi.md). Đủ 60 câu: 40 trắc nghiệm, 20 tự luận.

Trắc nghiệm chỉ ghi lựa chọn; tự luận ghi kết quả và phần giải thích tối đa 2 dòng. Đoạn mã được giữ khi đề yêu cầu viết hoặc sửa mã.

## Trắc nghiệm

| Mã câu | Đáp án |
|---|:---:|
| B4-001 | C |
| B4-002 | A |
| B4-003 | B |
| B4-004 | C |
| B4-005 | D |
| B4-006 | B |
| B4-007 | A |
| B4-011 | D |
| B4-012 | B |
| B4-013 | A |
| B4-014 | D |
| B4-015 | C |
| B4-016 | A |
| B4-017 | B |
| B4-021 | D |
| B4-022 | C |
| B4-023 | A |
| B4-024 | C |
| B4-025 | D |
| B4-026 | C |
| B4-027 | B |
| B4-031 | C |
| B4-032 | C |
| B4-033 | B |
| B4-034 | A |
| B4-035 | A |
| B4-036 | D |
| B4-037 | D |
| B4-041 | B |
| B4-042 | D |
| B4-043 | A |
| B4-044 | B |
| B4-045 | A |
| B4-046 | C |
| B4-051 | B |
| B4-052 | B |
| B4-053 | D |
| B4-054 | D |
| B4-055 | C |
| B4-056 | A |

## Tự luận

### B4-008

p = 2/5 = 40%; hai giá thiếu không chứng minh ≥80 và không được tự điền 0.
`q = (df.loc[df["gia"].notna(), "gia"] < 80).mean()` = 2/3 ≈ 66,67%; chênh 26,67 điểm phần trăm.

### B4-009

In `[120.0,360.0]` vì sửa s không sửa bảng dưới CoW; chỉ sửa giá thì in `[90.0,360.0]`, tiền vẫn cũ.
Sau sửa đủ: giá `[90,50,60]`, ba đêm `[270,150,180]`; df giữ `[120,50,80]`, PR giữ 50.

```python
bao_gia.loc[mask, "gia"] *= 0.75
bao_gia["ba_dem"] = bao_gia["gia"] * 3
```

### B4-010

KeyError: r giữ nhãn `[10,30,40]`; sửa `print(r.iloc[1,1])` được 40.0.
`r.loc[[30],"gia"]`: Series (1,); `r.loc[[30],["gia"]]`: DataFrame (1,1).

### B4-018

Mean từng lần 90/70, giảm 20; cùng a,b,c thì mean 60/70, mỗi chỗ tăng 10; giá lần 2 của d chưa biết.
Hai chiều khác nhau vì tập hàng khác; giữ nhóm chung để so:

```python
chung = df["lan_1"].notna() & df["lan_2"].notna()
tb1 = df.loc[chung, "lan_1"].mean()
tb2 = df.loc[chung, "lan_2"].mean()
```

### B4-019

In `380.0 760.0`: gán qua bảng trung gian không sửa bao_gia; chỉ sửa giá thì `330.0 760.0`.
Sau tính lại: giá `[120,50,80,80]`, hai đêm `[240,100,160,160]`, tổng 660; PR và nguon giữ nguyên.

```python
bao_gia.loc[m, "gia"] *= 0.8
bao_gia["hai_dem"] = bao_gia["gia"] * 2
```

### B4-020

Theo thứ tự (nhãn, gia, id): `(4,50,B2), (15,65,E1), (7,75,D4), (12,95,A7)`.

```python
r = df.loc[df["loai"].isin(["Studio", "Phòng riêng"]), ["gia", "id"]].sort_values("gia")
```

### B4-028

Top: nhãn 27, X5, 860; mean/median trước 200/40, sau 35/35; df vẫn 5 hàng.
860 kéo mean mạnh hơn median; giữ mã X5/X1, kiểm đơn vị và nguồn trước kết luận giá lớn/nhỏ sai.

```python
top = df.nlargest(1, "gia")[["id", "gia"]]
sau = df.drop(top.index)
truoc_mean, truoc_median = df["gia"].mean(), df["gia"].median()
sau_mean, sau_median = sau["gia"].mean(), sau["gia"].median()
```

### B4-029

In `[60.0,50.0,100.0]` vì thu/goc cùng đối tượng; CoW không bảo vệ phép gán tên này.
Khôi phục từ truoc; kiểm goc = `[60,80,100]`, thu = `[60,50,100]`; copy sau sửa không tự phục hồi 80.

```python
goc = truoc.copy()
thu = goc.copy()
thu.loc["b", "gia"] = 50.
```

### B4-030

and/or đòi một bool, Series có nhiều phần tử nên gây ValueError; dùng &/| với ngoặc.
Giữ S1/S4; giá 60 không <60, NaN không qua so sánh nhưng chưa biết có vượt ngưỡng không.

```python
m = (((df["loai"] == "Studio") & (df["gia"] <= 90))
     | ((df["loai"] == "PR") & (df["gia"] < 60)))
```

### B4-038

In 12.0 vì chia 5 thay vì 3 giá đã biết; sửa `tb = s.mean()` được 20.0.
Điền hai NaN bằng 0 tạo giá giả; giá 0 vốn có vẫn là quan sát hợp lệ.

### B4-039

In `[63.0,330.0]`: phí bị nhân 3, tổng dùng giá cũ; sửa được tổng `[270,229,270]`, nguồn giữ nguyên.
C rẻ nhất từ 7 đêm: n=6 cho A/B/C=540/418/420, n=7 cho 630/481/470.

```python
bao = nguon.copy()
bao.loc["B", "gia"] *= 0.9
bao["tong"] = bao["gia"] * 3 + bao["phi"]
```

### B4-040

In 60; r có nhãn `[1,3,6]`, loc[1:3] lấy nhãn 1/3, gồm cận cuối.
Sửa `print(r.iloc[1:3,0].sum())` được 100; iloc lấy vị trí 1/2, bỏ stop 3.

### B4-047

True chỉ kiểm shape/tổng, chưa kiểm cặp id–giá; kiểm dưới đây cho False.
Khớp goc vẫn chưa chứng minh giá thực tế đúng; cần tra mã, đơn vị và ngữ cảnh nguồn.

```python
a, b = goc.sort_values("id"), lai.sort_values("id")
dung = a["id"].tolist() == b["id"].tolist() and a["gia"].tolist() == b["gia"].tolist()
```

### B4-048

Bao cũ: shape (2,3), nhãn w/y, giá `[50,30]`, hai đêm `[200,120]`; đã mất PR và giữ tiền cũ.
Đúng: shape (4,3), giá `[50,80,30,40]`, hai đêm `[100,160,60,80]`; nguon giữ giá/cột gốc.

```python
bao = nguon.copy()
bao.loc[bao["loai"] == "NC", "gia"] *= 0.5
bao["hai"] = bao["gia"] * 2
```

### B4-049

`s.value_counts()` → NC:2, PR:1, Shared:1; `s.value_counts(normalize=True)` → 0,5/0,25/0,25, mẫu số 4.
`s.isna().sum()` = 2; `s.isna().mean()` = 1/3; chia số đếm cho 6 không khớp normalize mặc định.

### B4-050

Category lưu hai nhãn Đông/Tây cùng 6 mã tham chiếu; lần đo này khu giảm bộ nhớ, id tăng.
deep=True tính cả nội dung chuỗi; khu lặp phù hợp hơn id duy nhất, không bảo đảm mọi cột đều tiết kiệm.

### B4-057

B: 3 chỗ, 50% trên 6 hàng; median B/toàn bảng = 60/50, cao hơn 20%; B chỉ có 2 giá biết.
Tỷ trọng mô tả chỗ ở trong snapshot, chưa phải lượt đặt hay thị phần thực tế toàn thành phố.

```python
q = df.loc[df["quan"] == TEN_QUAN]
so_cho, ty_trong = len(q), len(q)/len(df)
tv_quan, tv_tp = q["gia"].median(), df["gia"].median()
chenh_pct = (tv_quan/tv_tp - 1)*100
```

### B4-058

Theo thứ tự (nhãn,id,giá): `(5,U6,20), (1,U2,40), (4,U5,60)`.
Giữ id để truy nguồn; giá 20 chưa chắc sai, cần kiểm đơn vị/ngữ cảnh U6.

```python
r = df.loc[df["loai"].isin(["NC", "PR"]), ["id", "gia"]].nsmallest(3, "gia")
```

### B4-059

In `540.0 360.0`; tam riêng nên chưa sửa bao; chỉ sửa giá trong bao thì tiền vẫn 540.
Sau tính lại: giá `[20,60,40]`, ba đêm `[60,180,120]`, tổng 360; B giữ 60/180, goc giữ giá/cột gốc.

```python
bao.loc[bao["loai"] == "A", "gia"] *= 0.5
bao["ba_dem"] = bao["gia"] * 3
```

### B4-060

File cũ mất mã vì bỏ index; thứ tự đã sắp không khôi phục được mã; xuất lại bằng index_label="ma".
Đọc lại: (3,2), cột ma/gia, 0 thiếu, tổng 90, cặp R7–15/R9–30/R2–45; chưa chứng minh giá nguồn đúng.

```python
gui.to_csv("bang_060.csv", index_label="ma")
lai = pd.read_csv("bang_060.csv")
```
