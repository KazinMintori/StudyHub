// Cheatsheets for Physics 1 (Vật lý đại cương 1) — Chapters 1, 3–20.
// Based on Young & Freedman, University Physics with Modern Physics, 15th Edition.
// Chapter 2 is already authored in physics-motion-course.mjs.

const d = tex => '$$\n' + tex + '\n$$'

// ==========================================
// CHƯƠNG 1: ĐƠN VỊ, ĐẠI LƯỢNG VẬT LÝ VÀ VECTOR
// ==========================================
export const unitsVectorsCheatsheet = {
  summary: 'Định nghĩa, quy tắc và công thức cốt lõi về hệ đơn vị SI, phân tích vector, tích vô hướng và tích có hướng trong không gian ba chiều.',
  sections: [
    {
      id: 'units-prefixes',
      title: 'Hệ đơn vị SI và thứ nguyên',
      badge: 'Mục 1.3–1.5',
      items: [
        {
          name: 'Bảy đơn vị cơ bản trong hệ SI',
          description: String.raw`Các đơn vị cơ bản định nghĩa các đại lượng đo lường độc lập: Chiều dài đo bằng mét ($\mathrm{m}$), khối lượng đo bằng kilôgam ($\mathrm{kg}$), thời gian đo bằng giây ($\mathrm{s}$), cường độ dòng điện đo bằng ampe ($\mathrm{A}$), nhiệt độ nhiệt động lực học đo bằng kelvin ($\mathrm{K}$), lượng chất đo bằng mol ($\mathrm{mol}$), cường độ sáng đo bằng candela ($\mathrm{cd}$).`
        },
        {
          name: 'Tiền tố thập phân của hệ SI',
          description: String.raw`Các ước số và bội số chuẩn hóa: Nano ($10^{-9}$), micro ($10^{-6}$), milli ($10^{-3}$), centi ($10^{-2}$), kilo ($10^3$), mega ($10^6$), giga ($10^9$).`
        }
      ]
    },
    {
      id: 'vector-components',
      title: 'Phân tích và phép cộng vector',
      badge: 'Mục 1.7–1.8',
      items: [
        {
          name: 'Thành phần và độ lớn của vector trong mặt phẳng',
          formulaRows: [
            { label: 'Thành phần theo hai trục tọa độ vuông góc', formula: d(String.raw`A_x = A\cos\theta,\quad A_y = A\sin\theta`) },
            { label: 'Độ lớn và góc hướng của vector', formula: d(String.raw`\begin{aligned}&A = \sqrt{A_x^2 + A_y^2}, \\ &\tan\theta = \frac{A_y}{A_x}.\end{aligned}`) }
          ],
          variables: [
            String.raw`$A$: Độ lớn của vector $\vec A$ (Luôn không âm)`,
            String.raw`$A_x, A_y$: Thành phần đại số của vector $\vec A$ dọc theo hai trục $x$ và $y$`,
            String.raw`$\theta$: Góc định hướng của vector so với chiều dương trục $x$ ($\mathrm{rad}$ hoặc độ)`
          ],
          description: String.raw`Các thành phần $A_x, A_y$ có thể dương, âm hoặc bằng không tùy thuộc góc định hướng $\theta$.`
        },
        {
          name: 'Phép cộng vector theo thành phần trong không gian',
          formulaRows: [
            { label: 'Hợp vector của hai vector', formula: d(String.raw`\begin{aligned}\vec R &= \vec A + \vec B, \\ R_x &= A_x + B_x, \\ R_y &= A_y + B_y, \\ R_z &= A_z + B_z.\end{aligned}`) },
            { label: 'Khai triển tổng quát cho n vector', formula: d(String.raw`\begin{aligned}\vec R &= \vec A_1 + \vec A_2 + \dots + \vec A_n \\ &= \sum_{i=1}^n \vec A_i.\end{aligned}`) }
          ],
          variables: [
            String.raw`$\vec R$: Vector tổng hợp`,
            String.raw`$R_x, R_y, R_z$: Thành phần của vector tổng theo ba trục tọa độ`,
            String.raw`$\hat{\mathbf i}, \hat{\mathbf j}, \hat{\mathbf k}$: Các vector đơn vị chỉ hướng dương trục $x, y, z$`
          ],
          description: String.raw`Mỗi thành phần của vector tổng bằng tổng đại số các thành phần tương ứng của từng vector thành phần.`
        }
      ]
    },
    {
      id: 'scalar-product',
      title: 'Tích vô hướng (Dot Product)',
      badge: 'Mục 1.9',
      items: [
        {
          name: 'Định nghĩa và biểu thức tọa độ của tích vô hướng',
          formulaRows: [
            { label: 'Định nghĩa hình học qua góc kẹp', formula: d(String.raw`\vec A \cdot \vec B = AB\cos\phi`) },
            { label: 'Biểu thức theo các thành phần tọa độ', formula: d(String.raw`\vec A \cdot \vec B = A_x B_x + A_y B_y + A_z B_z`) }
          ],
          variables: [
            String.raw`$\vec A \cdot \vec B$: Tích vô hướng của hai vector (Đại lượng vô hướng)`,
            String.raw`$A, B$: Độ lớn của hai vector $\vec A$ và $\vec B$`,
            String.raw`$\phi$: Góc kẹp giữa hai vector ($0 \le \phi \le \pi$)`
          ],
          description: String.raw`Tích vô hướng có tính giao hoán $\vec A \cdot \vec B = \vec B \cdot \vec A$. Hai vector khác không vuông góc với nhau khi và chỉ khi tích vô hướng bằng không.`
        }
      ]
    },
    {
      id: 'vector-product',
      title: 'Tích có hướng (Cross Product)',
      badge: 'Mục 1.10',
      items: [
        {
          name: 'Định nghĩa và biểu thức tọa độ của tích có hướng',
          formulaRows: [
            { label: 'Độ lớn của tích có hướng', formula: d(String.raw`C = |\vec A \times \vec B| = AB\sin\phi`) },
            { label: 'Các thành phần của tích có hướng', formula: d(String.raw`\begin{aligned}\vec C &= \vec A \times \vec B, \\ C_x &= A_yB_z - A_zB_y, \\ C_y &= A_zB_x - A_xB_z, \\ C_z &= A_xB_y - A_yB_x.\end{aligned}`) }
          ],
          variables: [
            String.raw`$\vec C = \vec A \times \vec B$: Vector tích có hướng, vuông góc với mặt phẳng chứa $\vec A$ và $\vec B$`,
            String.raw`$\phi$: Góc hợp bởi hai vector ($0 \le \phi \le \pi$)`
          ],
          description: String.raw`Chiều của $\vec C$ tuân theo quy tắc bàn tay phải. Tích có hướng có tính phản giao hoán: $\vec A \times \vec B = -(\vec B \times \vec A)$. Hai vector cùng phương khi và chỉ khi tích có hướng bằng vector không.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 3: CHUYỂN ĐỘNG TRONG HAI HOẶC BA CHIỀU
// ==========================================
export const motion3dCheatsheet = {
  summary: 'Công thức vector vị trí, vận tốc, gia tốc tiếp tuyến và pháp tuyến, chuyển động ném xiên, chuyển động tròn đều và vận tốc tương đối.',
  sections: [
    {
      id: 'kinematics-vectors',
      title: 'Vector vận tốc và gia tốc',
      badge: 'Mục 3.1–3.2',
      items: [
        {
          name: 'Vector vận tốc và gia tốc tức thời',
          formulaRows: [
            { label: 'Đạo hàm của vector bán kính vị trí', formula: d(String.raw`\vec v = \frac{d\vec r}{dt} = v_x\hat{\mathbf i} + v_y\hat{\mathbf j} + v_z\hat{\mathbf k}`) },
            { label: 'Đạo hàm của vector vận tốc', formula: d(String.raw`\vec a = \frac{d\vec v}{dt} = a_x\hat{\mathbf i} + a_y\hat{\mathbf j} + a_z\hat{\mathbf k}`) }
          ],
          variables: [
            String.raw`$\vec r(t)$: Vector vị trí của chất điểm tại thời điểm $t$ ($\mathrm{m}$)`,
            String.raw`$\vec v$: Vector vận tốc tức thời, luôn tiếp tuyến với quỹ đạo ($\mathrm{m/s}$)`,
            String.raw`$\vec a$: Vector gia tốc tức thời, luôn hướng về phía lõm của quỹ đạo ($\mathrm{m/s^2}$)`
          ],
          description: String.raw`Vector vận tốc luôn tiếp tuyến với quỹ đạo chuyển động. Khi hướng chuyển động uốn cong, vector gia tốc có góc lệch so với vector vận tốc.`
        },
        {
          name: 'Gia tốc tiếp tuyến và gia tốc pháp tuyến',
          formulaRows: [
            { label: 'Thành phần tiếp tuyến làm thay đổi tốc độ', formula: d(String.raw`a_\parallel = a_{\mathrm{tan}} = \frac{dv}{dt}`) },
            { label: 'Thành phần pháp tuyến làm đổi hướng vận tốc', formula: d(String.raw`a_\perp = a_{\mathrm{rad}} = \frac{v^2}{\rho}`) }
          ],
          variables: [
            String.raw`$a_{\mathrm{tan}}$: Gia tốc tiếp tuyến với quỹ đạo ($\mathrm{m/s^2}$)`,
            String.raw`$a_{\mathrm{rad}}$: Gia tốc pháp tuyến (hướng tâm), vuông góc với quỹ đạo ($\mathrm{m/s^2}$)`,
            String.raw`$\rho$: Bán kính cong của quỹ đạo tại điểm khảo sát ($\mathrm{m}$)`,
            String.raw`$v$: Tốc độ tức thời của vật ($v = |\vec v|$) ($\mathrm{m/s}$)`
          ],
          description: String.raw`Gia tốc toàn phần có độ lớn $a = \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2}$.`
        }
      ]
    },
    {
      id: 'projectile-motion',
      title: 'Chuyển động ném trong trọng trường',
      badge: 'Mục 3.3',
      items: [
        {
          name: 'Phương trình tọa độ và vận tốc của vật ném',
          formulaRows: [
            { label: 'Tọa độ theo trục nằm ngang ax = 0', formula: d(String.raw`x(t) = x_0 + (v_0\cos\alpha_0)t`) },
            { label: 'Tọa độ theo trục thẳng đứng ay = -g', formula: d(String.raw`y(t) = y_0 + (v_0\sin\alpha_0)t - \tfrac12gt^2`) },
            { label: 'Vận tốc tức thời theo trục thẳng đứng', formula: d(String.raw`v_y(t) = v_0\sin\alpha_0 - gt`) }
          ],
          variables: [
            String.raw`$v_0$: Tốc độ ném ban đầu ($\mathrm{m/s}$)`,
            String.raw`$\alpha_0$: Góc ném ban đầu so với phương ngang ($0 \le \alpha_0 \le 90^\circ$)`,
            String.raw`$g$: Gia tốc rơi tự do ($\approx 9{,}80\,\mathrm{m/s^2}$)`
          ],
          description: String.raw`Bỏ qua lực cản không khí, chuyển động ném là sự kết hợp của chuyển động thẳng đều theo trục $x$ và chuyển động rơi tự do biến đổi đều theo trục $y$.`
        },
        {
          name: 'Tầm cao và tầm xa trên mặt đất bằng phẳng',
          formulaRows: [
            { label: 'Độ cao cực đại trên mặt đất', formula: d(String.raw`h_{\max} = \frac{v_0^2\sin^2\alpha_0}{2g}`) },
            { label: 'Tầm bay xa khi ném từ và rơi về cùng độ cao', formula: d(String.raw`R = \frac{v_0^2\sin 2\alpha_0}{g}`) }
          ],
          variables: [
            String.raw`$h_{\max}$: Độ cao lớn nhất vật đạt được so với mốc ném ban đầu ($\mathrm{m}$)`,
            String.raw`$R$: Tầm bay xa của vật khi trở về cùng cao độ xuất phát ($\mathrm{m}$)`
          ],
          description: String.raw`Tầm xa $R$ đạt cực đại khi góc ném ban đầu $\alpha_0 = 45^\circ$. Hai góc ném phụ nhau có cùng giá trị tầm xa.`
        }
      ]
    },
    {
      id: 'circular-motion',
      title: 'Chuyển động tròn đều',
      badge: 'Mục 3.4',
      items: [
        {
          name: 'Gia tốc hướng tâm và chu kỳ',
          formulaRows: [
            { label: 'Gia tốc hướng tâm theo tốc độ dài', formula: d(String.raw`a_{\mathrm{rad}} = \frac{v^2}{R}`) },
            { label: 'Gia tốc hướng tâm theo chu kỳ quay T', formula: d(String.raw`a_{\mathrm{rad}} = \frac{4\pi^2 R}{T^2}`) }
          ],
          variables: [
            String.raw`$a_{\mathrm{rad}}$: Gia tốc hướng tâm, luôn hướng vào tâm quỹ đạo ($\mathrm{m/s^2}$)`,
            String.raw`$v$: Tốc độ dài không đổi của chuyển động tròn đều ($\mathrm{m/s}$)`,
            String.raw`$R$: Bán kính đường tròn quỹ đạo ($\mathrm{m}$)`,
            String.raw`$T$: Chu kỳ thời gian đi hết một vòng ($T = 2\pi R / v$) ($\mathrm{s}$)`
          ],
          description: String.raw`Trong chuyển động tròn đều, tốc độ không đổi nên gia tốc tiếp tuyến bằng không, chỉ tồn tại gia tốc hướng tâm làm đổi hướng vector vận tốc.`
        }
      ]
    },
    {
      id: 'relative-velocity',
      title: 'Vận tốc tương đối',
      badge: 'Mục 3.5',
      items: [
        {
          name: 'Định lý cộng vận tốc Galilei',
          formula: d(String.raw`\vec v_{P/A} = \vec v_{P/B} + \vec v_{B/A}`),
          variables: [
            String.raw`$\vec v_{P/A}$: Vận tốc của chất điểm $P$ đối với hệ quy chiếu $A$ ($\mathrm{m/s}$)`,
            String.raw`$\vec v_{P/B}$: Vận tốc của chất điểm $P$ đối với hệ quy chiếu chuyển động $B$ ($\mathrm{m/s}$)`,
            String.raw`$\vec v_{B/A}$: Vận tốc của hệ quy chiếu $B$ đối với hệ quy chiếu $A$ ($\mathrm{m/s}$)`
          ],
          description: String.raw`Hệ thức đúng trong cơ học cổ điển khi các tốc độ nhỏ hơn rất nhiều so với tốc độ ánh sáng. Khi hai hệ chuyển động thẳng đều với nhau, gia tốc của chất điểm trong hai hệ là như nhau.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 4: CÁC ĐỊNH LUẬT CHUYỂN ĐỘNG CỦA NEWTON
// ==========================================
export const newtonLawsCheatsheet = {
  summary: 'Ba định luật động lực học kinh điển của Newton, khối lượng quán tính, trọng lực, các lực liên kết cơ học và sơ đồ vật tự do.',
  sections: [
    {
      id: 'force-superposition',
      title: 'Khái niệm lực và nguyên lý chồng chất lực',
      badge: 'Mục 4.1',
      items: [
        {
          name: 'Nguyên lý chồng chất lực tác dụng',
          formula: d(String.raw`\vec R = \sum_{i=1}^n \vec F_i = \vec F_1 + \vec F_2 + \dots + \vec F_n`),
          variables: [
            String.raw`$\vec R$: Hợp lực tác dụng lên chất điểm ($\mathrm{N}$)`,
            String.raw`$\vec F_i$: Các lực thành phần cùng tác dụng lên vật ($\mathrm{N}$)`
          ],
          description: String.raw`Tác dụng của đồng thời nhiều lực lên một chất điểm tương đương với tác dụng của một lực duy nhất bằng tổng vector của chúng.`
        }
      ]
    },
    {
      id: 'newton-first-second',
      title: 'Định luật I và II Newton',
      badge: 'Mục 4.2–4.3',
      items: [
        {
          name: 'Định luật I Newton (Quán tính)',
          description: String.raw`Trong hệ quy chiếu quán tính, một vật không chịu tác dụng của ngoại lực hoặc hợp lực bằng không thì giữ nguyên trạng thái đứng yên hoặc chuyển động thẳng đều ($\vec a = \vec 0$).`
        },
        {
          name: 'Định luật II Newton dạng vector và thành phần',
          formulaRows: [
            { label: 'Phương trình vector cơ bản', formula: d(String.raw`\sum\vec F = m\vec a`) },
            { label: 'Hệ phương trình theo ba trục tọa độ', formula: d(String.raw`\sum F_x = ma_x,\quad \sum F_y = ma_y,\quad \sum F_z = ma_z`) }
          ],
          variables: [
            String.raw`$\sum\vec F$: Hợp lực của tất cả các ngoại lực tác dụng lên vật ($\mathrm{N}$)`,
            String.raw`$m$: Khối lượng quán tính của vật ($\mathrm{kg}$)`,
            String.raw`$\vec a$: Vector gia tốc của vật ($\mathrm{m/s^2}$)`
          ],
          description: String.raw`Gia tốc của vật tỷ lệ thuận với hợp lực tác dụng và tỷ lệ nghịch với khối lượng. Hướng của gia tốc luôn trùng với hướng của hợp lực. Đơn vị đo: $1\,\mathrm N = 1\,\mathrm{kg\cdot m/s^2}$.`
        }
      ]
    },
    {
      id: 'mass-weight',
      title: 'Khối lượng và trọng lượng',
      badge: 'Mục 4.4',
      items: [
        {
          name: 'Trọng lực gần bề mặt Trái Đất',
          formula: d(String.raw`\vec w = m\vec g,\quad w = mg`),
          variables: [
            String.raw`$\vec w$: Vector trọng lực tác dụng lên vật ($\mathrm{N}$)`,
            String.raw`$m$: Khối lượng của vật ($\mathrm{kg}$)`,
            String.raw`$g$: Độ lớn gia tốc trọng trường tự do ($\approx 9{,}80\,\mathrm{m/s^2}$)`
          ],
          description: String.raw`Khối lượng là đại lượng vô hướng đặc trưng cho lượng vật chất và mức quán tính của vật. Trọng lượng là độ lớn lực hấp dẫn của Trái Đất tác dụng lên vật, thay đổi tùy theo vị trí địa lý.`
        }
      ]
    },
    {
      id: 'newton-third',
      title: 'Định luật III Newton và lực tương tác',
      badge: 'Mục 4.5–4.6',
      items: [
        {
          name: 'Cặp lực tác dụng và phản tác dụng',
          formula: d(String.raw`\vec F_{A\to B} = -\vec F_{B\to A}`),
          variables: [
            String.raw`$\vec F_{A\to B}$: Lực do vật $A$ tác dụng lên vật $B$ ($\mathrm{N}$)`,
            String.raw`$\vec F_{B\to A}$: Lực do vật $B$ tác dụng ngược lại lên vật $A$ ($\mathrm{N}$)`
          ],
          description: String.raw`Hai lực này cùng độ lớn, cùng phương, ngược chiều, cùng bản chất và đặt vào hai vật khác nhau, do đó không bao giờ tự triệt tiêu lẫn nhau.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 5: ÁP DỤNG CÁC ĐỊNH LUẬT NEWTON
// ==========================================
export const newtonApplicationsCheatsheet = {
  summary: 'Phương pháp giải bài toán cân bằng, động lực học chất điểm, ma sát trượt và ma sát nghỉ, lực cản chất lưu và động lực học chuyển động tròn.',
  sections: [
    {
      id: 'equilibrium-dynamics',
      title: 'Cân bằng và động lực học chất điểm',
      badge: 'Mục 5.1–5.2',
      items: [
        {
          name: 'Điều kiện cân bằng chất điểm',
          formula: d(String.raw`\sum\vec F = \vec 0 \iff \begin{cases}\sum F_x = 0, \\ \sum F_y = 0.\end{cases}`),
          variables: [
            String.raw`$\sum F_x, \sum F_y$: Tổng các thành phần lực tác dụng dọc theo trục $x$ và $y$ ($\mathrm{N}$)`
          ],
          description: String.raw`Áp dụng khi chất điểm đứng yên hoặc chuyển động thẳng đều với gia tốc bằng không.`
        },
        {
          name: 'Trọng lượng biểu kiến trong hệ quy chiếu gia tốc',
          formula: d(String.raw`n = m(g + a_y)`),
          variables: [
            String.raw`$n$: Phản lực pháp tuyến của sàn lên người (Trọng lượng biểu kiến) ($\mathrm{N}$)`,
            String.raw`$m$: Khối lượng của người ($\mathrm{kg}$)`,
            String.raw`$a_y$: Gia tốc của thang máy theo chiều hướng lên ($\mathrm{m/s^2}$)`
          ],
          description: String.raw`Khi thang máy tăng tốc đi lên ($a_y > 0$), trọng lượng biểu kiến tăng; khi thang máy gia tốc đi xuống ($a_y < 0$), trọng lượng biểu kiến giảm. Khi rơi tự do ($a_y = -g$), vật ở trạng thái không trọng lượng ($n = 0$).`
        }
      ]
    },
    {
      id: 'friction',
      title: 'Lực ma sát khô',
      badge: 'Mục 5.3',
      items: [
        {
          name: 'Ma sát nghỉ và ma sát trượt',
          formulaRows: [
            { label: 'Lực ma sát nghỉ cực đại trước khi trượt', formula: d(String.raw`f_{\mathrm s} \le \mu_{\mathrm s} n,\quad f_{\mathrm s,\max} = \mu_{\mathrm s} n`) },
            { label: 'Lực ma sát trượt khi hai bề mặt chuyển động', formula: d(String.raw`f_{\mathrm k} = \mu_{\mathrm k} n`) }
          ],
          variables: [
            String.raw`$f_{\mathrm s}$: Độ lớn lực ma sát nghỉ, tự điều chỉnh cân bằng với lực kéo ($\mathrm{N}$)`,
            String.raw`$f_{\mathrm k}$: Độ lớn lực ma sát trượt giữa hai bề mặt tiếp xúc ($\mathrm{N}$)`,
            String.raw`$\mu_{\mathrm s}, \mu_{\mathrm k}$: Hệ số ma sát nghỉ và hệ số ma sát trượt (Không thứ nguyên)`,
            String.raw`$n$: Độ lớn phản lực pháp tuyến giữa hai bề mặt ($\mathrm{N}$)`
          ],
          description: String.raw`Lực ma sát luôn có phương tiếp tuyến với bề mặt tiếp xúc và ngược chiều với xu hướng chuyển động hoặc chiều chuyển động tương đối. Thông thường $\mu_{\mathrm k} < \mu_{\mathrm s}$.`
        }
      ]
    },
    {
      id: 'drag-terminal',
      title: 'Lực cản chất lưu và tốc độ giới hạn',
      badge: 'Mục 5.3',
      items: [
        {
          name: 'Tốc độ rơi giới hạn trong chất lưu',
          formulaRows: [
            { label: 'Tốc độ giới hạn khi lực cản f = kv', formula: d(String.raw`v_t = \frac{mg}{k}`) },
            { label: 'Tốc độ giới hạn khi lực cản f = Dv^2', formula: d(String.raw`v_t = \sqrt{\frac{mg}{D}}`) }
          ],
          variables: [
            String.raw`$v_t$: Tốc độ rơi giới hạn đạt được khi lực cản cân bằng trọng lực ($\mathrm{m/s}$)`,
            String.raw`$k, D$: Hệ số cản của chất lưu phụ thuộc hình dạng và độ nhớt`
          ],
          description: String.raw`Khi vật đạt tốc độ giới hạn, hợp lực tác dụng triệt tiêu và gia tốc bằng không, vật chuyển động thẳng đều với tốc độ $v_t$.`
        }
      ]
    },
    {
      id: 'circular-dynamics',
      title: 'Động lực học chuyển động tròn',
      badge: 'Mục 5.4',
      items: [
        {
          name: 'Lực hướng tâm và góc nghiêng của khúc cua',
          formulaRows: [
            { label: 'Độ lớn hợp lực hướng tâm', formula: d(String.raw`F_{\mathrm{rad}} = m\frac{v^2}{R} = m\omega^2 R`) },
            { label: 'Góc nghiêng đường cua không cần ma sát', formula: d(String.raw`\tan\beta = \frac{v^2}{gR}`) }
          ],
          variables: [
            String.raw`$F_{\mathrm{rad}}$: Hợp lực hướng tâm cần thiết để duy trì quỹ đạo tròn ($\mathrm{N}$)`,
            String.raw`$\beta$: Góc nghiêng của mặt đường so với phương nằm ngang ($\mathrm{rad}$ hoặc độ)`,
            String.raw`$R$: Bán kính cong của khúc cua ($\mathrm{m}$)`
          ],
          description: String.raw`Lực hướng tâm không phải là một loại lực mới trong tự nhiên mà là tên gọi của hợp lực hoặc thành phần lực hướng vào tâm quỹ đạo.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 6: CÔNG VÀ ĐỘNG NĂNG
// ==========================================
export const workEnergyCheatsheet = {
  summary: 'Công của lực không đổi và biến thiên, động năng chất điểm, định lý công – động năng và công suất cơ học.',
  sections: [
    {
      id: 'work-definition',
      title: 'Công của lực tác dụng',
      badge: 'Mục 6.1–6.2',
      items: [
        {
          name: 'Công của lực không đổi trên độ dời thẳng',
          formula: d(String.raw`W = \vec F \cdot \vec s = F s\cos\phi = F_\parallel s`),
          variables: [
            String.raw`$W$: Công cơ học thực hiện bởi lực $\vec F$ ($\mathrm{J}$)`,
            String.raw`$F$: Độ lớn của lực tác dụng ($\mathrm{N}$)`,
            String.raw`$s$: Độ lớn của độ dời ($\mathrm{m}$)`,
            String.raw`$\phi$: Góc hợp bởi vector lực $\vec F$ và vector độ dời $\vec s$`
          ],
          description: String.raw`Công là đại lượng vô hướng. Khi $\phi < 90^\circ$ thì $W > 0$ (Công phát động); khi $\phi > 90^\circ$ thì $W < 0$ (Công cản); khi $\phi = 90^\circ$ thì $W = 0$. Đơn vị: $1\,\mathrm J = 1\,\mathrm{N\cdot m} = 1\,\mathrm{kg\cdot m^2/s^2}$.`
        },
        {
          name: 'Công của lực biến thiên dọc theo đường đi',
          formulaRows: [
            { label: 'Lực biến thiên một chiều theo tọa độ x', formula: d(String.raw`W = \int_{x_1}^{x_2} F_x\,dx`) },
            { label: 'Công của lực đàn hồi lò xo', formula: d(String.raw`W_{\mathrm{el}} = \tfrac12 k x_1^2 - \tfrac12 k x_2^2`) }
          ],
          variables: [
            String.raw`$F_x(x)$: Thành phần lực biến thiên theo vị trí $x$ ($\mathrm{N}$)`,
            String.raw`$k$: Độ cứng của lò xo ($\mathrm{N/m}$)`,
            String.raw`$x_1, x_2$: Độ biến dạng của lò xo tại vị trí đầu và cuối ($\mathrm{m}$)`
          ],
          description: String.raw`Trên đồ thị $F_x$ theo $x$, công thực hiện bằng diện tích có dấu giới hạn bởi đường cong và trục hoành.`
        }
      ]
    },
    {
      id: 'work-energy-theorem',
      title: 'Động năng và định lý công – động năng',
      badge: 'Mục 6.2–6.3',
      items: [
        {
          name: 'Động năng chất điểm và định lý',
          formulaRows: [
            { label: 'Động năng của chất điểm', formula: d(String.raw`K = \tfrac12 mv^2`) },
            { label: 'Định lý công động năng', formula: d(String.raw`W_{\mathrm{tot}} = K_2 - K_1 = \Delta K`) }
          ],
          variables: [
            String.raw`$K$: Động năng của vật, luôn không âm ($\mathrm{J}$)`,
            String.raw`$W_{\mathrm{tot}}$: Tổng công của tất cả các ngoại lực tác dụng lên vật ($\mathrm{J}$)`,
            String.raw`$v_1, v_2$: Tốc độ của vật tại thời điểm ban đầu và thời điểm sau ($\mathrm{m/s}$)`
          ],
          description: String.raw`Tổng công của mọi ngoại lực tác dụng lên vật bằng độ biến thiên động năng của vật. Định lý nghiệm đúng cho mọi loại lực và mọi dạng quỹ đạo.`
        }
      ]
    },
    {
      id: 'power',
      title: 'Công suất cơ học',
      badge: 'Mục 6.4',
      items: [
        {
          name: 'Công suất trung bình và công suất tức thời',
          formulaRows: [
            { label: 'Công suất trung bình trong khoảng thời gian', formula: d(String.raw`P_{\mathrm{av}} = \frac{\Delta W}{\Delta t}`) },
            { label: 'Công suất tức thời theo vận tốc', formula: d(String.raw`P = \frac{dW}{dt} = \vec F \cdot \vec v`) }
          ],
          variables: [
            String.raw`$P$: Công suất cơ học ($\mathrm{W}$)`,
            String.raw`$\vec v$: Vector vận tốc tức thời của điểm đặt lực ($\mathrm{m/s}$)`
          ],
          description: String.raw`Đơn vị đo chuẩn: $1\,\mathrm W = 1\,\mathrm{J/s}$. Các đơn vị thông dụng khác: Mã lực ($1\,\mathrm{hp} \approx 746\,\mathrm W$), kilowatt-giờ ($1\,\mathrm{kW\cdot h} = 3{,}6\times 10^6\,\mathrm J$).`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 7: THẾ NĂNG VÀ BẢO TOÀN NĂNG LƯỢNG
// ==========================================
export const potentialEnergyCheatsheet = {
  summary: 'Lực thế, thế năng trọng trường và đàn hồi, định luật bảo toàn cơ năng, lực phi bảo toàn và quan hệ gradient thế năng.',
  sections: [
    {
      id: 'potential-forms',
      title: 'Các dạng thế năng cơ học',
      badge: 'Mục 7.1–7.2',
      items: [
        {
          name: 'Thế năng trọng trường và thế năng đàn hồi',
          formulaRows: [
            { label: 'Thế năng trọng trường gần mặt đất', formula: d(String.raw`U_{\mathrm{grav}} = mgy,\quad W_{\mathrm{grav}} = -\Delta U_{\mathrm{grav}}`) },
            { label: 'Thế năng đàn hồi của lò xo', formula: d(String.raw`U_{\mathrm{el}} = \tfrac12 k x^2,\quad W_{\mathrm{el}} = -\Delta U_{\mathrm{el}}`) }
          ],
          variables: [
            String.raw`$U_{\mathrm{grav}}$: Thế năng trọng trường của hệ vật và Trái Đất ($\mathrm{J}$)`,
            String.raw`$y$: Cao độ của vật so với mốc thế năng chọn trước ($\mathrm{m}$)`,
            String.raw`$U_{\mathrm{el}}$: Thế năng đàn hồi của lò xo khi biến dạng $x$ ($\mathrm{J}$)`
          ],
          description: String.raw`Công của lực thế luôn bằng độ giảm thế năng: $W_{\mathrm{cons}} = -\Delta U = U_1 - U_2$. Giá trị thế năng phụ thuộc vào điểm mốc quy ước, nhưng hiệu thế năng $\Delta U$ có tính tuyệt đối.`
        }
      ]
    },
    {
      id: 'energy-conservation',
      title: 'Định luật bảo toàn cơ năng',
      badge: 'Mục 7.1–7.3',
      items: [
        {
          name: 'Bảo toàn cơ năng khi chỉ có lực thế',
          formula: d(String.raw`E = K + U = \mathrm{const} \iff K_1 + U_1 = K_2 + U_2`),
          variables: [
            String.raw`$E$: Cơ năng toàn phần của hệ kín ($\mathrm{J}$)`,
            String.raw`$K$: Tổng động năng của các vật trong hệ ($\mathrm{J}$)`,
            String.raw`$U$: Tổng thế năng của hệ ($\mathrm{J}$)`
          ],
          description: String.raw`Cơ năng của hệ kín chỉ gồm các lực thế sinh công được bảo toàn nguyên vẹn, động năng và thế năng có thể chuyển hóa qua lại lẫn nhau.`
        },
        {
          name: 'Cơ năng khi có lực không thế (Ma sát)',
          formula: d(String.raw`K_1 + U_1 + W_{\mathrm{other}} = K_2 + U_2 \iff \Delta E = W_{\mathrm{other}}`),
          variables: [
            String.raw`$W_{\mathrm{other}}$: Tổng công của các lực phi bảo toàn như ma sát hoặc lực cản ($\mathrm{J}$)`
          ],
          description: String.raw`Khi có lực ma sát sinh công âm, cơ năng của hệ giảm dần và chuyển hóa thành nội năng nhiệt: $\Delta U_{\mathrm{int}} = -W_{\mathrm{other}} = f_{\mathrm k} s$. Năng lượng toàn phần luôn được bảo toàn.`
        }
      ]
    },
    {
      id: 'force-gradient',
      title: 'Quan hệ giữa lực và thế năng',
      badge: 'Mục 7.4',
      items: [
        {
          name: 'Lực thế là đạo hàm đổi dấu của thế năng',
          formulaRows: [
            { label: 'Trường hợp chuyển động một chiều', formula: d(String.raw`F_x = -\frac{dU}{dx}`) },
            { label: 'Trường hợp không gian ba chiều', formula: d(String.raw`\vec F = -\nabla U = -\left(\frac{\partial U}{\partial x}\hat{\mathbf i} + \frac{\partial U}{\partial y}\hat{\mathbf j} + \frac{\partial U}{\partial z}\hat{\mathbf k}\right)`) }
          ],
          variables: [
            String.raw`$\vec F$: Lực thế tác dụng lên vật ($\mathrm{N}$)`,
            String.raw`$U$: Hàm thế năng của hệ phụ thuộc tọa độ vị trí ($\mathrm{J}$)`
          ],
          description: String.raw`Lực thế luôn có hướng về phía thế năng giảm. Vị trí cân bằng có $dU/dx = 0$: Cân bằng bền khi $d^2U/dx^2 > 0$ (Cực tiểu thế năng); cân bằng không bền khi $d^2U/dx^2 < 0$ (Cực đại thế năng).`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 8: ĐỘNG LƯỢNG, XUNG LƯỢNG VÀ VA CHẠM
// ==========================================
export const momentumCheatsheet = {
  summary: 'Vector động lượng, định lý xung lượng – động lượng, bảo toàn động lượng hệ kín, va chạm đàn hồi và mềm, chuyển động khối tâm và phản lực tên lửa.',
  sections: [
    {
      id: 'momentum-impulse',
      title: 'Động lượng và xung lượng',
      badge: 'Mục 8.1–8.2',
      items: [
        {
          name: 'Động lượng và định lý xung lượng – động lượng',
          formulaRows: [
            { label: 'Vector động lượng của chất điểm', formula: d(String.raw`\vec p = m\vec v`) },
            { label: 'Định luật II Newton dạng tổng quát', formula: d(String.raw`\sum\vec F = \frac{d\vec p}{dt}`) },
            { label: 'Xung lượng và độ biến thiên động lượng', formula: d(String.raw`\vec J = \int_{t_1}^{t_2} \sum\vec F\,dt = \Delta\vec p = \vec p_2 - \vec p_1`) }
          ],
          variables: [
            String.raw`$\vec p$: Vector động lượng của chất điểm ($\mathrm{kg\cdot m/s}$)`,
            String.raw`$\vec J$: Xung lượng của hợp lực trong khoảng thời gian $\Delta t$ ($\mathrm{N\cdot s}$)`,
            String.raw`$\vec F_{\mathrm{av}}$: Lực tác dụng trung bình ($\vec J = \vec F_{\mathrm{av}}\Delta t$) ($\mathrm{N}$)`
          ],
          description: String.raw`Động lượng là đại lượng vector cùng hướng với vận tốc. Xung lượng của lực tác dụng làm biến thiên động lượng của vật.`
        }
      ]
    },
    {
      id: 'momentum-conservation',
      title: 'Định luật bảo toàn động lượng',
      badge: 'Mục 8.2',
      items: [
        {
          name: 'Bảo toàn động lượng của hệ cô lập kín',
          formula: d(String.raw`\vec P_{\mathrm{tot}} = \sum_{i=1}^n \vec p_i = \mathrm{const} \iff \vec p_{A1} + \vec p_{B1} = \vec p_{A2} + \vec p_{B2}`),
          variables: [
            String.raw`$\vec P_{\mathrm{tot}}$: Tổng vector động lượng của toàn hệ ($\mathrm{kg\cdot m/s}$)`
          ],
          description: String.raw`Khi tổng ngoại lực tác dụng lên hệ triệt tiêu ($\sum\vec F_{\mathrm{ext}} = \vec 0$), tổng động lượng của hệ được bảo toàn nguyên vẹn theo cả độ lớn và hướng.`
        }
      ]
    },
    {
      id: 'collisions',
      title: 'Phân loại va chạm',
      badge: 'Mục 8.3–8.4',
      items: [
        {
          name: 'Va chạm hoàn toàn không đàn hồi (Va chạm mềm)',
          formula: d(String.raw`\vec v_2 = \frac{m_A\vec v_{A1} + m_B\vec v_{B1}}{m_A + m_B}`),
          variables: [
            String.raw`$\vec v_2$: Vận tốc chung của hai vật sau khi dính liền vào nhau ($\mathrm{m/s}$)`
          ],
          description: String.raw`Động lượng được bảo toàn, nhưng tổng động năng không bảo toàn và tổn thất một lượng cực đại chuyển hóa thành nhiệt và biến dạng.`
        },
        {
          name: 'Va chạm đàn hồi một chiều',
          formulaRows: [
            { label: 'Vận tốc tương đối đổi dấu sau va chạm', formula: d(String.raw`v_{B2x} - v_{A2x} = -(v_{B1x} - v_{A1x})`) },
            { label: 'Nghiệm vận tốc khi vật B ban đầu đứng yên', formula: d(String.raw`v_{A2x} = \frac{m_A - m_B}{m_A + m_B}v_{A1x},\quad v_{B2x} = \frac{2m_A}{m_A + m_B}v_{A1x}`) }
          ],
          variables: [
            String.raw`$v_{A1x}, v_{B1x}$: Vận tốc trước va chạm của hai vật ($\mathrm{m/s}$)`,
            String.raw`$v_{A2x}, v_{B2x}$: Vận tốc sau va chạm của hai vật ($\mathrm{m/s}$)`
          ],
          description: String.raw`Trong va chạm đàn hồi, cả động lượng và tổng động năng của hệ đều được bảo toàn nguyên vẹn.`
        }
      ]
    },
    {
      id: 'center-of-mass',
      title: 'Khối tâm và chuyển động phản lực',
      badge: 'Mục 8.5–8.6',
      items: [
        {
          name: 'Tọa độ và chuyển động của khối tâm',
          formulaRows: [
            { label: 'Tọa độ khối tâm của hệ chất điểm', formula: d(String.raw`\vec r_{\mathrm{cm}} = \frac{\sum m_i\vec r_i}{\sum m_i} = \frac{1}{M}\sum m_i\vec r_i`) },
            { label: 'Phương trình định luật II Newton cho khối tâm', formula: d(String.raw`\sum\vec F_{\mathrm{ext}} = M\vec a_{\mathrm{cm}}`) }
          ],
          variables: [
            String.raw`$M = \sum m_i$: Tổng khối lượng của hệ ($\mathrm{kg}$)`,
            String.raw`$\vec a_{\mathrm{cm}}$: Gia tốc của điểm khối tâm ($\mathrm{m/s^2}$)`
          ],
          description: String.raw`Khối tâm của hệ chuyển động như thể toàn bộ khối lượng tập trung tại đó và chịu tác dụng của tổng ngoại lực.`
        },
        {
          name: 'Phương trình chuyển động tên lửa (Tsiolkovsky)',
          formula: d(String.raw`v - v_0 = v_{\mathrm{ex}}\ln\left(\frac{m_0}{m}\right),\quad F_{\mathrm{thrust}} = -v_{\mathrm{ex}}\frac{dm}{dt}`),
          variables: [
            String.raw`$v_{\mathrm{ex}}$: Tốc độ phụt khí tương đối so với tên lửa ($\mathrm{m/s}$)`,
            String.raw`$m_0, m$: Khối lượng ban đầu và khối lượng còn lại của tên lửa ($\mathrm{kg}$)`,
            String.raw`$F_{\mathrm{thrust}}$: Lực đẩy phản lực của động cơ tên lửa ($\mathrm{N}$)`
          ],
          description: String.raw`Lực đẩy phản lực sinh ra do sự biến thiên khối lượng của hệ khi phụt nhiên liệu khí với tốc độ $v_{\mathrm{ex}}$.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 9: CHUYỂN ĐỘNG QUAY CỦA VẬT RẮN
// ==========================================
export const rotationKinematicsCheatsheet = {
  summary: 'Tọa độ góc, vận tốc và gia tốc góc, mối liên hệ chuyển động thẳng và quay, động năng quay, momen quán tính và định lý Steiner.',
  sections: [
    {
      id: 'angular-kinematics',
      title: 'Các đại lượng động học góc',
      badge: 'Mục 9.1–9.2',
      items: [
        {
          name: 'Vận tốc góc và gia tốc góc tức thời',
          formulaRows: [
            { label: 'Vận tốc góc là đạo hàm của tọa độ góc', formula: d(String.raw`\omega = \frac{d\theta}{dt}`) },
            { label: 'Gia tốc góc là đạo hàm của vận tốc góc', formula: d(String.raw`\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}`) }
          ],
          variables: [
            String.raw`$\theta$: Tọa độ góc của vật ($\mathrm{rad}$)`,
            String.raw`$\omega$: Vận tốc góc tức thời ($\mathrm{rad/s}$)`,
            String.raw`$\alpha$: Gia tốc góc tức thời ($\mathrm{rad/s^2}$)`
          ],
          description: String.raw`Góc $\theta$ bắt buộc tính bằng radian ($1\,\mathrm{rev} = 2\pi\,\mathrm{rad} = 360^\circ$). Vận tốc góc và gia tốc góc là các đại lượng đại số theo trục quay.`
        },
        {
          name: 'Bốn phương trình quay với gia tốc góc không đổi',
          formulaRows: [
            { label: 'Vận tốc góc sau thời gian t', formula: d(String.raw`\omega = \omega_0 + \alpha t`) },
            { label: 'Độ dời góc sau thời gian t', formula: d(String.raw`\theta - \theta_0 = \omega_0 t + \tfrac12\alpha t^2`) },
            { label: 'Hệ thức độc lập thời gian', formula: d(String.raw`\omega^2 - \omega_0^2 = 2\alpha(\theta - \theta_0)`) },
            { label: 'Độ dời góc theo vận tốc đầu và cuối', formula: d(String.raw`\theta - \theta_0 = \tfrac12(\omega_0 + \omega)t`) }
          ],
          variables: [
            String.raw`$\omega_0$: Vận tốc góc ban đầu tại thời điểm $t = 0$ ($\mathrm{rad/s}$)`,
            String.raw`$\alpha$: Gia tốc góc không đổi của vật rắn ($\mathrm{rad/s^2}$)`
          ],
          description: String.raw`Hệ phương trình chỉ áp dụng khi gia tốc góc $\alpha$ không đổi trong suốt khoảng thời gian khảo sát.`
        }
      ]
    },
    {
      id: 'linear-angular',
      title: 'Quan hệ giữa đại lượng dài và đại lượng góc',
      badge: 'Mục 9.3',
      items: [
        {
          name: 'Chuyển động của một điểm cách trục quay khoảng r',
          formulaRows: [
            { label: 'Quãng đường đi trên cung tròn', formula: d(String.raw`s = r\theta`) },
            { label: 'Tốc độ dài tiếp tuyến', formula: d(String.raw`v = r\omega`) },
            { label: 'Gia tốc tiếp tuyến làm đổi tốc độ', formula: d(String.raw`a_{\mathrm{tan}} = r\alpha`) },
            { label: 'Gia tốc hướng tâm làm đổi hướng vận tốc', formula: d(String.raw`a_{\mathrm{rad}} = \frac{v^2}{r} = \omega^2 r`) }
          ],
          variables: [
            String.raw`$r$: Khoảng cách vuông góc từ điểm khảo sát đến trục quay ($\mathrm{m}$)`,
            String.raw`$v$: Tốc độ dài tức thời ($\mathrm{m/s}$)`
          ],
          description: String.raw`Gia tốc toàn phần của điểm là $a = \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2} = r\sqrt{\alpha^2 + \omega^4}$.`
        }
      ]
    },
    {
      id: 'rotational-inertia',
      title: 'Momen quán tính và động năng quay',
      badge: 'Mục 9.4–9.5',
      items: [
        {
          name: 'Động năng quay và biểu thức momen quán tính',
          formulaRows: [
            { label: 'Động năng của vật rắn quay quanh trục', formula: d(String.raw`K_{\mathrm{rot}} = \tfrac12 I\omega^2`) },
            { label: 'Momen quán tính hệ chất điểm', formula: d(String.raw`I = \sum_{i=1}^n m_i r_i^2 = m_1 r_1^2 + \dots + m_n r_n^2`) },
            { label: 'Momen quán tính vật liên tục', formula: d(String.raw`I = \int r^2\,dm`) }
          ],
          variables: [
            String.raw`$K_{\mathrm{rot}}$: Động năng quay của vật rắn ($\mathrm{J}$)`,
            String.raw`$I$: Momen quán tính của vật rắn đối với trục quay đã cho ($\mathrm{kg\cdot m^2}$)`
          ],
          description: String.raw`Momen quán tính đo mức quán tính của vật rắn trong chuyển động quay, phụ thuộc vào khối lượng và sự phân bố khối lượng quanh trục quay.`
        },
        {
          name: 'Định lý trục song song (Steiner)',
          formula: d(String.raw`I_P = I_{\mathrm{cm}} + Md^2`),
          variables: [
            String.raw`$I_P$: Momen quán tính đối với trục quay đi qua điểm $P$ ($\mathrm{kg\cdot m^2}$)`,
            String.raw`$I_{\mathrm{cm}}$: Momen quán tính đối với trục song song đi qua khối tâm ($\mathrm{kg\cdot m^2}$)`,
            String.raw`$M$: Tổng khối lượng của vật rắn ($\mathrm{kg}$)`,
            String.raw`$d$: Khoảng cách vuông góc giữa hai trục song song ($\mathrm{m}$)`
          ],
          description: String.raw`Trục quay qua khối tâm luôn có momen quán tính nhỏ nhất so với tất cả các trục song song với nó.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 10: ĐỘNG LỰC HỌC CHUYỂN ĐỘNG QUAY
// ==========================================
export const rotationDynamicsCheatsheet = {
  summary: 'Momen lực, phương trình cơ bản động lực học quay, chuyển động lăn không trượt, bảo toàn momen động lượng và hiện tượng tuế sai.',
  sections: [
    {
      id: 'torque-equation',
      title: 'Momen lực và phương trình chuyển động quay',
      badge: 'Mục 10.1–10.2',
      items: [
        {
          name: 'Định nghĩa momen lực',
          formulaRows: [
            { label: 'Biểu thức vector tích có hướng', formula: d(String.raw`\vec\tau = \vec r \times \vec F`) },
            { label: 'Độ lớn momen lực qua cánh tay đòn', formula: d(String.raw`\tau = F l = r F\sin\phi`) }
          ],
          variables: [
            String.raw`$\vec\tau$: Vector momen lực đối với một điểm hoặc trục quay ($\mathrm{N\cdot m}$)`,
            String.raw`$l = r\sin\phi$: Cánh tay đòn của lực, khoảng cách vuông góc từ trục quay đến giá của lực ($\mathrm{m}$)`
          ],
          description: String.raw`Momen lực đặc trưng cho tác dụng làm quay của lực. Chiều dương quy ước theo chiều ngược chiều kim đồng hồ.`
        },
        {
          name: 'Phương trình động lực học quay quanh trục cố định',
          formula: d(String.raw`\sum\tau_z = I\alpha_z`),
          variables: [
            String.raw`$\sum\tau_z$: Tổng đại số momen các ngoại lực tác dụng quanh trục quay $z$ ($\mathrm{N\cdot m}$)`,
            String.raw`$I$: Momen quán tính của vật rắn đối với trục $z$ ($\mathrm{kg\cdot m^2}$)`,
            String.raw`$\alpha_z$: Gia tốc góc của vật quanh trục $z$ ($\mathrm{rad/s^2}$)`
          ],
          description: String.raw`Đây là dạng tương đương của định luật II Newton dành cho chuyển động quay quanh một trục cố định.`
        }
      ]
    },
    {
      id: 'rolling-motion',
      title: 'Chuyển động lăn không trượt và công suất',
      badge: 'Mục 10.3–10.4',
      items: [
        {
          name: 'Điều kiện lăn không trượt và tổng động năng',
          formulaRows: [
            { label: 'Liên hệ vận tốc và gia tốc khối tâm', formula: d(String.raw`v_{\mathrm{cm}} = R\omega,\quad a_{\mathrm{cm}} = R\alpha`) },
            { label: 'Tổng động năng của vật lăn không trượt', formula: d(String.raw`K = \tfrac12 M v_{\mathrm{cm}}^2 + \tfrac12 I_{\mathrm{cm}}\omega^2`) }
          ],
          variables: [
            String.raw`$v_{\mathrm{cm}}, a_{\mathrm{cm}}$: Vận tốc và gia tốc tịnh tiến của khối tâm ($\mathrm{m/s}, \mathrm{m/s^2}$)`,
            String.raw`$R$: Bán kính hình trụ hoặc quả cầu lăn ($\mathrm{m}$)`
          ],
          description: String.raw`Động năng toàn phần bằng tổng động năng tịnh tiến của khối tâm và động năng quay quanh trục đi qua khối tâm.`
        },
        {
          name: 'Công và công suất trong chuyển động quay',
          formulaRows: [
            { label: 'Công của momen lực làm quay góc Δθ', formula: d(String.raw`W = \int_{\theta_1}^{\theta_2}\tau_z\,d\theta = \tau_z\Delta\theta`) },
            { label: 'Công suất tức thời trong chuyển động quay', formula: d(String.raw`P = \tau_z\omega_z`) }
          ],
          variables: [
            String.raw`$W$: Công cơ học do momen lực thực hiện ($\mathrm{J}$)`,
            String.raw`$P$: Công suất quay tức thời ($\mathrm{W}$)`
          ],
          description: String.raw`Định lý công động năng quay: $W_{\mathrm{tot}} = \frac{1}{2}I\omega_2^2 - \frac{1}{2}I\omega_1^2$.`
        }
      ]
    },
    {
      id: 'angular-momentum',
      title: 'Momen động lượng và định luật bảo toàn',
      badge: 'Mục 10.5–10.6',
      items: [
        {
          name: 'Momen động lượng và định luật II tổng quát',
          formulaRows: [
            { label: 'Momen động lượng của chất điểm', formula: d(String.raw`\vec L = \vec r \times \vec p = \vec r \times (m\vec v)`) },
            { label: 'Momen động lượng của vật rắn quanh trục', formula: d(String.raw`L_z = I\omega_z,\quad \sum\tau_z = \frac{dL_z}{dt}`) }
          ],
          variables: [
            String.raw`$\vec L$: Vector momen động lượng ($\mathrm{kg\cdot m^2/s}$)`,
            String.raw`$L_z$: Thành phần momen động lượng theo trục quay đối xứng $z$`
          ],
          description: String.raw`Tốc độ biến thiên momen động lượng của hệ bằng tổng momen các ngoại lực tác dụng lên hệ.`
        },
        {
          name: 'Định luật bảo toàn momen động lượng',
          formula: d(String.raw`\vec L_{\mathrm{tot}} = \mathrm{const} \iff I_1\omega_1 = I_2\omega_2`),
          variables: [
            String.raw`$I_1, I_2$: Momen quán tính của hệ tại hai trạng thái khác nhau ($\mathrm{kg\cdot m^2}$)`,
            String.raw`$\omega_1, \omega_2$: Vận tốc góc tương ứng của hệ ($\mathrm{rad/s}$)`
          ],
          description: String.raw`Khi tổng ngoại momen lực tác dụng lên hệ triệt tiêu ($\sum\vec\tau_{\mathrm{ext}} = \vec 0$), momen động lượng toàn phần của hệ được bảo toàn nguyên vẹn.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 11: CÂN BẰNG VÀ ĐÀN HỒI
// ==========================================
export const equilibriumElasticityCheatsheet = {
  summary: 'Hai điều kiện cân bằng tĩnh học của vật rắn, trọng tâm, định luật Hooke cho biến dạng kéo nén, biến dạng thể tích và biến dạng trượt.',
  sections: [
    {
      id: 'equilibrium-rules',
      title: 'Hai điều kiện cân bằng tĩnh học',
      badge: 'Mục 11.1–11.3',
      items: [
        {
          name: 'Cân bằng tịnh tiến và cân bằng quay',
          formulaRows: [
            { label: 'Điều kiện 1: Hợp lực tịnh tiến triệt tiêu', formula: d(String.raw`\sum\vec F = \vec 0 \iff \begin{cases}\sum F_x = 0, \\ \sum F_y = 0.\end{cases}`) },
            { label: 'Điều kiện 2: Hợp momen lực quanh điểm bất kỳ triệt tiêu', formula: d(String.raw`\sum\vec\tau = \vec 0 \iff \sum\tau_z = 0`) }
          ],
          variables: [
            String.raw`$\sum\vec F$: Tổng các ngoại lực tác dụng lên vật rắn ($\mathrm{N}$)`,
            String.raw`$\sum\vec\tau$: Tổng momen các ngoại lực tính đối với điểm quay tùy ý ($\mathrm{N\cdot m}$)`
          ],
          description: String.raw`Cả hai điều kiện phải đồng thời thỏa mãn để vật rắn ở trạng thái cân bằng tĩnh học (đứng yên hoàn toàn).`
        }
      ]
    },
    {
      id: 'elastic-moduli',
      title: 'Ứng suất, biến dạng và các Modulus đàn hồi',
      badge: 'Mục 11.4–11.5',
      items: [
        {
          name: 'Biến dạng kéo nén và Modulus Young',
          formula: d(String.raw`Y = \frac{\text{Ứng suất kéo}}{\text{Biến dạng dài}} = \frac{F_\perp / A}{\Delta l / l_0} \iff \Delta l = \frac{1}{Y}\frac{F_\perp}{A}l_0`),
          variables: [
            String.raw`$Y$: Modulus Young của vật liệu đàn hồi ($\mathrm{Pa} = \mathrm{N/m^2}$)`,
            String.raw`$F_\perp$: Lực tác dụng vuông góc lên tiết diện thanh ($\mathrm{N}$)`,
            String.raw`$A$: Diện tích tiết diện ngang của thanh ($\mathrm{m^2}$)`,
            String.raw`$\Delta l$: Độ biến dạng dài của thanh ($\mathrm{m}$)`,
            String.raw`$l_0$: Chiều dài ban đầu tự nhiên của thanh ($\mathrm{m}$)`
          ],
          description: String.raw`Định luật Hooke cho biến dạng dài chỉ nghiệm đúng trong giới hạn tỷ lệ đàn hồi của vật liệu.`
        },
        {
          name: 'Biến dạng thể tích và Modulus khối (Bulk Modulus)',
          formula: d(String.raw`B = -\frac{\Delta p}{\Delta V / V_0} \iff \Delta V = -\frac{V_0\Delta p}{B}`),
          variables: [
            String.raw`$B$: Modulus khối của vật chất ($\mathrm{Pa}$)`,
            String.raw`$\Delta p$: Độ tăng áp suất tác dụng đều từ mọi hướng ($\mathrm{Pa}$)`,
            String.raw`$\Delta V$: Độ biến thiên thể tích của vật (Dấu âm biểu thị thể tích giảm khi áp suất tăng) ($\mathrm{m^3}$)`,
            String.raw`$k = 1/B$: Độ nén của vật chất ($\mathrm{Pa^{-1}}$)`
          ],
          description: String.raw`Dấu trừ đảm bảo $B$ luôn là một số dương khi thể tích giảm dưới áp suất nén.`
        },
        {
          name: 'Biến dạng trượt và Modulus trượt (Shear Modulus)',
          formula: d(String.raw`S = \frac{\text{Ứng suất trượt}}{\text{Biến dạng trượt}} = \frac{F_\parallel / A}{x / h}`),
          variables: [
            String.raw`$S$: Modulus trượt của chất rắn ($\mathrm{Pa}$)`,
            String.raw`$F_\parallel$: Lực tiếp tuyến tác dụng song song với bề mặt ($\mathrm{N}$)`,
            String.raw`$x / h = \tan\phi \approx \phi$: Biến dạng trượt tỷ đối theo góc trượt $\phi$`
          ],
          description: String.raw`Chỉ chất rắn mới có modulus trượt $S$, chất lưu tĩnh không có modulus trượt vì không chịu được ứng suất cắt tĩnh.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 12: CƠ HỌC CHẤT LƯU
// ==========================================
export const fluidMechanicsCheatsheet = {
  summary: 'Áp suất thủy tĩnh, định luật Pascal, lực đẩy Archimedes, phương trình liên tục của dòng chảy và phương trình Bernoulli.',
  sections: [
    {
      id: 'fluid-pressure',
      title: 'Áp suất thủy tĩnh và định luật Pascal',
      badge: 'Mục 12.1–12.2',
      items: [
        {
          name: 'Áp suất theo độ sâu trong chất lưu không nén được',
          formula: d(String.raw`\begin{aligned}&p = p_0 + \rho gh, \\ &p_2 - p_1 = \rho g(y_1 - y_2).\end{aligned}`),
          variables: [
            String.raw`$p$: Áp suất tuyệt đối ở độ sâu $h$ trong lòng chất lưu ($\mathrm{Pa}$)`,
            String.raw`$p_0$: Áp suất ở bề mặt thoáng, thường là áp suất khí quyển $p_{\mathrm{atm}}$ ($\mathrm{Pa}$)`,
            String.raw`$\rho$: Khối lượng riêng của chất lưu ($\mathrm{kg/m^3}$)`,
            String.raw`$h$: Độ sâu đo thẳng đứng từ mặt thoáng xuống điểm khảo sát ($\mathrm{m}$)`
          ],
          description: String.raw`Áp suất ở cùng một độ sâu trong cùng một chất lưu đứng yên là như nhau theo mọi hướng. Đơn vị đo: Một atm tương đương khoảng $1{,}013\times 10^5\,\mathrm{Pa}$ hoặc $760\,\mathrm{mmHg}$.`
        },
        {
          name: 'Nguyên lý truyền áp suất Pascal',
          formula: d(String.raw`\frac{F_1}{A_1} = \frac{F_2}{A_2} \iff F_2 = F_1\frac{A_2}{A_1}`),
          variables: [
            String.raw`$F_1, F_2$: Lực tác dụng lên hai piston ở máy nâng thủy lực ($\mathrm{N}$)`,
            String.raw`$A_1, A_2$: Diện tích tiết diện của hai piston tương ứng ($\mathrm{m^2}$)`
          ],
          description: String.raw`Độ tăng áp suất tác dụng lên một bình chất lưu kín được truyền nguyên vẹn tới mọi điểm trong lòng chất lưu và tới thành bình.`
        }
      ]
    },
    {
      id: 'buoyancy',
      title: 'Lực đẩy Archimedes và điều kiện nổi',
      badge: 'Mục 12.3',
      items: [
        {
          name: 'Định luật Archimedes',
          formula: d(String.raw`F_{\mathrm B} = \rho_{\mathrm{fluid}} V_{\mathrm{sub}} g`),
          variables: [
            String.raw`$F_{\mathrm B}$: Độ lớn lực đẩy Archimedes hướng thẳng đứng lên trên ($\mathrm{N}$)`,
            String.raw`$\rho_{\mathrm{fluid}}$: Khối lượng riêng của chất lưu xung quanh ($\mathrm{kg/m^3}$)`,
            String.raw`$V_{\mathrm{sub}}$: Thể tích phần vật chìm trong lòng chất lưu ($\mathrm{m^3}$)`
          ],
          description: String.raw`Lực đẩy Archimedes có độ lớn đúng bằng trọng lượng phần chất lưu bị vật chiếm chỗ. Vật nổi cân bằng khi trọng lượng vật bằng lực đẩy: $\frac{V_{\mathrm{sub}}}{V_{\mathrm{tot}}} = \frac{\rho_{\mathrm{object}}}{\rho_{\mathrm{fluid}}}$.`
        }
      ]
    },
    {
      id: 'fluid-dynamics',
      title: 'Động lực học chất lưu lý tưởng',
      badge: 'Mục 12.4–12.5',
      items: [
        {
          name: 'Phương trình liên tục của dòng chảy',
          formula: d(String.raw`A_1 v_1 = A_2 v_2 = \frac{dV}{dt} = \mathrm{const}`),
          variables: [
            String.raw`$A_1, A_2$: Diện tích tiết diện của ống dòng tại hai vị trí ($\mathrm{m^2}$)`,
            String.raw`$v_1, v_2$: Tốc độ dòng chảy tại các tiết diện tương ứng ($\mathrm{m/s}$)`,
            String.raw`$\frac{dV}{dt}$: Lưu lượng thể tích không đổi của chất lưu lý tưởng ($\mathrm{m^3/s}$)`
          ],
          description: String.raw`Chất lưu không nén được chảy qua tiết diện càng nhỏ thì tốc độ dòng chảy càng lớn.`
        },
        {
          name: 'Phương trình Bernoulli cho chất lưu lý tưởng',
          formula: d(String.raw`\begin{aligned}p_1 + \tfrac12\rho v_1^2 + \rho g y_1 &= \mathrm{const}, \\ p_2 + \tfrac12\rho v_2^2 + \rho g y_2 &= \mathrm{const}.\end{aligned}`),
          variables: [
            String.raw`$p$: Áp suất tĩnh của chất lưu ($\mathrm{Pa}$)`,
            String.raw`$\frac{1}{2}\rho v^2$: Áp suất động liên quan đến tốc độ dòng chảy ($\mathrm{Pa}$)`,
            String.raw`$\rho g y$: Thành phần áp suất do cao độ trọng trường ($\mathrm{Pa}$)`
          ],
          description: String.raw`Phương trình biểu thị sự bảo toàn năng lượng dọc theo một đường dòng. Định lý Torricelli: Tốc độ chất lưu thoát ra từ lỗ nhỏ ở đáy bình hở là $v = \sqrt{2gh}$.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 13: HẤP DẪN
// ==========================================
export const gravitationCheatsheet = {
  summary: 'Định luật vạn vật hấp dẫn của Newton, thế năng hấp dẫn vũ trụ, các vận tốc vũ trụ, quỹ đạo vệ tinh và ba định luật Kepler.',
  sections: [
    {
      id: 'gravitational-force',
      title: 'Định luật vạn vật hấp dẫn của Newton',
      badge: 'Mục 13.1–13.2',
      items: [
        {
          name: 'Lực hấp dẫn giữa hai khối lượng điểm',
          formula: d(String.raw`F_{\mathrm g} = G\frac{m_1 m_2}{r^2}`),
          variables: [
            String.raw`$F_{\mathrm g}$: Độ lớn lực hút hấp dẫn giữa hai vật ($\mathrm{N}$)`,
            String.raw`$G$: Hằng số hấp dẫn phổ quát ($\approx 6{,}674\times 10^{-11}\,\mathrm{N\cdot m^2/kg^2}$)`,
            String.raw`$m_1, m_2$: Khối lượng của hai chất điểm hoặc hai quả cầu đồng nhất ($\mathrm{kg}$)`,
            String.raw`$r$: Khoảng cách giữa hai tâm khối lượng ($r > 0$) ($\mathrm{m}$)`
          ],
          description: String.raw`Lực hấp dẫn luôn là lực hút, nằm dọc theo đường nối hai tâm vật. Quả cầu phân bố khối lượng đối xứng cầu hút các vật bên ngoài như thể toàn bộ khối lượng tập trung ở tâm.`
        },
        {
          name: 'Gia tốc trọng trường theo độ cao',
          formula: d(String.raw`g(r) = \frac{GM_{\mathrm E}}{r^2},\quad g_0 = \frac{GM_{\mathrm E}}{R_{\mathrm E}^2}`),
          variables: [
            String.raw`$g(r)$: Gia tốc rơi tự do ở khoảng cách $r$ tính từ tâm Trái Đất ($r \ge R_{\mathrm E}$) ($\mathrm{m/s^2}$)`,
            String.raw`$g_0$: Gia tốc trọng trường tại mặt đất ($\approx 9{,}80\,\mathrm{m/s^2}$)`,
            String.raw`$M_{\mathrm E}, R_{\mathrm E}$: Khối lượng và bán kính của Trái Đất`
          ],
          description: String.raw`Gia tốc trọng trường tỷ lệ nghịch với bình phương khoảng cách tính từ tâm Trái Đất.`
        }
      ]
    },
    {
      id: 'gravitational-energy',
      title: 'Thế năng hấp dẫn và năng lượng quỹ đạo',
      badge: 'Mục 13.3–13.4',
      items: [
        {
          name: 'Thế năng hấp dẫn vũ trụ (Mốc ở vô cực)',
          formula: d(String.raw`\begin{aligned}&U(r) = -G\frac{mM}{r}, \\ &W_{\mathrm{grav}} = GMm\left(\frac{1}{r_2} - \frac{1}{r_1}\right).\end{aligned}`),
          variables: [
            String.raw`$U(r)$: Thế năng hấp dẫn của hệ hai vật với mốc quy ước $U(\infty) = 0$ ($\mathrm{J}$)`
          ],
          description: String.raw`Thế năng hấp dẫn luôn có giá trị âm vì lực hấp dẫn là lực hút và công phải bỏ ra để tách rời hai vật ra xa vô cực.`
        },
        {
          name: 'Vận tốc vũ trụ và năng lượng cơ học vệ tinh',
          formulaRows: [
            { label: 'Vận tốc quỹ đạo tròn bán kính r', formula: d(String.raw`v_{\mathrm{orb}} = \sqrt{\frac{GM}{r}}`) },
            { label: 'Vận tốc thoát ly khỏi bề mặt thiên thể', formula: d(String.raw`v_{\mathrm{esc}} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}`) },
            { label: 'Cơ năng của vệ tinh trên quỹ đạo tròn', formula: d(String.raw`\begin{aligned}E &= K + U \\ &= -\frac{GMm}{2r} \\ &= \tfrac12 U = -K.\end{aligned}`) }
          ],
          variables: [
            String.raw`$v_{\mathrm{orb}}$: Tốc độ chuyển động của vệ tinh trên quỹ đạo tròn ($\mathrm{m/s}$)`,
            String.raw`$v_{\mathrm{esc}}$: Tốc độ tối thiểu để vật thoát khỏi trường hấp dẫn của thiên thể ($\mathrm{m/s}$)`,
            String.raw`$E$: Cơ năng toàn phần của vệ tinh, có giá trị âm đối với quỹ đạo đóng kín ($\mathrm{J}$)`
          ],
          description: String.raw`Đối với Trái Đất, vận tốc thoát khoảng $11{,}2\,\mathrm{km/s}$, bằng $\sqrt{2}$ lần vận tốc quỹ đạo tròn ngay sát bề mặt.`
        }
      ]
    },
    {
      id: 'kepler-laws',
      title: 'Ba định luật Kepler về chuyển động thiên thể',
      badge: 'Mục 13.5',
      items: [
        {
          name: 'Nội dung và công thức các định luật Kepler',
          formulaRows: [
            { label: 'Định luật II: Bảo toàn diện tích quét theo thời gian', formula: d(String.raw`\frac{dA}{dt} = \frac{L}{2m} = \mathrm{const}`) },
            { label: 'Định luật III: Bình phương chu kỳ theo bán trục lớn a', formula: d(String.raw`T^2 = \frac{4\pi^2}{GM_{\mathrm S}} a^3`) }
          ],
          variables: [
            String.raw`$a$: Bán trục lớn của quỹ đạo elip ($\mathrm{m}$)`,
            String.raw`$T$: Chu kỳ quay quanh Mặt Trời của hành tinh ($\mathrm{s}$)`,
            String.raw`$M_{\mathrm S}$: Khối lượng của Mặt Trời hoặc thiên thể trung tâm ($\mathrm{kg}$)`
          ],
          description: String.raw`Định luật I: Mọi hành tinh chuyển động theo quỹ đạo elip với Mặt Trời nằm ở một tiêu điểm. Định luật II là hệ quả trực tiếp của định luật bảo toàn momen động lượng trong trường lực xuyên tâm.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 14: DAO ĐỘNG
// ==========================================
export const oscillationsCheatsheet = {
  summary: 'Phương trình vi phân dao động điều hòa, con lắc lò xo, con lắc đơn, con lắc vật lý, năng lượng dao động, dao động tắt dần và cộng hưởng.',
  sections: [
    {
      id: 'shm-kinematics',
      title: 'Động học dao động điều hòa (SHM)',
      badge: 'Mục 14.1–14.2',
      items: [
        {
          name: 'Phương trình li độ, vận tốc và gia tốc',
          formulaRows: [
            { label: 'Phương trình vi phân và li độ', formula: d(String.raw`\begin{aligned}&\frac{d^2x}{dt^2} + \omega^2 x = 0, \\ &x(t) = A\cos(\omega t + \phi).\end{aligned}`) },
            { label: 'Vận tốc tức thời, sớm pha π/2 so với li độ', formula: d(String.raw`\begin{aligned}&v(t) = -\omega A\sin(\omega t + \phi), \\ &v_{\max} = \omega A.\end{aligned}`) },
            { label: 'Gia tốc tức thời, ngược pha so với li độ', formula: d(String.raw`\begin{aligned}a(t) &= -\omega^2 A\cos(\omega t + \phi) \\ &= -\omega^2 x(t), \\ a_{\max} &= \omega^2 A.\end{aligned}`) }
          ],
          variables: [
            String.raw`$x(t)$: Li độ dao động của chất điểm tại thời điểm $t$ ($\mathrm{m}$)`,
            String.raw`$A$: Biên độ dao động, giá trị li độ cực đại ($A > 0$) ($\mathrm{m}$)`,
            String.raw`$\omega$: Tần số góc của dao động ($\mathrm{rad/s}$)`,
            String.raw`$\phi$: Pha ban đầu tại thời điểm $t = 0$ ($\mathrm{rad}$)`
          ],
          description: String.raw`Gia tốc luôn tỷ lệ thuận và trái dấu với li độ, luôn hướng về vị trí cân bằng. Chu kỳ và tần số liên hệ qua: $\omega = 2\pi f = 2\pi / T$.`
        }
      ]
    },
    {
      id: 'shm-energy',
      title: 'Năng lượng và hệ thức độc lập thời gian',
      badge: 'Mục 14.3',
      items: [
        {
          name: 'Bảo toàn cơ năng trong dao động điều hòa',
          formulaRows: [
            { label: 'Cơ năng toàn phần bảo toàn', formula: d(String.raw`\begin{aligned}E &= K + U \\ &= \tfrac12 mv^2 + \tfrac12 kx^2 \\ &= \tfrac12 kA^2 \\ &= \tfrac12 mv_{\max}^2.\end{aligned}`) },
            { label: 'Hệ thức độc lập thời gian giữa x và v', formula: d(String.raw`\begin{aligned}&x^2 + \frac{v^2}{\omega^2} = A^2, \\ &v = \pm\omega\sqrt{A^2 - x^2}.\end{aligned}`) }
          ],
          variables: [
            String.raw`$E$: Cơ năng của vật dao động điều hòa ($\mathrm{J}$)`,
            String.raw`$k$: Độ cứng của hệ đàn hồi ($k = m\omega^2$) ($\mathrm{N/m}$)`
          ],
          description: String.raw`Cơ năng tỷ lệ thuận với bình phương biên độ dao động. Động năng và thế năng biến thiên tuần hoàn với tần số góc $2\omega$.`
        }
      ]
    },
    {
      id: 'pendulums',
      title: 'Các hệ dao động con lắc chuẩn',
      badge: 'Mục 14.2, 14.4–14.5',
      items: [
        {
          name: 'Tần số góc và chu kỳ của các hệ dao động',
          formulaRows: [
            { label: 'Con lắc lò xo', formula: d(String.raw`\omega = \sqrt{\frac{k}{m}},\quad T = 2\pi\sqrt{\frac{m}{k}}`) },
            { label: 'Con lắc đơn ở góc nhỏ θ ≪ 1 rad', formula: d(String.raw`\omega = \sqrt{\frac{g}{L}},\quad T = 2\pi\sqrt{\frac{L}{g}}`) },
            { label: 'Con lắc vật lý', formula: d(String.raw`\omega = \sqrt{\frac{mgd}{I}},\quad T = 2\pi\sqrt{\frac{I}{mgd}}`) },
            { label: 'Con lắc xoắn', formula: d(String.raw`\omega = \sqrt{\frac{\kappa}{I}},\quad T = 2\pi\sqrt{\frac{I}{\kappa}}`) }
          ],
          variables: [
            String.raw`$L$: Chiều dài dây treo của con lắc đơn ($\mathrm{m}$)`,
            String.raw`$d$: Khoảng cách từ trục quay đến khối tâm của con lắc vật lý ($\mathrm{m}$)`,
            String.raw`$I$: Momen quán tính của con lắc đối với trục quay ($\mathrm{kg\cdot m^2}$)`,
            String.raw`$\kappa$: Hằng số xoắn của dây treo ($\mathrm{N\cdot m/rad}$)`
          ],
          description: String.raw`Chu kỳ dao động nhỏ của con lắc đơn không phụ thuộc vào khối lượng của vật nặng.`
        }
      ]
    },
    {
      id: 'damped-resonance',
      title: 'Dao động tắt dần và hiện tượng cộng hưởng',
      badge: 'Mục 14.7–14.8',
      items: [
        {
          name: 'Dao động tắt dần yếu và hiện tượng cộng hưởng',
          formulaRows: [
            { label: 'Li độ dao động tắt dần dưới lực cản f = -bv', formula: d(String.raw`\begin{aligned}&x(t) = Ae^{-\beta t}\cos(\omega' t + \phi), \\ &\beta = \frac{b}{2m}, \\ &\omega' = \sqrt{\frac{k}{m} - \beta^2}.\end{aligned}`) },
            { label: 'Tần số góc cộng hưởng khi có lực cưỡng bức', formula: d(String.raw`\omega_{\mathrm d} \approx \omega_0 = \sqrt{\frac{k}{m}}`) }
          ],
          variables: [
            String.raw`$b$: Hệ số cản nhớt của môi trường ($\mathrm{kg/s}$)`,
            String.raw`$\beta=b/(2m)$: Hệ số suy giảm biên độ theo thời gian ($\mathrm{s^{-1}}$)`,
            String.raw`$\omega_{\mathrm d}$: Tần số góc của ngoại lực cưỡng bức tuần hoàn ($\mathrm{rad/s}$)`
          ],
          description: String.raw`Hiện tượng cộng hưởng xảy ra khi tần số ngoại lực cưỡng bức xấp xỉ bằng tần số dao động riêng của hệ, làm biên độ dao động đạt giá trị cực đại.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 15: SÓNG CƠ
// ==========================================
export const mechanicalWavesCheatsheet = {
  summary: 'Phương trình sóng truyền điều hòa, tốc độ sóng trên dây căng, công suất sóng, hiện tượng sóng dừng và điều kiện hình thành nút – bụng.',
  sections: [
    {
      id: 'wave-kinematics',
      title: 'Các đặc trưng cơ bản của sóng',
      badge: 'Mục 15.1–15.3',
      items: [
        {
          name: 'Hệ thức giữa chu kỳ, tần số, bước sóng và tốc độ sóng',
          formulaRows: [
            { label: 'Tốc độ lan truyền của pha dao động', formula: d(String.raw`v = \frac{\lambda}{T} = \lambda f`) },
            { label: 'Tần số góc và số sóng', formula: d(String.raw`\omega = 2\pi f = \frac{2\pi}{T},\quad k = \frac{2\pi}{\lambda}`) }
          ],
          variables: [
            String.raw`$v$: Tốc độ truyền sóng trong môi trường ($\mathrm{m/s}$)`,
            String.raw`$\lambda$: Bước sóng, quãng đường sóng truyền đi trong một chu kỳ ($\mathrm{m}$)`,
            String.raw`$k$: Số sóng, số radian pha trên một đơn vị chiều dài ($\mathrm{rad/m}$)`
          ],
          description: String.raw`Tốc độ sóng $v$ chỉ phụ thuộc vào tính chất cơ học của môi trường truyền sóng, không phụ thuộc vào biên độ hay tần số sóng.`
        },
        {
          name: 'Hàm sóng truyền điều hòa một chiều',
          formulaRows: [
            { label: 'Sóng truyền theo chiều dương +x', formula: d(String.raw`\begin{aligned}y(x,t) &= A\cos(kx - \omega t) \\ &= A\cos\left[2\pi\left(\tfrac{x}{\lambda} - \tfrac{t}{T}\right)\right].\end{aligned}`) },
            { label: 'Sóng truyền theo chiều âm -x', formula: d(String.raw`y(x, t) = A\cos(kx + \omega t)`) }
          ],
          variables: [
            String.raw`$y(x, t)$: Li độ dao động của phần tử môi trường tại vị trí $x$ vào thời điểm $t$ ($\mathrm{m}$)`,
            String.raw`$A$: Biên độ của sóng cơ ($\mathrm{m}$)`
          ],
          description: String.raw`Vận tốc dao động của phần tử môi trường $v_y = \frac{\partial y}{\partial t} = \omega A\sin(kx - \omega t)$ vuông góc với vận tốc truyền sóng $v$ đối với sóng ngang.`
        }
      ]
    },
    {
      id: 'wave-speed-energy',
      title: 'Tốc độ sóng và công suất truyền năng lượng',
      badge: 'Mục 15.4–15.5',
      items: [
        {
          name: 'Tốc độ sóng trên dây căng và công suất',
          formulaRows: [
            { label: 'Tốc độ sóng cơ trên dây căng', formula: d(String.raw`v = \sqrt{\frac{F}{\mu}}`) },
            { label: 'Công suất truyền sóng trung bình', formula: d(String.raw`\begin{aligned}P_{\mathrm{av}} &= \tfrac12\sqrt{\mu F}\omega^2 A^2 \\ &= \tfrac12\mu v\omega^2 A^2.\end{aligned}`) }
          ],
          variables: [
            String.raw`$F$: Lực căng của sợi dây đàn hồi ($\mathrm{N}$)`,
            String.raw`$\mu = m/L$: Mật độ khối lượng dài của sợi dây ($\mathrm{kg/m}$)`,
            String.raw`$P_{\mathrm{av}}$: Công suất trung bình truyền qua một tiết diện dây ($\mathrm{W}$)`
          ],
          description: String.raw`Công suất truyền sóng tỷ lệ thuận với bình phương biên độ và bình phương tần số góc của sóng.`
        }
      ]
    },
    {
      id: 'standing-waves',
      title: 'Hiện tượng sóng dừng',
      badge: 'Mục 15.6–15.8',
      items: [
        {
          name: 'Phương trình sóng dừng và điều kiện nút, bụng',
          formulaRows: [
            { label: 'Hàm sóng dừng khi đầu x = 0 là nút cố định', formula: d(String.raw`y(x, t) = (2A\sin kx)\sin\omega t`) },
            { label: 'Vị trí các nút sóng (Biên độ triệt tiêu)', formula: d(String.raw`x_n = n\frac{\lambda}{2},\quad n = 0, 1, 2, \dots`) },
            { label: 'Vị trí các bụng sóng (Biên độ cực đại 2A)', formula: d(String.raw`x_n = \left(n + \tfrac12\right)\frac{\lambda}{2}`) }
          ],
          variables: [
            String.raw`$2A\sin kx$: Biên độ dao động của phần tử tại tọa độ $x$ ($\mathrm{m}$)`,
            String.raw`$n=0,1,2,\dots$: Chỉ số các nút và bụng sóng theo chiều dương trục $x$`
          ],
          description: String.raw`Khoảng cách giữa hai nút sóng liên tiếp hoặc hai bụng sóng liên tiếp bằng nửa bước sóng $\lambda/2$. Khoảng cách từ một nút đến bụng liền kề bằng $\lambda/4$.`
        },
        {
          name: 'Tần số riêng của dây hai đầu cố định dài L',
          formula: d(String.raw`f_n = n\frac{v}{2L} = n f_1`),
          variables: [
            String.raw`$f_1 = v/(2L)$: Tần số cơ bản hay họa ba thứ nhất ($\mathrm{Hz}$)`,
            String.raw`$f_n$: Tần số của họa ba thứ $n$ ($\mathrm{Hz}$), với $n=1,2,3,\dots$`
          ],
          description: String.raw`Dây hai đầu cố định có thể phát ra mọi họa ba nguyên lần tần số cơ bản. Đối với dây một đầu cố định một đầu tự do: $f_n = (2n - 1)\frac{v}{4L}$ (chỉ tồn tại các họa ba lẻ).`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 16: ÂM HỌC
// ==========================================
export const acousticsCheatsheet = {
  summary: 'Sóng âm và dao động áp suất, tốc độ truyền âm, cường độ và mức cường độ âm decibel, sóng dừng cột khí và hiệu ứng Doppler.',
  sections: [
    {
      id: 'sound-waves',
      title: 'Sóng âm và biên độ áp suất',
      badge: 'Mục 16.1',
      items: [
        {
          name: 'Biến thiên áp suất trong sóng âm',
          formulaRows: [
            { label: 'Hàm dao động áp suất', formula: d(String.raw`p(x, t) = p_{\max}\sin(kx - \omega t)`) },
            { label: 'Biên độ dao động áp suất', formula: d(String.raw`p_{\max} = B k s_{\max} = \rho v\omega s_{\max}`) }
          ],
          variables: [
            String.raw`$p_{\max}$: Biên độ dao động áp suất so với áp suất khí quyển tĩnh ($\mathrm{Pa}$)`,
            String.raw`$B$: Modulus khối của môi trường truyền âm ($\mathrm{Pa}$)`,
            String.raw`$s_{\max}$: Biên độ li độ dao động dọc của phần tử môi trường ($\mathrm{m}$)`
          ],
          description: String.raw`Sóng âm là sóng dọc. Dao động áp suất lệch pha $\pi/2$ so với dao động li độ: Nút áp suất tương ứng với bụng li độ và ngược lại.`
        }
      ]
    },
    {
      id: 'sound-speed',
      title: 'Tốc độ truyền âm',
      badge: 'Mục 16.2',
      items: [
        {
          name: 'Tốc độ truyền âm trong chất lưu và khí lý tưởng',
          formulaRows: [
            { label: 'Trong chất lưu tổng quát', formula: d(String.raw`v = \sqrt{\frac{B}{\rho}}`) },
            { label: 'Trong chất khí lý tưởng', formula: d(String.raw`v = \sqrt{\frac{\gamma RT}{M}}`) }
          ],
          variables: [
            String.raw`$\gamma = C_p / C_V$: Chỉ số đoạn nhiệt của chất khí`,
            String.raw`$R$: Hằng số khí lý tưởng ($8{,}314\,\mathrm{J/(mol\cdot K)}$)`,
            String.raw`$T$: Nhiệt độ tuyệt đối của môi trường khí ($\mathrm{K}$)`,
            String.raw`$M$: Khối lượng mol của chất khí ($\mathrm{kg/mol}$)`
          ],
          description: String.raw`Tốc độ âm trong không khí ở $20^\circ\mathrm C$ ($293\,\mathrm K$) xấp xỉ $344\,\mathrm{m/s}$. Tốc độ âm tăng theo căn bậc hai của nhiệt độ tuyệt đối $T$.`
        }
      ]
    },
    {
      id: 'intensity-level',
      title: 'Cường độ âm và mức cường độ âm',
      badge: 'Mục 16.3',
      items: [
        {
          name: 'Cường độ âm và thang đo Decibel',
          formulaRows: [
            { label: 'Cường độ sóng âm', formula: d(String.raw`I = \frac{p_{\max}^2}{2\rho v} = \frac{P_{\mathrm{av}}}{4\pi r^2}`) },
            { label: 'Mức cường độ âm theo thang logarit', formula: d(String.raw`\beta = (10\,\mathrm{dB})\log_{10}\left(\frac{I}{I_0}\right)`) }
          ],
          variables: [
            String.raw`$I$: Cường độ âm, công suất truyền qua một đơn vị diện tích ($\mathrm{W/m^2}$)`,
            String.raw`$I_0$: Ngưỡng nghe chuẩn tại tần số $1000\,\mathrm{Hz}$ ($I_0 = 10^{-12}\,\mathrm{W/m^2}$)`,
            String.raw`$\beta$: Mức cường độ âm đo bằng decibel ($\mathrm{dB}$)`
          ],
          description: String.raw`Khi cường độ âm tăng lên $10$ lần thì mức cường độ âm tăng thêm $10\,\mathrm{dB}$. Tăng lên $100$ lần thì mức cường độ tăng thêm $20\,\mathrm{dB}$.`
        }
      ]
    },
    {
      id: 'pipes-doppler',
      title: 'Sóng dừng trong cột khí và hiệu ứng Doppler',
      badge: 'Mục 16.4, 16.8',
      items: [
        {
          name: 'Tần số riêng của cột không khí trong ống',
          formulaRows: [
            { label: 'Ống hở hai đầu: Đủ mọi họa ba', formula: d(String.raw`f_n = n\frac{v}{2L},\quad n = 1, 2, 3, \dots`) },
            { label: 'Ống một đầu kín, một đầu hở: Chỉ có họa ba lẻ', formula: d(String.raw`f_n = (2n - 1)\frac{v}{4L}`) },
            { label: 'Tần số phách giữa hai sóng âm', formula: d(String.raw`f_{\mathrm{beat}} = |f_a - f_b|`) }
          ],
          variables: [
            String.raw`$L$: Chiều dài của ống cộng hưởng ($\mathrm{m}$)`,
            String.raw`$n=1,2,3,\dots$: Chỉ số mode dao động của cột không khí`
          ],
          description: String.raw`Đầu hở của ống luôn là nút áp suất (bụng li độ); đầu kín của ống luôn là bụng áp suất (nút li độ).`
        },
        {
          name: 'Hiệu ứng Doppler cho sóng âm',
          formula: d(String.raw`f_{\mathrm L} = \left(\frac{v + v_{\mathrm L}}{v + v_{\mathrm S}}\right)f_{\mathrm S}`),
          variables: [
            String.raw`$f_{\mathrm L}$: Tần số âm do máy thu nhận được ($\mathrm{Hz}$)`,
            String.raw`$f_{\mathrm S}$: Tần số âm do nguồn phát phát ra ($\mathrm{Hz}$)`,
            String.raw`$v$: Tốc độ truyền âm trong không khí ($\mathrm{m/s}$)`,
            String.raw`$v_{\mathrm L}, v_{\mathrm S}$: Vận tốc của máy thu và nguồn phát theo quy ước chiều dương hướng từ máy thu đến nguồn phát`
          ],
          description: String.raw`Khi nguồn và máy thu tiến lại gần nhau, tần số nhận được tăng lên ($f_{\mathrm L} > f_{\mathrm S}$); khi ra xa nhau, tần số nhận được giảm xuống ($f_{\mathrm L} < f_{\mathrm S}$).`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 17: NHIỆT ĐỘ VÀ NHIỆT LƯỢNG
// ==========================================
export const temperatureHeatCheatsheet = {
  summary: 'Các thang đo nhiệt độ, sự nở vì nhiệt, nhiệt dung riêng, nhiệt chuyển pha, phương trình cân bằng nhiệt và ba cơ chế truyền nhiệt.',
  sections: [
    {
      id: 'temp-expansion',
      title: 'Nhiệt độ và sự nở vì nhiệt',
      badge: 'Mục 17.1–17.4',
      items: [
        {
          name: 'Quy đổi thang nhiệt độ',
          formula: d(String.raw`T_{\mathrm K} = T_{\mathrm C} + 273{,}15,\quad T_{\mathrm F} = \tfrac95 T_{\mathrm C} + 32^\circ\mathrm F`),
          variables: [
            String.raw`$T_{\mathrm K}$: Nhiệt độ tuyệt đối theo thang Kelvin ($\mathrm{K}$)`,
            String.raw`$T_{\mathrm C}$: Nhiệt độ theo thang Celsius ($^\circ\mathrm C$)`
          ],
          description: String.raw`Độ biến thiên nhiệt độ có quan hệ: $\Delta T_{\mathrm K} = \Delta T_{\mathrm C} = \frac{5}{9}\Delta T_{\mathrm F}$. Độ không tuyệt đối tương ứng $0\,\mathrm K = -273{,}15^\circ\mathrm C$.`
        },
        {
          name: 'Nở dài và nở thể tích của vật rắn',
          formulaRows: [
            { label: 'Sự nở dài theo nhiệt độ', formula: d(String.raw`\Delta L = \alpha L_0\Delta T`) },
            { label: 'Sự nở thể tích (Chất rắn đẳng hướng β ≈ 3α)', formula: d(String.raw`\Delta V = \beta V_0\Delta T \approx 3\alpha V_0\Delta T`) },
            { label: 'Ứng suất nhiệt khi hai đầu bị giữ cố định', formula: d(String.raw`\frac{F}{A} = -Y\alpha\Delta T`) }
          ],
          variables: [
            String.raw`$\alpha$: Hệ số nở dài của vật liệu ($\mathrm{K^{-1}}$ hoặc $^\circ\mathrm C^{-1}$)`,
            String.raw`$\beta$: Hệ số nở thể tích ($\mathrm{K^{-1}}$)`
          ],
          description: String.raw`Khi bị nung nóng mà không cho giãn nở ($\Delta L = 0$), trong vật xuất hiện ứng suất nén nhiệt có độ lớn rất lớn tỷ lệ với modulus Young $Y$.`
        }
      ]
    },
    {
      id: 'heat-phase-change',
      title: 'Nhiệt dung và nhiệt chuyển pha',
      badge: 'Mục 17.5–17.6',
      items: [
        {
          name: 'Nhiệt lượng làm thay đổi nhiệt độ và chuyển pha',
          formulaRows: [
            { label: 'Nhiệt lượng làm biến thiên nhiệt độ', formula: d(String.raw`Q = mc\Delta T = n C\Delta T`) },
            { label: 'Nhiệt lượng trong quá trình chuyển pha đẳng nhiệt', formula: d(String.raw`Q = \pm mL`) }
          ],
          variables: [
            String.raw`$Q$: Nhiệt lượng truyền cho hệ ($Q > 0$ khi hệ thu nhiệt, $Q < 0$ khi hệ tỏa nhiệt) ($\mathrm{J}$)`,
            String.raw`$c$: Nhiệt dung riêng của chất ($\mathrm{J/(kg\cdot K)}$)`,
            String.raw`$C$: Nhiệt dung mol của chất ($\mathrm{J/(mol\cdot K)}$)`,
            String.raw`$L$: Nhiệt ẩn chuyển pha (Nhiệt nóng chảy $L_{\mathrm f}$ hoặc nhiệt hóa hơi $L_{\mathrm v}$) ($\mathrm{J/kg}$)`
          ],
          description: String.raw`Phương trình cân bằng nhiệt trong hệ kín cô lập nhiệt: $\sum Q = 0$. Đơn vị: $1\,\mathrm{cal} = 4{,}186\,\mathrm J$.`
        }
      ]
    },
    {
      id: 'heat-transfer',
      title: 'Các cơ chế truyền nhiệt',
      badge: 'Mục 17.7',
      items: [
        {
          name: 'Dẫn nhiệt (Định luật Fourier)',
          formula: d(String.raw`H = \frac{dQ}{dt} = kA\frac{T_{\mathrm H} - T_{\mathrm C}}{L}`),
          variables: [
            String.raw`$H$: Tốc độ truyền nhiệt hay dòng nhiệt qua vật dẫn ($\mathrm{W} = \mathrm{J/s}$)`,
            String.raw`$k$: Độ dẫn nhiệt của vật liệu ($\mathrm{W/(m\cdot K)}$)`,
            String.raw`$A$: Diện tích bề mặt tiếp xúc vuông góc với dòng nhiệt ($\mathrm{m^2}$)`,
            String.raw`$L$: Chiều dày của lớp vật liệu dẫn nhiệt ($\mathrm{m}$)`
          ],
          description: String.raw`Nhiệt truyền tự phát từ vùng có nhiệt độ cao $T_{\mathrm H}$ về vùng có nhiệt độ thấp $T_{\mathrm C}$.`
        },
        {
          name: 'Bức xạ nhiệt (Định luật Stefan–Boltzmann)',
          formulaRows: [
            { label: 'Công suất bức xạ nhiệt phát ra', formula: d(String.raw`H = Ae\sigma T^4`) },
            { label: 'Dòng nhiệt bức xạ ròng trao đổi với môi trường', formula: d(String.raw`H_{\mathrm{net}} = Ae\sigma(T^4 - T_{\mathrm s}^4)`) }
          ],
          variables: [
            String.raw`$\sigma$: Hằng số Stefan–Boltzmann ($\approx 5{,}67\times 10^{-8}\,\mathrm{W/(m^2\cdot K^4)}$)`,
            String.raw`$e$: Độ phát xạ của bề mặt ($0 \le e \le 1$, vật đen tuyệt đối có $e = 1$)`,
            String.raw`$T_{\mathrm s}$: Nhiệt độ tuyệt đối của môi trường xung quanh ($\mathrm{K}$)`
          ],
          description: String.raw`Bức xạ nhiệt truyền được trong chân không dưới dạng sóng điện từ. Công suất bức xạ tỷ lệ thuận với lũy thừa bậc 4 của nhiệt độ tuyệt đối.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 18: THUYẾT ĐỘNG HỌC CHẤT KHÍ
// ==========================================
export const kineticTheoryCheatsheet = {
  summary: 'Phương trình khí lý tưởng, áp suất vi mô, động năng phân tử, phân bố vận tốc Maxwell, nguyên lý phân bố đều năng lượng và khí thực Van der Waals.',
  sections: [
    {
      id: 'ideal-gas',
      title: 'Phương trình trạng thái khí lý tưởng',
      badge: 'Mục 18.1',
      items: [
        {
          name: 'Phương trình trạng thái Clapeyron–Mendeleev',
          formula: d(String.raw`pV = nRT = N k_{\mathrm B} T`),
          variables: [
            String.raw`$p$: Áp suất tuyệt đối của khối khí ($\mathrm{Pa}$)`,
            String.raw`$V$: Thể tích chứa khối khí ($\mathrm{m^3}$)`,
            String.raw`$n$: Số mol chất khí ($\mathrm{mol}$)`,
            String.raw`$N$: Tổng số phân tử chất khí ($N = n N_{\mathrm A}$)`,
            String.raw`$R$: Hằng số khí lý tưởng ($8{,}314\,\mathrm{J/(mol\cdot K)}$)`,
            String.raw`$k_{\mathrm B} = R/N_{\mathrm A}$: Hằng số Boltzmann ($\approx 1{,}381\times 10^{-23}\,\mathrm{J/K}$)`
          ],
          description: String.raw`Phương trình nghiệm đúng cho khí thực ở điều kiện nhiệt độ không quá thấp và áp suất không quá cao.`
        }
      ]
    },
    {
      id: 'microscopic-pressure',
      title: 'Mô hình động học phân tử và tốc độ căn quân phương',
      badge: 'Mục 18.2–18.3',
      items: [
        {
          name: 'Áp suất và động năng tịnh tiến phân tử',
          formulaRows: [
            { label: 'Áp suất từ va chạm phân tử lên thành bình', formula: d(String.raw`p = \tfrac13\frac{Nm}{V}(v^2)_{\mathrm{av}} = \tfrac23\frac{N}{V}K_{\mathrm{tr,av}}`) },
            { label: 'Động năng tịnh tiến trung bình một phân tử', formula: d(String.raw`K_{\mathrm{tr,av}} = \tfrac32 k_{\mathrm B} T`) },
            { label: 'Tốc độ căn quân phương (rms)', formula: d(String.raw`v_{\mathrm{rms}} = \sqrt{(v^2)_{\mathrm{av}}} = \sqrt{\frac{3k_{\mathrm B} T}{m}} = \sqrt{\frac{3RT}{M}}`) }
          ],
          variables: [
            String.raw`$K_{\mathrm{tr,av}}$: Động năng tịnh tiến trung bình của một phân tử khí ($\mathrm{J}$)`,
            String.raw`$v_{\mathrm{rms}}$: Tốc độ căn quân phương của phân tử khí ($\mathrm{m/s}$)`,
            String.raw`$M$: Khối lượng mol của chất khí ($\mathrm{kg/mol}$)`
          ],
          description: String.raw`Nhiệt độ tuyệt đối $T$ là thước đo trực tiếp của động năng tịnh tiến trung bình của phân tử. Tổng động năng tịnh tiến của $n$ mol khí là $K_{\mathrm{tr}} = \frac{3}{2}nRT$.`
        }
      ]
    },
    {
      id: 'speeds-equipartition',
      title: 'Phân bố vận tốc và phân bố đều năng lượng',
      badge: 'Mục 18.3–18.4',
      items: [
        {
          name: 'Các tốc độ đặc trưng theo phân bố Maxwell–Boltzmann',
          formulaRows: [
            { label: 'Tốc độ có xác suất lớn nhất', formula: d(String.raw`v_{\mathrm{mp}} = \sqrt{\frac{2RT}{M}}`) },
            { label: 'Tốc độ trung bình', formula: d(String.raw`v_{\mathrm{av}} = \sqrt{\frac{8RT}{\pi M}}`) },
            { label: 'Thứ tự so sánh ba giá trị tốc độ', formula: d(String.raw`v_{\mathrm{mp}} < v_{\mathrm{av}} < v_{\mathrm{rms}}`) }
          ],
          variables: [
            String.raw`$v_{\mathrm{mp}}$: Tốc độ tương ứng với đỉnh của hàm phân bố Maxwell–Boltzmann ($\mathrm{m/s}$)`
          ],
          description: String.raw`Tỷ lệ giữa ba tốc độ là $v_{\mathrm{mp}} : v_{\mathrm{av}} : v_{\mathrm{rms}} = \sqrt{2} : \sqrt{8/\pi} : \sqrt{3} \approx 1 : 1{,}128 : 1{,}225$.`
        },
        {
          name: 'Nhiệt dung mol và nguyên lý phân bố đều năng lượng',
          formulaRows: [
            { label: 'Khí đơn nguyên tử (3 bậc tự do tịnh tiến)', formula: d(String.raw`C_V = \tfrac32 R,\quad C_p = \tfrac52 R,\quad \gamma = \tfrac53 \approx 1{,}67`) },
            { label: 'Khí lưỡng nguyên tử ở nhiệt độ phòng', formula: d(String.raw`C_V = \tfrac52 R,\quad C_p = \tfrac72 R,\quad \gamma = \tfrac75 = 1{,}40`) }
          ],
          variables: [
            String.raw`$C_V$: Nhiệt dung mol đẳng tích ($\mathrm{J/(mol\cdot K)}$)`,
            String.raw`$C_p$: Nhiệt dung mol đẳng áp ($C_p = C_V + R$) ($\mathrm{J/(mol\cdot K)}$)`,
            String.raw`$\gamma = C_p / C_V$: Chỉ số đoạn nhiệt của chất khí`
          ],
          description: String.raw`Mỗi bậc tự do đóng góp $\frac{1}{2}k_{\mathrm B}T$ vào năng lượng trung bình của một phân tử ($\frac{1}{2}RT$ vào mỗi mol).`
        }
      ]
    },
    {
      id: 'van-der-waals',
      title: 'Khí thực và phương trình Van der Waals',
      badge: 'Mục 18.6',
      items: [
        {
          name: 'Phương trình trạng thái khí thực Van der Waals',
          formula: d(String.raw`\left(p + \frac{an^2}{V^2}\right)(V - nb) = nRT`),
          variables: [
            String.raw`$a$: Hằng số bù trừ cho lực hút liên phân tử ($\mathrm{Pa\cdot m^6/mol^2}$)`,
            String.raw`$b$: Hằng số thể tích riêng của bản thân các phân tử khí ($\mathrm{m^3/mol}$)`
          ],
          description: String.raw`Số hạng $an^2/V^2$ bù trừ cho lực hút giữa các phân tử làm giảm áp suất lên thành bình; $nb$ là thể tích riêng bị chiếm chỗ không tham gia chuyển động tự do.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 19: NGUYÊN LÝ THỨ NHẤT CỦA NHIỆT ĐỘNG LỰC HỌC
// ==========================================
export const firstLawThermoCheatsheet = {
  summary: 'Công nhiệt động p-V, nội năng, nguyên lý thứ nhất nhiệt động lực học và các quá trình đẳng tích, đẳng áp, đẳng nhiệt, đoạn nhiệt của khí lý tưởng.',
  sections: [
    {
      id: 'work-internal-energy',
      title: 'Công nhiệt động và nội năng',
      badge: 'Mục 19.1–19.3',
      items: [
        {
          name: 'Công sinh ra khi thể tích biến thiên',
          formula: d(String.raw`W = \int_{V_1}^{V_2} p\,dV`),
          variables: [
            String.raw`$W$: Công cơ học do khối khí sinh ra ($\mathrm{J}$)`,
            String.raw`$p$: Áp suất tuyệt đối của khối khí trong quá trình dãn nở ($\mathrm{Pa}$)`,
            String.raw`$V_1, V_2$: Thể tích ban đầu và thể tích cuối của khối khí ($\mathrm{m^3}$)`
          ],
          description: String.raw`Quy ước dấu: Khi chất khí dãn nở ($V_2 > V_1$), hệ sinh công phát động $W > 0$; khi chất khí bị nén ($V_2 < V_1$), hệ nhận công $W < 0$. Trên giản đồ $p-V$, công bằng diện tích dưới đường biểu diễn quá trình.`
        },
        {
          name: 'Nội năng là hàm trạng thái',
          description: String.raw`Nội năng $U$ chỉ phụ thuộc trạng thái hiện tại của hệ nhiệt động. Đối với khí lý tưởng, nội năng chỉ phụ thuộc vào nhiệt độ tuyệt đối $T$: $\Delta U = n C_V\Delta T$ trong MỌI quá trình.`
        }
      ]
    },
    {
      id: 'first-law',
      title: 'Nguyên lý thứ nhất của nhiệt động lực học',
      badge: 'Mục 19.4',
      items: [
        {
          name: 'Biểu thức nguyên lý thứ nhất',
          formula: d(String.raw`\Delta U = Q - W \iff dU = dQ - dW`),
          variables: [
            String.raw`$\Delta U$: Độ biến thiên nội năng của hệ ($\mathrm{J}$)`,
            String.raw`$Q$: Nhiệt lượng hệ nhận vào ($Q > 0$ khi thu nhiệt, $Q < 0$ khi tỏa nhiệt) ($\mathrm{J}$)`,
            String.raw`$W$: Công do hệ sinh ra tác dụng lên môi trường ngoài ($\mathrm{J}$)`
          ],
          description: String.raw`Định luật bảo toàn năng lượng tổng quát cho các quá trình nhiệt động. Trong chu trình khép kín ($\Delta U = 0$), nhiệt lượng ròng nhận vào chuyển hóa hoàn toàn thành công sinh ra: $Q = W$.`
        }
      ]
    },
    {
      id: 'gas-processes',
      title: 'Bốn quá trình cơ bản của khí lý tưởng',
      badge: 'Mục 19.5–19.8',
      items: [
        {
          name: 'Quá trình đẳng tích, đẳng áp và đẳng nhiệt',
          formulaRows: [
            { label: 'Đẳng tích dV = 0: Công bằng không', formula: d(String.raw`W = 0,\quad Q = \Delta U = n C_V\Delta T`) },
            { label: 'Đẳng áp p = const: Công và nhiệt dung', formula: d(String.raw`W = p(V_2 - V_1) = nR\Delta T,\quad Q = n C_p\Delta T`) },
            { label: 'Đẳng nhiệt T = const: Nội năng không đổi', formula: d(String.raw`\Delta U = 0,\quad Q = W = nRT\ln\left(\frac{V_2}{V_1}\right) = nRT\ln\left(\frac{p_1}{p_2}\right)`) }
          ],
          variables: [
            String.raw`$C_p = C_V + R$: Hệ thức Mayer cho nhiệt dung mol của khí lý tưởng`
          ],
          description: String.raw`Trong quá trình đẳng nhiệt của khí lý tưởng, toàn bộ nhiệt lượng thu vào được chuyển hóa thành công sinh ra chống lại ngoại lực.`
        },
        {
          name: 'Quá trình đoạn nhiệt của khí lý tưởng',
          formulaRows: [
            { label: 'Điều kiện đoạn nhiệt Q = 0', formula: d(String.raw`Q = 0 \implies \Delta U = -W = n C_V(T_2 - T_1)`) },
            { label: 'Phương trình trạng thái đoạn nhiệt Poisson', formula: d(String.raw`pV^\gamma = \mathrm{const},\quad TV^{\gamma-1} = \mathrm{const}`) },
            { label: 'Công do khối khí sinh ra khi đoạn nhiệt', formula: d(String.raw`W = \frac{p_1 V_1 - p_2 V_2}{\gamma - 1} = \frac{nR(T_1 - T_2)}{\gamma - 1}`) }
          ],
          variables: [
            String.raw`$\gamma = C_p / C_V$: Chỉ số đoạn nhiệt của chất khí ($\gamma > 1$)`
          ],
          description: String.raw`Đường đoạn nhiệt trên giản đồ $p-V$ có độ dốc lớn hơn đường đẳng nhiệt tại cùng một điểm vì hệ số $\gamma > 1$. Khi khí dãn nở đoạn nhiệt, nhiệt độ của khối khí giảm xuống.`
        }
      ]
    }
  ]
}

// ==========================================
// CHƯƠNG 20: NGUYÊN LÝ THỨ HAI VÀ ENTROPY
// ==========================================
export const secondLawEntropyCheatsheet = {
  summary: 'Động cơ nhiệt, máy lạnh, chu trình và định lý Carnot, phát biểu nguyên lý II nhiệt động lực học, hàm trạng thái entropy và nguyên lý tăng entropy.',
  sections: [
    {
      id: 'engines-refrigerators',
      title: 'Động cơ nhiệt và máy làm lạnh',
      badge: 'Mục 20.1–20.4',
      items: [
        {
          name: 'Hiệu suất nhiệt của động cơ nhiệt',
          formulaRows: [
            { label: 'Công có ích thực hiện trong một chu trình', formula: d(String.raw`W = Q_{\mathrm H} + Q_{\mathrm C} = |Q_{\mathrm H}| - |Q_{\mathrm C}|`) },
            { label: 'Hiệu suất nhiệt của động cơ', formula: d(String.raw`e = \frac{W}{Q_{\mathrm H}} = 1 - \frac{|Q_{\mathrm C}|}{Q_{\mathrm H}}`) }
          ],
          variables: [
            String.raw`$Q_{\mathrm H}$: Nhiệt lượng nhận từ nguồn nóng ở nhiệt độ $T_{\mathrm H}$ ($Q_{\mathrm H} > 0$) ($\mathrm{J}$)`,
            String.raw`$Q_{\mathrm C}$: Nhiệt lượng nhả cho nguồn lạnh ở nhiệt độ $T_{\mathrm C}$ ($Q_{\mathrm C} < 0$) ($\mathrm{J}$)`,
            String.raw`$e$: Hiệu suất nhiệt của động cơ ($0 \le e < 1$)`
          ],
          description: String.raw`Động cơ nhiệt nhận nhiệt từ nguồn nóng, chuyển một phần thành công cơ học và bắt buộc phải nhả phần nhiệt lượng còn lại ra nguồn lạnh.`
        },
        {
          name: 'Hệ số hiệu quả của máy làm lạnh và bơm nhiệt',
          formulaRows: [
            { label: 'Hệ số hiệu quả máy lạnh (COP)', formula: d(String.raw`K = \frac{Q_{\mathrm C}}{|W|} = \frac{Q_{\mathrm C}}{|Q_{\mathrm H}| - Q_{\mathrm C}}`) },
            { label: 'Hệ số hiệu quả bơm nhiệt', formula: d(String.raw`K_{\mathrm{hp}} = \frac{|Q_{\mathrm H}|}{|W|} = K + 1`) }
          ],
          variables: [
            String.raw`$|W|$: Công cơ học cần cung cấp từ bên ngoài để vận hành máy ($\mathrm{J}$)`
          ],
          description: String.raw`Máy làm lạnh tiêu tốn công ngoại lực để lấy nhiệt từ nguồn lạnh và đẩy nhiệt ra nguồn nóng hơn.`
        }
      ]
    },
    {
      id: 'carnot-cycle',
      title: 'Chu trình Carnot và định lý Carnot',
      badge: 'Mục 20.5–20.6',
      items: [
        {
          name: 'Hiệu suất của chu trình Carnot thuận nghịch',
          formulaRows: [
            { label: 'Tỷ số nhiệt lượng và nhiệt độ tuyệt đối', formula: d(String.raw`\frac{|Q_{\mathrm C}|}{Q_{\mathrm H}} = \frac{T_{\mathrm C}}{T_{\mathrm H}}`) },
            { label: 'Hiệu suất cực đại của động cơ Carnot', formula: d(String.raw`e_{\mathrm{Carnot}} = 1 - \frac{T_{\mathrm C}}{T_{\mathrm H}}`) },
            { label: 'Hệ số máy lạnh Carnot', formula: d(String.raw`K_{\mathrm{Carnot}} = \frac{T_{\mathrm C}}{T_{\mathrm H} - T_{\mathrm C}}`) }
          ],
          variables: [
            String.raw`$T_{\mathrm H}, T_{\mathrm C}$: Nhiệt độ tuyệt đối của nguồn nóng và nguồn lạnh ($\mathrm{K}$)`
          ],
          description: String.raw`Định lý Carnot: Mọi động cơ nhiệt thực tế hoạt động giữa hai nguồn nhiệt cố định đều có hiệu suất nhỏ hơn hoặc cùng lắm bằng hiệu suất của động cơ Carnot thuận nghịch: $e \le e_{\mathrm{Carnot}}$.`
        }
      ]
    },
    {
      id: 'entropy-concept',
      title: 'Định nghĩa và tính toán Entropy',
      badge: 'Mục 20.7',
      items: [
        {
          name: 'Định nghĩa hàm trạng thái Entropy',
          formulaRows: [
            { label: 'Độ biến thiên entropy trong quá trình thuận nghịch', formula: d(String.raw`\Delta S = S_2 - S_1 = \int_1^2 \frac{dQ_{\mathrm{rev}}}{T}`) },
            { label: 'Quá trình chuyển pha đẳng nhiệt thuận nghịch', formula: d(String.raw`\Delta S = \frac{Q}{T} = \frac{mL}{T}`) },
            { label: 'Biến thiên entropy của khí lý tưởng', formula: d(String.raw`\Delta S = n C_V\ln\left(\frac{T_2}{T_1}\right) + nR\ln\left(\frac{V_2}{V_1}\right)`) }
          ],
          variables: [
            String.raw`$S$: Hàm trạng thái entropy ($\mathrm{J/K}$)`,
            String.raw`$dQ_{\mathrm{rev}}$: Nhiệt lượng vi phân trao đổi trong một quá trình thuận nghịch ($\mathrm{J}$)`
          ],
          description: String.raw`Entropy là hàm trạng thái: Độ biến thiên $\Delta S$ giữa hai trạng thái chỉ phụ thuộc trạng thái đầu và trạng thái cuối, không phụ thuộc vào đường đi thực tế.`
        }
      ]
    },
    {
      id: 'second-law-principle',
      title: 'Nguyên lý tăng entropy và ý nghĩa thống kê',
      badge: 'Mục 20.7–20.8',
      items: [
        {
          name: 'Nguyên lý tăng entropy của hệ cô lập',
          formula: d(String.raw`\Delta S_{\mathrm{isolated}} \ge 0`),
          description: String.raw`Trong mọi quá trình tự nhiên xảy ra trong một hệ cô lập, entropy của hệ không bao giờ giảm: Nó giữ nguyên trong quá trình thuận nghịch lý tưởng và luôn luôn tăng trong mọi quá trình thực tế bất thuận nghịch.`
        },
        {
          name: 'Công thức entropy thống kê của Boltzmann',
          formula: d(String.raw`S = k_{\mathrm B}\ln w`),
          variables: [
            String.raw`$w$: Số trạng thái vi mô tương ứng với cùng một trạng thái vĩ mô (Xác suất nhiệt động lực học)`
          ],
          description: String.raw`Entropy là thước đo định lượng mức độ hỗn loạn vi mô và mức độ phân tán năng lượng của hệ vật chất.`
        }
      ]
    }
  ]
}
