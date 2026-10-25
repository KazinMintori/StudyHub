export const physics1OscillationConcepts={
  "chu-ky-va-tan-so-dao-dong": {
    "name": "Chu kỳ và tần số dao động",
    "aliases": [
      "chu kỳ dao động",
      "tần số dao động"
    ],
    "definition": "Chu kỳ $T$ là thời gian một dao động đầy đủ. Tần số $f$ là số dao động trong một đơn vị thời gian, với $f=1/T$.",
    "example": "Vật đi từ biên này sang biên kia mới hoàn thành nửa chu kỳ trong dao động qua lại đối xứng.",
    "use": "Đổi giữa nhịp lặp và thời gian một vòng dao động.",
    "question": "Từ một biên tới biên đối diện có phải một chu kỳ đầy đủ không?",
    "answer": "Không. Cần trở về cùng vị trí và cùng trạng thái chuyển động để hoàn thành một chu kỳ."
  },
  "tan-so-goc-dao-dong": {
    "name": "Tần số góc của dao động",
    "aliases": [
      "tần số góc của dao động",
      "tần số góc dao động"
    ],
    "definition": "Tần số góc $\\omega$ bằng $2\\pi$ lần tần số, có đơn vị rad/s. Nó là tốc độ tăng của pha trong dao động hình sin có tần số không đổi.",
    "example": "Pha tăng $2\\pi$ ứng với một dao động đầy đủ, còn số chu kỳ tăng một.",
    "use": "Viết pha và liên hệ chu kỳ với phương trình dao động.",
    "question": "Tần số góc có phải tốc độ góc của mọi vật đang dao động không?",
    "answer": "Không. Vật dao động thẳng không quay trong không gian. Ký hiệu $\\omega$ vẫn mô tả tốc độ biến thiên pha của hàm sin."
  },
  "pha-dao-dong-co-hoc": {
    "name": "Pha của dao động cơ",
    "aliases": [
      "pha dao động",
      "pha ban đầu của dao động"
    ],
    "definition": "Trong $x=A\\cos(\\omega t+\\phi)$, pha là $\\omega t+\\phi$ và $\\phi$ là pha ban đầu. Pha phải phù hợp cả vị trí lẫn vận tốc đầu.",
    "example": "Cùng vị trí đầu nhưng vận tốc trái dấu có thể cho hai pha khác nhau và cùng biên độ.",
    "use": "Khôi phục trạng thái đầu và so sánh các dao động hình sin.",
    "question": "Chỉ dùng arctan của một tỷ số đã luôn xác định đúng pha chưa?",
    "answer": "Chưa. Cần xét góc phần tư từ cả dấu cos và sin hoặc dùng hàm $\\operatorname{atan2}$. Khi biên độ bằng không, pha không có giá trị vật lý duy nhất."
  },
  "dao-dong-dieu-hoa-goc": {
    "name": "Dao động điều hòa góc",
    "aliases": [
      "dao động điều hòa góc",
      "dao động xoắn"
    ],
    "definition": "Dao động góc lý tưởng có mômen phục hồi tuyến tính $\\tau_z=-\\kappa\\theta$, với $\\kappa>0$, và không có lực cản.",
    "example": "Bánh xe cân bằng quay qua lại vì lò xo xoắn tạo mômen ngược dấu góc lệch.",
    "use": "Tính tần số của các hệ quay đàn hồi.",
    "question": "Mômen quán tính trong công thức có thể lấy quanh một trục bất kỳ không?",
    "answer": "Không. $I$ phải lấy quanh đúng trục dao động, còn $\\kappa$ liên hệ mômen với góc tính bằng radian."
  },
  "con-lac-don": {
    "name": "Con lắc đơn",
    "aliases": [
      "con lắc đơn"
    ],
    "definition": "Mô hình chất điểm treo ở đầu dây không khối lượng, không dãn, dài $L$. Ở góc nhỏ tính bằng radian, chu kỳ gần bằng $2\\pi\\sqrt{L/g}$.",
    "example": "Tại đáy, gia tốc tiếp tuyến bằng không nhưng gia tốc hướng tâm vẫn hướng lên khi vật đi qua với tốc độ khác không.",
    "use": "Phân tích lực tiếp tuyến và chu kỳ dao động nhỏ của vật treo bằng dây.",
    "question": "Chu kỳ con lắc đơn có độc lập với biên độ ở mọi góc không?",
    "answer": "Không. Tính gần đẳng thời dùng cho biên độ góc nhỏ. Biên độ lớn cần hiệu chỉnh và làm chu kỳ dài hơn."
  },
  "con-lac-vat-ly": {
    "name": "Con lắc vật lý",
    "aliases": [
      "con lắc vật lý"
    ],
    "definition": "Vật có kích thước quay quanh trục treo cố định. Khi trọng tâm ở dưới trục một đoạn $d>0$, dao động góc nhỏ có chu kỳ $T=2\\pi\\sqrt{I/(mgd)}$.",
    "example": "Hai vật cùng khối lượng và cùng vị trí trọng tâm có thể có chu kỳ khác nếu mômen quán tính quanh trục khác nhau.",
    "use": "Xác định chu kỳ từ phân bố khối lượng hoặc đo mômen quán tính bằng dao động.",
    "question": "Chỉ biết vị trí trọng tâm đã đủ tính chu kỳ con lắc vật lý chưa?",
    "answer": "Chưa. Cần thêm mômen quán tính đối với chính trục treo và giữ giả thiết dao động nhỏ."
  },
  "dao-dong-cuong-buc": {
    "name": "Dao động cưỡng bức",
    "aliases": [
      "dao động cưỡng bức",
      "ngoại lực tuần hoàn"
    ],
    "definition": "Chuyển động của hệ được kích thích bởi ngoại lực tuần hoàn. Trong hệ tuyến tính có cản, sau khi quá độ tắt, tần số đáp ứng ổn định bằng tần số ngoại lực.",
    "example": "Cùng một xích đu có thể bị buộc dao động theo những nhịp khác nhau, nhưng biên độ đáp ứng phụ thuộc nhịp kích thích.",
    "use": "Phân biệt tần số riêng với tần số đáp ứng và tính cộng hưởng.",
    "question": "Đáp ứng cưỡng bức ổn định luôn có tần số riêng của dao động tự do không?",
    "answer": "Không. Tần số đáp ứng ổn định bằng tần số lực cưỡng bức. Tần số riêng cùng các tham số khác quyết định miền đáp ứng mạnh."
  },
  "tat-dan-toi-han": {
    "name": "Tắt dần tới hạn",
    "aliases": [
      "Tắt dần tới hạn",
      "tắt dần tới hạn",
      "critical damping"
    ],
    "definition": "Tắt dần tới hạn là ngưỡng giữa dao động và đáp ứng không dao động. Với hệ lò xo có lực cản tuyến tính, $b_c=2\\sqrt{km}$. Với mạch RLC nối tiếp, $R_c=2\\sqrt{L/C}$.",
    "example": "Với điện tích đầu dương và dòng đầu bằng không, nghiệm tới hạn trở về không mà không dao động lặp lại. Một vật gắn lò xo bị lệch rồi thả từ nghỉ cũng trở về mà không dao động qua lại ở ngưỡng tới hạn.",
    "use": "Phân loại đáp ứng sau một kích thích và phân biệt ngưỡng tắt dần với ngưỡng mất đỉnh cộng hưởng.",
    "question": "Ngưỡng tới hạn của dao động tự do có bằng ngưỡng mất đỉnh biên độ cưỡng bức không?",
    "answer": "Không. Ngưỡng tự do là $2\\sqrt{km}$, còn đỉnh biên độ li độ ở tần số dương mất khi $b\\ge\\sqrt{2km}$."
  }
}
export const physics1OscillationWikiDetails={
  "chu-ky-va-tan-so-dao-dong": "Chu kỳ có đơn vị giây, tần số có đơn vị hertz. Một hertz bằng một chu kỳ mỗi giây.\n\n$$\nf=\\frac1T\n$$\n\nKhông đồng nhất tần số dao động với tốc độ của vật ở một thời điểm. Vật có thể dừng tức thời ở biên trong khi tần số của cả dao động vẫn xác định.",
  "tan-so-goc-dao-dong": "$$\n\\omega=2\\pi f=\\frac{2\\pi}{T}\n$$\n\nTrong mô hình chiếu chuyển động tròn đều, $\\omega$ trùng tốc độ góc của điểm chuyển động tròn phụ trợ. Sự trùng nhau này không biến chuyển động của con trượt thẳng thành chuyển động quay.",
  "pha-dao-dong-co-hoc": "Với $A>0$, điều kiện đầu là:\n\n$$\nx_0=A\\cos\\phi\n$$\n\n$$\nv_0=-\\omega A\\sin\\phi\n$$\n\nMột lựa chọn pha phù hợp là:\n\n$$\n\\phi=\\operatorname{atan2}(-v_0/\\omega,x_0)\n$$\n\nCác pha khác nhau bởi bội nguyên của $2\\pi$ mô tả cùng trạng thái. Pha là tọa độ xác định vị trí trong một chu kỳ, không phải góc quay thật của một con trượt.",
  "dao-dong-dieu-hoa-goc": "Phương trình quay là:\n\n$$\nI\\ddot\\theta=-\\kappa\\theta\n$$\n\nDo đó, tần số góc bằng:\n\n$$\n\\omega=\\sqrt{\\frac\\kappa I}\n$$\n\nChu kỳ bằng $2\\pi/\\omega$. Cấu trúc giống hệ lò xo–vật, nhưng $I$ giữ vai trò quán tính quay còn $\\kappa$ liên hệ mômen và góc.",
  "con-lac-don": "Khi dây còn căng, đường đi là cung tròn. Trọng lực cung cấp thành phần tiếp tuyến:\n\n$$\nF_\\theta=-mg\\sin\\theta\n$$\n\nVới góc nhỏ tính bằng radian, $\\sin\\theta\\approx\\theta$. Từ đó, chu kỳ gần đúng là:\n\n$$\nT=2\\pi\\sqrt{\\frac Lg}\n$$\n\nLực căng dây theo bán kính không thay thế thành phần phục hồi tiếp tuyến. Chu kỳ góc nhỏ không phụ thuộc khối lượng vật nặng.",
  "con-lac-vat-ly": "Trọng lực gây mômen phục hồi:\n\n$$\n\\tau_z=-mgd\\sin\\theta\n$$\n\nVới góc nhỏ, trục không ma sát và trọng lực gần đều:\n\n$$\n\\omega=\\sqrt{\\frac{mgd}{I}}\n$$\n\nKý hiệu $I$ không mặc nhiên là mômen qua khối tâm. Phải chuyển trục nếu dữ kiện ban đầu cho mômen quanh trục khác.",
  "dao-dong-cuong-buc": "Xét lực $F(t)=F_{\\max}\\cos\\omega_dt$, với $m>0$, $k>0$, $b>0$. Phương trình là:\n\n$$\nm\\ddot x+b\\dot x+kx=F(t)\n$$\n\nĐặt:\n\n$$\n\\delta=k-m\\omega_d^2\n$$\n\nBiên độ ổn định là:\n\n$$\nA=\\frac{F_{\\max}}{\\sqrt{\\delta^2+b^2\\omega_d^2}}\n$$\n\nPhần dao động tự do có cản còn được cộng vào trong giai đoạn quá độ. Đáp ứng ngay sau lúc bắt đầu kích thích vì vậy có thể khác nghiệm ổn định.",
  "tat-dan-toi-han": "### Hệ lò xo có lực cản tuyến tính\n\n$$\nb_c=2\\sqrt{km}\n$$\n\nDưới tới hạn, $0<b<b_c$, bao biên giảm nhưng vật còn dao động. Tại và quá tới hạn, vật bị lệch rồi thả từ nghỉ không dao động qua lại.\n\nVới vận tốc đầu tùy ý, cần đọc đầy đủ nghiệm để xác định vật có cắt qua cân bằng một lần hay không. Căn âm trong biểu thức tần số báo không còn tần số dao động thực, không phải một dao động vật lý có “tần số ảo”.\n\nỞ ngưỡng tới hạn, nghiệm cơ học có dạng:\n\n$$\nx(t)=(C_1+C_2t)e^{-\\beta t}\n$$\n\n$$\n\\beta=\\frac{b_c}{2m}\n$$\n\nVới vị trí đầu $x_0$ và vận tốc đầu $v_0$, các hằng số thỏa:\n\n$$\nC_1=x_0,\\qquad C_2=v_0+\\beta x_0\n$$\n\n### Mạch RLC nối tiếp\n\nNgưỡng tới hạn RLC được xác định bởi nghiệm kép của phương trình đặc trưng. Với $R^2=4L/C$, tốc độ suy giảm là $\\alpha=R/(2L)$ và\n\n$$\nq(t)=(a+bt)e^{-\\alpha t}.\n$$\n\nĐiện tích đầu $q_0$ cho $a=q_0$. Dòng đầu $i_0$ cho $b=i_0+\\alpha q_0$. Với $i_0=0$ và $q_0$ dương, điện tích giữ dấu dương rồi tiến về không. Với dòng đầu khác không, $a+bt$ có thể bằng không một lần.\n\nHệ không có các lần đổi dấu lặp lại như dao động. Kết luận không dao động phải được phân biệt với kết luận không bao giờ đổi dấu dưới mọi điều kiện đầu."
}
export const physics1OscillationWikiConnections={
  "chu-ky-va-tan-so-dao-dong": [
    "dao-dong-dieu-hoa",
    "tan-so-goc-dao-dong"
  ],
  "tan-so-goc-dao-dong": [
    "chu-ky-va-tan-so-dao-dong",
    "pha-dao-dong-co-hoc"
  ],
  "pha-dao-dong-co-hoc": [
    "dao-dong-dieu-hoa",
    "tan-so-goc-dao-dong"
  ],
  "dao-dong-dieu-hoa-goc": [
    "momen-luc",
    "momen-quan-tinh",
    "dao-dong-dieu-hoa"
  ],
  "con-lac-don": [
    "dao-dong-dieu-hoa",
    "gia-toc-huong-tam",
    "con-lac-vat-ly"
  ],
  "con-lac-vat-ly": [
    "momen-quan-tinh",
    "momen-luc",
    "con-lac-don"
  ],
  "dao-dong-cuong-buc": [
    "dao-dong-tat-dan",
    "cong-huong-co-hoc",
    "tan-so-goc-dao-dong"
  ],
  "tat-dan-toi-han": [
    "dao-dong-tat-dan",
    "luc-can-tuyen-tinh",
    "cong-huong-co-hoc",
    "mach-rlc",
    "qua-tat-dan"
  ]
}
