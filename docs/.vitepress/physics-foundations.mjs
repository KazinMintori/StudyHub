import { physicsMotionConcepts, physicsMotionWikiDetails, physicsMotionWikiConnections } from './physics-motion-foundations.mjs'
export const physicsConcepts = {
  ...physicsMotionConcepts,
  "dong-luong-vat-ly": {
    "name": "Động lượng trong vật lý",
    "aliases": [
      "Động lượng trong vật lý",
      "động lượng"
    ],
    "definition": "Động lượng của chất điểm là vector $\\mathbf p=m\\mathbf v$. Tổng động lượng của hệ thay đổi theo xung lượng ngoài. Khi xung lượng ngoài bằng không, tổng động lượng bảo toàn.",
    "example": "Hai vật va chạm có thể giữ tổng động lượng dù động năng chuyển thành nhiệt và biến dạng.",
    "use": "Phân tích va chạm, xung lực và chuyển động khối tâm.",
    "question": "Bảo toàn động lượng có bảo đảm bảo toàn động năng không?",
    "answer": "Không. Va chạm không đàn hồi có thể bảo toàn động lượng nhưng không bảo toàn động năng."
  },
  "momen-luc": {
    "name": "Mômen lực",
    "aliases": [
      "Mômen lực",
      "mômen lực",
      "momen lực"
    ],
    "definition": "Mômen của lực đối với gốc O là $\\boldsymbol\\tau=\\mathbf r\\times\\mathbf F$. Nó mô tả tác dụng làm quay và phụ thuộc cả lực lẫn vị trí đường tác dụng đối với gốc.",
    "example": "Đẩy cửa gần mép tạo mômen lớn hơn đẩy gần bản lề với cùng lực vuông góc cửa.",
    "use": "Lập cân bằng vật rắn và phương trình quay.",
    "question": "Lực khác không có thể cho mômen bằng không không?",
    "answer": "Có. Khi đường tác dụng đi qua gốc tính mômen, cánh tay đòn bằng không."
  },
  "momen-quan-tinh": {
    "name": "Mômen quán tính",
    "aliases": [
      "Mômen quán tính",
      "mômen quán tính",
      "momen quán tính"
    ],
    "definition": "Mômen quán tính đối với một trục là $I=\\int r^2dm$, với r là khoảng cách vuông góc tới trục. Nó đo mức quán tính quay và phụ thuộc phân bố khối lượng.",
    "example": "Vành mỏng có nhiều khối lượng xa trục hơn đĩa đồng chất cùng khối lượng và bán kính.",
    "use": "Tính động năng quay, gia tốc góc và chuyển động lăn.",
    "question": "Chỉ biết khối lượng có đủ biết mômen quán tính không?",
    "answer": "Không. Cần phân bố khối lượng và trục được chọn."
  },
  "dao-dong-dieu-hoa": {
    "name": "Dao động điều hòa",
    "aliases": [
      "Dao động điều hòa",
      "dao động điều hòa"
    ],
    "definition": "Dao động điều hòa có độ dời $x=A\\cos(\\omega t+\\varphi)$ và gia tốc $a=-\\omega^2x$. Lực phục hồi tuyến tính dẫn tới dạng này trong mô hình không tổn hao.",
    "example": "Vật gắn lò xo lý tưởng qua cân bằng với tốc độ lớn nhất và dừng tức thời ở hai biên.",
    "use": "Mô tả dao động lò xo, con lắc góc nhỏ và mạch LC.",
    "question": "Ở biên, gia tốc có bằng không như vận tốc không?",
    "answer": "Không. Gia tốc có độ lớn cực đại và hướng về cân bằng."
  },
  "nhiet-do-tuyet-doi": {
    "name": "Nhiệt độ tuyệt đối",
    "aliases": [
      "Nhiệt độ tuyệt đối",
      "nhiệt độ tuyệt đối",
      "thang Kelvin"
    ],
    "definition": "Nhiệt độ tuyệt đối T dùng thang kelvin. Tỷ số nhiệt độ trong phương trình khí và giới hạn Carnot phải dùng thang này, với $T(\\mathrm K)=t(^\\circ\\mathrm C)+273.15$.",
    "example": "Độ chênh nhiệt độ trên thang kelvin bằng độ chênh tương ứng trên thang Celsius, nhưng tỷ số hai nhiệt độ không bằng nhau.",
    "use": "Tính trạng thái khí, entropy và hiệu suất nhiệt.",
    "question": "Có dùng trực tiếp nhiệt độ Celsius trong tỷ số Carnot không?",
    "answer": "Không. Phải đổi hai nhiệt độ sang kelvin."
  },
  "khi-ly-tuong": {
    "name": "Khí lý tưởng",
    "aliases": [
      "Khí lý tưởng",
      "khí lý tưởng"
    ],
    "definition": "Khí lý tưởng là mô hình bỏ thể tích riêng và tương tác phân tử ngoài va chạm, thỏa $pV=nRT$. p là áp suất tuyệt đối, n là số mol và T tính bằng kelvin.",
    "example": "Khí đủ loãng và xa miền ngưng tụ có thể gần mô hình khí lý tưởng.",
    "use": "Tính trạng thái khí và các quá trình nhiệt động cơ bản.",
    "question": "Phương trình khí lý tưởng có mô tả đầy đủ ngưng tụ không?",
    "answer": "Không. Tương tác giữa phân tử cần được xét để mô tả chuyển pha."
  },
  "noi-nang": {
    "name": "Nội năng",
    "aliases": [
      "Nội năng",
      "nội năng"
    ],
    "definition": "Nội năng là năng lượng vi mô của hệ trong mô tả nhiệt động, không gồm động năng chuyển động toàn khối đang xét riêng. Nó là hàm trạng thái và biến thiên theo nhiệt cùng công trao đổi.",
    "example": "Khí giãn đoạn nhiệt có thể giảm nội năng dù không trao đổi nhiệt.",
    "use": "Lập nguyên lý I và phân biệt trạng thái với quá trình.",
    "question": "Nhiệt lượng có phải một hàm trạng thái như nội năng không?",
    "answer": "Không. Nhiệt mô tả năng lượng truyền trong một quá trình."
  },
  "entropy-nhiet-dong": {
    "name": "Entropy trong nhiệt động lực học",
    "aliases": [
      "Entropy trong nhiệt động lực học",
      "entropy",
      "entropy nhiệt động"
    ],
    "definition": "Entropy là hàm trạng thái với $dS=\\delta Q_{\\mathrm{rev}}/T$ trên quá trình thuận nghịch. Tổng entropy của một hệ cô lập không giảm.",
    "example": "Nhiệt truyền từ nguồn nóng sang nguồn lạnh làm tổng entropy hai nguồn tăng.",
    "use": "Xét chiều quá trình, tính giới hạn động cơ và phân biệt thuận nghịch.",
    "question": "Entropy của một vật riêng có luôn tăng không?",
    "answer": "Không. Nó có thể giảm khi thải nhiệt; phải xét tổng hệ và môi trường."
  },
  "dien-truong": {
    "name": "Điện trường",
    "aliases": [
      "Điện trường",
      "điện trường",
      "cường độ điện trường"
    ],
    "definition": "Điện trường là vector mô tả lực điện trên một đơn vị điện tích thử: $\\mathbf F=q\\mathbf E$. Trường do nguồn quyết định; dấu q quyết định chiều lực.",
    "example": "Điện tích âm chịu lực ngược chiều điện trường tại cùng điểm.",
    "use": "Tính tương tác điện, thông lượng và quan hệ với điện thế.",
    "question": "Đổi dấu điện tích thử có đổi chiều điện trường nguồn không?",
    "answer": "Không nếu điện tích thử không làm thay đổi phân bố nguồn."
  },
  "dien-dung": {
    "name": "Điện dung",
    "aliases": [
      "Điện dung",
      "điện dung"
    ],
    "definition": "Điện dung của tụ là $C=Q/V$ trong mô hình điện môi tuyến tính, với Q là độ lớn điện tích một bản và V là hiệu điện thế giữa hai bản. Đơn vị là farad.",
    "example": "Đưa điện môi vào tụ cô lập làm điện dung tăng trong khi điện tích tự do giữ nguyên.",
    "use": "Phân tích ghép tụ và năng lượng điện trường.",
    "question": "Tụ nối nguồn điện áp lý tưởng có giữ điện tích khi thêm điện môi không?",
    "answer": "Không nói chung. Điện áp giữ nguyên; điện tích thay đổi theo điện dung."
  },
  "dong-dien": {
    "name": "Dòng điện",
    "aliases": [
      "Dòng điện",
      "dòng điện",
      "cường độ dòng điện"
    ],
    "definition": "Dòng điện là tốc độ điện tích đi qua một tiết diện: $I=dQ/dt$. Chiều quy ước theo hạt tải dương; electron trôi ngược chiều đó trong kim loại.",
    "example": "Trong một nhánh ổn định không rò, điện trở làm tiêu hao năng lượng nhưng không làm dòng giảm dần dọc nhánh.",
    "use": "Lập phương trình nút, tính công suất và mật độ dòng.",
    "question": "Điện trở tiêu thụ dòng điện hay năng lượng?",
    "answer": "Năng lượng. Bảo toàn điện tích giữ dòng trong nhánh ổn định."
  },
  "dien-tro": {
    "name": "Điện trở",
    "aliases": [
      "Điện trở",
      "điện trở",
      "điện trở suất"
    ],
    "definition": "Điện trở R liên hệ điện áp với dòng theo $V=IR$ trong miền ohmic. Điện trở suất là tính chất vật liệu, còn điện trở còn phụ thuộc hình học và nhiệt độ.",
    "example": "Dây đồng nhất dài hơn có điện trở lớn hơn khi tiết diện, vật liệu và nhiệt độ giữ nguyên.",
    "use": "Rút gọn mạch và tính nhiệt Joule.",
    "question": "Điện trở và điện trở suất có cùng đơn vị không?",
    "answer": "Không. Điện trở đo bằng ohm; điện trở suất đo bằng ohm mét."
  },
  "tu-truong": {
    "name": "Từ trường",
    "aliases": [
      "Từ trường",
      "từ trường",
      "cảm ứng từ"
    ],
    "definition": "Từ trường là vector $\\mathbf B$ tạo phần lực Lorentz $q\\mathbf v\\times\\mathbf B$ lên điện tích chuyển động. Đơn vị là tesla; lực này vuông góc vận tốc.",
    "example": "Điện tích bay vuông góc trường đều có thể chuyển động tròn mà tốc độ không đổi.",
    "use": "Tính lực lên hạt, dây và khung dòng điện.",
    "question": "Lực từ riêng có làm tăng động năng của hạt không?",
    "answer": "Không. Tích vô hướng lực từ với vận tốc bằng không."
  },
  "cam-ung-dien-tu": {
    "name": "Cảm ứng điện từ",
    "aliases": [
      "Cảm ứng điện từ",
      "cảm ứng điện từ",
      "định luật Faraday",
      "định luật Lenz"
    ],
    "definition": "Cảm ứng điện từ là sự xuất hiện suất điện động liên hệ với biến thiên từ thông của mạch. Faraday cho độ lớn và dấu; Lenz cho chiều chống biến thiên gây ra đáp ứng.",
    "example": "Khi từ thông qua vòng kín tăng, dòng cảm ứng tạo từ trường chống sự tăng đó.",
    "use": "Phân tích máy phát, vòng dây chuyển động và điện trường cảm ứng.",
    "question": "Lenz có luôn yêu cầu trường cảm ứng ngược trường ban đầu không?",
    "answer": "Không. Nó chống sự biến thiên; khi từ thông giảm, trường cảm ứng có thể cùng hướng trường ban đầu."
  },
  "tu-cam": {
    "name": "Tự cảm",
    "aliases": [
      "Tự cảm",
      "tự cảm",
      "hệ số tự cảm"
    ],
    "definition": "Tự cảm là đáp ứng cảm ứng của mạch khi chính dòng mạch biến thiên. Trong mô hình tuyến tính, $\\mathcal E_L=-L\\,di/dt$, với L đo bằng henry.",
    "example": "Dòng giảm qua cuộn khiến suất điện động tự cảm có xu hướng giữ dòng theo chiều đang có.",
    "use": "Tính quá trình RL, dao động LC và năng lượng từ trường.",
    "question": "Suất điện động tự cảm luôn ngược dòng đang có không?",
    "answer": "Không. Nó chống thay đổi dòng, nên phụ thuộc dấu đạo hàm dòng."
  },
  "pha-song": {
    "name": "Pha của dao động và sóng",
    "aliases": [
      "Pha của dao động và sóng",
      "pha sóng",
      "độ lệch pha"
    ],
    "definition": "Pha là đối số của hàm điều hòa, chẳng hạn $kx-\\omega t+\\varphi$ trong một sóng truyền. Hiệu pha quyết định quan hệ giữa hai dao động cùng tần số.",
    "example": "Hai sóng cùng biên độ có thể triệt tiêu tại một điểm nếu lệch pha một nửa vòng.",
    "use": "Đọc hướng truyền, giao thoa và lệch pha mạch xoay chiều.",
    "question": "Cùng tần số có bảo đảm cùng pha không?",
    "answer": "Không. Còn cần pha đầu và đường truyền phù hợp."
  },
  "giao-thoa-song": {
    "name": "Giao thoa sóng",
    "aliases": [
      "Giao thoa sóng",
      "giao thoa",
      "nguồn kết hợp"
    ],
    "definition": "Giao thoa là phân bố tăng giảm biên độ do chồng chất sóng. Vân ổn định cần quan hệ pha đủ ổn định giữa các nguồn trong điều kiện đo.",
    "example": "Hai sóng bằng biên độ và ngược pha triệt tiêu tại điểm đang xét.",
    "use": "Phân tích hai khe, phách, sóng dừng và màng mỏng.",
    "question": "Hai nguồn cùng tần số có luôn cho vân ổn định không?",
    "answer": "Không. Cần xét tính kết hợp và pha tương đối trong khoảng đo."
  },
  "chiet-suat": {
    "name": "Chiết suất",
    "aliases": [
      "Chiết suất",
      "chiết suất"
    ],
    "definition": "Chiết suất n là tỷ số tốc độ ánh sáng chân không với tốc độ pha trong môi trường: $n=c/v$. Nó có thể phụ thuộc bước sóng và điều kiện vật liệu.",
    "example": "Tia vào môi trường có chiết suất lớn hơn lệch về pháp tuyến ở mặt phân cách phẳng.",
    "use": "Tính khúc xạ, phản xạ toàn phần và đường quang.",
    "question": "Khúc xạ ở mặt đứng yên có đổi tần số ánh sáng không?",
    "answer": "Không. Tốc độ và bước sóng đổi, tần số giữ nguyên."
  },
  "nhieu-xa-anh-sang": {
    "name": "Nhiễu xạ ánh sáng",
    "aliases": [
      "Nhiễu xạ ánh sáng",
      "nhiễu xạ",
      "đĩa Airy"
    ],
    "definition": "Nhiễu xạ là sự lan và giao thoa của ánh sáng qua khẩu độ hoặc quanh mép. Khẩu độ hữu hạn làm ảnh nguồn điểm có độ rộng, tạo giới hạn phân giải của hệ quang.",
    "example": "Thu hẹp khe làm vân trung tâm nhiễu xạ rộng hơn trong miền màn xa.",
    "use": "Tính phổ một khe, cách tử và độ phân giải khẩu độ tròn.",
    "question": "Cực tiểu một khe có gồm bậc bằng không không?",
    "answer": "Không. Tâm là cực đại; công thức cực tiểu bắt đầu từ bậc khác không."
  },
  "thuyet-tuong-doi-hep": {
    "name": "Thuyết tương đối hẹp",
    "aliases": [
      "Thuyết tương đối hẹp",
      "thuyết tương đối hẹp",
      "hệ số Lorentz"
    ],
    "definition": "Thuyết tương đối hẹp mô tả các hệ quán tính với tốc độ ánh sáng chân không bất biến. Biến đổi Lorentz nối tọa độ không gian và thời gian giữa các hệ.",
    "example": "Đồng hồ chuyển động được hệ quan sát đo với khoảng thời gian dài hơn thời gian riêng giữa cùng hai nhịp.",
    "use": "Xét vận tốc gần ánh sáng và năng lượng–động lượng.",
    "question": "Tính đồng thời có giống nhau trong mọi hệ quán tính không?",
    "answer": "Không với các sự kiện cách xa; nó phụ thuộc hệ quy chiếu."
  },
  "photon": {
    "name": "Photon",
    "aliases": [
      "Photon",
      "photon",
      "lượng tử ánh sáng"
    ],
    "definition": "Photon là lượng tử của trường điện từ. Trong chân không, nó có $E=hf=hc/\\lambda$, $p=E/c$ và khối lượng nghỉ bằng không.",
    "example": "Tăng tần số làm tăng năng lượng một photon; tăng cường độ cùng tần số chủ yếu tăng thông lượng photon.",
    "use": "Giải quang điện, Compton, chuyển mức và bức xạ.",
    "question": "Photon có khối lượng nghỉ bằng không thì có động lượng không?",
    "answer": "Có. Động lượng photon bằng năng lượng chia tốc độ ánh sáng."
  },
  "ham-song-luong-tu": {
    "name": "Hàm sóng lượng tử",
    "aliases": [
      "Hàm sóng lượng tử",
      "hàm sóng",
      "quy tắc Born"
    ],
    "definition": "Hàm sóng mô tả trạng thái lượng tử trong một biểu diễn. Với một hạt trong không gian, bình phương môđun hàm sóng cho mật độ xác suất tìm hạt.",
    "example": "Hàm sóng hộp một chiều có các nút nơi xác suất tìm hạt bằng không trong trạng thái đó.",
    "use": "Chuẩn hóa, tính xác suất và giải Schrödinger.",
    "question": "Có thể dùng trực tiếp hàm sóng làm xác suất không?",
    "answer": "Không. Phải dùng bình phương môđun và tích phân trên miền cần xét."
  },
  "spin-luong-tu": {
    "name": "Spin lượng tử",
    "aliases": [
      "Spin lượng tử",
      "spin",
      "spin electron"
    ],
    "definition": "Spin là mômen động lượng nội tại của hạt. Electron có số lượng tử spin một nửa và hai giá trị thành phần spin trên một trục đo.",
    "example": "Hai electron trong cùng orbital có thể khác giá trị spin trên trục được chọn.",
    "use": "Mô tả cấu trúc nguyên tử, từ tính và nguyên lý Pauli.",
    "question": "Spin có phải quả cầu electron quay theo cơ học cổ điển không?",
    "answer": "Không. Đó là thuộc tính lượng tử nội tại."
  },
  "nguyen-ly-pauli": {
    "name": "Nguyên lý loại trừ Pauli",
    "aliases": [
      "Nguyên lý loại trừ Pauli",
      "nguyên lý Pauli",
      "nguyên lý loại trừ"
    ],
    "definition": "Trong mô hình nguyên tử, không hai electron cùng cả bốn số lượng tử. Một orbital có tối đa hai electron với số lượng tử spin khác nhau.",
    "example": "Một orbital được điền đầy bởi hai trạng thái spin khác nhau.",
    "use": "Đếm trạng thái lớp nguyên tử và giải thích sự điền vùng năng lượng.",
    "question": "Hai electron có cùng ba số lượng tử orbital có nhất thiết vi phạm Pauli không?",
    "answer": "Không. Chúng có thể khác spin; chỉ cùng cả bốn số mới bị loại."
  },
  "vung-nang-luong": {
    "name": "Vùng năng lượng trong chất rắn",
    "aliases": [
      "Vùng năng lượng trong chất rắn",
      "vùng năng lượng",
      "vùng cấm",
      "vùng dẫn"
    ],
    "definition": "Vùng năng lượng là các miền mức được phép hình thành khi nhiều nguyên tử tương tác trong chất rắn. Vùng cấm là khoảng không có trạng thái electron khối được phép trong mô hình vùng đang xét.",
    "example": "Vùng được điền một phần có thể cho electron đáp ứng dòng điện, còn vùng đầy bị ngăn bởi một khoảng cấm cho đáp ứng khác.",
    "use": "Phân biệt kim loại, cách điện, bán dẫn và pha tạp.",
    "question": "Bán dẫn loại n có nhất thiết tích điện tổng âm không?",
    "answer": "Không. Hạt tải và điện tích ion có thể bù nhau, giữ mẫu trung hòa."
  },
  "phan-ra-phong-xa": {
    "name": "Phân rã phóng xạ",
    "aliases": [
      "Phân rã phóng xạ",
      "phân rã phóng xạ",
      "chu kỳ bán rã",
      "hoạt độ phóng xạ"
    ],
    "definition": "Phân rã phóng xạ là quá trình hạt nhân biến đổi theo xác suất. Với hằng số phân rã không đổi, số hạt còn lại giảm theo hàm mũ; chu kỳ bán rã là thời gian tỷ lệ còn lại trung bình giảm một nửa.",
    "example": "Sau mỗi chu kỳ bán rã, tỷ lệ hạt nhân ban đầu chưa phân rã lại giảm một nửa trong mô hình thống kê.",
    "use": "Tính số hạt còn lại, hoạt độ và năng lượng phản ứng.",
    "question": "Có biết chính xác khi nào một hạt nhân riêng sẽ phân rã từ chu kỳ bán rã không?",
    "answer": "Không. Chu kỳ bán rã mô tả xác suất và thống kê, không lịch phân rã của từng hạt."
  }
}

export const physicsConceptIds = Object.keys(physicsConcepts)

export const physicsWikiDetails = {
  ...physicsMotionWikiDetails,
  "dong-luong-vat-ly": "Chọn hệ trước khi phân biệt nội lực với ngoại lực. Quan hệ $\\Delta\\mathbf P=\\int\\mathbf F_{\\mathrm{ngoài}}dt$ cần xét các thành phần vector trong cùng hệ quán tính. Trong va chạm ngắn, có thể bỏ xung lượng ngoài dù ngoại lực không bằng không từng thời điểm, nếu xung lượng đó nhỏ so với trao đổi giữa các vật.\n\nỞ vận tốc gần tốc độ ánh sáng, dùng $\\mathbf p=\\gamma m\\mathbf v$ thay cho biểu thức Newton. “Momentum” trong tối ưu hóa là một thuật toán khác; đây là đại lượng cơ học.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 8. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "momen-luc": "Độ lớn mômen là $\\tau=Fd$ với $d$ là khoảng cách vuông góc từ gốc tới đường tác dụng lực. Không thay $d$ bằng khoảng cách từ gốc tới điểm đặt nếu lực không vuông góc vector vị trí.\n\nĐơn vị là newton mét; mômen là vector, khác công là số vô hướng. Trong hệ quán tính với gốc cố định, tổng mômen ngoài quyết định đạo hàm mômen động lượng đối với cùng gốc.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 10. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "momen-quan-tinh": "Với $n$ phần tử, $I=m_1r_1^2+\\cdots+m_nr_n^2=\\sum_{i=1}^nm_ir_i^2$. Đơn vị là kilôgam mét vuông. Với trục cố định và $I$ không đổi, $K=I\\omega^2/2$ và $\\sum\\tau_z=I\\alpha_z$.\n\nĐịnh lý $I=I_{\\mathrm{cm}}+Md^2$ dùng hai trục song song, một trục qua khối tâm. Không áp dụng nó cho hai trục bất kỳ.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 9. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "dao-dong-dieu-hoa": "$\\omega$ là tần số góc, $T=2\\pi/\\omega$ là chu kỳ. Biên độ và pha được xác định bởi vị trí và vận tốc ban đầu. Với vật lò xo, $\\omega=\\sqrt{k/m}$; con lắc chỉ gần điều hòa khi góc nhỏ.\n\nCó lực cản hoặc kích thích ngoài thì phải phân biệt tần số riêng, tần số kích thích và tần số dao động tắt dần. Không đồng nhất các đại lượng này trong mọi điều kiện.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 14. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "nhiet-do-tuyet-doi": "Nguyên lý không của nhiệt động lực học làm cơ sở so nhiệt độ qua cân bằng nhiệt. Kelvin viết không kèm ký hiệu độ. Đối với khoảng chênh, $\\Delta T=\\Delta t_C$, vì hằng số đổi thang triệt tiêu.\n\nNhiệt độ mô tả trạng thái, không phải tổng nội năng hay nhiệt lượng chứa trong một vật. Hai hệ cùng nhiệt độ vẫn có thể có nội năng khác nhau.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 17. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "khi-ly-tuong": "$pV=nRT=Nk_BT$ dùng số mol $n$ hoặc số phân tử $N$, không trộn hai đại lượng. Với lượng khí cố định, cần thêm điều kiện đẳng tích, đẳng áp hoặc đẳng nhiệt để nối hai trạng thái.\n\nNội năng khí lý tưởng phụ thuộc nhiệt độ, nhưng nhiệt dung còn phụ thuộc bậc tự do được kích hoạt. Không mặc định mọi khí có nhiệt dung của khí đơn nguyên tử.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 18. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "noi-nang": "Với quy ước nhiệt hệ nhận dương và công hệ thực hiện dương, $\\Delta U=Q-W$. Nếu dùng quy ước công nhận vào hệ, dấu công trong phương trình đổi; phải ghi quy ước trước.\n\nMột chu trình có $\\Delta U=0$ nhưng vẫn có thể nhận nhiệt ròng và sinh công ròng. Đẳng nhiệt khí lý tưởng có nội năng không đổi, còn chất thực cần xét phương trình nội năng phù hợp.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 19. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "entropy-nhiet-dong": "Để tính biến thiên entropy của quá trình không thuận nghịch, chọn một đường thuận nghịch tưởng tượng nối cùng hai trạng thái rồi tích phân. Không thay nhiệt thực vào $\\int\\delta Q/T$ nếu thiếu điều kiện thuận nghịch.\n\n$S=k_B\\ln\\Omega$ liên hệ với số trạng thái vi mô trong mô hình thống kê phù hợp. Định nghĩa này khác entropy thông tin dù hai lĩnh vực có quan hệ hình thức.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 20. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "dien-truong": "Đơn vị điện trường là newton trên coulomb, tương đương volt trên mét. Điện trường nhiều nguồn cộng vector tại cùng điểm. Trong tĩnh điện, $\\mathbf E=-\\nabla V$.\n\nĐường sức biểu diễn hướng trường, không phải quỹ đạo bắt buộc của hạt có vận tốc ban đầu. Điện trường cảm ứng có thể không là gradient của điện thế tĩnh đơn trị.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 21. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "dien-dung": "Tụ phẳng lý tưởng có $C=\\varepsilon A/d$, bỏ trường mép và dùng môi trường phù hợp. Năng lượng $U=Q^2/(2C)=CV^2/2$. Khi điện dung thay đổi, phải xác định đại lượng được giữ nguyên và năng lượng trao đổi với nguồn.\n\nTụ nối tiếp và song song có quy tắc ghép khác điện trở. Nút trung gian trung hòa là một giả thiết của quy tắc điện tích bằng nhau trong chuỗi tụ.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 24. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "dong-dien": "Mật độ dòng $\\mathbf J=nq\\mathbf v_d$ liên hệ với mật độ hạt và vận tốc trôi. Dòng qua mặt là tích phân $\\mathbf J\\cdot d\\mathbf A$. Chiều dấu phụ thuộc hướng pháp tuyến hoặc chiều nhánh được chọn.\n\nQuy tắc nút dạng tổng dòng vào bằng tổng dòng ra cần mô hình nút không tích lũy điện tích đáng kể. Nếu có tích điện, phải đưa tốc độ biến thiên điện tích nút vào phương trình.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 25. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "dien-tro": "Dây đồng nhất có $R=\\rho_e\\ell/A$. Công suất điện trở là $I^2R=V^2/R$ khi các đại lượng phù hợp cùng thời điểm hoặc dùng hiệu dụng cho mạch điều hòa.\n\nQuan hệ ohmic chỉ đúng trong điều kiện đáp ứng tuyến tính đang xét. Một linh kiện không ohmic không thể dùng một R không đổi cho toàn đường đặc tuyến điện áp–dòng.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 25. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "tu-truong": "Hướng lực dùng bàn tay phải cho điện tích dương rồi đảo chiều với điện tích âm. Từ thông qua mặt là $\\Phi_B=\\int\\mathbf B\\cdot d\\mathbf A$. Thông lượng mặt kín bằng không không bắt buộc từ trường bằng không từng điểm.\n\nDòng ổn định tạo trường theo Biot–Savart; điện trường biến thiên cũng góp nguồn trong Ampère–Maxwell. Không nhầm từ trường với lực từ, vì lực còn phụ thuộc điện tích và vận tốc.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 27. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "cam-ung-dien-tu": "Cuộn N vòng cùng từ thông có $\\mathcal E=-N\\,d\\Phi_B/dt$. Từ thông có thể đổi do trường, diện tích hoặc góc. Vòng không kín có thể có suất điện động nhưng chưa có dòng vòng.\n\nMạch chuyển động cần xét cả điện trường và lực từ trên điện tích theo vận tốc dây. Năng lượng cảm ứng đến từ tác nhân đổi trường hoặc tác nhân thực hiện công chuyển động.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 29. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "tu-cam": "Điện áp cuộn theo quy ước thụ động là $v_L=L\\,di/dt$ và năng lượng $U_B=Li^2/2$. Dòng không thể nhảy tức thời nếu L khác không và điện áp hữu hạn.\n\nHỗ cảm là liên kết giữa hai mạch, khác tự cảm của một mạch. L và M có thể phụ thuộc trạng thái vật liệu từ; công thức hệ số không đổi cần miền tuyến tính phù hợp.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 30. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "pha-song": "Trong sóng điều hòa, $k=2\\pi/\\lambda$ và $\\omega=2\\pi f$. Theo dõi một pha cố định giúp xác định hướng truyền: $kx-\\omega t$ truyền theo chiều x dương khi các tham số dương.\n\nCác pha bằng nhau sai khác số nguyên lần một vòng là tương đương. Khi truyền trong nhiều môi trường, cần đường quang hoặc thời gian truyền, không chỉ chiều dài hình học.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 15. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "giao-thoa-song": "Cộng biên độ trước khi tính cường độ. Với hai sóng cùng tần số và phân cực phù hợp, $I=I_1+I_2+2\\sqrt{I_1I_2}\\cos\\delta$. Nếu pha ngẫu nhiên nhanh, số hạng giao thoa trung bình có thể bằng không.\n\nTriệt tiêu hoàn toàn cần biên độ bằng nhau. Hai nguồn khác biên độ có cực tiểu nhưng cường độ cực tiểu còn dương.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 35. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "chiet-suat": "Snell dùng góc đo từ pháp tuyến: $n_1\\sin\\theta_1=n_2\\sin\\theta_2$. Phản xạ toàn phần cần $n_1>n_2$ và góc tới vượt góc giới hạn.\n\nĐường quang của đoạn trong môi trường đồng nhất là n nhân chiều dài hình học. Phân biệt tốc độ pha dùng trong định nghĩa với tốc độ nhóm khi xét xung trong môi trường tán sắc.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 33. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "nhieu-xa-anh-sang": "Khe rộng a trong miền Fraunhofer có cực tiểu $a\\sin\\theta=m\\lambda$ với m nguyên khác không. Cường độ tại tâm lấy bằng giới hạn của biểu thức sinc bình phương.\n\nKhẩu độ tròn có cực tiểu đầu gần $1.22\\lambda/D$. Tiêu chuẩn Rayleigh là quy ước cho hai nguồn điểm không kết hợp trong mô hình nhiễu xạ giới hạn, không thay mọi tiêu chí xử lý ảnh.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 36. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "thuyet-tuong-doi-hep": "Hệ số $\\gamma=1/\\sqrt{1-v^2/c^2}$ áp dụng cho $|v|<c$. Cần xác định đúng thời gian riêng và chiều dài riêng trước khi dùng giãn thời gian hoặc co chiều dài.\n\nĐộng lượng $\\mathbf p=\\gamma m\\mathbf v$ và năng lượng $E=\\gamma mc^2$ trở về gần đúng Newton khi vận tốc nhỏ. Trọng trường và các bài toán rộng hơn cần lý thuyết tương đối rộng.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 37. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "photon": "Đơn vị electronvolt là năng lượng, không phải điện áp. Khi dùng h theo joule giây, cần đổi năng lượng sang joule hoặc đổi h sang hệ electronvolt phù hợp.\n\nMột photon không được mô tả đầy đủ bằng hạt cổ điển có quỹ đạo luôn xác định; các lần phát hiện riêng lẻ có thể tạo phân bố giao thoa. Quang điện một photon cần xét công thoát và tần số ngưỡng.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 38. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "ham-song-luong-tu": "Trong một chiều, $\\int|\\Psi|^2dx=1$ và $P(a\\le x\\le b)=\\int_a^b|\\Psi|^2dx$. Hàm sóng có thể phức; pha tương đối ảnh hưởng giao thoa dù pha tổng thể không đổi xác suất.\n\nTrạng thái dừng có pha thời gian nhưng mật độ xác suất giữ nguyên. Điều kiện biên của bài toán quyết định miền được phép và các mức năng lượng; không dùng cùng nghiệm cho hộp vô hạn và giếng hữu hạn.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 40. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "spin-luong-tu": "Với electron, $s=1/2$, $m_s=\\pm1/2$ và thành phần $S_z=m_s\\hbar$. Độ lớn mômen spin liên hệ $\\sqrt{s(s+1)}\\hbar$, khác chỉ độ lớn thành phần trên trục.\n\nKhông thể nói mọi thành phần spin theo các trục đều sắc nét trong cùng một trạng thái. Phân biệt spin với mômen động lượng orbital do cấu trúc không gian của hàm sóng.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 41. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "nguyen-ly-pauli": "Nguyên lý loại trừ áp dụng cho fermion giống nhau; electron là fermion. Các boson không tuân cùng quy tắc chiếm trạng thái này.\n\nVới lớp chính n, các orbital được đếm qua những giá trị orbital và thành phần cho tối đa $2n^2$ electron. Việc đếm số trạng thái không tự xác định thứ tự năng lượng của nguyên tử nhiều electron.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 41. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "vung-nang-luong": "Độ dẫn phụ thuộc cả cấu trúc vùng, mức điền trạng thái và các cơ chế tán xạ. Không chỉ so khoảng cấm mà bỏ mật độ hạt tải hoặc nhiệt độ.\n\nPha tạp tạo các mức chất cho hoặc nhận và điều chỉnh hạt tải. Lỗ trống là mô tả hiệu dụng của trạng thái thiếu electron trong vùng gần đầy, không phải một proton chuyển động trong tinh thể.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 42. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương.",
  "phan-ra-phong-xa": "$N(t)=N_0e^{-\\lambda_dt}$, $T_{1/2}=\\ln2/\\lambda_d$ và hoạt độ $\\mathcal A=\\lambda_dN$. Đơn vị becquerel dùng thời gian tính bằng giây.\n\nHoạt độ không phải liều hấp thụ. Phân rã alpha, beta và gamma cần xét loại hạt phát ra và những định luật bảo toàn phù hợp; phát gamma thuần túy không đổi số proton và neutron.\n\nNguồn: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 43. Bài giảng tương ứng trong Vật lý đại cương 1 hoặc 2 ghi đầy đủ các mục và trang của chương."
}

export const physicsWikiConnections = {
  ...physicsMotionWikiConnections,
  "dong-luong-vat-ly": [
    "luc",
    "cong-nang-luong",
    "vector"
  ],
  "momen-luc": [
    "luc",
    "momen-quan-tinh",
    "dong-luong-vat-ly"
  ],
  "momen-quan-tinh": [
    "momen-luc",
    "cong-nang-luong",
    "dao-dong-dieu-hoa"
  ],
  "dao-dong-dieu-hoa": [
    "cong-nang-luong",
    "pha-song",
    "song"
  ],
  "nhiet-do-tuyet-doi": [
    "khi-ly-tuong",
    "noi-nang",
    "entropy-nhiet-dong"
  ],
  "khi-ly-tuong": [
    "nhiet-do-tuyet-doi",
    "noi-nang",
    "entropy-nhiet-dong"
  ],
  "noi-nang": [
    "cong-nang-luong",
    "khi-ly-tuong",
    "entropy-nhiet-dong"
  ],
  "entropy-nhiet-dong": [
    "noi-nang",
    "nhiet-do-tuyet-doi",
    "khi-ly-tuong"
  ],
  "dien-truong": [
    "dien-tich",
    "dien-the",
    "thong-luong"
  ],
  "dien-dung": [
    "dien-the",
    "dien-truong",
    "cong-nang-luong"
  ],
  "dong-dien": [
    "dien-tich",
    "dien-tro",
    "dien-the"
  ],
  "dien-tro": [
    "dong-dien",
    "dien-the",
    "cong-nang-luong"
  ],
  "tu-truong": [
    "dong-dien",
    "cam-ung-dien-tu",
    "vector"
  ],
  "cam-ung-dien-tu": [
    "tu-truong",
    "thong-luong",
    "tu-cam"
  ],
  "tu-cam": [
    "cam-ung-dien-tu",
    "dong-dien",
    "dien-dung"
  ],
  "pha-song": [
    "song",
    "dao-dong-dieu-hoa",
    "giao-thoa-song"
  ],
  "giao-thoa-song": [
    "pha-song",
    "song",
    "nhieu-xa-anh-sang"
  ],
  "chiet-suat": [
    "song",
    "giao-thoa-song",
    "nhieu-xa-anh-sang"
  ],
  "nhieu-xa-anh-sang": [
    "giao-thoa-song",
    "chiet-suat",
    "photon"
  ],
  "thuyet-tuong-doi-hep": [
    "dong-luong-vat-ly",
    "cong-nang-luong",
    "photon"
  ],
  "photon": [
    "song",
    "thuyet-tuong-doi-hep",
    "ham-song-luong-tu"
  ],
  "ham-song-luong-tu": [
    "photon",
    "tich-phan",
    "nguyen-ly-pauli"
  ],
  "spin-luong-tu": [
    "ham-song-luong-tu",
    "nguyen-ly-pauli",
    "tu-truong"
  ],
  "nguyen-ly-pauli": [
    "spin-luong-tu",
    "ham-song-luong-tu",
    "vung-nang-luong"
  ],
  "vung-nang-luong": [
    "nguyen-ly-pauli",
    "ham-song-luong-tu",
    "dong-dien"
  ],
  "phan-ra-phong-xa": [
    "photon",
    "thuyet-tuong-doi-hep",
    "cong-nang-luong"
  ]
}
