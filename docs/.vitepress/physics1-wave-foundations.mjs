export const physics1WaveConcepts={
  "song-co-hoc": {
    "name": "Sóng cơ học",
    "aliases": [
      "sóng cơ học",
      "sóng cơ"
    ],
    "definition": "Nhiễu loạn truyền trong môi trường vật chất nhờ tương tác giữa các phần môi trường. Chuyển động phần tử và chiều truyền nhiễu loạn là hai điều cần phân biệt.",
    "example": "Trên dây, một điểm có thể dao động lên xuống trong khi hình dạng sóng truyền dọc dây.",
    "use": "Xác định môi trường, phương dao động và phương truyền trước khi chọn mô hình sóng.",
    "question": "Tốc độ truyền sóng có luôn bằng tốc độ chuyển động của một phần tử môi trường không?",
    "answer": "Không. Tốc độ truyền mô tả sự chuyển vị trí của nhiễu loạn, còn vận tốc phần tử là đạo hàm li độ theo thời gian ở một vị trí cân bằng."
  },
  "buoc-song-co-hoc": {
    "name": "Bước sóng cơ học",
    "aliases": [
      "bước sóng cơ học",
      "bước sóng của sóng cơ"
    ],
    "definition": "Khoảng cách giữa hai điểm liên tiếp cùng pha của sóng tuần hoàn. Với tốc độ pha $v$ và tần số $f>0$, bước sóng là $\\lambda=v/f$.",
    "example": "Hai đỉnh kề nhau của một sóng sin cách nhau một bước sóng. Hai vị trí bất kỳ đang cùng li độ chưa chắc cùng pha.",
    "use": "Đổi giữa cấu trúc không gian và nhịp dao động theo thời gian của sóng tuần hoàn.",
    "question": "Hai vị trí có cùng li độ tại một thời điểm đã đủ kết luận cách nhau một bước sóng chưa?",
    "answer": "Chưa. Trong một bước sóng có thể có hai vị trí cùng li độ nhưng vận tốc dao động trái dấu. Bước sóng nối hai điểm cùng pha liên tiếp."
  },
  "so-song": {
    "name": "Số sóng",
    "aliases": [
      "số sóng",
      "số sóng góc"
    ],
    "definition": "Độ biến thiên pha theo vị trí trong một sóng sin. Quy ước số sóng góc là $k=2\\pi/\\lambda$, có đơn vị rad/m.",
    "example": "Đi dọc chiều dài một bước sóng làm pha không gian tăng $2\\pi$ radian.",
    "use": "Viết pha, xác định bước sóng và liên hệ tốc độ truyền với tần số góc.",
    "question": "Số sóng k có đơn vị giống tần số góc không?",
    "answer": "Không. k có đơn vị rad/m, còn tần số góc có đơn vị rad/s. Tỷ số của tần số góc với k cho tốc độ truyền."
  },
  "ham-song-co-hoc": {
    "name": "Hàm sóng cơ học",
    "aliases": [
      "hàm sóng cơ học",
      "hàm li độ sóng"
    ],
    "definition": "Hàm y(x,t) mô tả li độ phần tử có vị trí cân bằng x tại thời điểm t. Đọc theo x cho dạng tức thời, còn đọc theo t cho dao động tại một vị trí.",
    "example": "Trong $y=A\\cos(kx-\\omega t)$ với k và tần số góc dương, một điểm pha không đổi chuyển về phía x tăng.",
    "use": "Tính li độ, vận tốc, gia tốc phần tử và xác định chiều truyền từ pha.",
    "question": "Lấy đạo hàm theo thời gian của y(x,t) có cho tốc độ truyền sóng không?",
    "answer": "Không. Đạo hàm đó cho vận tốc dao động của phần tử tại vị trí x cố định. Tốc độ truyền của sóng sin là tỷ số của tần số góc với số sóng."
  },
  "toc-do-song-ngang-tren-day": {
    "name": "Tốc độ sóng ngang trên dây",
    "aliases": [
      "tốc độ sóng ngang trên dây",
      "tốc độ truyền sóng trên dây"
    ],
    "definition": "Trong mô hình dây mềm đồng nhất, lực căng gần đều và độ dốc nhỏ, tốc độ sóng ngang là $v=\\sqrt{F/\\mu}$, với $\\mu$ là khối lượng riêng dài.",
    "example": "Cùng dây và chiều dài, tăng lực căng bốn lần làm tốc độ truyền tăng hai lần trong mô hình này.",
    "use": "Liên hệ tính đàn hồi phục hồi của dây với quán tính khi tính bước sóng hoặc tần số riêng.",
    "question": "Có thể bỏ khối lượng riêng dài vì đang bỏ trọng lượng dây khi tính lực căng không?",
    "answer": "Không. Bỏ trọng lượng trong phép tính lực căng không loại bỏ khối lượng quán tính của dây. Sóng vẫn cần $\\mu$ để xác định gia tốc phần tử."
  },
  "cong-suat-song-co": {
    "name": "Công suất sóng cơ",
    "aliases": [
      "công suất sóng cơ",
      "công suất của sóng trên dây"
    ],
    "definition": "Tốc độ năng lượng truyền qua một tiết diện. Với sóng chạy hình sin trên dây lý tưởng, công suất trung bình tỉ lệ bình phương biên độ li độ và bình phương tần số khi tính chất dây giữ nguyên.",
    "example": "Giảm biên độ li độ xuống một phần mười ở cùng tần số làm công suất trung bình còn một phần một trăm.",
    "use": "Tính năng lượng truyền mỗi giây và phân biệt công suất tức thời với trung bình.",
    "question": "Trong sóng dừng lý tưởng, công suất tức thời qua mọi điểm có luôn bằng không không?",
    "answer": "Không. Công suất tức thời có thể đổi dấu khi năng lượng trao đổi cục bộ, còn giá trị trung bình qua mọi điểm bằng không."
  },
  "cuong-do-song-co": {
    "name": "Cường độ sóng cơ",
    "aliases": [
      "cường độ sóng cơ",
      "cường độ sóng âm"
    ],
    "definition": "Công suất trung bình truyền qua một đơn vị diện tích vuông góc chiều truyền. Đơn vị SI là $\\mathrm{W/m^2}$. Công suất toàn phần và cường độ là hai đại lượng khác nhau.",
    "example": "Với nguồn phát đều mọi hướng và không hấp thụ, xa nguồn gấp đôi làm cường độ còn một phần tư.",
    "use": "Mô tả phân bố năng lượng qua diện tích và áp dụng định luật nghịch đảo bình phương đúng điều kiện.",
    "question": "Cường độ giảm theo khoảng cách có buộc công suất nguồn giảm không?",
    "answer": "Không. Cùng công suất có thể phân bố trên diện tích lớn hơn. Nguồn phát đều trong môi trường không hấp thụ có công suất qua mỗi mặt cầu như nhau."
  },
  "chong-chat-song-tuyen-tinh": {
    "name": "Chồng chất sóng tuyến tính",
    "aliases": [
      "chồng chất sóng tuyến tính",
      "nguyên lý chồng chất sóng"
    ],
    "definition": "Trong hệ sóng tuyến tính, li độ tổng tại cùng vị trí và thời điểm bằng tổng đại số các li độ thành phần.",
    "example": "Hai xung dương có tổng li độ không âm khi chồng nhau. Hai xung đối dấu có thể triệt tiêu li độ trong vùng chung.",
    "use": "Dựng dạng tổng, giải thích phản xạ và xây dựng sóng dừng từ các sóng chạy.",
    "question": "Hai xung triệt tiêu ở một thời điểm có phải đã biến mất vĩnh viễn không?",
    "answer": "Không. Trong mô hình tuyến tính lý tưởng, từng sóng thành phần tiếp tục truyền sau khi vượt qua nhau. Sự triệt tiêu mô tả tổng tại vị trí và thời điểm đang xét."
  },
  "dieu-kien-bien-cua-day": {
    "name": "Điều kiện biên của dây sóng",
    "aliases": [
      "điều kiện biên của dây",
      "đầu cố định của dây",
      "đầu tự do của dây"
    ],
    "definition": "Các yêu cầu cơ học tại đầu dây mà hàm li độ phải thỏa. Đầu cố định có li độ bằng không, còn đầu tự do lý tưởng có độ dốc bằng không.",
    "example": "Xung phản xạ ở đầu cố định đảo dấu. Xung phản xạ ở vòng nhẹ trượt không ma sát giữ dấu li độ.",
    "use": "Chọn dấu và pha của sóng phản xạ, hoặc xác định các tần số riêng.",
    "question": "Đầu tự do có nghĩa không có lực căng dọc dây không?",
    "answer": "Không. Vòng và giá đỡ vẫn có thể duy trì lực căng dọc dây nhưng không tác dụng lực theo phương dao động. Điều kiện tự do đang nói đến phương dao động ngang."
  },
  "dang-dao-dong-rieng-cua-day": {
    "name": "Dạng dao động riêng của dây",
    "aliases": [
      "dạng dao động riêng của dây",
      "dạng riêng của dây"
    ],
    "definition": "Chuyển động điều hòa của dây trong đó mọi phần tử tham gia có cùng tần số, còn biên độ phụ thuộc vị trí. Với hai đầu cố định, các tần số là bội nguyên dương của tần số cơ bản.",
    "example": "Dạng thứ hai có hai bó sóng và một nút ở giữa dây. Dạng cơ bản có một bó và bụng ở giữa.",
    "use": "Tính các tần số tự nhiên và phân tích dao động phức tạp của dây đàn.",
    "question": "Mọi phần tử có cùng tần số đã có nghĩa chúng phải có cùng biên độ không?",
    "answer": "Không. Biên độ bằng không ở nút, lớn nhất ở bụng và có giá trị trung gian tại những vị trí khác."
  },
  "hoa-am-va-am-boi": {
    "name": "Họa âm và âm bồi",
    "aliases": [
      "họa âm của dây",
      "âm bồi",
      "dãy họa âm"
    ],
    "definition": "Trong dãy họa âm lý tưởng, họa âm thứ n có tần số $nf_1$. Âm cơ bản là họa âm thứ nhất. Âm bồi thứ nhất là họa âm thứ hai.",
    "example": "Âm bồi thứ hai có tần số gấp ba âm cơ bản, không phải gấp hai.",
    "use": "Đọc đúng chỉ số trong bài toán dây đàn và phân biệt cao độ với thành phần họa âm.",
    "question": "Họa âm thứ ba là âm bồi thứ mấy?",
    "answer": "Là âm bồi thứ hai vì các âm bồi được đếm từ thành phần đầu tiên nằm trên âm cơ bản."
  },
  "phan-tich-hoa-am-cua-day": {
    "name": "Phân tích họa âm của dây",
    "aliases": [
      "phân tích họa âm của dây",
      "chuỗi Fourier của dây"
    ],
    "definition": "Biểu diễn chuyển động của dây tuyến tính thành tổng các dạng dao động riêng. Hệ số mỗi thành phần phụ thuộc hình dạng và vận tốc ban đầu.",
    "example": "Một dây kéo thành tam giác không chỉ dao động theo một đường sin. Nhiều thành phần cùng tồn tại và được cộng tại từng điểm.",
    "use": "Liên hệ hình dạng ban đầu, thành phần họa âm và âm sắc nhạc cụ.",
    "question": "Biên độ thành phần cơ bản có bắt buộc bằng chiều cao cực đại của hình tam giác ban đầu không?",
    "answer": "Không. Chiều cao thực là tổng các đóng góp thành phần tại vị trí ấy. Hệ số cơ bản chỉ là một hệ số của khai triển."
  },
  "nut-va-bung-song": {
    "name": "Nút và bụng sóng",
    "aliases": [
      "nút sóng",
      "bụng sóng"
    ],
    "definition": "Trong sóng dừng, nút là điểm có li độ luôn bằng không, còn bụng là điểm có biên độ lớn nhất. Hai nút kề hoặc hai bụng kề cách nhau nửa bước sóng.",
    "example": "Cả dây có thể đi qua vị trí cân bằng tại một thời điểm. Chỉ những điểm luôn đứng yên trong cả chu kỳ mới là nút.",
    "use": "Đọc hình sóng dừng và phân biệt khoảng cách nút–nút với khoảng cách nút–bụng kề.",
    "question": "Một điểm đang có li độ bằng không đã đủ để gọi là nút chưa?",
    "answer": "Chưa. Li độ phải bằng không ở mọi thời điểm, nghĩa là biên độ của điểm ấy bằng không."
  },
  "song-dung-co-hoc": {
    "name": "Sóng dừng cơ học",
    "aliases": [
      "sóng dừng cơ học",
      "sóng dừng trên dây"
    ],
    "definition": "Dạng dao động có các nút và bụng cố định, tạo bởi hai sóng sin cùng biên độ, tần số và bước sóng truyền ngược chiều. Nút luôn có li độ bằng không, còn bụng có biên độ lớn nhất.",
    "example": "Trong dây cố định tại gốc, hai nút kề cách nửa bước sóng. Điểm qua li độ không ở một thời điểm chưa chắc là nút.",
    "use": "Xác định vị trí nút, bụng và biên độ khi sóng tới chồng với sóng phản xạ.",
    "question": "Không truyền công suất trung bình có nghĩa mọi điểm của dây đều đứng yên không?",
    "answer": "Không. Những điểm ngoài nút vẫn dao động và năng lượng trao đổi cục bộ. Trung bình công suất qua một tiết diện bằng không trong sóng dừng lý tưởng."
  }
}
export const physics1WaveWikiDetails={
  "song-co-hoc": "Một sóng ngang có phương dao động vuông góc phương truyền. Một sóng dọc có hai phương cùng phương. Sóng mặt nước có thể kết hợp cả hai thành phần.\n\nTrong mô hình dao động nhỏ, phần tử dao động quanh vị trí cân bằng, còn năng lượng được truyền nhờ lực giữa các phần môi trường. Điều này không phủ định mọi dòng chảy hoặc chuyển khối ngoài mô hình tuyến tính.\n\nVới sóng tuần hoàn:\n\n$$\nv=\\lambda f\n$$\n\nSóng cơ cần môi trường. Sóng điện từ còn có thể truyền trong chân không.",
  "buoc-song-co-hoc": "Trong một chu kỳ $T$, dạng sóng chạy được quãng đường bằng một bước sóng:\n\n$$\n\\lambda=vT=\\frac vf\n$$\n\nĐơn vị SI của bước sóng là mét. Với môi trường không tán sắc và các tính chất giữ nguyên, tốc độ truyền không đổi nên tần số tăng làm bước sóng giảm.\n\nĐối với sóng dọc, bước sóng có thể đo giữa hai tâm vùng nén kề nhau hoặc hai tâm vùng giãn kề nhau.",
  "so-song": "Với pha $kx-\\omega t+\\varphi$, giữ thời gian cố định rồi thay vị trí sẽ làm pha đổi theo hệ số $k$.\n\n$$\nk=\\frac{2\\pi}{\\lambda},\\qquad v=\\frac\\omega k\n$$\n\nỞ đây quy ước $k>0$ và $\\omega>0$. Dấu giữa phần không gian và thời gian trong hàm sóng chọn chiều truyền. Một số tài liệu dùng tên số sóng cho $1/\\lambda$, nên phải đọc rõ quy ước trước khi thay số.",
  "ham-song-co-hoc": "Một sóng sin truyền theo chiều dương có dạng:\n\n$$\ny=A\\cos(kx-\\omega t)\n$$\n\nĐặt $\\theta=kx-\\omega t$. Vận tốc và gia tốc phần tử là:\n\n$$\nv_y=\\omega A\\sin\\theta\n$$\n\n$$\na_y=-\\omega^2y\n$$\n\nSóng truyền theo chiều âm có dấu cộng giữa $kx$ và $\\omega t$. Trong mô hình tuyến tính với tốc độ không đổi, hàm li độ thỏa:\n\n$$\n\\frac{\\partial^2y}{\\partial x^2}=\\frac1{v^2}\\frac{\\partial^2y}{\\partial t^2}\n$$\n\nHàm li độ sóng cơ không phải hàm sóng lượng tử. Đại lượng y ở đây là một độ dời cơ học.",
  "toc-do-song-ngang-tren-day": "Với dây đồng nhất dài $L$, khối lượng $m$:\n\n$$\n\\mu=\\frac mL\n$$\n\nLực căng cung cấp thành phần phục hồi khi dây cong, còn $\\mu$ quyết định quán tính của một đoạn dây. Phương trình Newton dẫn tới:\n\n$$\n\\frac{\\partial^2y}{\\partial x^2}=\\frac\\mu F\\frac{\\partial^2y}{\\partial t^2}\n$$\n\nSo sánh với phương trình sóng cho:\n\n$$\nv=\\sqrt{\\frac F\\mu}\n$$\n\nCông thức cần dây mềm, độ dốc nhỏ và lực căng gần đều. Độ cứng uốn, biến thiên lực căng hoặc dao động lớn có thể đòi mô hình khác.",
  "cong-suat-song-co": "Lực của phần dây trái lên phần bên phải thực hiện công với công suất:\n\n$$\nP=-F\\frac{\\partial y}{\\partial x}\\frac{\\partial y}{\\partial t}\n$$\n\nVới một sóng chạy hình sin theo chiều dương, đặt $\\theta=kx-\\omega t$:\n\n$$\nP=\\sqrt{\\mu F}\\,\\omega^2A^2\\sin^2\\theta\n$$\n\nTrung bình trên một số nguyên chu kỳ:\n\n$$\nP_{\\mathrm{tb}}=\\frac12\\sqrt{\\mu F}\\,\\omega^2A^2\n$$\n\nĐơn vị công suất là watt. Kết luận tỉ lệ $A^2f^2$ dùng biên độ li độ A và các tính chất cơ học không đổi, không tự chuyển sang công thức theo biên độ áp suất hoặc biên độ điện trường.",
  "cuong-do-song-co": "Nếu cường độ đều trên diện tích $S$ vuông góc chiều truyền:\n\n$$\nI=\\frac{P_{\\mathrm{tb}}}{S}\n$$\n\nVới nguồn phát đều mọi hướng, diện tích mặt cầu là $4\\pi r^2$. Khi không có năng lượng bị hấp thụ giữa các mặt cầu:\n\n$$\nI=\\frac P{4\\pi r^2}\n$$\n\n$$\n\\frac{I_1}{I_2}=\\frac{r_2^2}{r_1^2}\n$$\n\nỞ đây $P$ là công suất trung bình của nguồn. Phản xạ, hướng tính nguồn và hấp thụ có thể làm phân bố cường độ khác mô hình này.",
  "chong-chat-song-tuyen-tinh": "Với hai thành phần:\n\n$$\ny(x,t)=y_1(x,t)+y_2(x,t)\n$$\n\nPhương trình sóng tuyến tính cho phép cộng nghiệm vì đạo hàm của tổng bằng tổng các đạo hàm. Các thành phần phải cùng tuân mô hình môi trường và điều kiện biên tương ứng.\n\nTổng là tổng đại số li độ, không phải cộng các độ lớn. Hai giá trị cùng dấu tăng độ lớn tổng, còn hai giá trị trái dấu bù nhau một phần hoặc toàn phần. Hệ phi tuyến không tự động có tính chất cộng nghiệm này.",
  "dieu-kien-bien-cua-day": "Tại đầu cố định đặt ở $x=0$:\n\n$$\ny(0,t)=0\n$$\n\nSóng phản xạ phải đảo dấu để tổng li độ tại đầu bằng không. Tại đầu tự do lý tưởng, lực theo phương dao động bằng không, nên:\n\n$$\n\\left.\\frac{\\partial y}{\\partial x}\\right|_{x=0}=0\n$$\n\nHai sóng cùng dấu và truyền ngược chiều có thể thỏa điều kiện độ dốc bằng không tại biên đối xứng. Dây cố định hai đầu cần nút tại cả hai đầu, nên chỉ có một dãy các dạng sóng dừng điều hòa phù hợp.",
  "dang-dao-dong-rieng-cua-day": "Với chiều dài $L$ cố định hai đầu, một, hai, ba,... nửa bước sóng nằm trong chiều dài dây. Chỉ số $n=1,2,3,\\ldots$ cho:\n\n$$\n\\lambda_n=\\frac{2L}n\n$$\n\n$$\nf_n=\\frac{nv}{2L}=nf_1\n$$\n\nVới $k_n=n\\pi/L$ và $\\omega_n=2\\pi f_n$, hàm $y_n(x,t)$ viết gọn:\n\n$$\ny_n=A_{\\mathrm{SW}}\\sin k_nx\\sin\\omega_nt\n$$\n\nPha thời gian được chọn phù hợp trạng thái đầu. Công thức hai đầu cố định chỉ chọn những sóng dừng điều hòa riêng lẻ, không phủ định khả năng dây mang một nhiễu loạn tổng quát.",
  "hoa-am-va-am-boi": "Dãy tần số của dây mềm lý tưởng cố định hai đầu bắt đầu bằng $f_1$, $2f_1$, $3f_1$, $4f_1$, v.v. Với $n=1,2,3,\\ldots$:\n\n$$\nf_n=nf_1\n$$\n\nHọa âm thứ nhất là âm cơ bản, họa âm thứ hai là âm bồi thứ nhất, còn họa âm thứ ba là âm bồi thứ hai. Các thành phần biên độ khác nhau góp phần tạo âm sắc của âm phức.\n\nKhông phải mọi hệ dao động đều có dãy tần số riêng là bội nguyên chính xác. Kết luận dãy họa âm ở đây dùng mô hình dây mềm đồng nhất với hai đầu cố định.",
  "phan-tich-hoa-am-cua-day": "Gọi $Y_1,Y_2,Y_3,\\ldots$ là li độ của các thành phần tại cùng $x,t$. Khai triển trực tiếp là:\n\n$$\ny=Y_1+Y_2+Y_3+\\cdots\n$$\n\nKý hiệu gọn:\n\n$$\ny=\\sum_{n=1}^{\\infty}Y_n\n$$\n\nChỉ số $n$ chạy qua các số nguyên dương ứng với các dạng riêng. Với dây được thả từ nghỉ, đặt $k_n=n\\pi/L$, $\\omega_n=2\\pi f_n$ và viết:\n\n$$\nY_n=B_n\\sin k_nx\\cos\\omega_nt\n$$\n\nMỗi hệ số $B_n$ được xác định bởi hình dạng đầu. Các cos theo thời gian cho vận tốc ban đầu bằng không. Khi có vận tốc đầu khác không, cần thêm những thành phần pha phù hợp.",
  "nut-va-bung-song": "Với nút tại gốc và số sóng $k=2\\pi/\\lambda$, li độ có thừa số không gian $\\sin kx$. Các nút ở $0$, $\\lambda/2$, $\\lambda$, $3\\lambda/2$, v.v.\n\n$$\nx_n=\\frac{n\\lambda}2\n$$\n\nChỉ số $n=0,1,2,\\ldots$ đếm các nút từ gốc. Bụng nằm giữa các nút, tại $\\lambda/4$, $3\\lambda/4$, $5\\lambda/4$, v.v. Khoảng cách nút–bụng kề là:\n\n$$\nd=\\frac\\lambda4\n$$\n\nMột điểm tại bụng không luôn có li độ cực đại. Nó có biên độ lớn nhất nhưng vẫn đi qua vị trí cân bằng trong mỗi chu kỳ.",
  "song-dung-co-hoc": "Với nút tại $x=0$, hàm $y(x,t)$ được viết gọn:\n\n$$\ny=A_{\\mathrm{SW}}\\sin kx\\sin\\omega t\n$$\n\nBiên độ tại bụng $A_{\\mathrm{SW}}=2A$ bằng hai lần biên độ mỗi sóng chạy thành phần. Biên độ tại vị trí x là độ lớn thừa số không gian, nên bằng không khi $\\sin kx=0$.\n\nCác nút lần lượt ở $0$, $\\lambda/2$, $\\lambda$, $3\\lambda/2$, v.v. Viết gọn với $n=0,1,2,\\ldots$:\n\n$$\nx_n=\\frac{n\\lambda}2\n$$\n\nCác điểm trong một bó dao động cùng pha. Hai bó kề ngược pha. Khoảng cách nút–bụng kề bằng một phần tư bước sóng. Công suất tức thời có thể khác không và đổi dấu, nhưng trung bình bằng không ở mọi điểm trong sóng dừng lý tưởng.\n\n### Dây cố định hai đầu\n\nVới dây dài $L$ cố định hai đầu:\n\n$$\nL=n\\lambda_n/2\n$$\n\nCác chỉ số được phép là các số nguyên dương. Tần số của dạng thứ $n$ được xác định từ tốc độ truyền sóng và bước sóng của dạng đó:\n\n$$\nf_n=nv/(2L)\n$$\n\nKhông dùng điều kiện hai đầu cố định cho một hệ có đầu tự do hoặc những điều kiện biên khác."
}
export const physics1WaveWikiConnections={
  "song-co-hoc": [
    "buoc-song-co-hoc",
    "ham-song-co-hoc",
    "toc-do-song-ngang-tren-day"
  ],
  "buoc-song-co-hoc": [
    "song-co-hoc",
    "so-song",
    "pha-song"
  ],
  "so-song": [
    "buoc-song-co-hoc",
    "pha-song",
    "ham-song-co-hoc"
  ],
  "ham-song-co-hoc": [
    "song-co-hoc",
    "so-song",
    "dao-ham-rieng",
    "ham-song-luong-tu"
  ],
  "toc-do-song-ngang-tren-day": [
    "song-co-hoc",
    "ham-song-co-hoc",
    "dang-dao-dong-rieng-cua-day"
  ],
  "cong-suat-song-co": [
    "cuong-do-song-co",
    "toc-do-song-ngang-tren-day",
    "song-dung-co-hoc"
  ],
  "cuong-do-song-co": [
    "cong-suat-song-co",
    "song-co-hoc"
  ],
  "chong-chat-song-tuyen-tinh": [
    "giao-thoa-song",
    "dieu-kien-bien-cua-day",
    "song-dung-co-hoc"
  ],
  "dieu-kien-bien-cua-day": [
    "chong-chat-song-tuyen-tinh",
    "song-dung-co-hoc",
    "dang-dao-dong-rieng-cua-day"
  ],
  "dang-dao-dong-rieng-cua-day": [
    "song-dung-co-hoc",
    "hoa-am-va-am-boi",
    "toc-do-song-ngang-tren-day"
  ],
  "hoa-am-va-am-boi": [
    "dang-dao-dong-rieng-cua-day",
    "phan-tich-hoa-am-cua-day"
  ],
  "phan-tich-hoa-am-cua-day": [
    "chong-chat-song-tuyen-tinh",
    "dang-dao-dong-rieng-cua-day",
    "hoa-am-va-am-boi"
  ],
  "nut-va-bung-song": [
    "song-dung-co-hoc",
    "dang-dao-dong-rieng-cua-day",
    "buoc-song-co-hoc"
  ],
  "song-dung-co-hoc": [
    "chong-chat-song-tuyen-tinh",
    "dieu-kien-bien-cua-day",
    "dang-dao-dong-rieng-cua-day"
  ]
}
