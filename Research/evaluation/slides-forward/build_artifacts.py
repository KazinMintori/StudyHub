import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def block(kind, content, sources, addition=False, rationale=None):
    field = {'text': 'text', 'equation': 'latex', 'table': 'rows'}[kind]
    row = {'type': kind, field: content, 'provenance': 'pedagogical-addition' if addition else 'source-adaptation', 'source_unit_ids': sources}
    if addition:
        row['rationale'] = rationale
    return row

def text(content, sources, rationale=None):
    return block('text', content, sources, bool(rationale), rationale)

def eq(content, sources, rationale=None):
    return block('equation', content, sources, bool(rationale), rationale)

slides = []

def slide(n, title, goal, sources, introduced, used, body, minutes, speech, study, bridge, role='explanation', checkpoint=None):
    row = {'id': f'L01-S{n:03}', 'lecture_id': 'L01', 'layer': 'core', 'role': role,
           'title': title, 'learning_goal': goal, 'source_unit_ids': sources,
           'prerequisite_slide_ids': [slides[-1]['id']] if slides else [],
           'introduced_term_ids': introduced, 'used_term_ids': used,
           'body': body, 'visuals': [], 'speaker_notes': speech,
           'study_note_ref': f'study-note.md#slide-{n}', 'study_text': study,
           'next_bridge': bridge, 'estimated_minutes': minutes}
    if checkpoint:
        row['checkpoint'] = checkpoint
    slides.append(row)

slide(1, 'Từ đạo hàm đến một bước tìm giá trị nhỏ hơn',
      'Nêu mục tiêu tìm x để f(x) nhỏ và xác định nghiệm của ví dụ bằng tính không âm.',
      ['SRC-02'], ['TERM-OBJECTIVE'], ['TERM-DERIVATIVE', 'TERM-OBJECTIVE'],
      [eq(r'f(x)=(x-3)^2,\qquad x_0=0', ['SRC-02']),
       text('Ta muốn chọn x để hàm mục tiêu f(x) nhỏ nhất.', ['SRC-02'], 'Giới thiệu nghĩa của tối ưu trong ví dụ.'),
       eq(r'f(x)\geq 0,\qquad f(3)=0', ['SRC-02'], 'Dùng kiến thức bình phương để xác định đích của ví dụ.'),
       text('Ta sẽ dùng đạo hàm để tính từng bước từ x₀ = 0.', ['SRC-02'], 'Mở câu hỏi về quá trình thay vì chỉ biết nghiệm.')],
      0.75,
      'Hàm này nhỏ nhất ở đâu? Vì bình phương không âm và bằng 0 tại x = 3, ta đã biết đích của ví dụ. Nhưng hôm nay ta học cách dùng đạo hàm để tính từng bước từ x₀ = 0. Sau bài, ta cần tính được một bước mới, giải thích dấu trừ và phân biệt hai quy ước dấu xuất hiện trong nguồn.',
      'Hàm mục tiêu là hàm dùng để đánh giá lựa chọn x. Trong ví dụ, ta muốn làm f(x) = (x − 3)² nhỏ nhất. Với mọi x thực, f(x) không âm; tại x = 3, f(3) = 0. Vì thế x = 3 cho giá trị nhỏ nhất. Biết đích trong ví dụ giúp kiểm tra các bước tính sau, nhưng quy tắc cập nhật vẫn cần được học riêng.',
      'Để chọn bước từ x₀, ta đọc quy tắc gradient descent.')

slide(2, 'Dấu trừ chọn hướng; αₖ điều chỉnh độ dời',
      'Đọc đúng các ký hiệu và phân biệt hướng với điểm cập nhật trong một biến.',
      ['SRC-01'], ['TERM-GRADIENT', 'TERM-ITERATE', 'TERM-STEP', 'TERM-GD'],
      ['TERM-DERIVATIVE', 'TERM-GRADIENT', 'TERM-ITERATE', 'TERM-STEP', 'TERM-GD'],
      [eq(r'x_{k+1}=x_k-\alpha_k\nabla f(x_k),\qquad \alpha_k>0', ['SRC-01']),
       text('xₖ là giá trị ở bước k; xₖ₊₁ là giá trị sau cập nhật. αₖ là bước học.', ['SRC-01'], 'Giải nghĩa ký hiệu trước khi truy vết.'),
       text('Gradient gom các đạo hàm riêng trong bài nhiều biến. Với một biến, ∇f(x) là f′(x).', ['SRC-01'], 'Nối ký hiệu gradient với đạo hàm người học đã biết; không yêu cầu tính nhiều biến.'),
       text('Nếu f′(xₖ) < 0, cập nhật làm x tăng; nếu f′(xₖ) > 0, cập nhật làm x giảm.', ['SRC-01'], 'Giải thích dấu trừ bằng dấu đạo hàm và αₖ dương.'),
       text('Đi theo hướng này chưa bảo đảm f giảm với mọi bước học dương.', ['SRC-01'], 'Giữ giới hạn của phát biểu, nguồn chưa cho điều kiện hội tụ.')],
      1.75,
      'Chỉ số k đếm số lần cập nhật, không phải số mũ. Ta lấy gradient tại xₖ rồi nhân với αₖ. Với một biến, hãy đọc gradient như đạo hàm đã biết. Khi đạo hàm âm, hàm giảm nếu x tăng một lượng đủ nhỏ; dấu trừ làm độ dời dương. Khi đạo hàm dương thì hướng ngược lại. Hướng là điều ta chọn trước, còn độ dời bằng −αₖf′(xₖ). Một αₖ quá lớn vẫn có thể đưa ta đến giá trị hàm lớn hơn.',
      'Gradient descent là quy tắc tạo dãy các giá trị x₀, x₁, x₂, … cho bài toán không ràng buộc. Trong công thức, k là chỉ số bước; αₖ > 0 điều chỉnh mức thay đổi. Gradient ∇f gom các đạo hàm riêng khi có nhiều biến. Bài này chỉ tính một biến, nên ∇f(x) = f′(x). Nếu f′(xₖ) âm thì −αₖf′(xₖ) dương, do đó xₖ₊₁ > xₖ. Nếu f′(xₖ) dương thì độ dời âm. Dấu đạo hàm mô tả thay đổi ở gần xₖ; nó không bảo đảm mọi αₖ dương đều làm f giảm. Bài không đưa ra định lý hội tụ cho hàm tổng quát.',
      'Ta dùng quy tắc ấy để tính bước đầu của ví dụ.')

slide(3, 'Bước đầu đưa x từ 0 đến 1,5',
      'Tính đạo hàm tại x₀, độ dời, x₁ và kiểm tra giá trị hàm.',
      ['SRC-01', 'SRC-02'], [], ['TERM-DERIVATIVE', 'TERM-GRADIENT', 'TERM-ITERATE', 'TERM-STEP', 'TERM-GD'],
      [eq(r'f(x)=(x-3)^2,\quad x_0=0,\quad\alpha=\tfrac14', ['SRC-02']),
       eq(r'f\prime(x)=2(x-3),\qquad f\prime(0)=-6', ['SRC-02'], 'Mở bước đạo hàm của ví dụ nguồn.'),
       eq(r'\Delta x_0=-\tfrac14(-6)=\tfrac32,\qquad x_1=0+\tfrac32=1{,}5', ['SRC-01', 'SRC-02'], 'Tách độ dời khỏi điểm cập nhật để tránh nhầm dấu.'),
       eq(r'f(x_0)=9,\qquad f(x_1)=2{,}25', ['SRC-02'], 'Kiểm tra độc lập xem bước vừa tính có làm hàm giảm.')],
      2.0,
      'Ta tính đạo hàm trước: f′(x) = 2(x − 3). Thay x₀ = 0 được −6. Vì α = 1/4, độ dời là −(1/4)(−6) = 1,5. Hai dấu âm triệt tiêu, nên x tăng từ 0 lên 1,5. Δx₀ chỉ là ký hiệu cho độ dời ở bước đầu; x₁ mới là điểm sau cập nhật. Kiểm tra lại: bình phương khoảng cách đến 3 giảm từ 9 xuống 2,25.',
      'Với f(x) = (x − 3)², đạo hàm là f′(x) = 2(x − 3). Tại x₀ = 0, đạo hàm bằng −6. Ký hiệu Δx₀ là độ dời x₁ − x₀. Theo quy tắc cập nhật, Δx₀ = −(1/4)(−6) = 3/2, nên x₁ = 1,5. Giá trị hàm tại x₀ là 9, còn tại x₁ là (1,5 − 3)² = 2,25. Bước này thực sự làm hàm giảm. Kết quả đó được kiểm tra bằng giá trị hàm, không chỉ bằng dấu của đạo hàm.',
      'Ở bước tiếp theo, ta phải lấy đạo hàm tại đâu?')

slide(4, 'Tự tính bước từ x₁ đến x₂',
      'Tính bước mới với đạo hàm tại x₁ thay vì lặp lại đạo hàm tại x₀.',
      ['SRC-01', 'SRC-02'], [], ['TERM-DERIVATIVE', 'TERM-GRADIENT', 'TERM-ITERATE', 'TERM-STEP', 'TERM-GD'],
      [eq(r'x_1=1{,}5,\qquad\alpha=\tfrac14,\qquad f\prime(x)=2(x-3)', ['SRC-01', 'SRC-02'], 'Nhắc dữ kiện đủ để tự thực hiện bước mới.'),
       text('Tính f′(x₁), x₂ và f(x₂). Giá trị hàm tăng hay giảm?', ['SRC-01', 'SRC-02'], 'Kiểm tra truy vết một bước tương tự, giảm hỗ trợ.')],
      1.25,
      'Dành 35 giây để tự tính ba giá trị. Điểm cần kiểm tra là đạo hàm phải được lấy tại x₁ = 1,5. Chưa chiếu lời giải. Nếu người học dùng −6 lần nữa, hỏi họ ký hiệu xₖ trong công thức đang ứng với giá trị nào. Sau khi có câu trả lời, chuyển sang trang kế tiếp để đối chiếu.',
      'Hãy tự tính trước khi đọc lời giải ở mục Slide 5. Dùng f′(x₁) với x₁ = 1,5 và α = 1/4 để tìm x₂, rồi thay x₂ vào f(x) = (x − 3)². Bài đạt khi chọn đúng điểm lấy đạo hàm, xử lý đúng dấu và dùng giá trị hàm để kết luận tăng hay giảm.',
      'Ta đối chiếu từng bước, rồi xét xem α dương đã đủ chưa.', role='checkpoint',
      checkpoint={'prompt': 'Tính f′(1,5), x₂ và f(x₂) với α = 1/4. Hàm tăng hay giảm?',
                  'answer': 'f′(1,5) = −3; x₂ = 2,25; f(x₂) = 0,5625 < 2,25, nên hàm giảm.',
                  'rationale': 'Mỗi bước dùng đạo hàm tại giá trị vừa có, không tại x₀.',
                  'anticipated_error': 'Lặp f′(x₀) = −6 và tính x₂ = 3.',
                  'feedback': 'Thay x₁ = 1,5 vào 2(x − 3) trước; sau đó mới nhân −1/4.',
                  'answer_placement': 'next_slide', 'answer_slide_id': 'L01-S005',
                  'provenance': 'pedagogical-addition', 'source_unit_ids': ['SRC-01', 'SRC-02'],
                  'provenance_rationale': 'Cho người học truy vết bước kế tiếp của ví dụ nguồn.'})

slide(5, 'Cập nhật đúng; bước học lớn vẫn có thể làm hàm tăng',
      'Đối chiếu x₂ và bác bỏ suy luận mọi α dương đều làm f giảm.',
      ['SRC-01', 'SRC-02'], [], ['TERM-DERIVATIVE', 'TERM-GRADIENT', 'TERM-ITERATE', 'TERM-STEP', 'TERM-GD'],
      [eq(r'f\prime(1{,}5)=-3,\quad x_2=1{,}5-\tfrac14(-3)=2{,}25', ['SRC-01', 'SRC-02'], 'Hiển thị lời giải checkpoint sau thời gian trả lời.'),
       eq(r'f(x_2)=(2{,}25-3)^2=0{,}5625<2{,}25', ['SRC-02'], 'Hoàn tất kiểm tra giá trị hàm.'),
       text('Thử thay riêng bước học ở x₀ = 0 bằng α = 2.', ['SRC-01', 'SRC-02'], 'Thử biên để kiểm tra suy rộng về mọi bước học dương.'),
       eq(r'x_1=0-2(-6)=12,\qquad f(12)=81>9=f(0)', ['SRC-01', 'SRC-02'], 'Phản ví dụ cụ thể cho khẳng định mọi α > 0 đều làm f giảm.')],
      1.75,
      'Đạo hàm tại 1,5 bằng −3. Độ dời là 0,75, nên x₂ = 2,25. Giá trị hàm tiếp tục giảm còn 0,5625. Bây giờ chỉ thay bước học của bước đầu bằng 2, vẫn là số dương. Ta đến x₁ = 12 và giá trị hàm bằng 81, lớn hơn 9. Ví dụ này cho thấy α > 0 chưa đủ để bảo đảm giảm. Nó không phủ nhận kết quả vừa tính với α = 1/4 và cũng không chứng minh một điều kiện chọn bước cho mọi hàm.',
      'Lời giải Slide 4: f′(1,5) = 2(1,5 − 3) = −3. Do đó x₂ = 1,5 − (1/4)(−3) = 2,25 và f(x₂) = (2,25 − 3)² = 0,5625. Giá trị này nhỏ hơn f(x₁) = 2,25. Để kiểm tra giới hạn của quy tắc, giữ f và x₀ = 0 nhưng thay riêng α bằng 2. Khi đó x₁ = 12, f(x₁) = 81 > 9. Đây là ví dụ bổ sung để bác bỏ phát biểu “mọi bước học dương đều làm hàm giảm”. Không suy từ ví dụ rằng mọi α lớn đều thất bại hoặc mọi α nhỏ đều hội tụ.',
      'α là tham số cập nhật. Nguồn còn có một tham số khác trong bài có ràng buộc.')

slide(6, 'Với h(x) = 0, lập hàm Lagrange',
      'Giải nghĩa ràng buộc đẳng thức và nhận đúng quy ước dấu của ν.',
      ['SRC-03', 'SRC-02'], ['TERM-EQUALITY', 'TERM-LAGRANGE', 'TERM-MULTIPLIER'],
      ['TERM-OBJECTIVE', 'TERM-EQUALITY', 'TERM-LAGRANGE', 'TERM-MULTIPLIER'],
      [eq(r'h(x)=0,\qquad L(x,\nu)=f(x)+\nu h(x)', ['SRC-03']),
       text('Ràng buộc đẳng thức yêu cầu chỉ xét x thỏa h(x) = 0. ν là nhân tử Lagrange.', ['SRC-03'], 'Giải nghĩa đối tượng và ký hiệu mới.'),
       text('Trong quy ước này, ν không bị giới hạn dấu.', ['SRC-03']),
       eq(r'\text{Ví dụ: } h(x)=x-1,\qquad L(x,\nu)=(x-3)^2+\nu(x-1)', ['SRC-03', 'SRC-02'], 'Cụ thể hóa công thức L bằng hàm quen thuộc và một đẳng thức mới.'),
       text('Điều kiện x − 1 = 0 chỉ cho phép x = 1. Bài này chỉ học cách lập L.', ['SRC-03'], 'Giới hạn phạm vi, không mở thêm điều kiện tối ưu nhiều biến.')],
      1.75,
      'Nguồn chuyển sang một bài toán khác: x còn phải thỏa h(x) = 0. Ví dụ x − 1 = 0 chỉ cho phép x = 1. Hàm Lagrange kết hợp hàm mục tiêu với ν lần h(x); ν được gọi là nhân tử Lagrange. Nguồn quy định ν không bị giới hạn dấu cho ràng buộc đẳng thức. Ta giữ đúng quy ước dấu cộng trước νh(x). Ta chưa học điều kiện tìm ν hay cách giải tối ưu có ràng buộc trong buổi này.',
      'Ràng buộc đẳng thức h(x) = 0 giới hạn các giá trị x được phép xét. Hàm Lagrange trong nguồn được định nghĩa bởi L(x,ν) = f(x) + νh(x). ν là nhân tử Lagrange và không bị giới hạn dấu trong quy ước này. Với ví dụ bổ sung h(x) = x − 1 và hàm mục tiêu cũ, L(x,ν) = (x − 3)² + ν(x − 1). Ràng buộc chỉ cho phép x = 1. Khi x thỏa h(x) = 0, số hạng νh(x) bằng 0, nên L(x,ν) = f(x) với mọi ν. Quan sát này là phép thay vào công thức; nó không chọn ν hay chứng minh các điều kiện tối ưu. Bài chỉ giới thiệu cách lập L và quy ước dấu của ν.',
      'Dấu của ν có giống điều kiện αₖ > 0 không?')

slide(7, 'ν = −2 có bị loại vì âm không?',
      'Phân biệt điều kiện αₖ > 0 và quy ước ν không bị giới hạn dấu.',
      ['SRC-01', 'SRC-03'], [], ['TERM-STEP', 'TERM-EQUALITY', 'TERM-LAGRANGE', 'TERM-MULTIPLIER'],
      [eq(r'L(x,\nu)=f(x)+\nu h(x),\qquad h(x)=x-1', ['SRC-03'], 'Nhắc dữ kiện bài tập, h là ví dụ bổ sung.'),
       text('Một bạn viết: “αₖ > 0, nên ν cũng phải > 0.” Suy luận này đúng không?', ['SRC-01', 'SRC-03'], 'Chẩn đoán nhầm hai tham số có vai trò khác nhau.'),
       text('Nếu ν = −2, hãy viết L(x, −2). Có bị loại chỉ vì ν âm không?', ['SRC-03'], 'Cho phép vận dụng trực tiếp quy ước dấu.')],
      1.25,
      'Chờ 25 giây để người học viết một câu giải thích và biểu thức L(x, −2). Cần phân biệt điều kiện đối với bước học αₖ và quy ước đối với nhân tử ν. Không yêu cầu tìm ν tối ưu. Nếu người học nói ν = −2 chắc chắn là nghiệm, nhắc rằng câu hỏi chỉ kiểm tra dấu có được phép hay không.',
      'Tự trả lời trước khi xem Slide 8: αₖ > 0 có kéo theo ν > 0 không? Với h(x) = x − 1 và ν = −2, hãy viết L(x, −2). Đánh giá riêng hai việc: giá trị ν âm có được phép theo quy ước đẳng thức hay không, và bài đã đủ thông tin để khẳng định ν ấy là một nhân tử của nghiệm hay chưa.',
      'Ta sửa suy luận về dấu và nhắc lại việc từng tham số làm.', role='checkpoint',
      checkpoint={'prompt': 'αₖ > 0 có suy ra ν > 0 không? Viết L(x, −2) khi h(x) = x − 1.',
                  'answer': 'Không. ν không bị giới hạn dấu; L(x, −2) = f(x) − 2(x − 1). ν = −2 được phép về dấu, chưa được khẳng định là nhân tử tại nghiệm.',
                  'rationale': 'αₖ điều chỉnh bước cập nhật, ν nhân ràng buộc đẳng thức; nguồn đặt điều kiện dấu riêng.',
                  'anticipated_error': 'Áp điều kiện dương của αₖ cho ν, hoặc coi mọi ν được phép là một nghiệm.',
                  'feedback': 'Đọc lại đối tượng của từng điều kiện dấu. “Được phép về dấu” chưa phải “đã tìm được nhân tử tại nghiệm”.',
                  'answer_placement': 'next_slide', 'answer_slide_id': 'L01-S008',
                  'provenance': 'pedagogical-addition', 'source_unit_ids': ['SRC-01', 'SRC-03'],
                  'provenance_rationale': 'Kiểm tra sự phân biệt giữa bước học và nhân tử trong hai bài toán của nguồn.'})

slide(8, 'Hai tham số có hai vai trò khác nhau',
      'Sửa suy luận sai về dấu và tóm tắt cách thực hiện một bước cập nhật.',
      ['SRC-01', 'SRC-02', 'SRC-03'], [], ['TERM-STEP', 'TERM-GD', 'TERM-EQUALITY', 'TERM-LAGRANGE', 'TERM-MULTIPLIER'],
      [eq(r'L(x,-2)=f(x)-2(x-1)', ['SRC-03'], 'Đáp án bài tập thay ν = −2 vào công thức nguồn với h bổ sung.'),
       block('table', [['Tham số', 'Vai trò', 'Điều kiện dấu trong nguồn'], ['αₖ', 'Điều chỉnh bước cập nhật', 'αₖ > 0'], ['ν', 'Nhân h(x) trong L', 'Không bị giới hạn dấu']], ['SRC-01', 'SRC-03']),
       text('ν = −2 được phép về dấu; ta chưa kết luận đó là nhân tử tại nghiệm.', ['SRC-03'], 'Ngăn việc suy từ miền tham số sang điều kiện tối ưu.'),
       text('Một bước gradient descent: lấy đạo hàm tại xₖ, tính độ dời, tìm xₖ₊₁, rồi kiểm tra giá trị hàm.', ['SRC-01', 'SRC-02'], 'Khép lại thao tác đã học, gồm kiểm tra kết quả thay vì chỉ thay số.')],
      1.5,
      'Suy luận ở trang trước không đúng. αₖ và ν có hai vai trò khác nhau, nên điều kiện dấu của αₖ không chuyển sang ν. Với ν = −2, L(x, −2) = f(x) − 2(x − 1). Giá trị âm được phép về dấu, nhưng chưa có kết luận rằng đây là nhân tử tại nghiệm. Dành 15 giây để người học nói lại quy trình bước cập nhật: đạo hàm tại xₖ, độ dời, điểm mới, kiểm tra f. Nhắc rằng bước học dương vẫn có thể làm f tăng như ví dụ α = 2.',
      'Lời giải Slide 7: từ L(x,ν) = f(x) + νh(x), thay h(x) = x − 1 và ν = −2 được L(x,−2) = f(x) − 2(x − 1). ν không bị giới hạn dấu đối với ràng buộc đẳng thức trong nguồn, nên không loại giá trị −2 chỉ vì nó âm. Điều kiện αₖ > 0 thuộc quy tắc gradient descent, nơi αₖ điều chỉnh bước cập nhật; ν thuộc hàm Lagrange, nơi nó nhân h(x). Bài chưa cung cấp các điều kiện để tìm nhân tử tại nghiệm. Để thực hiện gradient descent một biến, tính f′(xₖ), tính −αₖf′(xₖ), cộng độ dời vào xₖ, rồi kiểm tra f(xₖ₊₁). Kiểm tra bằng ví dụ không thay thế định lý hội tụ.',
      'Kết thúc bài; xem note để tự làm lại hai checkpoint.')

source_units = [
    {'id': 'SRC-01', 'location': 'Nguồn tự viết do người dùng cung cấp, câu 1, không có trang',
     'excerpt': 'Bài toán không ràng buộc: gradient descent cập nhật x_(k+1)=x_k-alpha_k grad f(x_k), alpha_k>0.',
     'priority': 'essential', 'treatment': 'core', 'reason': ''},
    {'id': 'SRC-02', 'location': 'Nguồn tự viết do người dùng cung cấp, câu 2, không có trang',
     'excerpt': 'Ví dụ f(x)=(x-3)^2, x_0=0, alpha=1/4.',
     'priority': 'essential', 'treatment': 'core', 'reason': ''},
    {'id': 'SRC-03', 'location': 'Nguồn tự viết do người dùng cung cấp, câu 3, không có trang',
     'excerpt': 'Một nội dung khác: với ràng buộc đẳng thức h(x)=0, L(x,nu)=f(x)+nu h(x), nu không bị giới hạn dấu.',
     'priority': 'essential', 'treatment': 'core', 'reason': ''}
]
for source in source_units:
    source['slide_ids'] = [s['id'] for s in slides if source['id'] in s['source_unit_ids']]

spec = {
    'skill_version': '6.0.0',
    'config': {'target_language': 'vi-VN', 'delivery_mode': 'live-with-study-companion',
               'course_mode': 'single-lecture', 'aspect_ratio': '16:9', 'assumed_term_ids': ['TERM-DERIVATIVE'],
               'session_minutes': 12, 'primary_format': 'spec-only-by-evaluation-request',
               'render_status': 'not-rendered-user-request', 'visible_footer': 'slide-number'},
    'audience_profile': {'confirmed': 'Sinh viên biết đạo hàm, mới học tối ưu.',
                         'assumptions': ['Biết tính đạo hàm đa thức và xử lý số thực.', 'Chưa yêu cầu kiến thức gradient nhiều biến, KKT hoặc lý thuyết hội tụ.'],
                         'possible_confusions': ['Dùng đạo hàm tại x₀ cho mọi bước.', 'Nhầm độ dời với điểm cập nhật.', 'Suy mọi α > 0 đều làm f giảm.', 'Áp điều kiện αₖ > 0 cho ν.']},
    'learning_objectives': [
        {'id': 'GOAL-01', 'goal': 'Tính một bước gradient descent trong ví dụ một biến và giải thích dấu trừ.', 'source_unit_ids': ['SRC-01', 'SRC-02'], 'evidence': 'Checkpoint Slide 4 và lời giải Slide 5.'},
        {'id': 'GOAL-02', 'goal': 'Nhận ra α > 0 chưa bảo đảm hàm giảm.', 'source_unit_ids': ['SRC-01', 'SRC-02'], 'evidence': 'Đối chiếu f(12) với f(0) ở Slide 5.'},
        {'id': 'GOAL-03', 'goal': 'Lập L với h cụ thể và phân biệt dấu αₖ, ν.', 'source_unit_ids': ['SRC-03'], 'evidence': 'Checkpoint Slide 7 và lời giải Slide 8.'}],
    'lectures': [{'id': 'L01', 'title': 'Một bước gradient descent và quy ước dấu của nhân tử Lagrange', 'session_minutes': 12}],
    'source_units': source_units, 'source_visuals': [],
    'source_visual_inventory_note': 'Nguồn là ba câu văn do người dùng cung cấp; không có hình nguồn.',
    'glossary': [{'id': ident, 'canonical': canonical} for ident, canonical in [
        ('TERM-DERIVATIVE', 'Đạo hàm f′(x)'), ('TERM-OBJECTIVE', 'Hàm mục tiêu f(x)'),
        ('TERM-GRADIENT', 'Gradient ∇f(x)'), ('TERM-ITERATE', 'Giá trị ở bước k: xₖ'),
        ('TERM-STEP', 'Bước học αₖ > 0'), ('TERM-GD', 'Gradient descent'),
        ('TERM-EQUALITY', 'Ràng buộc đẳng thức h(x) = 0'), ('TERM-LAGRANGE', 'Hàm Lagrange L(x,ν)'),
        ('TERM-MULTIPLIER', 'Nhân tử Lagrange ν')]],
    'teaching_contracts': [
        {'kind': 'algorithm', 'slide_ids': [s['id'] for s in slides[:5]],
         'learner_question': 'Đạo hàm cho ta tính điểm mới như thế nào?',
         'decisive_step': 'Lấy đạo hàm tại giá trị hiện tại rồi tính độ dời −αₖf′(xₖ).',
         'must_preserve': ['Bài toán không ràng buộc.', 'αₖ > 0.', 'Dữ kiện f, x₀, α của nguồn.', 'Không khẳng định hội tụ tổng quát.']},
        {'kind': 'definition', 'slide_ids': [s['id'] for s in slides[5:]],
         'learner_question': 'L được lập ra sao và ν có phải dương như αₖ không?',
         'decisive_step': 'Thay h và ν vào L; đọc quy ước dấu riêng cho ràng buộc đẳng thức.',
         'must_preserve': ['h(x) = 0.', 'L = f + νh.', 'ν không bị giới hạn dấu.', 'Không nhầm được phép về dấu với nhân tử tại nghiệm.']}],
    'design_plan': {'status': 'planned-unverified', 'slide_count_rationale': '8 slide tách làm mẫu, câu hỏi và đáp án; 12 phút gồm thời gian chờ.',
                    'palette': {'background': '#F7F5EF', 'text': '#17212B', 'iterate': '#2458A6', 'condition': '#9A4C11'},
                    'layout': 'Công thức theo dòng cho làm mẫu; câu hỏi riêng trang; bảng đối chiếu cho hai tham số.',
                    'math': 'Giữ LaTeX để renderer toán dựng sau; chưa render trong đánh giá.',
                    'fonts': 'Noto Sans và font toán cần được kiểm tra khi render.'},
    'qa_status': {'structure': 'pending-audit', 'render': 'not-performed-by-user-request',
                  'visual_quality': 'unverified', 'learner_outcomes': 'no-student-data'},
    'slides': slides
}

(ROOT / 'course-spec.json').write_text(json.dumps(spec, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

lines = ['# Một bước gradient descent và quy ước dấu của nhân tử Lagrange', '',
         'Bài giảng tiếng Việt 12 phút · 8 slide · phiên bản nội dung 1.0.', '',
         'Người học: sinh viên biết đạo hàm, mới học tối ưu. Phần tính toán chỉ dùng một biến thực. Đây là bản nội dung và đặc tả; chưa phải PDF hoặc bộ slide đã render.', '',
         'Mục tiêu: tính được bước cập nhật, nhận ra giới hạn của điều kiện α > 0, lập L với một h cụ thể và phân biệt quy ước dấu của αₖ và ν.', '',
         'Tự học: đọc phần “Note tự học” theo thứ tự. Với Slide 4 và Slide 7, tự trả lời trước khi mở lời giải ở mục kế tiếp. Phần “Lời giảng” dùng để tổ chức buổi học trực tiếp.', '']
for n, s in enumerate(slides, 1):
    lines.extend([f'<a id="slide-{n}"></a>', f'## Slide {n}: {s["title"]}', '', f'Thời gian dự kiến: {s["estimated_minutes"]:g} phút.', '', '### Chữ trên slide', ''])
    for b in s['body']:
        if b['type'] == 'text':
            lines.extend([b['text'], ''])
        elif b['type'] == 'equation':
            lines.extend(['$$', b['latex'], '$$', ''])
        elif b['type'] == 'table':
            rows = b['rows']
            lines.extend(['| ' + ' | '.join(rows[0]) + ' |', '| ' + ' | '.join(['---'] * len(rows[0])) + ' |'])
            lines.extend('| ' + ' | '.join(row) + ' |' for row in rows[1:])
            lines.append('')
    lines.extend(['### Lời giảng', '', s['speaker_notes'], '', '### Note tự học', '', s['study_text'], '', 'Câu nối: ' + s['next_bridge'], ''])
lines.extend(['## Nguồn và phạm vi bổ sung', '',
              'Nguồn duy nhất là ba câu tự viết do người dùng cung cấp; không có sách, số trang hoặc hình nguồn. SRC-01 là quy tắc cập nhật; SRC-02 là ví dụ; SRC-03 là ràng buộc đẳng thức, L và dấu ν. Tất cả đều có mặt trong tuyến chính.', '',
              'Phần bổ sung sư phạm gồm cách đọc gradient một biến, các phép tính x₁ và x₂, thử α = 2, ví dụ h(x) = x − 1 và hai checkpoint. Các phần này có lý do và liên kết nguồn trong course-spec.json; không gán chúng cho tác giả nguồn.', '',
              'Không mở rộng sang điều kiện tối ưu có ràng buộc, KKT hay định lý hội tụ. Thời gian 12 phút là ước lượng, gồm 35 giây tự tính ở Slide 4, 25 giây ở Slide 7 và 15 giây nhắc lại ở Slide 8.', '',
              '## Giới hạn kiểm tra', '',
              'Không render theo yêu cầu của môi trường đánh giá. Chưa kiểm chứng kích thước chữ, glyph tiếng Việt, font toán, ngắt dòng, tương phản trên output cuối hoặc chất lượng bố cục. Audit cấu trúc không chứng minh hiệu quả học tập hay chất lượng hình thức. Kết quả audit và phép tính được lưu riêng cùng thư mục.', ''])
(ROOT / 'study-note.md').write_text('\n'.join(lines), encoding='utf-8')
print('Created course-spec.json and study-note.md; core time:', sum(s['estimated_minutes'] for s in slides))
