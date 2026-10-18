# Bài 1 — Đáp án chi tiết và hướng dẫn chấm tự luận

## Nguồn đã đọc, giới hạn và các khác biệt

Đã đọc đầy đủ ba nguồn bắt buộc:

- **G**: [bai-01-tong-quan-va-chinh-sach-ai.md](<D:/LTXLDL_GK/Bài 1/bai-01-tong-quan-va-chinh-sach-ai.md>) — các mục 1–4.
- **L**: [lecture_01.ipynb](<D:/LTXLDL_GK/Bài 1/lecture_01.ipynb>) — cả code, hướng dẫn, bài tập, tự học và câu hỏi kiểm tra môi trường.
- **T**: [lab_01.ipynb](<D:/LTXLDL_GK/Bài 1/lab_01.ipynb>) — cả khởi động, ba thí nghiệm trạng thái, phân tích demo, assert, khai báo và bài tự làm.
- **P**: [Chính sách AI chi tiết](https://courses.iaidev.com/programming-for-data-processing/2627-1/ai-policy.html), phiên bản 07/2026, truy cập 17/10/2026. Đã truy cập được đầy đủ; không thiếu trang này. Các quy tắc cốt lõi có trong G được đối chiếu thêm với P; không đưa vào câu hỏi các mức kỷ luật ngoài phạm vi được hỏi.

Đề phong cách đã đọc toàn bộ: `2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf` (ưu tiên câu 1–2); `LTXLDL_AI_5.pdf`, `LTXLDL_DS_1.pdf`, `LTXLDL_DS_2.pdf` dùng tham khảo chính; `LTXLDL_AI_1.pdf`, `LTXLDL_AI_2.pdf` chỉ bổ trợ. Không lấy mức khó NumPy trong các đề làm mức khó Bài 1.

**Khác biệt cần giữ nguyên:** G§4 và P§2 nêu hai bài giấy 15 phút, còn tiêu đề các đề tuần 3 mẫu ghi 20 phút. Đề giữa kỳ luyện tập ghi 60 phút, không tự xác nhận thời lượng thi thật. G xếp việc cài local trong danh sách trước Bài 2, L§5 nói nên làm trước Bài 3; cả hai đều mô tả cài local là không bắt buộc hoàn thành ngay. Lộ trình là 15 bài, không tự suy thành 15 tuần; có thể xem [trang môn học](https://courses.iaidev.com/programming-for-data-processing/2627-1/) để phân biệt lịch theo tuần.

Đối chiếu kỹ thuật bổ trợ: [venv — tài liệu Python 3.12](https://docs.python.org/3.12/library/venv.html). Dùng để kiểm cơ chế kỹ thuật đã có trong phạm vi yêu cầu, không bổ sung tính năng để nâng khó. Không có tệp nguồn bắt buộc nào bị thiếu.

## Cách dùng hướng dẫn chấm

Mức độ là nhãn thiết kế, chưa đo thực nghiệm. Mỗi tự luận dùng thang 2 điểm/câu để chia điểm luyện tập; đây không phải cơ cấu điểm chính thức của học phần. Chấm từng ý đúng, chấp nhận lời văn/lệnh đúng tương đương, không đòi giống mẫu. Không loại cách đúng vì cách khác được khuyến nghị. Nếu đề thiếu điều kiện cho phép dùng AI, câu trả lời phải giữ sự thiếu điều kiện và hỏi giảng viên; không tự đoán thay. Với chính sách, chấm theo quy tắc và tình huống, không chấm theo phán xét đạo đức chung.

Đoạn Python và lịch trạng thái được thực thi bằng Python 3.12.14 với không gian tên riêng cho từng câu. Cơ chế biểu thức cuối cell được mô phỏng từ mã Python; không tuyên bố đã điều khiển giao diện Colab. Lệnh Bash/Command Prompt và các tình huống Python giả định 3.11.9/3.12.3 được đối chiếu nguồn/suy luận theo giả định, chưa chạy đúng các shell và phiên bản đó. Các câu không có code được đối chiếu trực tiếp nguồn.

## Ma trận đủ 60 câu

| Nhóm chính | Nền tảng | Vận dụng | Phân loại | TN | TL | Tổng |
|---|---:|---:|---:|---:|---:|---:|
| 1. Mục tiêu môn học và quá trình xử lý dữ liệu | 5 | 3 | 0 | 6 | 2 | 8 |
| 2. Colab, notebook và trạng thái thực thi | 3 | 4 | 3 | 6 | 4 | 10 |
| 3. Môi trường Python và khả năng chạy lại dự án | 4 | 7 | 3 | 11 | 3 | 14 |
| 4. Chính sách AI và trách nhiệm cá nhân | 2 | 8 | 4 | 9 | 5 | 14 |
| 5. Quy trình làm việc với AI và kiểm chứng | 0 | 6 | 2 | 4 | 4 | 8 |
| 6. Vận hành môn học, Git và bài tập lớn | 1 | 5 | 0 | 4 | 2 | 6 |
| **Tổng** | **15** | **33** | **12** | **40** | **20** | **60** |

## Danh mục mục tiêu nhỏ và đối chiếu nguồn

Danh mục và kế hoạch được lập trước khi viết câu. Dấu — nghĩa là không có đoạn trực tiếp tương ứng trong nguồn đó; “ngữ cảnh/áp dụng” không được trình bày như lời quy định nguyên văn. Mỗi mục dưới đây có câu yêu cầu dùng kiến thức, không chỉ được nhắc trong lời giải. K61 là mục xem trước về Secrets tìm thấy khi đọc đầy đủ notebook, chỉ hỏi mức ý nghĩa.

| Mã | Mục tiêu | G | L | T / đối chiếu bổ sung | Câu dự kiến và thực tế kiểm tra |
|---|---|---|---|---|---|
| K01 | Dữ liệu thô → sạch → thông tin → quyết định | G1 | L§2 | T§2 | B1-001, B1-021 |
| K02 | Thu thập/làm sạch/biến đổi/trực quan/kể chuyện; phân loại công việc | G1 | L§2 | T§2 | B1-001, B1-021, B1-030 |
| K03 | Dữ liệu thật: giá chuỗi, thiếu, bất thường; chưa tự kết luận sai | G1 | L§2 nhìn dữ liệu | T§2 | B1-011, B1-041 |
| K04 | Chất lượng đầu vào, chuẩn bị và kiểm tra chi phối kết luận | G1 | L§4 bài 1 | T§3 | B1-011, B1-041 |
| K05 | Python và hệ sinh thái; từ thử nghiệm đến pipeline | G1–2 | L§2,§5 | T§2 | B1-031, B1-051 |
| K06 | Chỉ đạo công cụ, hiểu từng dòng, kiểm chứng; không chỉ tự gõ | G3 mục tiêu2026 | L§3–4 | T§3 | B1-031 |
| K07 | Vị trí môn: sau Tư duy tính toán, trước các ứng dụng ML/KHDL | G1 môn này đứng ở đâu | — | — | B1-051 |
| K08 | Markdown/code; Shift+Enter chạy cell code | G2 notebook (ngữ cảnh) | L§1 | T§0 W1 | B1-002, B1-022 |
| K09 | print và giá trị biểu thức cuối cell | G2 notebook | L§1 cell2–4 | T§2 hiển thị output | B1-002 |
| K10 | Biến xuyên cell; lịch chạy thực tế quyết định trạng thái | — | L§1 state | T§1 bước1–2 | B1-012, B1-032, B1-052 |
| K11 | Có cell định nghĩa chưa nghĩa đã chạy; NameError ở phiên hiện tại | — | L§1 state | T§1 bước1 | B1-008, B1-012, B1-047 |
| K12 | Sửa/xóa cell không tự hoàn tác lần chạy trước | — | L§1 state | T§1 mở đầu | B1-028, B1-052 |
| K13 | Chạy lại cộng dồn; khác chạy lại khởi tạo | — | L§1 state | T§1 bước2 | B1-032, B1-057 |
| K14 | Restart xóa trạng thái, không xóa mã/tệp đã lưu chỉ vì restart | — | L§1 state | T§0 W2,§1 | B1-028, B1-047 |
| K15 | Run all trên phiên cũ khác Restart & Run all | — | L§1 state | T§1 bước3 | B1-008, B1-028, B1-057 |
| K16 | Chạy hết từ phiên sạch phát hiện phụ thuộc; chưa chứng minh đúng ý nghĩa | G3 kiểm chứng | L§1,§4 bài 1 | T§1,§3 | B1-008 |
| K17 | Save a copy in Drive trước khi làm | — | Lcell0 | Tcell0,§0 W2 | B1-002, B1-047 |
| K18 | Đọc shape hàng/cột và bảng đếm nhóm nhiều nhất | G2 notebook | L§2 | T§2 kiểm tra | B1-042 |
| K19 | Dấu ! chạy lệnh hệ điều hành trong Colab | — | L§3 | T§4 tự làm1 | B1-022 |
| K20 | Xem trước biểu đồ: điểm/màu; groupby ở mức gộp theo nhóm, không kỹ thuật | — | L§2 đồ thị,§4 bài 2 | T§2 biểu đồ | B1-050 |
| K21 | Colab có sẵn để học; VS Code+venv để kiểm soát dự án cá nhân | G2 hai môi trường | L§5 | T§4 tự làm1 | B1-005, B1-033 |
| K22 | venv tách thư viện giữa dự án | G2 venv | L§5 | T§4 tự làm1 | B1-005 |
| K23 | Trình thông dịch được gọi khi tạo venv quyết định Python nền | G2 venv,.python-version | L§5 | T§4 tự làm1 | B1-003, B1-053 |
| K24 | Kích hoạt khác chuyển thư mục; cwd không tự đổi môi trường | G2 venv | L§5 (lệnh tạo/kích hoạt) | T§4 tự làm1 | B1-013, B1-019, B1-025, B1-043 |
| K25 | pip/python cài vào môi trường đang được gọi, theo giả định rõ | G2 venv | L§5 | T§4 tự làm1 | B1-013, B1-019, B1-043 |
| K26 | pip install, pip freeze, pip install -r có vai trò khác nhau | G2 requirements | L§5 | T§4 tự làm1 | B1-015, B1-035 |
| K27 | freeze chụp phiên bản gói hiện tại, gồm phụ thuộc; venv không kế thừa hệ thống | G2 requirements | L§5 câu tự kiểm | — | B1-015, B1-019 |
| K28 | requirements ghi thư viện, không thay phiên bản Python | G2 requirements | L§5 | T§4 tự làm1 | B1-003, B1-023, B1-058 |
| K29 | .python-version ghi bản kiểm thử; không tự tải/cài/đổi khi không có trình quản lý | G2 .python-version | L§5 tạo venv (ngữ cảnh) | — | B1-003, B1-023, B1-053, B1-058 |
| K30 | Sao chép .venv không là cách dựng lại đáng tin trên máy khác | G2 chạy lại máy khác | L§5 tự dựng venv | — | B1-038 |
| K31 | Dựng lại: chọn đúng Python → venv → thư viện → chạy theo README | G2 .python-version | L§5 | T§4 tự làm1 | B1-038, B1-058 |
| K32 | README ghi OS và lệnh dựng/chạy dự án | G2 chạy lại máy khác | L§5 (ngữ cảnh) | — | B1-038 |
| K33 | Đúng môi trường hỗ trợ chạy lại, chưa bảo đảm code đúng hay đầu vào không đổi | G2–3 | L§4 kiểm chứng | T§3 kiểm chứng | B1-045 |
| K34 | .ipynb chứa mã/output lưu, không đóng gói thư viện hay trạng thái phiên sống | G2 notebook,venv | L§1,§5 tải/chạy local | T§1 state | B1-033, B1-037 |
| K35 | Đóng: quiz, giữa kỳ, vấn đáp; ít trợ giúp hoặc đã khai báo không đổi chế độ | G3 hai chế độ | L§3 khai báo (ngữ cảnh) | T§1 cách làm việc | B1-006, B1-014, B1-039, B1-048, B1-054 |
| K36 | Mở theo nhãn; thiếu nhãn hỏi GV, không suy từ tại nhà/ít điểm/viết nháp | G3 hai chế độ | L§5 nhãn mở | T§4 nhãn mở | B1-016, B1-048, B1-056 |
| K37 | Ba trách nhiệm khai báo–hiểu–kiểm chứng đều cần | G3 ba trách nhiệm | L§3–4 | T§3 | B1-009, B1-034 |
| K38 | Sửa nhiều code AI vẫn phải khai báo phần đã dùng | G3 khai báo | L§4 khai báo | T§3 bước5 | B1-004, B1-009 |
| K39 | Khai báo không miễn hiểu; phần không giải thích được nhận 0 điểm cá nhân | G3 ranh giới gian lận | L§3 đọc hiểu | T§3 bước2–3 | B1-006, B1-020 |
| K40 | Khai báo không miễn đúng/sai; người nộp chịu trách nhiệm, không đổ cho AI | G3 kiểm chứng | L§4 bài 1–2 | T§3 bước4 | B1-009, B1-024, B1-039 |
| K41 | AI ở chế độ mở, hiểu, kiểm chứng, khai báo: có thể được chấp nhận | G3 ranh giới gian lận | L§4 bài 2–3 | T§3–4 | B1-034 |
| K42 | Giấu/khai man hoặc AI viết lại bài nhóm khác vẫn vi phạm | G3 ranh giới gian lận | — | T§3 khai báo (ngữ cảnh) | B1-029 |
| K43 | AI dịch/sửa nội dung cũng phải xét chế độ và khai báo | G3 khai báo dùng gì/việc gì | — | T§3 mẫu khai báo (ngữ cảnh);P§1,§3 | B1-029, B1-056 |
| K44 | Phân biệt vi phạm chế độ, thiếu minh bạch và bài làm sai | G3 ranh giới gian lận | L§4 kiểm chứng | T§3 | B1-020, B1-024, B1-039 |
| K45 | Khuyến nghị tự gõ khác quy định cấm AI ở hình thức đánh giá đóng | G3 nhãn chế độ | L§4 khuyến khích dùng AI | Tcell1 và§4 | B1-048 |
| K46 | Khai báo công cụ/công việc/prompt/sai lệch/kiểm chứng; không dùng cũng ghi rõ | G3 khai báo | Lcell21 | T§3 bước5;P§4 | B1-004, B1-040, B1-044 |
| K47 | Quy trình phác → hỏi → đọc hiểu → kiểm chứng → khai báo | G3 quy trình | L§4 bài 2–3 | T§3 | B1-007, B1-040 |
| K48 | Tự xác định câu hỏi/dự đoán; prompt có ngữ cảnh/tên dữ liệu/yêu cầu | G3 tự phác/hỏi | L§4 bài 2 | T§3 bước1–3 | B1-007, B1-055 |
| K49 | Đọc từng dòng; hàm lạ đối chiếu tài liệu chính thức đúng phiên bản | G mục AI hay sai/kiểm chứng | L§4 đọc hiểu | T§3 bước2–3 | B1-007, B1-036, B1-055 |
| K50 | Mẫu nhỏ tính tay/cách độc lập; hai đáp án AI giống nhau chưa độc lập | G kiểm chứng | L§4 bài 2 | T§3 bước4 | B1-018, B1-026, B1-036, B1-059 |
| K51 | Tỷ lệ 0–1 khác %0–100; tổng gần 100 cần nhưng chưa đủ đúng từng nhóm | G3 kiểm chứng | L§4 kiểm chứng (ngữ cảnh) | T§3 bước1,4 | B1-026, B1-049 |
| K52 | mean bỏ thiếu đổi tập giá biết; không tự coi chưa biết là 0 | G3 quy ước mean | L§4 kiểm chứng (ngữ cảnh) | T§3 kiểm chứng (áp dụng) | B1-018, B1-059 |
| K53 | Vài assert/ca thử chỉ chứng minh điều được kiểm, không tất cả nguồn/trường hợp | G3 kiểm chứng | L§4 bài 1–2 | T§3 bước4 (giới hạn kiểm) | B1-049, B1-059 |
| K54 | Git ghi lịch sử; GitHub repo private, cộng tác và lịch sử commit nhóm | G2 Git/GitHub | — | — | B1-010 |
| K55 | Mỗi nhóm một thành phố; một lệnh → QA → KPI → biểu đồ → báo cáo + LLM review | G4 BTL | — | T§2 Airbnb (ngữ cảnh) | B1-027 |
| K56 | Test chung trên repo, vấn đáp từng người; output notebook không thay sản phẩm chạy lại | G4 BTL | L§5 chạy local | — | B1-037 |
| K57 | Trọng số 10/10/20/60; nguồn môn15 phút khác đề tuần 3 mẫu 20 phút | G4 cơ cấu điểm/kế hoạch | — | P§2 và tiêu đề PDF mẫu | B1-017, B1-046 |
| K58 | Lộ trình theo bài:1–5;6–8,10;11–14;9 giữa kỳ,15 vấn đáp; không suy thành tuần | G1 lộ trình | — | — | B1-046 |
| K59 | 3 tiết LT +3 tiết lab; Classroom nộp lab, Canvas thông báo/phân công | G4 mỗi tuần/BTL | L§4 thực hành lớp | T§1 cách làm việc | B1-060 |
| K60 | Trước bài 2: notebook, đọc policy, nhóm 4–5; cài local khuyến nghị, mốc trước 2/trước 3 | G4 việc trước bài 2 | L§5 và cuối notebook | T§4 và cuối notebook | B1-060 |
| K61 | Secrets/API key chỉ mức giới thiệu: không dán khóa thật vào mã/commit | — | Lcell16 | P§3 công cụ/dữ liệu | B1-050 |

## Kế hoạch từng câu

| Mã | Đợt | Nhóm chính | Dạng | Mức | Chính; phụ |
|---|---:|---:|---|---|---|
| B1-001 | 1 | 1 | TN | nền tảng | K02; K01 |
| B1-002 | 1 | 2 | TN | nền tảng | K08; K09; K17 |
| B1-003 | 1 | 3 | TN | vận dụng | K29; K23; K28 |
| B1-004 | 1 | 4 | TN | vận dụng | K38; K46 |
| B1-005 | 1 | 3 | TN | nền tảng | K22; K21 |
| B1-006 | 1 | 4 | TN | vận dụng | K35; K39 |
| B1-007 | 1 | 5 | TN | vận dụng | K47; K48; K49 |
| B1-008 | 1 | 2 | TL | phân loại | K15; K11; K16 |
| B1-009 | 1 | 4 | TL | phân loại | K37; K40; K38 |
| B1-010 | 1 | 6 | TL | vận dụng | K54 |
| B1-011 | 2 | 1 | TN | nền tảng | K03; K04 |
| B1-012 | 2 | 2 | TN | vận dụng | K10; K11 |
| B1-013 | 2 | 3 | TN | vận dụng | K24; K25 |
| B1-014 | 2 | 4 | TN | nền tảng | K35 |
| B1-015 | 2 | 3 | TN | vận dụng | K27; K26 |
| B1-016 | 2 | 4 | TN | vận dụng | K36 |
| B1-017 | 2 | 6 | TN | nền tảng | K57 |
| B1-018 | 2 | 5 | TL | phân loại | K52; K50 |
| B1-019 | 2 | 3 | TL | phân loại | K25; K24; K27 |
| B1-020 | 2 | 4 | TL | vận dụng | K39; K44 |
| B1-021 | 3 | 1 | TN | nền tảng | K01; K02 |
| B1-022 | 3 | 2 | TN | nền tảng | K19; K08 |
| B1-023 | 3 | 3 | TN | vận dụng | K28; K29 |
| B1-024 | 3 | 4 | TN | vận dụng | K40; K44 |
| B1-025 | 3 | 3 | TN | nền tảng | K24 |
| B1-026 | 3 | 5 | TN | vận dụng | K51; K50 |
| B1-027 | 3 | 6 | TN | vận dụng | K55 |
| B1-028 | 3 | 2 | TL | phân loại | K12; K14; K15 |
| B1-029 | 3 | 4 | TL | phân loại | K43; K42 |
| B1-030 | 3 | 1 | TL | vận dụng | K02 |
| B1-031 | 4 | 1 | TN | nền tảng | K05; K06 |
| B1-032 | 4 | 2 | TN | vận dụng | K13; K10 |
| B1-033 | 4 | 3 | TN | vận dụng | K34; K21 |
| B1-034 | 4 | 4 | TN | vận dụng | K41; K37 |
| B1-035 | 4 | 3 | TN | nền tảng | K26 |
| B1-036 | 4 | 5 | TN | vận dụng | K50; K49 |
| B1-037 | 4 | 6 | TN | vận dụng | K56; K34 |
| B1-038 | 4 | 3 | TL | phân loại | K30; K31; K32 |
| B1-039 | 4 | 4 | TL | phân loại | K44; K35; K40 |
| B1-040 | 4 | 5 | TL | vận dụng | K46; K47 |
| B1-041 | 5 | 1 | TN | vận dụng | K04; K03 |
| B1-042 | 5 | 2 | TN | nền tảng | K18 |
| B1-043 | 5 | 3 | TN | vận dụng | K25; K24 |
| B1-044 | 5 | 4 | TN | nền tảng | K46 |
| B1-045 | 5 | 3 | TN | vận dụng | K33 |
| B1-046 | 5 | 6 | TN | vận dụng | K58; K57 |
| B1-047 | 5 | 2 | TL | phân loại | K14; K11; K17 |
| B1-048 | 5 | 4 | TL | phân loại | K45; K36; K35 |
| B1-049 | 5 | 5 | TL | vận dụng | K53; K51 |
| B1-050 | 5 | 1 | TL | vận dụng | K20; K61 |
| B1-051 | 6 | 1 | TN | nền tảng | K07; K05 |
| B1-052 | 6 | 2 | TN | vận dụng | K12; K10 |
| B1-053 | 6 | 3 | TN | nền tảng | K23; K29 |
| B1-054 | 6 | 4 | TN | vận dụng | K35 |
| B1-055 | 6 | 5 | TN | vận dụng | K49; K48 |
| B1-056 | 6 | 4 | TN | vận dụng | K36; K43 |
| B1-057 | 6 | 2 | TL | vận dụng | K15; K13 |
| B1-058 | 6 | 3 | TL | phân loại | K31; K28; K29 |
| B1-059 | 6 | 5 | TL | phân loại | K52; K53; K50 |
| B1-060 | 6 | 6 | TL | vận dụng | K59; K60 |

## Đáp án trắc nghiệm nhanh

| Đợt | Đáp án |
|---|---|
| 1 | B1-001 **B**; B1-002 **C**; B1-003 **C**; B1-004 **A**; B1-005 **D**; B1-006 **C**; B1-007 **D** |
| 2 | B1-011 **D**; B1-012 **D**; B1-013 **C**; B1-014 **A**; B1-015 **D**; B1-016 **A**; B1-017 **C** |
| 3 | B1-021 **B**; B1-022 **D**; B1-023 **C**; B1-024 **C**; B1-025 **A**; B1-026 **A**; B1-027 **B** |
| 4 | B1-031 **A**; B1-032 **B**; B1-033 **D**; B1-034 **B**; B1-035 **B**; B1-036 **A**; B1-037 **C** |
| 5 | B1-041 **B**; B1-042 **D**; B1-043 **C**; B1-044 **B**; B1-045 **A**; B1-046 **B** |
| 6 | B1-051 **B**; B1-052 **C**; B1-053 **D**; B1-054 **A**; B1-055 **D**; B1-056 **A** |
## Đợt 1 — Đáp án và chấm bài

### B1-001 — B

Lấy thêm dữ liệu là thu thập; loại trùng là làm sạch; nối các bảng là biến đổi. Các thao tác chuẩn bị giúp đi từ dữ liệu thô đến thông tin dùng được.

- **A sai:** Đảo vai trò loại trùng và nối bảng.
- **C sai:** Lấy file mới không phải làm sạch; loại trùng không phải thu thập.
- **D sai:** Lấy file và nối bảng không tạo biểu đồ.

**Mục tiêu:** nhóm chính 1; chính K02; phụ K01. **Mức:** nền tảng. **Ngộ nhận:** Phân loại theo tên công cụ thay vì mục đích thao tác.

**Đọc lại:** G1; L§2; T§2.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-002 — C

Lưu bản sao riêng trước khi sửa. Cell code thực thi print và notebook còn hiển thị giá trị biểu thức cuối; Markdown dùng cho văn bản, không thực thi Python như cell code.

- **A sai:** Bỏ qua tác dụng của print.
- **B sai:** Quyền chỉ xem không cho sửa bản gốc; phải làm trên bản sao.
- **D sai:** Bỏ qua cơ chế hiển thị biểu thức cuối của notebook.

**Mục tiêu:** nhóm chính 2; chính K08; phụ K09, K17. **Mức:** nền tảng. **Ngộ nhận:** Nhầm mã với output, bỏ qua biểu thức cuối hoặc chưa lưu bản sao.

**Đọc lại:** G2 notebook (ngữ cảnh); L§1; T§0 W1; G2 notebook; L§1 cell2–4; T§2 hiển thị output; Lcell0; Tcell0,§0 W2.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-003 — C

venv được tạo bằng 3.11.9 vẫn dùng bản nền đó. .python-version ghi sau không sửa ngược môi trường, và freeze chỉ ghi các gói nó thu được; để khớp3.12.3 phải tạo venv bằng đúng trình thông dịch.

- **A sai:** Không có trình quản lý phiên bản; kích hoạt lại không tạo venv bằng Python khác.
- **B sai:** freeze không chuyển nội dung .python-version thành phiên bản Python nền.
- **D sai:** pip cài thư viện, không đổi trình thông dịch theo tệp phiên bản.

**Mục tiêu:** nhóm chính 3; chính K29; phụ K23, K28. **Mức:** vận dụng. **Ngộ nhận:** Coi .python-version hoặc requirements là cơ chế tự đổi Python.

**Đọc lại:** G2 .python-version; L§5 tạo venv (ngữ cảnh); G2 venv,.python-version; L§5; T§4 tự làm1; G2 requirements.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-004 — A

Nghĩa vụ khai báo theo việc đã sử dụng AI, không có ngưỡng phần trăm sửa code để miễn khai báo. Lab còn yêu cầu nêu prompt, sai lệch và cách kiểm chứng.

- **B sai:** Xóa hoặc sửa code không xóa lịch sử sử dụng công cụ.
- **C sai:** Nguồn không đặt ngưỡng giữ lại số dòng.
- **D sai:** Tên công cụ chưa đủ nội dung khai báo được yêu cầu.

**Mục tiêu:** nhóm chính 4; chính K38; phụ K46. **Mức:** vận dụng. **Ngộ nhận:** Đã sửa gần hết thì không còn phải khai báo.

**Đọc lại:** G3 khai báo; L§4 khai báo; T§3 bước5; Lcell21; T§3 bước5;P§4 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-005 — D

venv tách bộ thư viện giữa các dự án. VS Code dùng cho dự án local với phiên bản do người học kiểm soát; Colab thuận tiện cho thực hành có sẵn môi trường.

- **A sai:** Tên thư mục không tạo hai bộ thư viện độc lập.
- **B sai:** Hai bản ghi không tự tách nơi cài gói.
- **C sai:** Notebook không tự đóng gói một môi trường thư viện riêng.

**Mục tiêu:** nhóm chính 3; chính K22; phụ K21. **Mức:** nền tảng. **Ngộ nhận:** Nhầm tệp/thư mục hoặc requirements với sự cô lập của venv.

**Đọc lại:** G2 venv; L§5; T§4 tự làm1; G2 hai môi trường.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-006 — C

Chế độ áp dụng cho từng hoạt động: làm tại nhà mở, vấn đáp đóng. Việc đã khai báo không chuyển quyền sử dụng sang buổi vấn đáp.

- **A sai:** Trong hoạt động đóng, mức hỗ trợ ít không làm AI được phép.
- **B sai:** Khai báo không đổi chế độ của vấn đáp.
- **D sai:** Khai báo sau không hợp thức hóa sử dụng ở chế độ đóng.

**Mục tiêu:** nhóm chính 4; chính K35; phụ K39. **Mức:** vận dụng. **Ngộ nhận:** Đã khai báo nên được dùng AI khi vấn đáp.

**Đọc lại:** G3 hai chế độ; L§3 khai báo (ngữ cảnh); T§1 cách làm việc; G3 ranh giới gian lận; L§3 đọc hiểu; T§3 bước2–3 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-007 — D

Mai đã thực hiện tự phác và hỏi có bối cảnh. Còn ba bước đọc hiểu, kiểm chứng rồi khai báo; không dùng việc code chạy để thay cho hiểu và thử.

- **A sai:** Hoãn đọc hiểu và bỏ qua kiểm chứng ý nghĩa.
- **B sai:** Hai phản hồi AI không tự tạo phép kiểm độc lập.
- **C sai:** Dự đoán dùng kiểm chứng phải có trước hoặc độc lập, không lấy chính output làm chuẩn.

**Mục tiêu:** nhóm chính 5; chính K47; phụ K48, K49. **Mức:** vận dụng. **Ngộ nhận:** Bỏ hoặc đảo bước đọc hiểu, tự phác và kiểm chứng.

**Đọc lại:** G3 quy trình; L§4 bài 2–3; T§3; G3 tự phác/hỏi; L§4 bài 2; T§3 bước1–3; G mục AI hay sai/kiểm chứng; L§4 đọc hiểu; T§3 bước2–3.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-008

a) Run all dùng gia còn trong bộ nhớ nên in 80. b) Sau restart, A gặp NameError vì gia chưa được định nghĩa trong phiên sạch. c) Thêm cell `gia=40` trước A, chạy từ đầu và đối chiếu tổng với phép tính tay 40×2=80; chỉ chạy không lỗi chưa chứng minh đúng yêu cầu.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: kết quả 80 và dùng biến cũ | 0,5 |
| b: NameError tại A sau restart | 0,5 |
| c: định nghĩa gia trước A (0,5); kiểm độc lập 80 (0,5) | 1 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 2; chính K15; phụ K11, K16. **Mức:** phân loại. **Ngộ nhận:** Run all phiên cũ thành công nên tưởng notebook tự chạy được từ đầu.

**Đọc lại:** L§1 state; T§1 bước3; T§1 bước1; G3 kiểm chứng; L§1,§4 bài 1; T§1,§3.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-009

a) Nhóm đã minh bạch việc dùng AI; sửa nhiều code không miễn khai báo. b) Vẫn thiếu hiểu hàm và kiểm chứng số liệu. c) Người nộp chịu trách nhiệm về kết quả sai như bài sai khác; khai báo không miễn điểm sai hay thay cho hiểu code.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: ghi nhận khai báo và không có miễn trừ do sửa nhiều | 0,5 |
| b: chỉ ra cả thiếu hiểu và thiếu kiểm chứng | 0,75 |
| c: trách nhiệm người nộp, phân biệt khai báo với tính đúng | 0,75 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 4; chính K37; phụ K40, K38. **Mức:** phân loại. **Ngộ nhận:** Đã khai báo/đã sửa nhiều hoặc AI viết sai nên tưởng hết trách nhiệm.

**Đọc lại:** G3 ba trách nhiệm; L§3–4; T§3; G3 kiểm chứng; L§4 bài 1–2; T§3 bước4; G3 khai báo; L§4 khai báo; T§3 bước5 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-010

Git ghi lịch sử thay đổi, giúp theo dõi và quay lại các phiên bản; GitHub dùng lưu/cộng tác qua repo private của nhóm. Chỉ gửi bản cuối làm thiếu repo và lịch sử commit mà môn dùng trong đánh giá làm việc nhóm.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Git là lịch sử thay đổi, không chỉ nơi tải tệp | 0,75 |
| GitHub repo private/cộng tác | 0,5 |
| Thiếu lịch sử commit và repo theo cách nộp của môn | 0,75 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 6; chính K54. **Mức:** vận dụng. **Ngộ nhận:** Có bản code cuối nên tưởng không cần repo và lịch sử làm việc.

**Đọc lại:** G2 Git/GitHub.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### Cập nhật bao phủ sau đợt 1

Lũy kế 10/60: 7 TN, 3 TL.

| Nhóm | Đã xuất / kế hoạch |
|---|---:|
| 1 | 1 / 8 |
| 2 | 2 / 10 |
| 3 | 2 / 14 |
| 4 | 3 / 14 |
| 5 | 1 / 8 |
| 6 | 1 / 6 |

Đã có câu yêu cầu sử dụng: K01, K02, K08, K09, K11, K15, K16, K17, K21, K22, K23, K28, K29, K35, K37, K38, K39, K40, K46, K47, K48, K49, K54.
Mục chưa có câu: K03, K04, K05, K06, K07, K10, K12, K13, K14, K18, K19, K20, K24, K25, K26, K27, K30, K31, K32, K33, K34, K36, K41, K42, K43, K44, K45, K50, K51, K52, K53, K55, K56, K57, K58, K59, K60, K61.
Mục rộng còn nhánh/biến thể được bố trí ở đợt sau: K08, K15, K28, K29, K35, K37, K39, K40, K46, K47, K48, K49. Không tính việc chỉ nhắc trong lời giải là bao phủ.

## Đợt 2 — Đáp án và chấm bài

### B1-011 — D

Dữ liệu thật có thể lẫn định dạng, thiếu và bất thường. Chuẩn bị/kiểm tra là phần cốt lõi; giá lạ chưa tự chứng minh lỗi.

- **A sai:** Tự coi chưa biết bằng 0 tạo quy ước không được dữ kiện xác nhận.
- **B sai:** Không có quy tắc hay kiểm chứng nguồn để kết luận giá nhỏ chắc sai.
- **C sai:** Hiển thị được không xác nhận đầu vào hoặc thống kê đúng.

**Mục tiêu:** nhóm chính 1; chính K03; phụ K04. **Mức:** nền tảng. **Ngộ nhận:** Bỏ qua chuẩn bị dữ liệu hoặc kết luận cực trị sai chỉ từ độ lớn.

**Đọc lại:** G1; L§2 nhìn dữ liệu; T§2; L§4 bài 1; T§3.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-012 — D

Lần đầu A mới nằm trong file chứ chưa thực thi. Sau khi chạy A, x tồn tại xuyên cell nên B dùng được.

- **A sai:** Thứ tự nhìn thấy không chứng minh cell đã chạy.
- **B sai:** Python không tự khởi tạo biến chưa định nghĩa bằng 0.
- **C sai:** Các cell dùng chung trạng thái trong cùng phiên.

**Mục tiêu:** nhóm chính 2; chính K10; phụ K11. **Mức:** vận dụng. **Ngộ nhận:** Cell phía trên đã có trong file nên tưởng biến chắc tồn tại.

**Đọc lại:** L§1 state; T§1 bước1–2; T§1 bước1.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-013 — C

Đích cài theo trình thông dịch thực sự được gọi. Đề đã xác định executable là Python B, nên cài vào B; cwd và venv hiển thị đang kích hoạt không ghi đè đường dẫn đích danh.

- **A sai:** Bỏ qua trình thông dịch B được gọi đích danh.
- **B sai:** Chỉ có một Python thực hiện lệnh cài, không có hai lần cài.
- **D sai:** Đường dẫn đã được xác nhận thuộc venv B; đường dẫn tuyệt đối không biến nó thành Python hệ thống.

**Mục tiêu:** nhóm chính 3; chính K24; phụ K25. **Mức:** vận dụng. **Ngộ nhận:** Chuyển thư mục thì pip tự đổi môi trường.

**Đọc lại:** G2 venv; L§5 (lệnh tạo/kích hoạt); T§4 tự làm1; L§5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-014 — A

Quy tắc đóng áp dụng cho sử dụng AI trong hoạt động, không chỉ việc chép nguyên đáp án.

- **B sai:** Tự viết lại không làm việc dùng AI trong quiz thành được phép.
- **C sai:** Khai báo không chuyển hoạt động đóng sang mở.
- **D sai:** Trong lúc quiz đóng, hỗ trợ AI kiểu này vẫn là sử dụng AI.

**Mục tiêu:** nhóm chính 4; chính K35. **Mức:** nền tảng. **Ngộ nhận:** Chỉ hỏi một chút nên tưởng không tính là dùng AI.

**Đọc lại:** G3 hai chế độ; L§3 khai báo (ngữ cảnh); T§1 cách làm việc ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-015 — D

freeze ghi các phiên bản gói nó thu được từ môi trường hiện tại, không chỉ các tên người dùng trực tiếp gõ. Không cần đoán tên/số phụ thuộc chính xác.

- **A sai:** freeze ghi nhận, không chọn thêm gói để cài.
- **B sai:** Danh sách mô tả phiên bản hiện có, không phải lịch sử phiên bản.
- **C sai:** Giả định venv không kế thừa gói hệ thống đã loại suy luận đó.

**Mục tiêu:** nhóm chính 3; chính K27; phụ K26. **Mức:** vận dụng. **Ngộ nhận:** freeze chỉ ghi gói trực tiếp hoặc ghi cả lịch sử/cài đặt ngoài môi trường.

**Đọc lại:** G2 requirements; L§5 câu tự kiểm; L§5; T§4 tự làm1.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-016 — A

Thiếu nhãn thì không suy quyền dùng từ địa điểm, số điểm hay việc chỉ viết nháp. Cần thông tin còn thiếu từ giảng viên.

- **B sai:** Kiểm chứng và khai báo không thay điều kiện được phép sử dụng.
- **C sai:** Nguồn yêu cầu hỏi khi thiếu nhãn.
- **D sai:** Viết nháp vẫn là sử dụng AI cho bài.

**Mục tiêu:** nhóm chính 4; chính K36. **Mức:** vận dụng. **Ngộ nhận:** Làm ở nhà/ít điểm/chỉ nháp nên tưởng mặc định mở.

**Đọc lại:** G3 hai chế độ; L§5 nhãn mở; T§4 nhãn mở ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-017 — C

G§4 nêu đúng bốn trọng số; phần làm BTL tại nhà mở không làm vấn đáp mở. Đây là cơ cấu học phần, không phải tỷ trọng ngân hàng câu hỏi.

- **A sai:** Đảo trọng số kiểm tra lớp và giữa kỳ.
- **B sai:** Đúng trọng số nhưng sai chế độ vấn đáp.
- **D sai:** Sai trọng số lab và BTL.

**Mục tiêu:** nhóm chính 6; chính K57. **Mức:** nền tảng. **Ngộ nhận:** Gộp cả BTL vào một chế độ hoặc đảo các đầu điểm.

**Đọc lại:** G4 cơ cấu điểm/kế hoạch; P§2 và tiêu đề PDF mẫu.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-018

80=(40+80+120)/3, chỉ là trung bình ba giá đã biết, chưa xác định trung bình thực của cả năm. Có thể lấy chính mẫu này, tự tính tay tổng 240/số giá biết 3=80 để đối chiếu và kiểm việc xử lý hai ô chưa biết; không tự coi chúng là 0, phải nêu rõ quy ước và tập giá được dùng.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: ba giá, phép tính80 và giới hạn cả năm | 1 |
| b: mẫu/đối chiếu độc lập có kết quả80 (0,5); nêu quy ước không tự điền0 (0,5) | 1 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 5; chính K52; phụ K50. **Mức:** phân loại. **Ngộ nhận:** Code mean chạy được nên tưởng đã trả lời giá của cả các hàng chưa biết.

**Đọc lại:** G3 quy ước mean; L§4 kiểm chứng (ngữ cảnh); T§3 kiểm chứng (áp dụng); G kiểm chứng; L§4 bài 2; T§3 bước4.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-019

a) Tệp nằm ở B nhưng freeze dùng Python của A nên mô tả các gói mà nó thu được từ A. b) Kích hoạt đúng venv B rồi dùng Python của B ghi lại requirements; vị trí lưu không xác định môi trường được chụp.

```bash
source .venv/bin/activate
python -m pip freeze > requirements.txt
```

Hai lệnh này được thực hiện tại B; `.venv` ở đó là venv B theo đề. Không cần cài thêm gói để sửa việc chụp nhầm.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: phân biệt tệp ở B với môi trường A | 1 |
| b: chọn/kích hoạt đúng B (0,5); freeze lại bằng Python B (0,5) | 1 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 3; chính K25; phụ K24, K27. **Mức:** phân loại. **Ngộ nhận:** Ghi requirements ở thư mục B nên tưởng đã chụp môi trường B.

**Đọc lại:** G2 venv; L§5; T§4 tự làm1; L§5 (lệnh tạo/kích hoạt); G2 requirements; L§5 câu tự kiểm.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-020

Phần code không giải thích được nhận 0 điểm đối với cá nhân An. Không tự suy thành cả nhóm nhận 0; khai báo trung thực không thay trách nhiệm hiểu, còn việc An không dùng AI trong vấn đáp là đúng chế độ.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Đúng phạm vi phần không giải thích được và cá nhân An | 1 |
| Không suy0 cả nhóm; phân biệt khai báo/hiểu với tuân thủ chế độ | 1 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 4; chính K39; phụ K44. **Mức:** vận dụng. **Ngộ nhận:** Đã khai báo thì được miễn hiểu, hoặc hậu quả cá nhân tự chuyển thành 0 toàn nhóm.

**Đọc lại:** G3 ranh giới gian lận; L§3 đọc hiểu; T§3 bước2–3; L§4 kiểm chứng; T§3 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### Cập nhật bao phủ sau đợt 2

Lũy kế 20/60: 14 TN, 6 TL.

| Nhóm | Đã xuất / kế hoạch |
|---|---:|
| 1 | 2 / 8 |
| 2 | 3 / 10 |
| 3 | 5 / 14 |
| 4 | 6 / 14 |
| 5 | 2 / 8 |
| 6 | 2 / 6 |

Đã có câu yêu cầu sử dụng: K01, K02, K03, K04, K08, K09, K10, K11, K15, K16, K17, K21, K22, K23, K24, K25, K26, K27, K28, K29, K35, K36, K37, K38, K39, K40, K44, K46, K47, K48, K49, K50, K52, K54, K57.
Mục chưa có câu: K05, K06, K07, K12, K13, K14, K18, K19, K20, K30, K31, K32, K33, K34, K41, K42, K43, K45, K51, K53, K55, K56, K58, K59, K60, K61.
Mục rộng còn nhánh/biến thể được bố trí ở đợt sau: K08, K10, K15, K24, K25, K26, K28, K29, K35, K36, K37, K40, K44, K46, K47, K48, K49, K50, K52, K57. Không tính việc chỉ nhắc trong lời giải là bao phủ.

## Đợt 3 — Đáp án và chấm bài

### B1-021 — B

Từ dữ liệu sạch, phép tổng hợp tạo thông tin; biểu đồ giúp đọc; báo cáo kết nối thông tin với quyết định và giới hạn. Bảng sạch chưa tự là quyết định.

- **A sai:** Tổng hợp số theo khu là biến đổi, không phải sửa dữ liệu bẩn.
- **C sai:** Tình huống mô tả vẽ biểu đồ trước khi viết khuyến nghị; đảo hai bước cuối.
- **D sai:** Bảng tổng hợp tạo thông tin, chưa phải thao tác vẽ biểu đồ.

**Mục tiêu:** nhóm chính 1; chính K01; phụ K02. **Mức:** nền tảng. **Ngộ nhận:** Coi dữ liệu sạch là đã có kết luận hoặc đảo quyết định và bằng chứng.

**Đọc lại:** G1; L§2; T§2.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-022 — D

Colab là môi trường có thể chạy lệnh hệ điều hành qua !. Đây không phải lệnh cài/chọn bản Python trên máy cá nhân.

- **A sai:** Markdown không thực thi lệnh hệ điều hành; ! trong cell code mới gọi lệnh.
- **B sai:** --version báo phiên bản, không đổi phiên bản.
- **C sai:** Lệnh thực thi trong môi trường Colab đang chạy, không tự truy vấn máy cá nhân.

**Mục tiêu:** nhóm chính 2; chính K19; phụ K08. **Mức:** nền tảng. **Ngộ nhận:** Nhầm ! với Markdown hoặc lệnh xem phiên bản với lệnh đổi phiên bản.

**Đọc lại:** L§3; T§4 tự làm1; G2 notebook (ngữ cảnh); L§1; T§0 W1.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-023 — C

requirements ghi thư viện, không ghi thay phiên bản Python. Cần bản ghi riêng như .python-version cùng hướng dẫn chọn Python; chỉ thêm tệp không tự cài Python.

- **A sai:** Phiên bản thư viện không đồng nhất với phiên bản trình thông dịch.
- **B sai:** freeze ghi môi trường hiện có, không phục hồi môi trường trên máy cũ.
- **D sai:** Tên ngôn ngữ chung chưa ghi hoặc chọn đúng phiên bản trình thông dịch đã kiểm thử.

**Mục tiêu:** nhóm chính 3; chính K28; phụ K29. **Mức:** vận dụng. **Ngộ nhận:** Có requirements là đủ thông tin về cả Python và thư viện.

**Đọc lại:** G2 requirements; L§5; T§4 tự làm1; G2 .python-version; L§5 tạo venv (ngữ cảnh).

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-024 — C

Minh bạch và tính đúng là các nghĩa vụ khác nhau. Không tự biến lỗi tính toán đã khai báo thành hành vi giấu AI, cũng không miễn trách nhiệm kết quả.

- **A sai:** Trách nhiệm sản phẩm thuộc người nộp, không chuyển cho công cụ.
- **B sai:** Khai báo không sửa phép tính hoặc thay kiểm chứng.
- **D sai:** Đề nói hoạt động mở và minh bạch; không được tự suy vi phạm chế độ.

**Mục tiêu:** nhóm chính 4; chính K40; phụ K44. **Mức:** vận dụng. **Ngộ nhận:** Đổ lỗi cho AI hoặc gộp bài sai với gian lận/thiếu minh bạch.

**Đọc lại:** G3 kiểm chứng; L§4 bài 1–2; T§3 bước4; G3 ranh giới gian lận; L§4 kiểm chứng; T§3 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-025 — A

Đây là lệnh kích hoạt cho Bash trên hệ POSIX đã nêu. Không dùng lệnh chỉ chuyển thư mục hoặc ghi danh sách gói để thay kích hoạt.

- **B sai:** Chỉ đổi cwd, không kích hoạt venv.
- **C sai:** Ghi danh sách gói, không chọn venv mới.
- **D sai:** Đây là tạo venv, không phải kích hoạt trong shell hiện tại.

**Mục tiêu:** nhóm chính 3; chính K24. **Mức:** nền tảng. **Ngộ nhận:** Nhầm tạo môi trường, đi vào thư mục và kích hoạt.

**Đọc lại:** G2 venv; L§5 (lệnh tạo/kích hoạt); T§4 tự làm1.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-026 — A

Tổng 100 chỉ kiểm tổng tỷ lệ, không kiểm đúng nhãn. Ở đây A và B bị hoán đổi dù tổng khớp.

- **B sai:** Có phản ví dụ ngay trong dữ kiện: A,B bị đổi.
- **C sai:** Sai nhãn/số đếm không phải sai làm tròn.
- **D sai:** Lặp lại cùng nguồn AI chưa là phép kiểm độc lập với dữ liệu.

**Mục tiêu:** nhóm chính 5; chính K51; phụ K50. **Mức:** vận dụng. **Ngộ nhận:** Tổng tỷ lệ 100% nên tưởng từng nhóm đúng.

**Đọc lại:** G3 kiểm chứng; L§4 kiểm chứng (ngữ cảnh); T§3 bước1,4; G kiểm chứng; L§4 bài 2; T§3 bước4.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-027 — B

G§4 giới thiệu một đề chung nhưng mỗi nhóm một thành phố, với pipeline và hợp phần LLM. Bộ biểu đồ riêng lẻ của thành phố khác chưa đáp ứng mô tả sản phẩm.

- **A sai:** Bỏ phân công thành phố và các thành phần sản phẩm đã nêu.
- **C sai:** Output/ảnh không thay các hợp phần chạy được đã yêu cầu.
- **D sai:** Nguồn nêu thành phố theo phân công, không xác định là tùy chọn.

**Mục tiêu:** nhóm chính 6; chính K55. **Mức:** vận dụng. **Ngộ nhận:** Nhầm sản phẩm cuối nhìn được với toàn bộ sản phẩm có thể chạy và đúng phân công.

**Đọc lại:** G4 BTL; T§2 Airbnb (ngữ cảnh).

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-028

a) Trước restart B in 3; sau restart B gặp NameError. b) Xóa cell loại mã khỏi file chứ không xóa biến do lần chạy trước tạo trong phiên đang sống; restart mới xóa trạng thái đó. c) Khôi phục cell định nghĩa muc trước B rồi kiểm Restart & Run all.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: in 3 rồi NameError | 0,75 |
| b: phân biệt xóa mã với xóa trạng thái | 0,75 |
| c: thêm định nghĩa trước dùng và kiểm phiên sạch | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 2; chính K12; phụ K14, K15. **Mức:** phân loại. **Ngộ nhận:** Xóa cell nên biến và tác động cũ tự mất.

**Đọc lại:** L§1 state; T§1 mở đầu; T§0 W2,§1; T§1 bước3.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-029

Dùng AI dịch cũng là hỗ trợ AI, nên khai Không dùng AI là không trung thực; cần khai công cụ, công việc và kiểm tra bản dịch giữ đúng nội dung. Nhờ AI viết lại code nhóm khác vẫn là chép bài, không trở thành được phép nhờ khác câu chữ; nhóm phải làm phần của mình, hiểu, kiểm chứng và khai báo hỗ trợ hợp lệ.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Nhận diện hỗ trợ dịch và khai man | 0,75 |
| Viết lại bài nhóm khác vẫn vi phạm | 0,75 |
| Sửa theo tự làm nội dung + khai báo/kiểm chứng, không bịa phạt | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 4; chính K43; phụ K42. **Mức:** phân loại. **Ngộ nhận:** Chỉ code mới phải khai báo; AI viết lại bài khác làm mất nguồn gốc chép.

**Đọc lại:** G3 khai báo dùng gì/việc gì; T§3 mẫu khai báo (ngữ cảnh);P§1,§3; G3 ranh giới gian lận; T§3 khai báo (ngữ cảnh) ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-030

Lần lượt là thu thập, làm sạch, biến đổi, trực quan và kể chuyện. Chuẩn bị/kiểm tra dữ liệu là cơ sở để thống kê và kết luận đáng tin; làm biểu đồ hay viết báo cáo tốt không tự chữa đầu vào sai.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Đúng cả năm giai đoạn theo thứ tự; mỗi giai đoạn0,3 | 1,5 |
| Nêu tác động đầu vào đến kết luận | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 1; chính K02. **Mức:** vận dụng. **Ngộ nhận:** Gộp xử lý thiếu vào biến đổi hoặc nghĩ bước trình bày bù được dữ liệu đầu vào.

**Đọc lại:** G1; L§2; T§2.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### Cập nhật bao phủ sau đợt 3

Lũy kế 30/60: 21 TN, 9 TL.

| Nhóm | Đã xuất / kế hoạch |
|---|---:|
| 1 | 4 / 8 |
| 2 | 5 / 10 |
| 3 | 7 / 14 |
| 4 | 8 / 14 |
| 5 | 3 / 8 |
| 6 | 3 / 6 |

Đã có câu yêu cầu sử dụng: K01, K02, K03, K04, K08, K09, K10, K11, K12, K14, K15, K16, K17, K19, K21, K22, K23, K24, K25, K26, K27, K28, K29, K35, K36, K37, K38, K39, K40, K42, K43, K44, K46, K47, K48, K49, K50, K51, K52, K54, K55, K57.
Mục chưa có câu: K05, K06, K07, K13, K18, K20, K30, K31, K32, K33, K34, K41, K45, K53, K56, K58, K59, K60, K61.
Mục rộng còn nhánh/biến thể được bố trí ở đợt sau: K10, K12, K14, K15, K24, K25, K26, K28, K29, K35, K36, K37, K40, K43, K44, K46, K47, K48, K49, K50, K51, K52, K57. Không tính việc chỉ nhắc trong lời giải là bao phủ.

## Đợt 4 — Đáp án và chấm bài

### B1-031 — A

Nguồn giới thiệu Python cùng NumPy, pandas, trực quan và LLM; mục tiêu làm chủ quá trình, không chỉ tự gõ hoặc gọi tên công cụ. Hiểu từng dòng là điều kiện để chỉ đạo và kiểm chứng.

- **B sai:** Bỏ hai mục tiêu được nêu rõ trong G§3.
- **C sai:** Môn vẫn yêu cầu hiểu code nộp để kiểm chứng và vấn đáp.
- **D sai:** Nguồn dạy quá trình từ dữ liệu thô đến quyết định và pipeline.

**Mục tiêu:** nhóm chính 1; chính K05; phụ K06. **Mức:** nền tảng. **Ngộ nhận:** Nhầm làm chủ công cụ với chỉ gõ tay hoặc chỉ nhận code chạy được.

**Đọc lại:** G1–2; L§2,§5; T§2; G3 mục tiêu2026; L§3–4; T§3.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-032 — B

B cộng dồn trên trạng thái hiện có; chạy lại A đặt dem về0 trước lần B cuối.

- **A sai:** Tưởng mỗi lần chạy B notebook tự khởi tạo lại biến.
- **C sai:** Bỏ qua lần chạy lại cell khởi tạo A.
- **D sai:** In giá trị trước tăng thay vì sau phép gán trong B.

**Mục tiêu:** nhóm chính 2; chính K13; phụ K10. **Mức:** vận dụng. **Ngộ nhận:** Không phân biệt chạy lại cell tăng với chạy lại cell khởi tạo.

**Đọc lại:** L§1 state; T§1 bước2; T§1 bước1–2.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-033 — D

Notebook lưu mã và có thể lưu output, không mang theo toàn bộ thư viện hoặc bộ biến đang sống trên Colab. Cần venv được chọn trong VS Code và các thư viện theo hướng dẫn.

- **A sai:** Định dạng notebook không tự đóng gói thư viện.
- **B sai:** Output cũ không phản ánh trạng thái hay gói của phiên mới.
- **C sai:** Các import/định nghĩa phải được thực thi trong môi trường mới có đủ thư viện.

**Mục tiêu:** nhóm chính 3; chính K34; phụ K21. **Mức:** vận dụng. **Ngộ nhận:** Đã tải notebook nên tưởng có cả thư viện và trạng thái thực thi.

**Đọc lại:** G2 notebook,venv; L§1,§5 tải/chạy local; T§1 state; G2 hai môi trường; L§5; T§4 tự làm1.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-034 — B

Quyền dùng đến từ nhãn mở; hiểu, kiểm chứng và khai báo đều phải có. Không cần suy thêm điều kiện xin phép riêng khi đề đã cho phép.

- **A sai:** Minh bạch chưa thay nghĩa vụ hiểu và kiểm chứng.
- **C sai:** Gợi ý vẫn là hỗ trợ đã dùng, phải khai đúng.
- **D sai:** Vừa thiếu khai báo, vừa chưa có đối chiếu độc lập.

**Mục tiêu:** nhóm chính 4; chính K41; phụ K37. **Mức:** vận dụng. **Ngộ nhận:** Chỉ làm đúng một hoặc hai trách nhiệm rồi coi đã đáp ứng toàn bộ.

**Đọc lại:** G3 ranh giới gian lận; L§4 bài 2–3; T§3–4; G3 ba trách nhiệm; L§3–4; T§3 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-035 — B

install -r đọc danh sách gói để cài. freeze ghi trạng thái gói hiện tại, không cài lại.

- **A sai:** Ghi đè bản ghi bằng môi trường hiện có, không cài gói từ tệp.
- **C sai:** Chỉ yêu cầu cài pandas, không đọc danh sách gói và phiên bản trong requirements.txt.
- **D sai:** Chỉ xem phiên bản trình thông dịch, không cài thư viện.

**Mục tiêu:** nhóm chính 3; chính K26. **Mức:** nền tảng. **Ngộ nhận:** Nhầm lệnh ghi môi trường với lệnh cài lại từ bản ghi.

**Đọc lại:** G2 requirements; L§5; T§4 tự làm1.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-036 — A

Hai phản hồi giống nhau có thể lặp cùng sai lầm. Cần kiểm cơ chế hàm và kết quả dựa trên dữ liệu/chuẩn độc lập.

- **B sai:** Lặp thêm cùng nguồn không làm phép kiểm độc lập.
- **C sai:** Nhất quán phản hồi không xác nhận đúng mục tiêu hay dữ liệu.
- **D sai:** Đổi tên biến không tạo phép tính độc lập và không lỗi chưa là đúng.

**Mục tiêu:** nhóm chính 5; chính K50; phụ K49. **Mức:** vận dụng. **Ngộ nhận:** Hai lần hỏi AI cùng đáp án nên tưởng đã kiểm chứng độc lập.

**Đọc lại:** G kiểm chứng; L§4 bài 2; T§3 bước4; G mục AI hay sai/kiểm chứng; L§4 đọc hiểu; T§3 bước2–3.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-037 — C

Nguồn nêu test chung chạy trên repo, kể cả hợp phần LLM, và vấn đáp từng người. Output lưu và khai báo là các phần riêng, không thay khả năng chạy hay hiểu.

- **A sai:** Bản ghi kết quả không thay sản phẩm thực thi trên máy chấm.
- **B sai:** Nguồn nêu vấn đáp từng thành viên.
- **D sai:** Minh bạch không thay việc chạy code và giải thích.

**Mục tiêu:** nhóm chính 6; chính K56; phụ K34. **Mức:** vận dụng. **Ngộ nhận:** Notebook có output hoặc khai báo đủ nên tưởng đã đáp ứng cách chấm repo và vấn đáp.

**Đọc lại:** G4 BTL; L§5 chạy local; G2 notebook,venv; L§1,§5 tải/chạy local; T§1 state.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-038

Dùng đúng Python đã ghi/kiểm thử để tạo venv mới trên máy nhận, cài thư viện từ requirements.txt rồi chạy theo README. README cần ghi hệ điều hành cùng lệnh dựng và chạy; sao chép .venv không thay việc dựng lại môi trường theo các bản ghi.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Chọn đúng Python và tạo venv mới | 0,75 |
| Cài thư viện từ requirements rồi chạy theo README | 0,75 |
| README có OS/lệnh; không dựa vào copy .venv | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 3; chính K30; phụ K31, K32. **Mức:** phân loại. **Ngộ nhận:** Đóng gói bằng cách chép .venv thay vì ghi và dựng lại môi trường.

**Đọc lại:** G2 chạy lại máy khác; L§5 tự dựng venv; G2 .python-version; L§5; T§4 tự làm1; L§5 (ngữ cảnh).

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-039

I vi phạm chế độ đóng; khai báo không cấp quyền dùng AI trong quiz. II thiếu minh bạch/giấu sử dụng ở chế độ mở; quyền dùng không miễn khai báo. III là bài làm sai và người nộp chịu trách nhiệm; minh bạch không bảo đảm nội dung đúng.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| I: phân loại và giải thích đúng | 0,75 |
| II: phân loại và giải thích đúng | 0,75 |
| III: bài sai/trách nhiệm, không tự suy gian lận | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 4; chính K44; phụ K35, K40. **Mức:** phân loại. **Ngộ nhận:** Đánh đồng được phép, khai báo và tính đúng; một phần đúng tự hợp thức hóa phần sai.

**Đọc lại:** G3 ranh giới gian lận; L§4 kiểm chứng; T§3; G3 hai chế độ; L§3 khai báo (ngữ cảnh); T§1 cách làm việc; G3 kiểm chứng; L§4 bài 1–2; T§3 bước4 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-040

Tôi dùng ChatGPT (không biết model cụ thể) để viết nháp code tính phần trăm từng room_type của ds; prompt chính yêu cầu tính phần trăm số hàng theo room_type của ds ở thang 0–100. AI ban đầu trả tỷ lệ 0–1, tôi sửa sang phần trăm và kiểm bằng đếm tay mẫu nhỏ, đối chiếu từng nhóm cùng tổng gần 100%.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Tên công cụ và việc dùng, không bịa model | 0,5 |
| Prompt chính và sai lệch được phát hiện | 0,75 |
| Cách sửa và phép kiểm cụ thể | 0,75 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 5; chính K46; phụ K47. **Mức:** vận dụng. **Ngộ nhận:** Khai chung đã dùng AI mà không nêu việc, sai lệch hoặc cách kiểm chứng.

**Đọc lại:** G3 khai báo; Lcell21; T§3 bước5;P§4; G3 quy trình; L§4 bài 2–3; T§3.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### Cập nhật bao phủ sau đợt 4

Lũy kế 40/60: 28 TN, 12 TL.

| Nhóm | Đã xuất / kế hoạch |
|---|---:|
| 1 | 5 / 8 |
| 2 | 6 / 10 |
| 3 | 10 / 14 |
| 4 | 10 / 14 |
| 5 | 5 / 8 |
| 6 | 4 / 6 |

Đã có câu yêu cầu sử dụng: K01, K02, K03, K04, K05, K06, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K19, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K46, K47, K48, K49, K50, K51, K52, K54, K55, K56, K57.
Mục chưa có câu: K07, K18, K20, K33, K45, K53, K58, K59, K60, K61.
Mục rộng còn nhánh/biến thể được bố trí ở đợt sau: K10, K12, K13, K14, K15, K24, K25, K28, K29, K31, K35, K36, K43, K46, K48, K49, K50, K51, K52, K57. Không tính việc chỉ nhắc trong lời giải là bao phủ.

## Đợt 5 — Đáp án và chấm bài

### B1-041 — B

Chất lượng kết luận phụ thuộc đầu vào. Ô thiếu không tự là 0, giá nhỏ không tự là lỗi; cần kiểm nguồn/quy ước rồi mới diễn giải.

- **A sai:** Thay hình thức không kiểm tính đúng của dữ liệu đã biến đổi.
- **C sai:** Không lỗi cú pháp không xác nhận quy ước phân tích.
- **D sai:** Khai nguồn hỗ trợ không chuyển trách nhiệm kết luận cho người đọc.

**Mục tiêu:** nhóm chính 1; chính K04; phụ K03. **Mức:** vận dụng. **Ngộ nhận:** Code/biểu đồ chạy được nên tưởng quy ước đầu vào và kết luận đúng.

**Đọc lại:** G1; L§4 bài 1; T§3; L§2 nhìn dữ liệu; T§2.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-042 — D

shape theo thứ tự số hàng, số cột; bảng đếm cho biết số bản ghi mỗi nhãn, không cho giá trung bình hay lượt đặt.

- **A sai:** Đảo hai thành phần shape.
- **B sai:** Số đếm7 không phải số đo giá.
- **C sai:** Vị trí cuối bảng không làm số 2 lớn hơn7; phải đọc số đếm.

**Mục tiêu:** nhóm chính 2; chính K18. **Mức:** nền tảng. **Ngộ nhận:** Đảo shape hoặc diễn giải bảng đếm thành thống kê giá.

**Đọc lại:** G2 notebook; L§2; T§2 kiểm tra.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-043 — C

Trạng thái môi trường ở từng shell và Python thực sự được gọi quyết định đích thao tác; cùng cwd không làm hai venv thành một.

- **A sai:** Nhầm cwd với môi trường Python của cửa sổ1.
- **B sai:** Hai venv tách bộ thư viện; cài vào A không tự cài vào B.
- **D sai:** Shell2 không tự đổi Python theo thao tác của shell1.

**Mục tiêu:** nhóm chính 3; chính K25; phụ K24. **Mức:** vận dụng. **Ngộ nhận:** Cùng thư mục hoặc cùng máy nên tưởng hai terminal dùng cùng môi trường.

**Đọc lại:** G2 venv; L§5; T§4 tự làm1; L§5 (lệnh tạo/kích hoạt).

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-044 — B

Mẫu lecture cho phép ghi không dùng; trang Chính sách AI§4 cũng xác định đây là một khai báo. Phải phản ánh đúng việc đã làm.

- **A sai:** Nguồn yêu cầu ghi rõ cả trường hợp không dùng.
- **C sai:** Bịa công cụ làm bản khai không trung thực.
- **D sai:** Không dùng AI không bảo đảm bài đúng hay miễn trách nhiệm kết quả.

**Mục tiêu:** nhóm chính 4; chính K46. **Mức:** nền tảng. **Ngộ nhận:** Không dùng AI nên bỏ khai báo hoặc nghĩ được miễn kiểm chứng.

**Đọc lại:** G3 khai báo; Lcell21; T§3 bước5;P§4 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-045 — A

Môi trường là một điều kiện, không khóa dữ liệu đầu vào hoặc chứng minh code đúng. Thay đổi dữ liệu có thể làm kết quả khác dù môi trường khớp.

- **B sai:** Không loại trừ thay đổi đầu vào được nêu rõ.
- **C sai:** Tái lập thư viện chưa là kiểm chứng phép tính hay đầu vào.
- **D sai:** Không được thay kết quả để khớp số cũ thay vì kiểm nguyên nhân.

**Mục tiêu:** nhóm chính 3; chính K33. **Mức:** vận dụng. **Ngộ nhận:** Đúng môi trường nên kết quả phải như cũ hoặc phải đúng dù dữ liệu đã đổi.

**Đọc lại:** G2–3; L§4 kiểm chứng; T§3 kiểm chứng.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-046 — B

G§1 phân giai đoạn theo bài, không tự đồng nhất số bài với số tuần. G§4/chính sách nêu15 phút; tiêu đề đề mẫu 20/60 phút không tự là thông báo sửa quy định hay thời lượng thi thật.

- **A sai:** Nguồn nêu số bài; không được tự chuyển thành số tuần.
- **C sai:** Sai cách phân giai đoạn của G§1.
- **D sai:** Lấy thời lượng đề mẫu làm cập nhật hành chính không có căn cứ.

**Mục tiêu:** nhóm chính 6; chính K58; phụ K57. **Mức:** vận dụng. **Ngộ nhận:** Nhầm số bài với tuần, hoặc coi đề mẫu là thông báo đổi chính sách/thời lượng.

**Đọc lại:** G1 lộ trình; G4 cơ cấu điểm/kế hoạch; P§2 và tiêu đề PDF mẫu.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-047

a) print gặp NameError vì biến ten trong bộ nhớ phiên đã bị xóa. b) Chỉ restart không xóa mã notebook, output đã được lưu trong tài liệu hoặc tệp Drive; các output lưu là bản ghi cũ, không chứng minh biến ten đã tồn tại lại. Bản sao Drive cần được lưu trước khi làm để giữ phiên bản riêng, rồi chạy lại các định nghĩa khi khởi động phiên mới.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: NameError do mất biến phiên | 0,75 |
| b: phân biệt trạng thái với mã/output lưu/tệp đã lưu (0,75); không dùng output cũ chứng minh trạng thái mới (0,5) | 1,25 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 2; chính K14; phụ K11, K17. **Mức:** phân loại. **Ngộ nhận:** Restart xóa cả file hoặc output cũ đồng nghĩa biến vẫn sống.

**Đọc lại:** L§1 state; T§0 W2,§1; T§1 bước1; Lcell0; Tcell0,§0 W2.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-048

Khuyến nghị tự gõ để học không làm phần tự làm đã gắn mở thành đóng; phải đọc nhãn và hướng dẫn của từng hoạt động. Quiz đóng vẫn cấm AI dù chỉ hỏi chút. Nếu một hoạt động thiếu nhãn hoặc quyền dùng chưa rõ, hỏi giảng viên trước khi dùng, không tự suy từ địa điểm hay khuyến nghị học tập.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Phân biệt khuyến nghị với nhãn mở ở phần tự làm | 0,75 |
| Quiz đóng không được hỏi chút | 0,75 |
| Hỏi GV khi chế độ chưa rõ | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 4; chính K45; phụ K36, K35. **Mức:** phân loại. **Ngộ nhận:** Đồng nhất nên tự gõ với cấm mọi phần, nhưng lại miễn trừ hỏi ít ở quiz.

**Đọc lại:** G3 nhãn chế độ; L§4 khuyến khích dùng AI; Tcell1 và§4; G3 hai chế độ; L§5 nhãn mở; T§4 nhãn mở; L§3 khai báo (ngữ cảnh); T§1 cách làm việc ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-049

a) Chỉ kiểm được khoảng tỷ lệ A và tổng gần 100; B,C vẫn sai vì đếm tay cho B15%,C5%. b) Các tỷ lệ đúng là A0,8/B0,15/C0,05, tương ứng80%/15%/5%; cần đối chiếu từng nhãn với số đếm gốc16/20,3/20,1/20. Pass vài assert không chứng minh mọi nhãn hay mọi dữ liệu nguồn đúng.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Nêu đúng phạm vi hai assert đã qua | 0,5 |
| Phát hiện B15%,C5% mới đúng | 0,5 |
| Đủ ba tỷ lệ 0–1 và phần trăm tương ứng | 0,5 |
| Đối chiếu từng nhãn bằng số đếm độc lập; nêu giới hạn ca thử | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 5; chính K53; phụ K51. **Mức:** vận dụng. **Ngộ nhận:** Vài assert qua nên tưởng mọi nhóm và mọi dữ liệu đều đúng.

**Đọc lại:** G3 kiểm chứng; L§4 bài 1–2; T§3 bước4 (giới hạn kiểm); L§4 kiểm chứng (ngữ cảnh); T§3 bước1,4.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-050

a) Mỗi chấm biểu diễn một con chim; màu phân biệt loài, và gộp theo species là chia dữ liệu thành các nhóm loài để xử lý/vẽ từng nhóm, không tự là phép đếm. b) Không dán API key thật vào code hay commit; dùng chỗ lưu Secrets được giới thiệu (hoặc biến môi trường theo trang chính sách), chưa cần học kỹ thuật gọi API ở Bài 1.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Đúng đơn vị chấm và màu | 0,75 |
| Gộp theo loài ở mức ý nghĩa, không yêu cầu cú pháp | 0,5 |
| Không dán/commit khóa; nêu Secrets | 0,75 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 1; chính K20; phụ K61. **Mức:** vận dụng. **Ngộ nhận:** Lấy demo làm yêu cầu kỹ thuật bài sau hoặc công khai khóa thật trong notebook.

**Đọc lại:** L§2 đồ thị,§4 bài 2; T§2 biểu đồ; Lcell16; P§3 công cụ/dữ liệu.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### Cập nhật bao phủ sau đợt 5

Lũy kế 50/60: 34 TN, 16 TL.

| Nhóm | Đã xuất / kế hoạch |
|---|---:|
| 1 | 7 / 8 |
| 2 | 8 / 10 |
| 3 | 12 / 14 |
| 4 | 12 / 14 |
| 5 | 6 / 8 |
| 6 | 5 / 6 |

Đã có câu yêu cầu sử dụng: K01, K02, K03, K04, K05, K06, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K61.
Mục chưa có câu: K07, K59, K60.
Mục rộng còn nhánh/biến thể được bố trí ở đợt sau: K10, K12, K13, K15, K28, K29, K31, K35, K36, K43, K48, K49, K50, K52, K53. Không tính việc chỉ nhắc trong lời giải là bao phủ.

## Đợt 6 — Đáp án và chấm bài

### B1-051 — B

G§1 đặt môn sau nền tảng tư duy/Python, tập trung làm chủ dữ liệu với NumPy, pandas, trực quan, LLM, làm nền cho ứng dụng sau.

- **A sai:** Nhầm môn xử lý dữ liệu với môn học máy và bỏ kỹ năng chuẩn bị dữ liệu.
- **C sai:** Môn này dạy xây quá trình từ dữ liệu thô, không hoãn phần đó sang môn sau.
- **D sai:** Python cơ bản là nền được dùng để làm chủ dữ liệu, Colab chỉ là công cụ thực hành.

**Mục tiêu:** nhóm chính 1; chính K07; phụ K05. **Mức:** nền tảng. **Ngộ nhận:** Nhầm môn với đào tạo mô hình chuyên sâu hoặc khóa chỉ cài công cụ.

**Đọc lại:** G1 môn này đứng ở đâu; G1–2; L§2,§5; T§2.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-052 — C

Sửa văn bản code chưa cập nhật biến trong phiên. B đầu sau sửa vẫn dùng a=2; chạy A mới đặt a=50 nên B sau đó in 150.

- **A sai:** Tưởng sửa code tự chạy phép gán mới.
- **B sai:** Bỏ qua lần thực thi cell A mới.
- **D sai:** Chỉ sửa cell không xóa biến a đã có trong phiên.

**Mục tiêu:** nhóm chính 2; chính K12; phụ K10. **Mức:** vận dụng. **Ngộ nhận:** Sửa cell tự đổi biến hoặc tự hủy biến cũ.

**Đọc lại:** L§1 state; T§1 mở đầu; T§1 bước1–2.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-053 — D

Python thực sự được gọi tạo venv quyết định phiên bản nền. Tệp khác nội dung là thông tin phải làm rõ, không làm lệnh tự chọn3.11.9.

- **A sai:** Đã nêu không có công cụ tự đọc tệp để chuyển phiên bản.
- **B sai:** venv không tự chọn bản mới nhất khác executable được gọi.
- **C sai:** venv đã được tạo bằng trình thông dịch có sẵn; pip cài gói không tạo Python nền.

**Mục tiêu:** nhóm chính 3; chính K23; phụ K29. **Mức:** nền tảng. **Ngộ nhận:** Bản ghi phiên bản tự thắng trình thông dịch thực sự được gọi.

**Đọc lại:** G2 venv,.python-version; L§5; T§4 tự làm1; G2 .python-version; L§5 tạo venv (ngữ cảnh).

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-054 — A

Chính sách áp dụng công cụ AI, không chỉ giao diện chatbot; đề đã nêu đây là trợ lý AI. Cấm ở chế độ đóng không phụ thuộc số từ được nhận.

- **B sai:** Phạm vi công cụ có cả trợ lý lập trình.
- **C sai:** Nguồn không có ngưỡng số từ miễn áp dụng chế độ đóng.
- **D sai:** Khai báo không cấp quyền sử dụng trong bài đóng.

**Mục tiêu:** nhóm chính 4; chính K35. **Mức:** vận dụng. **Ngộ nhận:** Không phải chatbot hoặc chỉ vài từ nên tưởng không tính là dùng AI.

**Đọc lại:** G3 hai chế độ; L§3 khai báo (ngữ cảnh); T§1 cách làm việc ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-055 — D

Nguồn nhắc AI có thể đề xuất cú pháp không có ở phiên bản đang dùng. Kiểm tài liệu và kết quả theo mục tiêu là hai phần cần thiết; không lấy sự tự tin thay bằng chứng.

- **A sai:** Tên hợp lý và tự tin không chứng minh hàm tồn tại hay đúng nghĩa.
- **B sai:** Hai gợi ý vẫn chưa là đối chiếu nguồn chính thức.
- **C sai:** Bỏ chuẩn tự tính làm yếu phép đối chiếu; chạy hết chưa đủ đúng câu hỏi.

**Mục tiêu:** nhóm chính 5; chính K49; phụ K48. **Mức:** vận dụng. **Ngộ nhận:** Hàm nghe hợp lý hoặc AI xác nhận nên bỏ đọc docs và mẫu có chuẩn.

**Đọc lại:** G mục AI hay sai/kiểm chứng; L§4 đọc hiểu; T§3 bước2–3; G3 tự phác/hỏi; L§4 bài 2; T§3 bước1–3.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-056 — A

Thiếu nhãn là điều kiện chưa rõ. Hỗ trợ ngôn ngữ/nội dung cũng thuộc phạm vi AI, không được tự miễn vì chỉ viết nháp hoặc không phải code.

- **B sai:** Chính sách có công cụ hỗ trợ viết, không chỉ code.
- **C sai:** Địa điểm và mức sửa không thay yêu cầu hỏi khi thiếu nhãn.
- **D sai:** Viết lại không xóa việc đã dùng, khai như vậy không trung thực.

**Mục tiêu:** nhóm chính 4; chính K36; phụ K43. **Mức:** vận dụng. **Ngộ nhận:** Chỉ hỗ trợ lời văn ở nhà nên tự coi là mở và không phải khai báo.

**Đọc lại:** G3 hai chế độ; L§5 nhãn mở; T§4 nhãn mở; G3 khai báo dùng gì/việc gì; T§3 mẫu khai báo (ngữ cảnh);P§1,§3 ; P§2–5.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-057

Run all phiên cũ in 5 vì còn dem=4; sau restart A gặp NameError nên lượt từ đầu dừng trước B. Thêm khởi tạo rõ trước A, ví dụ `dem=0` cho lượt sạch in 1, hoặc `dem=4` nếu muốn khôi phục giá trị xuất phát cũ để in 5.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Lượt cũ in 5 | 0,5 |
| Lượt sạch NameError ở A, không dùng kết quả cũ | 0,75 |
| Khởi tạo rõ trước A và kết quả sạch khớp giá trị chọn (ví dụ0→1 hoặc4→5) | 0,75 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 2; chính K15; phụ K13. **Mức:** vận dụng. **Ngộ nhận:** Run all đã qua nên chắc chắn không có phụ thuộc trạng thái còn sót.

**Đọc lại:** L§1 state; T§1 bước3; T§1 bước2.

**Kiểm chứng:** đã thực thi các đoạn Python theo lịch cell, gồm lỗi dự kiến; kiểm output/trạng thái và mô phỏng biểu thức cuối. Chưa chạy giao diện Colab.

### B1-058

a) Đã dùng bản ghi thư viện, nhưng venv nền3.11.9 chưa khớp Python 3.12.3; chạy được không tự chứng minh khớp môi trường đã kiểm thử. b) Tạo một venv mới bằng executable đúng, kích hoạt, cài requirements rồi chạy theo README:

```bash
python3.12 -m venv .venv312
source .venv312/bin/activate
python -m pip install -r requirements.txt
```

.python-version là bản ghi chứ không tự sửa venv đã tạo sai nền.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: ghi nhận cài thư viện đúng và chỉ ra Python nền sai | 1 |
| b: đúng Python tạo venv mới (0,5); kích hoạt/cài và chạy theo README (0,5) | 1 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 3; chính K31; phụ K28, K29. **Mức:** phân loại. **Ngộ nhận:** Đã cài requirements và code chạy nên tưởng đủ mọi điều kiện chạy lại.

**Đọc lại:** G2 .python-version; L§5; T§4 tự làm1; G2 requirements; L§5 tạo venv (ngữ cảnh).

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-059

a) Không: các giá biết 20,40 phải có trung bình30; thay hai ô chưa biết bằng 0 tạo giá giả và đổi mẫu số thành 4 nên ra15. b) Dùng chính mẫu có thiếu này, tự tính(20+40)/2=30 để đối chiếu; ca không có ô thiếu không kiểm được quy ước xử lý thiếu và không chứng minh code đúng mọi dữ liệu.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| a: bác bỏ15, nêu30 và sai quy ước/mẫu số | 1 |
| b: phép kiểm độc lập có chuẩn30 (0,5); giới hạn ca thử trước (0,5) | 1 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 5; chính K52; phụ K53, K50. **Mức:** phân loại. **Ngộ nhận:** Thiếu tự là 0; code không lỗi và một ca đơn giản qua nên mọi trường hợp đúng.

**Đọc lại:** G3 quy ước mean; L§4 kiểm chứng (ngữ cảnh); T§3 kiểm chứng (áp dụng); G3 kiểm chứng; L§4 bài 1–2; T§3 bước4 (giới hạn kiểm); G kiểm chứng; L§4 bài 2; T§3 bước4.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### B1-060

Mỗi tuần có 3 tiết lý thuyết kèm notebook và 3 tiết lab với giảng viên thực hành; nộp lab qua GitHub Classroom, xem thông báo/hỏi đáp/phân công thành phố trên Canvas. Trước Bài 2 cần chạy notebook Bài 1, đọc Chính sách AI và bắt đầu tìm nhóm 4–5 người. Cài local Python 3.12+ và VS Code (Python/Jupyter extensions nếu làm notebook local) là khuyến nghị làm sớm, không bắt buộc ngay: G đặt trong việc trước Bài 2, lecture nói nên trước Bài 3; nếu mắc bước lab quá3 phút, hỏi giảng viên thực hành theo hướng dẫn lab.

**Ý bắt buộc và hướng dẫn chấm — 2 điểm**

| Ý cần đạt | Điểm |
|---|---:|
| Vai trò LT/lab, Classroom và Canvas đúng | 0,75 |
| Notebook, policy, tìm nhóm 4–5 đúng | 0,75 |
| Cài local khuyến nghị và giữ rõ hai mốc nguồn, không tự buộc hoàn thành ngay | 0,5 |

Chấp nhận cách đúng tương đương; không yêu cầu viết dài hơn giới hạn nêu trong đề.

**Mục tiêu:** nhóm chính 6; chính K59; phụ K60. **Mức:** vận dụng. **Ngộ nhận:** Nhầm kênh nộp/thông báo hoặc biến khuyến nghị cài sớm thành hạn bắt buộc.

**Đọc lại:** G4 mỗi tuần/BTL; L§4 thực hành lớp; T§1 cách làm việc; G4 việc trước bài 2; L§5 và cuối notebook; T§4 và cuối notebook.

**Kiểm chứng:** đã đối chiếu quy tắc và tự giải theo nguồn; các lệnh shell/tình huống môi trường nếu có chưa được chạy trên đúng OS/phiên bản giả định.

### Cập nhật bao phủ sau đợt 6

Lũy kế 60/60: 40 TN, 20 TL.

| Nhóm | Đã xuất / kế hoạch |
|---|---:|
| 1 | 8 / 8 |
| 2 | 10 / 10 |
| 3 | 14 / 14 |
| 4 | 14 / 14 |
| 5 | 8 / 8 |
| 6 | 6 / 6 |

Đã có câu yêu cầu sử dụng: K01, K02, K03, K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K26, K27, K28, K29, K30, K31, K32, K33, K34, K35, K36, K37, K38, K39, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61.
Mục chưa có câu: không còn.
Mục rộng còn nhánh/biến thể được bố trí ở đợt sau: không còn. Không tính việc chỉ nhắc trong lời giải là bao phủ.

## Đối chiếu cuối cùng

Đủ 60 mã liên tục,40 trắc nghiệm và 20 tự luận; đúng 15 nền tảng,33 vận dụng,12 phân loại. Mỗi câu chỉ tính vào một nhóm chính, nhiều nhất hai mục tiêu phụ. Đáp án A/B/C/D mỗi chữ đúng 10 lần, không theo chu kỳ cố định.61 mục đều có câu hỏi đòi hỏi sử dụng, tra bảng danh mục ở đầu tệp.

### Hoàn tất các nhánh dễ bỏ sót

| Nhánh | Câu thực sự kiểm tra |
|---|---|
| Markdown/code/Shift+Enter; print và biểu thức cuối | 002,022 |
| Lịch chạy, cell chưa thực thi, sửa/xóa, cộng dồn/khởi tạo | 012,028,032,052,057 |
| Restart đối chiếu với file/output lưu, Run all phiên cũ | 008,028,047,057 |
| OS/shell, Python nền, kích hoạt và cwd, pip theo môi trường | 003,013,019,025,043,053,058 |
| Phụ thuộc freeze, requirements và .python-version, README/venv copy | 015,019,023,035,038,058 |
| Chế độ đóng có quiz, giữa kỳ, vấn đáp; mở không miễn nghĩa vụ | 006,014,017,034,039,048,054 |
| Thiếu nhãn, hỗ trợ dịch/viết, khai không dùng, sửa gần hết | 004,009,016,029,040,044,056 |
|0 điểm phần không giải thích được của cá nhân, không tự lan cả nhóm | 020 |
| Đơn vị tỷ lệ/phần trăm, tổng 100 chưa đủ, assert có phạm vi | 026,040,049 |
| mean bỏ thiếu và không tự coi thiếu bằng 0 | 011,018,041,059 |
| Git/private/commit, thành phố, QA–KPI–LLM, testrepo và vấn đáp | 010,027,037 |
|10/10/20/60, giai đoạn bài 9/15, thời lượng khác, LT/lab/Canvas/Classroom, chuẩn bị | 017,046,060 |
| Xem trước biểu đồ/groupby/Secrets ở mức ý nghĩa | 050 |

### Bẫy trọng tâm và nhiều cách hỏi

| Ngộ nhận | Câu/biến thể |
|---|---|
| Đã khai báo nên được dùng AI khi vấn đáp | 006 xin gợi ý trong viva;039 khai sau quiz không cấp quyền;020 khai không miễn hiểu |
| Sửa gần hết nên không khai | 004 bản nháp đã viết lại;009 đã khai nhưng vẫn thiếu hiểu/kiểm |
| AI sai nên người nộp miễn trách nhiệm | 024 sai cột dù minh bạch;009 nhận diện nghĩa vụ còn thiếu;039 phân loại bài sai |
| Làm ở nhà/thiếu nhãn tự mở | 016 code nháp bài nhỏ;056 nháp lời văn;048 đọc nhãn từng phần |
| Hỏi ít không tính dùng AI | 014 gợi ý quiz;054 vài từ trợ lý lập trình;048 đối chiếu khuyến nghị với quiz đóng |
| .python-version tự đổi Python | 003 lệnh python cũ;053 gọi đích danh executable khác tệp;058 dựng lại |
| requirements đã ghi cả Python | 023 thiếu bản ghi;003 không tự đổi interpreter;058 đúng gói vẫn sai Python nền |
| Chuyển cwd tự đổi pip | 013 chọn đích cài qua executable;019 ghi freeze nhầm;043 hai shell cùng cwd |
| Tải .ipynb có cả thư viện/trạng thái | 033 import thiếu dù có output;037 output không thay repo chạy;047 output lưu không tạo biến |
| Cell phía trên chắc đã chạy | 012 chạy B trước A;008 thiếu định nghĩa ở phiên sạch |
| Xóa cell tự hoàn tác | 028 xóa định nghĩa rồi restart;057 cell khởi tạo mất;052 sửa chưa chạy |
| Không lỗi là đúng | 008 kiểm số tiền;041 biểu đồ rõ nhưng xử lý sai;059 ca không thiếu không chứng minh xử lý thiếu |
| Run all phiên cũ đủ chứng minh sạch | 008 phép tính dùng biến cũ;057 tăng bộ đếm thiếu khởi tạo |
| Tổng 100 bảo đảm từng nhóm | 026 A/B bị đổi;049 assert A và tổng qua nhưng B/C sai |
| Thiếu có thể tự thay0 | 011 bảng thô;018 mean giá đã biết;041 xóa/sửa không có quy ước;059 phản ví dụ cụ thể |

### Rà trùng, phạm vi và ưu tiên

Các câu cùng cơ chế được giữ ở dạng khác nhau: chọn nhận định, theo dõi lịch, sửa quy trình hoặc nêu giới hạn bằng chứng; không chỉ đổi tên và số. Ví dụ013 gọi Python đích danh,019 chụp nhầm môi trường,043 so hai terminal;012 chạy đảo thứ tự,028 xóa cell,032 tái khởi tạo,052 sửa chưa chạy. Không có cặp được thiết kế chỉ khác đúng một chi tiết; không thêm vượt 60 để lấp khoảng trống.

Câu 2 của giữa kỳ mẫu và các câu môi trường/AI trong các đề hỗ trợ định hướng trọng tâm, không chứng minh tần suất hay mức khó thực nghiệm của đề thi thật. Không sao chép các phương án tương đương cùng đúng từ đề mẫu. Không yêu cầu kỹ thuật pandas/matplotlib/groupby/API của các bài sau hoặc lệnh Git nâng cao.
