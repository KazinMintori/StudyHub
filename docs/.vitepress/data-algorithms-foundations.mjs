const term = (name, aliases, definition, example, use, question, answer) => ({ name, aliases: [name, ...aliases], definition, example, use, question, answer })

export const dataAlgorithmsConcepts = {
  'pagerank-ca-nhan-hoa': term('PageRank cá nhân hóa', ['personalized PageRank', 'PageRank theo chủ đề'],
    'Phân phối điểm bất động của bước đi trên đồ thị có nhảy lại theo một phân phối ưu tiên. Phải nêu rõ xác suất theo liên kết và cách phân phối lại điểm ở nút cụt. Điểm đo tầm quan trọng theo mô hình này, không tự chứng nhận nội dung đúng.',
    'Nếu bước nhảy chỉ đến trang A thì các trang nhận được điểm qua những đường đi xuất phát từ A. Trang không thể đến được có thể nhận điểm bằng 0.',
    'Xếp hạng theo chủ đề hoặc theo tập trang khởi đầu.',
    'Phân phối nhảy chỉ hỗ trợ một trang có làm mất tính duy nhất của PageRank khi hệ số theo liên kết nhỏ hơn 1 không?',
    'Không. Với ma trận chuyển đã xử lý nút cụt và giữ cố định, phép cập nhật vẫn là ánh xạ co.'),
  'trustrank': term('TrustRank', ['Trust Rank'],
    'Biến thể PageRank cá nhân hóa với phân phối nhảy đặt trên các trang hạt giống được đánh giá đáng tin. Nó lan truyền điểm qua cạnh theo giả thiết các liên kết từ trang đáng tin cung cấp tín hiệu hữu ích. Đây là tín hiệu xếp hạng, không phải một phép kiểm chứng nội dung.',
    'Một trang ngoài tập hạt giống vẫn có điểm TrustRank dương nếu nhận liên kết từ vùng có điểm.',
    'Phân tích và hạn chế tác động của thao túng liên kết.',
    'Một trang có TrustRank thấp có chắc chắn là trang rác không?',
    'Không. Trang có thể chưa được nối tốt với tập hạt giống, hoặc tập hạt giống chưa bao quát chủ đề của trang.'),
  'hits': term('HITS', ['hubs and authorities', 'điểm hub', 'điểm authority'],
    'Thuật toán gán hai loại điểm trên đồ thị liên kết. Điểm authority cộng đóng góp từ các hub trỏ đến trang. Điểm hub cộng điểm authority của các trang mà nó trỏ đến. Các véc tơ được chuẩn hóa trong quá trình lặp.',
    'Một danh mục liên kết có thể là hub tốt, còn trang giải thích chuyên sâu được danh mục trỏ đến có thể là authority tốt.',
    'Phân biệt vai trò dẫn đường với vai trò được tham khảo trong một mạng liên kết.',
    'Ma trận dùng trong HITS có cần chia mỗi cột theo bậc ra như PageRank không?',
    'Không. HITS cơ bản dùng ma trận kề, rồi chuẩn hóa các véc tơ điểm. Đó là mô hình khác với bước đi xác suất của PageRank.'),
  'shingling': term('Shingling', ['shingle', 'tập shingle'],
    'Cách biểu diễn văn bản bằng tập các đoạn liên tiếp có cùng độ dài, tính theo ký tự hoặc từ đã quy định. Chuẩn hóa văn bản và chọn đơn vị phải được thực hiện nhất quán trước khi lập tập. Dạng tập không giữ số lần lặp của một đoạn.',
    'Với shingle 2 ký tự, văn bản ababa cho tập {ab, ba}. Đoạn ab xuất hiện hai lần nhưng chỉ có một phần tử trong tập.',
    'Biểu diễn các mẫu cục bộ để so sánh tài liệu gần trùng.',
    'Hai văn bản có cùng tập shingle có nhất thiết là cùng chuỗi không?',
    'Không. Phép lập tập có thể làm mất tần suất và thông tin về thứ tự tổng thể.'),
  'jaccard': term('Độ tương đồng Jaccard', ['Jaccard', 'Jaccard similarity'],
    'Với hai tập có hợp khác rỗng, độ tương đồng Jaccard là kích thước giao chia kích thước hợp. Giá trị nằm từ 0 đến 1. Hai tập cùng rỗng cần một quy ước riêng, chẳng hạn gán độ tương đồng bằng 1.',
    'Hai tập {a, b, c, d} và {b, c, d, e} có giao gồm 3 phần tử, hợp gồm 5 phần tử, nên độ tương đồng bằng 3/5.',
    'So sánh độ trùng của hai tập shingle, tập từ hoặc tập mục.',
    'Jaccard bằng 1 có chứng minh hai văn bản gốc giống hệt nhau không?',
    'Không. Nó chứng minh hai tập biểu diễn bằng nhau. Phép biểu diễn có thể đã bỏ mất thông tin của văn bản gốc.'),
  'minhash': term('MinHash', ['MinHash signature', 'chữ ký MinHash'],
    'Với một hoán vị của vũ trụ phần tử, MinHash của tập khác rỗng là phần tử đầu tiên của tập theo thứ tự đó. Nếu hoán vị được chọn đều ngẫu nhiên và dùng chung cho hai tập, xác suất hai MinHash trùng nhau đúng bằng độ tương đồng Jaccard.',
    'Hai tập có Jaccard bằng 3/5 sẽ cho MinHash trùng nhau với xác suất 3/5 trong mô hình hoán vị ngẫu nhiên đều.',
    'Nén tập thành chữ ký để ước lượng Jaccard và tạo ứng viên tìm kiếm tương đồng.',
    'Một hàm băm bất kỳ có tự động bảo đảm định lý MinHash chính xác không?',
    'Không. Định lý phát biểu cho hoán vị ngẫu nhiên đều. Các họ băm thực dụng cần được xem xét về sai lệch, tính độc lập và va chạm.'),
  'lsh': term('Băm nhạy cảm cục bộ', ['LSH', 'locality-sensitive hashing'],
    'Họ hàm băm ngẫu nhiên có xác suất va chạm cao hơn cho các đối tượng gần nhau theo một độ đo đã chọn. Nó giúp tìm ứng viên để xác minh tiếp, với khả năng có ứng viên sai và bỏ sót. Họ băm phải phù hợp với độ đo.',
    'Trong LSH cho chữ ký MinHash, hai tài liệu là ứng viên nếu trùng toàn bộ các hàng trong ít nhất một dải.',
    'Giảm số cặp cần so sánh chính xác trong bài toán tìm tương đồng.',
    'Mốc gần đúng của đường cong LSH có phải ngưỡng bảo đảm mọi cặp phía trên đều được giữ không?',
    'Không. Xác suất thay đổi liên tục theo độ tương đồng. Ngưỡng quyết định kết quả được áp dụng riêng ở bước xác minh.'),
  'phan-dai-minhash': term('Phân dải MinHash', ['banding', 'phân dải chữ ký'],
    'Chia chữ ký thành các dải có cùng số hàng. Hai chữ ký khớp một dải khi mọi hàng trong dải đó bằng nhau. Cặp được tạo ứng viên nếu khớp ít nhất một dải. Mô hình xác suất chuẩn giả sử các hàng độc lập và không có va chạm phụ của bộ băm dải.',
    'Chữ ký 100 hàng có thể chia thành 20 dải, mỗi dải 5 hàng, hoặc 10 dải, mỗi dải 10 hàng. Hai cách cho xác suất ứng viên khác nhau.',
    'Điều chỉnh mức đánh đổi giữa số ứng viên và nguy cơ bỏ sót.',
    'Tăng số hàng mỗi dải và giữ số dải cố định làm xác suất ứng viên tăng hay giảm?',
    'Nó giảm hoặc giữ nguyên vì việc khớp toàn bộ một dải đòi hỏi nhiều điều kiện đồng thời hơn.')
}

export const dataAlgorithmsWikiDetails = {
  'pagerank-ca-nhan-hoa': String.raw`Giữ quy ước cột nguồn. Gọi $S$ là ma trận chuyển không âm có tổng mỗi cột bằng 1, sau khi đã xử lý nút cụt. Gọi $v$ là véc tơ xác suất nhảy và $0\le\beta<1$. Phép cập nhật là $F(x)=\beta Sx+(1-\beta)v$.

Với hai véc tơ, khoảng cách theo chuẩn tổng trị tuyệt đối sau cập nhật không vượt quá $\beta$ lần khoảng cách trước cập nhật. Do đó có duy nhất điểm bất động, kể cả khi một số phần tử của $v$ bằng 0. Điều này không có nghĩa mọi trang nhận điểm dương hoặc chuỗi Markov bất khả quy.

Nếu giữ nguyên $S$ và $\beta$, nghiệm phụ thuộc tuyến tính vào $v$. Có thể trộn các véc tơ điểm chủ đề bằng cùng trọng số dùng để trộn phân phối nhảy. Nếu quy tắc nút cụt cũng thay theo $v$, cần xét lại điều kiện giữ nguyên $S$.`,
  'trustrank': String.raw`Tập hạt giống và trọng số nhảy là dữ kiện đầu vào của mô hình. Chúng cần được đánh giá độc lập với kết quả xếp hạng. Điểm TrustRank thấp có thể phản ánh khoảng cách đến hạt giống hoặc sự thiếu bao phủ, nên không đủ để kết luận một trang là rác.

Khi so sánh PageRank thông thường $r_i>0$ và TrustRank $t_i$, chỉ số spam mass là $1-t_i/r_i$. Chỉ số này có thể âm khi $t_i>r_i$. Nó không phải xác suất nhãn rác. Muốn diễn giải phép so sánh, phải ghi rõ đồ thị, hệ số theo liên kết, chuẩn hóa và cách xử lý nút cụt của hai lần tính.`,
  'hits': String.raw`Đặt $L_{ij}=1$ khi trang $i$ trỏ đến trang $j$. Một bước HITS tính véc tơ authority từ $L^T h$, chuẩn hóa, rồi tính véc tơ hub từ $La$ và chuẩn hóa. Với quy ước này, hàng của $L$ là trang nguồn, khác cách đánh chỉ số ma trận chuyển theo cột của PageRank.

Kết hợp hai phép cập nhật cho thấy authority gắn với $L^TL$ và hub gắn với $LL^T$. Hai véc tơ tương ứng với các véc tơ kỳ dị phải và trái của $L$. Nếu trị kỳ dị lớn nhất không đơn thì không thể khẳng định có một hướng điểm trội duy nhất độc lập khởi tạo. Ma trận toàn 0 làm bước chuẩn hóa mất nghĩa và cần được xử lý riêng.`,
  'shingling': String.raw`Trước khi lập shingle, phải xác định chuẩn Unicode, cách xử lý chữ hoa, dấu câu, khoảng trắng và việc tách từ. Mỗi lựa chọn thay đổi bài toán tương đồng. Không có một độ dài shingle phù hợp với mọi loại tài liệu.

Biểu diễn tập chỉ ghi nhận một đoạn có xuất hiện hay không. Nếu cần dùng tần suất thì phải thay cả mô hình biểu diễn lẫn độ đo tương ứng. Khi văn bản ngắn hơn độ dài shingle, tập nhận được rỗng. Trường hợp này cần được xử lý trước khi tạo chữ ký MinHash.`,
  'jaccard': String.raw`Đặt $c=|A\cap B|$ là số phần tử chung và $u=|A\cup B|$ là số phần tử thuộc ít nhất một tập. Khi $u>0$, độ tương đồng là $J(A,B)=c/u$. Khoảng cách Jaccard là $d_J(A,B)=1-J(A,B)$.

Nếu dùng quy ước $J(\varnothing,\varnothing)=1$, khoảng cách giữa hai tập rỗng bằng 0. Với một tập rỗng và một tập khác rỗng, độ tương đồng bằng 0. Jaccard so sánh tập đã biểu diễn, không trực tiếp đo nghĩa văn bản hoặc chứng minh quan hệ sao chép.`,
  'minhash': String.raw`Phần tử nhỏ nhất của $A\cup B$ theo một hoán vị ngẫu nhiên đều có khả năng như nhau là bất kỳ phần tử nào trong hợp. Hai MinHash bằng nhau đúng khi phần tử này thuộc giao. Vì thế xác suất va chạm bằng kích thước giao chia kích thước hợp.

Với $k$ hoán vị độc lập, gọi $I_i$ bằng 1 khi hàng thứ $i$ trùng nhau và bằng 0 nếu không. Trung bình $(I_1+I_2+\cdots+I_k)/k$ là ước lượng không chệch của Jaccard. Nếu $s$ là Jaccard thật, phương sai của trung bình là $s(1-s)/k$. Một chữ ký hữu hạn vẫn có sai số.`,
  'lsh': String.raw`Họ băm phải được chọn theo độ đo của đối tượng. MinHash có xác suất va chạm bằng Jaccard cho tập khác rỗng. Băm bằng dấu của tích vô hướng với một hướng ngẫu nhiên đẳng hướng cho các véc tơ khác 0 có xác suất va chạm phụ thuộc góc, không trực tiếp bằng Jaccard.

LSH là bước lọc ứng viên. Bước xác minh bằng độ đo chính xác loại được ứng viên không đạt ngưỡng, nhưng không khôi phục được các cặp đã bị bộ lọc bỏ sót. Khi có một thùng băm rất lớn, số cặp trong thùng vẫn có thể tăng theo bình phương kích thước thùng.`,
  'phan-dai-minhash': String.raw`Gọi $b$ là số dải và $r$ là số hàng trong một dải. Với các hàng MinHash độc lập và hai tập có Jaccard $s$, xác suất một dải khớp là $s^r$. Xác suất thành ứng viên là $p(s)=1-(1-s^r)^b$.

Mốc xác suất bằng một nửa là nghiệm của $p(s)=1/2$. Nó không trùng với mốc gần đúng $b^{-1/r}$. Khi tăng $b$ mà giữ $r$, xác suất giữ cặp tăng nhưng chữ ký cũng dài thêm. Khi giữ tổng số hàng, phải xét đồng thời thay đổi của cả hai tham số.`
}

export const dataAlgorithmsWikiConnections = {
  'pagerank-ca-nhan-hoa': ['trustrank', 'do-thi', 'ma-tran'],
  'trustrank': ['pagerank-ca-nhan-hoa', 'hits'],
  'hits': ['ma-tran', 'tri-rieng', 'do-thi'],
  'shingling': ['jaccard', 'minhash'],
  'jaccard': ['shingling', 'minhash', 'lsh'],
  'minhash': ['jaccard', 'doc-lap', 'phan-dai-minhash'],
  'lsh': ['minhash', 'phan-dai-minhash', 'bam'],
  'phan-dai-minhash': ['minhash', 'lsh', 'doc-lap']
}
