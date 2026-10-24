export const physics1FluidConcepts={
  "ty-khoi": {
    "name": "Tỉ khối",
    "aliases": [
      "tỉ khối",
      "tỷ khối",
      "khối lượng riêng tương đối"
    ],
    "definition": "Tỉ khối là tỉ số khối lượng riêng của một vật liệu và khối lượng riêng của nước ở 4,0 °C: $d=\\rho/\\rho_{\\mathrm w}$. Đây là đại lượng không có đơn vị.",
    "example": "Hai vật có cùng khối lượng riêng thì có cùng tỉ khối dù khối lượng và thể tích của chúng khác nhau.",
    "use": "So sánh khối lượng riêng của các vật liệu bằng cùng một giá trị tham chiếu.",
    "question": "Tỉ khối có cùng đơn vị với khối lượng riêng không?",
    "answer": "Không. Hai đơn vị khối lượng riêng triệt tiêu trong tỉ số, nên tỉ khối không có đơn vị."
  },
  "nguyen-ly-pascal": {
    "name": "Nguyên lý Pascal",
    "aliases": [
      "nguyên lý Pascal",
      "định luật Pascal"
    ],
    "definition": "Độ tăng áp suất tác dụng lên chất lưu kín được truyền nguyên vẹn tới mọi phần chất lưu và thành bình trong mô hình cân bằng với khối lượng riêng không đổi.",
    "example": "Hai pít-tông ở cùng cao độ chịu cùng phần áp suất tăng thêm. Pít-tông có diện tích lớn hơn chịu lực lớn hơn theo cùng tỉ lệ diện tích.",
    "use": "Liên hệ lực và diện tích trong máy nâng, kích và phanh thủy lực.",
    "question": "Nguyên lý Pascal có nói áp suất tuyệt đối ở mọi độ sâu đều bằng nhau không?",
    "answer": "Không. Phần áp suất tăng thêm được truyền nguyên vẹn. Áp suất tổng vẫn có thể khác nhau do chênh cao trong trọng trường."
  },
  "ap-suat-tuyet-doi-va-ap-suat-du": {
    "name": "Áp suất tuyệt đối và áp suất dư",
    "aliases": [
      "áp suất tuyệt đối",
      "áp suất dư",
      "áp suất tương đối"
    ],
    "definition": "Áp suất dư là hiệu giữa áp suất tuyệt đối và áp suất khí quyển tại nơi đo: $p_{\\mathrm g}=p-p_{\\mathrm{atm}}$. Áp suất dư có thể âm.",
    "example": "Một bình có áp suất bằng áp suất khí quyển có áp suất dư bằng không, trong khi áp suất tuyệt đối vẫn bằng áp suất khí quyển.",
    "use": "Đọc áp kế, so sánh áp suất trong và ngoài bình, hoặc xác định điều kiện biên trong bài dòng chảy.",
    "question": "Áp suất dư âm có đồng nghĩa áp suất tuyệt đối âm không?",
    "answer": "Không. Nó chỉ có nghĩa áp suất tuyệt đối thấp hơn áp suất khí quyển được chọn làm mốc."
  },
  "suc-cang-be-mat": {
    "name": "Sức căng bề mặt",
    "aliases": [
      "sức căng bề mặt",
      "căng bề mặt"
    ],
    "definition": "Sức căng bề mặt là biểu hiện của lực liên kết phân tử làm bề mặt chất lỏng có xu hướng giảm diện tích và chống lại sự kéo giãn.",
    "example": "Một kẹp giấy đặt nhẹ có thể được mặt nước giữ dù khối lượng riêng vật liệu của nó lớn hơn khối lượng riêng nước.",
    "use": "Mô tả giọt nhỏ và các hiện tượng mà hiệu ứng bề mặt không thể bỏ qua.",
    "question": "Lực nổi Archimedes có đủ để giải thích mọi vật được giữ trên mặt nước không?",
    "answer": "Không. Khi hiệu ứng bề mặt đáng kể, phải xét cả tác dụng của sức căng bề mặt."
  },
  "chat-luu-ly-tuong": {
    "name": "Chất lưu lý tưởng",
    "aliases": [
      "chất lưu lý tưởng",
      "dòng chất lưu lý tưởng"
    ],
    "definition": "Chất lưu lý tưởng là mô hình chất lưu không nén được và không có ma sát bên trong. Khối lượng riêng không thay đổi trong chuyển động của phần tử chất lưu.",
    "example": "Dòng nước trong ống có thể được xấp xỉ bằng mô hình lý tưởng khi biến đổi khối lượng riêng và tác dụng nhớt nhỏ trong phạm vi đang xét.",
    "use": "Xác định điều kiện của phương trình liên tục không nén được và phương trình Bernoulli không tổn hao.",
    "question": "Chất lưu lý tưởng có bắt buộc đứng yên không?",
    "answer": "Không. Chất lưu lý tưởng vẫn có thể chuyển động và có gia tốc. Tính ổn định của dòng là một giả thiết khác."
  },
  "do-nhot-chat-luu": {
    "name": "Độ nhớt chất lưu",
    "aliases": [
      "độ nhớt",
      "ma sát bên trong chất lưu",
      "lực nhớt"
    ],
    "definition": "Độ nhớt đặc trưng ma sát bên trong chất lưu. Lực nhớt chống lại chuyển động tương đối giữa các phần chất lưu.",
    "example": "Dòng chất lỏng nhớt trong một ống trụ có tốc độ nhỏ gần thành và lớn hơn ở vùng giữa ống.",
    "use": "Xác định khi nào tác dụng ma sát bên trong và chênh áp duy trì dòng không thể bỏ qua.",
    "question": "Nếu độ nhớt nhỏ, có thể bỏ qua nó trong mọi tình huống không?",
    "answer": "Không. Độ nhớt nhỏ vẫn có thể ảnh hưởng đáng kể đến lớp biên, dòng quanh vật và lực do chất lưu gây ra."
  },
  "chay-tang-va-chay-roi": {
    "name": "Chảy tầng và chảy rối",
    "aliases": [
      "chảy tầng",
      "chảy rối",
      "dòng tầng",
      "dòng rối"
    ],
    "definition": "Chảy tầng có những phần chất lưu trượt êm tương đối. Chảy rối có chuyển động bất quy tắc và trường vận tốc thay đổi theo thời gian trong mô tả của chương.",
    "example": "Dòng khói ban đầu có thể tạo những vệt êm, sau đó chuyển thành dòng nhiều xoáy và biến đổi liên tục.",
    "use": "Đánh giá phạm vi mô hình dòng ổn định lý tưởng và các ảnh hưởng của nhiễu loạn.",
    "question": "Có một tốc độ tới hạn dùng chung cho mọi dòng chất lưu không?",
    "answer": "Không. Sự chuyển sang chảy rối còn phụ thuộc độ nhớt, hình dạng biên và nhiễu loạn của tình huống cụ thể."
  },
  "dong-nhot-trong-ong-tru": {
    "name": "Dòng nhớt trong ống trụ",
    "aliases": [
      "dòng nhớt trong ống trụ",
      "dòng chảy nhớt trong ống"
    ],
    "definition": "Dòng tầng của chất lưu nhớt trong ống trụ dài có vận tốc lớn nhất ở trục và bằng không tại thành. Với cùng chất lưu và lưu lượng, chênh áp cần thiết tỉ lệ $L/R^4$.",
    "example": "Nếu chỉ giảm một nửa bán kính trong của ống, chênh áp cần để duy trì cùng lưu lượng tăng 16 lần trong mô hình này.",
    "use": "So sánh chênh áp khi chiều dài hoặc bán kính ống thay đổi mà lưu lượng và chất lưu được giữ.",
    "question": "Giảm 10% bán kính có làm chênh áp cần thiết chỉ tăng 10% không?",
    "answer": "Không. Với cùng chiều dài và lưu lượng, hệ số tăng là 1/0,9⁴, xấp xỉ 1,52."
  },
  "duong-dong-chat-luu": {
    "name": "Đường dòng chất lưu",
    "aliases": [
      "đường dòng"
    ],
    "definition": "Đường dòng là đường có tiếp tuyến tại mỗi điểm cùng hướng vector vận tốc chất lưu ở thời điểm đang xét. Đường đi của một phần tử mô tả vị trí của chính phần tử đó theo thời gian.",
    "example": "Trong dòng ổn định, các phần tử đi qua cùng một vị trí lần lượt chuyển động theo cùng đường đi. Đường đi khi đó trùng với đường dòng.",
    "use": "Mô tả trường vận tốc và xác định hai điểm của cùng một dòng khi dùng phương trình liên tục hoặc Bernoulli.",
    "question": "Trong dòng không ổn định, đường đi của một phần tử có luôn trùng đường dòng tức thời không?",
    "answer": "Không. Trường vận tốc thay đổi theo thời gian, nên quỹ đạo của phần tử không nhất thiết trùng đường tiếp tuyến tức thời."
  },
  "phuong-trinh-lien-tuc": {
    "name": "Phương trình liên tục",
    "aliases": [
      "phương trình liên tục",
      "bảo toàn lưu lượng khối lượng"
    ],
    "definition": "Hệ thức bảo toàn khối lượng của dòng chất lưu. Với dòng ổn định, khối lượng đi qua các tiết diện của cùng một ống dòng trong cùng thời gian bằng nhau.",
    "example": "Trong một ống có dòng chất lỏng ổn định và không nén được, tiết diện hẹp hơn đi kèm tốc độ trung bình lớn hơn.",
    "use": "Liên hệ tốc độ và tiết diện trước khi áp dụng phương trình năng lượng cho dòng.",
    "question": "Tích tiết diện và tốc độ có luôn bằng nhau cho dòng khí có khối lượng riêng thay đổi không?",
    "answer": "Không. Khi có tính nén, phải giữ cả khối lượng riêng trong biểu thức lưu lượng khối lượng."
  },
  "ong-dong-chat-luu": {
    "name": "Ống dòng chất lưu",
    "aliases": [
      "ống dòng"
    ],
    "definition": "Ống dòng là vùng được giới hạn bởi các đường dòng đi qua đường biên của một tiết diện. Trong dòng ổn định, chất lưu không đi xuyên qua mặt bên của ống dòng.",
    "example": "Hai tiết diện ở hai đầu một ống dòng nhận và đưa đi cùng khối lượng trong cùng thời gian nếu dòng ổn định và không có nhánh cấp hoặc hút.",
    "use": "Chọn vùng khảo sát để áp dụng bảo toàn khối lượng và phương trình năng lượng của dòng.",
    "question": "Ống dòng có nhất thiết là một ống vật chất với thành rắn không?",
    "answer": "Không. Biên ống dòng được dựng từ trường vận tốc và có thể là một mặt tưởng tượng."
  },
  "duong-di-phan-tu-chat-luu": {
    "name": "Đường đi của phần tử chất lưu",
    "aliases": [
      "đường đi phần tử chất lưu",
      "quỹ đạo phần tử chất lưu"
    ],
    "definition": "Đường đi của một phần tử chất lưu là quỹ đạo dựng bằng cách theo dõi vị trí của chính phần tử đó theo thời gian. Nó trùng đường dòng trong dòng ổn định, nhưng không nhất thiết trùng trong dòng không ổn định.",
    "example": "Một hạt đánh dấu rất nhỏ chuyển động cùng nước cho phép theo dõi đường đi của phần nước quanh nó trong mô hình hạt bám theo dòng.",
    "use": "Phân biệt việc theo dõi một phần tử với việc quan sát hướng trường vận tốc tại cùng một thời điểm.",
    "question": "Ảnh trường vận tốc tại một thời điểm có tự cho biết toàn bộ đường đi tương lai của một phần tử không?",
    "answer": "Không. Nếu dòng thay đổi theo thời gian, cần biết sự biến đổi của trường vận tốc sau thời điểm đó."
  },
  "luu-luong-chat-luu": {
    "name": "Lưu lượng chất lưu",
    "aliases": [
      "lưu lượng thể tích",
      "lưu lượng khối lượng"
    ],
    "definition": "Lưu lượng thể tích là thể tích qua một tiết diện trong một đơn vị thời gian. Lưu lượng khối lượng là khối lượng qua tiết diện trong một đơn vị thời gian. Hai đại lượng có đơn vị khác nhau.",
    "example": "Nếu dòng không nén được chảy ổn định qua hai đoạn ống nối tiếp, tốc độ có thể đổi nhưng lưu lượng thể tích không đổi khi không có nhánh trao đổi chất lưu.",
    "use": "Đổi giữa thể tích, khối lượng và tốc độ qua một tiết diện, đồng thời phát biểu đúng bảo toàn dòng.",
    "question": "Dòng khí ổn định có khối lượng riêng thay đổi có bắt buộc bảo toàn lưu lượng thể tích không?",
    "answer": "Không. Lưu lượng khối lượng được bảo toàn trong ống dòng không có nguồn hoặc nhánh hút, còn lưu lượng thể tích có thể thay đổi theo khối lượng riêng."
  }
}
export const physics1FluidWikiDetails={
  "ty-khoi": "Khối lượng riêng của nước tham chiếu ở 4,0 °C xấp xỉ 1000 kg/m³. Nhiệt độ của vật liệu đang xét có thể khác nhiệt độ tham chiếu, vì khối lượng riêng của vật liệu phụ thuộc trạng thái.\n\nVới vật không đồng nhất hoặc vật rỗng, phải phân biệt khối lượng riêng vật liệu với khối lượng riêng trung bình của toàn vật.",
  "nguyen-ly-pascal": "Khi áp suất ở mặt chuẩn tăng một lượng Δp₀, áp suất ở mọi độ sâu tăng cùng lượng đó, nếu khối lượng riêng và trạng thái cân bằng của mô hình được giữ. Sự tăng này không xóa chênh áp do trọng lượng chất lưu.\n\nVới hai pít-tông cùng cao độ, bỏ qua ma sát và khối lượng pít-tông, ta có:\n\n$$\n\\frac{F_1}{A_1}=\\frac{F_2}{A_2}\n$$\n\nCác lực trong hệ thức này tương ứng cùng phần áp suất tăng thêm tác dụng lên hai pít-tông.",
  "ap-suat-tuyet-doi-va-ap-suat-du": "Áp suất tuyệt đối dùng chân không làm mốc, còn áp suất dư dùng áp suất khí quyển tại nơi đo. Hai giá trị liên hệ bởi:\n\n$$\np=p_{\\mathrm{atm}}+p_{\\mathrm g}\n$$\n\nÁp kế ống hở đo chênh áp giữa bình và khí quyển bằng chênh cao cột chất lỏng. Khí áp kế với đỉnh cột gần chân không dùng chiều cao cột thủy ngân để xác định áp suất khí quyển.",
  "suc-cang-be-mat": "Phân tử ở sâu bên trong chất lỏng bị hút từ nhiều phía. Ở bề mặt, môi trường lân cận không đối xứng và bề mặt có xu hướng co lại. Một giọt nhỏ do sức căng chi phối có xu hướng gần hình cầu, vì hình cầu có diện tích nhỏ nhất ở cùng thể tích.\n\nVới hình cầu bán kính r, tỉ số diện tích trên thể tích là:\n\n$$\n\\frac AV=\\frac3r\n$$\n\nDo đó, khi kích thước giảm, hiệu ứng bề mặt tăng tương đối so với những tác dụng gắn với thể tích. Nước nóng và xà phòng làm giảm sức căng trong tình huống giặt rửa. Đối với khối chất lỏng lớn, tác dụng bề mặt thường có thể được bỏ qua so với áp lực và trọng lượng trong mô hình đang xét.",
  "chat-luu-ly-tuong": "Không nén được là giả thiết về khối lượng riêng. Không nhớt là giả thiết bỏ qua ứng suất do ma sát bên trong. Một chất khí vẫn có thể được coi gần như không nén được nếu chênh áp giữa các vùng không lớn.\n\nDòng ổn định có trường vận tốc không đổi theo thời gian tại mỗi vị trí. Vận tốc của một phần tử vẫn có thể đổi khi phần tử đi qua những vị trí khác nhau. Vì vậy, không được đồng nhất dòng ổn định với chuyển động thẳng đều của mọi phần tử.",
  "do-nhot-chat-luu": "Các phần chất lưu chuyển động với vận tốc khác nhau tác dụng lực nhớt lên nhau. Gần một bề mặt rắn, chất lưu có xu hướng bám bề mặt. Trong mô hình không trượt, vận tốc tương đối tại bề mặt bằng không.\n\nỞ những chất được xét, độ nhớt của khí tăng và độ nhớt của chất lỏng giảm khi nhiệt độ tăng. Điều kiện nhiệt độ do đó phải được giữ khi so sánh các quan hệ dòng nhớt.",
  "chay-tang-va-chay-roi": "Nhiễu nhỏ có thể tắt dần trong một dòng tầng ổn định. Khi dòng mất ổn định, nhiễu có thể phát triển và phá vỡ cấu trúc chuyển động êm. Tốc độ lớn, nhám thành và biến đổi hình học có thể ảnh hưởng quá trình này.\n\nChảy tầng không đồng nghĩa độ nhớt bằng không. Dòng nhớt tầng trong ống cần chênh áp để bù tác dụng cản nhớt.",
  "dong-nhot-trong-ong-tru": "Tác dụng nhớt giữa các vùng tốc độ khác nhau cản chuyển động tương đối. Trong ống trụ dài với dòng tầng và điều kiện bám thành, phân bố tốc độ theo bán kính có dạng parabol.\n\nVới cùng chất lưu, nhiệt độ và lưu lượng thể tích, quan hệ được sử dụng trong mục này là:\n\n$$\n\\Delta p\\propto\\frac L{R^4}\n$$\n\nKhi chiều dài không đổi:\n\n$$\n\\frac{\\Delta p'}{\\Delta p}=\\left(\\frac R{R'}\\right)^4\n$$\n\nHệ số tỉ lệ phụ thuộc tính chất của chất lưu. Không áp dụng quan hệ này cho dòng rối hoặc thay đổi chất lưu mà giữ nguyên hệ số tỉ lệ.",
  "duong-dong-chat-luu": "Đường đi được dựng bằng cách theo dõi một phần tử theo thời gian. Đường dòng được dựng từ trường vận tốc ở một thời điểm. Trong dòng ổn định, trường vận tốc không đổi theo thời gian nên hai cách dựng trùng nhau.\n\nNhững đường dòng qua biên của một tiết diện tạo thành ống dòng. Chất lưu không đi xuyên qua thành bên của ống dòng đang xét trong mô hình dòng ổn định. Đây là điều kiện hình học để áp dụng bảo toàn khối lượng giữa hai tiết diện.\n\nĐường sức điện cũng dùng tiếp tuyến để biểu diễn hướng một trường vector. Sự tương tự hình học này không có nghĩa điện trường là dòng chất hoặc đường sức là quỹ đạo điện tích.",
  "ong-dong-chat-luu": "Các đường dòng qua đường biên của một diện tích tạo nên mặt bên của ống dòng. Vận tốc tại mặt bên tiếp tuyến với mặt, nên không có thành phần vận tốc xuyên qua mặt bên trong mô hình đang xét.\n\nỐng dòng là một vùng không gian, còn một đường dòng là đường cong. Khi dòng không ổn định, cần phân biệt ống dựng từ trường vận tốc tức thời với một tập phần tử chất lưu được theo dõi theo thời gian.",
  "duong-di-phan-tu-chat-luu": "Quỹ đạo gắn với một phần tử cụ thể qua nhiều thời điểm. Đường dòng lại được dựng bằng tiếp tuyến với trường vận tốc tại một thời điểm. Dòng ổn định giữ nguyên trường vận tốc tại mỗi vị trí, nên phần tử lần lượt đi theo chính đường dòng.\n\nỔn định không có nghĩa tốc độ của mỗi phần tử không đổi: Tốc độ và hướng vẫn có thể đổi khi phần tử đi qua các vị trí khác nhau.",
  "luu-luong-chat-luu": "Với tốc độ đều trên tiết diện hoặc tốc độ trung bình theo tiết diện:\n\n$$\nQ=\\frac{dV}{dt}=Av\n$$\n\nĐơn vị của Q là mét khối trên giây. Lưu lượng khối lượng là:\n\n$$\n\\dot m=\\rho Q=\\rho Av\n$$\n\nĐơn vị của lưu lượng khối lượng là kilôgam trên giây. Quan hệ cuối dùng khối lượng riêng đồng nhất tại tiết diện trong mô hình đang xét. Dòng ổn định không có nguồn bảo toàn lưu lượng khối lượng, còn bảo toàn lưu lượng thể tích cần thêm khối lượng riêng không đổi."
}
export const physics1FluidWikiConnections={
  "ty-khoi": [
    "khoi-luong-rieng",
    "don-vi"
  ],
  "nguyen-ly-pascal": [
    "ap-suat-chat-luu",
    "ap-suat-tuyet-doi-va-ap-suat-du",
    "luc"
  ],
  "ap-suat-tuyet-doi-va-ap-suat-du": [
    "ap-suat-chat-luu",
    "nguyen-ly-pascal",
    "don-vi"
  ],
  "suc-cang-be-mat": [
    "luc-day-archimedes",
    "khoi-luong-rieng"
  ],
  "chat-luu-ly-tuong": [
    "phuong-trinh-lien-tuc",
    "phuong-trinh-bernoulli",
    "do-nhot-chat-luu"
  ],
  "do-nhot-chat-luu": [
    "chat-luu-ly-tuong",
    "dong-nhot-trong-ong-tru",
    "chay-tang-va-chay-roi"
  ],
  "chay-tang-va-chay-roi": [
    "duong-dong-chat-luu",
    "do-nhot-chat-luu",
    "phuong-trinh-bernoulli"
  ],
  "dong-nhot-trong-ong-tru": [
    "do-nhot-chat-luu",
    "phuong-trinh-lien-tuc",
    "ap-suat-chat-luu"
  ],
  "duong-dong-chat-luu": [
    "vector",
    "phuong-trinh-lien-tuc",
    "phuong-trinh-bernoulli"
  ],
  "ong-dong-chat-luu": [
    "duong-dong-chat-luu",
    "phuong-trinh-lien-tuc",
    "phuong-trinh-bernoulli"
  ],
  "duong-di-phan-tu-chat-luu": [
    "duong-dong-chat-luu",
    "ong-dong-chat-luu",
    "van-toc-vat-ly"
  ],
  "luu-luong-chat-luu": [
    "phuong-trinh-lien-tuc",
    "khoi-luong-rieng",
    "ong-dong-chat-luu"
  ]
}
