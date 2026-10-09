// Các mục tra cứu được rút từ Young & Freedman 15, mục 1.7–1.8 và chương 2.
export const physicsMotionConcepts = {
  'do-doi': {
    name: 'Độ dời', aliases: ['độ dời', 'vector độ dời'],
    definition: 'Độ dời là vector nối vị trí đầu với vị trí cuối. Trong chuyển động dọc trục x, thành phần độ dời là $\\Delta x=x_2-x_1$. Nó có thể dương, âm hoặc bằng không và khác quãng đường đã đi.',
    example: 'Xe ở 19 m rồi đến 277 m trên cùng trục có độ dời theo x bằng 258 m, như Hình 2.1.',
    use: 'Tính vận tốc trung bình và phân biệt vị trí cuối với toàn bộ hành trình.',
    question: 'Nếu đi rồi trở về vị trí đầu, độ dời có bằng quãng đường không?',
    answer: 'Độ dời bằng không, còn quãng đường khác không nếu vật đã chuyển động.'
  },
  'thanh-phan-vector': {
    name: 'Thành phần vector', aliases: ['thành phần vector', 'thành phần của vector'],
    definition: 'Trong hệ trục vuông góc đã chọn, các thành phần là những số có dấu biểu diễn vector theo các hướng trục. Với vector nằm trong mặt phẳng xy, $A_x=A\\cos\\theta$, $A_y=A\\sin\\theta$ khi $\\theta$ đo từ chiều +x về chiều +y.',
    example: 'Trong chuyển động dọc trục x, các thành phần y và z của độ dời bằng không, như mục 2.1.',
    use: 'Giữ nhất quán dấu của độ dời, vận tốc và gia tốc khi chọn chiều dương.',
    question: 'Một thành phần âm có nghĩa độ lớn vector âm không?',
    answer: 'Không. Thành phần âm chỉ hướng ngược chiều dương của trục; độ lớn vector không âm.'
  },
  'van-toc-vat-ly': {
    name: 'Vận tốc', aliases: ['vận tốc', 'vận tốc trung bình', 'vận tốc tức thời'],
    definition: 'Vận tốc là đại lượng vector. Trên trục x, vận tốc trung bình là $v_{\\mathrm{av}-x}=\\Delta x/\\Delta t$ với $\\Delta t>0$, còn vận tốc tức thời là $v_x=dx/dt$. Dấu của thành phần cho biết hướng chuyển động theo trục đã chọn.',
    example: 'Trong Ví dụ 2.1, từ 1,0 s đến 2,0 s báo có vận tốc trung bình 15 m/s; vận tốc tức thời ở 1,0 s là 10 m/s.',
    use: 'Đọc độ dốc đồ thị vị trí theo thời gian và xác định hướng chuyển động.',
    question: 'Hai vật đi qua cùng một điểm tại cùng thời điểm có nhất thiết cùng vận tốc không?',
    answer: 'Không. Ở Ví dụ 2.5, khi gặp nhau, ô tô đi 15 m/s còn cảnh sát đi 30 m/s.'
  },
  'toc-do-chuyen-dong': {
    name: 'Tốc độ chuyển động', aliases: ['tốc độ tức thời', 'tốc độ trung bình'],
    definition: 'Tốc độ tức thời là độ lớn của vận tốc tức thời, nên trong chuyển động thẳng $v=|v_x|$. Tốc độ trung bình bằng tổng quãng đường chia tổng thời gian. Hai đại lượng đều vô hướng và không âm.',
    example: 'Ở ví dụ bơi của mục 2.2, bơi 100,0 m trong 46,91 s cho tốc độ trung bình khoảng 2,132 m/s, nhưng vận tốc trung bình bằng không vì trở về điểm đầu.',
    use: 'Phân biệt quãng đường với độ dời, nhanh chậm với hướng chuyển động.',
    question: 'Hai vận tốc +25 m/s và −25 m/s có cùng tốc độ không?',
    answer: 'Có. Cả hai có tốc độ 25 m/s, nhưng hướng chuyển động ngược nhau.'
  },
  'gia-toc': {
    name: 'Gia tốc', aliases: ['gia tốc', 'gia tốc trung bình', 'gia tốc tức thời'],
    definition: 'Gia tốc là đại lượng vector mô tả sự biến thiên vận tốc. Trên trục x, $a_{\\mathrm{av}-x}=\\Delta v_x/\\Delta t$ với $\\Delta t>0$, còn $a_x=dv_x/dt$. Gia tốc dương không tự có nghĩa vật nhanh dần.',
    example: 'Trong Ví dụ 2.2(c), vận tốc từ $-0.4\\,\\mathrm{m/s}$ đến $-1.0\\,\\mathrm{m/s}$ trong $2.0\\,\\mathrm s$ cho gia tốc trung bình $-0.3\\,\\mathrm{m/s^2}$, trong khi tốc độ tăng.',
    use: 'Đọc độ dốc đồ thị vận tốc và phân biệt nhanh dần, chậm dần theo dấu của vận tốc và gia tốc.',
    question: 'Trong chuyển động thẳng, vận tốc và gia tốc trái dấu thì tốc độ biến đổi thế nào?',
    answer: 'Tốc độ giảm trên khoảng chúng trái dấu. Cùng dấu thì tốc độ tăng.'
  },
  'roi-tu-do': {
    name: 'Rơi tự do', aliases: ['rơi tự do', 'gia tốc trọng trường'],
    definition: 'Rơi tự do là chuyển động chỉ chịu tác dụng trọng lực. Gần mặt đất, trên quãng nhỏ so với bán kính Trái Đất và bỏ ảnh hưởng quay, gia tốc được coi không đổi, luôn hướng xuống. Chọn +y hướng lên thì $a_y=-g$, với $g\\approx9.80\\,\\mathrm{m/s^2}>0$.',
    example: 'Trong Ví dụ 2.7, bóng ném thẳng lên có vận tốc bằng không ở đỉnh nhưng gia tốc vẫn hướng xuống.',
    use: 'Giải cả giai đoạn đi lên lẫn đi xuống của vật được ném thẳng đứng khi bỏ lực cản không khí.',
    question: 'Vật đi lên sau khi rời tay có còn rơi tự do không?',
    answer: 'Có, nếu từ đó chỉ trọng lực tác dụng. Rơi tự do không đòi hỏi vận tốc phải hướng xuống.'
  }
}

export const physicsMotionWikiDetails = {
  'do-doi': 'Chọn vị trí đầu và cuối trước khi trừ. Trong chuyển động thẳng, $\\Delta x$ là thành phần có dấu của vector độ dời, không phải độ lớn luôn dương. Quãng đường cộng độ dài các đoạn đã đi và phụ thuộc hành trình. Độ dời chỉ phụ thuộc hai đầu.\n\nXe đua ở $x_1=19\\,\\mathrm m$ lúc $t_1=1.0\\,\\mathrm s$ và ở $x_2=277\\,\\mathrm m$ lúc $t_2=4.0\\,\\mathrm s$ có $\\Delta x=258\\,\\mathrm m$. Khi xe tải đi ngược từ 277 m về 19 m, thành phần độ dời bằng −258 m.\n\nNguồn: Young & Freedman, ấn bản 15, mục 1.7, trang in 10–14; mục 2.1, trang in 34–37, công thức (2.1) và Hình 2.1–2.2.',
  'thanh-phan-vector': 'Góc θ trong $A_x=A\\cos\\theta$ và $A_y=A\\sin\\theta$ phải đo từ chiều +x về chiều +y. Khi chọn góc từ một trục khác, cần xác định lại cạnh kề, cạnh đối và dấu. Trong ba chiều, $\\vec A=A_x\\hat{\\mathbf i}+A_y\\hat{\\mathbf j}+A_z\\hat{\\mathbf k}$. Các thành phần có cùng đơn vị với vector.\n\nTrong chương 2, vật chỉ đi trên trục x, nên $v_y=v_z=0$ và $a_y=a_z=0$ khi dùng trục x cho chuyển động. Với bài rơi tự do dùng trục y, thành phần cần xét chuyển sang y.\n\nNguồn: Young & Freedman, ấn bản 15, mục 1.8–1.9, trang in 14–19; mục 2.1–2.3, trang in 34–44.',
  'van-toc-vat-ly': 'Vận tốc trung bình dùng độ dời giữa hai đầu và cả khoảng thời gian. Vận tốc tức thời dùng giới hạn khi khoảng thời gian tiến tới không. Không lấy giá trị tại một thời điểm thay cho trung bình trên một khoảng nếu chưa biết đặc điểm chuyển động.\n\nTrên đồ thị x–t, độ dốc dây cung là vận tốc trung bình, còn độ dốc tiếp tuyến là vận tốc tức thời. Đường cong x–t không phải quỹ đạo thật của vật. Vận tốc bằng không khi tiếp tuyến nằm ngang; tọa độ tại đó có thể khác không.\n\nNguồn: Young & Freedman, ấn bản 15, mục 2.1–2.2, trang in 34–40, công thức (2.2)–(2.3), Ví dụ 2.1; Ví dụ 2.5, trang in 49.',
  'toc-do-chuyen-dong': 'Tốc độ trung bình dùng toàn bộ quãng đường. Độ lớn vận tốc trung bình dùng độ lớn độ dời. Hành trình bơi trở lại điểm xuất phát ở mục 2.2 cho vận tốc trung bình bằng không dù tốc độ trung bình dương.\n\nTốc độ tức thời luôn bằng độ lớn vận tốc tức thời. Trong chuyển động dọc trục x, $v=|v_x|$, nên đổi dấu v_x không làm tốc độ âm.\n\nNguồn: Young & Freedman, ấn bản 15, mục 2.2, trang in 37–40, phần phân biệt speed và velocity, ví dụ bơi 100,0 m trong 46,91 s.',
  'gia-toc': 'Trong chuyển động thẳng, dấu của gia tốc cho biết vận tốc có dấu đang tăng hay giảm, không tự cho biết tốc độ tăng hay giảm. Khi $v_x$ và $a_x$ cùng dấu, vật nhanh dần. Khi trái dấu, vật chậm dần. Tại điểm đổi chiều, $v_x=0$ không bắt buộc $a_x=0$.\n\nTrên đồ thị v_x–t, gia tốc tức thời là độ dốc tiếp tuyến. Trên đồ thị x–t, gia tốc là đạo hàm bậc hai $a_x=d^2x/dt^2$. Với a_x không đổi, vận tốc là hàm tuyến tính của thời gian; công thức vận tốc trung bình bằng nửa tổng vận tốc đầu và cuối chỉ được dùng trong trường hợp này.\n\nNguồn: Young & Freedman, ấn bản 15, mục 2.3–2.4, trang in 40–49, công thức (2.4)–(2.6), Bảng 2.3–2.4 và phương trình (2.10).',
  'roi-tu-do': 'Độ lớn g là số dương; thành phần gia tốc có dấu phụ thuộc trục. Chọn +y hướng lên cho $a_y=-g$ ở cả nhánh đi lên và nhánh đi xuống, kể cả tại điểm cao nhất. Vận tốc thay đổi liên tục, còn gia tốc giữ nguyên trong mô hình của chương.\n\nDùng các phương trình gia tốc không đổi với x thay bằng y và a_x thay bằng −g. Trước khi thay số, xác định vị trí đầu, vận tốc đầu và mốc thời gian; một vật được thả từ khinh khí cầu đang đi lên không có vận tốc đầu bằng không so với mặt đất.\n\nNguồn: Young & Freedman, ấn bản 15, mục 2.5, trang in 50–53, Ví dụ 2.6–2.8; bài 2.42, trang in 61.'
}

export const physicsMotionWikiConnections = {
  'do-doi': ['thanh-phan-vector', 'van-toc-vat-ly', 'toc-do-chuyen-dong'],
  'thanh-phan-vector': ['vector', 'do-doi', 'van-toc-vat-ly'],
  'van-toc-vat-ly': ['do-doi', 'toc-do-chuyen-dong', 'gia-toc'],
  'toc-do-chuyen-dong': ['van-toc-vat-ly', 'do-doi', 'gia-toc'],
  'gia-toc': ['van-toc-vat-ly', 'dao-ham', 'roi-tu-do'],
  'roi-tu-do': ['gia-toc', 'van-toc-vat-ly', 'thanh-phan-vector']
}
