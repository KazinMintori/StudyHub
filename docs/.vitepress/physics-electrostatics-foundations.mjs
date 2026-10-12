export const electrostaticsConcepts = {
  'tich-co-huong': {
    name: 'Tích có hướng', aliases: ['tích có hướng', 'tích vector', 'tích vectơ'],
    definition: 'Tích có hướng $\\vec A\\times\\vec B$ là vector vuông góc hai vector đầu vào, có độ lớn $AB\\sin\\varphi$ và hướng theo quy tắc bàn tay phải. Đổi thứ tự hai vector làm tích đổi dấu.',
    example: 'Mômen lực lên lưỡng cực là $\\vec\\tau=\\vec p\\times\\vec E$. Mômen bằng không khi hai vector song song hoặc ngược chiều.',
    use: 'Xác định hướng mômen lực và phân biệt với tích vô hướng.',
    question: 'Đổi từ A × B sang B × A có giữ hướng không?', answer: 'Không. Kết quả đổi dấu, tức đảo hướng nếu khác vector không.'
  },
  'can-bang-co-hoc': {
    name: 'Cân bằng bền và không bền', aliases: ['cân bằng bền', 'cân bằng không bền'],
    definition: 'Cân bằng bền có xu hướng trở về khi bị lệch nhỏ, còn cân bằng không bền có xu hướng đi xa hơn sau lệch nhỏ. Với tọa độ tự do đang xét, cực tiểu thế năng gắn với cân bằng bền và cực đại với cân bằng không bền.',
    example: 'Lưỡng cực có mômen cùng chiều trường đều ở cân bằng bền; ngược chiều ở cân bằng không bền.',
    use: 'Phân biệt mômen bằng không với điều kiện ổn định khi lưỡng cực quay.',
    question: 'Mômen lực bằng không có bảo đảm cân bằng bền không?', answer: 'Không. Phải xét sự đáp ứng sau một lệch nhỏ.'
  },
  'duong-dong-chat-luu': {
    name: 'Đường dòng chất lưu', aliases: ['đường dòng'],
    definition: 'Đường dòng có tiếp tuyến tại mỗi điểm cùng hướng vector vận tốc chất lưu ở thời điểm đang xét. Đây là cách biểu diễn hướng trường vận tốc.',
    example: 'Đường sức điện dùng cách định hướng tiếp tuyến tương tự đường dòng, nhưng không có chất nào chảy trong điện trường.',
    use: 'Hình dung đường sức như đường biểu diễn một trường vector.',
    question: 'So sánh với đường dòng có nghĩa điện trường là dòng vật chất không?', answer: 'Không. Sự tương tự là về cách biểu diễn toán học.'
  },
  'vat-dan-cach-dien': {
    name: 'Vật dẫn và vật cách điện', aliases: ['vật dẫn', 'vật cách điện', 'electron tự do'],
    definition: 'Vật dẫn cho điện tích dễ chuyển động qua vật, còn vật cách điện thì không. Kim loại có electron tự do. Ở cân bằng tĩnh điện, trường bên trong vật liệu dẫn bằng không.',
    example: 'Dây đồng truyền điện tích đến cầu kim loại, còn sợi nylon treo cầu ngăn điện tích thoát qua giá đỡ.',
    use: 'Giải thích nhiễm điện tiếp xúc, nối đất và cân bằng tĩnh điện.',
    question: 'Trường trong vật liệu dẫn bằng không có tự bảo đảm trường trong mọi lỗ rỗng bằng không không?', answer: 'Không. Phải xét điện tích và cấu hình của lỗ rỗng riêng.'
  },
  'phan-cuc-dien': {
    name: 'Phân cực điện', aliases: ['phân cực điện', 'phân cực'],
    definition: 'Phân cực điện là sự dịch chuyển tương đối của điện tích dương và âm trong vật. Vật có thể giữ tổng điện tích bằng không dù hai phía có phân bố điện tích khác nhau.',
    example: 'Lược mang điện hút mảnh nhựa trung hòa vì phần trái dấu gần lược chịu lực hút mạnh hơn lực đẩy lên phần cùng dấu ở xa.',
    use: 'Giải thích lực lên vật trung hòa và mômen lưỡng cực.',
    question: 'Bị phân cực có nhất thiết nghĩa là vật có điện tích tổng khác không?', answer: 'Không. Phân cực tách vị trí điện tích, không bắt buộc thay đổi tổng điện tích.'
  },
  'luong-cuc-dien': {
    name: 'Lưỡng cực điện', aliases: ['lưỡng cực điện', 'mômen lưỡng cực', 'mômen lưỡng cực điện'],
    definition: 'Lưỡng cực gồm hai điện tích điểm +q và −q cách nhau d, với q dương. Mômen có độ lớn $p=qd$, hướng từ âm đến dương. Trong trường ngoài đều, hợp lực bằng không nhưng mômen lực có thể khác không.',
    example: 'Phân tử nước trung hòa nhưng hai phía điện tích tách nhau, nên tương tác với ion trong dung dịch.',
    use: 'Tính mômen lực, thế năng và trường xa của hệ hai điện tích trái dấu.',
    question: 'Hợp lực bằng không trong trường đều có nghĩa mômen lực cũng bằng không không?', answer: 'Không. Hai lực có thể tạo ngẫu lực làm lưỡng cực quay.'
  }
}

export const electrostaticsWikiDetails = {
  'tich-co-huong': 'Với hệ cơ sở trực chuẩn thuận tay phải, các thành phần là:\n\n$$\n\\begin{aligned}\nC_x&=A_yB_z-A_zB_y,\\\\\nC_y&=A_zB_x-A_xB_z,\\\\\nC_z&=A_xB_y-A_yB_x.\n\\end{aligned}\n$$\n\nĐộ lớn tích bằng không khi hai vector song song, ngược chiều hoặc một vector bằng không. Tích có hướng khác tích vô hướng: Tích vô hướng là số, còn tích có hướng là vector.\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 1.10, trang 19–24 và mục 21.7, trang 702–703.',
  'can-bang-co-hoc': 'Một hướng có mômen lực bằng không mới chỉ là vị trí cân bằng. Để xét bền, quay lệch một góc nhỏ và xác định chiều mômen sau lệch. Với lưỡng cực trong trường đều, $U=-pE\\cos\\varphi$. Cùng chiều trường cho thế năng nhỏ nhất −pE, còn ngược chiều cho thế năng lớn nhất +pE.\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 7.5 và mục 21.7, trang 703–705.',
  'duong-dong-chat-luu': 'Đường dòng biểu diễn một trường vận tốc qua tiếp tuyến. Đường sức điện cũng dùng tiếp tuyến để biểu diễn hướng vector điện trường. Sự giống nhau không cho phép xem trường điện là một dòng chất chảy, hoặc đồng nhất đường sức với quỹ đạo điện tích.\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 12.5 và mục 21.6, trang 700–701.',
  'vat-dan-cach-dien': 'Trong kim loại, một phần electron ngoài cùng có thể di chuyển khắp vật, còn các hạt nhân nằm gần vị trí cố định. Trong chất cách điện, điện tích vẫn có thể dịch tương đối một khoảng nhỏ, gây phân cực, dù không chạy tự do qua toàn vật.\n\nỞ cân bằng tĩnh điện, trường trong vật liệu dẫn phải bằng không vì nếu khác không, các điện tích tự do sẽ chịu lực và có chuyển động tổng. Điều kiện này cần được nêu cùng kết luận.\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 21.2, trang 682–684 và mục 21.4, trang 692.',
  'phan-cuc-dien': 'Phân biệt phân cực với việc nhận điện tích tổng: Một vật trung hòa có thể tách các tâm điện tích mà tổng đại số vẫn bằng không. Trong trường không đều, hai phía chịu lực không bù hết, vì vậy vật trung hòa có thể bị hút. Trong trường đều, lưỡng cực lý tưởng có hợp lực bằng không nhưng có mômen quay.\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 21.2, trang 684 và mục 21.7, trang 702–704.',
  'luong-cuc-dien': 'Trong trường ngoài đều:\n\n$$\n\\begin{aligned}\n\\vec\\tau&=\\vec p\\times\\vec E,\\\\\n\\tau&=pE\\sin\\varphi,\\\\\nU&=-\\vec p\\cdot\\vec E.\n\\end{aligned}\n$$\n\nGóc φ nằm giữa hai vector. Mômen quay có xu hướng đưa p cùng chiều trường. Điều kiện trường đều thiết yếu cho kết luận hợp lực bằng không. Trong trường không đều, lưỡng cực có thể chịu hợp lực. Ở xa trên trục, với r lớn hơn nhiều kích thước d, trường gần có độ lớn $\\frac{2kp}{r^3}$.\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 21.7, trang 701–705.'
}

export const electrostaticsWikiConnections = {
  'tich-co-huong':['vector','tich-vo-huong','momen-luc'],
  'can-bang-co-hoc':['luong-cuc-dien','momen-luc','cong-nang-luong'],
  'duong-dong-chat-luu':['vector','dien-truong'],
  'vat-dan-cach-dien':['dien-tich','dien-truong','phan-cuc-dien'],
  'phan-cuc-dien':['luong-cuc-dien','vat-dan-cach-dien','dien-tich'],
  'luong-cuc-dien':['dien-truong','tich-co-huong','phan-cuc-dien']
}
