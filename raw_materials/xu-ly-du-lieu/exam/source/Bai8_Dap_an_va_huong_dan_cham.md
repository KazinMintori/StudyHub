# Bài 8 — Đáp án và hướng dẫn chấm 72 câu

Đối chiếu theo mã với [file câu hỏi](D:/LTXLDL_GK/output/bai8/Bai8_72_cau_hoi.md). TN chấm 1 điểm khi chọn đúng duy nhất một đáp án; TL dùng thang tham khảo 5 điểm mỗi câu. Không cộng thành tỷ trọng đề thi chính thức. Với TL, chấp nhận code/cách tính đúng tương đương; lỗi tính riêng không tự mất điểm phần giải thích đúng. Không trừ điểm vì chọn count khi cột không thiếu và phép đếm đáp ứng câu hỏi.

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

## Kiểm chứng thực tế

Đã chạy **72 ca kiểm chứng độc lập**, một ca cho mỗi câu, bằng Python 3.12.14 và pandas **3.0.3**; 72/72 PASS. Mỗi ca dựng lại dữ liệu riêng và dùng assert đối chiếu ngày/NaT, lịch, cửa sổ, kỳ gốc hoặc kết quả phù hợp. Các câu cố ý gây lỗi được kiểm loại lỗi, không so nguyên văn thông báo. Các nhận định về phạm vi nguồn, nhân quả và tính hợp lý của lựa chọn được rà bằng suy luận; việc assert chạy qua không được coi là chứng minh các nhận định ấy.

Không tuyên bố đã chạy toàn bộ notebook với snapshot thật. Đã tính tay lại trên bảng nhỏ; kiểm trực tiếp mask tháng/quý; kiểm tổng số đếm với hàng hợp lệ hoặc tổng số review của bảng đếm; kiểm hai mốc29/06 và30/06; thử ngày/tháng vắng và giá trị0/NaN. Phần code lời giải thay các dòng tương ứng rồi chạy lại từ đầu trên khởi tạo của câu.

## Tra cứu đáp án trắc nghiệm

| Đợt | Trọng tâm | Bổ sung |
|---|---|---|
| 1 | B8-001: **B**; B8-002: **D**; B8-003: **C**; B8-004: **A**; B8-005: **B**; B8-006: **C**; B8-007: **D** | B8-MR01: **D** |
| 2 | B8-011: **C**; B8-012: **A**; B8-013: **D**; B8-014: **B**; B8-015: **A**; B8-016: **D**; B8-017: **C** | B8-MR03: **A**; B8-MR04: **C** |
| 3 | B8-021: **A**; B8-022: **C**; B8-023: **B**; B8-024: **D**; B8-025: **C**; B8-026: **B** | B8-MR05: **C** |
| 4 | B8-031: **D**; B8-032: **B**; B8-033: **A**; B8-034: **C**; B8-035: **D**; B8-036: **A**; B8-037: **B** | B8-MR07: **B**; B8-MR08: **D** |
| 5 | B8-041: **B**; B8-042: **D**; B8-043: **C**; B8-044: **A**; B8-045: **D**; B8-046: **B**; B8-047: **A** | B8-MR09: **B** |
| 6 | B8-051: **C**; B8-052: **A**; B8-053: **B**; B8-054: **D**; B8-055: **A**; B8-056: **C** | B8-MR11: **A** |

## Đợt 1 — B. Đáp án và hướng dẫn chấm

### Trọng tâm

#### B8-001

**Đáp án B.** A đảo ngày/tháng theo MM/DD/YYYY. B đúng: 04/09 là ngày 4 tháng 9, 09/04 là ngày 9 tháng 4. C áp tháng của hàng đầu cho mọi hàng. D sai: `format` đã xác định cách đọc; tính mơ hồ khi chưa biết nguồn không làm hai ngày hợp lệ phát sinh lỗi. `%d` là ngày, `%m` là tháng, `%Y` là năm bốn chữ số. Không có giá trị thiếu.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K02. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Đảo ngày/tháng dù cả hai đều hợp lệ. Tham chiếu cách hỏi: GK26(a).

**Đọc lại:** G §1; L ô 6–10.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-002

**Đáp án D.** Lịch ngày là 01, 02, 03, 04/08 với số review `[2,2,0,1]`. Kỳ gốc của 02/08 là 01/08: `2/2-1=0`; của 03/08 là 02/08: `0/2-1=-1`. A đã nhân phần tử giảm với 100 dù đề cần tỷ lệ. B bỏ qua ngày có số đếm 0. C dùng `kỳ này/kỳ gốc` mà quên trừ 1 ở ngày thứ hai. D đúng. Ngày đầu thiếu vì chưa có kỳ gốc; 03/08 là 0 đã biết, không phải ngày chưa thu thập.

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K12; phụ K14, K21. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Bỏ ngày 0; nhầm tỷ lệ với phần trăm.

**Đọc lại:** L ô 39–44, 67–69; GK câu 19.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-003

**Đáp án C.** Giờ Việt Nam là 02:15 ngày 01/01/2027, thứ Sáu; `dayofweek=4` vì thứ Hai bằng 0. A giữ nguyên ngày giờ UTC. B đếm thứ Hai bằng 1. C đúng. D chỉ đổi thứ nhưng giữ sai tháng và năm. `tz_convert` giữ cùng thời điểm thực, thay cách biểu diễn theo múi giờ.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29; phụ K06. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Đổi múi giờ nhưng quên đổi ngày, năm hoặc quy ước thứ.

**Đọc lại:** L ô 26–28; GK câu 20.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-004

**Đáp án A.** Có ba review tháng 3: id 12, 11, 13. A đúng. B đếm hai ngày khác nhau thay vì review. C không lọc tháng và tính cả 28/02. D sai vì DatetimeIndex cho phép trùng ngày. Ngày review không tự là ngày booking/nhận phòng; không xóa hai review ngày 03/03 chỉ vì cùng ngày.

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K08; phụ K09. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Nhầm nhiều sự kiện cùng ngày với bản ghi trùng cần xóa.

**Đọc lại:** L ô 30–38.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-005

**Đáp án B.** Cửa sổ cuối chứa các nhãn 28/02, 31/03, 30/04 với giá trị `[18,12,24]`; tổng 54, trung bình 18 review/tháng. A dùng cửa sổ trước. B đúng. C nhầm `mean` thành `sum`. D nhầm nhãn cuối cửa sổ với toàn bộ dữ liệu dùng để tính. Hai kết quả đầu là NaN vì chưa đủ ba giá trị không thiếu.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K16; phụ K17. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm nhãn gắn kết quả, cửa sổ hoặc sum/mean.

**Đọc lại:** L ô 51–56.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-006

**Đáp án C.** `shift(1)` ở đây dịch giá trị xuống một hàng, giữ nhãn. Tháng 3 nhận 10 của tháng 2, chỉ mục không đổi. A không dịch giá trị. B đọc giá trị hàng sau và cho rằng nhãn cũng dịch. C đúng. D có giá trị đúng nhưng hiểu sai việc giữ nhãn. Hàng đầu của `p` thiếu kỳ gốc.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K20. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Coi shift không có freq là dịch nhãn ngày.

**Đọc lại:** L ô 59–64.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-007

**Đáp án D.** R3 chứa ngày không tồn tại, còn R2 đã thiếu từ nguồn. Cả hai thành NaT nhưng chỉ R3 thỏa `raw.notna() & parsed.isna()`. A chỉ nhìn cột đã chuyển và gộp mọi nguyên nhân thiếu. B coi coerce đã sửa được ngày sai. C chỉ đánh dấu thiếu nguồn, ngược mục tiêu. D đúng. `coerce` tạo dấu thiếu để tiếp tục xử lý, không khôi phục ngày đúng.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K04. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Chỉ nhìn cột đã đổi kiểu để giải thích mọi NaT.

**Đọc lại:** L ô 11–15; Lab ô 5–9.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-008

```python
vao = pd.to_datetime(dat["vao"], format="%d/%m/%Y", errors="coerce")
ra = pd.to_datetime(dat["ra"], format="%d/%m/%Y", errors="coerce")
so_dem = (ra - vao).dt.days
loi_vao = dat["vao"].notna() & vao.isna()
```

Số đêm D1=2, D2=3, D3 và D4 thiếu. D3 là lỗi ngày không tồn tại; D4 thiếu từ nguồn. `loi_vao` chỉ đúng ở D3. Thiếu một toán hạng hợp lệ khiến hiệu là NaT, số ngày là thiếu, không phải khoảng thời gian 0. Giữ dữ liệu gốc để truy vết; 0 đêm sẽ là một giá trị đã biết khác về ý nghĩa.

**Chấm 5 điểm:** đổi đúng cả hai cột, có format và coerce (1,5); hiệu và `.dt.days` đúng (1); kết quả 2,3, thiếu, thiếu (1); mask đúng (1); giải thích không điền 0 (0,5). Chấp nhận cách tương đương, không buộc đúng tên biến trung gian.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K05; phụ K04, K07. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** NaT bị đổi thành 0 đêm; quên năm nhuận hoặc ranh giới năm.

**Đọc lại:** Lab ô 5–9; L ô 19–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-009

```python
goc = pd.Series([20, 180])
nay = pd.Series([40, 198])
doi_tong = nay.sum() / goc.sum() - 1
print(f"{doi_tong:.1%}")
```

Tổng kỳ này 238, tổng kỳ gốc 200; tăng 19,0%. Tỷ lệ tháng là 100% và 10%; trung bình không trọng số là 55%. Tỷ lệ của tổng dùng trọng số theo số review kỳ gốc (20/200, 180/200), không cho mỗi tháng cùng trọng số. Kỳ gốc là tổng tháng 1–2/2025; mẫu số 200 review. Hai giai đoạn đầy đủ và tương ứng, nhưng số review không xác định nguyên nhân biến động; cần bằng chứng khác về quảng cáo.

**Chấm 5 điểm:** xác định hai tổng và kỳ gốc (1); công thức/code và 19,0% (1,5); giải thích 55% cùng trọng số tháng khác với tỷ lệ tổng (1,5); giới hạn kết luận nguyên nhân (1).

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K24; phụ K23. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Trung bình tỷ lệ thay đổi thay cho tỷ lệ của tổng; so cùng kỳ thành kết luận nhân quả.

**Đọc lại:** G §3 Bài tập 3; L ô 82–83.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-010

```python
rv["ngay"] = pd.to_datetime(rv["ngay"], format="%d/%m/%Y")
thang = rv.set_index("ngay").sort_index().resample("ME").size()
tron = thang.loc[thang.index <= pd.Timestamp("2026-05-31")]
tang_tron = tron.pct_change(fill_method=None)
```

(a) Bỏ format có thể đọc 05/04 thành 4/5 theo tháng/ngày; các chuỗi trong bảng đều có thể bị đọc nhầm mà vẫn là ngày hợp lệ. (b) Dùng `%d/%m/%Y`, đổi `M` sang `ME`. (c) Nhãn 30/06 chỉ là nhãn: số đếm `[2,2,2]` gồm tháng 4 trọn, tháng 5 trọn và 01–12/06. Tỷ lệ tháng 6 là `2/2-1=0`, so 12 ngày tháng 6 với toàn tháng 5 (31 ngày), không đủ cơ sở kết luận xu hướng tháng trọn. Bỏ tháng 6 theo phạm vi đã biết hoặc so 01–12/06 với 01–12/05 và ghi rõ giới hạn; không coi ngày 13–30/06 là 0.

**Chấm 5 điểm:** nhận diện lỗi đọc ngày (1); sửa format (1); sửa ME (1); nêu tháng 6 chưa trọn, kỳ gốc tháng 5 và mẫu số 2 review (1); cách chọn kỳ/phạm vi tương ứng và giới hạn kết luận (1).

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K12; phụ K02, K11. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Cấu trúc (a)(b)(c) gần GK26; API cũ, ngày mơ hồ và kỳ chưa trọn.

**Đọc lại:** L ô 23–25,39–47; GK câu 26.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.


### Tự học bổ sung

#### B8-MR01

**Đáp án D.** `a` lấy ba hàng 01,04,08/06, tổng 15; `b` ở 08/06 lấy khoảng `(05/06 00:00,08/06 00:00]`, chỉ có 7. A coi ba hàng là ba ngày. B áp cửa sổ thời gian cho cả `a`. C lấy hai hàng gần nhất dù 04/06 nằm ngoài ba ngày. D đúng. Hai lệnh có cùng min_periods nên khác biệt do thành phần cửa sổ, không do điều kiện đủ dữ liệu.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K31; phụ K16. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Đồng nhất cửa sổ số hàng và số ngày.

**Đọc lại:** L ô 88–89.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-MR02

```python
u = pd.to_datetime(raw, format="%Y-%m-%d %H:%M").dt.tz_localize("UTC")
v = u.dt.tz_convert("Asia/Ho_Chi_Minh")
dau = pd.Timestamp("2026-07-01", tz="Asia/Ho_Chi_Minh")
cuoi = pd.Timestamp("2026-07-02", tz="Asia/Ho_Chi_Minh")
giu = (v >= dau) & (v < cuoi)
so = int(giu.sum())
```

Giờ Việt Nam lần lượt 30/06 23:30, 01/07 00:00, 01/07 17:00, 02/07 00:00; giữ hàng 1,2, số review=2. Localize trực tiếp sang Việt Nam sẽ coi giờ UTC trên mặt đồng hồ là giờ Việt Nam, gán sai thời điểm thực. Dùng `.dt` vì đây là Series. Mẫu số nếu tính review/ngày cho phạm vi này là một ngày đã thu đủ.

**Chấm 5 điểm:** parse và localize UTC (1); convert Việt Nam (1); hai mốc cùng timezone và phải mở (1,5); hàng 1,2 và số đếm 2 (1); giải thích gán sai thời điểm (0,5).

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29; phụ K30, K13. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Gắn sai múi giờ nguồn; lấy ngày theo UTC hoặc bỏ sự kiện cuối ngày.

**Đọc lại:** L ô 86–91.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

### C. Cập nhật độ bao phủ sau đợt 1

Đã hoàn thành **10/60 trọng tâm** (7 TN, 3 TL) và **2/12 bổ sung** (1 TN, 1 TL).

Số câu trọng tâm đã có theo nhóm 1–6: 3 / 1 / 2 / 1 / 2 / 1.

Mục tiêu đã được dùng trong yêu cầu trả lời: K02, K04, K05, K06, K07, K08, K09, K11, K12, K13, K14, K16, K17, K20, K21, K23, K24, K29, K30, K31.

Mục tiêu chưa dùng tới đợt này và mã câu bù đã lên kế hoạch:

- K01: Chuỗi khác ngày giờ; không trừ chuỗi; sắp DD/MM khác thứ tự thời gian; sẽ kiểm ở B8-011.
- K03: Bỏ format có thể sai không lỗi; dayfirst là ưu tiên, không kiểm chặt mọi định dạng; sẽ kiểm ở B8-016, B8-038, B8-051.
- K10: Lọc trước tổng hợp; theo dõi hàng ngoài mốc/NaT; ngoài mốc chưa là lỗi nhập; sẽ kiểm ở B8-018, B8-042, B8-048, B8-058.
- K15: Lịch cho sẵn, reindex; asfreq cho chuỗi đã tổng hợp, không gộp sự kiện/không tự mở hai đầu; sẽ kiểm ở B8-013, B8-028, B8-046, B8-MR10, B8-052.
- K18: Cửa sổ bảy ngày gồm t và sáu ngày trước; không dùng tương lai; đối chiếu gốc; sẽ kiểm ở B8-029, B8-049, B8-058, B8-MR12.
- K19: idxmax khác max và cực đại gốc; trễ không cố định; làm mượt không dự báo/nhân quả; sẽ kiểm ở B8-023, B8-029, B8-053.
- K22: Cùng kỳ: shift 12 tháng, shift 4 quý; periods đúng tần suất và lịch; sẽ kiểm ở B8-030, B8-043, B8-054.
- K25: month bỏ năm; gộp mùa có chủ ý; cùng số năm đóng góp, tránh năm chưa trọn; sẽ kiểm ở B8-020, B8-056, B8-059.
- K26: Chỉ số 100=mức trung bình; chưa loại xu hướng/số ngày; hiểu quy tắc chia trung bình trượt; sẽ kiểm ở B8-020, B8-059.
- K27: days_in_month có năm nhuận; tổng tháng khác review/ngày; mẫu số mọi ngày đã quan sát; sẽ kiểm ở B8-015, B8-034, B8-037, B8-045, B8-050, B8-060.
- K28: Gộp nhiều năm: tổng review/tổng ngày; không chia ngày một năm hoặc mean các mức ngày; sẽ kiểm ở B8-034, B8-050.
- K32: Kiểm bằng mask tháng/quý, tổng số đếm, cửa sổ gốc, kỳ gốc; assert không chứng minh nhân quả; sẽ kiểm ở B8-029, B8-030, B8-039, B8-049, B8-059.

Còn các biến thể: scalar/nhãn tháng (012), tháng thiếu (013), năm đóng góp không đều (020), min_periods có NaN (014), lịch ở hai đầu (028), cùng kỳ quý (030), tổng/ngày nhiều năm (034,050), biên giờ (048), dayfirst không kiểm chặt (051).


## Đợt 2 — B. Đáp án và hướng dẫn chấm

### Trọng tâm

#### B8-011

**Đáp án C.** Sắp từ điển xét ký tự đầu nên thứ tự là 02/12,03/02,15/01; thứ tự thời gian là 15/01,03/02,02/12. Trừ hai chuỗi báo TypeError. A coi chuỗi tự là ngày giờ. B lấy thứ tự thời gian cho một phép sắp chuỗi. C đúng. D tự diễn giải phần năm rồi tạo khoảng 0 không có căn cứ. Cần parse theo `%d/%m/%Y`, sau đó mới sắp và trừ hai Timestamp để được Timedelta.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K01; phụ K07. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Đồng nhất sắp văn bản với sắp thời gian và trừ chuỗi.

**Đọc lại:** L ô 6–7,19–22.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-012

**Đáp án A.** Nhãn đầy đủ khớp duy nhất một phần tử nên lấy số 12; nhãn tháng là chọn một khoảng nên vẫn là Series. B bỏ qua kiểu chọn rút gọn. C suy mọi truy cập DatetimeIndex đều trả Series. D đảo ngược hai cơ chế. Kết luận về scalar dựa trên index duy nhất và độ chính xác đã cho; không áp máy móc khi index trùng hoặc có nhiều thời điểm trong một ngày.

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K08. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Một hàng được chọn không đồng nghĩa luôn trả scalar.

**Đọc lại:** L ô 70–72.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-013

**Đáp án D.** Trước chuẩn lịch, hàng trước tháng 3 là tháng 1 nên `a=12`. `asfreq('ME')` thêm tháng 2 với NaN; sau dịch, tháng 3 nhận NaN. A coi asfreq không thêm nhãn. B và C đồng nhất chưa thu thập với 0 review. D đúng. Không được điền 0 cho tháng 2 khi chưa biết dữ liệu; asfreq chỉ đưa chuỗi đã tổng hợp về lịch giữa hai đầu, không suy ra số review.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K20; phụ K15, K14. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Hàng trước không luôn là tháng trước; chưa biết không phải 0.

**Đọc lại:** L ô 62–66.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-014

**Đáp án B.** Cửa sổ cuối 03–05/06 chứa `[NaN,4,6]`, chỉ hai giá trị không thiếu, không đạt min_periods=3. A ngầm thay NaN bằng 0. B đúng. C áp phép bỏ thiếu của mean nhưng bỏ qua min_periods. D thay kết quả chưa biết bằng 0. 0 ở 02/06 là một giá trị hợp lệ được đếm; vấn đề ở đây là NaN ngày 03/06.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K17; phụ K16. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Đủ k hàng bị hiểu là đủ k giá trị không thiếu.

**Đọc lại:** L ô 51–53; Lab ô 21–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-015

**Đáp án A.** DatetimeIndex có `.days_in_month` trực tiếp, trả 28 và 29, kể cả năm nhuận. A đúng. B mặc định tháng 2 luôn 28 ngày. C mặc định cả hai năm có 29 ngày. D báo tổng review như mức review/ngày, chưa chia số ngày. Các mẫu số là mọi ngày của từng tháng đã thu đủ, không phải số ngày có review.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K27; phụ K06. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Quên năm nhuận hoặc nhầm tổng với mức mỗi ngày.

**Đọc lại:** Lab ô 34–36.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-016

**Đáp án D.** `a` và `b` đều là 06/08 và 11/08/2026 (tháng 8). A đánh dấu sai một cách thực sự đáp ứng đề. B sai vì 06/08 cũng hợp lệ theo MM/DD nên cần quy ước nguồn. C nhầm cách hiển thị với cách diễn giải chuỗi. D đúng. `dayfirst=True` là ưu tiên; không suy từ ví dụ này rằng nó sẽ kiểm chặt mọi yêu cầu về định dạng. Khi yêu cầu chặt, cần nêu và kiểm quy tắc tương ứng.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K03; phụ K02. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Coi dayfirst luôn sai; suy quy ước chỉ từ một ngày mơ hồ/cách hiển thị.

**Đọc lại:** G §1; L ô 8–10,23–25,84.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-017

**Đáp án C.** Kỳ này 50 review, kỳ gốc 40 review, `p=50/40-1=0.25`. A in `0.2%` theo quy tắc làm tròn của định dạng trong trường hợp này, vì thêm dấu % không tự đổi đơn vị. B in `2500.0%`, nhân 100 hai lần. C định dạng tỷ lệ thành phần trăm một lần. D in `125.0%`, là mức kỳ này bằng bao nhiêu phần trăm kỳ gốc, khác phần trăm tăng.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K21. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhân 100 hai lần hoặc nhầm tỷ số mức với tỷ lệ tăng.

**Đọc lại:** L ô 67–72; AI5 câu 4.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-018

```python
d = pd.to_datetime(raw["date"], format="%Y-%m-%d", errors="coerce")
loi = raw["date"].notna() & d.isna()
ngoai = d.notna() & ((d < "2026-06-01") | (d > "2026-06-29"))
giu = d.notna() & (d >= "2026-06-01") & (d <= "2026-06-29")
r = raw.assign(ngay=d).loc[giu].set_index("ngay").sort_index()
```

Giữ 3 hàng (id 2,1,3 theo ngày; không yêu cầu thứ tự hai hàng cùng ngày). Ngoài phạm vi có 1 hàng id4; lỗi đọc 1 hàng id6; thiếu nguồn 1 hàng id5. Hai hàng không có ngày hợp lệ được loại khỏi phân tích ngày và báo riêng, không coi là “sau mốc”. Không xóa review cùng ngày; ngày trùng không chứng minh cùng một sự kiện. Ngày 30/06 chưa tự là lỗi nhập, chỉ ngoài phạm vi đang xét.

**Chấm 5 điểm:** parse và giữ raw, phân loại thiếu/lỗi (1,5); mask trong/ngoài với ngày hợp lệ (1); index/sort đúng (1); bốn số đếm đúng (1); không xóa ngày trùng và không kết luận ngoài mốc là sai (0,5).

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K10; phụ K09, K04. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Mất truy vết NaT; xóa review trùng ngày; đồng nhất ngoài phạm vi với lỗi nguồn.

**Đọc lại:** L ô 30–38,84–85; Lab ô 12–13.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-019

```python
rv["ngay"] = pd.to_datetime(rv["ngay"], format="%d/%m/%Y")
q = rv.set_index("ngay").sort_index().resample("QE").size()
tron = q.loc[q.index <= pd.Timestamp("2026-06-29")]
assert q.sum() == len(rv)
```

(a) Bỏ format có thể đảo ngày/tháng; `Q` không dùng trong pandas 3, cần `QE`. (b) Nhãn quý 31/03 và 30/06 có số đếm `[3,3]`; chỉ quý I được giữ. (c) Quý I đã quan sát 90 ngày, quý II mới có `30+31+29=90` ngày, chưa đủ 91 ngày của quý. Hai số đếm bằng nhau và hai khoảng tình cờ cùng 90 ngày không chứng minh quý II trọn hoặc xu hướng ổn định. Mẫu số của tỷ lệ hiện tại là 3 review quý I; chưa biết tổng quý II. Nếu báo hai giai đoạn 90 ngày, phải ghi rõ phạm vi, không gọi là so hai quý trọn.

**Chấm 5 điểm:** hai vấn đề (1); sửa format/QE (1,5); chọn quý I theo mốc (0,5); 90/90 ngày và đối chiếu tổng 6 review (1); giới hạn kết luận, không suy đủ kỳ từ nhãn (1).

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K12; phụ K11, K02. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Cấu trúc GK26; nhãn quý II bị hiểu đã đủ 30/06; khớp tổng bị hiểu thành chứng minh xu hướng.

**Đọc lại:** Lab ô 14–20; L ô 39–47; GK26.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-020

Chỉ dùng 2024–2025 để mỗi tháng cùng đóng góp từ hai năm. Tháng 1: `20+40=60`; tháng 2: `30+30=60`; mỗi tháng khác `30+30=60`, nên trung bình 12 tổng là 60 và hai chỉ số đều 100.

```python
dem = pd.Series([60] * 12, index=range(1, 13))
chi_so = dem / dem.mean() * 100
```

`.month` bỏ năm: phù hợp mục tiêu gộp tháng số, sai nếu cần tách từng tháng của từng năm. Dùng 2026 khiến tháng 1–2 có ba năm đóng góp nhưng tháng 3–12 chỉ hai năm, không so tương ứng. Chỉ số còn chịu xu hướng dài hạn và độ dài tháng; chưa thể gọi là thành phần mùa đã tách xu hướng hoặc giải thích nguyên nhân.

**Chấm 5 điểm:** chọn hai năm trọn và nêu chênh số năm nếu thêm 2026 (1,5); tổng 60/60, trung bình 60 và chỉ số 100/100 (1,5); ý nghĩa mất năm/có chủ ý theo mục tiêu (1); hai giới hạn xu hướng và số ngày (1).

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K25; phụ K26, K23. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Gộp số năm không đều; chỉ số 100 bị hiểu là đã loại xu hướng và số ngày.

**Đọc lại:** L ô 77–80.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.


### Tự học bổ sung

#### B8-MR03

**Đáp án A.** Tại 04/08 12:00 cửa sổ là `(01/08 12:00,04/08 12:00]`; loại đúng điểm biên trái có giá trị2, giữ 5,7,11, tổng 23. A đúng. B đóng cả hai biên, cộng thêm2. C bỏ nhầm hàng ngày 02 vì đếm ba ngày theo nhãn không theo giờ. D chỉ lấy thời điểm cuối. Không có bù 0 cho những thời điểm không xuất hiện.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K31. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Lấy cả điểm đúng biên trái của cửa sổ phải đóng.

**Đọc lại:** L ô 88–89.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-MR04

**Đáp án C.** Với cửa sổ số hàng 3, default min_periods=3 nên a đầu thiếu. Với cửa sổ thời gian3D, default min_periods=1 nên b đầu=2, cửa sổ chỉ chứa hàng 01/06. A áp mặc định1 cho cả hai. B áp mặc định3 cho cả hai. C đúng. D đảo ngược mặc định. Muốn chỉ kiểm sự khác nhau giữa hàng và thời gian thì nên đặt cùng min_periods như MR01.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K31; phụ K17. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm mặc định min_periods giữa hai loại cửa sổ.

**Đọc lại:** L ô 52,88–89.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

### C. Cập nhật độ bao phủ sau đợt 2

Đã hoàn thành **20/60 trọng tâm** (14 TN, 6 TL) và **4/12 bổ sung** (3 TN, 1 TL).

Số câu trọng tâm đã có theo nhóm 1–6: 5 / 3 / 3 / 2 / 5 / 2.

Mục tiêu đã được dùng trong yêu cầu trả lời: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K20, K21, K23, K24, K25, K26, K27, K29, K30, K31.

Mục tiêu chưa dùng tới đợt này và mã câu bù đã lên kế hoạch:

- K18: Cửa sổ bảy ngày gồm t và sáu ngày trước; không dùng tương lai; đối chiếu gốc; sẽ kiểm ở B8-029, B8-049, B8-058, B8-MR12.
- K19: idxmax khác max và cực đại gốc; trễ không cố định; làm mượt không dự báo/nhân quả; sẽ kiểm ở B8-023, B8-029, B8-053.
- K22: Cùng kỳ: shift 12 tháng, shift 4 quý; periods đúng tần suất và lịch; sẽ kiểm ở B8-030, B8-043, B8-054.
- K28: Gộp nhiều năm: tổng review/tổng ngày; không chia ngày một năm hoặc mean các mức ngày; sẽ kiểm ở B8-034, B8-050.
- K32: Kiểm bằng mask tháng/quý, tổng số đếm, cửa sổ gốc, kỳ gốc; assert không chứng minh nhân quả; sẽ kiểm ở B8-029, B8-030, B8-039, B8-049, B8-059.

Còn các biến thể: .days và ngày thực có giờ (021,027), sum bảng đếm (022), cực đại rolling/bảy ngày (023,029), kỳ trọn không có sự kiện cuối (025), lịch hai đầu (028), cùng kỳ quý (030), count trên cột không thiếu (032), giữ tháng cuối (039), trọng số ngày nhiều năm (050).


## Đợt 3 — B. Đáp án và hướng dẫn chấm

### Trọng tâm

#### B8-021

**Đáp án A.** Hiệu hai Timestamp là Timedelta scalar, từ30/12 đến02/01 là 3 ngày, dùng `.days` trực tiếp. A đúng. B nhầm khoảng thời gian với thời điểm. C bỏ mất một ngày ở ranh giới năm. D áp accessor dành cho Series cho một scalar; Series khoảng thời gian mới dùng `.dt.days`.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K07; phụ K06. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Nhầm Timestamp/Timedelta hoặc .days/.dt.days.

**Đọc lại:** L ô 19–22.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-022

**Đáp án C.** Tổng4+2+6=12 review. A đếm3 hàng trong bảng tổng hợp. B đếm3 giá trị không thiếu. C đúng. D trả4 review trên một ngày có review, không phải tổng 12 hay trung bình trên mọi ngày đã quan sát. Với lịch đầy đủ bốn ngày `[4,0,2,6]`, review/ngày là 3. Nhãn30/09 không biến 4 ngày này thành cả tháng trọn.

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K13; phụ K14. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Dùng size/count trên bảng số đếm thay vì cộng review.

**Đọc lại:** L ô 39–50.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-023

**Đáp án B.** Các trung bình đủ cửa sổ kết thúc03–06/06 là 20/3,17/3,9,19/3. Cực đại tại05/06, từ cửa sổ 03–05/06 `[8,9,10]`. A dùng cực đại gốc ngày 01 có12. B đúng. C lấy nhãn cực đại rolling nhưng giá trị gốc 10 thay mean 9. D gắn trung bình vào giữa cửa sổ dù center=False. `idxmax` trả nhãn; `max` trả giá trị9 review/ngày trong cửa sổ.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K19; phụ K16. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm nhãn/giá trị cực đại rolling với cực đại ngày gốc.

**Đọc lại:** Lab ô 21–28; L ô 51–57.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-024

**Đáp án D.** Chênh100−80=20 review; tăng `(100−80)/80=0.25=25%`; tỷ số 100/80=1.25=125%. A chia chênh cho kỳ hiện tại100, sai kỳ gốc. B đảo tỷ lệ tăng và tỷ số mức. C dùng tỷ lệ như số review. D đúng. Mẫu số so sánh là 80 review tháng 4, không phải100 và không phải số ngày.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K21; phụ K23. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Nhầm chênh tuyệt đối, tỷ lệ tăng và tỷ số mức.

**Đọc lại:** L ô 67–76.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-025

**Đáp án C.** A nhầm ngày sự kiện cuối với ngày quan sát cuối. B xóa máy móc kỳ cuối đã trọn. C đúng vì đã xác nhận thu đủ cả30/06 và 0 là đã biết. D dựa nhãn tổng hợp để suy độ đầy đủ; cùng nhãn30/06 vẫn có thể là quý thiếu dữ liệu nếu nguồn dừng sớm. Không cần có sự kiện ở ngày cuối mới gọi là đã quan sát ngày đó.

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K11; phụ K14. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Luôn bỏ kỳ cuối; dùng sự kiện cuối hoặc nhãn để suy độ đầy đủ.

**Đọc lại:** L ô 45–47; Lab ô 18–20.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-026

**Đáp án B.** A gọi convert trên dữ liệu naive nên lỗi. B gắn quy ước nguồn UTC rồi đổi biểu diễn cùng thời điểm sang Việt Nam:02/07 03:00 và02/07 08:00. C gán các giờ trên mặt đồng hồ thành giờ Việt Nam nên sai thời điểm. D localize lần hai trên dữ liệu đã aware nên lỗi. `.dt` cần thiết để xử lý các giá trị của Series; không tự gán UTC nếu nguồn chỉ đưa ngày thuần và không nói múi giờ.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Nhầm gắn quy ước nguồn và đổi cách biểu diễn.

**Đọc lại:** L ô 26–28,86–87.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-027

```python
vao = pd.to_datetime(dat["vao"], format="%Y-%m-%d %H:%M", errors="coerce")
ra = pd.to_datetime(dat["ra"], format="%Y-%m-%d %H:%M", errors="coerce")
khoang = ra - vao
ngay_thuc = khoang.dt.total_seconds() / 86400
ngay_nguyen = khoang.dt.days
```

Hai hiệu đầu là 36 giờ=1,50 ngày và30 giờ=1,25 ngày; `.dt.days` trả1 và1, chỉ phần ngày nguyên, không phải số ngày thập phân. Hàng2 thiếu từ nguồn nên hiệu là NaT, số ngày thiếu. Hiệu của hai Timestamp scalar dùng `.days` hoặc `.total_seconds()` trực tiếp; các cột ở đây là Series nên dùng `.dt`.

**Chấm 5 điểm:** parse đúng định dạng giờ (1); hiệu và total_seconds/86400 (1,5); kết quả1,50/1,25/thiếu (1); .dt.days=1/1 và giải thích phần nguyên (1); giữ thiếu, không bù0 (0,5).

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K07; phụ K05. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm phần ngày nguyên với số ngày thập phân; mất NaT.

**Đọc lại:** L ô 19–22.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-028

```python
du = s.reindex(lich, fill_value=0)
tb = du.mean()
assert du.sum() == s.sum()
```

`du=[0,2,0,4,0]`; tổng 6 review, mẫu số 5 ngày, trung bình1,2 review/ngày. Resample/asfreq chỉ đi từ02–04/06 trong dữ liệu này, không tự biết01 và05 cũng đã thu đủ. Resample cần sum vì dữ liệu đã là số đếm; asfreq không tổng hợp sự kiện. Chỉ điền0 cho ngày vắng thuộc phạm vi **đã xác nhận**; ngày 06 chưa biết phải để NaN nếu đưa vào lịch, không tự coi không review.

**Chấm 5 điểm:** reindex đúng lịch và0 trong phạm vi xác nhận (1,5); dãy/tổng/trung bình và mẫu số 5 (1,5); giới hạn hai đầu resample/asfreq (1); ngày 06 giữ chưa biết (1).

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K15; phụ K14, K13. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Không bổ sung hai đầu lịch; điền0 cho ngày chưa thu thập.

**Đọc lại:** L ô 39–50,62–66.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-029

```python
tb7 = s.rolling(7, min_periods=7, center=False).mean()
ngay = tb7.idxmax()
cua_so = s.loc[ngay - pd.Timedelta(days=6):ngay]
assert len(cua_so) == 7
assert abs(cua_so.mean() - tb7.loc[ngay]) < 1e-9
```

Sáu kết quả đầu NaN vì chưa đủ 7 giá trị. Cửa sổ01–07/11 là `[14,0,0,3,4,5,6]`, tổng 32, mean 32/7≈4,5714; cửa sổ 02–08/11 `[0,0,3,4,5,6,7]`, tổng 25, mean 25/7. Cực đại rolling tại07/11, khác cực đại gốc 01/11=14. Khoảng trễ6 ngày chỉ xảy ra trong dữ liệu này, không phải quy luật cố định. Rolling mô tả/làm mượt quá khứ, không tự dự báo ngày mai hoặc giải thích nguyên nhân. So sánh số thực dùng sai số 1e-9.

**Chấm 5 điểm:** rolling đúng và sáu NaN đầu (1,5); idxmax ngày 07 và liệt kê đúng cửa sổ, tính lại32/7 (1,5); phân biệt cực đại gốc (0,5); bác trễ cố định/dự báo và nêu giới hạn (1,5).

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K18; phụ K19, K32. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Nhầm idxmax/max; làm mượt thành dự báo; khẳng định trễ cố định.

**Đọc lại:** Lab ô 21–28; L ô 54–57.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-030

```python
doi = q / q.shift(4) - 1
p = doi.loc["2026-03-31"]
# Nếu có bảng review gốc rv:
# dem = ((rv["date"] >= "2025-01-01") & (rv["date"] < "2025-04-01")).sum()
# assert dem == q.loc["2025-03-31"]
```

Kỳ này50, kỳ gốc 40 review; tỷ lệ0,25, tăng25%. Cần4 hàng vì mỗi hàng là một quý; shift 12 là 12 quý=3 năm, sẽ lấy quýI/2023 nếu đủ lịch, không phải cùng quý năm trước. Trong chuỗi5 hàng đã cho, shift 12 làm mọi kỳ gốc thiếu. Mask phải lấy từ01/01 đến trước 01/04, bao gồm mọi giờ của31/03.

**Chấm 5 điểm:** sửa4 hàng (1,5); chỉ kỳ gốc và0,25/25% (1); shift 12 làquýI/2023, hiện thiếu (1); mask đúng và đối chiếu count40 (1,5).

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K22; phụ K23, K32. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Dùng12 hàng cho chuỗi quý; kiểm quý bằng biên ngày thiếu giờ.

**Đọc lại:** Lab ô 29–33.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.


### Tự học bổ sung

#### B8-MR05

**Đáp án C.** A convert trên naive nên lỗi. B gán sai quy ước nguồn, làm thay thời điểm. C đúng: gắn giờ Việt Nam rồi trừ7 giờ khi biểu diễn UTC, lùi ngày/tháng. D cộng7 thay vì trừ7. Nếu sẵn aware thì không localize lại; nếu là Series thì dùng `.dt`.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Gắn UTC cho giờ địa phương; đổi múi giờ sai chiều.

**Đọc lại:** L ô 86–87.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-MR06

```python
a = s.rolling(3, min_periods=2, center=False).mean()
b = s.rolling("3D", min_periods=2, center=False, closed="right").mean()
```

Cửa sổ3 hàng lấy02/06,04/06,05/06: `[0,NaN,8]`, có2 giá trị không thiếu nên mean 4. Cửa sổ3 ngày là `(02/06 09:00,05/06 09:00]`, loại đúng biên trái02/06; còn `[NaN,8]`, chỉ 1 giá trị không thiếu nên kết quả NaN. 0 vẫn là giá trị đã biết, không bị bỏ khi đếm min_periods. Không thể suy ngày 03/06 bằng 0 từ dữ liệu đã cho.

**Chấm 5 điểm:** hai lệnh đúng/cùng min_periods (1); liệt kê cửa sổ 3 hàng và mean 4 (1,5); biên trái mở, cửa sổ 3D và NaN (1,5); giải thích0/thiếu và không tự thêm dữ liệu (1).

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K31; phụ K17. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Bỏ0 như thiếu; lấy biên trái; đếm vị trí thay giá trị đã biết.

**Đọc lại:** L ô 88–89; Lab ô 21–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

### C. Cập nhật độ bao phủ sau đợt 3

Đã hoàn thành **30/60 trọng tâm** (20 TN, 10 TL) và **6/12 bổ sung** (4 TN, 2 TL).

Số câu trọng tâm đã có theo nhóm 1–6: 7 / 4 / 5 / 4 / 7 / 3.

Mục tiêu đã được dùng trong yêu cầu trả lời: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K29, K30, K31, K32.

Mục tiêu chưa dùng tới đợt này và mã câu bù đã lên kế hoạch:

- K28: Gộp nhiều năm: tổng review/tổng ngày; không chia ngày một năm hoặc mean các mức ngày; sẽ kiểm ở B8-034, B8-050.

Còn các biến thể: count có thể đúng và trùng số nhưng sai ý nghĩa (032), không ngầm fill trước pct_change (033), mean mức ngày khác mức gộp (034,050), giữ tháng 6 trọn (039,048), W-SUN (044), lọc trước rolling (058), quy tắc điều chỉnh theo trung bình trượt12 tháng (059), không tự gán UTC cho ngày thuần (060).


## Đợt 4 — B. Đáp án và hướng dẫn chấm

### Trọng tâm

#### B8-031

**Đáp án D.** Ngày29/02/2025 không tồn tại; raise dừng bằng lỗi chuyển đổi, coerce chuyển ngày sai thành NaT. None cũng thành NaT theo coerce. A coi chuyển kiểu tự sửa ngày. B nhầm nguyên nhân lỗi và bỏ qua ngày không tồn tại. C đảo hai chế độ. D đúng. Riêng cột b không phân biệt được hai nguyên nhân thiếu nếu bỏ raw; cần đối chiếu nguồn.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K04. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Coerce bị hiểu là sửa ngày; đảo chế độ raise/coerce.

**Đọc lại:** L ô 11–15; Lab ô 5–9.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-032

**Đáp án B.** size đếm4 hàng; id không thiếu nên count cũng trả4 đúng yêu cầu trên dữ liệu này. A sai vì count bỏ điểm thiếu và trả3. B đúng. C có mean(5,4,3)=4 nhưng đơn vị là điểm/review có điểm, số 4 trùng ngẫu nhiên với số review không làm phép tính đáp ứng yêu cầu. D phủ nhận một cách đúng trên cột id không thiếu. Đây là lý do phải kiểm đối tượng và đơn vị, không chỉ kiểm con số cuối.

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K13. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm count với size; bác mọi count; trùng số bị hiểu là đúng ý nghĩa.

**Đọc lại:** L ô 39–50.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-033

**Đáp án A.** Tháng1 chưa có kỳ gốc; tháng 2 thiếu kỳ này; tháng 3 thiếu kỳ gốc tháng 2; tháng 4=30/15−1=1. A đúng. B ngầm điền giá trị10 cho tháng 2. C tự điền0. D bỏ tháng thiếu khi tìm kỳ gốc, so tháng 3 với tháng 1 thay vì tháng 2. `fill_method=None` không ngầm bù số liệu trước phép tính.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K21; phụ K14. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Tự bù hoặc bỏ tháng chưa biết trước pct_change.

**Đọc lại:** L ô 62–69.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-034

**Đáp án C.** Tử số 860 review, mẫu số 57 ngày đã quan sát. A cho mỗi năm cùng trọng số dù năm 2024 có29 ngày; mean 15 khác860/57≈15,0877. B chia tổng hai năm cho ngày chỉ một năm. C đúng. D bỏ ngày nhuận. Cách tổng/tổng cân theo số ngày; không mặc định mean các mức năm bằng mức gộp chung.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K28; phụ K27. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Chia tổng nhiều năm cho ngày một năm hoặc mean các mức không cùng trọng số.

**Đọc lại:** Lab ô 34–37.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-035

**Đáp án D.** A khẳng định quá rộng: chọn đúng nhãn03/03 vẫn được. B nhầm sắp xếp với loại trùng. C suy thứ tự ngày từ id. D đúng; trên bảng này `r.sort_index().loc['2026-01':'2026-02']` trả id2,3. Không cần học thuộc thông báo lỗi; cần hiểu index chưa sắp có thể không đáp ứng cắt khoảng theo nhãn rút gọn.

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K08. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Khẳng định mọi chọn nhãn trên index chưa sắp đều lỗi.

**Đọc lại:** L ô 36–38.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-036

**Đáp án A.** rolling(3) lấy ba hàng cuối là 02,08,09/06, `[4,6,8]`, tổng 18. A đúng. B tự chuyển số hàng thành số ngày, thêm0 không được xác nhận. C loại hàng 02 vì quá xa theo lịch dù code không dùng cửa sổ thời gian. D dùng cửa sổ kết thúc ở hàng trước. Không có giả định các ngày vắng là 0 trong đề này.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K16. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Cửa sổ theo hàng bị hiểu là theo ngày trên lịch khuyết.

**Đọc lại:** L ô 51–53.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-037

**Đáp án B.** Theo tổng:294/310−1≈−5,2%. Theo ngày: tháng 1=10, tháng 2=10,5 review/ngày;10,5/10−1=5,0%. A đảo kết quả/chiều biến động. B đúng. C bỏ ảnh hưởng mẫu số ngày. D dùng tỷ số số ngày 31/28−1≈10,7% thay tỷ lệ giữa hai mức review/ngày, bỏ qua số review294 và310. Mẫu số mức ngày là 31 và28 ngày, còn mẫu số tỷ lệ so hai mức là 10 review/ngày tháng 1.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K27; phụ K23. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** So tổng tháng thay cho so mức review/ngày hoặc chỉ ước lượng từ tên tháng.

**Đọc lại:** Lab ô 34–37.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-038

Trong pandas3.0.3, không nêu format ở ví dụ này đọc thành08/04 và08/07, hiển thị `2026-04-08 2026-07-08`, hiệu91 ngày, vẫn không báo lỗi vì cả hai đều hợp lệ theo MM/DD/YYYY.

```python
vao = pd.to_datetime(vao_raw, format="%d/%m/%Y")
ra = pd.to_datetime(ra_raw, format="%d/%m/%Y")
so_dem = (ra - vao).days
```

Đúng là 04/08 đến07/08, 3 đêm. YYYY-MM-DD chỉ là cách biểu diễn giá trị đã diễn giải; không chứng minh cách đọc chuỗi nguồn đúng. Một chuỗi mơ hồ có thể mang hai ngày khác nhau nên cần quy ước nguồn. Với các giá trị này, cách `dayfirst=True` cũng được chấp nhận nếu đọc đúng và không yêu cầu kiểm định dạng chặt.

**Chấm 5 điểm:** mô tả hai ngày đọc sai và91 (1,5); sửa hai chuyển kiểu và3 đêm (1,5); hiển thị khác diễn giải (1); không suy nguồn từ một ngày mơ hồ (1).

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K02; phụ K03. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Chạy được/hiển thị ISO bị hiểu là đọc đúng ngữ nghĩa.

**Đọc lại:** G §1; L ô 8–10,23–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-039

```python
rv["date"] = pd.to_datetime(rv["date"], format="%d/%m/%Y")
m = rv.set_index("date").sort_index().resample("ME").size()
m = m.loc[m.index <= pd.Timestamp("2026-06-30")]
dem6 = ((rv["date"] >= "2026-06-01") & (rv["date"] < "2026-07-01")).sum()
assert dem6 == m.loc["2026-06-30"]
assert m.sum() == len(rv)
```

(a) Bỏ format có nguy cơ đảo ngày/tháng (trong bảng này còn có thể lỗi khi gặp29/06 sau khi suy cách đọc từ đầu); mã M cần đổi thành ME. (b) Giữ cả tháng 6 vì nguồn đã thu hết30/06; không luôn bỏ hàng cuối. (c) Ba tháng có số đếm `[2,2,2]`, dem6=2, tổng 6. Các kiểm tra xác nhận phép đếm trên dữ liệu/phạm vi cho sẵn; không xác định nguyên nhân, không chứng minh xu hướng dài hạn từ ba tháng bằng nhau. Ngày sự kiện cuối29/06 không làm tháng 6 thiếu. Nếu dùng AI, khai báo công cụ, yêu cầu chính và kết quả tự kiểm; ví dụ tự đếm hai review tháng 6 bằng mask độc lập. Khi nhờ AI cần nêu định dạng, phạm vi, kỳ gốc, phép gộp và cửa sổ nếu có.

**Chấm 5 điểm:** hai lỗi (1); hai dòng sửa (1,5); giữ tháng 6 dựa trên phạm vi (0,5); mask và đối chiếu2/tổng 6 (1); giới hạn assert/xu hướng/nguyên nhân (0,5); khai báo AI kèm kết quả tự kiểm (0,5).

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K12; phụ K11, K32. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Cấu trúc GK26; luôn bỏ kỳ cuối đã trọn; assert khớp bị hiểu là chứng minh kết luận.

**Đọc lại:** L ô 39–47,84–85; Lab ô 18–20; GK26.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-040

```python
bao_cao = nay.sum() / goc.sum() - 1
print(f"{bao_cao:.1%}")
```

(a) Code cũ lấy mean(1,0, −0,1)=0,3, tức30%, mỗi tháng cùng trọng số. (b) Tổng420 so400 review, tăng5,0%; mẫu số 400 review quýI/2025. Tỷ lệ tổng tương đương trung bình tỷ lệ tháng với trọng số 40/400,160/400,200/400. (c) Không mâu thuẫn: riêng tháng 3 là 180/200−1=−10%, kỳ gốc tháng 3/2025, còn tổng quý dùng toàn quýI/2025. Một phần giảm không bắt buộc tổng giảm.

**Chấm 5 điểm:**0,3 và trọng số đều theo tháng (1); sửa dòng, tổng 420/400 và5,0% (2); −10% và hai kỳ gốc (1); giải thích không mâu thuẫn nhờ phạm vi khác nhau (1).

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K24; phụ K23. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Mean tỷ lệ thay tổng; một tháng giảm bị hiểu là cả giai đoạn giảm.

**Đọc lại:** L ô 70–76,82–83.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.


### Tự học bổ sung

#### B8-MR07

**Đáp án B.** A chỉ lấy00:00 ngày 15. B đúng với khoảng `[15/08 00:00,16/08 00:00)`, lấy cả14:20 và23:59. C nhận thừa00:00 ngày 16. D bỏ mất00:00 ngày 15. Không dùng <=ngày cuối ở00:00 để lấy mọi giờ của ngày đó. Các mốc phải thống nhất timezone nếu dữ liệu aware.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K30. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm00:00 với hết ngày; đóng sai một trong hai biên.

**Đọc lại:** L ô 90–91.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-MR08

**Đáp án D.** A localize lại dữ liệu aware sẽ lỗi. B nhầm cùng thời điểm thực với cùng ngày trên lịch. C có ngày đúng nhưng hiểu sai thời điểm; chỉ biểu diễn đổi. D đúng: UTC+7 đẩy sang năm mới và thứ Năm=3. `utc=True` phù hợp ở đây vì đề đã cho chuỗi ghi UTC, không dùng như quy tắc mặc định cho cột chỉ có ngày.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29; phụ K06. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Nhầm ngày với thời điểm thực; localize dữ liệu đã aware.

**Đọc lại:** L ô 26–28,86–87; GK20.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

### C. Cập nhật độ bao phủ sau đợt 4

Đã hoàn thành **40/60 trọng tâm** (27 TN, 13 TL) và **8/12 bổ sung** (6 TN, 2 TL).

Số câu trọng tâm đã có theo nhóm 1–6: 9 / 5 / 7 / 5 / 9 / 5.

Mục tiêu đã được dùng trong yêu cầu trả lời: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32.

Không còn mục tiêu K chưa được sử dụng. Các đợt sau (nếu còn) tiếp tục kiểm biến thể về cửa sổ, phạm vi và mẫu số, không tự tăng mức khó.

Còn các biến thể: quý/thứ (041), W-SUN (044), giữ tháng trọn khi có giờ (048), đủ 7 vị trí nhưng thiếu một số đếm (049), gộp ngày năm nhuận (050), dayfirst khi nguồn cần format (051), asfreq không gộp sự kiện (052), xóa tháng 0 làm sai shift 12 (054), kỳ gốc 0 (055), lọc năm trước rolling (058), quy tắc điều chỉnh xu hướng (059).


## Đợt 5 — B. Đáp án và hướng dẫn chấm

### Trọng tâm

#### B8-041

**Đáp án B.** Tháng7 thuộc quýIII; thứ Năm=3 khi thứ Hai=0. A cho tháng 7 vào quýII. B đúng. C đếm thứ Hai bằng 1. D nhầm độ dài Series với khả năng dùng accessor: Series ngày giờ dùng được .dt dù chỉ một phần tử. Các thuộc tính lấy từ ngày đã chuyển, không từ cách viết chuỗi.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K06. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Sai quý hoặc quy ước thứ; nhầm .dt với độ dài dữ liệu.

**Đọc lại:** L ô 16–18.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-042

**Đáp án D.** A biến giới hạn phân tích thành quy tắc sửa dữ liệu. B đánh đồng ngày ghi review với nhận phòng. C suy đủ tháng từ nhãn. D đúng: phạm vi câu hỏi quyết định hàng dùng; nguồn giải thích hợp lý việc có ngày sau mốc nhưng không khiến các hàng ấy thuộc phạm vi phân tích. Dữ liệu chỉ có ngày nên <=29/06 bao gồm toàn ngày theo độ chính xác đã cho; nếu có giờ thì phải xét biên khác.

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K10; phụ K09, K11. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Sửa ngày ngoài mốc; nhầm review với ngày lưu trú; suy trọn kỳ từ nhãn.

**Đọc lại:** L ô 30–38; Lab ô 12–17.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-043

**Đáp án C.**12 hàng là 12 quý=3 năm:100/40−1=1,5=150%. Đúng cùng kỳ năm trước là 4 quý:100/80−1=0,25=25%. A áp quy tắc chuỗi tháng cho chuỗi quý. B bỏ qua periods 12. C đúng. D gắn tỷ lệ của kỳ gốc 80 cho phép chia thực tế có mẫu số 40; đổi mô tả không sửa phép tính.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K22; phụ K23. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** 12 kỳ quý bị coi là 12 tháng; đổi lời diễn giải thay vì sửa mẫu số.

**Đọc lại:** Lab ô 29–33; L ô 73–76.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-044

**Đáp án A.** Nhãn12/07 nhận review06/07 và hai review12/07, tổng 3; nhãn19/07 nhận13/07, tổng 1. A đúng. B chuyển nhầm review Chủ nhật sang tuần sau. C đếm hai ngày khác nhau06 và12/07 thay ba review trong tuần đầu; tuần sau có một ngày 13/07. D bỏ qua ranh giới tuần, gộp hết thành một kỳ. W-SUN gộp theo lịch, không phải mỗi7 hàng.

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K12; phụ K13. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Gộp sai biên Chủ nhật hoặc đếm ngày thay review.

**Đọc lại:** L ô 39–44.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-045

**Đáp án D.** A tính trên ngày có review, khác câu hỏi. B chỉ dùng phạm vi giữa hai ngày có sự kiện, bỏ hai đầu đã quan sát. C dùng số hàng thay tổng review. D đúng: (2+4)/6=1 review/ngày. Nguồn cho phép điền0 vào các ngày đã thu không có sự kiện; không suy chính sách này cho ngày ngoài01–06/06.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K27; phụ K13. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Mẫu số ngày có review/giữa hai sự kiện thay mọi ngày đã quan sát.

**Đọc lại:** L ô 48–50; Lab ô 34–37.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-046

**Đáp án B.** Sau asfreq, tháng 2 là NaN. Tháng3 không có kỳ gốc tháng 2 nên tỷ lệ NaN; tháng 4 có kỳ gốc tháng 3=30,60/30−1=1. A bỏ tháng 2 và so tháng 3 với tháng 1. B đúng. C điền0 cho tháng 2 chưa thu. D nhầm tỷ lệ với phần trăm ở tháng 4. Dòng code trả lời thay đổi theo tháng lịch, không phải theo lần có số liệu trước.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K20; phụ K15, K21. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Lịch thiếu kéo sai kỳ gốc; nhầm0/NaN và tỷ lệ/phần trăm.

**Đọc lại:** L ô 62–69.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-047

**Đáp án A.** Hàng0 hiệu03−01=2 ngày; hàng 1 có NaT ở ngày vào nên số đêm thiếu. A đúng. B đồng nhất thiếu ngày giờ với khoảng0. C dùng thành phần ngày thay hiệu ngày. D tự tạo một ngày vào không có trong nguồn, thay đổi ý nghĩa dữ liệu. NaT khác một ngày hợp lệ và khác Timedelta0.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K05; phụ K04. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** NaT bị hiểu là số đêm0 hoặc bị sửa bằng một ngày tự đặt.

**Đọc lại:** L ô 11–22; Lab ô 5–9.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-048

```python
giu = (t >= pd.Timestamp("2026-06-01")) & (t < pd.Timestamp("2026-07-01"))
so = int(giu.sum())
```

Giữ hàng 0–3,4 review; code cũ giữ3 và bỏ review30/06 18:00. Nguồn xác nhận tháng 6 đã thu đủ, nên được giữ sau sửa mask. Mốc00:00 trong code là lỗi biểu diễn biên trên của câu hỏi, không chứng minh nguồn chỉ thu đến00:00. Hàng01/07 bị loại vì ngoài phạm vi tháng 6; sự tồn tại của nó không chứng minh tháng 7 trọn hoặc ngày đó sai nguồn.

**Chấm 5 điểm:** khoảng đầu tháng đến trước đầu tháng sau (2); đếm4 và chỉ ra hàng bị mất ở code cũ (1); phân biệt mốc lọc với độ đầy đủ nguồn (1); giữ tháng 6/không suy tháng 7 trọn hoặc sai nguồn (1).

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K11; phụ K30, K10. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Lẫn thời điểm cắt code với phạm vi nguồn; bỏ phần ngày còn giờ.

**Đọc lại:** L ô 45–47,90–91; Lab ô 18–20.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-049

```python
tb = s.rolling(7, min_periods=7, center=False).mean()
tb6 = s.rolling(7, min_periods=6, center=False).mean()
```

(a) Sáu hàng đầu chưa đủ cửa sổ; hai hàng sau có một ngày chưa biết. Điền0 tạo thông tin “trung bình0 review/ngày” không có căn cứ. (b) Cả07 và08/06 là NaN. Cửa sổ08/06 gồm02–08/06 `[2,NaN,4,0,6,8,10]`, chỉ 6 giá trị hợp lệ. (c) Mean trên6 giá trị đã biết là 30/6=5 review/ngày có số liệu, không phải trung bình xác định của đủ 7 ngày;0 ở05/06 vẫn được tính trong mẫu số 6. Không được tự coi NaN là 0 để lấy30/7.

**Chấm 5 điểm:** giải thích thiếu đầu chuỗi/thiếu trong cửa sổ và không bù0 (1,5); sửa và hai NaN (1); đúng7 ngày/6 giá trị (1); mean 5 với mẫu số 6, diễn giải giới hạn đúng (1,5).

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K17; phụ K18, K32. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Điền NaN đầu chuỗi/thiếu nguồn thành0 cho đẹp; min_periods theo số vị trí.

**Đọc lại:** L ô 51–53; Lab ô 21–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-050

```python
ngay = pd.Series(m.index.days_in_month, index=m.index)
tong = m.groupby(m.index.month).sum()
tong_ngay = ngay.groupby(ngay.index.month).sum()
tb = tong / tong_ngay
p_tong = tong.loc[2] / tong.loc[1] - 1
p_ngay = tb.loc[2] / tb.loc[1] - 1
```

Tháng1:930 review/62 ngày=15/ngày. Tháng2:860 review/57 ngày≈15,087719/ngày. Theo tổng giảm7,5%; theo ngày tăng0,6%. Kỳ gốc là tổng tháng 1 hoặc mức/ngày tháng 1 tương ứng, không dùng lẫn mẫu số. Mean các mức tháng 2 là(10+20)/2=15, cho mỗi năm cùng trọng số; mức gộp cân theo28 và29 ngày. Số ngày tháng 2 ít hơn tháng 1 khoảng8,1% (57/62−1), nên không thể đọc chiều biến động mức ngày từ tổng mà bỏ mẫu số.

**Chấm 5 điểm:** groupby tháng số và tổng review đúng (1); days_in_month/tổng 62,57 (1); hai mức/ngày đúng (1); hai tỷ lệ và chiều giảm/tăng đúng, kỳ gốc rõ (1); giải thích mean năm sai trọng số (1). Chấp nhận tính tay hoặc code tương đương; tỷ lệ sai số 1e-9 trước làm tròn.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K28; phụ K27, K23. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Tổng nhiều năm chia ngày một năm; mean năm thay tổng/tổng; chiều biến động đảo sau chuẩn ngày.

**Đọc lại:** Lab ô 34–37.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.


### Tự học bổ sung

#### B8-MR09

**Đáp án B.** A nhầm văn bản giống ngày với DatetimeIndex cần cho cách dùng cửa sổ theo thời gian. B đúng theo bài: chuyển kiểu, sắp index, chỉ rõ điều kiện đủ giá trị và biên. C xóa sự kiện hợp lệ chỉ vì cùng ngày. D tự tạo số 0 cho dữ liệu chưa biết; rolling theo thời gian có thể làm việc trên lịch không đều mà không cần điền mọi ngày. Chỉ số 0 đã được xác nhận mới được coi là giá trị biết.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K31; phụ K08. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Để index chuỗi; bắt bổ sung0/xóa ngày trùng khi không có căn cứ.

**Đọc lại:** L ô 88–89.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-MR10

```python
v = pd.to_datetime(raw, format="%Y-%m-%d %H:%M").dt.tz_localize("UTC").dt.tz_convert("Asia/Ho_Chi_Minh")
dau = pd.Timestamp("2027-01-01", tz="Asia/Ho_Chi_Minh")
cuoi = pd.Timestamp("2027-01-02", tz="Asia/Ho_Chi_Minh")
giu = (v >= dau) & (v < cuoi)
dem = pd.Series(1, index=pd.DatetimeIndex(v[giu])).resample("D").size()
bao_cao = dem.reindex(lich)
```

Giữ hàng 1,2; báo cáo ngày 01 là 2, ngày 02 là NaN. Giờ Việt Nam lần lượt31/12 23:59,01/01 00:00,01/01 23:59,02/01 00:00. Phạm vi đã thu đủ là 1 ngày nên2 review/ngày. Một hàng 02/01 chỉ chứng minh có sự kiện lúc00:00, không xác nhận tổng trọn ngày; không bù0 hoặc dùng số 1 như tổng ngày đã biết. Nếu ngày 01 không có sự kiện vẫn phải tạo số 0 dựa trên lịch/phạm vi thu đủ, không để resample tự đoán ngoài hai đầu.

**Chấm 5 điểm:** gắn UTC/convert đúng (1); mask ngày Việt Nam phải mở (1); giữ hàng 1,2 và tổng 2 (1); reindex giữ ngày 02 NaN (1); mẫu số 1 ngày/không suy trọn ngày từ hàng có sẵn (1).

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29; phụ K30, K15. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Lấy ngày UTC; nhầm hàng đầu ngày chưa thu đủ với tổng ngày; fill0 ngoài phạm vi.

**Đọc lại:** L ô 86–91,48–50,62–66.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

### C. Cập nhật độ bao phủ sau đợt 5

Đã hoàn thành **50/60 trọng tâm** (34 TN, 16 TL) và **10/12 bổ sung** (7 TN, 3 TL).

Số câu trọng tâm đã có theo nhóm 1–6: 11 / 7 / 8 / 6 / 11 / 7.

Mục tiêu đã được dùng trong yêu cầu trả lời: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32.

Không còn mục tiêu K chưa được sử dụng. Các đợt sau (nếu còn) tiếp tục kiểm biến thể về cửa sổ, phạm vi và mẫu số, không tự tăng mức khó.

Còn các biến thể: dayfirst và format nguồn (051), asfreq không tổng hợp/không mở hai đầu (052), giới hạn dự báo/độ trễ (053), xóa tháng 0 làm sai cùng kỳ và phân biệt tháng trước (054), kỳ gốc 0 (055), month bỏ năm theo mục tiêu báo cáo (056), mẫu số 5 ngày của phần tháng (057), lọc năm trước rolling (058), chỉ số 100 và tỷ số điều chỉnh đã cho (059), ngày thuần không tự gán UTC (060), ba ngày lịch khác3D đến một thời điểm (MR12).


## Đợt 6 — B. Đáp án và hướng dẫn chấm

### Trọng tâm

#### B8-051

**Đáp án C.** A coi dayfirst là bộ kiểm chặt. B coi format chỉ là cách in và không áp quy ước khi parse. C đúng: với chuỗi này, pandas đọc a theo tháng/ngày sau khi cách ưu tiên không hợp lệ (có thể cảnh báo); b không đọc được tháng 13 theo `%d/%m/%Y` nên NaT. D đảo hai hành vi. Đây là câu có yêu cầu rõ về quy ước, khác việc chỉ cần đọc đúng một bộ ngày cụ thể. `raw.notna() & b.isna()` đánh dấu hàng 0 là lỗi chuyển đổi, không phải thiếu nguồn.

**Hồ sơ câu:** Nhóm chính 1 — Đọc ngày, NaT, thành phần ngày và khoảng thời gian. Mục tiêu chính K03; phụ K02, K04. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Ưu tiên dayfirst bị hiểu là yêu cầu định dạng không có ngoại lệ.

**Đọc lại:** G §1; L ô 8–15,84.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-052

**Đáp án A.** A đúng: asfreq đưa chuỗi đã tổng hợp về lịch giữa hai đầu, không biết các ngày quan sát ngoài khoảng nhãn gốc. B gán thông tin nguồn mà hàm không nhận. C nhầm đưa về lịch với đếm hàng; tổng vẫn8 review. D nhầm asfreq với tổng hợp nhiều sự kiện; index trùng còn có thể không reindex được. Với lịch đã biết01–05, `s.reindex(lich,fill_value=0)` cho `[0,3,0,5,0]`.

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K15; phụ K14, K13. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Asfreq bị hiểu là tổng hợp sự kiện hoặc biết hai đầu lịch ngoài dữ liệu.

**Đọc lại:** L ô 39–50,62–66.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-053

**Đáp án B.** A biến làm mượt thành dự báo. B đúng: các mean đủ cửa sổ là 28/3,19/3,9,10; cực đại duy nhất10 gắn tháng 6 từ cửa sổ tháng 4–6 `[9,10,11]`. C sai vì hai kiểu cực đại đo khác đối tượng. D suy độ trễ cố định từ một ví dụ. Giá trị gốc lớn chỉ ảnh hưởng các cửa sổ chứa nó, không quyết định mọi nhãn cực đại đường mượt. Mẫu số ở mỗi trung bình là 3 tháng, không phải số ngày.

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K19; phụ K16. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Làm mượt thành dự báo, yêu cầu cực đại trùng nhau hoặc trễ cố định.

**Đọc lại:** L ô 51–57; Lab ô 24–28.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-054

**Đáp án D.** Chuỗi đầy đủ: cùng năm 80/40−1=100%; tháng trước 80/60−1≈33,3%. Sau xóa tháng 6/2025,12 hàng trước tháng 3/2026 trở thành tháng 2/2025=10, nên80/10−1=700%. A coi mọi kỳ gốc giống nhau. B đảo phép cùng kỳ và tháng trước. C bỏ qua việc shift đếm hàng, không tự dò tháng. D đúng.0 là quan sát hợp lệ phải giữ trong lịch; không dùng fill0 để thay cho tháng chưa biết trong trường hợp khác.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K22; phụ K20, K23. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Xóa tháng 0 làm lịch lệch; cùng kỳ khác tháng trước.

**Đọc lại:** L ô 62–76.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-055

**Đáp án A.** Hàng đầu không có kỳ gốc; tháng 2 là 0/0−1 nên NaN; tháng 3 là 5/0−1 nêninf; tháng 4 là 10/5−1=1. A đúng. B gán0 cho 0/0 và dùng chênh tuyệt đối5 thay tỷ lệ. C gán phần trăm hữu hạn cho chia0, đồng thời đổi đơn vị. D cho rằng từ0 lên dương luôn tăng100%. Không báo một tỷ lệ tăng trưởng hữu hạn khi mẫu số 0; cần nêu số đếm gốc và quy tắc báo riêng.

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K21. Mức độ: Nền tảng.

**Sai lầm được kiểm tra:** Chia0 bị báo thành tăng hữu hạn;0/0 thành0.

**Đọc lại:** L ô 67–69.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-056

**Đáp án C.** `.index.month` là thuộc tính trực tiếp, chỉ còn số tháng, nên x có tháng 1=3 và tháng 2=1. A cho rằng năm còn trong khóa nhóm. B dùng .dt không đúng cho DatetimeIndex. C đúng: resample ME giữ nhãn năm-tháng; nếu cần mọi tháng đến12/2026, phải bổ sung lịch vì sự kiện cuối ở01/2026. D đổi phép đếm không khôi phục thông tin năm bị bỏ khỏi khóa nhóm. Gộp theo month có thể đúng nếu mục tiêu là phân bố tháng qua năm, nhưng khác yêu cầu ở đây.

**Hồ sơ câu:** Nhóm chính 2 — DatetimeIndex, chọn khoảng và phạm vi quan sát. Mục tiêu chính K08; phụ K25, K06. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** month bỏ năm; đổi count không thể sửa khóa nhóm.

**Đọc lại:** L ô 36–44,77–79.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-057

```python
df["date"] = pd.to_datetime(df["date"], format="%d/%m/%Y")
m = df.set_index("date")["n"].resample("ME").sum()
tb1 = m.loc["2024-01-31"] / 31
tb2 = m.loc["2024-02-29"] / 5
```

(a) Bỏ format có thể đảo ngày/tháng; M cần ME. size đếm số dòng ngày, không cộng số review. (b) Tổng tháng 1=20, phần quan sát tháng 2=10; tổng 30 bằng `df['n'].sum()`, khác4 hàng. (c) Mẫu số 31 ngày tháng 1 và5 ngày 01–05/02, mức 20/31≈0,645161 và2 review/ngày. Không chia phần tháng 2 cho 29 ngày vì chưa thu đủ tháng; tổng giảm50% là so5 ngày với 31 ngày, không là mức giảm của tháng 2 trọn. Có thể so01–05 của hai tháng với 10 so8 review, ghi rõ phạm vi, không suy nguyên nhân.

**Chấm 5 điểm:** vấn đề format/API/đếm sai đơn vị (1,5); sửa hai dòng và tổng 20/10 (1,5); mẫu số 31/5 và hai mức (1); giới hạn kỳ chưa trọn và cách diễn giải đúng (1). Chấp nhận lời giải không tính tỷ lệ của tổng vì đề chỉ yêu cầu nhận xét tính hợp lý.

**Hồ sơ câu:** Nhóm chính 3 — Resample, lịch đầy đủ và phép tổng hợp. Mục tiêu chính K13; phụ K12, K11. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Cấu trúc GK26; size bảng tổng hợp; lấy số ngày cả tháng cho kỳ chưa trọn.

**Đọc lại:** L ô 39–50; Lab ô 34–37; GK26.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-058

```python
nam = s.loc["2025"]
tb7 = nam.rolling(7, min_periods=7, center=False).mean()
w = nam.loc["2025-01-01":"2025-01-07"]
assert abs(tb7.loc["2025-01-07"] - w.mean()) < 1e-9
```

01–06/01 đều NaN vì chỉ dùng năm 2025 nên chưa đủ 7 giá trị. Cửa sổ07/01 chứa `[1,1,1,1,1,1,7]`, tổng 13, mean 13/7≈1,857143. Code sai có kết quả06/01=(70+6)/7, dùng31/12/2024, dù sau đó lọc nhãn về năm 2025; nhãn kết quả trong năm không bảo đảm mọi dữ liệu cửa sổ cũng trong năm. Không dùng dữ liệu sau ngày đang xét.

**Chấm 5 điểm:** lọc năm trước rolling (1,5); sáu NaN đầu (1); cửa sổ và13/7, đối chiếu đúng (1,5); nêu rò dữ liệu ngoài phạm vi của cách cũ (1).

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K18; phụ K17, K10. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Lọc nhãn sau rolling bị hiểu là đã giới hạn dữ liệu đầu vào của cửa sổ.

**Đọc lại:** Lab ô 21–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-059

```python
chi_so8 = 1500 / 1000 * 100
goc = pd.Series([180, 264], index=["2025-07", "2025-08"])
muot12 = pd.Series([120, 240], index=goc.index)
dieu_chinh = goc / muot12
```

(a) Chỉ số 150: tổng tháng 8 bằng 150% mức trung bình của12 tổng tháng (cao hơn50%);100 là mức trung bình, không phải100 review hay xác suất100%. (b) Mức1,5 và1,1; tháng 8/2025 có264 review cao hơn nhưng tỷ số điều chỉnh thấp hơn tháng 7/2025. Mẫu số điều chỉnh thay theo tháng, khác mẫu số 1000 review trong chỉ số gộp. (c) Chỉ số gốc chưa loại xu hướng dài hạn và số ngày tháng. Chia theo quy tắc minh họa không tự chứng minh đã tách hoàn toàn mùa, đã chuẩn số ngày, hay nguyên nhân biến động; hai kiểm tra số học chỉ xác nhận cách tính trên đầu vào đã cho. Không cần mô hình phân rã nâng cao.

**Chấm 5 điểm:**150 và định nghĩa100 chính xác (1,5); hai tỷ số/chiều xếp hạng đúng (1,5); phân biệt mẫu số (0,5); giới hạn xu hướng, số ngày và kiểm chứng/nhân quả (1,5).

**Hồ sơ câu:** Nhóm chính 5 — Shift, pct_change và so sánh giữa các kỳ. Mục tiêu chính K26; phụ K25, K32. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Chỉ số 100 bị hiểu là số đếm hoặc đã loại xu hướng; kiểm số học bị hiểu là chứng minh mô hình/nhân quả.

**Đọc lại:** G §3 chỉ số theo tháng; L ô 77–85.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-060

```python
v = pd.to_datetime(raw, format="%Y-%m-%d %H:%M").dt.tz_localize("UTC").dt.tz_convert("Asia/Ho_Chi_Minh")
dau = pd.Timestamp("2027-01-01", tz="Asia/Ho_Chi_Minh")
cuoi = pd.Timestamp("2027-01-02", tz="Asia/Ho_Chi_Minh")
giu = (v >= dau) & (v < cuoi)
so = int(giu.sum())
```

Giữ hàng 1,2,3: giờ địa phương lần lượt01/01 00:00,06:00,23:30; tổng 3 review/1 ngày đã thu đủ=3 review/ngày. Hàng2 thuộc01/01/2027 thứ Sáu, dayofweek=4. Hàng0 là 31/12 23:30, hàng 4 là 02/01 00:00, bị loại. Không tự gán UTC cho bảng chỉ có ngày khi nguồn không nói; ngày review không cung cấp thời điểm00:00 UTC, gán như vậy tự thêm giả định và có thể làm sai việc gộp theo lịch.

**Chấm 5 điểm:** localize/convert theo nguồn (1); biên ngày cùngtimezone đúng (1); giữ1,2,3 và3/ngày, mẫu số 1 (1); ngày/thứ của hàng 2 đúng (1); không tựgán UTC cho ngày thuần và lý do (1).

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29; phụ K30, K27. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Gộp theo ngày UTC thay ngày Việt Nam; mặc định gán UTC cho cột chỉ có ngày.

**Đọc lại:** L ô 26–28,86–91; Lab ô 34–37.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.


### Tự học bổ sung

#### B8-MR11

**Đáp án A.** Giờ Việt Nam là 01/08 01:00,01/08 08:00,02/08 00:30; v có2 ở01/08,1 ở02/08. UTC có1 ở31/07,2 ở01/08. A đúng. B nhầm bất biến thời điểm với bất biến nhóm ngày. C quên review17:30UTC đã sang02/08. D localize lại dữ liệu aware sai cách. Chỉ số 2 ngày 01/08 Việt Nam có đủ phạm vi nguồn; số 1 ngày 02/08 chưa được bảo đảm là tổng trọn ngày.

**Hồ sơ câu:** Nhóm chính 6 — Múi giờ, lịch và chuẩn hóa theo số ngày. Mục tiêu chính K29; phụ K13. Mức độ: Vận dụng.

**Sai lầm được kiểm tra:** Đổi timezone sau khi đã gộp ngày bị hiểu tương đương đổi trước gộp.

**Đọc lại:** L ô 86–87,39–44.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

#### B8-MR12

```python
v = pd.to_datetime(raw, format="%Y-%m-%d %H:%M", utc=True).tz_convert("Asia/Ho_Chi_Minh")
ev = pd.Series(1, index=v).sort_index()
a = ev.rolling("3D", min_periods=1, closed="right").sum().loc[pd.Timestamp("2026-07-03", tz="Asia/Ho_Chi_Minh")]
d = ev.resample("D").size().reindex(lich, fill_value=0)
b = d.rolling(3, min_periods=3, center=False).sum().loc["2026-07-03"]
```

Giờ Việt Nam:30/06 01:00,01/07 01:00,03/07 00:00,04/07 01:00.
(a) Khoảng `(30/06 00:00,03/07 00:00]` cóba sự kiện đầu, tổng 3.
(b) Lịch ngày `[1,1,0,1,1]`; cửa sổ 01–03/07 có `[1,0,1]`, tổng 2; tương ứng phạm vi `[01/07 00:00,04/07 00:00)`.
Hai cửa sổ khác cả điểm bắt đầu và điểm kết thúc; “3D đến đúng một thời điểm” không tự là “ba ngày lịch nguyên kết thúc hết ngày đó”. Không cần bù dữ liệu ngoài lịch đã thu đủ.

**Chấm 5 điểm:** parse UTC/convert và giữ index sự kiện có giờ (1); (a) biên đúng, ba sự kiện/tổng 3 (1,5); (b) lịch ngày đầy đủ/rolling/cửa sổ 1,0,1/tổng 2 (1,5); giải thích khác phạm vi và không mâu thuẫn (1). Chấp nhận mask trực tiếp tương đương nếu liệt kê đúng cửa sổ và vẫn nêu cách rolling theo yêu cầu(b).

**Hồ sơ câu:** Nhóm chính 4 — Rolling và diễn giải cửa sổ trượt. Mục tiêu chính K31; phụ K29, K18. Mức độ: Phân loại.

**Sai lầm được kiểm tra:** Đồng nhất3 ngày tính lùi từ thời điểm với ba ngày lịch đã quan sát trọn.

**Đọc lại:** L ô 86–91; Lab ô 21–25.

**Kiểm chứng:** Đã thực thi ca độc lập bằng pandas 3.0.3, PASS; phần diễn giải/lựa chọn đã rà bằng suy luận.

### C. Cập nhật độ bao phủ sau đợt 6

Đã hoàn thành **60/60 trọng tâm** (40 TN, 20 TL) và **12/12 bổ sung** (8 TN, 4 TL).

Số câu trọng tâm đã có theo nhóm 1–6: 12 / 8 / 10 / 8 / 14 / 8.

Mục tiêu đã được dùng trong yêu cầu trả lời: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32.

Không còn mục tiêu K chưa được sử dụng. Kiểm kê cuối bên dưới xác nhận đủ nhóm, dạng câu và mức độ.

Đã hoàn thành cả các tiểu ý cuối: dayfirst/format nguồn, lịch hai đầu, kỳ gốc 0, giữ lịch đủ khi shift 12, lọc trước rolling, chỉ số 100 và ý nghĩa quy tắc điều chỉnh, ngày thuần không tự gán UTC, khác biệt3D và ba ngày lịch. Không còn nội dung bắt buộc bỏ trống trong phạm vi ba nguồn đã đọc.

## Kiểm kê cuối và giới hạn sử dụng

- Đủ B8-001–B8-060 và B8-MR01–B8-MR12; không lặp mã, không thiếu mã.
- Trọng tâm: 60 = 40 TN + 20 TL; nhóm chính 1–6: 12,8,10,8,14,8; mức độ: 15 nền tảng,33 vận dụng,12 phân loại.
- Bổ sung: 12 = 8 TN + 4 TL. Mỗi đợt đúng10 trọng tâm và2 bổ sung.
- Đáp án TN trọng tâm: A/B/C/D mỗi chữ10 lần; bổ sung mỗi chữ2 lần, không theo chu kỳ cố định. Mỗi bộ lựa chọn đã được rà để có đúng một đáp án theo dữ kiện/đơn vị được nêu.
- Cấu trúc gần GK26: B8-010,019,039,057 đều yêu cầu phát hiện lỗi đọc ngày/API, sửa code và kiểm phạm vi/mẫu số/kết luận.
- Đã loại tình huống đồng hạng idxmax ngoài chủ ý; không hỏi scalar khi độ chính xác/index không bảo đảm; không đánh dấu dayfirst/count đúng là sai vì cách khác rõ hơn.
- Độ bao phủ bài học căn cứ G/L/Lab và danh mục K; mức ưu tiên kiểu đề căn cứ GK19–20,26 cùng năm đề bổ trợ; MR là tự học có căn cứ. Không suy từ ngân hàng ra xác suất xuất hiện hoặc nội dung chắc chắn của đề thật.

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

## Đối chiếu 20 sai lầm trọng tâm

| STT | Sai lầm | Câu sử dụng để trả lời |
|---|---|---|
| 1 | Ngày/tháng đảo nhưng vẫn hợp lệ | B8-001, B8-010, B8-016, B8-019, B8-038, B8-051 |
| 2 | NaT bị coi là 0 đêm | B8-008, B8-027, B8-047 |
| 3 | Chỉ nhìn cột đã chuyển để giải thích mọi thiếu | B8-007, B8-008, B8-018, B8-031 |
| 4 | Xóa sự kiện vì trùng ngày | B8-004, B8-018, B8-044, B8-MR09 |
| 5 | size đếm dòng bảng tổng hợp thay tổng review | B8-022, B8-032, B8-045, B8-057 |
| 6 | Nhãn cuối kỳ bị coi là đã thu đủ | B8-010, B8-019, B8-025, B8-039, B8-057 |
| 7 | Luôn bỏ hàng cuối dù đã trọn | B8-025, B8-039, B8-048 |
| 8 | Tháng/ngày chưa thu bị gán 0 | B8-013, B8-028, B8-033, B8-046, B8-MR10 |
| 9 | rolling theo hàng bị hiểu theo ngày | B8-005, B8-036, B8-MR01, B8-MR06, B8-MR12 |
| 10 | Đủ k vị trí bị hiểu là đủ k giá trị biết | B8-014, B8-049, B8-MR06 |
| 11 | shift 1 luôn là tháng trước | B8-013, B8-046, B8-054 |
| 12 | shift 12 chuỗi quý bị hiểu cùng năm trước | B8-030, B8-043 |
| 13 | pct_change đã nhân 100 hoặc sai đơn vị | B8-002, B8-017, B8-024, B8-055 |
| 14 | Mean tỷ lệ thay đổi thay tỷ lệ của tổng | B8-009, B8-040 |
| 15 | Gộp tháng qua năm với số năm đóng góp khác nhau | B8-020, B8-056, B8-059 |
| 16 | So tổng tháng bỏ qua số ngày | B8-015, B8-034, B8-037, B8-045, B8-050, B8-057 |
| 17 | localize bị dùng thay convert | B8-026, B8-060, B8-MR02, B8-MR05, B8-MR08 |
| 18 | Mốc 00:00 bị hiểu là hết ngày | B8-048, B8-MR07, B8-MR10, B8-MR12 |
| 19 | Cực đại rolling bị coi là cực đại gốc | B8-023, B8-029, B8-053 |
| 20 | Hai phép kiểm khớp bị coi chứng minh xu hướng/nhân quả | B8-032, B8-039, B8-059 |

Các sai lầm được hỏi qua kết quả code, chọn nhận định, sửa dòng và giải thích ngắn. Những câu cùng khái niệm thay đổi đối tượng đếm, lịch thiếu, vị trí thiếu, mốc cắt hoặc mục tiêu; không chỉ đổi số của đề mẫu.

## Các phép đối chiếu tiêu biểu đã chạy

| Nội dung kiểm | Câu/ca thực thi | Kết quả đối chiếu |
|---|---|---|
| NaT và thiếu nguồn | B8-007,008,018,031,047,051 | Mask dùng raw loại đúng lỗi chuyển, giữ thiếu số đêm |
| Đếm tháng/quý trực tiếp | B8-010,019,030,039 | Mask cùng phạm vi khớp số đếm tổng hợp |
| Tổng review và đơn vị | B8-002,010,019,028,039,044,057 | Sự kiện: tổng=size số hàng hợp lệ; bảng đếm: tổng=sum n |
| Kỳ trước cuối và đúng cuối | B8-019,025,039 | Mốc29/06 chỉ giữ quýI; mốc30/06 có thể giữ quýII nếu thu đủ |
| Cửa sổ gốc | B8-023,029,049,058, MR03, MR06, MR12 | Lấy đúng nhãn và số giá trị không thiếu; tái tính tổng/mean |
| Kỳ này/kỳ gốc | B8-013,030,043,054,055 | In/đối chiếu hàng dịch, lịch tháng/quý, 0/0 và dương/0 |
| Số ngày | B8-015,034,037,050,057 | Có ngày nhuận; gộp tổng/tổng; phần tháng không dùng cả tháng |
| Múi giờ và biên ngày | B8-003,026,048,060, MR02, MR07, MR10–12 | Cùng thời điểm nhưng có thể đổi ngày/tháng/năm/thứ; phải mở đúng ngày sau |
