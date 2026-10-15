import re

bullet = """    - **Căn lề dấu bằng thẳng hàng (Aligned Equals Signs)**:
      - Trong môi trường `\\begin{aligned}`, dấu bằng ở các dòng phải thẳng hàng nhau bằng cách đặt `&` ngay trước dấu bằng hoặc dấu quan hệ (`&=`, `&\\le`, `&\\ge`, `&\\approx`, v.v.).
      - Tuyệt đối không đặt dấu `&` bên trong dấu ngoặc đơn (ví dụ: Cấm viết `P(Y &= 2)` hay `P(1 &\\le X)` mà phải viết `P(Y = 2) &= ...` hay `P(1 \\le X) &= ...`).
      - Không đặt `&` sau dấu bằng (như `= &`), và không để sót dòng có dấu bằng mà thiếu ký hiệu `&` gây lệch cột.
"""

target = "    - Chỉ dùng `\\begin{aligned}` khi có chuỗi biến đổi nhiều bước qua dấu bằng hoặc hệ nhiều phương trình.\n"

for filename in ['AGENTS.md', 'GEMINI.md']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n')
    if target in content and "Căn lề dấu bằng thẳng hàng" not in content:
        content = content.replace(target, target + bullet)
    with open(filename, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write(content)
print("Updated AGENTS.md and GEMINI.md")
