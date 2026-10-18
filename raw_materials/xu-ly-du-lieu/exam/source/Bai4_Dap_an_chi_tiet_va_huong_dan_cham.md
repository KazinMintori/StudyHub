# Bài 4 — Đáp án chi tiết và hướng dẫn chấm tự luận

- Giả định pandas 3.0.x với Copy-on-Write; notebook tham chiếu 3.0.3. Code đã kiểm chứng trên pandas 3.0.1.
- Giả định `import pandas as pd` và `import numpy as np` đã chạy. Mỗi câu độc lập; khi chuyển câu, khởi tạo lại dữ liệu của câu đó.
- Cột giá trong các ví dụ số/NaN là `float64`; NaN là `np.nan`, không dùng nullable Float64/pd.NA.
- Cảnh báo được hiển thị và không cấu hình warnings thành errors. `ChainedAssignmentError` trong các câu này là cảnh báo, không tự làm dừng chương trình.
- Mỗi câu trắc nghiệm có đúng một phương án A/B/C/D. Ký hiệu `nan` trong phương án là giá trị thiếu. Bỏ qua khác biệt khoảng trắng khi in danh sách/tuple.
- Các bảng là giả lập; mã NC/PR/Shared và các tên loại được hiểu đúng như ghi trong từng câu. Phí ghi “một lần” chỉ thu một lần cho một lượt ở.
- Không yêu cầu nhớ số liệu snapshot Santiago hoặc số byte của môi trường khác. Câu 050 cung cấp số đo quan sát để diễn giải.

## Cách chấm

Mỗi tự luận có rubric riêng theo thang **5 điểm/câu** để luyện tập. Chấm theo từng tiêu chí, cho điểm phần đúng; một lỗi số học nhỏ không làm mất điểm cơ chế đã giải thích đúng. Chấp nhận code đúng tương đương, trừ khi đề bắt buộc dùng một hàm/cách chọn cụ thể. Không trừ điểm vì cách khác kém ngắn gọn hơn lời giải mẫu. Một bước sửa kỹ thuật đúng không tự có điểm cho yêu cầu còn thiếu về tập hàng, cột phụ thuộc hoặc ý nghĩa kết quả. Chấp nhận sai số làm tròn hợp lý khi tính tỷ lệ; phải đúng đơn vị %, tỷ lệ hoặc điểm phần trăm.

Trắc nghiệm: bảng đáp án nhanh chỉ để tra cứu; từng câu bên dưới giải thích lựa chọn đúng và lý do ba phương án còn lại sai. Mức độ là nhãn thiết kế, chưa đo độ khó thực nghiệm; quy mô ngân hàng không phải tỷ trọng đề thi chính thức.

## Nguồn và phạm vi

Đã đọc đủ: `Bài 4/bai-04-lam-quen-pandas.md`, toàn bộ `lecture_04.ipynb`, toàn bộ `lab_04.ipynb` (cả hướng dẫn, code, tự học, bài tập và yêu cầu kiểm chứng).

Đã đọc toàn bộ `2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf`, chú trọng câu 8,9,22; tham khảo chính `LTXLDL_AI_5.pdf`, `LTXLDL_DS_1.pdf`, `LTXLDL_DS_2.pdf`; bổ trợ `LTXLDL_AI_1.pdf`, `LTXLDL_AI_2.pdf`. Nội dung NumPy tuần3 chỉ dùng hiệu chỉnh phong cách hỏi. Không thiếu nguồn trong danh sách yêu cầu.

60 câu cốt lõi không dùng groupby/agg theo nhóm, merge, transform, khớp nhãn giữa hai Series, SQL, API, regex hoặc dữ liệu thời gian. agg đơn giản trên một Series vẫn thuộc Bài 4.

## Đáp án trắc nghiệm nhanh

| Đợt | Mã câu và đáp án |
|---|---|
| 1 | B4-001: **C**; B4-002: **A**; B4-003: **B**; B4-004: **C**; B4-005: **D**; B4-006: **B**; B4-007: **A** |
| 2 | B4-011: **D**; B4-012: **B**; B4-013: **A**; B4-014: **D**; B4-015: **C**; B4-016: **A**; B4-017: **B** |
| 3 | B4-021: **D**; B4-022: **C**; B4-023: **A**; B4-024: **C**; B4-025: **D**; B4-026: **C**; B4-027: **B** |
| 4 | B4-031: **C**; B4-032: **C**; B4-033: **B**; B4-034: **A**; B4-035: **A**; B4-036: **D**; B4-037: **D** |
| 5 | B4-041: **B**; B4-042: **D**; B4-043: **A**; B4-044: **B**; B4-045: **A**; B4-046: **C** |
| 6 | B4-051: **B**; B4-052: **B**; B4-053: **D**; B4-054: **D**; B4-055: **C**; B4-056: **A** |

## Đợt 1 — Đáp án và chấm bài

### B4-001 — C

**C đúng.** Ba hàng, hai cột dữ liệu `ma`, `gia`. Index không được tính vào số cột.

- A sai: đếm thêm index như một cột dữ liệu.
- B sai: đảo số hàng với số cột.
- D sai: dùng nhãn hàng thay cho tên cột.

**Nhãn:** nhóm chính 1; mục tiêu chính K02; phụ K01; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm index với cột dữ liệu hoặc đảo hai thành phần shape.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-002 — A

**A đúng.** Phép nhân tạo Series mới, giữ tên và nhãn, lan truyền NaN; giá trong `df` không đổi.

- B sai: phép toán không đánh lại index.
- C sai: NaN không tự biến thành 0.
- D sai: chưa có phép gán kết quả trở lại bảng gốc.

**Nhãn:** nhóm chính 1; mục tiêu chính K05; phụ K03; mức vận dụng.
**Sai lầm kiểm tra:** Tưởng phép toán trên Series làm mất nhãn, tự điền thiếu hoặc sửa đầu vào.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-003 — B

**B đúng.** `read_csv` tạo DataFrame. Ý nghĩa một hàng và đơn vị giá phải theo mô tả nguồn. Số 102 là trung bình các mã số, không phải thống kê giá.

- A sai: đổi chỗ ở thành lượt đặt phòng và diễn giải sai mã.
- C sai: đọc cả CSV ở đây trả DataFrame, không phải Series.
- D sai: phép tính dùng cột `id`, không dùng cột `price`.

**Nhãn:** nhóm chính 2; mục tiêu chính K07; phụ K08; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm đơn vị quan sát, vai trò cột và ý nghĩa nghiệp vụ của một phép tính chạy được.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-004 — C

**C đúng.** Có bốn hàng, ba giá đã biết. Mask là `[True, False, True, False]`, nên mean bằng 2/4.

- A sai: `count()` không đếm NaN.
- B sai: dùng mẫu số 3 trong khi code lấy mean trên bốn giá trị bool.
- D sai: loại giá 0 hợp lệ khỏi tử số.

**Nhãn:** nhóm chính 3; mục tiêu chính K18; phụ K14, K25; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm len/count, coi giá 0 là thiếu, chọn sai mẫu số mean bool.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-005 — D

**D đúng.** Sau lọc, nhãn là `[1,2,4,5]`, giá tương ứng `[30,70,50,90]`. `loc[2:4]` lấy nhãn 2 và 4: 120. `iloc[2:4]` lấy vị trí 2 và 3: 140.

- A sai: 210 là tổng cả bảng lọc, không phải lát loc.
- B sai: coi hai cách cắt dùng cùng cơ chế.
- C sai: đảo kết quả nhãn và vị trí.

**Nhãn:** nhóm chính 4; mục tiêu chính K23; phụ K22, K20; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm nhãn nguyên với vị trí sau lọc; tưởng index tự đánh lại.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-006 — B

**B đúng.** `a` và `df` cùng một bảng; `b` là bảng riêng. Hai cột `hai_dem` đều còn giá trị cũ 160.

- A sai: coi copy như gán thêm tên.
- C sai: coi cột dẫn xuất tự cập nhật.
- D sai: coi phép gán tên tạo bản sao.

**Nhãn:** nhóm chính 5; mục tiêu chính K30; phụ K31, K35; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm alias/copy và công thức tự cập nhật.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-007 — A

**A đúng.** `index=False` bỏ index dù nó có tên; bảng được xuất chỉ gồm `gia`.

- B sai: tên index không làm vô hiệu index=False.
- C sai: code đã yêu cầu bỏ index.
- D sai: CSV không bắt buộc có cột chỉ mục; read_csv tạo index mặc định.

**Nhãn:** nhóm chính 6; mục tiêu chính K38; mức nền tảng.
**Sai lầm kiểm tra:** Tưởng index có tên luôn được giữ khi xuất.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-008

a) p=2/5=0,4. Ba False gồm giá 120 và hai giá chưa biết, nên không được suy ra cả ba đều >=80. Chỉ một hàng được biết chắc có giá >=80. Không tự điền 0; điều đó tạo thêm giá miễn phí không có trong nguồn.

b)

```python
co_gia = df["gia"].notna()
q = (df.loc[co_gia, "gia"] < 80).mean()
```

q=2/3, vẫn giữ giá 0 hợp lệ.

c) p=40%; q≈66,67%; chênh lệch≈26,67 điểm phần trăm, không phải mức tăng tương đối 26,67%.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: mẫu số 5 (0,5); phân biệt False với biết chắc >=80 (1); không tự điền 0 (0,5) | 2 |
| b: lọc notna đúng (1); q=2/3 và giữ giá 0 (0,5) | 1,5 |
| c: hai phần trăm (0,5); chênh lệch 26,67 điểm phần trăm và đúng đơn vị (1) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 3; mục tiêu chính K18; phụ K19, K13; mức phân loại.
**Sai lầm kiểm tra:** Coi chưa biết là không đạt, tự điền 0, nhầm phần trăm với điểm phần trăm.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-009

a) In `[120.0,360.0]`. Sửa Series s không sửa bao_gia dưới CoW.

b)

```python
bao_gia.loc[mask, "gia"] = bao_gia.loc[mask, "gia"] * 0.75
```

c) Sau riêng b: `[90.0,360.0]`. Cột ba_dem còn giá trị cũ. Thêm sau sửa giá:

```python
bao_gia["ba_dem"] = bao_gia["gia"] * 3
assert bao_gia["gia"].tolist() == [90., 50., 60.]
assert bao_gia["ba_dem"].tolist() == [270., 150., 180.]
assert df["gia"].tolist() == [120., 50., 80.]
assert df.columns.tolist() == ["loai", "gia"]
```

Hàng PR giữ giá 50; nguồn không thêm cột hay bị đổi giá.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: output ban đầu (0,5); giải thích CoW đúng đối tượng (1) | 1,5 |
| b: gán trực tiếp đúng bảng/cột/hàng và hệ số | 1,5 |
| c: output sau riêng b (0,5); tính lại (0,5); kiểm ba hàng và nguồn giữ nguyên (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 5; mục tiêu chính K32; phụ K33, K35; mức phân loại.
**Sai lầm kiểm tra:** Sửa Series tưởng sửa bảng; sửa giá nhưng quên cột phụ thuộc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-010

a) KeyError vì r giữ nhãn `[10,30,40]`, không có nhãn 1. loc dùng nhãn.

b)

```python
print(r.iloc[1, 1])
```

In 40.0. Với bảng này, `r.loc[30,"gia"]` cũng đúng.

c) Biểu thức một tên cột trả Series shape `(1,)`; danh sách một tên cột trả DataFrame shape `(1,1)`.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: nhãn [10,30,40] (0,5); KeyError và lý do loc dùng nhãn (1) | 1,5 |
| b: chọn đúng ô (1); kết quả 40 (0,5) | 1,5 |
| c: mỗi biểu thức đúng cả kiểu và shape được 1 điểm | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 4; mục tiêu chính K23; phụ K20, K03; mức vận dụng.
**Sai lầm kiểm tra:** Tưởng index sau lọc tự đánh lại; nhầm nhãn/vị trí và Series/DataFrame.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### Cập nhật sau đợt 1

Lũy kế 10/60 câu: 7 trắc nghiệm, 3 tự luận.

| Nhóm chính | Đã xuất / kế hoạch |
|---|---:|
| 1 | 2 / 6 |
| 2 | 1 / 6 |
| 3 | 2 / 10 |
| 4 | 2 / 12 |
| 5 | 2 / 14 |
| 6 | 1 / 8 |
| 7 | 0 / 4 |

Mục tiêu đã có ít nhất một câu yêu cầu sử dụng (không đồng nghĩa mọi nhánh của mục rộng đã hoàn tất): K01, K02, K03, K05, K07, K08, K13, K14, K18, K19, K20, K22, K23, K25, K30, K31, K32, K33, K35, K38.
Mục tiêu chưa có câu: K04, K06, K09, K10, K11, K12, K15, K16, K17, K21, K24, K26, K27, K28, K29, K34, K36, K37, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50.


## Đợt 2 — Đáp án và chấm bài

### B4-011 — D

**D đúng.** Một tên cột cho Series một chiều shape(3,), dtype float64. Danh sách một tên cột giữ DataFrame hai chiều shape(3,1).

- A sai: đảo shape của Series và DataFrame.
- B sai: đảo kiểu trả về của tên đơn và danh sách tên.
- C sai: giá là float64, không phải int64.

**Nhãn:** nhóm chính 1; mục tiêu chính K03; phụ K04; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm kiểu, shape và dtype khi chọn cột.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-012 — B

**B đúng.** Có 6 hàng, gia có 4 non-null nên thiếu 2. Bốn giá biết20,40,60,80 có tổng 200 và mean 200/4=50.

- A sai: mean bỏ qua hai NaN. Nếu tự thay chúng bằng 0, mean thành 200/6≈33,33, không phải50.
- C sai: đọc số không thiếu 4 thành số thiếu 4.
- D sai: 50% là trung vị, không phải tỷ lệ giá bằng 50. Không giá nào trong bảng bằng 50; median là trung bình40 và60.

**Nhãn:** nhóm chính 2; mục tiêu chính K10; phụ K11, K12; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm non-null với thiếu và phân vị với tần suất.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-013 — A

**A đúng.** s==np.nan cho bốn False; isna nhận đúng một ô thiếu; count đếm ba giá biết gồm cả0.

- B sai: phép bằng không xác định NaN.
- C sai: bỏ sót NaN và tính nó như giá đã biết.
- D sai: coi0 là giá thiếu thứ hai.

**Nhãn:** nhóm chính 3; mục tiêu chính K14; phụ K13; mức nền tảng.
**Sai lầm kiểm tra:** Dùng == np.nan hoặc coi 0 là thiếu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-014 — D

**D đúng.** H1,H3 là Studio giá 90,100 thỏa <=100; H2 là Phòng riêng giá 60 thỏa <75. H4 giá 75 không thỏa <75; H5 khác loại; H6 thiếu giá nên so sánh cho False.

- A sai: giữ H4 do nhầm < với <= ở ngưỡng75.
- B sai: bỏ H3 do nhầm <= với < ở ngưỡng100.
- C sai: như thể yêu cầu đồng thời là Studio và Phòng riêng, thay vì hoặc giữa hai nhánh.

**Nhãn:** nhóm chính 4; mục tiêu chính K24; phụ K25; mức vận dụng.
**Sai lầm kiểm tra:** Sai biên < / <= và sai ghép và/hoặc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-015 — C

**C đúng.** Gán nối tiếp không sửa df và phát cảnh báo ChainedAssignmentError. Code vẫn chạy; loc sau đó đặt giá hàng B thành 45. Hai hàng A giữ80,100.

- A sai: tưởng phép gán nối tiếp đã đổi A thành 60.
- B sai: coi cảnh báo là ngoại lệ dừng dưới giả định đã nêu.
- D sai: tưởng cảnh báo làm lệnh loc tiếp theo cũng không có tác dụng.

**Nhãn:** nhóm chính 5; mục tiêu chính K34; phụ K33; mức vận dụng.
**Sai lầm kiểm tra:** Coi cảnh báo là ngoại lệ dừng hoặc tưởng chained assignment sửa được bảng.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-016 — A

**A đúng.** to_csv mặc định ghi index. Vì index tên dong, cột được ghi mang tên dong, chứa7,2,9. id vẫn là cột dữ liệu riêng chứaM8,M2,M5.

- B sai: tưởng mặc định index=False.
- C sai: quên index đã được đặt tên dong.
- D sai: lấy nhãn index thay giá trị của cột id.

**Nhãn:** nhóm chính 6; mục tiêu chính K37; phụ K38; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm index được ghi với cột id.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-017 — B

**B đúng.** Các nhãn không thiếu khác nhau là Bắc,Nam,Tây; nunique mặc định bỏ thiếu. khu có nhãn phân loại lặp; id có sáu mã riêng.

- A sai: đếm thiếu như một nhãn thứ tư.
- C sai: chọn khóa riêng từng hàng thay cho nhãn lặp.
- D sai: lấy số hàng làm số nhãn khác nhau.

Cân nhắc category không bảo đảm bảng nhỏ này luôn giảm bộ nhớ; cần đo theo dữ liệu và môi trường.

**Nhãn:** nhóm chính 7; mục tiêu chính K44; phụ K45; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm số hàng với số nhãn; chọn category cho khóa riêng.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-018

a) Lần1: (30+60+90+180)/4=90; lần2: (40+70+100)/3=70. Trung bình các giá đã biết giảm 20 USD/đêm.

b)

```python
chung = df["lan_1"].notna() & df["lan_2"].notna()
tb1 = df.loc[chung, "lan_1"].mean()
tb2 = df.loc[chung, "lan_2"].mean()
```

Nhóm chung a,b,c có trung bình60 rồi70, tăng 10.

c) Cách a dùng hai tập hàng khác nhau: d giá 180 có ở lần1 nhưng thiếu ở lần2. Cách b giữ cùng tập a,b,c. Cả ba chỗ ở trong nhóm chung đều tăng 10 USD/đêm. Không suy ra giá lần2 của d, không tự coi bằng 0 hay giữ180.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: hai trung bình 90 và 70 (1); mức giảm 20 (0,5) | 1,5 |
| b: mask chung (1); trung bình 60 và 70 (1) | 2 |
| c: khác thành phần (0,5); nhóm chung tăng 10 (0,5); không suy giá d (0,5) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 3; mục tiêu chính K17; phụ K15; mức phân loại.
**Sai lầm kiểm tra:** So hai trung bình khác tập hàng như cùng nhóm.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-019

a) In 380.0 760.0. bao_gia[m] là bảng trung gian; gán cột trên đó không ghi vào bao_gia trong pandas3. Phát cảnh báo ChainedAssignmentError, code vẫn tiếp tục theo giả định.

b)

```python
bao_gia.loc[m, "gia"] = bao_gia.loc[m, "gia"] * 0.8
```

c) Sau riêng b:330.0 760.0. Cột hai_dem còn kết quả cũ. Thêm sau khi sửa giá:

```python
bao_gia["hai_dem"] = bao_gia["gia"] * 2
```

Giá cuối:[120.,50.,80.,80.]; tiền hai đêm:[240.,100.,160.,160.]; hai tổng 330 và660. PR ở D2,D4 giữ giá 50,80. Nguồn giữ giá[150.,50.,100.,80.] và hai cột loai,gia.

```python
assert bao_gia["gia"].tolist() == [120., 50., 80., 80.]
assert bao_gia["hai_dem"].tolist() == [240., 100., 160., 160.]
assert nguon["gia"].tolist() == [150., 50., 100., 80.]
assert nguon.columns.tolist() == ["loai", "gia"]
```

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: tổng 380/760 (0,5); bảng trung gian và cảnh báo (1) | 1,5 |
| b: gán loc đúng bảng, mask, cột và hệ số | 1,5 |
| c: tổng sau riêng b 330/760 (0,5); tính lại (0,5); kiểm đầy đủ hàng PR và nguồn (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 5; mục tiêu chính K34; phụ K35, K36; mức phân loại.
**Sai lầm kiểm tra:** Sửa bảng trung gian, quên tổng phụ thuộc và bỏ kiểm nguồn.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-020

```python
m = df["loai"].isin(["Studio", "Phòng riêng"])
r = df.loc[m, ["gia", "id"]].sort_values("gia")
```

| Nhãn | gia | id |
|---:|---:|---|
| 4 | 50.0 | B2 |
| 15 | 65.0 | E1 |
| 7 | 75.0 | D4 |
| 12 | 95.0 | A7 |

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: isin đúng hai loại (1); hai cột đúng thứ tự (1); sort_values tăng dần (1) | 3 |
| b: đúng bốn hàng/cặp giá-id (1); đúng thứ tự và giữ index [4,15,7,12] (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 4; mục tiêu chính K26; phụ K21; mức vận dụng.
**Sai lầm kiểm tra:** Sai thứ tự cột/hàng hoặc giữ loại phòng rẻ nhưng ngoài yêu cầu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### Cập nhật sau đợt 2

Lũy kế 20/60 câu: 14 trắc nghiệm, 6 tự luận.

| Nhóm chính | Đã xuất / kế hoạch |
|---|---:|
| 1 | 3 / 6 |
| 2 | 2 / 6 |
| 3 | 4 / 10 |
| 4 | 4 / 12 |
| 5 | 4 / 14 |
| 6 | 2 / 8 |
| 7 | 1 / 4 |

Mục tiêu đã có ít nhất một câu yêu cầu sử dụng (không đồng nghĩa mọi nhánh của mục rộng đã hoàn tất): K01, K02, K03, K04, K05, K07, K08, K10, K11, K12, K13, K14, K15, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K30, K31, K32, K33, K34, K35, K36, K37, K38, K44, K45.
Mục tiêu chưa có câu: K06, K09, K16, K27, K28, K29, K39, K40, K41, K42, K43, K46, K47, K48, K49, K50.


## Đợt 3 — Đáp án và chấm bài

### B4-021 — D

**D đúng.** dtypes là Series, nhãn của nó là tên các cột. Pandas 3 suy luận cột chuỗi này là str; giá là float64. index và columns đều là đối tượng Index.

- A sai: dtypes không phải DataFrame.
- B sai: nhãn của Series dtype là tên cột, không phải nhãn hàng của df.
- C sai: dùng kết quả suy luận chuỗi kiểu cũ thay cho giả định pandas 3. Dtype của từng cột cũng không phải dtype chung của cả bảng.

**Nhãn:** nhóm chính 1; mục tiêu chính K04; phụ K02; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm nhãn của Series dtypes và áp dụng suy luận dtype chuỗi của phiên bản cũ.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-022 — C

**C đúng.** head(2) lấy A,B theo vị trí đầu. Seed giúp lặp lại mẫu trong điều kiện đã nêu, không chứng minh tính đại diện hay bảo đảm thống kê mẫu khớp toàn bảng.

- A sai: head không lấy ngẫu nhiên; sample không tối ưu giá.
- B sai: khả năng lặp lại khác với tính đại diện.
- D sai: seed không ép trung bình mẫu bằng trung bình toàn bảng.

**Nhãn:** nhóm chính 2; mục tiêu chính K09; phụ K12; mức nền tảng.
**Sai lầm kiểm tra:** Tưởng xem vài hàng đầu hoặc cố định seed là bảo đảm đại diện.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-023 — A

**A đúng.** Bốn giá biết có tổng 400, mean 100, median (20+30)/2=25, min 10, max 340; thứ tự kết quả theo danh sách hàm.

- B sai: là thống kê nếu tự thay NaN bằng 0, trái với code.
- C sai: chọn phần tử giữa phía trên thay vì trung bình hai phần tử giữa.
- D sai: sum mặc định bỏ qua NaN trong ví dụ có giá đã biết này.

**Nhãn:** nhóm chính 3; mục tiêu chính K15; phụ K16; mức vận dụng.
**Sai lầm kiểm tra:** Tự coi thiếu là 0, tính median chẵn sai hoặc cho rằng NaN làm sum thành NaN.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-024 — C

**C đúng.** Hai danh sách quyết định thứ tự hàng r,p và cột phi,gia. k là DataFrame (2,2); ô vị trí [0,1] là giá của r, bằng 80.

- A sai: tự đưa hàng về thứ tự gốc.
- B sai: tự đưa cột về thứ tự gốc rồi lấy phí thay vì giá.
- D sai: chọn nhiều hàng và danh sách cột tạo DataFrame, không phải Series.

**Nhãn:** nhóm chính 4; mục tiêu chính K21; phụ K03, K20; mức vận dụng.
**Sai lầm kiểm tra:** Tưởng thứ tự gốc ghi đè thứ tự trong danh sách loc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-025 — D

**D đúng.** Gán tên cột mới thêm cột thứ ba. Tổng là 25*2+5=55; NaN*2+10 vẫn NaN; 40*2=80.

- A sai: quên đếm cột mới.
- B sai: coi giá thiếu là 0.
- C sai: nhân cả phí với 2, khác biểu thức đã cho.

**Nhãn:** nhóm chính 5; mục tiêu chính K29; phụ K05; mức nền tảng.
**Sai lầm kiểm tra:** Quên cột mới trong shape, coi NaN là 0 hoặc đổi ngoặc phép tính.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-026 — C

**C đúng.** Hai đêm: 200, 140+80=220, 100+200=300. Tám đêm: 800, 560+80=640, 400+200=600. A rẻ nhất cho hai đêm; C rẻ nhất cho tám đêm.

- A sai: nhân cả phí một lần với số đêm.
- B sai: bỏ phí trong cả hai trường hợp.
- D sai: chỉ bỏ phí ở trường hợp tám đêm.

**Nhãn:** nhóm chính 5; mục tiêu chính K28; mức vận dụng.
**Sai lầm kiểm tra:** Nhân phí một lần với số đêm hoặc bỏ phí khi so lựa chọn.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-027 — B

**B đúng.** Hai bảng cùng shape (3,2), cùng tổng 70 nhưng A đổi từ 10 sang 40, C từ 40 sang 10. Hai phép kiểm không kiểm quan hệ mã–giá.

- A sai: shape/tổng là điều kiện chưa đủ để chứng minh đúng từng cặp.
- C sai: hoán đổi không thay tổng.
- D sai: hoán đổi không thay số hàng/cột.

**Nhãn:** nhóm chính 6; mục tiêu chính K41; phụ K40; mức vận dụng.
**Sai lầm kiểm tra:** Dùng shape và tổng như bằng chứng đủ về đúng quan hệ mã–giá.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-028

a,b)

```python
top = df.nlargest(1, "gia")[["id", "gia"]]
truoc_mean = df["gia"].mean()
truoc_median = df["gia"].median()
sau = df.drop(top.index)
sau_mean = sau["gia"].mean()
sau_median = sau["gia"].median()
```

top chứa nhãn 27, id X5, giá 860. Ban đầu: mean=200, median=40. Sau khi tạm bỏ hàng này: mean=35, median=35. df vẫn đủ năm hàng.

c) Giá 860 kéo mean lên mạnh; median phụ thuộc thứ hạng và các giá ở giữa nên thay đổi ít hơn ở ví dụ này. Hai đại lượng trả lời câu hỏi khác nhau. Cực lớn hoặc cực nhỏ chưa tự chứng minh sai: giữ id X5/X1 để tra bản ghi, kiểm đơn vị và ngữ cảnh trước khi quyết định sửa/xóa.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: top-k có id (0,5); mean 200 và median 40 (1) | 1,5 |
| b: drop theo top.index và không sửa df (1); hai thống kê 35/35 (0,5) | 1,5 |
| c: so ảnh hưởng mean/median (1); không kết luận sai và nêu tra id/đơn vị/ngữ cảnh (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 3; mục tiêu chính K16; phụ K47, K27; mức phân loại.
**Sai lầm kiểm tra:** Xóa theo vị trí thay vì nhãn; coi giá cực trị tự động là lỗi.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-029

a) In `[60.0,50.0,100.0]`. thu và goc là cùng một đối tượng, không phải hai đối tượng rút ra độc lập; CoW không đổi ý nghĩa phép gán tên.

b)

```python
goc = truoc.copy()
thu = goc.copy()
thu.loc["b", "gia"] = 50.
```

c)

```python
assert goc["gia"].tolist() == [60., 80., 100.]
assert thu["gia"].tolist() == [60., 50., 100.]
```

Copy một bảng đã bị sửa chỉ sao chép giá 50 hiện tại; không khôi phục lịch sử. Ở đây truoc giữ dữ liệu ban đầu nên dùng được để khôi phục.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: output (0,5); cùng đối tượng và vai trò CoW (1) | 1,5 |
| b: khôi phục từ truoc (1); copy riêng rồi sửa thu (1) | 2 |
| c: kiểm cả hai bảng (1); copy không khôi phục lịch sử (0,5) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 5; mục tiêu chính K30; phụ K31, K36; mức phân loại.
**Sai lầm kiểm tra:** Tưởng CoW bảo vệ hai tên của cùng bảng; tưởng copy sau lỗi khôi phục dữ liệu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-030

a) and/or của Python cần giá trị đúng/sai duy nhất cho mỗi vế; Series có nhiều phần tử nên không thể dùng như vậy, phát ValueError.

b)

```python
m = (((df["loai"] == "Studio") & (df["gia"] <= 90))
     | ((df["loai"] == "PR") & (df["gia"] < 60)))
```

c) Giữ S1,S4. S2 giá 60 không thỏa <60. S5 thiếu giá, phép so sánh cho False; không được từ đó kết luận giá của S5 cao hơn ngưỡng.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: cơ chế bool duy nhất và ValueError | 1 |
| b: toán tử và/hoặc theo phần tử đúng (1); đủ ngoặc và đúng từng điều kiện (1) | 2 |
| c: S1,S4 (1); giá 60 (0,5); thiếu không có nghĩa biết chắc vượt ngưỡng (0,5) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 4; mục tiêu chính K24; phụ K25; mức vận dụng.
**Sai lầm kiểm tra:** Dùng and/or cho Series; sai ngoặc/biên và diễn giải giá thiếu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### Cập nhật sau đợt 3

Lũy kế 30/60 câu: 21 trắc nghiệm, 9 tự luận.

| Nhóm chính | Đã xuất / kế hoạch |
|---|---:|
| 1 | 4 / 6 |
| 2 | 3 / 6 |
| 3 | 6 / 10 |
| 4 | 6 / 12 |
| 5 | 7 / 14 |
| 6 | 3 / 8 |
| 7 | 1 / 4 |

Mục tiêu đã có ít nhất một câu yêu cầu sử dụng (không đồng nghĩa mọi nhánh của mục rộng đã hoàn tất): K01, K02, K03, K04, K05, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K40, K41, K44, K45, K47.
Mục tiêu chưa có câu: K06, K39, K42, K43, K46, K48, K49, K50.


## Đợt 4 — Đáp án và chấm bài

### B4-031 — C

**C đúng.** Pandas có thể tính toán trên dtype số, nhưng không tự biết vai trò nghiệp vụ. id là khóa, còn gia là số đo có đơn vị USD/đêm.

- A sai: gán đơn vị giá cho một trung bình mã.
- B sai: mã bình quân không phải mã điển hình hay mức giá đại diện.
- D sai: phép tính số học này vẫn chạy; vấn đề là ý nghĩa, không phải lỗi dtype.

**Nhãn:** nhóm chính 1; mục tiêu chính K06; phụ K08; mức vận dụng.
**Sai lầm kiểm tra:** Coi dtype số là đủ để thống kê mã định danh có ý nghĩa.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-032 — C

**C đúng.** describe đếm bốn giá đã biết. Các phân vị trước làm tròn là 17,7;25,2;32,7. round(0) làm tròn Series thống kê trả về, không sửa s.

- A sai: count không đếm NaN.
- B sai: tưởng round trên thống kê sửa giá gốc.
- D sai: coi tên các mức phân vị như chính giá trị thống kê. Làm tròn để báo cáo không tăng độ chính xác dữ liệu nguồn.

**Nhãn:** nhóm chính 2; mục tiêu chính K11; phụ K48; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm count với len, mức phân vị với giá trị và làm tròn thống kê với sửa dữ liệu gốc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-033 — B

**B đúng.** p=3/6=0,5; q=3/4=0,75; (q-p)*100=25 điểm phần trăm.

- A sai: tỷ lệ 0,5 tương ứng 50%, không phải 0,5%.
- C sai: mức tăng tương đối là (0,75−0,5)/0,5=50%; 25 là điểm phần trăm.
- D sai: đảo mẫu số và kết quả hai phép tính.

**Nhãn:** nhóm chính 3; mục tiêu chính K19; phụ K18; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm tỷ lệ/phần trăm/điểm phần trăm và mức tăng tương đối.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-034 — A

**A đúng.** Hai giá lớn nhất là 150(T2),120(T4), theo thứ tự giảm dần; danh sách chọn cột giữ gia trước id. Giữ id giúp tra nguồn.

- B sai: lấy hai giá nhỏ nhất.
- C sai: đảo thứ tự hai hàng đã chọn.
- D sai: bỏ qua thứ tự cột được yêu cầu.

**Nhãn:** nhóm chính 4; mục tiêu chính K27; phụ K21; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm nlargest/nsmallest hoặc tự đổi thứ tự cột/hàng.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-035 — A

**A đúng.** b độc lập với df, còn a là tên khác của b. Sửa a làm b đổi nhưng không làm df đổi.

- B sai: bỏ qua copy.
- C sai: tưởng a=b cũng tạo bản sao riêng.
- D sai: đảo bảng bị sửa và bảng giữ nguyên.

**Nhãn:** nhóm chính 5; mục tiêu chính K31; phụ K30; mức nền tảng.
**Sai lầm kiểm tra:** Không theo dõi bảng mà tên mới thực sự chỉ tới.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-036 — D

**D đúng.** tong lưu giá trị cũ (50+20)*3=210. Tổng đúng theo giá mới là 40*3+20=140. Code có cả lỗi nhân phí một lần và chưa tính lại cột.

- A sai: giả định công thức đã được sửa và tự cập nhật.
- B sai: giả định tự tính lại biểu thức sai (40+20)*3.
- C sai: giả định tổng cũ đã dùng đúng phí một lần: 50*3+20.

**Nhãn:** nhóm chính 5; mục tiêu chính K28; phụ K35; mức vận dụng.
**Sai lầm kiểm tra:** Nhân phí một lần với số đêm và tưởng cột tổng tự tính lại.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-037 — D

**D đúng.** Mặc định index=True; index_label đặt tiêu đề ma cho cột chứa A,B,C.

- A sai: index=False vẫn loại index; index_label không đưa mã trở lại.
- B sai: giữ mã nhưng đặt tên id, không đúng yêu cầu tên ma.
- C sai: ma chưa là cột dữ liệu để chọn bằng columns; phát KeyError. Giữ index hay chuyển nó thành cột đều là cách hợp lệ nếu đáp ứng đúng yêu cầu, nhưng chỉ D trong các lựa chọn này đúng.

**Nhãn:** nhóm chính 6; mục tiêu chính K39; phụ K38, K37; mức nền tảng.
**Sai lầm kiểm tra:** Tưởng index_label có thể cứu index=False hoặc chọn tên index như tên cột dữ liệu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-038

a) sum bỏ NaN nên tử số 60, len=5; in 12.0. Tử số chỉ dùng giá biết nhưng mẫu số đếm cả hai hàng chưa biết.

b)

```python
tb = s.mean()
```

Hoặc `s.sum()/s.count()`. Dùng ba giá 0,20,40; kết quả 20.0.

c) Thay thiếu bằng 0 tạo hai giá miễn phí không được nguồn xác nhận, vẫn ra 12 và làm thấp trung bình các giá đã biết. Giá 0 ban đầu là quan sát hợp lệ, phải tham gia cả tử số và mẫu số.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: output 12 (0,5); tử số/mẫu số khác tập (1) | 1,5 |
| b: một dòng đúng (1); ba giá và kết quả20 (0,5) | 1,5 |
| c: không tự điền0 và hệ quả (1); giữ giá 0 hợp lệ (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 3; mục tiêu chính K13; phụ K14, K15; mức phân loại.
**Sai lầm kiểm tra:** Sai mẫu số trong code chạy được; chữa kỹ thuật bằng cách làm sai ý nghĩa thiếu dữ liệu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-039

a) In `[63.0,330.0]`. Phí bị nhân số đêm; tong còn tính từ giá B cũ 70.

b)

```python
bao = nguon.copy()
bao.loc["B", "gia"] *= 0.9
bao["tong"] = bao["gia"] * 3 + bao["phi"]
assert bao["tong"].tolist() == [270., 229., 270.]
assert nguon["gia"].tolist() == [90., 70., 50.]
assert nguon["phi"].tolist() == [0., 40., 120.]
```

c) C<A khi 50n+120<90n, tức n>3. C<B khi 50n+120<63n+40, tức 13n>80. Kết hợp, số nguyên đầu tiên là **7**. Sáu đêm: A540,B418,C420, C chưa rẻ hơn B. Bảy đêm: A630,B481,C470, C rẻ hơn cả hai.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: output (0,5); hai lỗi mỗi lỗi0,5 | 1,5 |
| b: copy và thứ tự sửa–tính (0,5); công thức đúng (0,5); tổng ba hàng và nguồn (0,5) | 1,5 |
| c: hai bất đẳng thức (1); mốc 7 (0,5); kiểm6/7 (0,5) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 5; mục tiêu chính K28; phụ K35, K36; mức phân loại.
**Sai lầm kiểm tra:** Sửa giá đúng nhưng vẫn nhân phí một lần hoặc dùng tổng cũ; chỉ kiểm một đối thủ khi tìm ngưỡng.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-040

a) Nhãn còn `[1,3,6]`, giá `[20,40,60]`. loc[1:3] lấy nhãn 1 và 3 nên in 60; đó là hàng thứ nhất và thứ hai của r.

b)

```python
print(r.iloc[1:3, 0].sum())
```

In 100: vị trí1 và2, nhãn 3 và6.

c) loc gồm nhãn cuối3; iloc bỏ vị trí stop3, lấy vị trí1,2. Lọc không tự đánh lại nhãn.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: nhãn/giá sau lọc (0,5); output60 và chọn theo nhãn (1) | 1,5 |
| b: lát iloc đúng (1); tổng 100 và hai hàng đúng (0,5) | 1,5 |
| c: loc gồm cuối (1); iloc bỏ stop và không đánh lại index (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 4; mục tiêu chính K22; phụ K20, K23; mức vận dụng.
**Sai lầm kiểm tra:** Dùng lát nhãn như lát vị trí sau lọc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### Cập nhật sau đợt 4

Lũy kế 40/60 câu: 28 trắc nghiệm, 12 tự luận.

| Nhóm chính | Đã xuất / kế hoạch |
|---|---:|
| 1 | 5 / 6 |
| 2 | 4 / 6 |
| 3 | 8 / 10 |
| 4 | 8 / 12 |
| 5 | 10 / 14 |
| 6 | 4 / 8 |
| 7 | 1 / 4 |

Mục tiêu đã có ít nhất một câu yêu cầu sử dụng (không đồng nghĩa mọi nhánh của mục rộng đã hoàn tất): K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K44, K45, K47, K48.
Mục tiêu chưa có câu: K42, K43, K46, K49, K50.


## Đợt 5 — Đáp án và chấm bài

### B4-041 — B

**B đúng.** B có 4/7 hàng; PR có 3/7 hàng; 7−6=1 giá thiếu; trung vị sáu giá 10,20,40,50,60,70 là45. Mẫu hai hàng không bảo đảm đại diện snapshot; các tỷ trọng còn giới hạn ở bảng đang khảo sát, chưa đại diện toàn bộ thị trường.

- A sai: thay tỷ trọng toàn bảng bằng tỷ trọng trong mẫu nhỏ.
- C sai: quy mô quận đếm mọi chỗ ở, không chỉ hàng có giá.
- D sai: dùng số hàng NC làm số hàng PR.

**Nhãn:** nhóm chính 2; mục tiêu chính K12; phụ K50, K09; mức vận dụng.
**Sai lầm kiểm tra:** Thực thi năm bước mà không đọc đúng output; nhầm mẫu xem, mẫu số quy mô và cơ cấu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-042 — D

**D đúng.** Tổng 1000/4=250; median=(30+40)/2=35. Một giá rất lớn kéo mean lên mạnh; median phản ánh vị trí giữa. Cần kiểm nguồn trước khi kết luận lỗi.

- A sai: đảo mean và median.
- B sai: median của số lượng chẵn có thể là trung bình hai giá giữa.
- C sai: chênh lệch hai thống kê không tự chứng minh lỗi dữ liệu.

**Nhãn:** nhóm chính 3; mục tiêu chính K15; phụ K16; mức nền tảng.
**Sai lầm kiểm tra:** Đổi mean/median hoặc tự gắn nhãn sai cho cực trị.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-043 — A

**A đúng.** Sau lọc còn A95,B40,D60,E50. Hai giá nhỏ nhất là B40,E50.

- B sai: lấy C dù loại Shared bị loại trước top-k.
- C sai: lấy hai giá lớn nhất của tập được phép.
- D sai: lấy hai hàng đầu thay vì hai giá nhỏ nhất.

**Nhãn:** nhóm chính 4; mục tiêu chính K26; phụ K27; mức vận dụng.
**Sai lầm kiểm tra:** Quên lọc loại trước top-k hoặc nhầm head/nlargest/nsmallest.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-044 — B

**B đúng.** Nhãn 0 nằm ở hàng thứ hai, giá 25. Vị trí0 là hàng đầu nhãn 2, giá 15. Hai kết quả là giá trị một ô, không phải DataFrame.

- A sai: dùng cả hai như vị trí.
- C sai: dùng cả hai như nhãn.
- D sai: đảo cơ chế loc và iloc.

**Nhãn:** nhóm chính 4; mục tiêu chính K20; phụ K03; mức nền tảng.
**Sai lầm kiểm tra:** Thấy nhãn nguyên thì coi loc như iloc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-045 — A

**A đúng.** Copy giữ df độc lập. Sửa s khiến Series này tách khỏi b theo CoW; giá 99 chỉ ở s. Gán loc sửa b thành 5 ở hàng 0.

- B sai: bỏ qua copy và làm df đổi theo b.
- C sai: tưởng sửa s ghi trở lại b.
- D sai: tưởng phép gán trực tiếp loc không sửa được b.

**Nhãn:** nhóm chính 5; mục tiêu chính K32; phụ K31; mức vận dụng.
**Sai lầm kiểm tra:** Trộn quan hệ copy, Series rút ra và gán trực tiếp.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-046 — C

**C đúng.** Hai cột id,gia được giữ; một giá thiếu vẫn thiếu. Hai sum đều bỏ qua NaN và bằng 100. Đây là kiểm chứng một số bất biến ghi/đọc, chưa xác nhận giá nguồn đúng thực tế hay tự thay thế kiểm từng cặp mã–giá.

- A sai: suy từ tính nhất quán file thành tính đúng nguồn.
- B sai: code không có bước điền0.
- D sai: với dữ liệu này hai sum đều bằng 100.

**Nhãn:** nhóm chính 6; mục tiêu chính K40; phụ K42; mức vận dụng.
**Sai lầm kiểm tra:** Coi file khớp bất biến là chứng nhận nguồn đúng hoặc tưởng CSV tự điền thiếu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-047

a) True: cả hai shape(3,2), tổng 100, nhưng các giá được ghép với id sai.

b)

```python
a = goc.sort_values("id")
b = lai.sort_values("id")
dung = (a["id"].tolist() == b["id"].tolist()
        and a["gia"].tolist() == b["gia"].tolist())
```

dung=False. So cùng danh sách id đã sắp và giá tương ứng bảo đảm so đúng cặp theo giả định id duy nhất, không thiếu giá. Có thể kiểm từng mã bằng loc hoặc cách tương đương trong phạm vi bài.

c) Khớp goc chỉ chứng minh giữ dữ liệu tham chiếu; cần tra mã trong nguồn, kiểm đơn vị và ngữ cảnh để đánh giá giá có đúng thực tế không.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: True (0,5); cùng tổng/shape vẫn sai cặp (1) | 1,5 |
| b: so đủ id (0,5); giá đúng cặp bất kể thứ tự (1); kết quả False (0,5) | 2 |
| c: phân biệt khớp tham chiếu với đúng thực tế (1); tra mã/đơn vị/ngữ cảnh (0,5) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 6; mục tiêu chính K41; phụ K40, K42; mức phân loại.
**Sai lầm kiểm tra:** Tổng/shape che giấu ghép sai mã–giá; sửa phép kiểm nhưng vẫn suy quá giới hạn nguồn.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-048

a) bao có shape(2,3), nhãn w,y; giá 50,30 nhưng hai vẫn200,120. Code làm mất hai hàng PR và giữ cột dẫn xuất cũ.

b)

```python
bao = nguon.copy()
m = bao["loai"] == "NC"
bao.loc[m, "gia"] *= 0.5
bao["hai"] = bao["gia"] * 2
```

c)

```python
assert bao.shape == (4, 3)
assert bao["gia"].tolist() == [50., 80., 30., 40.]
assert bao["hai"].tolist() == [100., 160., 60., 80.]
assert nguon["gia"].tolist() == [100., 80., 60., 40.]
assert nguon.columns.tolist() == ["loai", "gia"]
```

PR x,z giữ80,40. Giảm đúng một tập con không bù được việc làm mất các hàng cần giữ.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: shape và hai dãy (1); phát hiện thiếu hàng PR và tổng cũ (0,5) | 1,5 |
| b: giữ đủ hàng/copy (0,5); loc giảm đúng (0,5); tính lại sau giảm (0,5) | 1,5 |
| c: kiểm giá PR và shape (1); tổng và nguồn (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 5; mục tiêu chính K33; phụ K35, K36; mức phân loại.
**Sai lầm kiểm tra:** Sửa được giá mục tiêu nhưng đánh mất hàng khác và quên tổng phụ thuộc.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-049

a)

```python
dem = s.value_counts()
co_cau = s.value_counts(normalize=True)
```

Số đếm: NC2, PR1, Shared1. Tỷ lệ tương ứng0,5;0,25;0,25. Giá trị thiếu bị bỏ mặc định.

b) Mẫu số 4, không phải6. Chia cho6 cho cơ cấu trên toàn bộ hàng, khác quy ước mặc định normalize và có tổng các tỷ lệ nhãn biết bằng 4/6.

c)

```python
so_thieu = s.isna().sum()
ty_le_thieu = s.isna().mean()
```

Hai nhãn thiếu, tỷ lệ2/6=1/3≈33,33%.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: lệnh đúng (1); số đếm và tỷ lệ đúng (1) | 2 |
| b: mẫu số 4 (0,5); giải thích vì sao chia6 khác (1) | 1,5 |
| c: isna().sum đúng (0,5); số thiếu 2 và tỷ lệ1/3 (1) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 7; mục tiêu chính K43; phụ K14; mức vận dụng.
**Sai lầm kiểm tra:** Dùng toàn bộ hàng làm mẫu số normalize mặc định hoặc lẫn mẫu số cơ cấu và thiếu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-050

a) Lưu danh sách hai nhãn Đông,Tây và một mã tham chiếu cho mỗi trong sáu hàng; không biến khu thành số đo để tính trung bình mã.

b) Lần đo này khu giảm dung lượng, id tăng dung lượng. deep=True giúp ước tính cả nội dung chuỗi/đối tượng mà thống kê nông có thể không tính đầy đủ; các số đã gồm cùng index mặc định. Không suy con số byte thành hằng số cho máy/phiên bản khác.

c) khu là nhãn phân loại lặp nên phù hợp hơn. id có sáu giá trị riêng, việc thêm danh sách nhãn và mã có thể gây overhead. Mức tiết kiệm phụ thuộc số hàng, số nhãn khác nhau và cách lưu; đo trên dữ liệu/môi trường thực tế thay vì khẳng định luôn giảm.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: hai nhãn riêng (0,5); sáu mã tham chiếu (1) | 1,5 |
| b: khu giảm/id tăng (0,5); giải thích deep và tính phụ thuộc môi trường (1) | 1,5 |
| c: chọn khu với lý do nhãn lặp (1); bác bỏ khẳng định luôn giảm bằng overhead/độ đa dạng (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 7; mục tiêu chính K45; phụ K46; mức vận dụng.
**Sai lầm kiểm tra:** Coi category là số đo, hoặc khẳng định mọi cột đều tiết kiệm bộ nhớ.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### Cập nhật sau đợt 5

Lũy kế 50/60 câu: 34 trắc nghiệm, 16 tự luận.

| Nhóm chính | Đã xuất / kế hoạch |
|---|---:|
| 1 | 5 / 6 |
| 2 | 5 / 6 |
| 3 | 9 / 10 |
| 4 | 10 / 12 |
| 5 | 12 / 14 |
| 6 | 6 / 8 |
| 7 | 3 / 4 |

Mục tiêu đã có ít nhất một câu yêu cầu sử dụng (không đồng nghĩa mọi nhánh của mục rộng đã hoàn tất): K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K50.
Mục tiêu chưa có câu: K49.


## Đợt 6 — Đáp án và chấm bài

### B4-051 — B

**B đúng.** Mỗi khóa dict tạo một cột; index=nhan đặt nhãn hàng và không tạo cột thứ ba. id giữ vai trò khóa.

- A sai: không truyền index thì nhãn mặc định0,1,2.
- C sai: ma_hang được tạo thành cột thứ ba, không thành index; shape(3,3).
- D sai: cách tạo đúng nhưng diễn giải mean(id) thành giá là sai; giá trung bình ở đây là60.

**Nhãn:** nhóm chính 1; mục tiêu chính K01; phụ K06, K02; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm nhãn với cột được tạo từ dict; coi trung bình mã là giá.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-052 — B

**B đúng.** <50 là T,F,F,F; >=50 là F,T,T,F. Cả hai mask là bool không thiếu, mẫu số đều4. Tổng tỷ lệ0,75 vì hàng chưa biết không thuộc nhóm so sánh nào.

- A sai: False của <50 có cả NaN, không đồng nghĩa biết >=50.
- C sai: so sánh diễn ra trước mean, chuyển ô NaN thành False chứ không bỏ hàng.
- D sai: <50 không bao gồm giá 50.

**Nhãn:** nhóm chính 3; mục tiêu chính K18; phụ K25; mức vận dụng.
**Sai lầm kiểm tra:** Dùng phần bù mask như kết luận đã biết giá hoặc tự loại NaN khỏi mẫu số.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-053 — D

**D đúng.** Một nhãn hàng đơn cho Series chứa hai phần tử phi,gia. Danh sách một nhãn giữ hàng dưới dạng DataFrame một hàng, hai cột.

- A sai: nhãn hàng đơn không giữ kết quả dưới dạng bảng ở cách chọn này.
- B sai: Series có hai giá trị, không phải một.
- C sai: đảo số hàng và số cột của b.

**Nhãn:** nhóm chính 4; mục tiêu chính K21; phụ K03; mức nền tảng.
**Sai lầm kiểm tra:** Nhầm một nhãn hàng với danh sách một nhãn và đếm shape theo số hàng nguồn.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-054 — D

**D đúng.** Gán nối tiếp vào b phát cảnh báo và không sửa bảng. a=df nên gán loc ở hàng a sửa df thành 8. Cột hai giữ giá trị cũ.

- A sai: cho rằng chained assignment có tác dụng và cột dẫn xuất tự cập nhật.
- B sai: cho rằng chained assignment có tác dụng.
- C sai: cho rằng a là bản sao, hoặc cảnh báo chặn cả lệnh loc sau đó.

**Nhãn:** nhóm chính 5; mục tiêu chính K34; phụ K30, K35; mức vận dụng.
**Sai lầm kiểm tra:** Tưởng alias cứu chained assignment hoặc suy rằng mọi bước sau cảnh báo đều thất bại.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-055 — C

**C đúng.** reset_index chuyển index tên id thành cột id. index=False chỉ bỏ index mới, không bỏ cột id vừa tạo. NaN vẫn thiếu; sum15+45=60.

- A sai: tưởng index=False xóa cả cột id sau reset_index.
- B sai: tưởng index mới vẫn được ghi dù index=False.
- D sai: tưởng CSV tự thay thiếu bằng 0. Mã đọc lại theo thứ tự S3,S1,S2.

**Nhãn:** nhóm chính 6; mục tiêu chính K40; phụ K39; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm index trước/sau reset_index và tưởng bỏ index làm mất cột id đã chuyển.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-056 — A

**A đúng.** Có năm nhãn không thiếu; A xuất hiện2 nên tỷ lệ2/5=0,4. Có ba nhãn khác nhau A,B,C; count=5.

- B sai: dùng len=6 cho cả normalize và count.
- C sai: tính thiếu như một nhãn trong nunique mặc định.
- D sai: bỏ qua normalize=True và trả số đếm.

**Nhãn:** nhóm chính 7; mục tiêu chính K43; phụ K44; mức vận dụng.
**Sai lầm kiểm tra:** Nhầm số đếm, tỷ lệ, số nhãn khác nhau và số giá trị không thiếu.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-057

a,b)

```python
q = df.loc[df["quan"] == TEN_QUAN]
so_cho = len(q)
ty_trong = so_cho / len(df)
tv_quan = q["gia"].median()
tv_tp = df["gia"].median()
chenh_pct = (tv_quan / tv_tp - 1) * 100
```

B có 3 chỗ ở, tỷ trọng3/6=50%. Trung vị B=(50+70)/2=60 USD/đêm; toàn bảng có năm giá biết20,40,50,70,100, median 50. B cao hơn(60−50)/50=20% (cho phép sai số hiển thị số thực).

c) Tỷ trọng quy mô dùng cả6 hàng, gồm hàng thiếu giá; trung vị B chỉ dùng2 giá đã biết. Mỗi hàng là chỗ ở, không phải lượt đặt. Các tỷ lệ mô tả snapshot đang có; chưa đủ để suy rộng toàn thị trường thực tế.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: lọc từ TEN_QUAN và tái sử dụng (0,5); quy mô/tỷ trọng đúng (0,5); hai trung vị đúng (1) | 2 |
| b: số 3 và50% (0,5); median 60/50 (0,5); chênh20% với mẫu số 50 (0,5) | 1,5 |
| c: phân biệt6 hàng và2 giá (0,5); không nhầm lượt đặt (0,5); giới hạn snapshot (0,5) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 2; mục tiêu chính K49; phụ K50, K08; mức vận dụng.
**Sai lầm kiểm tra:** Hard-code quận ở nhiều nơi; dùng số giá biết làm mẫu số quy mô; diễn giải sai đơn vị quan sát.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-058

a)

```python
m = df["loai"].isin(["NC", "PR"])
r = df.loc[m, ["id", "gia"]].nsmallest(3, "gia")
```

b) Nhãn 5,id U6,giá 20; nhãn 1,id U2,giá 40; nhãn 4,id U5,giá 60. Hai giá 5 và10 bị loại vì Shared.

c) id giúp tra đúng bản ghi nguồn và giữ quan hệ mã–giá sau lọc/sắp xếp. Giá 20 thấp chưa tự chứng minh sai; kiểm đơn vị và ngữ cảnh bản ghi U6 trước khi sửa/xóa.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: isin đúng (0,5); nsmallest3 sau lọc (1); cột/thứ tự đúng (0,5) | 2 |
| b: ba cặp id–giá (1); nhãn và thứ tự5,1,4 (0,5) | 1,5 |
| c: vai trò mã tra nguồn (0,5); không tự kết luận sai và nêu đối chiếu (1) | 1,5 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 4; mục tiêu chính K27; phụ K26, K21; mức vận dụng.
**Sai lầm kiểm tra:** Lấy top-k toàn bảng trước khi lọc loại hoặc bỏ mã cần truy nguồn.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-059

a) In 540.0 360.0. tam là một bảng riêng; sửa và tính cột trong tam không thay đổi bảng đích bao.

b)

```python
m = bao["loai"] == "A"
bao.loc[m, "gia"] *= 0.5
bao["ba_dem"] = bao["gia"] * 3
```

c) Sau riêng bước giảm giá, ba_dem vẫn có tổng 540; phải tính lại mới bằng 360. Giá cuối20,60,40; ba_dem60,180,120. Có thể kiểm:

```python
assert bao["gia"].tolist() == [20., 60., 40.]
assert bao["ba_dem"].tolist() == [60., 180., 120.]
assert goc["gia"].tolist() == [40., 60., 80.]
assert goc.columns.tolist() == ["loai", "gia"]
```

Hàng B q giữ giá 60 và tiền ba đêm180. Chỉ xem tam không kiểm chứng được yêu cầu trên bao.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: hai tổng (0,5); phân biệt tam/bao (1) | 1,5 |
| b: giảm đúng đối tượng/hàng (1); tính lại đúng thứ tự (0,5) | 1,5 |
| c: tổng còn540 nếu chưa tính lại (0,5); giá/tổng cuối (0,5); B và goc giữ nguyên (1) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 5; mục tiêu chính K32; phụ K35, K36; mức phân loại.
**Sai lầm kiểm tra:** Kiểm nhầm bảng trung gian dù code trên bảng đó đúng; không tính lại cột trên bảng đích.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### B4-060

a) File chỉ còn gia theo thứ tự15,30,45. Mã chỉ nằm trong index đã bị bỏ; thứ tự sau sort khác thứ tự ban đầu và tự nó không chứa quan hệ mã–giá. Không thể khôi phục đáng tin cậy chỉ từ file này.

b) Một cách:

```python
gui.to_csv("bang_060.csv", index_label="ma")
lai = pd.read_csv("bang_060.csv")
```

Hoặc `gui.reset_index().to_csv("bang_060.csv",index=False)` vì index đã tên ma. Cả hai giữ mã thành cột của file.

c) Các cặp theo thứ tự: R7–15;R9–30;R2–45.

```python
assert lai.shape == (3, 2)
assert lai.columns.tolist() == ["ma", "gia"]
assert lai["gia"].isna().sum() == 0
assert lai["gia"].sum() == 90.
assert lai["ma"].tolist() == ["R7", "R9", "R2"]
assert lai["gia"].tolist() == [15., 30., 45.]
```

Các kiểm tra chứng minh file giữ dữ liệu tham chiếu trong tình huống này, không chứng nhận giá nguồn đúng thực tế; vẫn cần đối chiếu bản ghi/đơn vị/ngữ cảnh nếu có nghi vấn.

**Hướng dẫn chấm — 5 điểm**

| Tiêu chí | Điểm |
|---|---:|
| a: nhận ra mất mã (0,5); thứ tự không mã hóa quan hệ nguồn (1) | 1,5 |
| b: xuất có mã đúng tên (1); đọc lại (0,5) | 1,5 |
| c: cặp mã–giá (0,5); đủ kiểm shape/cột/thiếu/tổng/cặp (1); giới hạn nguồn (0,5) | 2 |

Chấp nhận cách giải tương đương đúng theo yêu cầu đề; không yêu cầu câu chữ giống lời giải mẫu.

**Nhãn:** nhóm chính 6; mục tiêu chính K39; phụ K41, K42; mức phân loại.
**Sai lầm kiểm tra:** Mất mã khi bỏ index; tưởng thứ tự hoặc tổng khớp cứu được quan hệ mã–giá và xác nhận nguồn.
**Kiểm chứng:** đã thực thi code câu hỏi và/hoặc thao tác tương ứng, cùng code sửa trong lời giải, trên pandas 3.0.1. Các câu giải thích kết hợp kiểm bằng suy luận về ý nghĩa dữ liệu.

### Cập nhật sau đợt 6

Lũy kế 60/60 câu: 40 trắc nghiệm, 20 tự luận.

| Nhóm chính | Đã xuất / kế hoạch |
|---|---:|
| 1 | 6 / 6 |
| 2 | 6 / 6 |
| 3 | 10 / 10 |
| 4 | 12 / 12 |
| 5 | 14 / 14 |
| 6 | 8 / 8 |
| 7 | 4 / 4 |

Mục tiêu đã có ít nhất một câu yêu cầu sử dụng (không đồng nghĩa mọi nhánh của mục rộng đã hoàn tất): K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50.
Mục tiêu chưa có câu: không còn.

## Đối chiếu cuối cùng

Đủ 60 mã liên tục B4-001–B4-060; 40 trắc nghiệm, 20 tự luận. Đáp án A/B/C/D mỗi chữ đúng10 lần. Đủ15 nền tảng,33 vận dụng,12 phân loại. Mỗi câu thuộc đúng một nhóm chính; nhiều nhất hai mục tiêu phụ.

| Nhóm | Nền tảng | Vận dụng | Phân loại | TN | TL | Tổng |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 2 | 0 | 6 | 0 | 6 |
| 2 | 2 | 4 | 0 | 5 | 1 | 6 |
| 3 | 2 | 4 | 4 | 6 | 4 | 10 |
| 4 | 2 | 10 | 0 | 7 | 5 | 12 |
| 5 | 2 | 6 | 6 | 8 | 6 | 14 |
| 6 | 2 | 4 | 2 | 6 | 2 | 8 |
| 7 | 1 | 3 | 0 | 2 | 2 | 4 |
| **Tổng** | **15** | **33** | **12** | **40** | **20** | **60** |

### Hoàn tất những nhánh từng được ghi là mới kiểm tra một phần

| Mục | Bằng chứng câu hỏi thực sự yêu cầu |
|---|---|
| K04 | 011 dtype số;021 dtypes là Series, nhãn tên cột, dtype str/float64 |
| K11 | 012 non-null/count/mean/median;032 đọc25%,50%,75% và làm tròn |
| K12 | 041 nêu đủ năm bước, yêu cầu đọc quy mô, mẫu, non-null, describe, value_counts;022 giới hạn mẫu |
| K15 | 018 mean trên nhóm chung;023 mean,median,min,max,sum,agg;042 diễn giải mean/median |
| K21 | 020 thứ tự cột;024 danh sách thứ tự hàng/cột;053 một hàng Series/DataFrame |
| K24 | 014 ghép toán tử theo phần tử tại biên;030 giải thích và sửa and/or cùng ngoặc |
| K37 | 016 ghi index mặc định;037 chọn index_label đúng |
| K38 | 007 bỏ mã chỉ ở index dù có tên;016 giữ id là cột;055 chuyển index thành cột |
| K45 | 017 nhận diện nhãn lặp;050 giải thích hai nhãn và sáu mã tham chiếu |

### Danh mục K01–K50: nguồn và câu kiểm tra

G: ghi chú Markdown; L: lecture; T: lab. B1/B5… là bước trong lab; TH là tự học. Mục đầu trong nhãn câu là mục tiêu chính. Các câu liệt kê là câu hỏi đòi hỏi dùng kiến thức, không chỉ lời giải nhắc lại.

| Mã | Mục tiêu | Nguồn G | Nguồn L | Nguồn T | Câu kiểm tra |
|---|---|---|---|---|---|
| K01 | Tạo DataFrame từ dict; DataFrame hai chiều | §1 | §1 tạo bảng | W1 | B4-001, B4-051 |
| K02 | index, columns là nhãn; shape không đếm index vào cột | §1 | §1 nhãn/kích thước | B1 | B4-001, B4-021, B4-051 |
| K03 | Series một chiều, tên; chọn một tên/danh sách đổi kiểu và shape | §1, §3 | §1, §3 | W1, W3 | B4-002, B4-010, B4-011, B4-024, B4-044, B4-053 |
| K04 | dtypes từng cột; df.dtypes là Series; dtype str của pandas 3 | §1 | §1 dtype | B1 info | B4-011, B4-021 |
| K05 | Phép toán Series giữ nhãn, lan NaN, không sửa đầu vào | §1 | §1 tính Series | B5 tính cột | B4-002, B4-025 |
| K06 | Dtype số khác ý nghĩa nghiệp vụ của mã định danh | §1–2 | §2 vai trò cột | B1, B5 giữ id | B4-031, B4-051 |
| K07 | read_csv tạo DataFrame; mỗi hàng là một chỗ ở | §2 | §2 đọc bảng | Khởi động | B4-003 |
| K08 | Khóa, số đo, nhãn phân loại; đơn vị và ngữ cảnh giá | §2 | §2 vai trò cột | B1, B4, B6 | B4-003, B4-031, B4-057 |
| K09 | head chỉ đầu bảng; sample có seed để lặp lại, không bảo đảm đại diện | §2 head | §2 head | B1 sample | B4-022, B4-041 |
| K10 | info: số non-null và suy ra số thiếu | — | Tự học kiểm bảng | B1 | B4-012 |
| K11 | Đọc describe: count, mean, min/max và các mốc phân vị | — | Tự học kiểm bảng | B1 | B4-012, B4-032 |
| K12 | Thói quen shape/sample/info/describe/value_counts; đọc số liệu để kiểm | §2, §5 | §2, tự học, kiểm chứng | B1 | B4-012, B4-022, B4-041 |
| K13 | NaN khác 0; không tự thay giá thiếu bằng 0 | §1–2 | §1, bài tập 2 | B6 | B4-008, B4-013, B4-038 |
| K14 | isna/notna, isna().sum(), count/len; không dùng == np.nan | §2, §5 | §2, §5 | B1, B6–7 | B4-004, B4-013, B4-038, B4-049 |
| K15 | mean/median/min/max/sum; agg đơn giản trên một Series | §2, §5 | §2 | B1, B4, B6 | B4-018, B4-023, B4-038, B4-042 |
| K16 | Giá lớn ảnh hưởng mean; median trả lời câu khác; cực trị cần tra nguồn | §2, §5 | §2, §5 | B4 | B4-023, B4-028, B4-042 |
| K17 | Hai lần thu thập có tập giá biết khác nhau; so lại nhóm chung | §2 bài tập 2 | Bài tập 2 | — | B4-018 |
| K18 | mean bool là tỷ lệ True; mẫu số toàn hàng/có giá; thiếu không đồng nghĩa không đạt | §3, §5 | §3, §5 | W2, B6 | B4-004, B4-008, B4-033, B4-052 |
| K19 | Tỷ lệ, phần trăm và điểm phần trăm | §5 | §5 | B6–7 | B4-008, B4-033 |
| K20 | loc theo nhãn kể cả nhãn số nguyên; iloc theo vị trí; chọn một ô | §3 | §3 | W3, B5 | B4-005, B4-010, B4-024, B4-040, B4-044 |
| K21 | Chọn nhiều hàng/cột theo đúng thứ tự danh sách; một hàng/cột thành Series hay bảng | §3 | §3 | W1, W3 | B4-020, B4-024, B4-034, B4-053, B4-058 |
| K22 | Lát loc lấy nhãn cuối; iloc bỏ stop | §3 tự học | §3 tự học | — | B4-005, B4-040 |
| K23 | df[mask] giữ hàng và mọi cột; sau lọc không đánh lại index | §3 | §3 | W3, B2–3 | B4-005, B4-010, B4-040 |
| K24 | Ghép &, \| và ngoặc; and/or đòi một giá trị bool | §3 | §3 | B3 | B4-014, B4-030 |
| K25 | < khác <= tại biên; so sánh số float64/np.nan cho False | §3 | §3 | B3, B6 | B4-004, B4-014, B4-030, B4-052 |
| K26 | isin nhiều loại; sort_values theo giá | — | Tự học chọn nhiều loại | — | B4-020, B4-043, B4-058 |
| K27 | nlargest/nsmallest; giữ mã để đối chiếu nguồn; tránh đồng hạng mơ hồ | §5 | §5 | B4 | B4-028, B4-034, B4-043, B4-058 |
| K28 | Tổng n đêm: giá*n + phí một lần; so lựa chọn theo n | §1 bài tập 1 | Bài tập 1 | — | B4-026, B4-036, B4-039 |
| K29 | Thêm cột tính bằng Series; shape và thiếu sau khi thêm | §4 | §4 | B5 | B4-025 |
| K30 | other=df là hai tên cùng chỉ một bảng | §4 | §4 so sánh copy | B5 giữ nguyên nguồn | B4-006, B4-029, B4-035, B4-054 |
| K31 | copy tạo bảng riêng cho dữ liệu số/chuỗi thông thường | §4 | §4 | B5 | B4-006, B4-029, B4-035, B4-045 |
| K32 | CoW pandas 3: sửa Series/bảng con tách ra không sửa bảng chứa | §4 | §4 | B5, tự làm lỗi AI | B4-009, B4-045, B4-059 |
| K33 | Gán trực tiếp loc; giảm giá có điều kiện, giữ các hàng khác | §4 | §4 | B5 | B4-009, B4-015, B4-048 |
| K34 | Chained assignment không sửa bảng; ChainedAssignmentError là cảnh báo nếu không nâng warning thành error | §4 | §4 cảnh báo | B5, tự làm lỗi AI | B4-015, B4-019, B4-054 |
| K35 | Cột dẫn xuất lưu giá trị; sửa đầu vào rồi tính lại | §4 | §4, bài tập 4 | B5 | B4-006, B4-009, B4-019, B4-036, B4-039, B4-048, B4-054, B4-059 |
| K36 | Kiểm bảng cần sửa, hàng giữ nguyên, nguồn giữ nguyên và cột phụ thuộc | §4–5 | Bài tập 4, kiểm chứng | B5 asserts | B4-019, B4-029, B4-039, B4-048, B4-059 |
| K37 | to_csv mặc định ghi index; index_label đặt tên cột mã được xuất | §5 | §5, bài tập 5 | B8 đối chiếu | B4-016, B4-037 |
| K38 | index=False vẫn giữ id là cột nhưng bỏ mã chỉ ở index dù index có tên | §5 | §5, bài tập 5 | B8 | B4-007, B4-016, B4-037 |
| K39 | Giữ index hoặc chuyển mã thành cột trước khi xuất | §5 bài tập 5 | Bài tập 5 | — | B4-037, B4-055, B4-060 |
| K40 | Đọc lại, kiểm shape/columns/thiếu/tổng và chỉ tiêu hồ sơ | §5 | §5 | B8 | B4-027, B4-046, B4-047, B4-055 |
| K41 | Kiểm quan hệ mã–giá; shape/tổng khớp vẫn có thể ghép sai | §5 kiểm chứng | Kiểm chứng | B8 giới hạn kiểm tra | B4-027, B4-047, B4-060 |
| K42 | Kiểm ghi/đọc không xác nhận dữ liệu nguồn đúng | §5 | §5 | B4, B8 | B4-046, B4-047, B4-060 |
| K43 | value_counts/normalize=True bỏ nhãn thiếu mặc định; mẫu số tương ứng | — | Tự học đếm loại | B1, B7 | B4-049, B4-056 |
| K44 | nunique đếm nhãn khác nhau, mặc định bỏ thiếu | — | Tự học category | — | B4-017, B4-056 |
| K45 | category lưu nhãn và mã tham chiếu; hợp cột nhãn lặp, không mặc định hợp id | — | Tự học category | — | B4-017, B4-050 |
| K46 | memory_usage(deep=True), đo trước/sau; category không luôn tiết kiệm | — | Tự học category | — | B4-050 |
| K47 | Lấy index của top-k rồi drop các hàng đó để đo ảnh hưởng | §2 | §2 bỏ ba giá cao nhất | — | B4-028 |
| K48 | round kết quả thống kê để báo cáo/hiển thị; không suy thêm độ chính xác nguồn | §2 | §2 round | B1, B6–8 | B4-032 |
| K49 | Một biến TEN_QUAN cấu hình phân tích lặp lại cho quận khác | — | — | Tự làm hồ sơ quận thứ hai | B4-057 |
| K50 | Hồ sơ: quy mô, tỷ trọng quận trong bảng, trung vị so thành phố; giới hạn suy rộng snapshot | — | §2 đơn vị quan sát | B2, B6–8, tự làm 1 | B4-041, B4-057 |

### Bẫy trọng tâm: hai hình thức kiểm tra

| Bẫy | Đọc code/kết quả | Giải thích/sửa lỗi |
|---|---|---|
| Nhãn khác vị trí sau lọc; index không tự đánh lại | 005,044 | 010,040 |
| Series khác DataFrame | 011,024,053 | 010,020 |
| Số hàng khác số giá không thiếu | 004,012,013 | 038,049 |
| Thiếu khác0; chưa biết không có nghĩa không đạt | 004,013,052 | 008,030,038 |
| Mẫu số mean trên bool | 004,033,052 | 008 |
| Sửa Series/bảng trung gian không sửa bảng đích | 015,045,054 | 009,019,059 |
| Giá đã sửa nhưng cột tiền còn cũ | 006,036,054 | 009,019,039,048,059 |
| Gán tên không phải copy | 006,035 | 029 |
| Phí một lần bị nhân số đêm | 026,036 | 039 |
| Bỏ index làm mất mã | 007,037 | 060 |
| Tổng khớp không xác nhận mã–giá hoặc nguồn đúng | 027,046 | 047,060 |

### Rà trùng ý và giới hạn

Các câu lặp cơ chế trọng tâm được giữ ở dạng khác nhau: đọc code, sửa lỗi, khôi phục nguồn đã bị sửa, kiểm bảng trung gian, kiểm cột phụ thuộc và giải thích giới hạn kết quả. Ví dụ006 theo dõi alias/copy;029 yêu cầu khôi phục từ trạng thái đã hỏng;035 kiểm nền tảng với alias trỏ bản sao;054 kết hợp alias với chained assignment. 027 phát hiện tổng che lỗi,047 thiết kế phép kiểm quan hệ mã–giá,060 sửa xuất mất mã sau sắp xếp. Không có cặp được thiết kế chỉ đổi một chi tiết duy nhất; không bổ sung vượt60 câu.

Phân bố đáp án chỉ được kiểm về tổng và thứ tự không theo chu kỳ cố định. Mức độ chưa được đo thực nghiệm; các câu nền tảng được giữ đúng ma trận. Mọi ví dụ đều cung cấp dữ liệu hoặc output cần thiết, không phụ thuộc trạng thái câu khác.

### Phần xem trước Bài 5 — không tính vào60 câu

Cuối lab có `groupby("neighbourhood")["price"].agg(["median","size"])`, chọn quận có ít nhất300 chỗ ở và kiểm lại median bằng lọc thủ công. Chỉ ghi nhận phạm vi xem trước; không dùng làm câu hỏi hoặc bằng chứng bao phủ Bài 4.
