"""Place method-specific teaching and measured output beside unchanged Python fences."""
from pathlib import Path
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from tempfile import TemporaryDirectory
from unittest.mock import patch
import argparse
import builtins
import importlib.util
import math
import os
import re

ROOT = Path(__file__).resolve().parents[1]
LABS = ROOT / "raw_materials/xu-ly-du-lieu/labs"
FENCE = re.compile(r"^```python[^\n]*\n(.*?)^```[ \t]*$", re.M | re.S)

# Each pair describes the actual operations of the two methods, not a style score.
NOTES = {
"08": [
("`to_datetime` đọc hai cột theo đúng `%d/%m/%Y`. `errors=\"coerce\"` đổi chuỗi sai lịch hoặc ô thiếu thành `NaT`. Lấy ngày ra trừ ngày vào tạo `Timedelta`, rồi `.dt.days` lấy số ngày nguyên. Dòng có một ngày không hợp lệ nhận kết quả thiếu, không được biến thành 0 đêm.", "`DataFrame.apply` mặc định chuyển từng cột vào hàm. Hai cột vì thế dùng cùng `format` và quy tắc lỗi trong một chỗ cấu hình. `.sub()` là phép trừ hai Series theo chỉ mục, sau đó `.dt.days` lấy số ngày. Cách này vẫn giữ định dạng bắt buộc, không thay bằng phỏng đoán `dayfirst`."),
("`notna()` kiểm tra chuỗi ngày có tồn tại trong dữ liệu gốc. `isna()` kiểm tra kết quả chuyển đổi bị thiếu. Kết hợp hai mặt nạ bằng `&` chỉ giữ trường hợp có đầu vào nhưng không đọc được ngày. Ô vốn đã thiếu không bị gán thành lỗi nhập ngày.", "Tách hai điều kiện thành những Series boolean có cùng chỉ mục giúp đọc rõ vai trò của mỗi vế. Phép kết hợp theo nhãn giữ kết quả ứng với đúng dòng ban đầu. Cần nhận Series ngày được tạo từ chính cột đang kiểm, tránh đưa một cột chuyển đổi có chỉ mục khác vào phép so sánh."),
("Đọc và kiểm ngày trước khi so sánh với mốc snapshot. Giữ các hàng không sau mốc, rồi `set_index` đưa ngày vào chỉ mục và `sort_index` sắp theo thời gian. Trả cả số dòng bị gắn cờ để người đọc biết phạm vi thay đổi. Việc lọc không chứng minh các dòng sau mốc chắc chắn là dữ liệu giả.", "Tách phần chuẩn bị ngày khỏi mặt nạ lọc giúp theo dõi từng bước trong chuỗi phương thức. `.loc` chọn các dòng thỏa điều kiện, còn `.copy()` làm rõ rằng bảng kết quả sẽ được xử lý riêng. Chỉ mục thời gian đã sắp là tiền đề để các bài sau cắt lát theo năm và tổng hợp theo lịch."),
("Với `DatetimeIndex`, `.loc[str(nam)]` chọn các nhãn thuộc năm đó, không phải chọn một vị trí dòng. `len` đếm số đánh giá trong lát cắt. Cần xử lý năm không có trong dữ liệu theo đúng đầu ra của đề, thay vì giả định năm nào cũng xuất hiện.", "So sánh thuộc tính `.index.year` với năm cần tìm tạo mặt nạ cùng độ dài bảng. Tổng các giá trị True hoặc số dòng sau lọc cho cùng số đánh giá. Cách viết này thể hiện trực tiếp điều kiện năm và thuận tiện khi muốn kết hợp thêm điều kiện theo tháng hoặc loại chỗ ở."),
("`resample` chia chỉ mục ngày thành các quý dương lịch, `.size()` đếm dòng trong từng quý. Quý chưa kết thúc tại mốc quan sát phải được nhận diện bằng ngày cuối kỳ. Đề có bước bỏ kỳ cuối trong dữ liệu đã cho, nhưng không được suy ra rằng kỳ cuối của mọi tập dữ liệu đều thiếu.", "Chuẩn hóa nhãn kỳ giúp so sánh mốc kết thúc quý với snapshot một cách tường minh. Sau khi tổng hợp, chỉ chọn những kỳ đáp ứng điều kiện đầy đủ. Cần giữ phân biệt giữa nhãn ngày cuối quý và ngày đánh giá cuối cùng xuất hiện trong quý, vì ngày cuối có sự kiện không xác định độ phủ dữ liệu."),
("So sánh nhãn ngày kết thúc quý với mốc được phép báo cáo. Mặt nạ lọc trả lại đúng các quý đã kết thúc, giữ nhãn và số đếm. Khi mốc nằm đúng ngày cuối quý, phải đọc rõ quy ước về hết ngày đó, không tự loại thêm một quý.", "Đưa mốc về `Timestamp` rồi dùng phép chọn theo chỉ mục giúp điều kiện thời gian không phụ thuộc vị trí cuối của Series. Cách này vẫn đúng khi dữ liệu có nhiều kỳ sau mốc. Hai cách đều cần cùng quy ước gồm hay không gồm ngày biên để kết quả đối chiếu có ý nghĩa."),
("Cắt giai đoạn cần so sánh trước khi tìm cực trị. `idxmax` và `idxmin` trả nhãn quý, còn `max` và `min` trả số đếm. Khi có nhiều quý cùng giá trị, các hàm tìm nhãn trả lần xuất hiện đầu, nên cần nêu quy tắc này trong báo cáo.", "Việc gom nhãn và giá trị vào một dict giữ kết quả có tên trường rõ ràng. Đừng tìm cực trị trên toàn lịch sử rồi mới kiểm xem nhãn có thuộc giai đoạn được hỏi hay không. Dữ liệu rỗng sau khi giới hạn kỳ cần được nhận diện trước khi gọi hàm tìm cực trị."),
("Tạo lịch ngày đầy đủ bằng `date_range`, đếm số đánh giá rồi `reindex` về lịch đó. `fill_value=0` ở đây có nghĩa là không có sự kiện trong log đã được quan sát, không phải cách điền tùy ý cho một phép đo bị thiếu. Ngày nhuận được lịch của pandas tính theo năm được chọn.", "Tổng hợp theo ngày rồi căn về cùng lịch cho phép so sánh các năm theo cùng định nghĩa. Giữ chỉ mục ngày liên tục là điều kiện để cửa sổ bảy dòng ở bài sau tương ứng với bảy ngày. Không dùng số ngày có sự kiện làm mẫu số khi câu hỏi hỏi trung bình trên mọi ngày trong năm."),
("`rolling(cua_so)` dùng số dòng, còn `mean()` tính trung bình trong mỗi cửa sổ. Trên lịch ngày liên tục ở bài trước, bảy dòng tương ứng bảy ngày. `min_periods` quy định cần bao nhiêu quan sát trước khi có kết quả, nên phần đầu chuỗi có thể là NaN.", "Tách chuỗi làm mượt và thao tác tìm đỉnh giúp đối chiếu cả nhãn ngày lẫn giá trị. Nếu chỉ mục có khoảng trống, cần lập lại lịch hoặc cân nhắc cửa sổ thời gian như `\"7D\"` với quy tắc biên rõ ràng. Đừng thay một cửa sổ bảy dòng bằng bảy ngày mà không kiểm cấu trúc chỉ mục."),
("Cùng kỳ theo quý nghĩa là so với quý cách bốn kỳ, không phải quý ngay trước. `pct_change(4)` trả mức thay đổi trên thang 0–1, cần nhân 100 khi trình bày phần trăm. Bốn kỳ đầu chưa có kỳ đối chiếu, nên kết quả thiếu là hợp lý.", "Tách giá trị hiện tại và giá trị dịch bốn kỳ bằng `shift(4)` làm rõ tử số và mẫu số. Phải dùng cùng lịch quý đầy đủ để bốn vị trí thực sự là một năm. Mẫu số bằng 0 không cho một tỷ lệ hữu hạn và cần được báo riêng thay vì diễn giải như tăng trưởng bình thường."),
("So sánh với kỳ trước và cùng kỳ là hai câu hỏi khác nhau. `shift(1)` lấy kỳ liền trước, còn dịch 12 tháng lấy cùng tháng năm trước nếu Series có lịch tháng liên tục. Giữ rõ mốc cần đọc trong kết quả, không lấy phần tử cuối theo vị trí nếu đề chỉ định một tháng cụ thể.", "Đóng gói các phép so sánh thành dict giúp báo cáo mang tên đại lượng rõ ràng. Kiểm tra sự tồn tại của kỳ gốc và giá trị mẫu số trước khi chia. Kết quả cho tháng hiện tại chỉ được báo như kết quả cả tháng khi phạm vi quan sát của tháng đó đã đầy đủ."),
("Tháng 1 và tháng 2 không có cùng số ngày. Chia số đánh giá từng tháng cho số ngày lịch của chính tháng đó tạo tốc độ đánh giá trên một ngày. Thuộc tính `days_in_month` giữ đúng tháng 2 của năm nhuận, tránh viết cứng 28 ngày.", "Tính cả tỷ lệ theo tổng tháng lẫn tỷ lệ theo số đánh giá mỗi ngày giúp thấy ảnh hưởng của độ dài tháng. Chúng có thể khác nhau mà không mâu thuẫn. Chỉ dùng số ngày lịch cho một tháng đã quan sát đủ, nếu dữ liệu kết thúc giữa tháng cần mẫu số là phạm vi quan sát tương ứng."),
("Đếm đánh giá theo từng ngày rồi tìm ngày có số đếm cao nhất. Nhãn ngày kỷ lục và số dòng của ngày đó là hai phần khác nhau của kết quả. Việc kiểm lại các bản ghi gốc giúp nhận biết một cụm nhập dữ liệu hoặc trùng khóa, không tự giải thích đó là ngày nhiều khách nhất.", "Gom các dấu kiểm vào một báo cáo giúp giữ lại số dòng, ngày và các thông tin đối chiếu. Tìm các chỗ ở hoặc bản ghi tạo nên đỉnh trước khi nêu một lời giải thích. Mỗi đánh giá là một sự kiện trong nguồn, không đồng nhất với một lần đặt phòng trong cùng ngày."),
("Đọc `last_review` thành ngày rồi lấy snapshot trừ ngày đánh giá cuối. `.dt.days` cho số ngày đã trôi qua, còn chỗ ở chưa có ngày đánh giá giữ NaN. Khoảng thời gian dài không có đánh giá là một dấu hiệu cần khảo sát, không đủ chứng minh chỗ ở đã ngừng hoạt động.", "Tạo các mặt nạ riêng cho ngày thiếu, ngày sau snapshot và ngày đã cũ giúp báo cáo phân biệt ba tình huống. Không gom mọi kết quả âm hoặc thiếu vào nhóm ngừng hoạt động. Quy tắc gắn cờ phải nêu rõ ngưỡng ngày và chỉ được dùng trong phạm vi nguồn đang xét."),
],
"10": [
("Tạo bản sao của cột trước khi gán để giữ dữ liệu gốc. Mặt nạ chỉ chọn chỗ ở có số đánh giá bằng 0 và tốc độ đánh giá đang thiếu. Điền 0 ở đúng các dòng đó theo giả thiết của bài, không lan sang dòng đã có đánh giá hoặc mọi cột giá trị thiếu.", "`mask` thay giá trị ở nơi điều kiện là True và giữ các vị trí còn lại. Điều kiện được tính theo cùng chỉ mục của bảng. Cách viết tập trung quy tắc thay thế vào một biểu thức, nhưng vẫn cần giải thích vì sao giá trị 0 có ý nghĩa cho đúng nhóm dòng đang xét."),
("Duyệt từng nhóm loại phòng, tính trung vị từ những giá đã có rồi chỉ điền vào ô thiếu trong nhóm. Giữ lại cả dấu kiểm giá vốn đã thiếu để phân biệt số quan sát với số đã ước lượng. Nhóm không có một giá hợp lệ không thể tự cung cấp trung vị.", "`groupby(...).transform(\"median\")` trả một trung vị tương ứng với từng dòng nguồn. `fillna` hoặc mặt nạ sau đó chỉ thay ô thiếu, giữ giá đã quan sát. `transform` có cùng chỉ mục với bảng, thuận tiện hơn việc ghép một bảng tổng hợp nhỏ trở lại từng dòng."),
("Xây từng cờ kiểm theo điều kiện giá thiếu, không dương hoặc vượt ngưỡng. Các cờ có thể chồng nhau, nên tổng số cờ không nhất thiết bằng số dòng lỗi phân biệt. Trả bảng cờ giữ chỉ mục để có thể đối chiếu chính xác bản ghi gốc.", "Biểu thức boolean theo cột thể hiện cùng bộ quy tắc cho toàn bảng. Tên cột cờ nên mô tả điều đã kiểm, thay vì gọi mọi dòng là chắc chắn sai. Ngưỡng là lựa chọn kiểm tra cần ghi lại, không phải bằng chứng tự động rằng giá cao phải bị xóa."),
("Tính P99 từ phần giá hợp lệ trước khi đếm dòng vượt ngưỡng. Tạo hai kết quả riêng cho bỏ hàng và chặn giá vì chúng thay đổi dữ liệu theo hai cách khác nhau. Giữ ngưỡng cùng số dòng bị tác động để người đọc đánh giá mức thay đổi.", "`clip(upper=nguong)` thay giá vượt ngưỡng bằng ngưỡng mà giữ số dòng. Lọc bằng mặt nạ lại làm giảm cỡ mẫu. Hai kết quả không thể xem là cùng một dữ liệu sau làm sạch, và không có quy tắc thống kê nào tự cho phép chặn mọi giá cao trong mọi bài toán."),
("`duplicated` tìm các dòng trùng theo những cột đã chọn, còn `drop_duplicates` thực hiện một quyết định loại dòng. Có mã review phân biệt thì có thể kiểm bản nhập lặp theo mã đó. Chỉ có `listing_id` và ngày chưa đủ phân biệt hai người cùng đánh giá trong một ngày.", "Tách phép đếm trùng khỏi phép loại dòng để báo cáo được cả hiện tượng lẫn quyết định. `keep=False` đánh dấu mọi thành viên của nhóm trùng, còn `keep=\"first\"` giữ một dòng đại diện. Kết quả phải ghi rõ đang đếm dòng tham gia nhóm hay số dòng vượt quá một đại diện."),
("Chuyển mốc so sánh thành `Timestamp`, rồi tính ngày nhỏ nhất, lớn nhất và số ngày vượt mốc. Phép `>` không gồm chính ngày mốc theo yêu cầu. Trả ba chỉ số có tên để không nhầm số dòng sau mốc với độ dài khoảng thời gian.", "Các phép tổng hợp trên Series ngày tránh duyệt từng dòng trong Python. Cột ngày phải được đọc đúng trước khi gọi hàm. Ngày vượt mốc cần gắn cờ để đối chiếu phạm vi thu thập, không được tự suy ra nguyên nhân hoặc lặng lẽ sửa ngày."),
("`isin(ds[\"id\"])` kiểm tra mã chỗ ở của từng dòng đánh giá có trong bảng danh mục hay không. Đảo mặt nạ bằng `~` rồi cộng boolean đếm số dòng không khớp. Một mã không khớp lặp ba lần vẫn tạo ba dòng được đếm.", "Phép ghép có chỉ báo hoặc đối chiếu tập khóa làm rõ phía nào thiếu bản ghi. Phải giữ đơn vị đếm là dòng đánh giá, không đổi thành số mã khác nhau nếu đề không yêu cầu. Các khóa thiếu cũng cần được hiểu theo quy tắc của bài trước khi gọi kết quả là toàn vẹn."),
("`duplicated` với hai cột mã chỗ ở và ngày xác định các cặp giống nhau. Chọn `keep=False` khi đếm mọi dòng tham gia cặp lặp. Đó là phép kiểm khóa tự nhiên được đề xuất, chưa phải bằng chứng tất cả những đánh giá đó là bản sao.", "Nhóm theo cặp khóa rồi đếm kích thước giúp xem phân bố các nhóm lặp. Tổng kích thước nhóm lớn hơn một khác với tổng số dòng dư sau khi giữ một đại diện. Giữ đúng định nghĩa cần trả và kiểm cả một cặp xuất hiện ba lần để thấy sự khác nhau."),
("Đếm review theo mã chỗ ở rồi `reindex` theo thứ tự ID của bảng danh mục. Điền 0 cho ID không xuất hiện trong log vì đang đếm số sự kiện của bảng đã cung cấp. So sánh với cột tính sẵn cho biết hai nguồn đếm có khớp trên cùng phạm vi hay không.", "Ghép bảng đếm theo ID rồi căn lại chỉ mục giữ cho kết quả đi cùng từng dòng danh mục. Khóa bảng tra cần đủ tính duy nhất để phép ghép không nhân bản dòng. Dấu lệch chưa chứng minh một trong hai bảng sai, vì chúng có thể dùng phạm vi thời gian hoặc tiêu chí giữ review khác nhau."),
("Lọc ngày theo cận dưới gồm chính ngày bắt đầu. Nếu có cận trên, áp dụng thêm điều kiện gồm ngày kết thúc. Đếm theo ID rồi căn về bảng danh mục, sau đó lấy số tính sẵn trừ số vừa đếm. Để `ket_thuc=None` có nghĩa không chặn trên, đúng như yêu cầu biến thể này.", "Tách mặt nạ thời gian, bảng đếm và phép đối chiếu giúp kiểm lại từng giả thiết về 12 tháng. Xem cả phân bố độ lệch, không chỉ đếm số dòng khác 0. Nếu thay cận trên bằng snapshot, phải tính lại và ghi đó là một định nghĩa cửa sổ khác."),
("Dựng từng bản ghi báo cáo theo thứ tự khóa của dict số dòng. Quy tắc có số dòng bằng 0 vẫn phải xuất hiện để phân biệt đã kiểm và không kiểm. `to_csv(index=False)` bỏ chỉ mục phụ, rồi đọc lại tệp để xác nhận cấu trúc xuất ra.", "Tạo DataFrame trực tiếp từ dữ liệu có cấu trúc giảm bước ghép từng dòng. `ghi_chu.get(..., \"\")` cho ghi chú rỗng khi chưa có nội dung, không làm mất quy tắc. `keep_default_na=False` khi đọc lại giữ chuỗi rỗng thay vì đổi thành NaN."),
("Nhóm các bản ghi có cùng khóa rồi xem số mức giá phân biệt. Những nhóm có nhiều giá phải được giữ riêng để đối chiếu, không chọn tùy ý dòng đầu rồi gọi là làm sạch. Các dòng không mâu thuẫn có thể chuyển sang bước gộp theo đúng quy tắc đã nêu.", "`nunique` và `transform` tạo cờ mâu thuẫn tương ứng từng dòng. Phép chọn bằng cờ giữ cả nhóm để kiểm tra nguồn, ngày hoặc đơn vị. Cần thống nhất cách xử lý giá thiếu khi đếm mức giá, vì một ô thiếu không tự mang một mức giá mới."),
("Mốt, giá trước đó và nội suy dùng những giả thiết khác nhau. Mốt dựa vào giá trị xuất hiện nhiều trong một nhóm, forward fill dùng quan sát trước, còn nội suy dùng vị trí giữa các mốc đã có. Kiểm thứ tự thời gian và ranh giới từng nhóm trước khi điền.", "Các phương thức theo nhóm và chỉ mục giúp áp dụng quy tắc nhất quán. Không để forward fill chảy từ chỗ ở này sang chỗ ở khác hoặc dùng dữ liệu tương lai trong bài toán dự báo. Nội suy ở giữa hai mốc có căn cứ khác với ngoại suy ra đầu hoặc cuối chuỗi."),
],
"11": [
("Lọc dòng có văn bản, thay đúng thẻ xuống dòng được quy định rồi kiểm độ dài. `sample` dùng `random_state` để chọn lại cùng mẫu khi dữ liệu và phiên bản giữ nguyên. Kết quả chỉ đại diện cho miền văn bản qua bộ lọc, không tự đại diện cho mọi review.", "Kiểm số dòng đủ điều kiện trước khi lấy mẫu giúp báo lỗi có nghĩa thay vì âm thầm giảm cỡ mẫu. `.copy()` giữ vùng dữ liệu dùng để chuẩn hóa riêng. Ngưỡng độ dài có thể loại các nhận xét ngắn nhưng rõ ý, nên phải ghi bộ lọc khi báo chất lượng mô hình."),
("Đếm độ dài văn bản rồi dùng quy tắc ước lượng token của đề. Nhân tổng token với đơn giá giả định cho chi phí ước tính, không phải số tiền đã thanh toán. Ước lượng này chưa thay thế tokenizer hay hóa đơn của nhà cung cấp.", "Tính theo Series làm rõ tổng ký tự và số bản ghi thay vì tích lũy thủ công. Tham số đơn giá cần giữ đơn vị trên một triệu token và thang tiền tệ đã nêu. Nếu thêm token đầu ra hoặc lời nhắc dùng chung, phải đưa chúng vào một giả thiết mới và báo riêng."),
("Lược đồ định nghĩa các trường bắt buộc cùng miền nhãn cho cảm xúc, khía cạnh và ngôn ngữ. Kiểm từng trường giúp thấy phản hồi bị loại vì thiếu dữ liệu, sai kiểu hay nhãn ngoài danh mục. Một phản hồi qua lược đồ vẫn có thể gán cảm xúc sai so với văn bản.", "Pydantic gom quy tắc cấu trúc vào một mô hình có thể dùng lại. `Literal` giới hạn các nhãn được chấp nhận, còn cấu hình trường thừa và chế độ kiểm kiểu phải được đọc cùng nhau. Ngoại lệ kiểm tra cho biết quy tắc nào không khớp, không chứng minh mô hình đã đọc đúng ý nghĩa câu."),
("Duyệt từng ID, giữ phản hồi hợp lệ và ghi riêng ID lỗi cấu trúc. Không để một phản hồi lỗi làm mất toàn bộ đợt đánh giá. Dữ liệu gốc cần được giữ để đọc lại nguyên nhân, thay vì chỉ giữ một tổng số lỗi.", "Báo cáo kiểm tra có thể giữ ID, trạng thái và thông tin lỗi cho mỗi phản hồi. Việc tách phần hợp lệ khỏi phần bị loại giúp tính đúng mẫu số ở bước sau. Không gọi tỷ lệ hợp lệ là độ chính xác cảm xúc, vì đây là hai phép đo khác nhau."),
("Đối chiếu nhãn dự đoán với nhãn tay trên các ID cùng tồn tại. Đếm số khớp và số được đánh giá trước khi chia. Báo cả tỷ lệ trong tập hợp lệ lẫn tỷ lệ trên toàn mẫu khi đề yêu cầu, không che các phản hồi lỗi cấu trúc bằng cách bỏ chúng khỏi mẫu số mà không nói rõ.", "Đưa nhãn dự đoán và tham chiếu thành hai cột giúp nhìn trực tiếp các ID không khớp. Phải căn theo ID, không ghép theo vị trí vì thứ tự hai dict hoặc hai bảng có thể khác. Nhãn tay cũng cần quy tắc gán nhất quán, nên đây là độ khớp với bộ tham chiếu đã cho."),
("Đọc nguyên văn các trường hợp không khớp trước khi đặt tên lỗi. Câu có cả khen và chê, phủ định hoặc khác biệt cách hiểu cần được mô tả bằng bằng chứng ngôn ngữ. Không suy ra nguyên nhân bên trong mô hình chỉ từ một nhãn sai.", "Các từ khóa có thể gợi ý một loại lỗi để người đọc xem lại, nhưng không tự phân loại ngữ nghĩa đầy đủ. Bảng đối chiếu giữ văn bản, nhãn dự đoán, nhãn tay và ghi chú làm bằng chứng. Khi sửa hướng dẫn gán nhãn, kiểm lại trên dữ liệu khác thay vì chỉ tối ưu cho vài câu đã thấy."),
("Kiểm những cặp nhãn có vẻ mâu thuẫn theo quy tắc đã định, chẳng hạn cảm xúc tích cực đi cùng khía cạnh chê. Danh sách ID gắn cờ là hàng đợi đọc lại, không phải toàn bộ các lỗi. Một câu có cảm xúc hỗn hợp hoặc nhận xét nhiều mặt có thể làm quy tắc đơn giản báo nhầm.", "Tách hàm kiểm từng phản hồi khỏi thao tác lọc cả đợt giúp dùng lại cùng điều kiện. Quy tắc hậu kiểm không thay thế nhãn tham chiếu. Cần đo cả trường hợp bị gắn cờ đúng, gắn cờ nhầm và lỗi không bị gắn cờ nếu muốn đánh giá chất lượng của chính bộ kiểm."),
("Đưa cùng tập nhãn tay vào mỗi lần đánh giá để so sánh các tỷ lệ trên cùng mẫu. Giữ tỷ lệ hợp lệ, độ khớp trong tập hợp lệ và độ khớp toàn mẫu thành các trường riêng. Kết quả của đợt phản hồi mô phỏng tốt hơn không chứng minh một lời nhắc mới sẽ luôn tốt hơn trên dữ liệu thực.", "Gom các phép kiểm thành một hàm báo cáo giúp chạy lại cùng tiêu chí trên nhiều bộ phản hồi đã lưu. So sánh theo ID và giữ nguyên đầu ra thô để có thể kiểm lại. Chênh lệch hai tỷ lệ phần trăm được trình bày bằng điểm phần trăm, còn mức tăng tương đối dùng một phép chia khác."),
],
"12": [
("Lấy tập ID chỗ ở thuộc quận rồi lọc review theo `isin`. `resample(\"ME\").size()` đếm theo tháng và giữ các tháng nằm giữa hai đầu chuỗi. Bài này yêu cầu bỏ phần tử cuối theo giả thiết kỳ cuối chưa trọn. Không dùng thao tác đó cho mọi tập dữ liệu nếu chưa kiểm mốc quan sát.", "Chuỗi phương thức gắn các bước lọc, đặt chỉ mục và tổng hợp trong một biểu thức. Mã quận được xác định từ bảng chỗ ở, không lấy từ vị trí dòng của review. Cách đếm vẫn là số đánh giá, không phải lưu lượng khách hoặc doanh thu của quận."),
("Lọc ngày theo snapshot trước khi tổng hợp. So sánh mốc quan sát với ngày cuối tháng để quyết định kỳ nào đã đầy đủ. Một ngày có sự kiện cuối cùng không tự xác định thời điểm dữ liệu đã quan sát đến đâu.", "Đặt quy tắc giữ kỳ thành mặt nạ riêng giúp kiểm rõ cận thời gian. Hai cách phải cùng quy ước về ngày kết thúc, đặc biệt khi snapshot đúng ngày cuối tháng. Nếu ngày có giờ, cần xác định mốc là đầu ngày hay hết ngày thay vì so sánh ngầm theo nửa đêm."),
("`subplots` tạo Figure chứa Axes mới, rồi `plot` dùng chỉ mục tháng làm trục ngang và số đếm làm trục dọc. Ghi nhãn đơn vị và phạm vi dữ liệu để người đọc hiểu mỗi điểm. `savefig` ghi chính Figure này, tránh lưu nhầm hình đang hoạt động khác.", "Gom thiết lập nhãn, nguồn và lưu hình trong một hàm giúp tạo lại biểu đồ theo cùng quy tắc. `bbox_inches=\"tight\"` thu khung theo nội dung, còn `dpi` ảnh hưởng bản raster. Tiêu đề phải được dữ liệu hỗ trợ, không dùng câu quảng cáo để làm đường biến động có vẻ mạnh hơn."),
("Nhóm theo quận rồi tính số dòng và tỷ lệ `room_type == \"Entire home/apt\"`. Lọc `n >= min_n` sau khi tổng hợp để ngưỡng áp dụng cho quy mô quận. Tỷ lệ ở thang 0–1, nên 0,8 tương ứng 80%, không phải 0,8%.", "Tạo cột boolean rồi dùng named aggregation giúp tên `n` và `pct` đi cùng định nghĩa của chúng. Sắp tỷ lệ tăng dần là thứ tự dữ liệu cho biểu đồ thanh ngang tiếp theo. Mẫu số cần giữ đúng số dòng trong quận, kể cả khi một kiểu phòng không xuất hiện."),
("`barh` tạo một thanh cho mỗi quận theo thứ tự bảng. Nhân tỷ lệ với 100 trước khi gắn nhãn phần trăm. Trục phải bắt đầu từ 0 để độ dài thanh phản ánh tỷ lệ, còn nhãn giá trị cho phép đọc con số mà không cần đo bằng mắt.", "Thiết lập nhãn và lưu hình trong cùng hàm giữ biểu đồ tái lập. `bar_label` đặt chuỗi lên từng thanh theo đúng container trả về. Nếu nhãn sát mép, mở thêm khoảng trống trong giới hạn trục thay vì cắt chữ hoặc giảm tỷ lệ chữ quá nhỏ."),
("Bỏ ô thiếu trước khi đưa `availability_365` vào histogram. `bins` quyết định cách chia khoảng, còn tổng tần suất phải bằng số giá trị hợp lệ. Đếm riêng giá trị 0 và từ 360 trở lên theo đúng cận của đề.", "Hàm trả cả Axes và hai số đếm giúp kiểm đối chiếu hình với bảng. Hai cụm trong histogram mô tả phân bố số ngày mở lịch của dữ liệu, không tự cho biết ý định chủ nhà hoặc số ngày thực sự có khách. Phải xem cả lựa chọn khoảng chia trước khi kết luận hình có hai đỉnh."),
("Chia các giá trị theo điều kiện mở lịch đã nêu rồi đếm từng nhóm. Giữ số ô thiếu riêng để người đọc biết phần dữ liệu chưa vào phép tính. Những khoảng chọn để tóm tắt cần được ghi rõ, không được đổi ngưỡng cho phù hợp một câu chuyện có sẵn.", "Các mặt nạ theo cột giúp kiểm lại từng cận dưới và cận trên. Báo số lượng và tỷ trọng với cùng mẫu số thay vì chỉ gọi một nhóm là áp đảo. Lịch đóng có thể do đã đặt, chủ nhà khóa ngày hoặc thiếu cập nhật, nên không đồng nhất với công suất phòng."),
("Tính phần trục còn lại sau khi cắt và so với toàn thang đo. Một chênh lệch số học giữ nguyên có thể chiếm tỷ lệ chiều cao lớn hơn trên hình bị cắt. Cần nêu cả giới hạn trục và giá trị dữ liệu để người đọc đối chiếu được.", "Đóng phép tính vào hàm giúp thử các mốc cắt khác nhau mà giữ dữ liệu. Kiểm giới hạn trục hợp lệ trước khi chia. Hệ số phóng đại hình ảnh mô tả cách trình bày, không phải mức tăng tương đối thật giữa hai nhóm."),
("Vẽ lại cùng giá trị và cùng thứ tự nhóm trên trục bắt đầu từ 0. Giữ nhãn phần trăm hoặc đơn vị ban đầu để việc so sánh không đổi đại lượng. Hình sửa cần cho thấy chênh lệch thật mà không thêm kết luận về nguyên nhân.", "Tạo Figure mới rồi đặt giới hạn, nhãn và lưu tệp trong hàm giúp tránh phụ thuộc hình đã vẽ trước. So sánh chiều cao cột với Series đầu vào bằng mã. Không chỉ kiểm rằng có ảnh được xuất ra, vì một ảnh lưu thành công vẫn có thể dùng sai dữ liệu hoặc sai thang đo."),
("Đọc lại cấu trúc Axes để kiểm tiêu đề, nhãn, số đường hoặc thanh và giới hạn trục. Các `assert` kiểm những điều quan sát được trong hình, như số điểm và giá trị đã vẽ. Chúng không đánh giá thay người đọc về sự đúng mức của thông điệp.", "Đóng các điều kiện thành hàm kiểm giúp dùng lại cho nhiều hình. Điều kiện cần phù hợp từng loại biểu đồ, vì trục log hoặc biểu đồ đường có quy ước khác biểu đồ thanh. Kiểm tự động cấu trúc phải đi cùng xem hình để phát hiện chữ bị cắt, màu khó phân biệt hoặc nguồn ghi sai."),
("Đưa các nhóm lên những khung hình có cùng thang đo để chiều cao và độ dài so sánh được. Nếu từng khung tự chọn giới hạn, một biến động nhỏ có thể trông lớn như biến động ở nhóm khác. Giữ tên nhóm và đơn vị ở vị trí dễ đọc.", "Dùng `subplots` và các tùy chọn chia sẻ trục giúp thống nhất giới hạn một cách tường minh. Mã vẫn cần kiểm dữ liệu của từng nhóm và thứ tự kỳ. Khi đơn vị hai đại lượng khác nhau, không ép chúng vào cùng thang rồi diễn giải như cùng độ lớn."),
],
}


def cell(value):
    if value is None:
        return "Thiếu"
    try:
        if isinstance(value, float) and math.isnan(value):
            return "NaN"
    except TypeError:
        pass
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(value):
    import pandas as pd
    if isinstance(value, pd.Series):
        value = value.rename(value.name or "Giá trị").to_frame()
    if isinstance(value, pd.DataFrame):
        frame = value.copy()
        if frame.shape[1] > 5:
            frame = frame.iloc[:, :5]
        frame = frame.head(6)
        columns = [frame.index.name or "Chỉ mục"] + [str(c) for c in frame.columns]
        rows = [[i, *row] for i, row in frame.iterrows()]
        suffix = "\n\nBảng hiển thị tối đa sáu dòng và năm cột dữ liệu để đối chiếu.\n" if value.shape[0] > 6 or value.shape[1] > 5 else ""
    elif isinstance(value, dict):
        scalar = [(k, v) for k, v in value.items() if not isinstance(v, (pd.Series, pd.DataFrame)) and not hasattr(v, "get_figure")]
        if not scalar:
            nested = next((v for v in value.values() if isinstance(v, (pd.Series, pd.DataFrame))), None)
            return table(nested) if nested is not None else ""
        columns, rows, suffix = ["Trường", "Kết quả"], [list(pair) for pair in scalar[:8]], ""
    elif isinstance(value, (list, tuple)):
        columns, rows, suffix = ["Vị trí", "Kết quả"], list(enumerate(value[:6])), ""
    elif isinstance(value, (int, float, bool, str)):
        columns, rows, suffix = ["Kết quả"], [[value]], ""
    else:
        return ""
    return "| " + " | ".join(map(cell, columns)) + " |\n| " + " | ".join("---" for _ in columns) + " |\n" + "\n".join("| " + " | ".join(map(cell, row)) + " |" for row in rows) + suffix


def capture_outputs(text):
    import pandas as pd
    from IPython import display as ipython_display
    namespace, results = {"__name__": "__lesson__"}, {}
    raw_print = builtins.print
    previous = Path.cwd()
    with TemporaryDirectory(prefix="studyhub-teaching-") as folder:
        try:
            os.chdir(folder)
            for match in FENCE.finditer(text):
                prefix = text[:match.start()]
                ids = re.findall(r'<span id="(data-lab-[^"]+)"', prefix)
                ways = re.findall(r'^#{3,5} Cách ([12])\b', prefix, re.M)
                records = []
                def show(*values, **kwargs):
                    records.extend(values)
                def record_print(*values, **kwargs):
                    records.extend(v for v in values if isinstance(v, (pd.Series, pd.DataFrame, dict, tuple, list, int, float, bool)))
                    raw_print(*values, **kwargs)
                console = StringIO()
                with patch.object(builtins, "print", record_print), patch.object(ipython_display, "display", show), redirect_stdout(console), redirect_stderr(StringIO()):
                    namespace["display"] = show
                    exec(compile(match[1], "lesson-visible-code", "exec"), namespace)
                if ids and ways:
                    key = (ids[-1], int(ways[-1]))
                    structured = [v for v in records if isinstance(v, (pd.Series, pd.DataFrame, dict, list, tuple))]
                    chosen = structured[-1] if structured else (records[-1] if records else None)
                    results[key] = table(chosen) if chosen is not None else ("```text\n" + console.getvalue().strip()[:1600] + "\n```" if console.getvalue().strip() else "")
            if "plt" in namespace:
                namespace["plt"].close("all")
        finally:
            os.chdir(previous)
    return results


def refine(lab):
    file = LABS / f"lab-{lab}.md"
    text = file.read_text(encoding="utf-8")
    before = [m[0] for m in FENCE.finditer(text)]
    output = capture_outputs(text)
    exercises = list(re.finditer(r'<span id="(data-lab-[^"]+)"', text))
    assert len(exercises) == len(NOTES[lab]), (lab, len(exercises))
    edits = []
    for index, anchor in enumerate(exercises):
        end = exercises[index + 1].start() if index + 1 < len(exercises) else len(text)
        part = text[anchor.start():end]
        solution = re.search(r'^::: solution[^\n]*\n(.*?)^:::[ \t]*$', part, re.M | re.S)
        assert solution, anchor[1]
        body = solution[1]
        headings = list(re.finditer(r'^#{3,5} Cách ([12])[^\n]*\n', body, re.M))
        assert len(headings) == 2, anchor[1]
        images = re.findall(r'^!\[[^\n]*\]\([^\n]+\)$', body, re.M)
        replacement = []
        for way, heading in enumerate(headings, 1):
            limit = headings[way].start() if way == 1 else len(body)
            region = body[heading.end():limit]
            code = FENCE.search(region)
            assert code, (anchor[1], way)
            measured = output.get((anchor[1], way), "")
            assert measured or images, f"No measured output {anchor[1]} method{way}"
            replacement += [heading[0].rstrip(), "", code[0], "", f"#### Giải thích cách {way}", "", NOTES[lab][index][way-1], "", f"#### Kết quả cách {way}", "", measured or "Biểu đồ được lưu từ dữ liệu và mã ở trên.", ""]
            if images:
                replacement += [*images, ""]
        absolute_start = anchor.start() + solution.start(1)
        absolute_end = anchor.start() + solution.end(1)
        edits.append((absolute_start, absolute_end, "\n".join(replacement)))
    for start, end, new in reversed(edits):
        text = text[:start] + new + text[end:]
    assert before == [m[0] for m in FENCE.finditer(text)], f"Code changed: {file}"
    file.write_text(text, encoding="utf-8")
    print(f"Lab {lab}: {len(exercises)} exercises, own explanation/output after both methods, code unchanged")


if __name__ == "__main__":
    os.environ["MPLBACKEND"] = "Agg"
    parser = argparse.ArgumentParser()
    parser.add_argument("labs", nargs="+", choices=list(NOTES))
    for name in parser.parse_args().labs:
        refine(name)
