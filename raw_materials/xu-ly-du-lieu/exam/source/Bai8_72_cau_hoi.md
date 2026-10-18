# Bài 8 — Xử lý dữ liệu thời gian: ngân hàng 72 câu hỏi

## Nguồn đã đọc và giả định

Đã đọc toàn văn ba nguồn quyết định phạm vi, gồm tất cả ô hướng dẫn, code, bài tập, assert và tự học:

- **G**: [bai-08-xu-ly-du-lieu-thoi-gian.md](<D:/LTXLDL_GK/Bài 8/bai-08-xu-ly-du-lieu-thoi-gian.md>).
- **L**: [lecture_08.ipynb](<D:/LTXLDL_GK/Bài 8/lecture_08.ipynb>), 93 ô.
- **Lab**: [lab_08.ipynb](<D:/LTXLDL_GK/Bài 8/lab_08.ipynb>), 40 ô.

Đã đọc toàn bộ sáu đề mẫu về phong cách:

- **GK**: [Đề giữa kỳ luyện tập](<D:/LTXLDL_GK/Bài_kiểm_tra/2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf>), 6 trang; ưu tiên câu 19 (đếm ngày rồi pct_change), 20 (UTC sang Việt Nam), 26 (chẩn đoán đọc ngày/API và kỳ chưa trọn). Đã xem thêm hình trang 4 và 6 để đối chiếu nguyên văn code và lựa chọn.
- [LTXLDL_AI_5.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_5.pdf>), [LTXLDL_DS_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_1.pdf>), [LTXLDL_DS_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_2.pdf>): tình huống ngắn, đọc kết quả, phân biệt ý nghĩa với code chạy được, nhiễu từ sai lầm cụ thể.
- [LTXLDL_AI_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_1.pdf>), [LTXLDL_AI_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_2.pdf>): bổ trợ cách đọc code và trả lời ngắn, không mở rộng phạm vi Bài 8 sang nội dung NumPy của các đề này.

Không thiếu nguồn nào trong danh sách yêu cầu. Không tải snapshot thật hoặc chạy lại toàn bộ notebook với dữ liệu Airbnb; ngân hàng dùng đầu vào giả lập độc lập, không yêu cầu nhớ số review trong snapshot. Các liên kết đọc thêm trong tài liệu không được coi là nguồn đã đọc toàn văn. Mã ô L/Lab là vị trí tính từ 0 trong file notebook, tính cả ô Markdown; G dùng mục/tiêu đề.

Giả định **pandas 3.0.3**; kiểm chứng thực tế cũng dùng đúng **3.0.3**, ngày biên soạn 18/10/2026 (Asia/Bangkok). Mỗi câu độc lập; đầu mỗi câu mặc định có `import pandas as pd`. Mọi đầu vào cần thiết được khởi tạo trong câu hoặc cho đầy đủ bằng bảng/mô tả; không dùng biến của câu trước. Với đoạn cố ý sai, lời giải là thay dòng rồi chạy lại từ đầu trên dữ liệu gốc, không chuyển tiếp từ cột đã bị đọc nhầm.

Dữ liệu chỉ có ngày được hiểu theo độ chính xác ngày, không tự gán UTC. Mọi chuỗi dạng năm-tháng-ngày trong code dùng quy ước **YYYY-MM-DD**; khi có giờ thì thêm **HH:MM**, trừ khi câu ghi rõ định dạng khác. Dữ liệu có giờ ghi rõ quy ước và múi giờ khi ảnh hưởng. `NaN`/`nan` là thiếu số, `NaT` là thiếu ngày giờ; không yêu cầu khớp nguyên văn dtype, số chữ số in hoặc thông báo lỗi. Khi không quy định riêng, chấp nhận sai số số thực 1e-9; phần trăm báo cáo làm tròn 1 chữ số thập phân. Các chuỗi đánh giá đều là ngày ghi nhận review; chỉ bảng lưu trú mới cung cấp ngày vào/ra.

Múi giờ có trong phần trọng tâm theo GK20 dù tài liệu đánh dấu tự học. Nội dung quý, cửa sổ bảy ngày, so cùng kỳ và review/ngày đều thuộc trọng tâm theo Lab. Phần MR đào sâu các biến thể tự học có căn cứ; không có DST, lịch tài chính/kinh doanh, ARIMA, dự báo, kiểm định hoặc STL. Các câu về làm mượt chỉ kiểm giới hạn diễn giải, không dạy mô hình dự báo.

Ma trận dưới đây là thiết kế ngân hàng; mức độ được phân loại theo suy luận cần dùng, **không phải tỷ trọng chính thức, độ khó đo thực nghiệm hoặc dự đoán chắc chắn đề thi thật**.

## Ma trận thiết kế toàn bộ

| Nhóm chính | Tổng | TN | TL | Nền tảng | Vận dụng | Phân loại |
|---|---:|---:|---:|---:|---:|---:|
| 1. Đọc ngày, NaT, thành phần ngày và khoảng thời gian | 12 | 9 | 3 | 7 | 5 | 0 |
| 2. DatetimeIndex, chọn khoảng và phạm vi quan sát | 8 | 6 | 2 | 1 | 7 | 0 |
| 3. Resample, lịch đầy đủ và phép tổng hợp | 10 | 5 | 5 | 1 | 6 | 3 |
| 4. Rolling và diễn giải cửa sổ trượt | 8 | 5 | 3 | 1 | 5 | 2 |
| 5. Shift, pct_change và so sánh giữa các kỳ | 14 | 9 | 5 | 3 | 6 | 5 |
| 6. Múi giờ, lịch và chuẩn hóa theo số ngày | 8 | 6 | 2 | 2 | 4 | 2 |
| **Tổng trọng tâm** | **60** | **40** | **20** | **15** | **33** | **12** |

Phần bổ sung: **12 câu = 8 TN + 4 TL**; mức độ MR chỉ để quản lý biên soạn, không cộng vào ma trận 15–33–12. Mỗi câu tính đúng một nhóm chính; mục tiêu đầu trong mã K là mục tiêu chính, sau đó tối đa hai mục tiêu phụ.

| Đợt | Mã trọng tâm | TN/TL trọng tâm | Nền tảng/Vận dụng/Phân loại | Mã bổ sung | TN/TL bổ sung |
|---|---|---:|---:|---|---:|
| 1 | B8-001–B8-010 | 7/3 | 3/5/2 | B8-MR01–B8-MR02 | 1/1 |
| 2 | B8-011–B8-020 | 7/3 | 2/6/2 | B8-MR03–B8-MR04 | 2/0 |
| 3 | B8-021–B8-030 | 6/4 | 3/5/2 | B8-MR05–B8-MR06 | 1/1 |
| 4 | B8-031–B8-040 | 7/3 | 2/6/2 | B8-MR07–B8-MR08 | 2/0 |
| 5 | B8-041–B8-050 | 7/3 | 3/5/2 | B8-MR09–B8-MR10 | 1/1 |
| 6 | B8-051–B8-060 | 6/4 | 2/6/2 | B8-MR11–B8-MR12 | 1/1 |

Cả sáu đợt được hoàn thành tự động theo yêu cầu cuối. Mỗi đợt gồm 10 câu trọng tâm và 2 câu MR ở mục riêng; không tăng độ khó theo số đợt.

## Danh mục mục tiêu và câu dự kiến kiểm tra

Danh mục K được lập cho toàn bộ sáu đợt trước khi xuất. Bảng sau ghi cả nguồn đối chiếu và mã câu thực tế theo kế hoạch đã hoàn thành; mỗi mục đều được yêu cầu trong thân câu, không chỉ được nhắc ở lời giải.

| Mã | Mục tiêu phải sử dụng để trả lời | Đối chiếu ba nguồn Bài 8 | Mã câu |
|---|---|---|---|
| K01 | Chuỗi khác ngày giờ; không trừ chuỗi; sắp DD/MM khác thứ tự thời gian | G §1; L ô 6–7 | B8-011 |
| K02 | Quy ước nguồn, format, %d/%m/%Y, ngày mơ hồ và cách hiển thị | G §1; L ô 6–10,23–25 | B8-001, B8-010, B8-016, B8-019, B8-038, B8-051 |
| K03 | Bỏ format có thể sai không lỗi; dayfirst là ưu tiên, không kiểm chặt mọi định dạng | G §1; L ô 23–25,84 | B8-016, B8-038, B8-051 |
| K04 | raise/coerce; NaT; giữ raw và phân biệt lỗi đọc với thiếu nguồn | G §1; L ô 11–15; Lab ô 5–9 | B8-007, B8-008, B8-018, B8-031, B8-047, B8-051 |
| K05 | Số đêm, thiếu toán hạng; NaT không phải 0; truy vết hàng thiếu | L ô 19–25; Lab ô 5–9 | B8-008, B8-027, B8-047 |
| K06 | Timestamp/Series; year, month, quarter, dayofweek; .dt và thuộc tính index | L ô 16–22,78–79 | B8-003, B8-015, B8-021, B8-MR08, B8-041, B8-056 |
| K07 | Timedelta, .days/.dt.days; ranh giới tháng/năm, năm nhuận và ngày thập phân | G §1; L ô 19–22; Lab ô 5–7 | B8-008, B8-011, B8-021, B8-027 |
| K08 | set_index/sort_index; chọn năm/tháng/khoảng; nhãn đầy đủ và scalar | L ô 36–38,70–72 | B8-004, B8-012, B8-035, B8-MR09, B8-056 |
| K09 | Đơn vị một review; ngày review khác booking; ngày trùng vẫn hợp lệ | L ô 0,30–38; Lab ô 12–13 | B8-004, B8-018, B8-042 |
| K10 | Lọc trước tổng hợp; theo dõi hàng ngoài mốc/NaT; ngoài mốc chưa là lỗi nhập | L ô 33–38; Lab ô 12–13 | B8-018, B8-042, B8-048, B8-058 |
| K11 | Phạm vi thu đầy đủ; nhãn cuối kỳ, sự kiện cuối và mốc cắt; giữ/bỏ kỳ có căn cứ | L ô 43–47; Lab ô 14–20 | B8-010, B8-019, B8-025, B8-039, B8-042, B8-048, B8-057 |
| K12 | Resample theo lịch D, ME, QE, W-SUN; API pandas 3 | L ô 39–44; Lab ô 14–15 | B8-002, B8-010, B8-019, B8-039, B8-044, B8-057 |
| K13 | size/count/sum/mean theo đơn vị sự kiện hay bảng đếm; count có thể đúng | L ô 39–50; Lab ô 14–15 | B8-MR02, B8-022, B8-028, B8-032, B8-044, B8-045, B8-052, B8-057, B8-MR11 |
| K14 | Ngày 0 khác chưa biết; resample chỉ biết khoảng dữ liệu, thiếu ở hai đầu | L ô 39–50,62–66 | B8-002, B8-013, B8-022, B8-025, B8-028, B8-033, B8-052 |
| K15 | Lịch cho sẵn, reindex; asfreq cho chuỗi đã tổng hợp, không gộp sự kiện/không tự mở hai đầu | L ô 48–50,62–66 | B8-013, B8-028, B8-046, B8-MR10, B8-052 |
| K16 | rolling(k) theo hàng; lịch liên tiếp; center=False; sum và mean | L ô 51–56 | B8-005, B8-MR01, B8-014, B8-023, B8-036, B8-053 |
| K17 | min_periods đếm giá trị không thiếu; 0 là đã biết; không điền NaN đầu cho đẹp | L ô 51–53; Lab ô 21–25 | B8-005, B8-014, B8-MR04, B8-MR06, B8-049, B8-058 |
| K18 | Cửa sổ bảy ngày gồm t và sáu ngày trước; không dùng tương lai; đối chiếu gốc | Lab ô 21–28 | B8-029, B8-049, B8-058, B8-MR12 |
| K19 | idxmax khác max và cực đại gốc; trễ không cố định; làm mượt không dự báo/nhân quả | L ô 54–57; Lab ô 24–28 | B8-023, B8-029, B8-053 |
| K20 | shift dịch giá trị giữ nhãn; hàng trước khác tháng trước khi lịch khuyết | L ô 59–66 | B8-006, B8-013, B8-046, B8-054 |
| K21 | pct_change, tỷ lệ/%; chênh tuyệt đối; kỳ gốc 0; không ngầm fill missing | L ô 67–72 | B8-002, B8-017, B8-024, B8-033, B8-046, B8-055 |
| K22 | Cùng kỳ: shift 12 tháng, shift 4 quý; periods đúng tần suất và lịch | L ô 73–76; Lab ô 29–33 | B8-030, B8-043, B8-054 |
| K23 | Nêu kỳ gốc; cùng phạm vi; so tháng trước khác cùng năm; không suy nguyên nhân | L ô 70–76; Lab ô 29–33 | B8-009, B8-020, B8-024, B8-030, B8-037, B8-040, B8-043, B8-050, B8-054 |
| K24 | Tỷ lệ hai tổng khác trung bình tỷ lệ tháng; trọng số là quy mô kỳ gốc | L ô 82–83 | B8-009, B8-040 |
| K25 | month bỏ năm; gộp mùa có chủ ý; cùng số năm đóng góp, tránh năm chưa trọn | L ô 77–80 | B8-020, B8-056, B8-059 |
| K26 | Chỉ số 100=mức trung bình; chưa loại xu hướng/số ngày; hiểu quy tắc chia trung bình trượt | G §3 chỉ số theo tháng; L ô 78–80 | B8-020, B8-059 |
| K27 | days_in_month có năm nhuận; tổng tháng khác review/ngày; mẫu số mọi ngày đã quan sát | L ô 48–50; Lab ô 34–37 | B8-015, B8-034, B8-037, B8-045, B8-050, B8-060 |
| K28 | Gộp nhiều năm: tổng review/tổng ngày; không chia ngày một năm hoặc mean các mức ngày | Lab ô 34–37 | B8-034, B8-050 |
| K29 | Naive/aware; localize theo nguồn, convert cùng thời điểm; .dt; đổi ngày/thứ/năm; không gán UTC cho ngày thuần | L ô 26–28,86–87; GK20 | B8-003, B8-MR02, B8-026, B8-MR05, B8-MR08, B8-MR10, B8-060, B8-MR11, B8-MR12 |
| K30 | Biên ngày có giờ: <=00:00 bỏ phần còn lại; khoảng [đầu ngày, đầu ngày sau), cùng timezone | L ô 90–91 | B8-MR02, B8-MR07, B8-048, B8-MR10, B8-060 |
| K31 | rolling(k) khác rolling(kD); index ngày giờ sắp; biên (t-kD, t]; default min_periods | L ô 88–89 | B8-MR01, B8-MR03, B8-MR04, B8-MR06, B8-MR09, B8-MR12 |
| K32 | Kiểm bằng mask tháng/quý, tổng số đếm, cửa sổ gốc, kỳ gốc; assert không chứng minh nhân quả | L ô 84–85; Lab ô 1,24–25,31–32,38 | B8-029, B8-030, B8-039, B8-049, B8-059 |

## Cách tự làm

TN: chọn duy nhất một trong A/B/C/D; mỗi câu 1 điểm khi tự chấm. TL: thang tham khảo 5 điểm/câu; chấp nhận cách đúng tương đương. Đây là ngân hàng luyện tập, không phải một đề thi 72 câu trong 60 phút. File này chỉ có câu hỏi, kế hoạch và danh mục; đáp án, mức độ từng câu, bẫy và hướng dẫn chấm nằm ở file riêng.


## Đợt 1

### A. Câu hỏi trọng tâm

#### B8-001 — Trắc nghiệm

Nguồn quy định **DD/MM/YYYY**, dữ liệu chỉ có ngày. Xét:

```python
s = pd.Series(["04/09/2026", "09/04/2026"])
d = pd.to_datetime(s, format="%d/%m/%Y")
print(d.dt.month.tolist())
```

Dòng cuối in ra gì?

**A.** `[4, 9]`

**B.** `[9, 4]`

**C.** `[9, 9]`

**D.** Báo lỗi vì hai chuỗi có thể đọc theo cả hai quy ước.


#### B8-002 — Trắc nghiệm

Mỗi phần tử sau là **một review**, có giờ, cùng giờ địa phương không gắn timezone. Đã thu đủ mọi ngày 01–04/08/2026; không có hàng nghĩa là không có review.

```python
t = pd.to_datetime(["2026-08-01 08:00", "2026-08-01 19:00",
                    "2026-08-02 09:00", "2026-08-02 11:00",
                    "2026-08-04 10:00"])
s = pd.Series(1, index=t).resample("D").size()
print(s.pct_change(fill_method=None).head(3).tolist())
```

Dòng cuối in ra gì? `nan` ký hiệu giá trị thiếu; kết quả ở dạng **tỷ lệ**.

**A.** `[nan, 0.0, -100.0]`

**B.** `[nan, 0.0, 0.0]`

**C.** `[nan, 1.0, -1.0]`

**D.** `[nan, 0.0, -1.0]`


#### B8-003 — Trắc nghiệm

Biết 31/12/2026 là **thứ Năm**; Việt Nam là UTC+7.

```python
t = pd.Timestamp("2026-12-31 19:15", tz="UTC")
v = t.tz_convert("Asia/Ho_Chi_Minh")
print(v.year, v.month, v.dayofweek)
```

Dòng cuối in ra gì?

**A.** `2026 12 3`

**B.** `2027 1 5`

**C.** `2027 1 4`

**D.** `2026 12 4`


#### B8-004 — Trắc nghiệm

Bảng sau ghi ngày review theo YYYY-MM-DD, chỉ có ngày, không có giá trị thiếu. Mỗi hàng là một review khác nhau, kể cả khi trùng ngày. Nguồn đã thu đủ tháng 3/2026.

```python
df = pd.DataFrame({"date": ["2026-03-03", "2026-03-01",
                             "2026-03-03", "2026-02-28"],
                   "id": [11, 12, 13, 14]})
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
r = df.set_index("date").sort_index()
print(len(r.loc["2026-03"]))
```

Dòng cuối in ra gì?

**A.** `3`

**B.** `2`

**C.** `4`

**D.** Báo lỗi vì chỉ mục ngày bị trùng.


#### B8-005 — Trắc nghiệm

`s` đã là số review của bốn tháng trọn liên tiếp, sắp đúng lịch, không thiếu.

```python
s = pd.Series([6, 18, 12, 24],
              index=pd.date_range("2026-01-31", periods=4, freq="ME"))
t = s.rolling(3, min_periods=3, center=False).mean()
print(t.iloc[-1])
```

Giá trị cuối được tính thế nào?

**A.** `12.0`, trung bình tháng 1–3.

**B.** `18.0`, trung bình tháng 2–4.

**C.** `54.0`, tổng tháng 2–4.

**D.** `24.0`, chỉ lấy tháng 4 vì cửa sổ kết thúc ở tháng 4.


#### B8-006 — Trắc nghiệm

Chuỗi sau đã tổng hợp theo tháng, có đủ tháng 1–4/2026, sắp tăng dần.

```python
s = pd.Series([8, 10, 15, 12],
              index=pd.date_range("2026-01-31", periods=4, freq="ME"))
p = s.shift(1)
print(p.loc["2026-03-31"], p.index.equals(s.index))
```

Dòng cuối in ra gì?

**A.** `15.0 True`

**B.** `12.0 False`

**C.** `10.0 True`

**D.** `10.0 False`


#### B8-007 — Trắc nghiệm

Nguồn dùng DD/MM/YYYY; `None` là thiếu từ nguồn, chuỗi khác None phải là một ngày hợp lệ theo quy ước đó.

```python
raw = pd.Series(["30/04/2026", None, "31/04/2026", "05/04/2026"],
                index=["R1", "R2", "R3", "R4"])
parsed = pd.to_datetime(raw, format="%d/%m/%Y", errors="coerce")
bad = raw.notna() & parsed.isna()
print(bad[bad].index.tolist())
```

Dòng cuối in ra gì?

**A.** `['R2', 'R3']`

**B.** `[]`

**C.** `['R2']`

**D.** `['R3']`


#### B8-008 — Tự luận ngắn

Mỗi hàng là một lượt lưu trú, ngày theo DD/MM/YYYY, không có giờ. Năm 2024 nhuận, tháng 2 có 29 ngày.

```python
dat = pd.DataFrame({"vao": ["28/02/2024", "30/12/2025", "31/04/2026", None],
                    "ra": ["01/03/2024", "02/01/2026", "03/05/2026", "04/05/2026"]},
                   index=["D1", "D2", "D3", "D4"])
```

Viết code tạo `vao`, `ra`, `so_dem` và mask `loi_vao` chỉ đánh dấu lỗi chuyển đổi. Nêu số đêm từng hàng và lý do không điền mọi số đêm thiếu bằng 0. Khoảng 6 dòng code cùng giải thích ngắn.

#### B8-009 — Tự luận ngắn

Đây là **tổng review của từng tháng trọn**, cùng cách thu thập, đã quan sát đầy đủ hai tháng đầu của mỗi năm. Không có tháng thiếu.

| Tháng | 2025 | 2026 |
|---|---:|---:|
| 1 | 20 | 40 |
| 2 | 180 | 198 |

Một bạn lấy trung bình hai tỷ lệ tăng từng tháng và báo “tổng hai tháng tăng 55%”. Hãy tính mức thay đổi đúng của **tổng hai tháng** (làm tròn 1 chữ số phần trăm), viết phép tính bằng Python và giải thích mẫu số/trọng số gây khác biệt. Có được từ kết quả này kết luận nguyên nhân là chiến dịch quảng cáo không?

#### B8-010 — Tự luận ngắn

Mỗi hàng là một review; ngày DD/MM/YYYY, chỉ có ngày, đều hợp lệ. Đã thu đủ **01/04 đến hết 12/06/2026**; sau đó chưa biết. Các ngày trong phạm vi không xuất hiện nghĩa là không có review. Code sau được viết cho pandas 3.0.3:

```python
rv = pd.DataFrame({"ngay": ["05/04/2026", "08/04/2026", "09/05/2026",
                             "10/05/2026", "11/06/2026", "12/06/2026"]})
rv["ngay"] = pd.to_datetime(rv["ngay"])
thang = rv.set_index("ngay").resample("M").size()
tang = thang.pct_change(fill_method=None)
```

(a) Dòng đọc ngày có thể sai ngữ nghĩa thế nào khi không báo lỗi? (b) Sửa **hai dòng đọc ngày và tổng hợp**. (c) Có nên dùng `tang` tháng 6 để kết luận xu hướng tháng trọn không? Nêu hai kỳ đang được so và cách xử lý phù hợp. Khoảng 6 dòng code/giải thích.


### A. Câu hỏi tự học bổ sung

#### B8-MR01 — Trắc nghiệm

Chuỗi đã tổng hợp tại **ba ngày không liên tiếp**, chỉ có ngày, index tăng dần, không thiếu giá trị. Không suy ra gì về các ngày không được liệt kê.

```python
s = pd.Series([3, 5, 7], index=pd.to_datetime([
    "2026-06-01", "2026-06-04", "2026-06-08"]))
a = s.rolling(3, min_periods=1, center=False).sum()
b = s.rolling("3D", min_periods=1, center=False, closed="right").sum()
print(a.iloc[-1], b.iloc[-1])
```

Dòng cuối in ra gì?

**A.** `15.0 15.0`

**B.** `7.0 7.0`

**C.** `15.0 12.0`

**D.** `15.0 7.0`


#### B8-MR02 — Tự luận ngắn

Nguồn cho biết các chuỗi sau là **giờ UTC**, chưa có timezone trong kiểu dữ liệu; mỗi hàng là một review. Việt Nam UTC+7. Hệ thống đã thu đủ cả ngày **01/07/2026 theo giờ Việt Nam**; ngoài ngày này không cần suy luận độ đầy đủ.

```python
raw = pd.Series(["2026-06-30 16:30", "2026-06-30 17:00",
                 "2026-07-01 10:00", "2026-07-01 17:00"])
```

Viết code gắn đúng múi giờ, đổi sang giờ Việt Nam, lọc trọn ngày 01/07 bằng khoảng phải mở và đếm review. Nêu các hàng được giữ (chỉ mục 0–3). Vì sao không dùng `tz_localize("Asia/Ho_Chi_Minh")` trực tiếp cho các giá trị gốc?


## Đợt 2

### A. Câu hỏi trọng tâm

#### B8-011 — Trắc nghiệm

Nguồn dùng DD/MM/YYYY, chỉ có ngày. Xét riêng hai thao tác trên danh sách chuỗi `x`:

```python
x = ["02/12/2026", "15/01/2026", "03/02/2026"]
thu_tu = sorted(x)
# Thao tác thứ hai, chạy riêng:
hieu = x[0] - x[1]
```

Nhận định nào đúng?

**A.** `thu_tu` theo đúng thời gian; `hieu` là số ngày từ 15/01 đến 02/12.

**B.** `thu_tu` bắt đầu bằng `15/01/2026`; phép trừ báo lỗi kiểu.

**C.** `thu_tu` bắt đầu bằng `02/12/2026`; phép trừ báo lỗi kiểu.

**D.** `thu_tu` bắt đầu bằng `02/12/2026`; `hieu` bằng 0 vì hai chuỗi cùng năm.


#### B8-012 — Trắc nghiệm

Chuỗi tổng review của các tháng trọn sau có **DatetimeIndex duy nhất**, độ chính xác ngày, sắp tăng dần; nhãn đều ở 00:00, không gắn timezone.

```python
s = pd.Series([8, 10, 12, 15], index=pd.to_datetime([
    "2026-01-31", "2026-02-28", "2026-03-31", "2026-04-30"]))
a = s.loc["2026-03-31"]
b = s.loc["2026-03"]
```

Nhận định nào đúng?

**A.** `a` là một giá trị số 12; `b` là Series một phần tử.

**B.** Cả `a` và `b` đều là giá trị số 12 vì chỉ có một hàng tháng 3.

**C.** Cả `a` và `b` đều là Series vì chỉ mục có kiểu ngày giờ.

**D.** `a` là Series; `b` là một giá trị số vì nhãn ngắn hơn.


#### B8-013 — Trắc nghiệm

Chuỗi tổng review theo tháng đã sắp, nhãn cuối tháng. Tháng 2/2026 **chưa thu thập**, các tháng liệt kê đã thu đủ.

```python
s = pd.Series([12, 18, 24, 30], index=pd.to_datetime([
    "2026-01-31", "2026-03-31", "2026-04-30", "2026-05-31"]))
a = s.shift(1).loc["2026-03-31"]
b = s.asfreq("ME").shift(1).loc["2026-03-31"]
```

Cặp `(a, b)` là gì?

**A.** `(12, 12)`

**B.** `(0, 0)`

**C.** `(12, 0)`

**D.** `(12, NaN)`


#### B8-014 — Trắc nghiệm

Mỗi hàng là số review một ngày trên lịch 01–05/06/2026 liên tiếp, sắp tăng dần. 0 nghĩa là đã quan sát không có review; NaN nghĩa là ngày chưa có số liệu.

```python
s = pd.Series([2, 0, float("nan"), 4, 6],
              index=pd.date_range("2026-06-01", periods=5, freq="D"))
t = s.rolling(3, min_periods=3, center=False).mean()
print(t.iloc[-1])
```

Dòng cuối cho kết quả nào?

**A.** `10/3` vì đủ ba vị trí cuối.

**B.** `NaN` vì cửa sổ cuối chỉ có hai giá trị không thiếu.

**C.** `5.0` vì mean luôn bỏ NaN bất kể min_periods.

**D.** `0.0` vì cửa sổ có một ngày chưa biết.


#### B8-015 — Trắc nghiệm

Hai tháng 2 sau đều thu đủ; số review tương ứng là 280 và 290, không thiếu ngày trong phạm vi thu thập. Năm 2024 nhuận.

```python
i = pd.to_datetime(["2023-02-28", "2024-02-29"])
s = pd.Series([280, 290], index=i)
print((s / s.index.days_in_month).tolist())
```

Dòng cuối in ra gì (review/ngày)?

**A.** `[10.0, 10.0]`

**B.** `[10.0, 290/28]`

**C.** `[280/29, 10.0]`

**D.** `[280.0, 290.0]`


#### B8-016 — Trắc nghiệm

Nguồn xác nhận các chuỗi chỉ có ngày theo DD/MM/YYYY. Nhiệm vụ hiện tại chỉ yêu cầu đọc đúng các giá trị đã cho, **không yêu cầu kiểm định dạng chặt**.

```python
s = pd.Series(["06/08/2026", "11/08/2026"])
a = pd.to_datetime(s, dayfirst=True)
b = pd.to_datetime(s, format="%d/%m/%Y")
```

Nhận định nào đúng?

**A.** `a` chắc chắn sai vì chỉ `format` mới đọc được DD/MM/YYYY.

**B.** Có thể xác nhận quy ước của mọi nguồn chỉ bằng chuỗi `06/08/2026`.

**C.** Nếu kết quả hiển thị YYYY-MM-DD thì pandas đã đọc chuỗi gốc theo YYYY-MM-DD.

**D.** Cả hai cách đọc đúng hai giá trị này; biết định dạng nguồn thì khai báo format phù hợp giúp thể hiện quy ước rõ ràng.


#### B8-017 — Trắc nghiệm

Chuỗi tổng review bốn tháng trọn liên tiếp, sắp tăng, không thiếu. Cần in phần trăm thay đổi tháng 2 so tháng 1, một chữ số thập phân.

```python
s = pd.Series([40, 50, 60, 72],
              index=pd.date_range("2026-01-31", periods=4, freq="ME"))
p = s.pct_change(fill_method=None).iloc[1]
```

Dòng nào in đúng **`25.0%`**?

**A.** `print(f"{p:.1f}%")`

**B.** `print(f"{p * 100:.1%}")`

**C.** `print(f"{p:.1%}")`

**D.** `print(f"{1 + p:.1%}")`


#### B8-018 — Tự luận ngắn

Mỗi hàng sau là một review; ngày YYYY-MM-DD, chỉ có ngày. Nguồn thu đủ 01–29/06/2026; ngày ngoài khoảng vẫn có thể hợp lệ do thu muộn. Hàng NaT không xác định được thuộc phạm vi nào.

```python
raw = pd.DataFrame({"id": [1,2,3,4,5,6],
                    "date": ["2026-06-29", "2026-06-02", "2026-06-29",
                             "2026-06-30", None, "2026-06-31"]})
```

Viết code giữ cột gốc, đổi kiểu có coerce, tạo `r` đã lọc phạm vi và sắp ngày để tổng hợp sau đó. Báo số hàng giữ, số hàng có ngày hợp lệ ngoài phạm vi, số lỗi đọc và số thiếu nguồn. Có nên xóa một trong hai hàng ngày 29/06 không?

#### B8-019 — Tự luận ngắn

Nguồn DD/MM/YYYY, chỉ có ngày; mỗi hàng là một review. Đã thu đủ **01/01 đến hết 29/06/2026**, ngày không có hàng trong khoảng đó là 0 review; 30/06 chưa biết. Năm 2026: quý I có 90 ngày; tháng 4 có 30 ngày, tháng 5 có 31 ngày.

```python
rv = pd.DataFrame({"ngay": ["02/01/2026", "03/02/2026", "04/03/2026",
                             "05/04/2026", "06/05/2026", "07/06/2026"]})
rv["ngay"] = pd.to_datetime(rv["ngay"])
q = rv.set_index("ngay").resample("Q").size()
doi = q.pct_change(fill_method=None)
```

(a) Chỉ ra vấn đề đọc ngày và mã tần suất. (b) Sửa hai dòng đó; viết thêm cách chọn quý đã trọn dựa trên mốc 29/06. (c) Quý II có nhãn 30/06 thì đã trọn chưa? Tính số ngày thực sự đã quan sát của hai quý, kiểm tổng số review và nhận xét về kết luận “quý II bằng quý I nên xu hướng không đổi”.

#### B8-020 — Tự luận ngắn

Để so **phân bố theo tháng số 1–12 qua nhiều năm**, bạn có tổng review từng tháng của hai năm 2024–2025 đã thu đủ cả năm và năm 2026 mới thu đủ tháng 1–2. Bảng nhỏ ghi riêng hai tháng cần tính; mười tháng khác trong mỗi năm trọn đều có tổng 30:

| Năm | Tháng 1 | Tháng 2 |
|---|---:|---:|
| 2024 | 20 | 30 |
| 2025 | 40 | 30 |
| 2026 | 60 | 60 |

Một bạn gộp mọi năm theo `.index.month` và cho rằng tháng nào cao hơn là mùa cao điểm đã loại xu hướng.
Hãy chọn phạm vi năm phù hợp, tính tổng tháng 1, tổng tháng 2 và chỉ số của chúng với **100 = trung bình 12 tổng tháng**. Giải thích thông tin mất đi khi lấy `.month`, rủi ro từ năm 2026 và hai giới hạn còn lại của chỉ số. Không cần viết bảng 36 hàng.


### A. Câu hỏi tự học bổ sung

#### B8-MR03 — Trắc nghiệm

Chuỗi sau có giờ, không gắn timezone, chỉ mục tăng dần. Các giá trị đã biết; không suy ra dữ liệu ngoài những thời điểm cho sẵn.

```python
s = pd.Series([2, 5, 7, 11], index=pd.to_datetime([
    "2026-08-01 12:00", "2026-08-02 12:00",
    "2026-08-04 11:00", "2026-08-04 12:00"]))
t = s.rolling("3D", min_periods=1, closed="right").sum()
print(t.iloc[-1])
```

Dòng cuối in ra gì?

**A.** `23.0`

**B.** `25.0`

**C.** `18.0`

**D.** `11.0`


#### B8-MR04 — Trắc nghiệm

Chuỗi ba ngày không liên tiếp, chỉ có ngày, index sắp tăng, không thiếu giá trị:

```python
s = pd.Series([2, 4, 6], index=pd.to_datetime([
    "2026-06-01", "2026-06-03", "2026-06-08"]))
a = s.rolling(3).mean()
b = s.rolling("3D", closed="right").mean()
```

Không truyền `min_periods`. Cặp giá trị **đầu tiên** của `(a,b)` là gì?

**A.** `(2.0, 2.0)`

**B.** `(NaN, NaN)`

**C.** `(NaN, 2.0)`

**D.** `(2.0, NaN)`



## Đợt 3

### A. Câu hỏi trọng tâm

#### B8-021 — Trắc nghiệm

Dữ liệu chỉ có ngày, không gắn timezone. Năm 2025 không nhuận.

```python
a = pd.Timestamp("2025-12-30")
b = pd.Timestamp("2026-01-02")
d = b - a
print(type(d).__name__, d.days)
```

Dòng cuối in ra gì?

**A.** `Timedelta 3`

**B.** `Timestamp 3`

**C.** `Timedelta 2`

**D.** Báo lỗi vì `.days` chỉ dùng qua `.dt`.


#### B8-022 — Trắc nghiệm

`s` là **số review đã tổng hợp của từng ngày có review**, không phải mỗi hàng một review. Đã thu đủ 01–04/09/2026, ngày không liệt kê là 0 review. Mọi giá trị trong s không thiếu.

```python
s = pd.Series([4, 2, 6], index=pd.to_datetime([
    "2026-09-01", "2026-09-03", "2026-09-04"]))
```

Cần tổng review tháng 9 trong **phạm vi 01–04/09 đã quan sát**. Lệnh và kết quả nào đúng?

**A.** `s.resample("ME").size()` cho 12 review.

**B.** `s.resample("ME").count()` cho 12 review.

**C.** `s.resample("ME").sum()` cho 12 review.

**D.** `s.resample("ME").mean()` cho 12 review.


#### B8-023 — Trắc nghiệm

Đây là số review sáu ngày liên tiếp đã thu đủ, sắp theo ngày. Không có đồng hạng cực đại trong chuỗi gốc hoặc chuỗi rolling.

```python
s = pd.Series([12, 0, 8, 9, 10, 0],
              index=pd.date_range("2026-06-01", periods=6, freq="D"))
t = s.rolling(3, min_periods=3, center=False).mean()
print(t.idxmax().day, t.max())
```

Dòng cuối in ra gì?

**A.** `1 12.0`

**B.** `5 9.0`

**C.** `5 10.0`

**D.** `4 9.0`


#### B8-024 — Trắc nghiệm

Hai tháng trọn liên tiếp tháng 4 và tháng 5/2026 được thu đầy đủ, tổng review lần lượt 80 và100. Lấy tháng 4 làm kỳ gốc. Bộ ba nào lần lượt là **chênh lệch tuyệt đối; phần trăm tăng; kỳ này bằng bao nhiêu phần trăm kỳ gốc**?

**A.** `20 review; 20%; 120%`

**B.** `20 review; 125%; 25%`

**C.** `0.25 review; 25%; 125%`

**D.** `20 review; 25%; 125%`


#### B8-025 — Trắc nghiệm

Nguồn xác nhận đã thu đầy đủ **01/04 đến hết 30/06/2026**, dữ liệu chỉ có ngày. Review cuối cùng xảy ra 29/06; ngày 30/06 đã kiểm tra và không có review. Sau tổng hợp, chuỗi quý có nhãn30/06.

Nhận định nào đúng?

**A.** Phải bỏ quý II vì sự kiện cuối không rơi vào30/06.

**B.** Phải bỏ hàng cuối bằng `iloc[:-1]` để tránh mọi kỳ chưa trọn.

**C.** Quý II trọn theo phạm vi thu thập đã xác nhận; có thể giữ, dù ngày cuối có0 review.

**D.** Quý II trọn chỉ vì nhãn của resample là 30/06, không cần biết phạm vi thu thập.


#### B8-026 — Trắc nghiệm

API xác nhận chuỗi giờ gốc là UTC nhưng chưa gắn timezone trong kiểu dữ liệu. Cần một cột giờ Việt Nam (UTC+7).

```python
s = pd.Series(pd.to_datetime(["2026-07-01 20:00", "2026-07-02 01:00"],
                             format="%Y-%m-%d %H:%M"))
```

Biểu thức nào thực hiện đúng?

**A.** `s.dt.tz_convert("Asia/Ho_Chi_Minh")`

**B.** `s.dt.tz_localize("UTC").dt.tz_convert("Asia/Ho_Chi_Minh")`

**C.** `s.dt.tz_localize("Asia/Ho_Chi_Minh")`

**D.** `s.dt.tz_localize("UTC").dt.tz_localize("Asia/Ho_Chi_Minh")`


#### B8-027 — Tự luận ngắn

Mỗi hàng là một khoảng lưu trú có **cả giờ**, cùng giờ địa phương không gắn timezone, không xét đổi múi giờ. Nguồn dùng YYYY-MM-DD HH:MM. Cần khoảng thời gian theo **ngày dạng số thực**, không phải quy tắc tính phí đêm.

```python
dat = pd.DataFrame({"vao": ["2026-06-30 18:00", "2026-12-31 12:00", None],
                    "ra": ["2026-07-02 06:00", "2027-01-01 18:00", "2026-07-03 12:00"]})
```

Viết phép chuyển kiểu và tính số ngày dạng số thực, đồng thời nêu `.dt.days` trả gì ở hai hàng đầu. Giữ thiếu ở hàng 2. Kết quả làm tròn2 chữ số hoặc sai số tuyệt đối không quá1e-9.

#### B8-028 — Tự luận ngắn

`s` đã là số review từng ngày có review; nguồn xác nhận thu đủ **01–05/06/2026**, các ngày không liệt kê trong khoảng này có0 review. Dữ liệu chỉ có ngày, index sắp tăng, không trùng. Ngày06/06 chưa biết.

```python
s = pd.Series([2, 4], index=pd.to_datetime(["2026-06-02", "2026-06-04"]))
lich = pd.date_range("2026-06-01", "2026-06-05", freq="D")
```

Dùng lịch cho sẵn để tạo `du`, rồi tính trung bình review trên **mọi ngày đã quan sát**. Vì sao chỉ `s.resample("D").sum()` hoặc `s.asfreq("D", fill_value=0)` chưa đủ lịch cần thiết? Nếu thêm ngày 06 vào lịch, có được tự điền0 không?

#### B8-029 — Tự luận ngắn

Chuỗi sau là số review của **tám ngày liên tiếp đã thu đủ**, 01–08/11/2026, không thiếu, index tăng dần. Chỉ dùng dữ liệu trong chuỗi, không dùng ngày trước 01/11. Không có đồng hạng cực đại.

```python
s = pd.Series([14, 0, 0, 3, 4, 5, 6, 7],
              index=pd.date_range("2026-11-01", periods=8, freq="D"))
```

Tạo trung bình7 ngày kết thúc tại ngày đang xét, `min_periods=7`, `center=False`. Tìm ngày đạt trung bình lớn nhất và kiểm lại bằng các giá trị gốc. Nêu sáu kết quả đầu, ngày gốc có nhiều review nhất và nhận xét về câu “đỉnh đường mượt luôn trễ6 ngày và dự báo ngày mai có cùng mức”.

#### B8-030 — Tự luận ngắn

Chuỗi `q` là tổng review các quý trọn liên tiếp, sắp tăng, không thiếu. Nguồn đã thu đủ toàn bộ năm 2025 và quýI/2026. Dữ liệu chỉ có ngày. Mỗi nhãn là cuối quý.

```python
q = pd.Series([40, 60, 80, 100, 50], index=pd.to_datetime([
    "2025-03-31", "2025-06-30", "2025-09-30", "2025-12-31", "2026-03-31"]))
doi = q / q.shift(12) - 1
```

Sửa dòng `doi` để đo quýI/2026 so quýI/2025; nêu tỷ lệ và phần trăm. Nếu có đủ lịch xa hơn, `shift(12)` tại quýI/2026 sẽ lấy quý nào? Viết mask ngày để kiểm độc lập số review quýI/2025 nếu có bảng sự kiện `rv` với cột ngày giờ `date` đã chuyển kiểu (không gắn timezone), không cần tạo dữ liệu rv.


### A. Câu hỏi tự học bổ sung

#### B8-MR05 — Trắc nghiệm

Nguồn xác nhận giá trị `t` là giờ **địa phương Việt Nam UTC+7**, chưa gắn timezone. Cần biểu diễn chính thời điểm đó ở UTC.

```python
t = pd.Timestamp("2026-08-01 02:00")
```

Lệnh nào đúng và cho giờ UTC tương ứng?

**A.** `t.tz_convert("UTC")` → 01/08 02:00 UTC.

**B.** `t.tz_localize("UTC")` → 01/08 02:00 UTC.

**C.** `t.tz_localize("Asia/Ho_Chi_Minh").tz_convert("UTC")` → 31/07 19:00 UTC.

**D.** `t.tz_localize("Asia/Ho_Chi_Minh").tz_convert("UTC")` → 01/08 09:00 UTC.


#### B8-MR06 — Tự luận ngắn

Chuỗi số đo đã tổng hợp tại bốn thời điểm sau, cùng giờ địa phương không gắn timezone. Index tăng; NaN là số đo chưa biết, không phải0. Không được tự bổ sung các thời điểm vắng.

```python
s = pd.Series([2, 0, float("nan"), 8], index=pd.to_datetime([
    "2026-06-01 09:00", "2026-06-02 09:00",
    "2026-06-04 09:00", "2026-06-05 09:00"]))
```

Tại05/06 09:00, so `rolling(3, min_periods=2).mean()` với `rolling("3D", min_periods=2, closed="right").mean()`, cả hai center=False. Liệt kê thành phần hai cửa sổ và giải thích kết quả; không điền NaN bằng 0. Sai số 1e-9.


## Đợt 4

### A. Câu hỏi trọng tâm

#### B8-031 — Trắc nghiệm

Nguồn chỉ có ngày, dùng DD/MM/YYYY; None là thiếu từ nguồn.

```python
raw = pd.Series(["29/02/2025", "28/02/2025", None])
# Xét độc lập, mỗi lần khởi tạo lại raw như trên:
a = pd.to_datetime(raw, format="%d/%m/%Y", errors="raise")
b = pd.to_datetime(raw, format="%d/%m/%Y", errors="coerce")
```

Biết2025 không nhuận, nhận định nào đúng? Hai lệnh được xét **riêng**, không hỏi việc chương trình có chạy tiếp sau lỗi hay không.

**A.** `a` và `b` đều đổi hàng 0 thành28/02/2025.

**B.** `a` chỉ báo lỗi vì None; `b` chỉ thiếu ở hàng 2.

**C.** `a` trả NaT; `b` báo lỗi cho ngày 29/02.

**D.** `a` báo lỗi vì ngày 29/02 không tồn tại; `b` có NaT ở hàng 0 và2.


#### B8-032 — Trắc nghiệm

Mỗi hàng là một review trong tháng 6/2026 đã thu đủ; ngày YYYY-MM-DD chỉ có ngày. `diem` có thể thiếu nhưng review vẫn tồn tại. `id` luôn có giá trị.

```python
rv = pd.DataFrame({"date": pd.to_datetime([
    "2026-06-01", "2026-06-01", "2026-06-02", "2026-06-03"]),
    "id": [11,12,13,14], "diem": [5, None, 4, 3]}).set_index("date")
```

Muốn đếm số review tháng 6, nhận định nào đúng?

**A.** Chỉ `rv.resample("ME")["diem"].count()` cho 4, vì count luôn đếm mọi hàng.

**B.** `rv.resample("ME").size()` và `rv.resample("ME")["id"].count()` đều cho 4; count trên `diem` cho 3.

**C.** `rv.resample("ME")["diem"].mean()` cho 4, nên đó cũng là số review đúng theo ý nghĩa phép tính.

**D.** Mọi cách dùng count đều sai dù cột được chọn không thiếu.


#### B8-033 — Trắc nghiệm

Chuỗi tháng liên tiếp có nhãn cuối tháng, sắp tăng. Tháng2 chưa thu thập nên NaN; các tháng khác đã thu đủ.

```python
s = pd.Series([10.0, float("nan"), 15.0, 30.0],
              index=pd.date_range("2026-01-31", periods=4, freq="ME"))
print(s.pct_change(fill_method=None).tolist())
```

Dòng cuối in ra gì, ở dạng tỷ lệ?

**A.** `[nan, nan, nan, 1.0]`

**B.** `[nan, 0.0, 0.5, 1.0]`

**C.** `[nan, -1.0, inf, 1.0]`

**D.** `[nan, nan, 0.5, 1.0]`


#### B8-034 — Trắc nghiệm

Hai tháng 2/2023 và2/2024 đều thu đủ, tổng review tương ứng280 và580. Tháng2/2023 có28 ngày, tháng 2/2024 có29 ngày. Cần **mức review/ngày gộp chung của hai tháng 2**, mọi ngày quan sát có trọng số như nhau.

Phép tính nào đúng?

**A.** `(280/28 + 580/29)/2 = 15`

**B.** `(280+580)/29`, vì dùng số ngày năm gần nhất.

**C.** `(280+580)/(28+29) = 860/57`

**D.** `(280+580)/(28*2) = 860/56`


#### B8-035 — Trắc nghiệm

Bảng sự kiện chỉ có ngày hợp lệ, index chưa sắp, không trùng. Xét:

```python
r = pd.DataFrame({"id": [1,2,3,4]}, index=pd.to_datetime([
    "2026-03-03", "2026-01-02", "2026-02-10", "2026-03-01"]))
```

Cần chọn từ tháng 1 đến hết tháng 2/2026. Nhận định nào đúng?

**A.** Mọi phép `.loc`, kể cả chọn đúng một nhãn có sẵn, đều luôn lỗi khi index chưa sắp.

**B.** `sort_index()` xóa các ngày trùng nên luôn phải tránh dùng.

**C.** Dữ liệu đã được sắp theo id thì chắc chắn cũng sắp đúng ngày.

**D.** Nên sắp index trước khi cắt khoảng nhãn; việc cắt khoảng trên index chưa sắp có thể lỗi, nhưng chọn nhãn có sẵn không vì thế mà luôn lỗi.


#### B8-036 — Trắc nghiệm

`s` đã tổng hợp ở bốn ngày được liệt kê, chỉ có ngày, index tăng. Chưa biết số liệu ở các ngày khác.

```python
s = pd.Series([2, 4, 6, 8], index=pd.to_datetime([
    "2026-06-01", "2026-06-02", "2026-06-08", "2026-06-09"]))
t = s.rolling(3, min_periods=3, center=False).sum()
```

Giá trị `t` tại09/06 dùng những ngày nào?

**A.** 02/06,08/06,09/06; tổng 18.

**B.** 07/06,08/06,09/06; tổng 14 vì mặc định07/06 là 0.

**C.** Chỉ08/06,09/06; tổng 14.

**D.** 01/06,02/06,08/06; tổng 12.


#### B8-037 — Trắc nghiệm

Tháng1/2026 có310 review trên31 ngày đã thu đủ; tháng 2/2026 có294 review trên28 ngày đã thu đủ. Các ngày không review đã được ghi nhận là 0, không có thiếu nguồn. Lấy tháng 1 làm kỳ gốc.

Nhận định nào đúng (làm tròn1 chữ số phần trăm)?

**A.** Theo tổng tăng5,0%; theo review/ngày giảm5,2%.

**B.** Theo tổng giảm5,2%; theo review/ngày tăng5,0%.

**C.** Theo cả hai cách đều giảm5,2% vì cùng dùng hai tháng.

**D.** Theo review/ngày tăng10,7% vì `31/28 - 1` là tỷ lệ cần báo.


#### B8-038 — Tự luận ngắn

Nguồn khẳng định DD/MM/YYYY, chỉ có ngày, không thiếu. Hai chuỗi là ngày vào/ra của một lượt lưu trú.

```python
vao_raw = "04/08/2026"
ra_raw = "07/08/2026"
vao = pd.to_datetime(vao_raw)
ra = pd.to_datetime(ra_raw)
print(vao.strftime("%Y-%m-%d"), ra.strftime("%Y-%m-%d"), (ra-vao).days)
```

Cho biết code trên có thể chạy nhưng trả kết quả sai yêu cầu thế nào; sửa hai phép chuyển kiểu và nêu kết quả đúng. Vì sao nhìn thấy YYYY-MM-DD ở output không chứng minh chuỗi đầu vào được đọc đúng? Chỉ riêng `04/08/2026` có xác định được quy ước của một nguồn chưa biết không?

#### B8-039 — Tự luận ngắn

Mỗi hàng là một review, nguồn DD/MM/YYYY, chỉ có ngày. Đã thu đủ **01/04 đến hết30/06/2026**, không có review trong ngày đã thu thì số đếm0. Review cuối xảy ra 29/06; không có review30/06.

```python
rv = pd.DataFrame({"date": ["02/04/2026", "03/04/2026", "04/05/2026",
                            "05/05/2026", "06/06/2026", "29/06/2026"]})
rv["date"] = pd.to_datetime(rv["date"])
m = rv.set_index("date").resample("M").size()
m = m.iloc[:-1]
```

(a) Nêu vấn đề của đọc ngày và API. (b) Sửa hai dòng đầu có vấn đề; thay dòng chọn kỳ cuối bằng điều kiện dựa trên phạm vi đã thu. (c) Đếm tháng 6 trực tiếp bằng mask để đối chiếu; nếu cả tổng số đếm và phép đếm này khớp thì đã chứng minh xu hướng/ nguyên nhân chưa? Nếu dùng AI cho bài tự làm, phần khai báo cần nêu những gì và bạn sẽ tự kiểm kết quả nào ở đây?

#### B8-040 — Tự luận ngắn

Đã thu đủ tháng 1–3 của cả hai năm 2025–2026. Mỗi phần tử là **tổng review một tháng**, theo thứ tự tháng 1,2,3; các vị trí hai Series mô tả tháng tương ứng, không thiếu.

```python
goc = pd.Series([40, 160, 200], index=[1,2,3])
nay = pd.Series([80, 160, 180], index=[1,2,3])
bao_cao = (nay / goc - 1).mean()
```

(a) `bao_cao` cho tỷ lệ nào và đang đặt trọng số lên đối tượng nào? (b) Chỉ thay dòng `bao_cao` để trả lời “tổng quýI/2026 thay đổi bao nhiêu so với tổng quýI/2025”; in phần trăm1 chữ số. (c) Tháng3/2026 giảm so cùng tháng năm trước thì có mâu thuẫn với kết quả tổng quý không? Nêu kỳ gốc của hai phép so.


### A. Câu hỏi tự học bổ sung

#### B8-MR07 — Trắc nghiệm

Nhật ký cùng giờ địa phương không gắn timezone, nguồn YYYY-MM-DD HH:MM, mỗi hàng là một sự kiện. Cần lấy **trọn ngày 15/08/2026**. Hệ thống thu đủ ngày này.

```python
t = pd.Series(pd.to_datetime(["2026-08-15 00:00", "2026-08-15 14:20",
                               "2026-08-15 23:59", "2026-08-16 00:00"]))
```

Mask nào đáp ứng yêu cầu, giữ đúng3 hàng đầu?

**A.** `(t >= "2026-08-15") & (t <= "2026-08-15")`

**B.** `(t >= "2026-08-15") & (t < "2026-08-16")`

**C.** `(t >= "2026-08-15") & (t <= "2026-08-16")`

**D.** `(t > "2026-08-15") & (t < "2026-08-16")`


#### B8-MR08 — Trắc nghiệm

Việt Nam UTC+7; biết31/12/2025 là thứ Tư.

```python
s = pd.Series(pd.to_datetime(["2025-12-31 21:00"], utc=True))
v = s.dt.tz_convert("Asia/Ho_Chi_Minh")
```

Nhận định nào đúng?

**A.** Cần thay convert bằng localize vì s đã có UTC.

**B.** `v` vẫn là 31/12/2025 thứ Tư vì chuyển múi giờ không đổi ngày.

**C.** `v` là 01/01/2026 thứ Năm nhưng là một thời điểm thực muộn hơn s đúng7 giờ.

**D.** `v` là 01/01/2026 04:00 thứ Năm, dayofweek=3; cùng thời điểm thực với s.



## Đợt 5

### A. Câu hỏi trọng tâm

#### B8-041 — Trắc nghiệm

Dữ liệu chỉ có ngày, YYYY-MM-DD. Biết02/07/2026 là thứ Năm.

```python
s = pd.Series(pd.to_datetime(["2026-07-02"], format="%Y-%m-%d"))
print(s.dt.year.iloc[0], s.dt.quarter.iloc[0], s.dt.dayofweek.iloc[0])
```

Dòng cuối in ra gì?

**A.** `2026 2 3`

**B.** `2026 3 3`

**C.** `2026 3 4`

**D.** Báo lỗi vì Series chỉ có một phần tử không dùng được `.dt`.


#### B8-042 — Trắc nghiệm

Snapshot có mốc phân tích29/06/2026, chỉ có ngày review theo YYYY-MM-DD. Nguồn cho biết thu các chỗ ở trong29/06–02/07 nên có một số review ngày 30/06 và01/07 hợp lệ. Nhiệm vụ là phân tích đến hết29/06; **không có thông tin về ngày nhận phòng**.

Nhận định nào đúng?

**A.** Mọi hàng sau29/06 là lỗi nhập và phải sửa thành29/06.

**B.** Ngày30/06 cho biết khách nhận phòng30/06 nên có thể tính số đêm từ đó.

**C.** Có nhãn30/06 sau resample thì được dùng toàn tháng 6 như tháng trọn.

**D.** Giữ dữ liệu gốc, báo số hàng ngoài mốc, rồi lọc ngày hợp lệ trong phạm vi trước khi tổng hợp; chưa đủ cơ sở coi ngày ngoài mốc là lỗi.


#### B8-043 — Trắc nghiệm

Một chuỗi tổng review **theo quý** có mọi quý liên tiếp, index nhãn cuối quý, sắp tăng. Tất cả các quý dùng đều đã thu đủ. Bạn muốn so quýIII/2026 với cùng quý năm trước nhưng dùng `q / q.shift(12) - 1`. Trong phần lịch liên quan, quýIII/2023 có40 review, quýIII/2025 có80, quýIII/2026 có100.

Nhận định nào đúng?

**A.** Code so với quýIII/2025 và cho 25%;12 hàng luôn bằng một năm.

**B.** Code so với quýII/2026 vì shift chỉ lùi một kỳ.

**C.** Code so với quýIII/2023 và cho 150%; sửa thành shift 4 để được25% so quýIII/2025.

**D.** Code so với quýIII/2023 và cho 25%; chỉ cần đổi nhãn kỳ gốc trong báo cáo.


#### B8-044 — Trắc nghiệm

Mỗi hàng sau là một review chỉ có ngày, cùng lịch địa phương, không thiếu. Biết06/07/2026 là thứ Hai,12/07 là Chủ nhật; đã thu đủ 06–19/07.

```python
t = pd.to_datetime(["2026-07-06", "2026-07-12", "2026-07-12", "2026-07-13"])
s = pd.Series(1, index=t).resample("W-SUN").size()
print(s.tolist())
```

Dòng cuối in ra gì? W-SUN gộp tuần kết thúc Chủ nhật.

**A.** `[3, 1]`

**B.** `[1, 3]`

**C.** `[2, 1]`

**D.** `[4]`


#### B8-045 — Trắc nghiệm

Đã thu đủ 01–06/06/2026. Bảng **đã tổng hợp** chỉ ghi ngày có review:02/06 có2,04/06 có4; mọi ngày còn lại trong khoảng thu có0. Dữ liệu chỉ có ngày, không thiếu số đếm. Muốn báo trung bình review **trên mọi ngày đã quan sát**.

Nhận định nào đúng?

**A.** Mẫu số 2 vì có hai hàng tổng hợp; kết quả3 review/ngày.

**B.** Mẫu số 3 vì khoảng giữa02 và04 có ba ngày; kết quả2 review/ngày.

**C.** Mẫu số 6 nhưng tử số 2 là số hàng; kết quả1/3 review/ngày.

**D.** Mẫu số 6 và tử số 6 review; kết quả1 review/ngày.


#### B8-046 — Trắc nghiệm

Chuỗi tổng review nhãn cuối tháng đã sắp. Chỉ tháng 1,3,4,5/2026 đã thu đủ, tháng 2 chưa biết.

```python
s = pd.Series([20, 30, 60, 90], index=pd.to_datetime([
    "2026-01-31", "2026-03-31", "2026-04-30", "2026-05-31"]))
p = s.asfreq("ME").pct_change(fill_method=None)
print(p.loc["2026-03-31"], p.loc["2026-04-30"])
```

Dòng cuối in ra gì, ở dạng tỷ lệ?

**A.** `0.5 1.0`

**B.** `nan 1.0`

**C.** `inf 1.0`

**D.** `nan 100.0`


#### B8-047 — Trắc nghiệm

Nguồn DD/MM/YYYY, chỉ có ngày; None là thiếu từ nguồn. Đây là các lượt lưu trú, không có quy tắc coi thiếu là ở0 đêm.

```python
vao = pd.to_datetime(pd.Series(["01/06/2026", None]), format="%d/%m/%Y")
ra = pd.to_datetime(pd.Series(["03/06/2026", "05/06/2026"]), format="%d/%m/%Y")
dem = (ra - vao).dt.days
```

Nhận định nào đúng?

**A.** `dem` là 2 vàthiếu; thiếu ngày vào không xác định được số đêm hàng 1.

**B.** `dem` là 2 và0 vì NaT là khoảng thời gian bằng 0.

**C.** `dem` là 3 và5 vì cần lấy ngày trong tháng của ngày ra.

**D.** Phải điền ngày vào thiếu bằng ngày ra để tạo số đêm hợp lệ bằng 0.


#### B8-048 — Tự luận ngắn

Các sự kiện có giờ cùng giờ địa phương không gắn timezone. Mỗi phần tử là một review. Nguồn xác nhận đã thu đủ 01–30/06/2026; dữ liệu01/07 chỉ là mẫu một phần, chưa biết đầy đủ.

```python
t = pd.Series(pd.to_datetime(["2026-06-01 09:00", "2026-06-29 20:00",
                               "2026-06-30 00:00", "2026-06-30 18:00",
                               "2026-07-01 00:00"]))
giu = t <= pd.Timestamp("2026-06-30")
```

Sửa mask để lấy mọi review trong **tháng 6 trọn** rồi đếm số hàng. Có nên loại tháng 6 vì thời điểm cắt đang viết là 00:00 hay vì dữ liệu có một hàng tháng 7? Phân biệt lỗi lọc của code với phạm vi thu thập đã được nguồn xác nhận.

#### B8-049 — Tự luận ngắn

`s` là số review trên lịch01–08/06/2026 liên tiếp, index tăng. Các ngày có0 đã thu đủ và không review; riêng03/06 chưa biết số đếm nên NaN.

```python
s = pd.Series([0, 2, float("nan"), 4, 0, 6, 8, 10],
              index=pd.date_range("2026-06-01", periods=8, freq="D"))
tb = s.rolling(7, min_periods=7, center=False).mean().fillna(0)
```

(a) Vì sao điền NaN sau rolling thành0 làm báo cáo sai ý nghĩa? (b) Sửa dòng tính để giữ ý nghĩa yêu cầu đủ 7 giá trị; nêu kết quả07 và08/06 cùng thành phần cửa sổ 08/06. (c) Nếu chủ động đổi yêu cầu thành tối thiểu6 giá trị đã biết, kết quả08/06 là bao nhiêu, và có được gọi đó là trung bình đã biết của đủ 7 ngày không?

#### B8-050 — Tự luận ngắn

Tổng review các tháng sau đã thu đủ, không thiếu ngày. Năm2023 không nhuận;2024 nhuận. Các nhãn là cuối tháng, chỉ có ngày, index tăng.

```python
m = pd.Series([310, 280, 620, 580], index=pd.to_datetime([
    "2023-01-31", "2023-02-28", "2024-01-31", "2024-02-29"]))
```

Gộp cùng tháng qua hai năm. Tính (i) tỷ lệ thay đổi tổng tháng 2 so tháng 1; (ii) tỷ lệ thay đổi review/ngày tháng 2 so tháng 1, mỗi mức gộp bằng tổng review/tổng số ngày. Dùng `.index.days_in_month`; in phần trăm1 chữ số. Vì sao mean hai mức review/ngày tháng 2 của từng năm không cho đúng mức gộp? Nêu tổng số ngày của hai tháng và chiều biến động theo hai cách.


### A. Câu hỏi tự học bổ sung

#### B8-MR09 — Trắc nghiệm

Cần tính cửa sổ theo khoảng3 ngày trên chuỗi số đo tại các ngày không đều. Chưa có ý định bù dữ liệu ở ngày vắng. Nhận định nào phù hợp cách dùng trong bài?

**A.** `rolling("3D")` chỉ cần index là các chuỗi nhìn giống ngày, không cần chuyển kiểu.

**B.** Dùng chỉ mục ngày giờ phù hợp đã sắp theo thời gian; nêu min_periods và biên khi chúng ảnh hưởng câu hỏi.

**C.** Cần xóa mọi hàng trùng ngày trước vì một cửa sổ không được chứa nhiều sự kiện cùng ngày.

**D.** Phải `fillna(0)` và thêm mọi ngày trước khi gọi rolling theo thời gian, dù số liệu các ngày đó chưa biết.


#### B8-MR10 — Tự luận ngắn

Nguồn API ghi **giờ UTC dạng YYYY-MM-DD HH:MM**, chưa có timezone trong kiểu. Mỗi hàng là một review. Nguồn xác nhận đã thu đủ cả ngày 01/01/2027 theo giờ Việt Nam UTC+7; ngày 02/01 chưa biết. Không có review khác trong ngày 01/01 ngoài các hàng đã cho.

```python
raw = pd.Series(["2026-12-31 16:59", "2026-12-31 17:00",
                 "2027-01-01 16:59", "2027-01-01 17:00"])
```

Viết code đổi múi giờ, đếm review ngày 01/01/2027 theo Việt Nam bằng biên phải mở. Cho sẵn lịch hai ngày để lập chuỗi báo cáo: `lich = pd.date_range("2027-01-01", "2027-01-02", tz="Asia/Ho_Chi_Minh", freq="D")`. Kết quả báo cáo phải phân biệt ngày 02/01 chưa biết với ngày đã quan sát. Nêu số review/ngày cho phạm vi **đã thu đủ**. Vì sao không lấy mọi hàng chuyển đổi rồi coi số đếm ngày 02/01 là tổng trọn ngày?


## Đợt 6

### A. Câu hỏi trọng tâm

#### B8-051 — Trắc nghiệm

Nguồn yêu cầu đọc theo **DD/MM/YYYY**; ngày 13 tháng 5 phải ghi `13/05/2026`. Chuỗi `05/13/2026` không hợp lệ theo quy ước nguồn. Cần đánh dấu các chuỗi không đọc được theo **format nguồn**, không chấp nhận tự đổi sang tháng/ngày. Xét độc lập:

```python
raw = pd.Series(["05/13/2026"])
a = pd.to_datetime(raw, dayfirst=True, errors="coerce")
b = pd.to_datetime(raw, format="%d/%m/%Y", errors="coerce")
```

Trong pandas3.0.3, nhận định nào đúng?

**A.** Cả a và b đều là NaT vì dayfirst kiểm định dạng nguồn chặt.

**B.** Cả a và b đều là 13/05 vì format chỉ quyết định cách hiển thị.

**C.** a có thể đọc thành13/05 do ưu tiên ngày trước không cấm cách đọc khác; b là NaT và đáp ứng yêu cầu của đề.

**D.** a là NaT còn b là 13/05 vì format tự đổi vị trí ngày/tháng khi tháng 13 không hợp lệ.


#### B8-052 — Trắc nghiệm

`s` là chuỗi **đã tổng hợp** số review từng ngày có review, index duy nhất tăng dần; đã thu đủ 01–05/06/2026, ngày vắng trong phạm vi này là 0. Không có thông tin ngoài phạm vi.

```python
s = pd.Series([3, 5], index=pd.to_datetime(["2026-06-02", "2026-06-04"]))
t = s.asfreq("D", fill_value=0)
```

Nhận định nào đúng?

**A.** t có nhãn02,03,04/06, giá trị `[3,0,5]`; cần lịch01–05/06 cho sẵn và reindex nếu muốn đủ phạm vi đã thu.

**B.** t tự thêm01 và05/06 vì asfreq biết nguồn đã thu đủ năm ngày.

**C.** t có tổng 2 vì asfreq luôn đếm số hàng gốc như size.

**D.** Nếu đưa bảng nhiều review cùng ngày vào asfreq thì nó tự gộp số review thay resample.


#### B8-053 — Trắc nghiệm

Số review của sáu tháng trọn liên tiếp đã thu đủ là `[18, 2, 8, 9, 10, 11]`, theo thứ tự tháng 1–6/2026. Index tăng, không thiếu. Bạn tính `rolling(3, min_periods=3, center=False).mean()` và thấy cực đại trung bình ở tháng 6, còn cực đại gốc ở tháng 1. Hai cực đại đều duy nhất.

Nhận định nào đúng?

**A.** Rolling dự báo tháng 7 có đúng10 review vì giá trị cuối là 10.

**B.** Cửa sổ cuối `[9,10,11]` có mean 10; đó là mô tả ba tháng đã qua, không tự chứng minh nguyên nhân hoặc số review tháng tới.

**C.** Dữ liệu sai vì cực đại rolling và cực đại gốc buộc phải cùng tháng.

**D.** Hai nhãn cực đại cách5 tháng nên mọi đường rolling3 đều trễ đúng5 tháng.


#### B8-054 — Trắc nghiệm

Chuỗi tổng review sau có lịch tháng liên tiếp, nhãn cuối tháng, sắp tăng; mọi tháng đã thu đủ,0 là không có review.

```python
s = pd.Series(10, index=pd.date_range("2025-01-31", periods=15, freq="ME"))
s.loc[["2025-03-31", "2026-02-28", "2026-03-31"]] = [40, 60, 80]
s.loc["2025-06-30"] = 0
rut = s[s > 0]
```

Tại tháng 3/2026, xét `s/s.shift(12)-1`, `s/s.shift(1)-1` và `rut/rut.shift(12)-1`. Nhận định nào đúng (phần trăm làm tròn1 chữ số)?

**A.** Cả ba đều so cùng tháng năm trước và tăng100,0%.

**B.** Phép đầu tăng33,3% vì kỳ gốc tháng 2/2026; phép thứ hai tăng100,0%.

**C.** Phép trên rut vẫn so tháng 3/2025 vì việc xóa tháng 0 không đổi khoảng12 hàng.

**D.** Phép đầu tăng100,0% so tháng 3/2025; phép thứ hai tăng33,3% so tháng 2/2026; phép trên rut lấy nhầm tháng 2/2025, cho 700,0%.


#### B8-055 — Trắc nghiệm

Chuỗi tổng review bốn tháng trọn liên tiếp, index tăng, đã thu đủ và không thiếu:

```python
s = pd.Series([0, 0, 5, 10],
              index=pd.date_range("2026-01-31", periods=4, freq="ME"))
print(s.pct_change(fill_method=None).tolist())
```

Dòng cuối in ra gì? `inf` là vô cực, không phải tỷ lệ tăng hữu hạn.

**A.** `[nan, nan, inf, 1.0]`

**B.** `[nan, 0.0, 5.0, 1.0]`

**C.** `[0.0, 0.0, 100.0, 100.0]`

**D.** `[nan, nan, 1.0, 1.0]`


#### B8-056 — Trắc nghiệm

Mỗi hàng của `r` là một review, index ngày giờ chỉ có ngày, đã sắp. Nguồn thu đủ 01/2025–12/2026, các ngày không có hàng là 0 review.

```python
r = pd.Series(1, index=pd.to_datetime([
    "2025-01-02", "2025-02-03", "2026-01-04", "2026-01-05"]))
x = r.groupby(r.index.month).size()
```

Yêu cầu báo số review **từng tháng của từng năm**. Nhận định nào đúng?

**A.** x giữ năm vì DatetimeIndex tự thêm năm vào mỗi nhóm month.

**B.** x sai cú pháp vì phải viết `r.index.dt.month`.

**C.** x gộp tháng 1 hai năm thành3; muốn tách năm-tháng có thể dùng resample ME và bổ sung lịch hai đầu đã thu nếu cần cả khoảng.

**D.** Chỉ cần đổi `.size()` thành `.count()` là x sẽ tách được từng năm.


#### B8-057 — Tự luận ngắn

Nguồn DD/MM/YYYY, chỉ có ngày. Đây là **bảng số review đã tổng hợp theo ngày có review**, không phải một hàng một review. Đã thu đủ 01/01 đến hết05/02/2024; trong khoảng này ngày vắng là 0, sau05/02 chưa biết. Tháng1 có31 ngày.

```python
df = pd.DataFrame({"date": ["04/01/2024", "11/01/2024", "03/02/2024", "05/02/2024"],
                   "n": [8, 12, 6, 4]})
df["date"] = pd.to_datetime(df["date"])
m = df.set_index("date")["n"].resample("M").size()
```

(a) Nêu vấn đề đọc ngày/API và đơn vị đang được đếm. (b) Sửa hai dòng để có **tổng review từng tháng trong phần đã quan sát**. (c) Tháng1 và tháng 2 đang chia cho bao nhiêu ngày nếu tính review/ngày? Tính hai mức; có nên gọi biến động tổng tháng 2 là thay đổi của cả tháng trọn không?

#### B8-058 — Tự luận ngắn

Nguồn đã thu đủ 31/12/2024–07/01/2025. Chuỗi sau là số review mỗi ngày trên lịch liên tiếp, sắp tăng, không thiếu. Bài phân tích yêu cầu **chỉ dùng ngày thuộc năm 2025**, không dùng lịch sử năm 2024 để tạo cửa sổ.

```python
s = pd.Series([70, 1, 1, 1, 1, 1, 1, 7],
              index=pd.date_range("2024-12-31", periods=8, freq="D"))
sai = s.rolling(7, min_periods=7, center=False).mean().loc["2025"]
```

Viết cách tính đúng, nêu sáu kết quả đầu và giá trị07/01. Liệt kê cửa sổ dùng cho 07/01, đối chiếu bằng số gốc. Vì sao tính trước rồi lọc năm như code trên không đáp ứng yêu cầu?

#### B8-059 — Tự luận ngắn

Trong một báo cáo dùng **cùng các năm trọn 2022–2025**, tổng review tháng 8 qua các năm là 1500 và trung bình của12 tổng tháng là 1000. Báo cáo gọi `1500/1000*100` là chỉ số tháng 8.

Một kiểm tra bổ sung cung cấp hai hàng tháng trọn cụ thể sau; các giá trị trung bình trượt12 tháng đã được tính đúng từ lịch đầy đủ và được **cho sẵn**, không yêu cầu tính lại:

| Nhãn tháng | Review gốc | Trung bình trượt12 tháng |
|---|---:|---:|
| 2025-07-31 | 180 | 120 |
| 2025-08-31 | 264 | 240 |

Theo quy tắc minh họa của tài liệu, mức điều chỉnh mỗi hàng = review gốc / trung bình trượt12 tháng của hàng đó.

(a) Chỉ số tháng 8 bằngbao nhiêu,100 nghĩa là gì? (b) Tính hai mức điều chỉnh; tháng có review gốc cao hơn có còn có mức điều chỉnh cao hơn không? (c) Hai phép tính khớp quy tắc có chứng minh đã tách hoàn toàn mùa hoặc nguyên nhân không? Nêu ảnh hưởng chưa được giải quyết khi chỉ dùng chỉ số tháng gốc.

#### B8-060 — Tự luận ngắn

API xác nhận các chuỗi là **giờ UTC**, chưa gắn timezone; mỗi hàng là một review. Việt Nam UTC+7. Nguồn đã thu đầy đủ ngày 01/01/2027 theo Việt Nam, không có review nào khác trong ngày này. Các ngày khác không được xác nhận đầy đủ. Biết31/12/2026 là thứ Năm.

```python
raw = pd.Series(["2026-12-31 16:30", "2026-12-31 17:00", "2026-12-31 23:00",
                 "2027-01-01 16:30", "2027-01-01 17:00"])
```

Viết cách đếm review trọn ngày 01/01/2027 theo Việt Nam, nêu các hàng giữ và mức review/ngày trong phạm vi đầy đủ. Xác định ngày/thứ tại Việt Nam của hàng 2. Nếu một bảng khác chỉ có cột ngày review `2027-01-01`, không có giờ hay thông tin múi giờ, có được tự coi đó là 00:00 UTC và đổi ngày theo cùng code không? Giải thích.


### A. Câu hỏi tự học bổ sung

#### B8-MR11 — Trắc nghiệm

Mỗi hàng là một review có thời điểm UTC; Việt Nam UTC+7. Đã thu đủ cả ngày 01/08/2026 tại Việt Nam; không có review khác trong ngày này. Các sự kiện ngoài ngày này không dùng để suy độ đầy đủ.

```python
t = pd.to_datetime(["2026-07-31 18:00", "2026-08-01 01:00",
                    "2026-08-01 17:30"], utc=True)
u = pd.Series(1, index=t).resample("D").size()
v = pd.Series(1, index=t.tz_convert("Asia/Ho_Chi_Minh")).resample("D").size()
```

Nhận định nào đúng?

**A.** u đếm `[1,2]` theo ngày UTC; v đếm `[2,1]` theo ngày Việt Nam. Muốn tổng trọn ngày 01/08 Việt Nam phải dùng số 2 ởv.

**B.** u và v đều đếm `[1,2]`, vì convert giữ nguyên thời điểm thực nên giữ nguyên nhóm ngày.

**C.** v đếm `[3]`, vì tất cả giờ UTC phải cộng vào cùng ngày 01/08.

**D.** Cần thay convert bằng localize Việt Nam để resample biết dời ngày.


#### B8-MR12 — Tự luận ngắn

Mỗi chuỗi dưới là thời điểm một review theo UTC; Việt Nam UTC+7. Nguồn đã thu đủ 30/06–04/07/2026 theo Việt Nam, không có review khác; ngày vắng trong khoảng là 0. Không có thiếu nguồn.

```python
raw = ["2026-06-29 18:00", "2026-06-30 18:00",
       "2026-07-02 17:00", "2026-07-03 18:00"]
lich = pd.date_range("2026-06-30", "2026-07-04", freq="D", tz="Asia/Ho_Chi_Minh")
```

Sau khi đổi về Việt Nam, cần hai đại lượng:
(a) Tổng review trong khoảng3 ngày kết thúc **đúng00:00 ngày 03/07**, biên `(t-3D,t]`, giữ giờ sự kiện gốc.
(b) Tổng review của **ba ngày lịch nguyên01,02,03/07**, lấy trọn ngày 03/07, tính từ chuỗi đếm ngày đầy đủ bằng rolling3 hàng, min_periods=3, center=False.

Viết code ngắn cho hai giá trị, liệt kê sự kiện/ngày thuộc mỗi cửa sổ và giải thích vì sao kết quả khác nhau không mâu thuẫn. Không dùng kết quả(a) như thể đã mô tả trọn ba ngày lịch của(b).
