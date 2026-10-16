const math = tex => '$$\n' + tex + '\n$$'
const entry = (name, description, formula) => ({ name, description, formula, variables: [] })
const note = '20-ham-song-schrodinger'
const slide = (title, bullets, formula) => ({ note, title, bullets, formula })

export const quantumWaveCheatsheet = {
  title: 'Cheatsheet: Hàm sóng và cơ học lượng tử một chiều',
  description: 'Định nghĩa, tính chất, điều kiện và công thức về hàm sóng, giếng thế, xuyên hầm, dao động tử và phép đo.',
  sections: [
    {
      id: 'probability', title: 'Hàm sóng và xác suất',
      items: [
        entry('Liên hợp phức và bình phương môđun',
          'a và b là số thực. Bình phương môđun là số thực không âm.',
          math('\\begin{aligned}z&=a+ib,\\\\z^*&=a-ib,\\\\|z|^2&=z^*z=a^2+b^2.\\end{aligned}')),
        entry('Mật độ xác suất',
          'Một hạt một chiều trong biểu diễn vị trí. Mật độ có đơn vị nghịch đảo chiều dài khi hàm sóng đã chuẩn hóa.',
          math('\\rho(x,t)=\\Psi^*(x,t)\\Psi(x,t).')),
        entry('Xác suất trong khoảng',
          '$P_{[a,b]}$ là xác suất vị trí nằm từ a đến b tại thời điểm t. Với phân bố liên tục, một điểm đơn lẻ có xác suất bằng không.',
          math('P_{[a,b]}=\\int_a^b\\rho(x,t)\\,dx.')),
        entry('Chuẩn hóa',
          'Trạng thái có chuẩn hữu hạn. Tích phân bao gồm toàn bộ miền và các đuôi ngoài giếng nếu có.',
          math('\\int_{-\\infty}^{\\infty}|\\Psi|^2\\,dx=1.')),
        entry('Giao thoa của hai thành phần',
          '$\\Psi=\\Psi_1+\\Psi_2$, $\\rho_j=|\\Psi_j|^2$. S là tích chéo giữa hai biên độ. Pha tương đối quyết định phần giao thoa.',
          math('\\begin{aligned}&S=\\Psi_1^*\\Psi_2,\\\\&\\rho=\\rho_1+\\rho_2+2\\operatorname{Re}S.\\end{aligned}')),
      ]
    },
    {
      id: 'dynamics', title: 'Phương trình và trạng thái dừng',
      items: [
        entry('Hạt tự do phi tương đối tính',
          'Chọn thế năng bằng không. E là động năng trong mô hình phi tương đối tính.',
          math('\\begin{aligned}p&=\\hbar k,\\\\E&=\\hbar\\omega=\\frac{\\hbar^2k^2}{2m}.\\end{aligned}')),
        entry('Vận tốc pha và vận tốc nhóm',
          'Gói hẹp phổ quanh k. Vận tốc nhóm phù hợp vận tốc hạt trong mô hình tự do.',
          math('\\begin{aligned}v_p&=\\frac{\\omega}{k}=\\frac{\\hbar k}{2m},\\\\v_g&=\\frac{d\\omega}{dk}=\\frac{\\hbar k}{m}.\\end{aligned}')),
        entry('Hamiltonian một chiều',
          'Khối lượng m không đổi, thế năng U và mô hình một hạt phi tương đối tính.',
          math('\\hat H=-\\frac{\\hbar^2}{2m}\\frac{\\partial^2}{\\partial x^2}+U.')),
        entry('Phương trình phụ thuộc thời gian',
          'Hamiltonian mô tả động năng và thế năng của hệ. Không bao gồm sự chọn kết quả có điều kiện của một phép đo lý tưởng.',
          math('i\\hbar\\frac{\\partial\\Psi}{\\partial t}=\\hat H\\Psi.')),
        entry('Phương trình không phụ thuộc thời gian',
          'Thế năng không phụ thuộc thời gian. Dấu phẩy là đạo hàm theo x.',
          math('-\\frac{\\hbar^2}{2m}\\psi^{\\prime\\prime}+U\\psi=E\\psi.')),
        entry('Trạng thái dừng',
          'Trạng thái riêng năng lượng. Mật độ vị trí giữ nguyên theo thời gian, không đồng nghĩa hạt cổ điển đứng yên.',
          math('\\begin{aligned}\\Psi(x,t)&=\\psi(x)e^{-iEt/\\hbar},\\\\|\\Psi(x,t)|^2&=|\\psi(x)|^2.\\end{aligned}')),
      ]
    },
    {
      id: 'box', title: 'Hạt trong hộp vô hạn',
      items: [
        entry('Các mức năng lượng',
          'Hộp rộng L, thế năng trong hộp bằng không. Số lượng tử $n=1,2,3,\\ldots$.',
          math('\\begin{aligned}E_n&=\\frac{n^2h^2}{8mL^2}\\\\&=\\frac{n^2\\pi^2\\hbar^2}{2mL^2}.\\end{aligned}')),
        entry('Hàm sóng chuẩn hóa',
          'Trong đoạn từ không đến L. Hàm bằng không ở hai vách và bên ngoài.',
          math('\\psi_n(x)=\\sqrt{\\frac2L}\\sin\\frac{n\\pi x}{L}.')),
        entry('Khoảng cách mức liền nhau',
          '$E_1$ là năng lượng cơ bản của hộp. Khoảng cách tăng khi n tăng.',
          math('E_{n+1}-E_n=(2n+1)E_1.')),
        entry('Giá trị kỳ vọng động lượng',
          'Trạng thái riêng của hộp vô hạn. Các mômen không khẳng định phân bố động lượng tự do chỉ có hai giá trị.',
          math('\\begin{aligned}\\langle p_x\\rangle&=0,\\\\\\langle p_x^2\\rangle&=\\left(\\frac{n\\pi\\hbar}{L}\\right)^2.\\end{aligned}')),
      ]
    },
    {
      id: 'finite', title: 'Giếng hữu hạn và điều kiện biên',
      items: [
        entry('Khoảng năng lượng liên kết',
          'Đáy giếng bằng không, thế năng ngoài bằng U₀. Năng lượng thoát được đo từ mức E đến ngưỡng ngoài.',
          math('\\begin{aligned}&0<E<U_0,\\\\&E_{\\rm thoat}=U_0-E.\\end{aligned}')),
        entry('Số sóng trong và hằng số suy giảm ngoài',
          'Khối lượng không đổi. k và κ có đơn vị nghịch đảo chiều dài.',
          math('\\begin{aligned}k&=\\frac{\\sqrt{2mE}}{\\hbar},\\\\\\kappa&=\\frac{\\sqrt{2m(U_0-E)}}{\\hbar}.\\end{aligned}')),
        entry('Đuôi trạng thái liên kết',
          'Giếng nằm từ không đến L. C và D là biên độ tại các biên tương ứng. Các nghiệm này giảm khi đi ra vô cực.',
          math('\\begin{aligned}&\\psi=Ce^{\\kappa x},\\quad x<0,\\\\&\\psi=De^{-\\kappa(x-L)},\\quad x>L.\\end{aligned}')),
        entry('Nối nghiệm qua bước thế hữu hạn',
          'Với thế không kỳ dị và khối lượng không đổi, ψ cùng đạo hàm bậc nhất liên tục. Quy tắc này không áp máy móc qua vách thế vô hạn.',
          ''),
      ]
    },
    {
      id: 'tunnel', title: 'Xuyên hầm qua hàng rào chữ nhật',
      items: [
        entry('Hệ số truyền gần đúng',
          'Thế năng hai phía bằng không, $0<E<U_0$. Hàng rào rộng L và xác suất truyền $T\\ll1$.',
          math('T\\approx Ge^{-2\\kappa L}.')),
        entry('Hệ số G và hằng số suy giảm',
          'G không phải một xác suất riêng lẻ. Khối lượng m và hiệu năng lượng quyết định κ.',
          math('\\begin{aligned}&G=16\\frac{E}{U_0}\\left(1-\\frac{E}{U_0}\\right),\\\\&\\kappa=\\frac{\\sqrt{2m(U_0-E)}}{\\hbar}.\\end{aligned}')),
        entry('So sánh hai độ rộng',
          'Cùng hạt, cùng năng lượng và độ cao hàng rào. Cả hai trường hợp thuộc miền gần đúng mờ đục.',
          math('\\frac{T(L_2)}{T(L_1)}=e^{-2\\kappa(L_2-L_1)}.')),
        entry('Hệ số truyền chính xác của hàng rào',
          'Cùng thế năng ở hai phía và $0<E<U_0$. a là hệ số không thứ nguyên, không phải chiều dài.',
          math('\\begin{aligned}&a=\\frac{U_0^2}{4E(U_0-E)},\\\\&T=\\frac{1}{1+a\\sinh^2(\\kappa L)}.\\end{aligned}')),
      ]
    },
    {
      id: 'oscillator', title: 'Dao động tử điều hòa',
      items: [
        entry('Thế năng và tần số góc',
          'Hằng số lực k′ dương, khối lượng m. Mốc thế năng tại cân bằng bằng không.',
          math('\\begin{aligned}&U=\\frac12k^{\\prime}x^2,\\\\&\\omega=\\sqrt{\\frac{k^{\\prime}}{m}}.\\end{aligned}')),
        entry('Các mức và lượng tử dao động',
          'Số lượng tử $n=0,1,2,\\ldots$. Mức cơ bản có năng lượng khác không và mọi khoảng cách mức liền nhau bằng nhau.',
          math('\\begin{aligned}E_n&=\\left(n+\\frac12\\right)\\hbar\\omega,\\\\E_{n+1}-E_n&=\\hbar\\omega.\\end{aligned}')),
        entry('Gaussian cơ bản đã chuẩn hóa',
          'α dương. Đây là hàm không phụ thuộc thời gian của mức cơ bản.',
          math('\\begin{aligned}\\alpha&=\\frac{m\\omega}{\\hbar},\\\\\\psi_0(x)&=\\left(\\frac{\\alpha}{\\pi}\\right)^{1/4}e^{-\\alpha x^2/2}.\\end{aligned}')),
        entry('Độ lệch chuẩn ở mức cơ bản',
          'Các đại lượng là độ lệch chuẩn của phân bố lượng tử, không phải biên độ quỹ đạo cổ điển.',
          math('\\begin{aligned}&\\Delta x=\\sqrt{\\frac{\\hbar}{2m\\omega}},\\\\&\\Delta p_x=\\sqrt{\\frac{m\\hbar\\omega}{2}},\\\\&\\Delta x\\,\\Delta p_x=\\frac{\\hbar}{2}.\\end{aligned}')),
        entry('Photon của một chuyển mức liền kề',
          'Năng lượng photon bằng khoảng cách mức, bỏ qua giật lùi trong mô hình dao động tử.',
          math('\\begin{aligned}E_\\gamma&=\\hbar\\omega,\\\\\\lambda&=\\frac{hc}{\\hbar\\omega}.\\end{aligned}')),
      ]
    },
    {
      id: 'measurement', title: 'Chồng chập và phép đo năng lượng',
      items: [
        entry('Hai trạng thái trực chuẩn',
          '$\\Psi=C\\Psi_1+D\\Psi_2$. Các thành phần được chuẩn hóa và trực giao.',
          math('|C|^2+|D|^2=1.')),
        entry('Xác suất của hai mức',
          'Phép đo năng lượng lý tưởng trên chồng chập đã chuẩn hóa của hai trạng thái riêng năng lượng trực chuẩn.',
          math('\\begin{aligned}P(E_1)&=|C|^2,\\\\P(E_2)&=|D|^2.\\end{aligned}')),
        entry('Giá trị kỳ vọng năng lượng',
          'Trung bình thống kê trên nhiều hệ chuẩn bị giống nhau. Không nhất thiết là một kết quả riêng lẻ.',
          math('\\langle E\\rangle=|C|^2E_1+|D|^2E_2.')),
      ]
    },
  ]
}

export const quantumWaveSlides = [
  slide('Hàm sóng cho mật độ, tích phân cho xác suất',
    ['Hàm sóng có thể phức.', 'Xác suất trên một khoảng là tích phân bình phương môđun.', 'Một điểm đơn lẻ của phân bố liên tục có xác suất bằng không.'],
    math('\\rho=\\Psi^*\\Psi.')),
  slide('Chồng biên độ trước khi tính xác suất',
    ['Tính tuyến tính cho phép chồng các nghiệm của cùng phương trình.', 'Pha tương đối tạo những số hạng giao thoa.', 'Một gói định xứ cần một phổ số sóng thích hợp.'],
    math('\\Psi=C\\Psi_1+D\\Psi_2.')),
  slide('Sóng vật chất phi tương đối tính có tán sắc',
    ['Tần số góc tỉ lệ bình phương số sóng.', 'Vận tốc pha khác vận tốc nhóm.', 'Gói sóng tự do có thể trải rộng theo thời gian.'],
    math('\\omega=\\frac{\\hbar k^2}{2m}.')),
  slide('Phương trình Schrödinger cần một mô hình cụ thể',
    ['Hamiltonian chứa động năng và thế năng.', 'Miền và điều kiện biên là một phần của bài toán.', 'Một nghiệm phương trình vi phân chưa chắc là trạng thái vật lý.'],
    math('i\\hbar\\frac{\\partial\\Psi}{\\partial t}=\\hat H\\Psi.')),
  slide('Trạng thái dừng có mật độ không đổi',
    ['Thế năng không phụ thuộc thời gian.', 'Một trạng thái riêng năng lượng chỉ nhận pha chung theo thời gian.', 'Năng lượng xác định không bảo đảm động lượng xác định.'],
    math('\\Psi(x,t)=\\psi(x)e^{-iEt/\\hbar}.')),
  slide('Hai vách tạo lượng tử hóa trong hộp',
    ['Hàm sóng bằng không tại hai đầu.', 'Số lượng tử bắt đầu từ một.', 'Khoảng cách mức tăng theo số lượng tử.'],
    math('E_n=\\frac{n^2\\pi^2\\hbar^2}{2mL^2}.')),
  slide('Chuẩn hóa bao gồm toàn miền',
    ['Biên độ lượng tử được ràng buộc bởi xác suất toàn phần.', 'Nút có mật độ bằng không.', 'Các khoảng bằng nhau không nhất thiết đồng xác suất.'],
    math('\\int_{-\\infty}^{\\infty}|\\psi|^2\\,dx=1.')),
  slide('Giếng hữu hạn có đuôi xác suất',
    ['Nghiệm bên trong dao động, bên ngoài suy giảm.', 'Nối hàm và đạo hàm tại bước thế hữu hạn.', 'Liên kết yếu tạo đuôi dài và số mức liên kết là hữu hạn.'],
    math('\\kappa=\\frac{\\sqrt{2m(U_0-E)}}{\\hbar}.')),
  slide('Xuyên hầm nhạy với độ rộng hàng rào',
    ['Truyền qua không đồng nghĩa tiêu hao cơ năng trong thế tĩnh.', 'Công thức gần đúng cần hệ số truyền rất nhỏ.', 'Sự phụ thuộc hàm mũ giải thích độ nhạy của STM.'],
    math('T\\approx Ge^{-2\\kappa L}.')),
  slide('Dao động tử có các mức cách đều',
    ['Số lượng tử bắt đầu từ không.', 'Mức cơ bản cao hơn đáy parabol.', 'Gần cân bằng bền, một thế năng thực có thể gần parabol.'],
    math('E_n=\\left(n+\\frac12\\right)\\hbar\\omega.')),
  slide('Gaussian cơ bản đạt giới hạn bất định',
    ['Hàm sóng cơ bản không phải một hạt đứng yên ở tâm.', 'Độ lệch chuẩn khác biên độ cổ điển.', 'Hàm sóng còn kéo dài ra miền ngoài biên độ cổ điển.'],
    math('\\Delta x\\,\\Delta p_x=\\frac{\\hbar}{2}.')),
  slide('Kết quả từng lần khác trung bình thống kê',
    ['Đo năng lượng của chồng chập cho một trong các mức được phép.', 'Xác suất phụ thuộc hệ số đã chuẩn hóa.', 'Một phép đo lý tưởng trên trạng thái riêng phù hợp có thể giữ nguyên trạng thái.'],
    math('\\langle E\\rangle=|C|^2E_1+|D|^2E_2.')),
]

export const quantumWaveTopics = [
  {
    title: 'Hàm sóng và sự giam giữ',
    topics: [
      { slug:'ham-song-schrodinger', title:'Hàm sóng và phương trình Schrödinger', question:'Biên độ phức mô tả trạng thái và xác suất như thế nào?', source:'40.1' },
      { slug:'hat-trong-hop', title:'Hạt trong hộp vô hạn', question:'Hai vách giới hạn các bước sóng và năng lượng ra sao?', source:'40.2' },
      { slug:'gieng-the-huu-han', title:'Giếng thế hữu hạn', question:'Điều gì thay đổi khi hàm sóng có thể thâm nhập ra ngoài giếng?', source:'40.3' },
    ]
  },
  {
    title: 'Xuyên hầm, dao động và phép đo',
    topics: [
      { slug:'hang-rao-xuyen-ham', title:'Hàng rào thế và xuyên hầm', question:'Hạt đi qua miền bị cấm cổ điển với xác suất nào?', source:'40.4' },
      { slug:'dao-dong-tu-dieu-hoa', title:'Dao động tử điều hòa', question:'Điều kiện ở vô cực chọn các mức dao động như thế nào?', source:'40.5' },
      { slug:'phep-do-luong-tu', title:'Phép đo trong cơ học lượng tử', question:'Kết quả đo liên hệ với trạng thái trước và sau phép đo ra sao?', source:'40.6' },
    ]
  },
]
