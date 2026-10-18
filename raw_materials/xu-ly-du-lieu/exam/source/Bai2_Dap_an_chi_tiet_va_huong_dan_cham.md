# Bài 2 — Đáp án chi tiết và hướng dẫn chấm tự luận

## Nguồn đã đọc và giới hạn

- **G**: [bai-02-python-co-ban.md](<D:/LTXLDL_GK/Bài 2/bai-02-python-co-ban.md>), toàn bộ nội dung, gồm phần tự học module và lời khuyên kiểm chứng.
- **L**: [lecture_02.ipynb](<D:/LTXLDL_GK/Bài 2/lecture_02.ipynb>), đủ 29 cell, gồm hướng dẫn, code, bài tập, 5 assert của clean_nights và pipeline tự làm.
- **T**: [lab_02.ipynb](<D:/LTXLDL_GK/Bài 2/lab_02.ipynb>), đủ 40 cell, gồm khởi động, đọc dữ liệu, chuyển giá, trung vị, xếp hạng khu, kiểm chéo review, JSON và hai bài tự làm.
- Đã đọc đủ `2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf`, ưu tiên câu 3–4 để hiệu chỉnh cách hỏi về truthiness và chuỗi số CSV. `LTXLDL_AI_5.pdf`, `LTXLDL_DS_1.pdf`, `LTXLDL_DS_2.pdf` là nguồn phong cách chính; `LTXLDL_AI_1.pdf`, `LTXLDL_AI_2.pdf` bổ trợ Python thuần. Không lấy độ khó NumPy trong các đề để nâng mức Bài 2. Các đề ở thư mục [Bài_kiểm_tra](D:/LTXLDL_GK/Bài_kiểm_tra).

Không thiếu nguồn bắt buộc. Không mở rộng toàn bộ sách/tài liệu được dẫn link đọc thêm vào phạm vi. Không yêu cầu NumPy, pandas, SQL, API, regex, datetime chuyên sâu hoặc OOP nâng cao. Dùng dữ liệu giả lập nhỏ, không yêu cầu thuộc số của snapshot thật hay tải file lớn.

**Điểm nguồn cần hiệu chỉnh:** Lcell14 gọi giá hợp lệ là >0 nhưng dùng `if p["gia_so"]`; Lcell23 cũng dùng truthiness cho yêu cầu >0, Lcell25 dùng `not gia_so`. Số âm vẫn truthy nên các mẫu này chưa thực hiện đầy đủ quy tắc dương nếu dữ liệu có âm. Ngân hàng kiểm theo yêu cầu đã nêu và hành vi Python thực tế: khác None, truthy,>=0 và >0 không được đánh đồng. Lab T15–16 chủ động dùng `is not None` và giải thích phải giữ 0 khi quy tắc cho phép.

Tcell1 nói hoàn thành assert là đáp ứng yêu cầu; khi dùng làm chứng cứ, cần giữ đúng phạm vi điều assert đã kiểm. T30 chỉ kiểm các phòng có 0 review; không tự chứng minh chiều ngược. T37 gợi câu hỏi nguyên nhân giảm review; số đếm riêng không đủ kết luận nguyên nhân, và snapshot mới đến 29/06 không đại diện cả năm 2026.

G nói copy tạo bản sao độc lập trong ví dụ list phẳng. Câu có list các dict giải thích rõ list ngoài được tách, dict bên trong còn dùng chung; không yêu cầu deepcopy. Các câu JSON round-trip chỉ dùng dict khóa chuỗi, list, số, chuỗi, bool, None; không khẳng định giữ nguyên mọi kiểu Python.

## Quy ước chấm và kiểm chứng

Mức độ là tham số thiết kế, chưa đo thực nghiệm và không phải tỷ trọng chính thức của đề thi. Tự luận chấm 2 điểm/câu để luyện tập, không tự gán thang điểm này cho bài kiểm tra thật. Chấm từng ý; chấp nhận code, lời văn và cấu trúc dữ liệu đúng tương đương nếu thỏa yêu cầu. Có thể chia nhỏ điểm của một dòng tiêu chí khi người học mới đạt một phần; không trừ vì khác tên biến hoặc dùng một cách đúng khác.

Các đoạn chạy tay, biểu thức đúng, lời giải sửa và ca biên liên quan đã được thực thi bằng Python 3.12.14, chỉ thư viện chuẩn. Mỗi câu có namespace và thư mục thử riêng; dữ liệu file được tạo đúng nội dung đề, không dùng Internet. Câu có code cố ý lỗi được xác nhận đúng loại lỗi; không coi đó là kiểm thử thất bại. Dòng trạng thái từng câu phân biệt chạy code gốc với code kiểm bổ sung/lời giải. Sự thành công của các ca thử không được trình bày như chứng minh mọi dữ liệu đầu vào đều đúng.

## Ma trận 60 câu

| Nhóm chính | Nền tảng | Vận dụng | Phân loại | TN | TL | Tổng |
|---|---:|---:|---:|---:|---:|---:|
| 1. Kiểu dữ liệu, định dạng, list/dict/set/tuple | 7 | 5 | 0 | 7 | 5 | 12 |
| 2. Comprehension, zip, sắp xếp và sao chép | 0 | 11 | 1 | 9 | 3 | 12 |
| 3. Hàm làm sạch, chuyển kiểu, try/except | 2 | 5 | 5 | 7 | 5 | 12 |
| 4. Đọc/ghi văn bản, CSV và JSON | 4 | 6 | 2 | 9 | 3 | 12 |
| 5. Tổng hợp bằng dict, thống kê và kiểm tra dữ liệu | 0 | 5 | 3 | 5 | 3 | 8 |
| 6. pathlib, module và tổ chức pipeline | 2 | 1 | 1 | 3 | 1 | 4 |
| **Tổng** | **15** | **33** | **12** | **40** | **20** | **60** |

## Danh mục mục tiêu nhỏ và đối chiếu cả ba nguồn

Danh mục và kế hoạch đủ 60 câu được lập trước khi viết câu. G§ là mục bài giảng; L/T kèm số là chỉ mục cell từ 0 trong notebook, không phải thứ tự thực thi. Dấu —: nguồn đó không có đoạn trực tiếp. Cụm ngữ cảnh/áp dụng/giới hạn phân biệt diễn giải thiết kế với câu chữ của bài. Mỗi mục dưới đây có ít nhất một câu yêu cầu dùng kiến thức, không tính việc chỉ xuất hiện trong đáp án.

| Mã | Mục tiêu | G | L | T | Câu dự kiến / thực tế |
|---|---|---|---|---|---|
| K01 | Số khác chuỗi số; int/float và đầu vào không chuyển được | G§1,§3 | L2,13,21 | T11–13 | B2-001, B2-051 |
| K02 | None, 0,0.0, chuỗi rỗng và "0"; truthiness, kể cả số âm | G§1–2 | L14–15 | T5,15–16 | B2-002, B2-047 |
| K03 | Khác None khác truthy và khác >0; quy tắc giữ tập giá trị | G§1–2 | L14–15,22–25 | T15–16 | B2-047 |
| K04 | Trung bình dùng đúng tập và mẫu số, không lấy len toàn bảng | G§1 | L14 | T5,15,19 | B2-010, B2-047, B2-054 |
| K05 | f-string phân cách nghìn, số thập phân; không đổi số gốc | G§1 | L13,14,19 | T4,25,27 | B2-018, B2-021 |
| K06 | Định dạng phần trăm khác .1f + %; không nhân 100 hai lần | G§1 | — | T4,15 | B2-031 |
| K07 | Căn trái/phải và độ rộng cột khi in báo cáo | G§1 (ngữ cảnh định dạng) | — | T25,27,35–36 | B2-018 |
| K08 | List có thứ tự; chỉ mục đầu/cuối/âm; slicing không lấy stop | G§1 | L6 | T37 (chuỗi năm); kiến thức nền | B2-011, B2-041 |
| K09 | Dict tra cứu khóa; list các dict; d[k] và get khi thiếu khóa | G§1 | L2,5 | T9,11 | B2-008 |
| K10 | get mặc định chỉ dùng khi thiếu khóa, không thay None/0 hiện có | G§1 (cơ chế get) | L5 | T24 (ứng dụng get) | B2-008 |
| K11 | Set khử trùng, thành viên; sorted khi cần thứ tự | G§1 | L7,9 | T6 | B2-022, B2-028 |
| K12 | Chiều trừ set, giao, hợp và kết hợp phép toán | G§1 | L7 | T6 | B2-028 |
| K13 | Tuple là bộ giá trị/cặp; giải nén cặp dữ liệu | G§1 | — | T25,27 (items/cặp) | B2-012, B2-018, B2-038, B2-057 |
| K14 | Chọn list/dict/set/tuple theo thứ tự, tra cứu, tập mã hoặc bộ giá trị | G§1 bảng chọn cấu trúc | L4–11 | T6,9,24 | B2-038 |
| K15 | for-if-append tương đương comprehension giữ cả lọc và biến đổi | G§2 | L8–10,22–23 | T15,27 | B2-003, B2-048 |
| K16 | List comprehension lấy id theo quy tắc, giữ thứ tự | G§2 | L6,22–23,25 | T30 | B2-048 |
| K17 | Dict comprehension tạo ánh xạ id→giá/loại đúng chiều | G§2 | L10,22–23 | T27 | B2-048 |
| K18 | Set comprehension loại trùng rồi sắp xếp nếu cần | G§2 | L9 | T6 (ngữ cảnh) | B2-022 |
| K19 | zip ghép theo vị trí, không tự hiểu ý nghĩa nhãn | G§2 | — | — | B2-004, B2-032 |
| K20 | Sắp riêng một dãy làm sai cặp; ghép trước khi sắp cả cặp | G§2 zip (áp dụng) | — | T25 (cặp items) | B2-004, B2-032 |
| K21 | sorted/key/lambda/reverse và top-k; kết quả có thứ tự xác định | G§3 lambda | — | T25,27 | B2-012, B2-023, B2-032, B2-036, B2-042, B2-052, B2-057 |
| K22 | Sắp xếp chuỗi số khác sắp xếp theo số | G§4 CSV + §3 lambda | L18 | T11,25 (áp dụng) | B2-015, B2-042 |
| K23 | max với key trả bản ghi, không phải riêng trị lớn nhất | G§3 lambda (ngữ cảnh) | — | T20–22 | B2-023, B2-057 |
| K24 | Sắp dict.items theo khóa hoặc giá trị; giải nén cặp | G§2 dict,§3 lambda | L10 | T24–27 | B2-012, B2-036, B2-052 |
| K25 | Gán b=a thêm tên cho cùng list; sửa qua alias tác động gốc | G§2 | L11 | — | B2-019, B2-033 |
| K26 | copy tách list ngoài; dict bên trong còn dùng chung nếu chỉ copy ngoài | G§2 copy (giới hạn kỹ thuật) | L11 (list phẳng) | — | B2-019, B2-033 |
| K27 | Hàm nhỏ một việc, tên rõ, cùng đầu vào đoán được; không sửa lén biến ngoài | G§3 viết hàm tốt | L13,21 | T13,18,27 | B2-030, B2-034 |
| K28 | Đọc docstring/type hint: mô tả quy ước, không tự ép kiểu hay kiểm nghiệp vụ | G§3 | L13,21 | T13,18 | B2-014, B2-034 |
| K29 | Truyền hàm vào map; list(map(...)) tương đương comprehension áp hàm | G§3 hàm là giá trị | L13–14 | T13–15 | B2-024, B2-049 |
| K30 | replace dấu tiền/phân cách rồi float để chuyển chuỗi giá | G§3 clean_price | L13 | T12–13 (float không dấu tiền) | B2-005, B2-024, B2-058 |
| K31 | Chuyển kiểu thành công chưa bảo đảm nghiệp vụ; âm/0 theo quy tắc nêu rõ | G§2–3 | L13–15,22–25 | T13,15–16 | B2-005, B2-014, B2-029, B2-053 |
| K32 | ValueError/TypeError/AttributeError tùy thao tác thực tế, không đoán theo tên hàm | G§3 | L13,21 | T12–13 | B2-009, B2-013, B2-043, B2-053, B2-058 |
| K33 | Bắt đúng lỗi dữ liệu; bắt rộng có thể che lỗi lập trình; ca thử thường vẫn cần | G§3 try/except, AI | L13,21 | T12–13 | B2-009, B2-043 |
| K34 | Trả None khác trả 0 khi dữ liệu hỏng; ảnh hưởng thống kê | G§1,§3 | L13–15 | T13–16 | B2-029, B2-039 |
| K35 | Kiểm ca bình thường/rỗng/None/âm/0/sai định dạng; không suy từ vài assert | G AI kiểm chứng | L13,21 | T13,16 | B2-029, B2-039, B2-043, B2-053, B2-058 |
| K36 | Bảo vệ None trước so sánh số bằng điều kiện ngắn mạch | G§2–3 | L22–25 (cần sửa truthiness) | T15–16,27 | B2-003, B2-009, B2-049 |
| K37 | Tập giá sau lọc có thể rỗng; quy ước None hoặc không chia | G§1 trung bình (giới hạn) | L26 (quy ước cần nêu) | T18 không rỗng (điều kiện) | B2-010, B2-039, B2-049 |
| K38 | with open đóng file; UTF8 theo mã nguồn; đọc và ghi đè khác nhau | G§4 | L17–19 | T9,33 | B2-006, B2-025, B2-059 |
| K39 | DictReader tạo list dict, giá trị CSV thường là chuỗi | G§4 | L17–18 | T9–11,30 | B2-007, B2-015, B2-040, B2-059 |
| K40 | CSV ô trống là ""; "0" khác 0, không tự thành None | G§4 | L18 | T11–16,29–30 | B2-007, B2-040, B2-054 |
| K41 | Chuyển int/float trước lọc/tính/sắp theo số | G§4 | L21–23 | T11–15,21,30 | B2-015, B2-040, B2-054 |
| K42 | DictWriter/fieldnames/writeheader/writerow; trích dẫn dấu phẩy; newline="" | G§4 (CSV ngữ cảnh) | L17 | — | B2-026, B2-059 |
| K43 | json.dump/load qua file; json.loads nhận chuỗi JSON | G§4 | L19 | T33 | B2-016, B2-044 |
| K44 | JSON số/chuỗi/bool/None/list; null/true/false không là chuỗi tương ứng | G§4 | L19 | T33 | B2-016, B2-050 |
| K45 | ensure_ascii=False biểu diễn chữ; indent trình bày, không đổi kiểu số | G§4 | L19 | T33 | B2-035, B2-050 |
| K46 | Đọc lại JSON đối chiếu; equality không chứng minh nghiệp vụ; dữ liệu round-trip phù hợp | G§4 | L19 | T33 | B2-035, B2-050 |
| K47 | Đếm nhóm bằng dict + get(k, 0) | G§1–2 dict (ngữ cảnh) | L26 | T24 | B2-020 |
| K48 | Tổng bản ghi khác số có giá hợp lệ; đúng đơn vị quan sát và tập bản ghi | G§1,§3 | L14,26 | T15,33,35,37 | B2-010, B2-060 |
| K49 | Gom list giá từng khu bằng Python thuần | G§2–3 | L26 | T26–27 | B2-020 |
| K50 | sum/len; trung vị lẻ/chẵn sau sorted; sorted không sửa list đầu vào | G§1 trung bình | L14 | T17–19 | B2-027 |
| K51 | Giá lớn tác động trung bình; chưa đủ kết luận sai/xóa, cần kiểm chứng | — | L24 | T20–22,28 | B2-027 |
| K52 | Top khu đông nhất khác top giá cao nhất; chọn đúng tập trước so giá | G§3 lambda (áp dụng) | L26 | T24–28,35 | B2-036 |
| K53 | Ngưỡng số phòng có giá khác ngưỡng tổng số phòng của khu | G§1 dữ liệu thiếu (áp dụng) | L26 | T35–36 | B2-020 |
| K54 | QA vi phạm ít nhất một điều kiện: OR/hợp, không đếm trùng đối tượng | G§2 lọc (áp dụng) | L24–25 | T31 (kiểm dữ liệu) | B2-045 |
| K55 | Gắn cờ để kiểm khác xóa dòng ngay | — | L24–25 | T22 | B2-045 |
| K56 | Kiểm tra chéo number_of_reviews và last_review | — | — | T29–31 | B2-046 |
| K57 | Kiểm một chiều không chứng minh chiều ngược hoặc toàn bộ dữ liệu đúng | G AI kiểm chứng (ngữ cảnh) | — | T30–31 (giới hạn assert) | B2-046 |
| K58 | date[: 4] lấy năm; đếm review theo năm bằng dict cộng dồn | G§1 slicing (cơ chế) | — | T37–38 | B2-055, B2-060 |
| K59 | Năm giữa chừng khác năm trọn; số đếm không tự chứng minh xu hướng/nguyên nhân | — | — | T37 snapshot 29/06/2026 | B2-055, B2-060 |
| K60 | Path / nối đường dẫn; mkdir parents/exist_ok không xóa file cũ | G§4 pathlib | L17 | — | B2-017, B2-037 |
| K61 | Path.parent và glob ở mức cây thư mục, không phụ thuộc repr theo OS | G§4 pathlib | — | — | B2-037 |
| K62 | import module và from module import hàm: tên được dùng đúng cách | G§3 module | L17,19 | T9,33 | B2-030 |
| K63 | Gom hàm vào cleaning.py để dùng lại; đọc dấu chấm module/phương thức đã biết | G§3 dấu chấm, module | L13,17 | T13 | B2-030 |
| K64 | Ghép load_csv→summarize→save_json theo kiểu đầu vào/đầu ra | G§3 hàm | L26–27 | T33 | B2-056 |

## Kế hoạch từng câu

| Mã | Đợt | Nhóm chính | Dạng | Mức | Mục tiêu chính; phụ |
|---|---:|---:|---|---|---|
| B2-001 | 1 | 1 | TN | nền tảng | K01 |
| B2-002 | 1 | 1 | TN | nền tảng | K02 |
| B2-003 | 1 | 2 | TN | vận dụng | K15; K36 |
| B2-004 | 1 | 2 | TN | vận dụng | K19; K20 |
| B2-005 | 1 | 3 | TN | vận dụng | K30; K31 |
| B2-006 | 1 | 4 | TN | nền tảng | K38 |
| B2-007 | 1 | 4 | TN | vận dụng | K39; K40 |
| B2-008 | 1 | 1 | TL | vận dụng | K09; K10 |
| B2-009 | 1 | 3 | TL | phân loại | K32; K33; K36 |
| B2-010 | 1 | 5 | TL | phân loại | K04; K48; K37 |
| B2-011 | 2 | 1 | TN | nền tảng | K08 |
| B2-012 | 2 | 2 | TN | vận dụng | K21; K24; K13 |
| B2-013 | 2 | 3 | TN | vận dụng | K32 |
| B2-014 | 2 | 3 | TN | nền tảng | K28; K31 |
| B2-015 | 2 | 4 | TN | vận dụng | K39; K41; K22 |
| B2-016 | 2 | 4 | TN | vận dụng | K43; K44 |
| B2-017 | 2 | 6 | TN | nền tảng | K60 |
| B2-018 | 2 | 1 | TL | vận dụng | K07; K13; K05 |
| B2-019 | 2 | 2 | TL | phân loại | K25; K26 |
| B2-020 | 2 | 5 | TL | phân loại | K53; K49; K47 |
| B2-021 | 3 | 1 | TN | nền tảng | K05 |
| B2-022 | 3 | 2 | TN | vận dụng | K18; K11 |
| B2-023 | 3 | 2 | TN | vận dụng | K23; K21 |
| B2-024 | 3 | 3 | TN | nền tảng | K29; K30 |
| B2-025 | 3 | 4 | TN | vận dụng | K38 |
| B2-026 | 3 | 4 | TN | nền tảng | K42 |
| B2-027 | 3 | 5 | TN | vận dụng | K50; K51 |
| B2-028 | 3 | 1 | TL | vận dụng | K12; K11 |
| B2-029 | 3 | 3 | TL | phân loại | K31; K34; K35 |
| B2-030 | 3 | 6 | TL | phân loại | K62; K63; K27 |
| B2-031 | 4 | 1 | TN | nền tảng | K06 |
| B2-032 | 4 | 2 | TN | vận dụng | K19; K20; K21 |
| B2-033 | 4 | 2 | TN | vận dụng | K25; K26 |
| B2-034 | 4 | 3 | TN | vận dụng | K27; K28 |
| B2-035 | 4 | 4 | TN | nền tảng | K45; K46 |
| B2-036 | 4 | 5 | TN | vận dụng | K52; K24; K21 |
| B2-037 | 4 | 6 | TN | vận dụng | K61; K60 |
| B2-038 | 4 | 1 | TL | vận dụng | K14; K13 |
| B2-039 | 4 | 3 | TL | phân loại | K34; K35; K37 |
| B2-040 | 4 | 4 | TL | phân loại | K39; K40; K41 |
| B2-041 | 5 | 1 | TN | nền tảng | K08 |
| B2-042 | 5 | 2 | TN | vận dụng | K22; K21 |
| B2-043 | 5 | 3 | TN | vận dụng | K33; K35; K32 |
| B2-044 | 5 | 4 | TN | nền tảng | K43 |
| B2-045 | 5 | 5 | TN | vận dụng | K54; K55 |
| B2-046 | 5 | 5 | TN | vận dụng | K56; K57 |
| B2-047 | 5 | 1 | TL | vận dụng | K03; K02; K04 |
| B2-048 | 5 | 2 | TL | vận dụng | K16; K17; K15 |
| B2-049 | 5 | 3 | TL | phân loại | K29; K36; K37 |
| B2-050 | 5 | 4 | TL | phân loại | K44; K45; K46 |
| B2-051 | 6 | 1 | TN | nền tảng | K01 |
| B2-052 | 6 | 2 | TN | vận dụng | K24; K21 |
| B2-053 | 6 | 3 | TN | vận dụng | K32; K31; K35 |
| B2-054 | 6 | 4 | TN | vận dụng | K40; K41; K04 |
| B2-055 | 6 | 5 | TN | vận dụng | K58; K59 |
| B2-056 | 6 | 6 | TN | nền tảng | K64 |
| B2-057 | 6 | 2 | TL | vận dụng | K23; K21; K13 |
| B2-058 | 6 | 3 | TL | phân loại | K30; K32; K35 |
| B2-059 | 6 | 4 | TL | vận dụng | K42; K38; K39 |
| B2-060 | 6 | 5 | TL | phân loại | K58; K59; K48 |

## Đáp án trắc nghiệm nhanh

| Đợt | Đáp án |
|---|---|
| 1 | B2-001 **B**; B2-002 **A**; B2-003 **C**; B2-004 **A**; B2-005 **B**; B2-006 **D**; B2-007 **B** |
| 2 | B2-011 **A**; B2-012 **C**; B2-013 **B**; B2-014 **C**; B2-015 **C**; B2-016 **C**; B2-017 **B** |
| 3 | B2-021 **C**; B2-022 **A**; B2-023 **C**; B2-024 **B**; B2-025 **B**; B2-026 **C**; B2-027 **A** |
| 4 | B2-031 **D**; B2-032 **A**; B2-033 **D**; B2-034 **D**; B2-035 **A**; B2-036 **B**; B2-037 **D** |
| 5 | B2-041 **B**; B2-042 **A**; B2-043 **D**; B2-044 **C**; B2-045 **A**; B2-046 **D** |
| 6 | B2-051 **D**; B2-052 **D**; B2-053 **B**; B2-054 **C**; B2-055 **D**; B2-056 **A** |
## Đợt 1 — Đáp án và hướng dẫn chấm

### B2-001 — B

Cộng hai chuỗi là nối thành "123"; sau chuyển kiểu, 12 + 3.0 là 15.0.

- **A sai:** Tự coi phép cộng chuỗi đầu tiên là cộng số.
- **C sai:** Bỏ qua việc int/float chuyển chuỗi sang số trước phép cộng thứ hai.
- **D sai:** Đảo cơ chế cộng chuỗi và cộng số.

**Mục tiêu:** nhóm chính 1; chính K01. **Mức:** nền tảng. **Bẫy:** Nhầm biểu diễn số bằng chuỗi với số dùng tính toán.

**Đọc lại:** G§1,§3; L2,13,21; T11–13.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-002 — A

None, số 0 và chuỗi rỗng là falsy; "0" là chuỗi không rỗng, số âm khác 0 là truthy.

- **B sai:** Coi chuỗi "0" như số 0 khi kiểm truthiness.
- **C sai:** Coi truthy là phải lớn hơn 0, nên loại nhầm số âm.
- **D sai:** Coi số 0 là truthy chỉ vì nó là dữ liệu đã biết.

**Mục tiêu:** nhóm chính 1; chính K02. **Mức:** nền tảng. **Bẫy:** Trộn quy tắc nghiệp vụ với truthiness.

**Đọc lại:** G§1–2; L14–15; T5,15–16.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-003 — C

Phải giữ cả điều kiện bảo vệ None, giữ 0 và phép đổi đơn vị; kết quả [1.2,0.0,2.4].

- **A sai:** Lọc đúng nhưng chưa đổi từ gam sang kg.
- **B sai:** Tự loại kiện có khối lượng0 đang được đề cho hợp lệ.
- **D sai:** Loại0 nhưng giữ -10; truthy không thay được quy tắc không âm.

**Mục tiêu:** nhóm chính 2; chính K15; phụ K36. **Mức:** vận dụng. **Bẫy:** Đúng bước lọc nhưng quên biến đổi, hoặc dùng sai tập được giữ.

**Đọc lại:** G§2; L8–10,22–23; T15,27; G§2–3; L22–25 (cần sửa truthiness); T15–16,27.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-004 — A

Sắp tên thành K1, K2, K3 rồi zip theo vị trí với4,9,2; quan hệ gốc đã sai, zip không tự tìm đúng kho.

- **B sai:** Tưởng zip tự dùng quan hệ kho/số kiện ban đầu dù tên đã được sắp riêng.
- **C sai:** Đọc từ cuối dãy số kiện thay vì ghép theo cùng chỉ mục.
- **D sai:** Sắp độc lập cả dãy số kiện tăng dần trước khi ghép với tên đã sắp.

**Mục tiêu:** nhóm chính 2; chính K19; phụ K20. **Mức:** vận dụng. **Bẫy:** Sắp riêng nhãn rồi tưởng zip khôi phục cặp ban đầu.

**Đọc lại:** G§2; G§2 zip (áp dụng); T25 (cặp items).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-005 — B

replace rồi float chuyển được -5 và 0; hàm chưa có điều kiện nghiệp vụ để loại giá âm. Chuỗi rỗng phát sinh ValueError và trả None.

- **A sai:** Gán cho hàm một quy tắc loại âm mà thân hàm chưa viết.
- **C sai:** Tưởng chuỗi rỗng được float chuyển thành 0 thay vì báo lỗi.
- **D sai:** Tưởng chuyển kiểu đã bao gồm việc loại mọi giá không dương.

**Mục tiêu:** nhóm chính 3; chính K30; phụ K31. **Mức:** vận dụng. **Bẫy:** Chuyển được sang float bị nhầm là đã đạt quy tắc giá.

**Đọc lại:** G§3 clean_price; L13; T12–13 (float không dấu tiền); G§2–3; L13–15,22–25; T13,15–16.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-006 — D

with đã đóng file khi ra khỏi khối; chuỗi đã đọc vẫn tồn tại trong text.

- **A sai:** Tưởng with chỉ mở file và cần gọi close riêng.
- **B sai:** Tưởng đóng file tự xóa giá trị chuỗi đã đọc.
- **C sai:** Nhầm cả trạng thái file và dữ liệu đã đọc.

**Mục tiêu:** nhóm chính 4; chính K38. **Mức:** nền tảng. **Bẫy:** Nhầm vòng đời file mở với dữ liệu đọc vào bộ nhớ.

**Đọc lại:** G§4; L17–19; T9,33.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-007 — B

DictReader giữ luot là chuỗi; không chuỗi nào bằng số 0, còn hai dòng có chuỗi "0".

- **A sai:** Tưởng DictReader tự đổi chuỗi số sang số nguyên.
- **C sai:** Đảo vai trò so với số 0 và chuỗi "0".
- **D sai:** Nhận ra kiểu chuỗi nhưng bỏ qua hai chuỗi "0" trong file.

**Mục tiêu:** nhóm chính 4; chính K39; phụ K40. **Mức:** vận dụng. **Bẫy:** CSV đọc lên là chuỗi nhưng lại so với số.

**Đọc lại:** G§4; L17–18; T9–11,30; L18; T11–16,29–30.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-008

Output là `[None,0,5]`: mặc định5 chỉ áp dụng khi thiếu khóa. `c["phi"]` gây KeyError, còn get trả 5; get không tự thay None hay0 đã được lưu.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Output đúng None, 0,5 theo thứ tự | 1 |
| Phân biệt KeyError với get mặc định; nêu chỉ dùng mặc định khi thiếu khóa | 1 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 1; chính K09; phụ K10. **Mức:** vận dụng. **Bẫy:** get mặc định không phải phép điền mọi giá trị thiếu hoặc falsy.

**Đọc lại:** G§1; L2,5; T9,11; G§1 (cơ chế get); L5; T24 (ứng dụng get).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-009

(a) float(None) phát sinh TypeError, chưa bị bắt. (b) Đổi thành `except (ValueError,TypeError):` rồi lọc `[x for x in v if x is not None and x > 0]`, được `[8.0]`. (c) "0" và "-2" đổi được thành 0.0,-2.0 nhưng đều bị loại theo quy tắc >0.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Chỉ đúng TypeError ở float(None), không chỉ nói lỗi dữ liệu | 0,5 |
| Bắt ValueError/TypeError và giữ None khi hỏng | 0,5 |
| Lọc bảo vệ None trước >0 và kết quả [8.0] | 0,5 |
| Hai ca chuyển được nhưng không đạt >0, như0 và âm | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 3; chính K32; phụ K33, K36. **Mức:** phân loại. **Bẫy:** Bắt sai lỗi và quên bảo vệ None; chuyển số chưa bảo đảm nghiệp vụ.

**Đọc lại:** G§3; L13,21; T12–13; G§3 try/except, AI; G§2–3; L22–25 (cần sửa truthiness); T15–16,27.

**Kiểm chứng:** đã chạy code gốc, xác nhận TypeError tại thao tác giải thích ở trên; đã chạy lời giải sửa và ca biên liên quan.

### B2-010

Code in 30.0 do vẫn chia 4 dòng trong khi chỉ có 3 giá đã biết. Sửa thành `sum(co_gia)/len(co_gia)` được 40.0, giữ giá 0 hợp lệ. Nếu danh sách rỗng thì không chia; chẳng hạn đặt `tb = sum(co_gia)/len(co_gia) if co_gia else None` và ghi rõ quy ước chưa có trung bình.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| 30.0 và sai mẫu số 4 thay vì3 | 0,75 |
| Đúng mẫu số và 40.0, giữ 0 | 0,75 |
| Tập rỗng không chia, quy ước đầu ra rõ | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 5; chính K04; phụ K48, K37. **Mức:** phân loại. **Bẫy:** Lọc đúng tử số nhưng chia theo toàn bảng; quên trường hợp không có giá.

**Đọc lại:** G§1; L14; T5,15,19; G§1,§3; L14,26; T15,33,35,37; G§1 trung bình (giới hạn); L26 (quy ước cần nêu); T18 không rỗng (điều kiện).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### Cập nhật bao phủ sau đợt 1

Lũy kế 10/60 câu: 7 TN, 3 TL.

| Nhóm | Đã có / kế hoạch |
|---|---:|
| 1 | 3 / 12 |
| 2 | 2 / 12 |
| 3 | 2 / 12 |
| 4 | 2 / 12 |
| 5 | 1 / 8 |
| 6 | 0 / 4 |

Mục đã có câu thực sự kiểm tra: K01, K02, K04, K09, K10, K15, K19, K20, K30, K31, K32, K33, K36, K37, K38, K39, K40, K48.
Mục chưa có câu: K03, K05, K06, K07, K08, K11, K12, K13, K14, K16, K17, K18, K21, K22, K23, K24, K25, K26, K27, K28, K29, K34, K35, K41, K42, K43, K44, K45, K46, K47, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64.
Mục tiếp tục có nhánh/biến thể ở đợt sau: K01, K02, K04, K15, K19, K20, K30, K31, K32, K33, K36, K37, K38, K39, K40, K48. Không dùng số mục đã chạm để suy mọi nhánh đã hoàn tất trước đợt cuối.

## Đợt 2 — Đáp án và hướng dẫn chấm

### B2-011 — A

Ba ngày cần lấy chỉ mục 1,2,3; stop 4 không được lấy. Tổng là 20.

- **B sai:** Bỏ ngày thứ Năm vì stop 3 không được lấy.
- **C sai:** Dịch cả khoảng sang thứ Tư đến thứ Sáu.
- **D sai:** Lấy thêm thứ Hai, thành bốn ngày.

**Mục tiêu:** nhóm chính 1; chính K08. **Mức:** nền tảng. **Bẫy:** Slicing không lấy stop; ngày thứ hai ứng với chỉ mục 1.

**Đọc lại:** G§1; L6; T37 (chuỗi năm); kiến thức nền.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-012 — C

Mỗi phần tử items là cặp (khóa, giá trị); key lấy số phòng, reverse=True giảm dần rồi lấy hai cặp đầu.

- **A sai:** Sắp theo tên khu thay vì số phòng.
- **B sai:** Sắp số phòng tăng dần vì bỏ reverse=True.
- **D sai:** Nhầm sorted các cặp trả riêng giá trị của key.

**Mục tiêu:** nhóm chính 2; chính K21; phụ K24, K13. **Mức:** vận dụng. **Bẫy:** Nhầm đối tượng được sắp với giá trị dùng làm khóa sắp.

**Đọc lại:** G§3 lambda; T25,27; G§2 dict,§3 lambda; L10; T24–27; G§1; T25,27 (items/cặp).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-013 — B

float không nhận None như một số/chuỗi số; None cũng không có phương thức replace. Lỗi phụ thuộc thao tác, không phải tên cột.

- **A sai:** Gán lỗi của float("N/A") cho float(None).
- **C sai:** Tưởng chưa tới float mà gọi replace trên None cũng là lỗi chuyển giá trị số.
- **D sai:** Đảo thao tác gọi hàm chuyển kiểu và tra phương thức.

**Mục tiêu:** nhóm chính 3; chính K32. **Mức:** vận dụng. **Bẫy:** Loại lỗi được quyết định bởi thao tác thực tế.

**Đọc lại:** G§3; L13,21; T12–13.

**Kiểm chứng:** đã chạy code gốc, xác nhận TypeError tại thao tác giải thích ở trên; đã chạy lời giải sửa và ca biên liên quan.

### B2-014 — C

Docstring và thân hàm mô tả chuyển kiểu; type hint không chặn số âm. Quy tắc dương cần bước kiểm riêng.

- **A sai:** int bao gồm số âm; type hint không làm kiểm tra nghiệp vụ.
- **B sai:** int(None) phát sinh TypeError, hàm trả None.
- **D sai:** Chuỗi "-2" chuyển được sang số nguyên -2.

**Mục tiêu:** nhóm chính 3; chính K28; phụ K31. **Mức:** nền tảng. **Bẫy:** Đọc type hint như bộ ép kiểu/kiểm tra dương tự động.

**Đọc lại:** G§3; L13,21; T13,18; G§2–3; L13–15,22–25; T13,15–16.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-015 — C

Chuỗi tăng dần là "100","20","3","8". Hai mã C, B được chọn, chưa phải hai lượt có số đêm nhỏ nhất.

- **A sai:** Tự giả định dem đã được chuyển thành int.
- **B sai:** Đọc như sắp chuỗi giảm dần thay vì tăng dần.
- **D sai:** Tưởng sorted chỉ lấy hai dòng đầu theo thứ tự file.

**Mục tiêu:** nhóm chính 4; chính K39; phụ K41, K22. **Mức:** vận dụng. **Bẫy:** Sắp chuỗi số như thể đã có dữ liệu số.

**Đọc lại:** G§4; L17–18; T9–11,30; L21–23; T11–15,21,30; G§4 CSV + §3 lambda; L18; T11,25 (áp dụng).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-016 — C

Số 4 thành int, null thành None, true/false thành True/False; phần tử có dấu nháy "null" vẫn là chuỗi.

- **A sai:** Nhầm null không có dấu nháy cũng thành chuỗi.
- **B sai:** Giữ nguyên true/false của văn bản JSON thay vì bool Python.
- **D sai:** Tưởng số 4 trong JSON được đọc thành chuỗi "4" như CSV.

**Mục tiêu:** nhóm chính 4; chính K43; phụ K44. **Mức:** vận dụng. **Bẫy:** Nhầm ký hiệu JSON với chuỗi hoặc cú pháp bool của Python.

**Đọc lại:** G§4; L19; T33.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-017 — B

parents hỗ trợ tạo cha khi cần; exist_ok cho phép đích là thư mục đã tồn tại, không xóa file hay cây cũ.

- **A sai:** Nhầm mkdir thành lệnh xóa và dựng lại.
- **C sai:** Bỏ qua exist_ok=True khi đích đã là thư mục.
- **D sai:** Bỏ qua parents=True cho phép tạo thư mục cha còn thiếu.

**Mục tiêu:** nhóm chính 6; chính K60. **Mức:** nền tảng. **Bẫy:** mkdir(exist_ok=True) không phải thao tác reset dữ liệu.

**Đọc lại:** G§4 pathlib; L17.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-018

```text
|An   | 1,200|
```
Tên có ba dấu cách sau An; số có một dấu cách trước 1,200. n vẫn là số nguyên 1200; định dạng không sửa giá trị gốc.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Giải nén đúng và căn tên đủ rộng 5: ba dấu cách | 0,75 |
| Số 1,200 căn phải rộng 6: một dấu cách đầu | 0,75 |
| n vẫn là int 1200, không thành chuỗi hoặc thay giá trị | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 1; chính K07; phụ K13, K05. **Mức:** vận dụng. **Bẫy:** Độ rộng là tối thiểu của cả trường đã định dạng, không phải số dấu cách.

**Đọc lại:** G§1 (ngữ cảnh định dạng); T25,27,35–36; G§1; T25,27 (items/cặp); L13,14,19; T4,25,27.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-019

In `4 0 5`: list ngoài đã tách, nhưng dict phòng 1 còn được dùng chung, nên đổi trường gia tác động cả a. append chỉ thêm vào list b. Với các dict phẳng đã cho, có thể tạo `b = [{"id":r["id"],"gia":r["gia"]} for r in a]` trước mọi phép sửa; hoặc copy từng dict, không chỉ copy list ngoài.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Kết quả4,0,5 đúng | 0,75 |
| Tách list ngoài nhưng dùng chung dict; append không thêm vào a | 0,75 |
| Tạo dict mới cho mỗi dòng trước khi sửa; chấp nhận [r.copy() for r in a] với dữ liệu phẳng | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 2; chính K25; phụ K26. **Mức:** phân loại. **Bẫy:** Coi copy list là sao chép sâu cả các dict chứa bên trong.

**Đọc lại:** G§2; L11; G§2 copy (giới hạn kỹ thuật); L11 (list phẳng).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-020

Code chọn A, B do đếm mọi phòng; thực tế A có 1 giá >0, B có 2 nên chỉ B đạt. Có thể sửa:
```python
def gia_khu(ten):
    return [r["gia"] for r in rows if r["khu"] == ten
            and r["gia"] is not None and r["gia"] > 0]
chon = sorted(k for k in dem if len(gia_khu(k)) >= 2)
```
gia_khu("B") là `[40,80]`; các phòng thiếu hoặc giá 0 vẫn là phòng nhưng không thuộc tập giá hợp lệ của xếp hạng này.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Hiện tại A, B; đúng chỉ B vì A1/B2 giá hợp lệ | 0,75 |
| Hàm gom đúng khu, bỏ None và giá<=0, trả list; chọn theo len list | 0,75 |
| B có [40,80], phân biệt tổng dòng với số giá | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 5; chính K53; phụ K49, K47. **Mức:** phân loại. **Bẫy:** Chọn đúng thao tác đếm nhưng trên sai tập bản ghi.

**Đọc lại:** G§1 dữ liệu thiếu (áp dụng); L26; T35–36; G§2–3; T26–27; G§1–2 dict (ngữ cảnh); T24.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### Cập nhật bao phủ sau đợt 2

Lũy kế 20/60 câu: 14 TN, 6 TL.

| Nhóm | Đã có / kế hoạch |
|---|---:|
| 1 | 5 / 12 |
| 2 | 4 / 12 |
| 3 | 4 / 12 |
| 4 | 4 / 12 |
| 5 | 2 / 8 |
| 6 | 1 / 4 |

Mục đã có câu thực sự kiểm tra: K01, K02, K04, K05, K07, K08, K09, K10, K13, K15, K19, K20, K21, K22, K24, K25, K26, K28, K30, K31, K32, K33, K36, K37, K38, K39, K40, K41, K43, K44, K47, K48, K49, K53, K60.
Mục chưa có câu: K03, K06, K11, K12, K14, K16, K17, K18, K23, K27, K29, K34, K35, K42, K45, K46, K50, K51, K52, K54, K55, K56, K57, K58, K59, K61, K62, K63, K64.
Mục tiếp tục có nhánh/biến thể ở đợt sau: K01, K02, K04, K05, K08, K13, K15, K19, K20, K21, K22, K24, K25, K26, K28, K30, K31, K32, K33, K36, K37, K38, K39, K40, K41, K43, K44, K48, K60. Không dùng số mục đã chạm để suy mọi nhánh đã hoàn tất trước đợt cuối.

## Đợt 3 — Đáp án và hướng dẫn chấm

### B2-021 — C

Dấu phẩy nhóm hàng nghìn; .0f hiển thị không có phần thập phân, làm tròn12340.75 thành 12341 khi hiển thị. gia vẫn là số ban đầu.

- **A sai:** Tưởng định dạng s đồng thời làm tròn giá trị gốc gia.
- **B sai:** Bỏ qua dấu phẩy phân cách nghìn.
- **D sai:** Dùng hiệu ứng .2f thay vì .0f.

**Mục tiêu:** nhóm chính 1; chính K05. **Mức:** nền tảng. **Bẫy:** Định dạng báo cáo không sửa dữ liệu số gốc.

**Đọc lại:** G§1; L13,14,19; T4,25,27.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-022 — A

Set comprehension bỏ trùng loạiB; sorted tạo thứ tự A, B, C; D không có trong tập.

- **B sai:** Coi comprehension dùng ngoặc nhọn vẫn tạo list giữ trùng và thứ tự dòng.
- **C sai:** Có sắp xếp nhưng chưa hiểu set đã loại trùng.
- **D sai:** Nhầm kiểm thành viên với việc D có thể là một nhãn loại trong miền dữ liệu.

**Mục tiêu:** nhóm chính 2; chính K18; phụ K11. **Mức:** vận dụng. **Bẫy:** Set loại trùng; thứ tự cần qua sorted, không dựa vào repr của set.

**Đọc lại:** G§2; L9; T6 (ngữ cảnh); G§1; L7,9; T6.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-023 — C

max trả bản ghi có khóa gia lớn nhất, nên vẫn tra được id và gia của cùng phòng.

- **A sai:** Lấy phòng có id lớn nhất hoặc dòng cuối thay vì key gia.
- **B sai:** Chọn cực tiểu thay vì cực đại.
- **D sai:** Nhầm max trả riêng giá trị của hàm key; thực tế p là dict.

**Mục tiêu:** nhóm chính 2; chính K23; phụ K21. **Mức:** vận dụng. **Bẫy:** max với key trả phần tử gốc, không chỉ trả khóa so sánh.

**Đọc lại:** G§3 lambda (ngữ cảnh); T20–22; G§3 lambda; T25,27.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-024 — B

Đối số đầu map là chính hàm, chưa gọi; list thu các kết quả áp hàm lên từng chuỗi.

- **A sai:** Gọi hàm ngay mà thiếu đối số s, phát sinh TypeError trước khi map chạy.
- **C sai:** Gọi hàm một lần trên cả list; list không có phương thức replace.
- **D sai:** Tạo list chứa các tham chiếu hàm, chưa áp hàm lên s.

**Mục tiêu:** nhóm chính 3; chính K29; phụ K30. **Mức:** nền tảng. **Bẫy:** Nhầm truyền hàm vào map với gọi hàm ngay hoặc chỉ lấy tên hàm.

**Đọc lại:** G§3 hàm là giá trị; L13–14; T13–15; G§3 clean_price; L13; T12–13 (float không dấu tiền).

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-025 — B

Mở w ghi đè nội dung file; biến truoc đã nhận chuỗi cũ nên không bị đổi theo file.

- **A sai:** Tưởng biến truoc giữ liên kết sống với nội dung file.
- **C sai:** Nhầm ghi đè w với ghi nối.
- **D sai:** Tưởng with chỉ đóng file mà không lưu nội dung đã ghi.

**Mục tiêu:** nhóm chính 4; chính K38. **Mức:** vận dụng. **Bẫy:** Nhầm đọc dữ liệu vào biến, ghi đè và ghi nối.

**Đọc lại:** G§4; L17–19; T9,33.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-026 — C

fieldnames quyết định cột và writeheader ghi tiêu đề. Giá có dấu phẩy được đặt trong dấu nháy để không thành hai trường; newline="" để csv quản lý xuống dòng.

- **A sai:** Bỏ trích dẫn trường có dấu phẩy, khiến dòng giống ba trường.
- **B sai:** Bỏ qua writeheader đã ghi dòng tên cột.
- **D sai:** Tưởng DictWriter tự làm sạch giá và chuyển chuỗi tiền thành số.

**Mục tiêu:** nhóm chính 4; chính K42. **Mức:** nền tảng. **Bẫy:** Nhầm dấu phẩy trong trường với dấu phân cách cột.

**Đọc lại:** G§4 (CSV ngữ cảnh); L17.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-027 — A

List lẻ cho 5; list chẵn sắp 10,20,30,140 có trung vị 25 và trung bình 50. sorted tạo list mới nên gia[0] vẫn140; chênh lệch hai thống kê không tự xác nhận lỗi dữ liệu.

- **B sai:** sorted trong hàm tạo list mới, không sắp tại chỗ gia.
- **C sai:** Đảo trung bình 50 và trung vị 25.
- **D sai:** Không có lệnh loại140; giá lớn không tự bị hàm trung vị xóa.

**Mục tiêu:** nhóm chính 5; chính K50; phụ K51. **Mức:** vận dụng. **Bẫy:** Trung bình khác trung vị; sorted không sửa đầu vào; ngoại lai cần kiểm chứng.

**Đọc lại:** G§1 trung bình; L14; T17–19; L24; T20–22,28.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-028

Hiện in `[15,16]`, là mã mới thêm chứ không phải biến mất. Sửa `bien_mat = cu - moi`, được `[11,12]` sau sorted. Biểu thức cuối cho `[11,12,15,16]`, gồm mã chỉ có ở một trong hai đợt (cả biến mất lẫn mới thêm), không gồm mã còn ở cả hai.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Output hiện tại và ý nghĩa mới thêm đúng | 0,5 |
| Sửa đúng chiều, xác định11,12 | 0,75 |
| Kết hợp hợp-trừ-giao cho 11,12,15,16 và giải thích | 0,75 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 1; chính K12; phụ K11. **Mức:** vận dụng. **Bẫy:** Đảo chiều trừ set; nhầm mọi thay đổi với chỉ mã mới hoặc chỉ mã mất.

**Đọc lại:** G§1; L7; T6; L7,9.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-029

In `[30.0,-3.0] 13.5`: truthiness bỏ 0 hợp lệ và giữ giá âm. Sửa `[x for x in v if x is not None and x >= 0]`, được `[30.0,0.0]`, trung bình 15.0. Cần ca "$0" và "$-3" (hoặc các giá 0/âm tương đương); các ca chuỗi hỏng chỉ kiểm chuyển kiểu chưa kiểm quy tắc này.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Output và cả hai lỗi giữ âm/mất0 | 0,75 |
| Điều kiện đúng, bảo vệ None, trung bình 15.0 | 0,75 |
| Hai ca 0 và âm, phân biệt chuyển kiểu với hợp lệ | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 3; chính K31; phụ K34, K35. **Mức:** phân loại. **Bẫy:** if x vừa làm mất giá 0 hợp lệ vừa giữ số âm không hợp lệ.

**Đọc lại:** G§2–3; L13–15,22–25; T13,15–16; G§1,§3; L13–15; T13–16; G AI kiểm chứng; L13,21; T13,16.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-030

File chính gặp NameError vì chỉ tên clean_price được nhập, chưa có tên cleaning. Sửa lời gọi thành `clean_price("$80")`, hoặc dùng `import cleaning` và giữ lời gọi cũ; đều cho 80.0. Module cho nhiều bước dùng chung hàm chuyển giá; replace là phương thức của chuỗi s, hàm này không sửa biến ngoài.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| NameError ở tên cleaning, không nhầm thiếu file/module | 0,5 |
| Một cách import/lời gọi khớp nhau và 80.0 | 0,75 |
| Tái sử dụng hàm một việc; replace thuộc chuỗi, không sửa lén biến ngoài | 0,75 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 6; chính K62; phụ K63, K27. **Mức:** phân loại. **Bẫy:** from module import hàm không tạo tên module trong không gian gọi.

**Đọc lại:** G§3 module; L17,19; T9,33; G§3 dấu chấm, module; L13,17; T13; G§3 viết hàm tốt; L13,21; T13,18,27.

**Kiểm chứng:** đã chạy code gốc, xác nhận NameError tại thao tác giải thích ở trên; đã chạy lời giải sửa và ca biên liên quan.

### Cập nhật bao phủ sau đợt 3

Lũy kế 30/60 câu: 21 TN, 9 TL.

| Nhóm | Đã có / kế hoạch |
|---|---:|
| 1 | 7 / 12 |
| 2 | 6 / 12 |
| 3 | 6 / 12 |
| 4 | 6 / 12 |
| 5 | 3 / 8 |
| 6 | 2 / 4 |

Mục đã có câu thực sự kiểm tra: K01, K02, K04, K05, K07, K08, K09, K10, K11, K12, K13, K15, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K47, K48, K49, K50, K51, K53, K60, K62, K63.
Mục chưa có câu: K03, K06, K14, K16, K17, K45, K46, K52, K54, K55, K56, K57, K58, K59, K61, K64.
Mục tiếp tục có nhánh/biến thể ở đợt sau: K01, K02, K04, K08, K13, K15, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K48, K60. Không dùng số mục đã chạm để suy mọi nhánh đã hoàn tất trước đợt cuối.

## Đợt 4 — Đáp án và hướng dẫn chấm

### B2-031 — D

Đuôi % tự nhân 100 để hiển thị; .1f chỉ định dạng số 0.04 thành 0.0 rồi ghép ký tự %. Không có phép gán sửa p.

- **A sai:** Tưởng chỉ ghép ký tự % cũng tự đổi tỷ lệ sang phần trăm.
- **B sai:** Bỏ qua phép đổi thang của đuôi định dạng %.
- **C sai:** Nhân thêm 100 ngoài hiệu ứng của định dạng và nhầm f cũng đổi thang.

**Mục tiêu:** nhóm chính 1; chính K06. **Mức:** nền tảng. **Bẫy:** Nhầm .1% với .1f kèm ký tự %, hoặc nhân 100 thêm lần nữa.

**Đọc lại:** G§1; T4,15.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-032 — A

Ghép các cặp gốc trước, sau đó sắp theo giá và lấy hai cặp: P3–10, P2–20.

- **B sai:** Sắp riêng giá làm P4 bị ghép với10.
- **C sai:** Sắp riêng mã làm P1 bị ghép với50.
- **D sai:** Sắp theo mã chọn P1–40, P2–20, không phải hai phòng rẻ nhất.

**Mục tiêu:** nhóm chính 2; chính K19; phụ K20, K21. **Mức:** vận dụng. **Bẫy:** Ghép theo vị trí và chỉ sắp cả cặp; không tự suy quan hệ từ tên.

**Đọc lại:** G§2; G§2 zip (áp dụng); T25 (cặp items); G§3 lambda; T25,27.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-033 — D

b và a cùng list nên sửa b[1] sửa a; c là list ngoài khác, được tạo trước lúc đổi3 thành 9.

- **A sai:** Tưởng gán b=a đã sao chép.
- **B sai:** Tưởng c vẫn là alias của a và hai thao tác đều lan sang cả hai.
- **C sai:** Hiểu append tách biệt nhưng tưởng sửa a còn lan sang bản copy phẳng c.

**Mục tiêu:** nhóm chính 2; chính K25; phụ K26. **Mức:** vận dụng. **Bẫy:** Phân biệt alias và copy của list số phẳng.

**Đọc lại:** G§2; L11; G§2 copy (giới hạn kỹ thuật); L11 (list phẳng).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-034 — D

Hàm đã chuyển được nhưng có tác động ngoài qua append. Type hint/docstring không tự bảo đảm tính chất không sửa biến ngoài.

- **A sai:** Type hint mô tả kiểu dự kiến, không chặn append vào list ngoài.
- **B sai:** Hint nằm ở đầu ra và không ép kiểm tra đầu vào; float("10") thành công.
- **C sai:** Đúng giá trị trả về chưa đủ đáp ứng điều kiện không sửa ngoài.

**Mục tiêu:** nhóm chính 3; chính K27; phụ K28. **Mức:** vận dụng. **Bẫy:** Hàm trả kết quả đúng nhưng còn vi phạm một phần giao ước.

**Đọc lại:** G§3 viết hàm tốt; L13,21; T13,18,27; G§3; T13,18.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-035 — A

ensure_ascii=False cho chữ không ASCII được ghi trực tiếp; indent dùng khoảng trắng/xuống dòng. Số 2 vẫn đọc lại thành số.

- **B sai:** Cờ này không quyết định kiểu số khi đọc JSON.
- **C sai:** Nhầm JSON với giá trị trường CSV qua DictReader.
- **D sai:** indent là độ thụt dòng, không phải định dạng số .2f.

**Mục tiêu:** nhóm chính 4; chính K45; phụ K46. **Mức:** nền tảng. **Bẫy:** Nhầm biểu diễn ký tự/độ thụt dòng với kiểu dữ liệu.

**Đọc lại:** G§4; L19; T33.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-036 — B

Hai khu đông nhất là A, C; trong tập này C có giá trung vị 50 cao hơn 20 của A. B đắt nhất toàn bộ nhưng không thuộc tập được xét.

- **A sai:** Chọn giá cao nhất toàn bộ khu, bỏ điều kiện hai khu đông nhất.
- **C sai:** Dừng ở khu đông nhất mà chưa so giá trong tập hai khu.
- **D sai:** Chọn khu ít phòng nhất do đọc chiều sắp xếp ngược.

**Mục tiêu:** nhóm chính 5; chính K52; phụ K24, K21. **Mức:** vận dụng. **Bẫy:** Đúng thao tác max nhưng có thể dùng sai tập khu.

**Đọc lại:** G§3 lambda (áp dụng); L26; T24–28,35; G§2 dict,§3 lambda; L10; T24–27; G§3 lambda; T25,27.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-037 — D

parent của HaNoi là data/raw; glob("*.csv") chỉ khớp các file CSV ngay ở đó, không tự đi vào hai thư mục con.

- **A sai:** Dùng DATA thay vì DATA.parent.
- **B sai:** Tưởng glob mẫu *.csv tự tìm đệ quy qua mọi thư mục con.
- **C sai:** Bỏ qua mẫu *.csv và tưởng trả tên các thư mục con.

**Mục tiêu:** nhóm chính 6; chính K61; phụ K60. **Mức:** vận dụng. **Bẫy:** Nhầm đường dẫn cha hoặc mức duyệt của glob.

**Đọc lại:** G§4 pathlib; L17.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-038

Lần lượt dùng list, dict, set và tuple: theo thứ tự ngày, tra theo khóa, so tập mã và giữ một bộ giá trị. Cặp tọa độ được giải nén bằng `lat, lon = (10,106)`, khi đó lat=10, lon=106.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Chọn đúng bốn cấu trúc, mỗi loại0,375 điểm | 1,5 |
| Giải nén đúng cặp và ý nghĩa hai thành phần | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 1; chính K14; phụ K13. **Mức:** vận dụng. **Bẫy:** Dùng một cấu trúc cho mọi mục tiêu hoặc nhầm tập mã với dãy thời gian.

**Đọc lại:** G§1 bảng chọn cấu trúc; L4–11; T6,9,24; G§1; T25,27 (items/cặp).

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-039

Hiện in 30.0 do v chứa30,0,90,0; giá đã biết thực tế có trung bình 60.0. Trả None khi hỏng, rồi lọc `[x for x in v if x is not None]` sau khi chạy lại hàm đã sửa. Nếu không có giá, trả None/ghi chưa có trung bình thay vì chia rỗng hay báo0 như một giá thật.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| 30.0 và 60.0, giải thích hai số 0 giả làm tăng mẫu số | 0,75 |
| Sửa trả None, tính lại v và lọc bỏ None | 0,75 |
| Tập rỗng có quy ước rõ, không biến thiếu thành trung bình 0 | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 3; chính K34; phụ K35, K37. **Mức:** phân loại. **Bẫy:** Thay dữ liệu hỏng bằng 0 làm lệch thống kê và che thiếu dữ liệu.

**Đọc lại:** G§1,§3; L13–15; T13–16; G AI kiểm chứng; L13,21; T13,16; G§1 trung bình (giới hạn); L26 (quy ước cần nêu); T18 không rỗng (điều kiện).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-040

Code in 9 vì sắp/so chuỗi theo thứ tự từ điển, chưa so số. Sửa `gia = [float(r["gia"]) for r in rows if r["gia"] != ""]`, được max100.0; chuỗi "0" vẫn được giữ thành 0.0 hợp lệ. Trước max phải kiểm gia không rỗng; nếu rỗng, báo chưa có giá lớn nhất hoặc dùng quy ước None.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| In 9 do so chuỗi, không phải100 | 0,5 |
| Đổi float và bỏ chỉ ô trống, max100.0 | 0,75 |
| Giữ giá 0 theo đề và có bảo vệ tập rỗng trước max | 0,75 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 4; chính K39; phụ K40, K41. **Mức:** phân loại. **Bẫy:** CSV là chuỗi; lọc rỗng chưa đủ để tính/sắp theo giá trị số.

**Đọc lại:** G§4; L17–18; T9–11,30; L18; T11–16,29–30; L21–23; T11–15,21,30.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### Cập nhật bao phủ sau đợt 4

Lũy kế 40/60 câu: 28 TN, 12 TL.

| Nhóm | Đã có / kế hoạch |
|---|---:|
| 1 | 9 / 12 |
| 2 | 8 / 12 |
| 3 | 8 / 12 |
| 4 | 8 / 12 |
| 5 | 4 / 8 |
| 6 | 3 / 4 |

Mục đã có câu thực sự kiểm tra: K01, K02, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K51, K52, K53, K60, K61, K62, K63.
Mục chưa có câu: K03, K16, K17, K54, K55, K56, K57, K58, K59, K64.
Mục tiếp tục có nhánh/biến thể ở đợt sau: K01, K02, K04, K08, K13, K15, K21, K22, K23, K24, K29, K30, K31, K32, K33, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K48. Không dùng số mục đã chạm để suy mọi nhánh đã hoàn tất trước đợt cuối.

## Đợt 5 — Đáp án và hướng dẫn chấm

### B2-041 — B

Chỉ mục 0 lấy đầu dãy, -1 lấy cuối, -2 lấy phần tử liền trước cuối.

- **A sai:** Đếm chỉ mục âm như thể -1 đã bỏ qua phần tử cuối.
- **C sai:** Đếm phần tử đầu bằng chỉ mục 1 thay vì0.
- **D sai:** Đọc -2 thành phần tử thứ hai từ đầu, thay vì thứ hai từ cuối.

**Mục tiêu:** nhóm chính 1; chính K08. **Mức:** nền tảng. **Bẫy:** Chỉ mục đầu/cuối và âm phải theo vị trí Python thực tế.

**Đọc lại:** G§1; L6; T37 (chuỗi năm); kiến thức nền.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-042 — A

key=int so theo số nhưng trả các phần tử chuỗi gốc; sorted không key so từ điển.

- **B sai:** Tưởng hàm key còn thay phần tử kết quả thành int.
- **C sai:** Đảo sắp theo số và theo chuỗi.
- **D sai:** Tưởng sorted tự nhận biết chuỗi chứa số ngay cả khi không có key.

**Mục tiêu:** nhóm chính 2; chính K22; phụ K21. **Mức:** vận dụng. **Bẫy:** key chỉ dùng so sánh, không tự đổi kiểu phần tử trả về.

**Đọc lại:** G§4 CSV + §3 lambda; L18; T11,25 (áp dụng); G§3 lambda; T25,27.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-043 — D

replcae viết sai gây AttributeError ngay cả với "$10"; except Exception che lỗi. Bắt AttributeError có chủ đích cho None cũng không tự phát hiện lỗi gõ này: phải sửa tên và có ca đầu vào bình thường.

- **A sai:** Bắt hẹp hơn không sửa tên replcae và vẫn có thể che lỗi này.
- **B sai:** Hai ca đều kiểm đầu ra None, không kiểm chuyển thành công.
- **C sai:** Exception bắt cả AttributeError này, nên lỗi lập trình bị che.

**Mục tiêu:** nhóm chính 3; chính K33; phụ K35, K32. **Mức:** vận dụng. **Bẫy:** Qua vài ca lỗi không chứng minh đường chuyển thành công; catch rộng che bug.

**Đọc lại:** G§3 try/except, AI; L13,21; T12–13; G AI kiểm chứng; T13,16; G§3.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-044 — C

load nhận file có phương thức read; loads nhận văn bản JSON. dump là ghi đối tượng ra file.

- **A sai:** Đảo nguồn file với nguồn chuỗi.
- **B sai:** Dùng hàm ghi thay cho đọc, đồng thời thiếu đối số file đích của dump.
- **D sai:** Dùng dump để đọc chuỗi, không đúng vai trò API.

**Mục tiêu:** nhóm chính 4; chính K43. **Mức:** nền tảng. **Bẫy:** Tên gần nhau nhưng load/loads/dump nhận nguồn/đích khác nhau.

**Đọc lại:** G§4; L19; T33.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-045 — A

Sai giá 1,3,4; sai đêm3,4,6. Hợp có 4 phòng khác nhau, rows vẫn6 dòng vì chưa có lệnh xóa.

- **B sai:** Cộng hai số lỗi mà đếm trùng phòng 3,4.
- **C sai:** Tưởng tính/gắn cờ tự xóa4 dòng khỏi rows.
- **D sai:** Dùng giao (cùng sai cả hai) thay điều kiện sai ít nhất một.

**Mục tiêu:** nhóm chính 5; chính K54; phụ K55. **Mức:** vận dụng. **Bẫy:** QA OR cần hợp mã và không đếm trùng; gắn cờ khác xóa.

**Đọc lại:** G§2 lọc (áp dụng); L24–25; T31 (kiểm dữ liệu); T22.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-046 — D

chua chỉ gồm A, D; cả hai có ngày trống. B có 1 review nhưng thiếu ngày, nên phép kiểm một chiều không phát hiện được.

- **A sai:** Suy ngược từ kiểm số review 0 sang mọi dòng có ngày trống.
- **B sai:** all chỉ duyệt chua đã lọc, không tự quay lại toàn rows.
- **C sai:** Quy tắc đang so chuỗi bằng "0", không dùng truthiness để suy số review.

**Mục tiêu:** nhóm chính 5; chính K56; phụ K57. **Mức:** vận dụng. **Bẫy:** Kiểm đúng một tập con không chứng minh chiều ngược hoặc toàn bảng.

**Đọc lại:** T29–31; G AI kiểm chứng (ngữ cảnh); T30–31 (giới hạn assert).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-047

In `[-4,8] 2.0`; sửa thành `[x for x in nhiet if x is not None]` để giữ `[-4,0,8]`, trung bình 4/3°C. Dùng >0 sẽ bỏ cả nhiệt độ âm hợp lệ và 0, ngoài ra so None với0 gây TypeError nếu không bảo vệ trước.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Output đúng và nhận ra mất0 | 0,5 |
| Sửa chỉ bỏ None, đúng tập và trung bình 4/3 | 1 |
| Âm/0 hợp lệ, >0 không tương đương và cần bảo vệ None khi so số | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 1; chính K03; phụ K02, K04. **Mức:** vận dụng. **Bẫy:** Quy tắc khác None không tương đương truthy hoặc dương.

**Đọc lại:** G§1–2; L14–15,22–25; T15–16; L14–15; T5,15–16; G§1; L14; T5,15,19.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-048

```python
ids = [r["id"] for r in rows if r["gia"] is not None and r["gia"] >= 0]
bang = {r["id"]: r["gia"] for r in rows
        if r["gia"] is not None and r["gia"] >= 0}
```
Kết quả là `["P2","P4"]` và `{"P2":0,"P4":50}`; không đảo chiều ánh xạ và không loại0.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| List comprehension đúng tập và thứ tự P2, P4 | 0,75 |
| Dict comprehension đúng chiều và cùng tập bản ghi | 0,75 |
| Hai kết quả đúng, giữ 0/bỏ âm và None | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 2; chính K16; phụ K17, K15. **Mức:** vận dụng. **Bẫy:** Đúng cấu trúc comprehension nhưng sai tập lọc hoặc chiều id→giá.

**Đọc lại:** G§2; L6,22–23,25; T30; L10,22–23; T27; L8–10,22–23; T15,27.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-049

Dừng trong comprehension tạo pos vì gặp None>0, gây TypeError; map đã tạo đủ `[10.0,None,0.0,-5.0,None]`. Sửa `pos = [x for x in v if x is not None and x > 0]`, được `[10.0]`, trung bình 10.0. Dùng `tb = sum(pos)/len(pos) if pos else None`.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| TypeError trong lọc, không nhầm lỗi còn ở hàm chuyển/map | 0,75 |
| Điều kiện bảo vệ đúng thứ tự; pos và trung bình đúng | 0,75 |
| Tập rỗng trả None bằng điều kiện rõ | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 3; chính K29; phụ K36, K37. **Mức:** phân loại. **Bẫy:** Bắt lỗi chuyển kiểu chưa bảo vệ phép so sánh ở bước sau.

**Đọc lại:** G§3 hàm là giá trị; L13–14; T13–15; G§2–3; L22–25 (cần sửa truthiness); T15–16,27; G§1 trung bình (giới hạn); L26 (quy ước cần nêu); T18 không rỗng (điều kiện).

**Kiểm chứng:** đã chạy code gốc, xác nhận TypeError tại thao tác giải thích ở trên; đã chạy lời giải sửa và ca biên liên quan.

### B2-050

In True nhưng so_phong vẫn là chuỗi "4", nên chưa đạt yêu cầu. Trước dump thêm `obj["so_phong"] = int(obj["so_phong"])` rồi ghi/đọc lại. Kiểm `isinstance(doc["so_phong"],int)` và đối chiếu giá trị với số phòng nguồn đã đếm độc lập; equality chỉ chứng minh dữ liệu phù hợp này đã ghi-đọc khớp, không sửa kiểu hay kiểm nghiệp vụ giúp ta.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| True và vẫn là chuỗi, chỉ ra không đạt quy định | 0,75 |
| Chuyển int trước ghi rồi đọc lại | 0,5 |
| Kiểm kiểu và đối chiếu số đếm nguồn, nêu giới hạn equality | 0,75 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 4; chính K44; phụ K45, K46. **Mức:** phân loại. **Bẫy:** Đọc lại bằng nhau chưa chứng minh báo cáo đúng kiểu hoặc đúng số liệu.

**Đọc lại:** G§4; L19; T33.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### Cập nhật bao phủ sau đợt 5

Lũy kế 50/60 câu: 34 TN, 16 TL.

| Nhóm | Đã có / kế hoạch |
|---|---:|
| 1 | 11 / 12 |
| 2 | 10 / 12 |
| 3 | 10 / 12 |
| 4 | 10 / 12 |
| 5 | 6 / 8 |
| 6 | 3 / 4 |

Mục đã có câu thực sự kiểm tra: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K51, K52, K53, K54, K55, K56, K57, K60, K61, K62, K63.
Mục chưa có câu: K58, K59, K64.
Mục tiếp tục có nhánh/biến thể ở đợt sau: K01, K04, K13, K21, K23, K24, K30, K31, K32, K35, K38, K39, K40, K41, K42, K48. Không dùng số mục đã chạm để suy mọi nhánh đã hoàn tất trước đợt cuối.

## Đợt 6 — Đáp án và hướng dẫn chấm

### B2-051 — D

float chuyển chuỗi thập phân thành số thực 3.5; int không nhận trực tiếp chuỗi dạng này.

- **A sai:** int của chuỗi "3.5" phát sinh ValueError, không tự cắt phần thập phân.
- **B sai:** Vẫn là chuỗi, không trở thành số thực để cộng số.
- **C sai:** Chuỗi không rỗng cho True, không phải số đo3.5.

**Mục tiêu:** nhóm chính 1; chính K01. **Mức:** nền tảng. **Bẫy:** Phân biệt chuyển thành số, giữ chuỗi và chỉ kiểm truthiness.

**Đọc lại:** G§1,§3; L2,13,21; T11–13.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-052 — D

Sắp cặp mặc định xét khóa chuỗi A, B,…; key lấy giá trị và reverse=True chọn9,5.

- **A sai:** Tưởng sorted(items) mặc định dùng số kiện tăng dần.
- **B sai:** Bỏ qua reverse=True ở cách sắp theo số.
- **C sai:** Đảo cách sắp theo mã và theo số.

**Mục tiêu:** nhóm chính 2; chính K24; phụ K21. **Mức:** vận dụng. **Bẫy:** items là cặp; khóa dict khác khóa sắp xếp key.

**Đọc lại:** G§2 dict,§3 lambda; L10; T24–27; G§3 lambda; T25,27.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-053 — B

int("3.0") gây ValueError, còn "-2" và "0" đổi được. Chưa có điều kiện loại không dương.

- **A sai:** Tưởng int tự chuyển chuỗi thập phân qua float rồi cắt phần lẻ.
- **C sai:** Tự thêm quy tắc dương vào một hàm chỉ chuyển kiểu.
- **D sai:** Vừa tự chuyển chuỗi "3.0", vừa tự loại0 và âm.

**Mục tiêu:** nhóm chính 3; chính K32; phụ K31, K35. **Mức:** vận dụng. **Bẫy:** Ca chuyển kiểu được/chưa được khác ca đạt quy tắc số đêm.

**Đọc lại:** G§3; L13,21; T12–13; G§2–3; L13–15,22–25; T13,15–16; G AI kiểm chứng; T13,16.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-054 — C

Chỉ bỏ chuỗi rỗng; "0" được đổi thành 0.0 và giữ trong 3 giá. Tổng 45 chia 3.

- **A sai:** Loại nhầm giá 0 hợp lệ bằng truthiness sau chuyển kiểu.
- **B sai:** Đếm 3 giá nhưng chia tổng cho 4 dòng nguồn.
- **D sai:** Bỏ qua điều kiện đã loại chuỗi rỗng trước float.

**Mục tiêu:** nhóm chính 4; chính K40; phụ K41, K04. **Mức:** vận dụng. **Bẫy:** Ô trống khác giá 0; dùng đúng mẫu số của tập giá đã biết.

**Đọc lại:** G§4; L18; T11–16,29–30; L21–23; T11–15,21,30; G§1; L14; T5,15,19.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-055 — D

Lát cắt[: 4] lấy năm và dict cộng dồn số review. Năm 2026 mới nửa năm, khác cửa sổ quan sát của2025; số đếm không tự chỉ ra nguyên nhân.

- **A sai:** So năm chưa trọn với năm trọn như cùng thời lượng.
- **B sai:** Số đếm không cung cấp bằng chứng nguyên nhân giá tăng.
- **C sai:** Nhầm khử trùng khóa với cộng dồn giá trị bằng get(nam, 0)+1.

**Mục tiêu:** nhóm chính 5; chính K58; phụ K59. **Mức:** vận dụng. **Bẫy:** Code đếm đúng chưa đủ để suy xu hướng cả năm hoặc nguyên nhân.

**Đọc lại:** G§1 slicing (cơ chế); T37–38; T37 snapshot 29/06/2026.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-056 — A

Đọc dữ liệu trước, dùng list rows để tổng hợp, rồi dùng dict báo cáo để ghi. Các hàm nhỏ ghép theo giao ước thay vì truyền đường dẫn vào hàm cần rows.

- **B sai:** Ghi list thay vì dict báo cáo và đưa kết quả hàm ghi vào summarize.
- **C sai:** Truyền chuỗi đường dẫn vào summarize rồi dùng báo cáo làm đường dẫn load.
- **D sai:** Bỏ bước load; summarize cần list dict chứ không phải tên file.

**Mục tiêu:** nhóm chính 6; chính K64. **Mức:** nền tảng. **Bẫy:** Đúng tên hàm nhưng sai trình tự hoặc kiểu dữ liệu giữa các bước.

**Đọc lại:** G§3 hàm; L26–27; T33.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-057

Output là `('P3',90)`, một tuple của bản ghi gốc, không chỉ là số 90. Hai mã rẻ nhất lấy bằng `[m for m,g in sorted(phong,key=lambda p:p[1])[:2]]`, cho `["P2","P4"]`. sorted tạo list kết quả nên phong[0] vẫn là ("P1", 40).

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Tuple P3,90 và giải thích max trả bản ghi | 0,75 |
| Biểu thức đúng sắp giá rồi lấy hai mã P2, P4 | 0,75 |
| Giải nén m, g đúng; đầu vào không đổi bởi sorted | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 2; chính K23; phụ K21, K13. **Mức:** vận dụng. **Bẫy:** Nhầm max trả số; nhầm sorted sửa list gốc hoặc lấy top-k theo mã.

**Đọc lại:** G§3 lambda (ngữ cảnh); T20–22; G§3 lambda; T25,27; G§1; T25,27 (items/cặp).

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### B2-058

None không có replace nên phát sinh AttributeError trước float; TypeError đang bắt không xử lý lỗi đó. Sửa `except (ValueError,AttributeError):`, v thành `[10.0,None,0.0,-2.0]`, lọc `[x for x in v if x is not None and x > 0]` được `[10.0]`. Vẫn cần ca 0/âm vì chuyển được sang số chưa đồng nghĩa hợp lệ, còn bộ thử cũ cũng thiếu None.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| AttributeError tại replace trên None, phân biệt với float(None) | 0,75 |
| Except đúng, v và lọc >0 có bảo vệ None | 0,75 |
| Ca 0/âm để kiểm nghiệp vụ, ca None kiểm đường lỗi thực tế | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 3; chính K30; phụ K32, K35. **Mức:** phân loại. **Bẫy:** Tên hàm giống nhau nhưng lỗi phụ thuộc thao tác chạy trước; test chưa đủ ca biên.

**Đọc lại:** G§3 clean_price; L13; T12–13 (float không dấu tiền); G§3; L13,21; T12–13; G AI kiểm chứng; T13,16.

**Kiểm chứng:** đã chạy code gốc, xác nhận AttributeError tại thao tác giải thích ở trên; đã chạy lời giải sửa và ca biên liên quan.

### B2-059

```python
import csv
with open("phong.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["ma","nhan","gia"])
    w.writeheader()
    w.writerow(row)
```
DictReader đọc nhan là chuỗi "Nam, Bắc", gia là chuỗi "0"; writer tự trích dẫn trường chứa dấu phẩy. newline="" để thư viện csv quản lý ký tự kết thúc dòng, tránh chuyển đổi xuống dòng thêm của lớp text; w ghi đè nội dung cũ.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| with open w, UTF8 và newline="" | 0,5 |
| DictWriter đúng fieldnames, writeheader và writerow | 0,75 |
| Giữ nguyên một trường nhan và gia là chuỗi "0" | 0,5 |
| Giải thích newline quản lý xuống dòng, không đổi kiểu dữ liệu | 0,25 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 4; chính K42; phụ K38, K39. **Mức:** vận dụng. **Bẫy:** Ghép CSV thủ công làm vỡ trường có dấu phẩy; đọc lại vẫn là chuỗi.

**Đọc lại:** G§4 (CSV ngữ cảnh); L17; G§4; L17–19; T9,33; L17–18; T9–11,30.

**Kiểm chứng:** đã chạy biểu thức/lời giải tương ứng trong dữ kiện đề và các kiểm tra bổ sung; câu không nhất thiết có lệnh print sẵn.

### B2-060

Hiện in `[('2025',1),('2026',2)]`, đếm phòng theo năm của review gần nhất, không phải mọi review. Đếm đúng:
```python
dem = {}
for r in reviews:
    nam = r["date"][:4]
    dem[nam] = dem.get(nam, 0) + 1
```
Kết quả2025: 4,2026: 2; 2026 mới nửa năm nên chưa so trực tiếp để suy cả năm, và số đếm riêng cũng chưa chứng minh nguyên nhân biến động.

**Hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Output1/2 và đúng đơn vị phòng theo review gần nhất | 0,75 |
| Đổi sang reviews, date[: 4], cộng dồn và kết quả4/2 | 0,75 |
| Giới hạn năm chưa trọn và không suy nguyên nhân từ số đếm | 0,5 |

Chấp nhận cách đúng tương đương; xem quy ước chấm ở đầu tệp.

**Mục tiêu:** nhóm chính 5; chính K58; phụ K59, K48. **Mức:** phân loại. **Bẫy:** Thao tác đếm/năm đúng nhưng dùng sai bảng và sai đơn vị quan sát.

**Đọc lại:** G§1 slicing (cơ chế); T37–38; T37 snapshot 29/06/2026; G§1,§3; L14,26; T15,33,35,37.

**Kiểm chứng:** đã chạy code gốc, đối chiếu output; lời giải sửa/ca biên nếu có được kiểm riêng.

### Cập nhật bao phủ sau đợt 6

Lũy kế 60/60 câu: 40 TN, 20 TL.

| Nhóm | Đã có / kế hoạch |
|---|---:|
| 1 | 12 / 12 |
| 2 | 12 / 12 |
| 3 | 12 / 12 |
| 4 | 12 / 12 |
| 5 | 8 / 8 |
| 6 | 4 / 4 |

Mục đã có câu thực sự kiểm tra: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64.
Mục chưa có câu: không còn.
Mục tiếp tục có nhánh/biến thể ở đợt sau: không còn. Không dùng số mục đã chạm để suy mọi nhánh đã hoàn tất trước đợt cuối.

## Đối chiếu cuối cùng

Đủ 60 mã liên tục B2-001–B2-060,40 TN và 20 TL, đúng phân bổ nhóm12/12/12/12/8/4, mức 15/33/12. Mỗi câu chỉ tính một nhóm chính, tối đa hai mục tiêu phụ. A/B/C/D mỗi chữ đúng10 lần; thứ tự được xáo, không theo chu kỳ cố định.64 mục có câu kiểm tra thực sự.

Các câu tích hợp có hành vi hiện tại, bước sửa và ca biên/hệ quả gồm 009,010,019,020,029,039,040,049,050,058,060; nhiều hơn yêu cầu tối thiểu4. Câu 028 còn yêu cầu dự đoán, sửa chiều trừ và giải thích tổ hợp set.

| Bẫy trọng tâm | Câu và biến thể kiểm tra |
|---|---|
| if x làm mất0 hợp lệ | 002 cơ chế; 029 sửa giá; 047 nhiệt độ; 054 CSV→giá |
| if x giữ âm, không thay >0 | 002; 005 chuyển giá; 029 sửa lọc; 049/058 bảo vệ None |
| Chuyển được số chưa đạt nghiệp vụ | 005 giá; 014/053 số đêm; 029/058 sửa theo quy tắc |
| Mẫu số toàn bảng sau lọc | 010 sửa trung bình; 020 ngưỡng khu; 039 số 0 giả; 054 output |
| Dữ liệu hỏng đổi0 | 029 phân biệt0 thật; 039 dự đoán/sửa/quy ước rỗng |
| CSV chuỗi so số | 007 dự đoán hai phép đếm; 040 sửa chuyển kiểu; 054 giữ 0 |
| Sắp số dưới dạng chuỗi | 015 chọn lượt thuê; 040 max; 042 key=int vẫn trả chuỗi |
| Chiều trừ set | 028 dự đoán mã mới, sửa mã mất, giải thích hợp-trừ-giao |
| Stop slicing | 011 khoảng ngày; 055/060 date[: 4] lấy năm |
| Gán list tưởng copy | 033 alias và copy; 019 phân biệt ngoài/trong, sửa cách tạo dữ liệu thử |
| zip theo vị trí | 004 output sai cặp; 032 chọn cách ghép/sắp đúng |
| get mặc định không thay None/0 | 008 output và KeyError; 020 get cộng dồn khi thiếu khu |
| Bắt sai lỗi/quá rộng | 009 float(None); 013 hai thao tác; 043 che typo; 058 None.replace |
| Hàm vào map khác gọi hàm | 024 chọn biểu thức; 049/058 theo dõi map rồi lọc/ngoại lệ |
| Phần trăm/nhân 100 hai lần | 031 phân biệt hai output và nhiễu nhân thêm 100 |
| JSON null/true khác chuỗi | 016 list/bool/null; 035/050 JSON không sửa kiểu giúp; 059 CSV khác JSON |
| mkdir không xóa/dựng lại | 017 chạy hai lần giữ file; 037 phân biệt parent/glob trên cây có sẵn |
| Đúng thao tác sai tập | 020 ngưỡng giá hợp lệ; 036 top đông rồi so giá; 046 kiểm một chiều; 060 đếm sai bảng |

### Rà nhánh dễ bỏ sót

Cả trung vị lẻ/chẵn và sorted không sửa đầu vào đều được hỏi ở027, bổ sung057 về sorted. Căn cột/độ rộng và giải nén tuple có 018/038. DictWriter, header, fieldnames, trích dẫn dấu phẩy và newline có 026/059. JSON có dump/load/loads, list/bool/None và round-trip đúng phạm vi ở016/035/044/050. Các đếm nhóm dùng get, gom list giá, ngưỡng số giá và QA hợp mã có 020/045. Kiểm chéo một chiều và năm chưa trọn có 046/055/060. Module và dấu chấm có 030, giao ước pipeline có 056.

Các câu gần chủ đề được phân biệt bằng thao tác cần làm: lọc khác None ở nhiệt độ không dùng chung quy tắc dương của giá; max trả bản ghi khác max chuỗi CSV; file CSV trích dẫn không đồng nghĩa JSON; equality đọc lại không phải QA nghiệp vụ. Không chỉ thay tên và số từ đề gốc. Tỷ trọng và các bẫy trong ngân hàng là lựa chọn thiết kế theo phạm vi, không phải khẳng định tần suất hay dự báo chắc chắn đề thi thật.
