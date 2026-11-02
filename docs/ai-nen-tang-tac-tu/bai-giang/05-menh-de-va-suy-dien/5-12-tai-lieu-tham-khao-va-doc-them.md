---
course: ai-nen-tang-tac-tu
lecture: 05-menh-de-va-suy-dien
section: topic
topic: 5-12-tai-lieu-tham-khao-va-doc-them
title: "5.12 Tài liệu tham khảo và đọc thêm"
description: "Chỉ mục lịch sử phát triển và tài liệu nghiên cứu chuyên sâu về logic mệnh đề, suy diễn tự động, lập trình logic, lập luận phi đơn điệu và mô hình nhân quả."
---

Logic mệnh đề có một lịch sử phát triển lâu dài và phong phú. Hệ thống ngữ nghĩa hình thức cho giải tích mệnh đề được trình bày trong chương này được kế thừa và phát triển từ các công trình đặt nền móng của Alfred Tarski (1956).

Thuật toán DPLL kinh điển cho bài toán thỏa mãn mệnh đề được đề xuất bởi Davis, Logemann và Loveland (1962). Giao thức tương tác khai báo – truy vấn (tell–ask protocol) giữa người dùng và cơ sở tri thức được Hector Levesque (1984) phân tích và chuẩn hóa. Phương pháp luận chẩn đoán dựa trên tính nhất quán (consistency-based diagnosis) được hình thức hóa chặt chẽ bởi de Kleer, Mackworth và Reiter (1992).

Phần lớn nền tảng lý thuyết của việc suy diễn trên mệnh đề xác định và mệnh đề Horn được phát triển trong bối cảnh rộng lớn hơn của logic bậc một (được trình bày ở Chương 15) dưới ngọn cờ của ngành lập trình logic (logic programming):

- Nguyên lý phân giải (resolution principle) được phát minh bởi John Alan Robinson (1965).
- Phân giải SLD được tiên phong khai phá bởi Robert Kowalski (1974) cùng nhóm nghiên cứu của Alain Colmerauer và cộng sự (1973) khi khai sinh ngôn ngữ Prolog, dựa trên các nghiên cứu tiền đề của Green (1969), Hayes (1973) và Hewitt (1969).
- Ngữ nghĩa điểm bất động tối tiểu (fixed-point semantics) cho các chương trình logic được Maarten van Emden và Robert Kowalski (1976) chứng minh. Cuốn chuyên khảo kinh điển của John Wylie Lloyd (1987) cung cấp nền tảng toán học toàn diện về ngữ nghĩa và các tính chất của lập trình logic.

Các nghiên cứu về phủ định như một thất bại (NAF) bắt nguồn từ công trình tiên phong của Keith Clark (1978) với khái niệm phép bao đóng Clark. Apt và Bol (1994) cung cấp một khảo cứu chi tiết về các kỹ thuật thuật toán và hệ ngữ nghĩa khác nhau cho phủ định như một thất bại. Quy trình suy diễn tiến cho NAF dựa trên hệ thống duy trì chân lý (Truth Maintenance System - TMS) của Jon Doyle (1979), người cũng đã nghiên cứu việc bổ sung và thu hồi động các mệnh đề trong cơ sở tri thức (xem Bài tập 5.15). Ý tưởng sử dụng các vị từ bất thường ($\mathit{abnormal}$) để mô hình hóa suy luận mặc định phi đơn điệu được John McCarthy (1986) khởi xướng thông qua khái niệm bao hàm chu vi (circumscription).

Khung suy luận giả thuyết (abduction) được trình bày trong chương này dựa trên hệ thống duy trì chân lý dựa trên giả định (ATMS) của Johan de Kleer (1986) và hệ thống Theorist của David Poole cùng các cộng sự (1987). Antonis Kakas và Marc Denecker (2002) đã tổng kết toàn diện các tiến bộ trong suy luận giả thuyết. Để tìm hiểu sâu về tư tưởng triết học và logic của Charles Sanders Peirce, người đầu tiên định hình khái niệm suy luận giả thuyết, bạn đọc có thể tham khảo công trình nghiên cứu của Robert Burch (2022). Việc cài đặt suy diễn Horn từ dưới lên cho ATMS nâng cao hơn khi xét đến vấn đề bổ sung động các mệnh đề và các nguyên tử khả giả định (xem Bài tập 5.16).

Phan Minh Dung (1995) đã đề xuất một khung lập luận trừu tượng (abstract argumentation framework) đóng vai trò nền tảng cho lý thuyết biện luận hiện đại. Chesñevar và cộng sự (2000) cùng Besnard và Hunter (2008) cung cấp các khảo cứu sâu rộng về các hệ thống biện luận logic và lập luận tương tác.

Các mô hình nhân quả và can thiệp được phân tích sâu sắc trong các công trình kinh điển của Judea Pearl (2009) cùng Peter Spirtes, Clark Glymour và Richard Scheines (2001) (xem thêm Chương 11).

Sự cố lỗi vi xử lý Intel Pentium FDIV và quá trình xây dựng các nhóm xác minh hình thức phần cứng tại Intel được Carl-Johan Seger (2021) ghi chép lại một cách sinh động. Xu và cộng sự (2008) cùng Armin Biere và cộng sự (2021) cung cấp cái nhìn toàn cảnh về các bộ giải SAT hiện đại cùng ứng dụng xác minh phần cứng và phần mềm. Việc ứng dụng SAT trong cấu hình dòng sản phẩm được khảo cứu bởi Sundermann và cộng sự (2021). Ứng dụng thực tế của các phương pháp hình thức để quản lý cấu hình các dòng xe của tập đoàn Mercedes-Benz được Carsten Sinz và cộng sự (2003) mô tả chi tiết. Hệ thống đặc tả hình thức TLA+ được Leslie Lamport (2002) và Markus Kuppe cùng cộng sự (2019) phát triển và hướng dẫn thực hành.

## Thư mục tài liệu tham khảo

1. Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Chapter 5: Propositions and Inference. Cambridge University Press. Bản gốc trực tuyến: [ArtInt3e.Ch5.S12.html](https://artint.info/3e/html/ArtInt3e.Ch5.S12.html).
2. Apt, K. R., & Bol, R. N. (1994). Logic programming and negation: A survey. *The Journal of Logic Programming*, 19–20, 9–71.
3. Besnard, P., & Hunter, A. (2008). *Elements of Argumentation*. MIT Press.
4. Biere, A., Heule, M., van Maaren, H., & Walsh, T. (Eds.). (2021). *Handbook of Satisfiability* (2nd ed.). IOS Press.
5. Burch, R. (2022). Charles Sanders Peirce. In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy*.
6. Chesñevar, C. I., Maguitman, A. G., & Loui, R. P. (2000). Logical models of argument. *ACM Computing Surveys*, 32(4), 337–383.
7. Clark, K. L. (1978). Negation as failure. In H. Gallaire & J. Minker (Eds.), *Logic and Data Bases* (pp. 293–322). Plenum Press.
8. Colmerauer, A., Kanoui, H., Pasero, R., & Roussel, P. (1973). *Un système de communication homme-machine en français*. Groupe de Recherche en Intelligence Artificielle, Université d'Aix-Marseille.
9. Davis, M., Logemann, G., & Loveland, D. (1962). A machine program for theorem-proving. *Communications of the ACM*, 5(7), 394–397.
10. de Kleer, J. (1986). An assumption-based TMS. *Artificial Intelligence*, 28(2), 127–162.
11. de Kleer, J., Mackworth, A. K., & Reiter, R. (1992). Characterizing diagnoses and systems. *Artificial Intelligence*, 56(2–3), 197–222.
12. Doyle, J. (1979). A truth maintenance system. *Artificial Intelligence*, 12(3), 231–272.
13. Dung, P. M. (1995). On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games. *Artificial Intelligence*, 77(2), 321–357.
14. Green, C. C. (1969). Application of theorem proving to problem solving. In *IJCAI-69* (pp. 219–239).
15. Hayes, P. J. (1973). Computation and deduction. In *Mathematical Foundations of Computer Science* (pp. 105–117).
16. Hewitt, C. (1969). PLANNER: A language for proving theorems in robots. In *IJCAI-69* (pp. 295–301).
17. Kakas, A. C., & Denecker, M. (2002). Abduction in logic programming. In *Computational Logic: Logic Programming and Beyond* (pp. 402–436). Springer.
18. Kowalski, R. (1974). Predicate logic as programming language. *Information Processing*, 74, 569–574.
19. Kuppe, M., Lamport, L., & Ricketts, D. (2019). The TLA+ proof manager. In *FM 2019* (pp. 184–200).
20. Lamport, L. (2002). *Specifying Systems: The TLA+ Language and Tools for Hardware and Software Engineers*. Addison-Wesley.
21. Levesque, H. J. (1984). Foundations of a functional approach to knowledge representation. *Artificial Intelligence*, 23(2), 155–212.
22. Lloyd, J. W. (1987). *Foundations of Logic Programming* (2nd ed.). Springer-Verlag.
23. McCarthy, J. (1986). Applications of circumscription to formalizing common-sense knowledge. *Artificial Intelligence*, 28(1), 89–116.
24. Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.
25. Poole, D., Goebel, R., & Aleliunas, R. (1987). Theorist: A logical reasoning system for defaults and diagnosis. In *The Knowledge Frontier* (pp. 331–352). Springer.
26. Robinson, J. A. (1965). A machine-oriented logic based on the resolution principle. *Journal of the ACM*, 12(1), 23–41.
27. Seger, C.-J. (2021). The FDIV bug and formal verification at Intel. *IEEE Micro*, 41(4), 10–19.
28. Sinz, C., Kaiser, A., & Küchlin, W. (2003). Formal methods for automotive configuration. In *Proceedings of the 18th IEEE International Conference on Automated Software Engineering* (pp. 72–78).
29. Spirtes, P., Glymour, C., & Scheines, R. (2001). *Causation, Prediction, and Search* (2nd ed.). MIT Press.
30. Sundermann, C. V., et al. (2021). Surveys on product configuration using SAT.
31. Tarski, A. (1956). *Logic, Semantics, Metamathematics*. Oxford University Press.
32. van Emden, M. H., & Kowalski, R. A. (1976). The semantics of predicate logic as a programming language. *Journal of the ACM*, 23(4), 733–742.
33. Xu, L., Hutter, F., Hoos, H. H., & Leyton-Brown, K. (2008). SATenstein: Automatically building local search SAT solvers. In *IJCAI-08* (pp. 517–524).
