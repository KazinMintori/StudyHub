const lesson = (number, slug, title, prerequisites) => ({ number, slug, title, prerequisites, status: 'ready' })
const slide = (note, title, bullets, formula = '', example = '') => ({ note, title, bullets, formula, example })
const slugs = ['bai-00-on-tap-nen-tang', 'bai-01-nhap-mon-toi-uu', 'bai-02-tap-loi', 'bai-03-doi-ngau-lagrange', 'bai-04-gradient-newton', 'bai-05-toi-uu-huan-luyen', 'bai-06-phuong-phap-thich-nghi', 'bai-07-quy-hoach-tuyen-tinh-va-dong']
const titles = ['Ôn tập nền tảng toán học cho AI', 'Giới thiệu tối ưu, tập lồi và hàm lồi', 'Các bài toán tối ưu lồi', 'Đối ngẫu Lagrange', 'Tối ưu không ràng buộc và ràng buộc đẳng thức', 'Các phương pháp tối ưu trong huấn luyện mô hình học sâu', 'Các phương pháp tối ưu trong học sâu', 'Quy hoạch tuyến tính và quy hoạch động']
const prerequisites = [
  ['ham-so', 'dao-ham', 'tap-hop'],
  ['vector', 'tich-vo-huong', 'gradient', 'hessian', 'ma-tran-psd'],
  ['tap-loi', 'ham-loi', 'chuan', 'ma-tran-psd'],
  ['ham-loi', 'gradient', 'he-phuong-trinh'],
  ['gradient', 'hessian', 'ma-tran-psd', 'he-phuong-trinh', 'kkt'],
  ['gradient', 'quy-tac-chuoi', 'ky-vong', 'phuong-sai'],
  ['gradient', 'hessian', 'ky-vong', 'phuong-sai'],
  ['ma-tran', 'he-phuong-trinh', 'tap-loi', 'do-thi']
]
const descriptions = [
  'Đọc kích thước ma trận, tính gradient và Hessian; nối mô hình nhiễu Gauss với bình phương tối thiểu.',
  'Lập bài toán, kiểm tra đoạn nối trong tập và dây cung của hàm; giải thích điều kiện tối ưu toàn cục.',
  'Nhận diện LP, QP, SOCP, SDP và GP; phân biệt cải dạng tương đương, xấp xỉ và nới lỏng.',
  'Tạo cận dưới từ Lagrangian, tính hàm đối ngẫu và dùng Slater, KKT để chứng nhận nghiệm.',
  'Theo dõi từng bước gradient, backtracking và Newton; giải hệ Newton–KKT khi có ràng buộc đẳng thức.',
  'Từ gradient toàn bộ dữ liệu đến lô nhỏ, momentum, Nesterov và khởi tạo trọng số.',
  'Tính từng trạng thái AdaGrad, RMSProp và Adam; đối chiếu với phương pháp dùng độ cong.',
  'Tìm nghiệm cơ sở của LP và tính Bellman ngược thời gian trên bài toán hữu hạn tất định.'
]
export const mathAiCourse = {
  id: 'toan-cho-ai', code: '02', name: 'Cơ sở toán cho AI', short: 'Toán cho AI', current: true,
  description: 'Tám lecture từ nền tảng đến tối ưu lồi và huấn luyện mô hình: đọc từng bước, thử mô phỏng, rồi tự giải bài tập.',
  foundations: ['tap-hop', 'ham-so', 'vector', 'ma-tran', 'tich-vo-huong', 'chuan', 'dao-ham', 'dao-ham-rieng', 'gradient', 'hessian', 'ma-tran-psd', 'he-phuong-trinh', 'ham-loi', 'tap-loi', 'quy-tac-chuoi', 'ky-vong', 'phuong-sai', 'kkt'],
  structureSource: 'https://courses.iaidev.com/math-4-AI/2627-1/',
  parts: [{ title: 'Bài giảng · Lecture 00–07', lessons: slugs }],
  lessons: titles.map((title, i) => ({ ...lesson(i, slugs[i], title, prerequisites[i]), description: descriptions[i] })),
  slides: [
    slide(slugs[0], 'Ma trận biến nhiều dự đoán thành một phép nhân', ['Với A kích thước m×n và w có n phần tử, Aw có m phần tử.', 'Một hàng của A tương ứng một quan sát; một cột tương ứng một đặc trưng.', 'Phần dư r=Aw−b đo sai lệch của từng dự đoán.'], 'A: m×n; w: n×1; r: m×1', 'A=[1;2;3], b=[1;2;2]: w=11/14 cho dự đoán [11/14;11/7;33/14].'),
    slide(slugs[0], 'Gradient mô tả bậc nhất, Hessian mô tả độ cong', ['Gradient của f là vector các đạo hàm riêng tại điểm khả vi.', 'Hessian của f là ma trận đạo hàm bậc hai.', 'Ma trận đối xứng PSD thỏa vᵀHv≥0 với mọi v; không kiểm PSD bằng dấu từng phần tử.'], 'f(w)=½‖Aw−b‖²; ∇f=Aᵀ(Aw−b); H=AᵀA'),
    slide(slugs[0], 'Nhiễu Gauss dẫn tới bình phương tối thiểu', ['Giả sử các nhiễu độc lập, cùng phương sai σ²>0.', 'Lấy âm log biến tích mật độ thành tổng bình phương phần dư cộng một hằng số.', 'Khi σ² cố định, cực đại likelihood theo w tương đương cực tiểu tổng bình phương phần dư.'], '−log p(b|w)=hằng số + ‖Aw−b‖²/(2σ²)'),
    slide(slugs[1], 'Trước khi tìm nghiệm, hãy kiểm tra miền khả thi', ['Biến quyết định khác dữ liệu cố định của bài toán.', 'Nghiệm phải khả thi và cho giá trị không lớn hơn mọi điểm khả thi khác.', 'Cận dưới hữu hạn không bảo đảm có điểm đạt cận đó.'], 'p* = inf{x∈C} f(x)', 'min x với x>0 có p*=0 nhưng không có nghiệm tối ưu.'),
    slide(slugs[1], 'Tập lồi giữ đoạn nối, hàm lồi nằm dưới dây cung', ['Kiểm tập lồi bằng mọi cặp điểm và mọi trọng số θ trong [0,1].', 'Kiểm hàm lồi bằng miền lồi và bất đẳng thức dây cung.', 'Đồ thị hàm lồi thường không phải tập lồi; epigraph mới là tập lồi.'], 'f(θx+(1−θ)y) ≤ θf(x)+(1−θ)f(y)'),
    slide(slugs[1], 'Một mặt phẳng tiếp tuyến có thể chứng nhận nghiệm', ['Với f khả vi, lồi trên miền mở lồi, xấp xỉ bậc nhất là cận dưới toàn cục.', 'Không ràng buộc: gradient bằng 0 đủ để tối ưu.', 'Có ràng buộc: phải so hướng gradient với các điểm khả thi.'], 'f(y) ≥ f(x)+∇f(x)ᵀ(y−x)', 'min (x−2)² với x≤1 đạt tại 1; đạo hàm tại đó bằng −2.'),
    slide(slugs[1], 'Tính lồi không tự tạo tính duy nhất', ['Tối ưu cục bộ của bài toán lồi là tối ưu toàn cục.', 'Lồi nghiêm trên miền khả thi lồi bảo đảm nhiều nhất một nghiệm.', 'Vẫn cần xét khả thi, bị chặn dưới và đạt nghiệm.']),
    slide(slugs[1], 'Mô hình điều khiển tuyến tính tạo mục tiêu toàn phương', ['Trạng thái hiện tại và đích là dữ liệu; hành động là biến cần chọn.', 'Bình phương sai lệch cộng điều chuẩn có Hessian PSD.', 'Giới hạn affine của hành động giữ miền khả thi lồi.'], 'f(u)=½‖Fs+Bu−r‖²+ρ‖u‖²/2, ρ≥0'),
    slide(slugs[1], 'Hồi quy logistic có loss lồi theo tham số', ['Điểm số aᵀw affine theo tham số, dù xác suất sigmoid phi tuyến.', 'Hessian từng loss là p(1−p)aaᵀ PSD.', 'Dữ liệu tách được có thể làm loss tiến về cận mà không đạt ở tham số hữu hạn.'], 'ℓ(w)=log(1+exp(aᵀw))−b aᵀw, b∈{0,1}'),
    slide(slugs[2], 'Dấu bất đẳng thức là một phần của chứng nhận tính lồi', ['Dạng chuẩn dùng fᵢ(x)≤0 với các fᵢ lồi.', 'Các đẳng thức phải affine.', 'Một biểu thức chưa đúng dạng chuẩn có thể có cải dạng tương đương lồi.'], 'min f₀(x); fᵢ(x)≤0; Ax=b'),
    slide(slugs[2], 'LP, QP và các nón là cách mô tả cấu trúc', ['LP dùng mục tiêu và ràng buộc affine.', 'QP dùng mục tiêu toàn phương PSD và ràng buộc affine.', 'SOCP dùng chuẩn Euclid; SDP dùng bất đẳng thức ma trận PSD.'], 'QP: min ½xᵀPx+qᵀx, P⪰0'),
    slide(slugs[2], 'Biến phụ có thể loại bỏ max và trị tuyệt đối', ['min maxᵢ fᵢ(x) tương đương min t với fᵢ(x)≤t.', 'Ràng buộc |u|≤t tương đương u≤t và −u≤t.', 'Phải chỉ ra cách thu hồi x và giá trị tối ưu sau cải dạng.'], 'min ‖Ax−b‖∞ ⇔ min t, −t1≤Ax−b≤t1'),
    slide(slugs[2], 'Nới lỏng cho cận; xấp xỉ đổi bài toán', ['Nới lỏng mở rộng miền khả thi và tạo cận dưới cho bài min.', 'Nghiệm nới lỏng có thể không khả thi cho bài gốc.', 'Xấp xỉ mục tiêu không tự cho cận nếu chưa chứng minh quan hệ giữa hai hàm.']),
    slide(slugs[3], 'Vì sao nhân tử bất đẳng thức phải không âm?', ['Tại điểm khả thi, λᵢfᵢ(x)≤0 khi λᵢ≥0.', 'Infimum của Lagrangian không lớn hơn giá trị tại điểm khả thi.', 'Suy ra g(λ,ν) là cận dưới kể cả khi bài gốc không lồi.'], 'g(λ,ν)=infₓ L(x,λ,ν) ≤ p*'),
    slide(slugs[3], 'Tính đối ngẫu bằng cách tối ưu theo x trước', ['Giữ nhân tử cố định, rồi lấy infimum theo x trong miền xác định.', 'Sau đó mới cực đại g theo các nhân tử khả thi.', 'Hàm g lõm vì là infimum của các hàm affine theo nhân tử.'], 'min (x−2)², x≤1: g(λ)=λ−λ²/4, λ≥0', 'λ*=2, x*=1; g(2)=f(1)=1.'),
    slide(slugs[3], 'Slater đủ cho đối ngẫu mạnh trong bài toán lồi', ['Slater tìm một điểm thuộc nội tương đối của miền chung, thỏa đẳng thức và thỏa chặt các bất đẳng thức.', 'Đối ngẫu mạnh là d*=p*.', 'KKT đủ trong bài toán lồi khả vi; với Slater và nghiệm đạt, KKT cũng cần.']),
    slide(slugs[3], 'KKT và khoảng cách đối ngẫu chứng nhận nghiệm', ['Kiểm khả thi gốc, dấu nhân tử, bù trừ và dừng.', 'Một nhân tử bằng 0 không cho biết ràng buộc có chặt hay không.', 'Nếu x và nhân tử đều khả thi, f(x)−g là cận trên cho độ thiếu tối ưu.'], '0 ≤ f(x)−p* ≤ f(x)−g(λ,ν)'),
    slide(slugs[4], 'Hướng giảm và độ dài bước là hai quyết định', ['Hướng d giảm cục bộ khi ∇fᵀd<0.', 'Backtracking thu nhỏ t cho đến khi ở trong miền và giảm đủ.', 'Hướng đúng vẫn có thể làm f tăng nếu chọn bước quá lớn.'], 'f(x+td) ≤ f(x)+αt∇fᵀd, 0<α<½, 0<β<1'),
    slide(slugs[4], 'Newton tối ưu mô hình toàn phương tại điểm hiện tại', ['Tính g và H rồi giải Hd=−g, thay vì lập H⁻¹.', 'H dương xác định bảo đảm hướng Newton là hướng giảm khi g khác 0.', 'Bài toàn phương dương xác định đến nghiệm sau một bước Newton đầy đủ.'], 'g+Hd=0'),
    slide(slugs[4], 'Hệ Newton–KKT giữ ràng buộc đẳng thức', ['Nếu Ax=b, hướng phải thỏa Ad=0.', 'Từ điểm chưa khả thi, vế phải khối dưới là b−Ax.', 'Tìm bước từ hệ tuyến tính; với khởi đầu chưa khả thi, tìm kiếm theo chuẩn phần dư KKT.'], '[H Aᵀ; A 0][d; Δν]=−[∇f+Aᵀν; Ax−b]'),
    slide(slugs[4], 'Tự tương hợp kiểm soát biến thiên độ cong', ['Một chiều: |f‴|≤2(f″)³ᐟ² trên miền.', 'Nhiều chiều: xét cùng điều kiện trên mọi đường thẳng trong miền.', 'Đây là giả thiết cho phân tích Newton, không có nghĩa mọi hàm lồi đều thỏa.'], 'f(x)=−log x, x>0: hai vế bằng 2/x³'),
    slide(slugs[5], 'Lô nhỏ ước lượng gradient toàn bộ dữ liệu', ['Mục tiêu huấn luyện là trung bình loss trên tập train.', 'Lấy mẫu đều cho gradient lô nhỏ không chệch tại tham số đang cố định.', 'Một bước SGD có thể tăng loss toàn bộ tập; giảm train loss không bảo đảm giảm validation loss.'], 'gᴮ=(1/|B|)∑ᵢ∈B ∇ℓᵢ(θ)'),
    slide(slugs[5], 'Momentum giữ thông tin từ các bước trước', ['Vận tốc v tích lũy hướng cập nhật.', 'Nesterov tính gradient tại điểm nhìn trước θ+μv.', 'Phải thống nhất quy ước dấu và khởi tạo v=0.'], 'v⁺=μv−ηg; θ⁺=θ+v⁺'),
    slide(slugs[5], 'Khởi tạo phải phá đối xứng và kiểm soát phương sai', ['Các neuron cùng cấu trúc với trọng số giống nhau có thể nhận gradient giống nhau.', 'Glorot cân bằng thang truyền tín hiệu dưới giả định của mô hình tuyến tính hóa.', 'Giá trị fan-in và fan-out đếm số đầu vào và đầu ra của tầng.'], 'Var(W)=2/(fan-in+fan-out)', 'fan-in=4, fan-out=2: uniform trên [−1,1] có phương sai 1/3.'),
    slide(slugs[6], 'AdaGrad và RMSProp thay thang cập nhật từng tọa độ', ['AdaGrad cộng dồn bình phương gradient từ đầu.', 'RMSProp dùng trung bình mũ để giảm ảnh hưởng các bước xa.', 'Các phép bình phương, căn và chia được thực hiện theo từng phần tử.'], 'AdaGrad: s⁺=s+g²; θ⁺=θ−ηg/(√s⁺+ε)'),
    slide(slugs[6], 'Adam dùng hai trạng thái và hiệu chỉnh khởi đầu', ['m theo dõi trung bình mũ của gradient.', 'v theo dõi trung bình mũ của bình phương gradient.', 'Chia cho 1−βᵗ để hiệu chỉnh trạng thái khởi tạo bằng 0.'], 'θ⁺=θ−η m̂/(√v̂+ε)', 'g₁=2, β₁=0.9, β₂=0.999: m̂₁=2 và v̂₁=4.'),
    slide(slugs[6], 'Độ cong còn có thể được dùng bằng hệ tuyến tính', ['Newton cần Hessian hoặc cách giải hệ tương ứng.', 'Gradient liên hợp giải hệ SPD bằng các hướng liên hợp.', 'BFGS cập nhật xấp xỉ Hessian nghịch đảo; điều kiện yᵀs>0 giữ tính dương xác định.']),
    slide(slugs[6], 'So phương pháp phải giữ cùng điều kiện thử nghiệm', ['Giữ cùng dữ liệu, khởi tạo, ngân sách và seed khi đối chiếu.', 'Báo train loss, validation loss và thời gian riêng.', 'Mô phỏng toàn phương hai chiều chỉ minh họa cập nhật; không xếp hạng cho mạng sâu.']),
    slide(slugs[7], 'LP đưa hàm tuyến tính lên đa diện', ['Dạng chuẩn là min cᵀx với Ax=b, x≥0.', 'Nghiệm cơ sở lấy các cột độc lập rồi đặt biến còn lại bằng 0.', 'Có đỉnh và giá trị tối ưu hữu hạn thì có một đỉnh tối ưu.'], 'xᴮ=Aᴮ⁻¹b ≥0', 'max 3x+2y, x+y≤4, x≤2, x,y≥0: tối ưu (2,2), giá trị 10.'),
    slide(slugs[7], 'Bellman ghép chi phí hiện tại với phần còn lại', ['Trạng thái phải chứa thông tin đủ để xác định các lựa chọn về sau.', 'Với thời hạn hữu hạn tất định, tính từ trạng thái cuối rồi đi ngược.', 'Lưu cả giá trị tối ưu và hành động đạt giá trị đó.'], 'Vₜ(s)=minₐ{cₜ(s,a)+Vₜ₊₁(Tₜ(s,a))}'),
    slide(slugs[7], 'LP và quy hoạch động có thể mô tả cùng một bài đường đi', ['DP dùng đệ quy theo cấu trúc thời gian hoặc DAG.', 'LP có thể dùng biến luồng hoặc các bất đẳng thức tiềm năng.', 'Có chu trình cần xử lý khác; đệ quy ngược trên DAG không áp dụng trực tiếp.'], 'V(T)=0; V(S)=min{c(S,u)+V(u)}', 'S→A:1, S→B:4, A→T:5, A→B:2, B→T:1: đường S→A→B→T có chi phí 4.')
  ], illustration: 'gradient'
}
