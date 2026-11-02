// Definitions and explanations reviewed with the lesson-7 AGY manuscript.
export const propositionalConcepts={
 'he-qua-logic':{
  name:'Hệ quả logic',aliases:['Hệ quả logic','hàm nghĩa'],
  definition:'Một câu truy vấn là hệ quả logic của cơ sở tri thức khi mọi mô hình làm cơ sở tri thức đúng cũng làm truy vấn đúng.',
  example:'Từ P và P kéo theo Q, mọi mô hình của tri thức đều làm Q đúng. Vì vậy Q là hệ quả logic.',
  use:'Kiểm tra truy vấn bằng phản mô hình hoặc bằng chứng minh phản chứng.',
  question:'Không suy ra được Q có đồng nghĩa suy ra được phủ định Q không?',answer:'Không. Có thể tồn tại một mô hình làm Q đúng và một mô hình khác làm Q sai.',
 },
 'dang-chuan-cnf':{
  name:'Dạng chuẩn CNF',aliases:['Dạng chuẩn CNF','dạng chuẩn hội','Conjunctive Normal Form'],
  definition:'Dạng chuẩn hội là một phép hội giữa các clause, trong đó mỗi clause là một phép tuyển của các literal. Literal là ký hiệu nguyên tử hoặc phủ định của nó.',
  example:'Công thức $(P\\lor\\neg Q)\\land(R\\lor P)$ là hội của hai clause tuyển.',
  use:'Chuẩn hóa tri thức thành đầu vào cho hợp giải phản chứng hoặc các bộ giải SAT.',
  question:'Clause rỗng khác tập clause rỗng như thế nào?',answer:'Clause rỗng biểu diễn Sai. Tập clause rỗng không chứa ràng buộc nào nên biểu diễn Đúng.',
 }
}
const detailText={
 'he-qua-logic':'Một câu truy vấn $q$ là hệ quả logic của $KB$ khi tập mô hình của tri thức là tập con của tập mô hình truy vấn.\\n\\n$$M(KB)\\subseteq M(q).$$\\n\\nNếu có một phép gán làm mọi câu trong KB đúng nhưng q sai, phép gán đó là phản mô hình. Không có phản mô hình tương đương với việc KB cùng phủ định q không thỏa được. Nếu KB đã mâu thuẫn, nó không có mô hình và mọi câu đều là hệ quả theo logic cổ điển. Vì vậy cần báo riêng tính nhất quán.',
 'dang-chuan-cnf':'Công thức logic mệnh đề có thể chuyển về CNF tương đương bằng cách khử kéo theo và tương đương, đưa phủ định sát ký hiệu nguyên tử, rồi phân phối tuyển qua hội. Clause chứa cả một literal và phủ định của nó luôn đúng, nên có thể bỏ khỏi phép hội.\\n\\nHợp giải dùng hai clause cha và khử đúng một cặp literal đối ngẫu. Nếu dẫn xuất được clause rỗng, tập clause không thỏa được. Phân phối trực tiếp có thể làm kích thước công thức tăng theo hàm mũ. Dùng biến phụ có thể giữ kích thước nhỏ hơn, nhưng phải phân biệt bảo toàn tính thỏa được với tương đương dưới mọi phép gán cho các biến phụ.'
}
export const propositionalWikiDetails=Object.fromEntries(Object.entries(detailText).map(([id,text])=>[id,text.replaceAll('\\n','\n')]))
