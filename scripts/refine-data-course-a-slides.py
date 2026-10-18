"""Write concise review cards aligned with the verified Python/NumPy/pandas Notes."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKTREE = Path('C:/Users/Ai/.codex/worktrees/data-course-20261018-a')
CARDS = {
'1': [
 ('Xác định câu hỏi trước khi cộng cột', ['Một hàng phải có đơn vị quan sát rõ ràng.', 'Kiểm tra khóa, đơn vị và phạm vi thời gian trước khi ghép hoặc tổng hợp.'], 'Hai bảng đơn hàng và thanh toán có thể khác tổng vì không cùng tập giao dịch.'),
 ('Chọn công cụ theo thao tác', ['NumPy phục vụ tính toán trên mảng, pandas hỗ trợ bảng có nhãn.', 'Matplotlib vẽ hình, còn các thư viện mô hình cần dữ liệu đầu vào đã được kiểm tra.'], 'Một bảng có thể cần đọc tệp, làm sạch, ghép rồi mới vẽ.'),
 ('Tệp notebook và trạng thái kernel khác nhau', ['Notebook lưu mã và kết quả, kernel giữ các biến của phiên đang chạy.', 'Chạy lại từ kernel mới giúp phát hiện phụ thuộc vào các ô đã xóa hoặc chạy khác thứ tự.'], 'Xóa một ô khai báo không tự xóa biến đã tạo trong kernel.'),
 ('Ghi lại môi trường để chạy lại', ['Dùng môi trường riêng cho các gói phụ thuộc của dự án.', 'Ghi phiên bản Python và thư viện, rồi kiểm tra việc chạy lại từ đầu.'], 'requirements.txt mô tả các gói, còn .python-version chỉ có tác dụng với công cụ hỗ trợ nó.')],
'2': [
 ('Thử lệnh và tra cứu trong IPython', ['Tab gợi ý tên và thuộc tính trong phiên làm việc.', 'Dấu hỏi tra tài liệu, còn hai dấu hỏi chỉ hiện mã nguồn khi có thể truy cập.'], 'np.array? tra thông tin về hàm tạo mảng.'),
 ('Gán tên không sao chép đối tượng', ['b = a có thể làm hai tên cùng tham chiếu một list.', 'Sửa list qua tham số khác với gán lại tên tham số trong hàm.'], 'b.append(40) làm đổi list dùng chung, còn b = [] chỉ gắn lại tên b.'),
 ('Phân biệt chuỗi ký tự và byte', ['str giữ văn bản Unicode, bytes giữ dãy byte.', 'Mã hóa và giải mã phải dùng đúng bảng mã của dữ liệu.'], 'encode("utf-8") và decode("utf-8") chuyển hai chiều khi dữ liệu hợp lệ.'),
 ('Giữ đúng ý nghĩa của điều kiện', ['None biểu thị vắng giá trị, còn 0 vẫn có thể là dữ liệu hợp lệ.', 'if, for và while điều khiển bước xử lý theo điều kiện đã nêu.'], 'Lọc bằng is not None không vô tình bỏ giá bằng 0.')],
'3': [
 ('Chọn list, tuple, dict hoặc set', ['List lưu dãy có thứ tự và cho phép sửa nội dung.', 'Dict tra theo khóa, set biểu diễn các giá trị phân biệt.', 'Tuple không cho thay phần tử nhưng phần tử con có thể khả biến.'], 'Dùng hiệu hai set để tìm mã mới xuất hiện hoặc không còn xuất hiện.'),
 ('Sao chép ngoài chưa tách dữ liệu bên trong', ['Sao chép nông tạo cấu trúc ngoài mới nhưng có thể giữ tham chiếu con.', 'Chọn copy phù hợp với phần dữ liệu mà chương trình định sửa.'], 'Hai list ngoài khác nhau vẫn có thể cùng chứa một list con.'),
 ('Viết hàm và bắt lỗi đúng phạm vi', ['Một hàm cần quy định đầu vào, đầu ra và trường hợp không hợp lệ.', 'Bắt đúng ngoại lệ giúp phân biệt dữ liệu sai với lỗi lập trình.'], 'Hàm đọc giá có thể trả None cho chuỗi không theo định dạng đã chọn.'),
 ('Đọc dãy và tệp theo nhu cầu', ['Generator cung cấp giá trị khi được yêu cầu, không tự lưu cả kết quả.', 'with open giúp đóng tệp khi thoát khỏi khối, còn encoding phải khớp nguồn.'], 'Đọc từng dòng không ngăn bộ nhớ tăng nếu vẫn giữ mọi dòng vào một list.')],
'4': [
 ('Đọc shape, dtype và số byte', ['shape nêu kích thước các trục, ndim nêu số trục.', 'nbytes bằng size nhân itemsize, không tính siêu dữ liệu hoặc lượng cấp phát mới của một view.'], 'A có shape (4, 3), dtype int64 nên có nbytes bằng 96.'),
 ('Chọn dữ liệu và kiểm tra dùng chung bộ nhớ', ['Lát cắt cơ bản thường tạo view, còn đọc bằng mảng chỉ mục tạo bản sao dữ liệu.', 'reshape có thể dùng lại bộ nhớ hoặc phải sao chép tùy strides và thứ tự được yêu cầu.'], 'Dùng np.shares_memory để kiểm tra hai mảng cụ thể, thay vì chỉ nhìn thuộc tính base.'),
 ('Broadcasting phải khớp đúng trục', ['So các trục từ phải sang trái, mỗi cặp cần bằng nhau hoặc có một trục dài 1.', 'Trung bình theo hàng cần giữ trục phù hợp trước khi trừ khỏi từng hàng.'], 'A + b + d[:, None] cộng b theo cột và d theo hàng khi shape phù hợp.'),
 ('Tính trên mảng và mô phỏng có điều kiện', ['Các phép toán số thường giảm công việc lặp ở tầng Python, nhưng hiệu năng cần được đo.', 'Dùng generator ngẫu nhiên và kiểm tra điều kiện chạm ngưỡng trước khi lấy argmax.'], 'Một đường đi chưa chạm ngưỡng vẫn có argmax bằng 0 trên mask toàn False.')],
'5': [
 ('Series và DataFrame mang nhãn', ['Series có một trục nhãn, DataFrame có nhãn hàng và cột.', 'Kiểm tra kiểu cột và giá thiếu trước khi tính hoặc so sánh.'], 'Chọn một tên cột trả Series, còn danh sách tên cột giữ kết quả DataFrame.'),
 ('Chọn theo nhãn hoặc theo vị trí', ['loc chọn theo nhãn, iloc chọn theo vị trí.', 'Trong pandas 3, gán qua đối tượng trung gian không cập nhật DataFrame gốc.'], 'Dùng df.loc[mask, "gia"] = ... để chỉ rõ hàng và cột đích.'),
 ('Phép toán khớp nhãn trước khi tính', ['Hai Series khác thứ tự vẫn được ghép theo nhãn.', 'Nhãn chỉ có một bên có thể tạo kết quả thiếu, cần nêu cách xử lý.'], 'Nhãn b có giá 20 và 30 cho tổng 50 dù nằm ở hai vị trí khác nhau.'),
 ('Mẫu số và tập hàng là một phần của kết luận', ['count và số hàng có thể khác nhau khi có giá thiếu.', 'So hai trung bình qua thời gian cần kiểm tra tập đối tượng được quan sát.'], 'Trong bài tập, trung bình toàn cột giảm nhưng trung bình trên cùng a, b lại tăng.')],
'B': [
 ('Magic bổ sung thao tác trong phiên tương tác', ['Phân biệt magic một dòng với magic của cả ô.', 'run có thể đưa các tên trong tệp vào phiên để tiếp tục kiểm tra.'], '%run script.py dùng trong IPython, không phải cú pháp của tệp Python thuần.'),
 ('Lịch sử giúp tìm lại phép thử', ['In và Out giữ lịch sử trong phạm vi phiên tương tác.', 'Lưu lại mã cần chạy lại, không phụ thuộc lâu dài vào số thứ tự đầu ra.'], 'Một kết quả trong Out phụ thuộc biểu thức đã thực thi ở phiên đó.'),
 ('Gỡ lỗi và đo thời gian trả lời hai câu hỏi', ['Debug giúp xem bước sai cùng trạng thái biến.', 'timeit và profile giúp đo thời gian hoặc tìm phần chiếm nhiều thời gian.'], 'Đo các cách làm trên cùng nhiệm vụ và tạo dữ liệu ở cùng giai đoạn.'),
 ('Reload và cấu hình cần được kiểm tra', ['autoreload hỗ trợ nạp lại mã trong quá trình phát triển nhưng không thay việc chạy lại từ đầu.', 'Phím tắt và cấu hình có thể khác theo terminal, chế độ sửa dòng và phiên bản.'], 'Sau thay đổi quan trọng, chạy lại từ phiên sạch để kiểm tra phụ thuộc trạng thái.')]
}


def main():
    contract = json.loads((ROOT/'raw_materials/xu-ly-du-lieu/authoring-contract.json').read_text(encoding='utf-8'))
    for entry in contract['lessons']:
        if entry['chapter'] not in CARDS:
            continue
        slides = [{'note':entry['slug'],'title':title,'bullets':bullets,'formula':'','example':example}
                  for title,bullets,example in CARDS[entry['chapter']]]
        file = WORKTREE/'src/content/courses/xu-ly-du-lieu/lectures'/entry['slug']/'slides.mjs'
        file.write_text('export const slides = '+json.dumps(slides,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Wrote 24 concise cards matching the six Group A units')


if __name__ == '__main__':
    main()
