/** Presentation-only feedback editing. The imported question, options and key stay intact. */
const SOURCE_NARRATOR = /^(?:theo (?:bản )?nguồn,?\s*|(?:bản )?nguồn\s+(?!gốc\b|lực\b|lý luận\b|tri thức\b|vận động\b|nội dung\b|phát sinh\b|thông tin\b|tôn giáo\b))/iu
const META_ONLY = /^(?:đúng (?:cả |hai |ba |tên|nhóm|cấp độ|trình tự|thời điểm|thứ tự|tiến trình|căn cứ|giới hạn|tác giả|quốc gia|chuỗi|nội dung|vai trò|hình thức)|khớp |giữ (?:đúng |cả |cách |bối cảnh |mốc)|đây là (?:nội dung|căn cứ|cách|phạm vi|trục|lý do|ba phương diện)|câu (?:chỉ |kiểm tra |không |giữ )|không (?:hiệu chỉnh|cập nhật)|đối chiếu trang|trang \d)/iu
const SOURCE_SUFFIX = /\s+(?:(?:mà|được|do)\s+)?(?:bản )?nguồn\s+(?:trực tiếp\s+)?(?:đã\s+)?(?:còn\s+)?(?:nêu|ghi(?: nhận)?|nhấn(?: mạnh)?|mô tả|trình bày|xác định|thừa nhận|liệt kê|giới thiệu|đưa ra|dùng làm căn cứ đánh giá|dùng|bác|tiếp theo|yêu cầu|phân biệt|xác nhận)(?:\s+(?:trực tiếp|riêng|ở đây))?\s*$/iu

// These clauses contain knowledge, so edit their grammar rather than deleting "nguồn".
const SENTENCE_EDITS = new Map([
  ['Nguồn cho Apeirôn luôn vận động', 'Apeirôn được quan niệm là luôn vận động'],
  ['Nguồn nói không khác về chất', 'Các nguyên tử được quan niệm là không khác nhau về chất'],
  ['Nguồn vẫn thừa nhận cân bằng tương đối', 'Đứng im là sự cân bằng tương đối'],
  ['Nguồn bác cách đặt nguyên nhân cuối cùng ngoài thế giới vật chất', 'Không thể đặt nguyên nhân cuối cùng ở ngoài thế giới vật chất'],
  ['Nguồn phủ nhận dạng thuần túy tách ngẫu nhiên', 'Tất nhiên không tồn tại thuần túy, tách khỏi ngẫu nhiên'],
  ['Nguồn nói tất nhiên không tồn tại thuần túy như vậy', 'Tất nhiên không tồn tại thuần túy, tách khỏi ngẫu nhiên'],
  ['Nguồn nói vai trò không ngang nhau', 'Các khả năng không giữ vai trò ngang nhau'],
  ['Nguồn cho phép hình thức có thể được thực hiện', 'Khả năng hình thức vẫn có thể trở thành hiện thực khi có điều kiện phù hợp'],
  ['Nguồn có cả hướng xuống thấp', 'Sự biến đổi còn có thể theo hướng đi xuống'],
  ['Nguồn gắn với 1843', 'Tác phẩm này gắn với năm 1843'],
  ['Nguồn gắn với 1875', 'Tác phẩm này gắn với năm 1875'],
  ['Nguồn gắn công trình về gia đình, tư hữu, nhà nước với 1884, không 1859', 'Công trình về gia đình, tư hữu và nhà nước gắn với năm 1884, khác mốc 1859'],
  ['Nguồn nêu tôn giáo thường dùng duy tâm luận chứng', 'Tôn giáo thường sử dụng chủ nghĩa duy tâm để luận chứng cho quan điểm của mình'],
  ['Nguồn không yêu cầu xóa vai trò ý thức', 'Thừa nhận vật chất quyết định ý thức không có nghĩa xóa bỏ vai trò của ý thức'],
  ['Nguồn không nói đồng nhất hay bất biến', 'Những quan hệ ấy không đồng nhất và không bất biến'],
  ['Nguồn nêu quan hệ, không nói đồng nhất', 'Các phương diện có quan hệ với nhau nhưng không đồng nhất'],
  ['Nguồn nêu sự phát triển của tri thức, niềm tin và định hướng, không tất định theo tuổi', 'Sự trưởng thành của thế giới quan gắn với tri thức, niềm tin và định hướng, không tự được quyết định bởi tuổi tác'],
  ['Đây là bình diện lượng trong nguồn', 'Đây là phương diện lượng của vận động'],
  ['Nguồn nội dung khách quan thống nhất với xử lý sáng tạo', 'Nội dung có cơ sở khách quan và được chủ thể xử lý sáng tạo'],
])

const PHRASE_EDITS = [
  [/\bBản nguồn gắn cách dùng thuật ngữ triết học với Xôcrát/gu, 'Cách dùng thuật ngữ triết học gắn với Xôcrát'],
  [/\bBản nguồn gắn thuật ngữ triết gia với Hêraclit/gu, 'Thuật ngữ triết gia gắn với Hêraclit'],
  [/\bBản nguồn xếp nhị nguyên xét đến cùng thuộc duy tâm/gu, 'Nhị nguyên luận xét đến cùng được xếp vào chủ nghĩa duy tâm'],
  [/\bTheo nguồn, lôgíc phát triển xã hội/gu, 'Trong quan niệm Mác – Lênin, lôgíc phát triển xã hội'],
  [/\bNguồn truy quan niệm về Êpiquya/gu, 'Quan niệm này được gắn với Êpiquya'],
  [/\bNguồn nối đấu tranh Xilêdi với Đồng minh những người chính nghĩa/gu, 'Đấu tranh Xilêdi gắn với Đồng minh những người chính nghĩa'],
  [/\bNguồn nêu hướng cách mạng tư sản dân quyền/gu, 'Đường lối cách mạng hướng từ cách mạng tư sản dân quyền'],
  [/\bNguồn tôn giáo ban đầu từ sức mạnh thiên nhiên/gu, 'Nguồn gốc ban đầu của tôn giáo gắn với sức mạnh thiên nhiên'],
  [/\bnguồn duy vật lý luận/giu, 'Cơ sở lý luận duy vật'],
  [/\bnguồn thuật ngữ/giu, 'sự ra đời của thuật ngữ'],
  [/\bnguồn tư tưởng/giu, 'sự hình thành tư tưởng'],
  [/\bnguồn trước/giu, 'học thuyết trước'],
  [/\bnguồn phổ biến/giu, 'nguồn gốc phổ biến của vận động'],
  [/\bnguồn ngoài vật chất/giu, 'nguồn gốc ở ngoài vật chất'],
  [/\bnguồn thay đổi/giu, 'nguồn gốc của sự thay đổi'],
  [/\bnguồn vận động/giu, 'nguồn gốc vận động'],
  [/\bnguồn nội dung/giu, 'cơ sở của nội dung'],
  [/\bnguồn hình ảnh/giu, 'cơ sở hình thành hình ảnh'],
  [/\bnguồn thông tin khách quan/giu, 'cơ sở thông tin khách quan'],
  [/\bnguồn phát sinh/giu, 'nguyên nhân phát sinh'],
  [/\bđoạn nguồn gốc nhận thức/giu, 'nguồn gốc nhận thức của triết học'],
  [/\btheo (?:bản )?nguồn\b/giu, ''],
  [/\btrong (?:bản )?nguồn\b/giu, ''],
  [/\bcủa (?:bản )?nguồn\b/giu, ''],
  [/\bở (?:đoạn )?nguồn\b/giu, ''],
  [/\bđoạn nguồn tiếp theo\b/giu, 'sự tác động qua lại giữa lý luận và thực tiễn'],
  [/\bdữ kiện quyết định là\s*/giu, ''],
  [/\bdữ kiện thể hiện\s*/giu, ''],
  [/\bdữ kiện yêu cầu\s*/giu, 'Cần'],
  [/\bđề đã (?:nêu|xác định)\s*/giu, ''],
  [/\bđề nêu\s*/giu, ''],
  [/\bdữ kiện\b/giu, 'thông tin'],
]

// Reviewed exceptions: the original wording is entirely editorial, or dropping it
// would lose the actual distinction. These edits add no facts to the question bank.
const REVIEWED_FEEDBACK = {
  CH010: { explanation: 'Trong truyền thống Trung Quốc, chữ triết gắn với sự hiểu biết sâu sắc về bản chất của con người, xã hội và vũ trụ, đồng thời định hướng nhân sinh quan.' },
  CH027: { distractors: { A: 'Vẫn giữ tham vọng biến triết học thành khoa học của mọi khoa học, thay vì xác định phạm vi nghiên cứu chung nhất.' } },
  CH033: { explanation: 'Lý tưởng là trình độ phát triển cao nhất của thế giới quan. Tri thức giữ vai trò cơ sở trực tiếp, còn lý tưởng thể hiện phương hướng giá trị mà con người theo đuổi.' },
  CH093: { explanation: 'Thực tiễn cách mạng của giai cấp vô sản là cơ sở thực tiễn chủ yếu nhất cho sự ra đời triết học Mác. Cần phân biệt cơ sở thực tiễn với những nguồn lý luận được kế thừa.' },
  CH095: { explanation: 'Triết học cổ điển Đức là nguồn lý luận trực tiếp của triết học Mác. Ba nguồn lý luận của toàn bộ chủ nghĩa Mác không đồng nhất với nguồn lý luận trực tiếp của riêng bộ phận triết học.' },
  CH021: { explanation: 'Đối tượng của triết học thay đổi trong lịch sử cùng sự phát triển của tri thức và sự phân hóa của các khoa học. Việc các ngành khoa học tách ra không làm mất nhiệm vụ nghiên cứu những vấn đề chung nhất của triết học.' },
  CH101: { distractors: { A: 'Nguồn lý luận trực tiếp của triết học Mác là triết học cổ điển Đức, khác với tiền đề khoa học tự nhiên.' } },
  CH110: { takeaway: 'Cần phân biệt năm sinh, thời điểm nhận bằng tiến sĩ và thời điểm bước ngoặt trong hoạt động báo chí của Mác.' },
  CH111: { distractors: { C: 'Bỏ qua tác động trực tiếp của hoạt động thực tiễn đối với sự chuyển biến tư tưởng của Mác.' } },
  CH119: { distractors: { D: 'Công trình này phê phán Smith và Ricardo, khác với việc phê phán Cáclây từ sự đối lập về lập trường chính trị.' } },
  CH123: { distractors: { A: 'Nhầm mốc xuất bản Gia đình thần thánh với thời gian xuất bản Niên giám Pháp–Đức, dù nội dung đóng góp được ghép đúng.' } },
  CH147: { explanation: 'Triết học gắn với phong trào vô sản trở thành vũ khí tinh thần để nhận thức và cải tạo hiện thực. Lý luận góp phần đưa phong trào từ tự phát lên tự giác.' },
  CH172: { takeaway: 'Nghiên cứu giai đoạn đế quốc chủ nghĩa gắn việc phân tích điều kiện thời đại với phát triển lý luận cách mạng.' },
  CH176: { takeaway: 'Chủ nghĩa xã hội và chủ nghĩa cộng sản được phân biệt thành hai giai đoạn của xã hội cộng sản chủ nghĩa.' },
  CH181: { explanation: 'Tác phẩm Cách mạng vô sản và tên phản bội Causky phê phán việc phủ nhận chuyên chính vô sản, phân biệt dân chủ tư sản với dân chủ vô sản và làm rõ vai trò của Nhà nước Xô viết.', distractors: { B: 'Định nghĩa giai cấp là đóng góp gắn với Sáng kiến vĩ đại, khác trọng tâm phân tích dân chủ và chuyên chính của tác phẩm đang xét.' } },
  CH184: { distractors: { C: 'Bỏ qua việc xem xét những điều kiện của cách mạng khi phân tích quan hệ lãnh đạo và quần chúng.' } },
  CH197: { takeaway: 'Vận dụng sáng tạo đòi hỏi xuất phát từ điều kiện lịch sử cụ thể của Việt Nam, thay vì sao chép một tiến trình khác.' },
  CH221: { takeaway: 'Khả năng định hướng của nguyên lý triết học dựa trên sự khái quát những thuộc tính và mối liên hệ phổ biến của hiện thực.' },
  CH224: { takeaway: 'Tôn trọng tự do tín ngưỡng cần đi cùng việc nhận thức và khắc phục những nguyên nhân vật chất, xã hội, thay vì chỉ cấm đoán.' },
  CH228: { explanation: 'Quan hệ sản xuất lạc hậu có thể kìm hãm lực lượng sản xuất. Sự không đồng bộ hoặc những yếu tố đi quá xa so với trình độ lực lượng sản xuất cũng có thể gây cản trở.' },
  CH234: { explanation: 'Hợp tác và đấu tranh cùng tồn tại trong đời sống quốc tế. Các mâu thuẫn của thời đại tiếp tục tồn tại nhưng có những đặc điểm và hình thức mới.' },
  CH258: { explanation: 'Khó khăn và thoái trào của chủ nghĩa xã hội không đồng nghĩa các phong trào công nhân, xã hội chủ nghĩa và độc lập dân tộc mất hẳn. Cần phân biệt sự suy giảm với việc chấm dứt tồn tại.' },
  CH267: { distractors: { B: 'Nhận thức, giáo dục, dự báo và phê phán cũng là các chức năng của triết học Mác–Lênin, dù không phải hai chức năng cơ bản.' } },
  CH274: { distractors: { A: 'Đặt yêu cầu phải biết hết thế giới trước khi có thế giới quan, trong khi tri thức hữu hạn vẫn phải đáp ứng nhu cầu định hướng hành động.' } },
  CH268: { explanation: 'Góp phần phê phán kinh tế chính trị học gắn với năm 1859, Tuyên ngôn của Đảng Cộng sản gắn với năm 1848 và Phê phán Cương lĩnh Gôta gắn với năm 1875. Cần phân biệt ba công trình và thời điểm của chúng.' },
  CH298: { explanation: 'Tính chỉnh thể và sự hợp tác quốc tế tăng lên không làm mất những mâu thuẫn về lợi ích. Sự liên kết và sự đấu tranh cần được xem xét trong cùng bối cảnh lịch sử.', takeaway: 'Phân tích thời đại cần xét đồng thời các mối liên hệ hợp tác và những mâu thuẫn lợi ích.' },
  CH306: { distractors: { A: 'Phân chia theo dân tộc sử dụng căn cứ cộng đồng, khác với việc phân biệt các hình thức tôn giáo, khoa học và triết học.' } },
  CH313: { distractors: { A: 'Đây là các đại biểu của chủ nghĩa xã hội không tưởng Pháp, khác với kinh tế chính trị học cổ điển Anh.', D: 'Đây là các đại biểu của triết học cổ điển Đức, khác với kinh tế chính trị học cổ điển Anh.' } },
  CH314: { takeaway: 'Các nguồn lý luận cần được phân biệt theo lĩnh vực và đại biểu, dù đều có ảnh hưởng đến sự hình thành chủ nghĩa Mác.' },
  CH316: { distractors: { D: 'Phép biện chứng Hêghen thuộc nguồn lý luận triết học, khác với những phát minh khoa học tự nhiên.' } },
  CH324: { takeaway: 'Khẳng định vai trò của quần chúng nhân dân không có nghĩa xóa bỏ vai trò của cá nhân trong lịch sử.' },
  CH330: { takeaway: 'Tình thế và thời cơ cách mạng là những vấn đề được phát triển trong Bệnh ấu trĩ “tả khuynh” trong phong trào cộng sản.', distractors: { A: 'Đây là tác phẩm của Ăngghen, khác với công trình của Lênin đang được hỏi.' } },
  CH335: { explanation: 'Khoa học hiện đại đặt ra những vấn đề mới, đòi hỏi triết học Mác–Lênin tiếp tục phát triển. Triết học cung cấp cơ sở phương pháp luận, còn những thành tựu khoa học góp phần bổ sung và phát triển triết học.' },
  CH337: { takeaway: 'Một kết luận lý luận về xu hướng phát triển không phải dự báo một lịch trình cụ thể và tự động.', distractors: { B: 'Thêm giả định mọi nơi thay đổi đồng thời theo một lịch trình định sẵn, trong khi nhận định về xu hướng không bao hàm những điều ấy.' } },
  CH340: { explanation: 'Triết học Mác–Lênin là thế giới quan và phương pháp luận của giai cấp công nhân, nhân dân lao động và những lực lượng tiến bộ trong việc nhận thức, cải tạo thế giới.' },
  Q007: { takeaway: 'Cần phân biệt việc phát hiện điện tử với việc nghiên cứu sự biến đổi của khối lượng điện tử.' },
  Q009: { takeaway: 'Thuyết tương đối hẹp và thuyết tương đối tổng quát là hai thành tựu khác nhau, cần phân biệt khi xác định các mốc lịch sử.' },
  Q022: { explanation: 'Tiêu chí tồn tại khách quan giúp nhận diện những quan hệ vật chất trong xã hội, qua đó gắn chủ nghĩa duy vật biện chứng với chủ nghĩa duy vật lịch sử.', distractors: { D: 'Việc con người tham gia tạo lập các quan hệ xã hội không làm mất tính khách quan của những quan hệ ấy.' } },
  Q024: { takeaway: 'Cần phân biệt những quan điểm duy tâm trong khủng hoảng vật lý với sự thay đổi của bản thân tri thức khoa học.' },
  Q061: { takeaway: 'Các trình độ phản ánh sinh học gắn với mức độ tổ chức và sự phát triển của cơ quan phản ánh.' },
  Q088: { explanation: 'Giấc mơ và nói nhịu là những ví dụ về vô thức. Việc phân tích vô thức gắn với vấn đề giải tỏa ức chế và cân bằng hoạt động tinh thần, khác với những thao tác tư duy được thực hiện có chủ đích.', takeaway: 'Cần phân biệt hiện tượng tâm lý không được ý thức trực tiếp kiểm soát với sự điều chỉnh có chủ đích.' },
  Q100: { explanation: 'Ý thức có cơ sở vật chất ở bộ óc người, còn sự hình thành con người gắn với quá trình tiến hóa tự nhiên. Không thể đảo quan hệ ấy thành ý thức tạo ra bộ óc hay giới tự nhiên.', takeaway: 'Giải thích nguồn gốc ý thức cần gắn bộ óc người với sự phát triển của giới tự nhiên.' },
  Q157: { takeaway: 'Tiến hóa nhấn mạnh cách thức phát triển từ từ, khác với việc đồng nhất mọi biến đổi với sự tiến bộ.' },
  Q159: { explanation: 'Cách hiểu siêu hình giản lược biến đổi thành tăng giảm về lượng hoặc lặp lại, đồng thời đặt nguồn gốc biến đổi ở ngoài đối tượng. Nó bỏ qua biến đổi về chất và động lực nội tại.', distractors: { B: 'Cách nhìn này thừa nhận vận động và sự chuyển hóa về chất, phù hợp với quan điểm biện chứng.' } },
  Q174: { takeaway: 'Cách giải thích tiến hóa ở đây nhấn mạnh sự sống sót và thích ứng, cần được phân biệt với tiêu chí đánh giá tiến bộ.', distractors: { B: 'Thay trọng tâm sống sót và thích ứng bằng một đặc điểm khác, nên không diễn đạt đúng cách giải thích tiến hóa đang xét.' } },
  Q180: { takeaway: 'Các cặp phạm trù giúp định hướng những phương pháp nhận thức như phân tích, tổng hợp, diễn dịch, quy nạp, khái quát hóa và trừu tượng hóa.' },
  Q186: { explanation: 'Duy thực đặt cái chung tồn tại độc lập, không phụ thuộc cái riêng. Đây là sự tách rời khác với quan điểm duy vật biện chứng rằng cái chung tồn tại trong và thông qua cái riêng.' },
  Q293: { takeaway: 'Có thể phân biệt khả năng theo việc nó liên quan đến biến đổi về chất hay biến đổi về lượng.', distractors: { D: 'Giới hạn cách phân loại quá hẹp, bỏ qua việc khả năng có thể gắn với những dạng biến đổi khác nhau.' } },
  Q339: { explanation: 'Tính khách quan của phủ định biện chứng thể hiện ở cơ sở nội tại của sự phủ định. Tính kế thừa thể hiện ở việc những yếu tố còn phù hợp của cái cũ được giữ lại và cải tạo trong cái mới.', distractors: { B: 'Thừa nhận cơ sở nội tại của phủ định nhưng hiểu sai tính kế thừa: Kế thừa không phải giữ nguyên mọi yếu tố của cái cũ.' } },
  Q379: { distractors: { A: 'Tách thực nghiệm khoa học khỏi việc vận dụng kết quả để cải tạo hiện thực, trong khi hai mặt có quan hệ với nhau.' } },
  Q415: { takeaway: 'Cần phân biệt mức phản ánh đầy đủ trong một phạm vi xác định với việc biết trọn vẹn mọi hiện thực.' },
  Q421: { takeaway: 'Tứ đại và ngũ hành đều giải thích khởi nguyên bằng những dạng vật chất cụ thể, nhưng có các yếu tố thành phần khác nhau.' },
  Q423: { distractors: { A: 'Phủ nhận sạch những cố gắng phê phán thuyết nguyên tử, dù các cố gắng ấy chưa vượt căn bản cách nhìn cơ học.' } },
  Q433: { explanation: 'Biến đổi về lượng có thể là tăng hoặc giảm. Sự chuyển hóa về chất phụ thuộc giới hạn của độ, điểm nút và điều kiện cụ thể, không chỉ phụ thuộc dấu tăng hay giảm.', distractors: { C: 'Bỏ qua giới hạn của độ khi cho rằng lượng vừa giảm thì chất lập tức thay đổi.' } },
  Q439: { takeaway: 'Phân loại theo lượng và chất khác với phân loại theo nội dung và mức độ phổ quát, nên không thể tráo tiêu chí hoặc số lượng giữa hai cách chia.' },
}

function prose(text) {
  let result = String(text || '').normalize('NFC')
    .replace(/\[([^\]]+)\]\([^)]+\)/gu, '$1')
    .replace(/\*\*|__|`/gu, '')
    .replace(/\s*→\s*/gu, '. ')
    .replace(/\s*;\s*/gu, '. ')
    .replace(/\s+/gu, ' ').trim()
  result = result.replace(/(?:^|\s)(?:trang(?: in\/PDF)?|tr\.|PDF)\s*\d+(?:\s*[–—-]\s*\d+)?(?:\s*[,–-]\s*\d+)*/giu, '')
  result = result.replace(/\s+([,.!?])/gu, '$1').replace(/([!?])\./gu, '$1').replace(/\.{2,}/gu, '.').replace(/^[\s,.]+|[\s,]+$/gu, '').trim()
  result = result.replace(/(^|[.!?]\s+|:\s*)(\p{Ll})/gu, (_, prefix, letter) => prefix + letter.toLocaleUpperCase('vi'))
  return result && !/[.!?…]$/u.test(result) ? `${result}.` : result
}

function clauses(text) {
  return text.replace(/\b(C|Ph|V\.I|V|I|A|Đ)\.\s+/gu, '$1\uE000 ')
    .split(/;|(?<=[.!?])\s+(?=[\p{Lu}\d“"])/u)
    .map(part => part.replace(/\uE000/gu, '.').replace(/[.\s]+$/gu, '').trim()).filter(Boolean)
}

function cleanClause(text, hasKnowledge) {
  let clause = text.trim()
  if (SENTENCE_EDITS.has(clause)) return SENTENCE_EDITS.get(clause)
  for (const [pattern, replacement] of PHRASE_EDITS) clause = clause.replace(pattern, replacement)
  if (META_ONLY.test(clause) && /nguồn|trang|giáo trình|tài liệu|đoạn|câu |bản /iu.test(text)) return ''
  if (/^(?:cả |đúng |khớp ).*\bkhớp(?:\s+trang\s*\d.*)?$/iu.test(clause)) return ''
  if (/^(?:Hai|Ba) mốc khớp$/iu.test(clause)) return ''
  // Source narration often repeats the answer verbatim. Keep the answer's knowledge instead.
  if (SOURCE_NARRATOR.test(clause)) {
    if (hasKnowledge) return ''
    clause = clause.replace(/^(?:theo (?:bản )?nguồn,?\s*|(?:bản )?nguồn\s+(?:trực tiếp\s+)?(?:nêu|ghi(?: nhận)?|cho (?:rằng )?|khẳng định|xác định|nhấn(?: mạnh)?|mô tả|trình bày)\s*)/iu, '')
  }
  clause = clause.replace(/^Nguồn phân biệt\s+/u, 'Cần phân biệt ')
    .replace(/^Nguồn không\s+/u, 'Không ')
    .replace(SOURCE_SUFFIX, '')
    .replace(/\s+(?:mà|được)\s*$/iu, '')
    .replace(/\s+(?:khác|trái|đúng|vượt)\s+(?:đoạn )?nguồn\s*$/iu, '')
    .replace(/\s+không có trong nguồn\s*$/iu, '')
    .replace(/\s+không phải (?:đoạn )?nguồn\s*$/iu, '')
    .replace(/\s+nguồn\s*$/iu, '')
    .trim()
  return clause
}

/** Strip authoring/citation scaffolding while preserving the substantive feedback. */
export function cleanQuizFeedback(text, question = null) {
  if (typeof text !== 'string' || !text.trim()) return ''
  let raw = text.trim().normalize('NFC')
  const selection = raw.match(/(?:Vì vậy|Do đó)\s+chọn\s+[ABCD]\s*:\s*([\s\S]+)$/iu)
  const answer = selection?.[1] || ''
  if (selection) raw = raw.slice(0, selection.index).trim()
  raw = raw.replace(/^(?:Nguồn|Dữ kiện\/cách hiểu quyết định)\s*:\s*/iu, '')
    .replace(/\s*→\s*chọn\s+[ABCD][.!]?\s*$/iu, '')
  const knowledge = raw.split(/\s*→\s*kiến thức\s*:\s*/iu)
  const pieces = knowledge.length === 2 ? [knowledge[1], knowledge[0]] : raw.split(/\s*→\s*đối chiếu\s*:\s*/iu)
  const cleaned = []
  for (const part of pieces.flatMap(clauses)) {
    const next = cleanClause(part, Boolean(answer || cleaned.length))
    if (next) cleaned.push(next)
  }
  let content = prose(cleaned.join('. '))
  if (answer) {
    let statement = answer
    for (const [pattern, replacement] of PHRASE_EDITS) statement = statement.replace(pattern, replacement)
    statement = prose(statement)
    content = prose([statement, content].filter(Boolean).join(' '))
  }
  return content
}

/** Clone just the feedback surface. Do not edit user-supplied question text or scoring. */
export function cleanQuestionFeedback(question) {
  if (!question || typeof question !== 'object' || Array.isArray(question)) return question
  const reviewed = REVIEWED_FEEDBACK[question.id] || {}
  return {
    ...question,
    explanation: prose(reviewed.explanation || cleanQuizFeedback(question.explanation, question)),
    distractors: Array.isArray(question.distractors) ? question.distractors.map(item => ({
      ...item, explanation: prose(reviewed.distractors?.[item.key] || cleanQuizFeedback(item.explanation, question)),
    })) : question.distractors,
    takeaway: prose(reviewed.takeaway || cleanQuizFeedback(question.takeaway, question)),
  }
}
