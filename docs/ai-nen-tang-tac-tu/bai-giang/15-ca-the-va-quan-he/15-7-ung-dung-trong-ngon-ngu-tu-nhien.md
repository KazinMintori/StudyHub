---
course: ai-nen-tang-tac-tu
lecture: 15-ca-the-va-quan-he
section: topic
topic: 15-7-ung-dung-trong-ngon-ngu-tu-nhien
title: "15.7 Ứng dụng trong ngôn ngữ tự nhiên"
description: "Văn phạm mệnh đề xác định (DCG) và danh sách sai phân: Phân tích cú pháp, trích xuất ngữ nghĩa và xây dựng giao diện hỏi đáp cơ sở dữ liệu."
---

Xử lý ngôn ngữ tự nhiên (Natural language processing) là một miền ứng dụng thú vị và đầy thử thách để phát triển cũng như đánh giá các lý thuyết biểu diễn tri thức và suy luận. Rất nhiều bài toán của trí tuệ nhân tạo nảy sinh trong miền này; giải quyết "bài toán ngôn ngữ tự nhiên" khó khăn gần như tương đương với giải quyết "bài toán AI", bởi vì bất kỳ miền tri thức nào cũng có thể được diễn đạt bằng ngôn ngữ tự nhiên. Lĩnh vực ngôn ngữ học tính toán (computational linguistics) sở hữu một kho tàng phong phú các kỹ thuật và tri thức. Phần này chỉ cung cấp một cái nhìn tổng quan.

### Hai truyền thống trong xử lý ngôn ngữ tự nhiên

Các hệ thống xử lý ngôn ngữ tự nhiên trong AI nhìn chung đi theo hai truyền thống tiếp cận:

- **Hệ thống có độ bao phủ rộng (Broad-coverage systems)**: Cố gắng thấu hiểu ngôn ngữ tự nhiên trong đời sống thực tế, và chấp nhận có một tỷ lệ lỗi nhất định.
- **Hệ thống trong miền ràng buộc (Constrained-domain systems)**: Hoạt động trong một miền xác định, nơi người dùng được kỳ vọng sẽ sử dụng ngôn ngữ tự nhiên có kiểm soát (controlled natural language), và các kết quả thu được có thể rõ ràng, không bị nhập nhằng.

Các hệ thống thuộc loại thứ nhất thường được sử dụng cho tính năng gõ phím dự đoán trên điện thoại thông minh và cho các hệ thống dịch thuật ngôn ngữ diện rộng. Các hệ thống thuộc loại thứ hai được sử dụng khi cùng một nhóm người dùng tương tác liên tục với hệ thống, chẳng hạn như truy vấn cơ sở dữ liệu về hàng tồn kho siêu thị, trò chơi, hoặc khi ngôn ngữ được định hình theo phong cách riêng — chẳng hạn như phân tích cú pháp câu hỏi trong trò chơi truyền hình *Jeopardy!* (như hệ thống Watson của IBM đã từng thực hiện).

Một điểm khác biệt lớn giữa hai truyền thống nằm ở cách xử lý các câu hoặc câu hỏi sai ngữ pháp, hoặc các từ vựng lạ:
- Ở loại hệ thống thứ nhất, các trường hợp này được đối xử tương tự như các câu đúng ngữ pháp (hệ thống vẫn cố gắng dự đoán).
- Ngược lại, các hệ thống thuộc loại thứ hai có thể yêu cầu người dùng làm rõ ý hoặc diễn đạt lại câu hỏi, hoặc thậm chí báo thất bại đối với những câu như vậy.

Dịch thuật bằng các hệ thống bao phủ rộng rất phù hợp cho mục đích sử dụng thông thường khi cái giá phải trả cho việc sai sót là thấp, hoặc khi người giao tiếp có thể hỏi lại và trao đổi qua lại để tìm ra ý nghĩa chính xác. Tuy nhiên, người ta thường không muốn sử dụng một hệ thống như vậy trong những tình huống mà cái giá phải trả cho sai sót hoặc hiểu lầm là rất đắt, chẳng hạn như trong các hợp đồng pháp lý.

Công nghệ hiện đại cho các hệ thống có độ bao phủ rộng là học từ dữ liệu, chẳng hạn như sử dụng mạng nơ-ron và học sâu.

Chương này xem xét các hệ thống thuộc loại thứ hai, nơi các kỹ thuật logic được trình bày ở đây vẫn tiếp tục được ứng dụng hiệu quả.

Có ít nhất ba lý do để nghiên cứu xử lý ngôn ngữ tự nhiên:

- Người dùng muốn giao tiếp theo cách riêng của họ, và nhiều người ưa thích ngôn ngữ tự nhiên hơn một ngôn ngữ nhân tạo hay giao diện đồ họa. Điều này đặc biệt quan trọng đối với người dùng phổ thông hoặc những người dùng như các nhà quản lý hay trẻ em, vốn không có thời gian hoặc không muốn học các kỹ năng tương tác mới.
- Có một kho tàng thông tin khổng lồ được ghi lại bằng ngôn ngữ tự nhiên mà máy tính có thể tiếp cận được. Thông tin liên tục được tạo ra dưới dạng tin nhắn, bài viết nhật ký, sách báo, tin tức, báo cáo kinh doanh, báo cáo chính phủ và các bài báo khoa học trực tuyến. Một hệ thống cần nhiều thông tin bắt buộc phải có khả năng xử lý ngôn ngữ tự nhiên để truy xuất lượng thông tin này.
- Rất nhiều vấn đề cốt lõi của AI xuất hiện dưới dạng rất rõ ràng và tường minh trong xử lý ngôn ngữ tự nhiên, vì vậy đây là một miền lý tưởng để thử nghiệm các lý thuyết tổng quát.

Có ít nhất ba khía cạnh lớn của ngôn ngữ tự nhiên:

- **Cú pháp (Syntax)**: Mô tả hình thức của ngôn ngữ. Ngôn ngữ tự nhiên phức tạp hơn nhiều so với các ngôn ngữ hình thức dùng trong logic và lập trình. Cú pháp thường được đặc tả bằng một văn phạm. Một số mô hình ngôn ngữ tự nhiên được biểu diễn bằng mạng nơ-ron để dự đoán từng từ dựa trên ngữ cảnh xung quanh mà không cần dựng cây phân tích cú pháp tường minh.
- **Ngữ nghĩa (Semantics)**: Cung cấp ý nghĩa của các phát ngôn hoặc câu trong ngôn ngữ. Dù tồn tại các lý thuyết ngữ nghĩa tổng quát, khi xây dựng hệ thống NLP cho một ứng dụng cụ thể, người ta thường chọn cách biểu diễn đơn giản nhất có thể. Ví dụ, trong phần xây dựng dưới đây, ta sử dụng một ánh xạ cố định giữa các từ và các khái niệm trong cơ sở tri thức — cách này đơn giản hóa quá trình phát triển nhưng không phù hợp cho các miền tổng quát. Một từ có thể có nhiều nghĩa khác nhau (chẳng hạn từ "bank" vừa là bờ sông, vừa là ngân hàng). Các mô hình nơ-ron thường biểu diễn từ bằng các vector có kích thước cố định gọi là các vector nhúng (embeddings), biểu diễn vừa đủ ngữ nghĩa để dự đoán từ trong ngữ cảnh hoặc phục vụ các tác vụ huấn luyện khác.
- **Ngữ dụng (Pragmatics)**: Giải thích các phát ngôn liên hệ như thế nào với thế giới thực. Để hiểu ngôn ngữ, một tác tử cần xem xét nhiều hơn là chỉ bản thân câu nói: Tác tử phải tính đến ngữ cảnh của câu, trạng thái của thế giới, mục tiêu của người nói và người nghe, các quy ước đặc thù, cùng các yếu tố liên quan khác.

Để hiểu rõ sự khác biệt giữa các khía cạnh này, hãy xem xét các câu sau, vốn có thể xuất hiện ở đầu một cuốn sách giáo trình về AI:

1. *This book is about artificial intelligence.* (Cuốn sách này viết về trí tuệ nhân tạo).
2. *The green frogs sleep soundly.* (Những chú ếch xanh ngủ say sưa).
3. *Colorless green ideas sleep furiously.* (Những ý niệm xanh không màu ngủ một cách giận dữ).
4. *Furiously sleep ideas green colorless.* (Giận dữ ngủ ý niệm xanh không màu).

Câu thứ nhất rất phù hợp ở phần mở đầu của cuốn sách giáo trình này; câu đạt chuẩn cả về cú pháp, ngữ nghĩa lẫn ngữ dụng. Câu thứ hai đúng cú pháp và ngữ nghĩa, nhưng sẽ rất kỳ lạ nếu xuất hiện ở đầu một cuốn sách về AI; câu không phù hợp về mặt ngữ dụng đối với ngữ cảnh đó. Hai câu cuối cùng do nhà ngôn ngữ học Noam Chomsky đưa ra vào năm 1957. Câu thứ ba hoàn toàn đúng cú pháp, nhưng lại vô nghĩa về mặt ngữ nghĩa. Câu thứ tư thì sai hỏng cả về mặt cú pháp; câu hoàn toàn vô nghĩa trên cả ba phương diện: Cú pháp, ngữ nghĩa và ngữ dụng.

Phần tiếp theo trình bày cách viết một hệ thống trả lời câu hỏi bằng ngôn ngữ tự nhiên áp dụng cho các miền hẹp, sử dụng ngôn ngữ tự nhiên có phong cách cố định mà người dùng bắt buộc phải tuân theo. Cách tiếp cận này phù hợp cho những miền bài toán hầu như không có sự nhập nhằng ngữ nghĩa.

## 15.7.1 Sử dụng các câu tuyển xác định cho văn phạm phi ngữ cảnh

Mục này trình bày cách sử dụng các câu tuyển xác định để biểu diễn cú pháp và ngữ nghĩa của ngôn ngữ tự nhiên.

Ngôn ngữ được định nghĩa thông qua các câu hợp lệ của ngôn ngữ đó. Một câu là một chuỗi các thẻ (tokens), thường biểu thị các từ trong ngôn ngữ, các cụm từ phổ biến (chẳng hạn "artificial intelligence"), và dấu câu. Một số mô hình biểu diễn các từ dưới dạng các phần cấu tạo, chẳng hạn tách các đuôi như "ing" hay "er" thành các thẻ riêng biệt hoặc sử dụng chuỗi ký tự. Ở đây, các câu được biểu diễn bằng các danh sách, và các thẻ là các chuỗi ký tự đặt trong dấu ngoặc kép.

Các câu hợp lệ được đặc tả bởi một văn phạm. Một văn phạm phi ngữ cảnh (Context-free grammar — CFG) được định nghĩa bởi một tập hợp các quy tắc viết lại (rewrite rules), chuyển đổi các ký hiệu không kết thúc (non-terminal symbols) thành một chuỗi các ký hiệu kết thúc và không kết thúc. Một câu của ngôn ngữ là một chuỗi các ký hiệu kết thúc được sinh ra bởi các quy tắc viết lại như vậy. Ví dụ, quy tắc văn phạm:

<span class="logic-expression logic-block">sentence ↦ noun_phrase, verb_phrase</span>

có nghĩa là ký hiệu không kết thúc $sentence$ có thể là một $noun\_phrase$ theo sau bởi một $verb\_phrase$. Ký hiệu "$\longmapsto$" có nghĩa là "có thể được viết lại thành".

Văn phạm phi ngữ cảnh cung cấp một phép xấp xỉ bước đầu cho văn phạm của một số ngôn ngữ tự nhiên. Đối với ngôn ngữ tự nhiên, các ký hiệu kết thúc là các thẻ từ vựng của ngôn ngữ. Nếu một câu của ngôn ngữ tự nhiên được biểu diễn dưới dạng một danh sách các thẻ, câu tuyển xác định sau đây phát biểu rằng một danh sách các từ là một câu nếu nó gồm một ngữ danh từ theo sau bởi một ngữ động từ:

<span class="logic-expression logic-block">sentence(S) ← noun_phrase(N) ∧ verb_phrase(V) ∧ append(N, V, S).</span>

Để phát biểu rằng từ "country" là một danh từ, ta có thể viết:

$$
noun(["country"]).
$$

Một cách biểu diễn khác đơn giản hơn cho các quy tắc văn phạm, được gọi là văn phạm mệnh đề xác định (Definite-clause grammar — DCG), sử dụng các câu tuyển xác định mà không cần gọi tường minh vị từ $append$. Để biểu diễn một văn phạm phi ngữ cảnh, mỗi ký hiệu không kết thúc $s$ trở thành một vị từ nhận hai đối số, $s(L_{1}, L_{2})$, vốn đúng khi danh sách $L_{2}$ là phần kết thúc của danh sách $L_{1}$ sao cho toàn bộ các từ trong $L_{1}$ đứng trước $L_{2}$ tạo thành một chuỗi từ thuộc phạm trù $s$. Hai danh sách $L_{1}$ và $L_{2}$ cùng nhau tạo thành một danh sách sai phân (difference list) gồm các từ thuộc lớp cú pháp do ký hiệu không kết thúc chỉ định, bởi vì chính phần hiệu giữa hai danh sách này tạo nên phạm trù cú pháp đó.

::: example Ví dụ 15.32: Danh sách sai phân cho ngữ danh từ
Dưới cách biểu diễn này, $noun\_phrase(L_{1}, L_{2})$ đúng nếu danh sách $L_{2}$ là phần đuôi của danh sách $L_{1}$ sao cho tất cả các từ trong $L_{1}$ đứng trước $L_{2}$ tạo thành một ngữ danh từ. $L_{2}$ chính là phần của $L_{1}$ nằm phía sau ngữ danh từ.

Khẳng định sau:

```prolog
noun_phrase(["large", "country", "bordering", "Paraguay", "borders", "Chile"],
            ["bordering", "Paraguay", "borders", "Chile"])
```

là đúng trong diễn giải dự định vì cụm từ "large country" tạo thành một ngữ danh từ.

Tương tự, khẳng định:

```prolog
noun_phrase(["large", "country", "bordering", "Paraguay", "borders", "Chile"],
            ["borders", "Chile"])
```

cũng đúng vì "large country bordering Paraguay" tạo thành một ngữ danh từ.
:::

Quy tắc văn phạm:

<span class="logic-expression logic-block">sentence ↦ noun_phrase, verb_phrase</span>

có nghĩa là tồn tại một câu nằm giữa $L_{0}$ và $L_{2}$ nếu tồn tại một ngữ danh từ nằm giữa $L_{0}$ và $L_{1}$, cùng một ngữ động từ nằm giữa $L_{1}$ và $L_{2}$:

$$
\overbrace{\underbrace{L_{0}}_{noun\_phrase} \underbrace{L_{1}}_{verb\_phrase}}^{sentence} L_{2}
$$

Quy tắc văn phạm này có thể được đặc tả thành câu tuyển:

```prolog
sentence(L0, L2) :-
    noun_phrase(L0, L1),
    verb_phrase(L1, L2).
```

Tổng quát hơn, quy tắc:

$$
h \longmapsto b_{1}, b_{2}, \ldots, b_{n}
$$

nói rằng $h$ được cấu thành từ một $b_{1}$ theo sau bởi một $b_{2}$, ..., theo sau bởi một $b_{n}$, và được viết dưới dạng câu tuyển xác định:

```prolog
h(L0, Ln) :-
    b1(L0, L1),
    b2(L1, L2),
    ...
    bn(Ln_minus_1, Ln).
```

dưới cách diễn giải trực quan:

$$
\overbrace{\underbrace{L_{0}}_{b_{1}} \underbrace{L_{1}}_{b_{2}} L_{2} \cdots \underbrace{L_{n-1}}_{b_{n}}}^{h} L_{n}
$$

trong đó các $L_{i}$ là các biến riêng biệt.

Để phát biểu rằng ký hiệu không kết thúc $h$ được ánh xạ thành các ký hiệu kết thúc $t_{1}, \ldots, t_{n}$, ta viết:

$$
h([t_{1}, \ldots, t_{n} \mid T], T)
$$

với ý nghĩa:

$$
\overbrace{t_{1}, \ldots, t_{n}}^{h} T
$$

Như vậy, $h(L_{1}, L_{2})$ là đúng nếu $L_{1} = [t_{1}, \ldots, t_{n} \mid L_{2}]$.

::: example Ví dụ 15.33: Quy tắc viết lại hỗn hợp gồm ký hiệu kết thúc và không kết thúc
Quy tắc đặc tả rằng ký hiệu không kết thúc $h$ có thể được viết lại thành ký hiệu không kết thúc $a$, theo sau bởi ký hiệu không kết thúc $b$, theo sau bởi các ký hiệu kết thúc $c$ và $d$, theo sau bởi ký hiệu không kết thúc $e$, theo sau bởi ký hiệu kết thúc $f$ và ký hiệu không kết thúc $g$, có thể được viết là:

$$
h \longmapsto a, b, [c, d], e, [f], g
$$

và được biểu diễn dưới dạng câu tuyển logic:

```prolog
h(L0, L6) :-
    a(L0, L1),
    b(L1, [c, d | L3]),
    e(L3, [f | L5]),
    g(L5, L6).
```

Lưu ý rằng các phép biến đổi $L_{2} = [c, d \mid L_{3}]$ và $L_{4} = [f \mid L_{5}]$ đã được thế vào một cách tường minh để giảm số lượng biến trung gian.
:::

Dưới đây là một văn phạm phi ngữ cảnh đơn giản cho các câu hỏi tiếng Anh:

```prolog
% Một ngữ danh từ gồm một từ hạn định (mạo từ như "the" hoặc "a"), theo sau bởi các tính từ,
% theo sau bởi một danh từ, và theo sau bởi một ngữ bổ nghĩa tùy chọn
noun_phrase(L0, L4) :-
    det(L0, L1),
    adjectives(L1, L2),
    noun(L2, L3),
    omp(L3, L4).

% Các tính từ gồm một chuỗi (có thể rỗng) các tính từ
adjectives(L, L).
adjectives(L0, L2) :-
    adj(L0, L1),
    adjectives(L1, L2).

% Một ngữ bổ nghĩa là một quan hệ (động từ hoặc giới từ) theo sau bởi một ngữ danh từ
mp(L0, L2) :-
    reln(L0, L1),
    noun_phrase(L1, L2).

% Một ngữ bổ nghĩa tùy chọn là một ngữ bổ nghĩa hoặc không có gì (rỗng)
omp(L, L).
omp(L0, L1) :-
    mp(L0, L1).

% Một số câu hỏi đơn giản dạng "What" và "What is"
question(["What" | L0], L2) :-
    noun_phrase(L0, L1),
    mp(L1, L2).

question(["What", "is" | L0], L1) :-
    mp(L0, L1).
```

*Hình 15.8: Văn phạm phi ngữ cảnh cho các câu hỏi tiếng Anh đơn giản.*

Kèm theo đó là một từ điển đơn giản gồm các từ và từ loại tương ứng:

```prolog
det(L, L).
det(["a" | L], L).
det(["the" | L], L).

noun(["country" | L], L).
noun(["city" | L], L).
noun([N | L], L) :- name(E, N).

adj(["large" | L], L).

reln(["bordering" | L], L).
reln(["borders" | L], L).
reln(["next", "to" | L], L).
reln(["the", "name", "of" | L], L).
```

*Hình 15.9: Từ điển đơn giản phục vụ văn phạm.*

Quy tắc đầu tiên cho $question$ cho phép xử lý các câu hỏi như *"What country borders Chile?"* hoặc *"What large country bordering Paraguay borders Chile?"*, trong khi quy tắc thứ hai cho phép xử lý các câu hỏi như *"What is bordering Chile?"*.

::: example Ví dụ 15.34: Phân tích cú pháp ngữ danh từ trong câu hỏi địa lý
Xét câu hỏi: *"What large country bordering Paraguay borders Chile?"*. Câu hỏi này được biểu diễn dưới dạng một danh sách các chuỗi ký tự, mỗi chuỗi tương ứng với một từ.

Đối với văn phạm ở Hình 15.8, từ điển ở Hình 15.9, và định nghĩa về $name$ ở Mục 15.4, câu truy vấn:

```prolog
ask noun_phrase(["large", "country", "bordering", "Paraguay", "borders", "Chile"], R).
```

sẽ có câu trả lời là:

<span class="logic-expression logic-block">R = [&quot;bordering&quot;, &quot;Paraguay&quot;, &quot;borders&quot;, &quot;Chile&quot;]</span>

nghĩa là "large country" là một ngữ danh từ.

Một câu trả lời khác là:

$$
R = ["borders", "Chile"]
$$

nghĩa là "large country bordering Paraguay" cũng là một ngữ danh từ.
:::

## 15.7.2 Mở rộng văn phạm

Một văn phạm phi ngữ cảnh thuần túy không thể hiện được đầy đủ độ phức tạp của ngữ pháp các ngôn ngữ tự nhiên như tiếng Anh. Hai cơ chế có thể được bổ sung vào văn phạm này để tăng cường khả năng biểu đạt:

- Bổ sung thêm các đối số cho các ký hiệu không kết thúc.
- Đưa các ràng buộc tùy ý vào thân các quy tắc.

Các đối số bổ sung cho phép ta thực hiện nhiều tác vụ quan trọng, bao gồm việc xây dựng một cây phân tích cú pháp và biểu diễn một truy vấn gửi tới cơ sở dữ liệu. Việc sử dụng các đối số và điều kiện tùy ý đồng nghĩa với việc một văn phạm mệnh đề xác định (DCG) có thể biểu đạt mạnh hơn nhiều so với một văn phạm phi ngữ cảnh; DCG có thể biểu diễn bất kỳ điều gì có thể tính toán được bằng máy Turing.

## 15.7.3 Xây dựng giao diện ngôn ngữ tự nhiên cho cơ sở dữ liệu

Văn phạm ở phần trước có thể được mở rộng để cài đặt một giao diện ngôn ngữ tự nhiên đơn giản cho cơ sở dữ liệu. Thay vì chuyển các ngữ con thành các cây phân tích cú pháp, ta có thể chuyển chúng trực tiếp thành thực thể mà từ loại đó đề cập đến. Để làm điều này, ta đưa ra các giả định đơn giản hóa sau đây (tuy không phải lúc nào cũng đúng, nhưng tạo thành một phép xấp xỉ bước đầu hữu ích):

- Danh từ riêng (chẳng hạn "Chile") tương ứng với các cá thể.
- Danh từ chung (chẳng hạn "country") và tính từ (chẳng hạn "large") tương ứng với các thuộc tính.
- Động từ (chẳng hạn "borders") và giới từ (chẳng hạn "next to") tương ứng với một quan hệ hai ngôi giữa hai cá thể: Chủ ngữ và tân ngữ.

Trong trường hợp này, một ngữ danh từ đại diện cho một cá thể cùng một tập hợp các thuộc tính xác định cá thể đó. Để trả lời một câu hỏi, hệ thống có thể tìm kiếm một cá thể sở hữu các thuộc tính này. Một ngữ bổ nghĩa (chẳng hạn một ngữ giới từ hoặc mệnh đề quan hệ) mô tả một cá thể thông qua mối quan hệ với một cá thể khác.

::: example Ví dụ 15.35: Chuyển đổi câu hỏi thành truy vấn cơ sở dữ liệu
Trong câu *"What large country borders Chile?"*, cụm từ "large country" là chủ ngữ của động từ "borders" và "Chile" là tân ngữ. Giả sử cơ sở dữ liệu địa lý ở Mục 15.4 được sử dụng. Đối với cá thể $S$ đóng vai trò chủ ngữ, $large(S)$ và $country(S)$ là đúng. Tân ngữ là cá thể $chile$, và động từ chỉ định quan hệ $borders(S, chile)$. Do đó, câu hỏi *"What large country borders Chile?"* có thể được chuyển đổi thành câu truy vấn:

<span class="logic-expression logic-block">ask  large(S) ∧ country(S) ∧ borders(S, chile)</span>

trong đó $large$ là một vị từ có thể đúng đối với các quốc gia có diện tích lớn hơn hai triệu kilômét vuông.

Câu hỏi *"What is the name of the capital of a Spanish-speaking country that borders Argentina?"* có thể được dịch thành yêu cầu tìm giá trị của $S$ cho truy vấn:

```prolog
ask name(C, S) /\ capital(X, C) /\ language(X, spanish) /\ borders(X, argentina).
```
:::

Dưới đây là một văn phạm đơn giản vừa phân tích cú pháp câu hỏi tiếng Anh, vừa trực tiếp trả lời câu hỏi đó thông qua cơ sở dữ liệu:

```prolog
% Một ngữ danh từ là một từ hạn định, theo sau bởi các tính từ, danh từ và ngữ bổ nghĩa tùy chọn,
% tất cả đều nói về cùng một cá thể Ind
noun_phrase(L1, L4, Ind) :-
    adjectives(L1, L2, Ind),
    noun(L2, L3, Ind),
    omp(L3, L4, Ind).

% Các tính từ về cùng một cá thể
adjectives(L0, L2, Ind) :-
    adj(L0, L1, Ind),
    adjectives(L1, L2, Ind).
adjectives(L, L, Ind).

% Ngữ bổ nghĩa / mệnh đề quan hệ là một quan hệ (động từ hoặc giới từ) theo sau bởi một ngữ danh từ
mp(L0, L2, Subject) :-
    reln(L0, L1, Subject, Object),
    noun_phrase(L1, L2, Object).

% Ngữ bổ nghĩa tùy chọn
omp(L0, L1, Ind) :- mp(L0, L1, Ind).
omp(L, L, Ind).

% adj(L0, L1, Ind) đúng nếu L0 - L1 là một tính từ đúng với cá thể Ind
adj(["large" | L], L, Ind) :- large(Ind).
adj([LangName, "speaking" | L], L, Ind) :-
    name(Lang, LangName),
    language(Ind, Lang).
adj(["a" | L], L, Ind).

% noun(L0, L1, Ind) đúng nếu L0 - L1 là danh từ đúng với Ind
noun(["country" | L], L, Ind) :- country(Ind).
noun([N | L], L, E) :- name(E, N).

% reln(L0, L1, Sub, Obj) đúng nếu L0 - L1 là quan hệ giữa Sub và Obj
reln(["borders" | L], L, Sub, Obj) :- borders(Sub, Obj).
reln(["bordering" | L], L, Sub, Obj) :- borders(Sub, Obj).
reln(["the", "capital", "of" | L], L, Sub, Obj) :- capital(Obj, Sub).
reln(["the", "name", "of" | L], L, Sub, Obj) :- name(Obj, Sub).
```

*Hình 15.10: Văn phạm đơn giản trực tiếp trả lời câu hỏi.*

Văn phạm này bỏ qua phần lớn các quy tắc ngữ pháp chi tiết của tiếng Anh, chẳng hạn như sự khác biệt giữa giới từ và động từ, hay giữa từ hạn định và tính từ, và đưa ra một phỏng đoán về ý nghĩa ngay cả khi câu hỏi không hoàn toàn đúng ngữ pháp. Các tính từ, danh từ và ngữ danh từ cùng quy chiếu tới một cá thể. Đối số bổ sung trong các vị từ chính là cá thể thỏa mãn các tính từ và danh từ đó.

::: example Ví dụ 15.36: Trả lời trực tiếp câu hỏi bằng văn phạm DCG
Giả sử $question(Q, A)$ có nghĩa là $A$ là một câu trả lời cho câu hỏi $Q$, trong đó câu hỏi là một danh sách các từ. Các luật sau đây cho phép trả lời câu hỏi dựa trên các câu tuyển ở Hình 15.10 (bỏ qua dấu câu):

Quy tắc trả lời các câu hỏi như *"What is next to Chile?"*:

```prolog
question(["What", "is" | L0], Ind) :-
    mp(L0, [], Ind).
```

Ký hiệu `[]` chỉ ra rằng trong câu hỏi không còn từ nào đứng sau ngữ bổ nghĩa.

Quy tắc trả lời các câu hỏi như *"What is a large Spanish-speaking country next to Chile?"*:

```prolog
question(["What", "is" | L], Ind) :-
    noun_phrase(L, [], Ind).
```

Quy tắc trả lời các câu hỏi như *"What large country bordering Paraguay borders Chile?"*:

```prolog
question(["What" | L0], L2, Ind) :-
    noun_phrase(L0, L1, Ind),
    mp(L1, L2, Ind).
```
:::

Cách tiếp cận trả lời trực tiếp câu hỏi trong quá trình phân tích cú pháp có hai hạn chế đáng lưu ý:

- Rất khó phân biệt trường hợp chương trình không thể phân tích cú pháp câu hỏi với trường hợp không có câu trả lời nào thỏa mãn trong cơ sở dữ liệu; trong cả hai trường hợp hệ thống đều chỉ trả về "no".
- Khi câu hỏi có tính nhập nhằng (tức tồn tại nhiều cây phân tích cú pháp hợp lệ) và mỗi cách phân tích có thể mang lại các câu trả lời khác nhau, hệ thống sẽ đưa ra tất cả các câu trả lời của mọi cách phân tích mà không phân biệt rõ câu trả lời nào thuộc về cách phân tích nào.

Những đặc tính này khiến việc gỡ lỗi các chương trình viết theo phong cách này trở nên khó khăn.

Một giải pháp thay thế là: Thay vì truy vấn trực tiếp cơ sở tri thức trong quá trình phân tích cú pháp, hệ thống xây dựng một **dạng thức logic** (logical form) của ngôn ngữ tự nhiên — tức một mệnh đề logic truyền tải trọn vẹn ý nghĩa của phát ngôn — trước khi gửi mệnh đề đó đi truy vấn cơ sở tri thức. Dạng thức ngữ nghĩa này còn có thể được dùng cho các tác vụ khác, chẳng hạn như nạp thêm tri thức mới vào hệ thống, diễn giải lại câu bằng ngôn ngữ tự nhiên, hoặc dịch sang một ngôn ngữ khác.

Ta có thể xây dựng một truy vấn bằng cách cho phép các ngữ danh từ trả về một cá thể cùng một danh sách các ràng buộc mà ngữ danh từ đó áp đặt lên cá thể. Các quy tắc văn phạm phù hợp được chỉ ra ở Hình 15.11, được sử dụng kết hợp với từ điển ở Hình 15.12:

```prolog
% Một ngữ danh từ gồm từ hạn định, tính từ, danh từ và ngữ bổ nghĩa tùy chọn
noun_phrase(L0, L4, Ind, C0, C4) :-
    det(L0, L1, Ind, C0, C1),
    adjectives(L1, L2, Ind, C1, C2),
    noun(L2, L3, Ind, C2, C3),
    omp(L3, L4, Ind, C3, C4).

% Chuỗi tính từ
adjectives(L, L, Ind, C, C).
adjectives(L0, L2, Ind, C0, C2) :-
    adj(L0, L1, Ind, C0, C1),
    adjectives(L1, L2, Ind, C1, C2).

% Ngữ bổ nghĩa
mp(L0, L2, Sub, C0, C2) :-
    reln(L0, L1, Sub, Obj, C0, C1),
    noun_phrase(L1, L2, Obj, C1, C2).

% Ngữ bổ nghĩa tùy chọn
omp(L, L, Ind, C, C).
omp(L0, L1, Ind, C0, C1) :-
    mp(L0, L1, Ind, C0, C1).
```

*Hình 15.11: Một phần văn phạm xây dựng câu truy vấn.*

Biểu thức:

<span class="logic-expression logic-block">noun_phrase(L_0, L_1, Ind, C_0, C_1)</span>

có nghĩa là danh sách $L_{1}$ là phần kết thúc của danh sách $L_{0}$, và các từ trong $L_{0}$ đứng trước $L_{1}$ tạo thành một ngữ danh từ quy chiếu tới cá thể $Ind$. $C_{1}$ là phần đuôi của danh sách ràng buộc $C_{0}$, và các công thức trong $C_{0}$ đứng trước $C_{1}$ là các ràng buộc áp đặt lên cá thể $Ind$ bởi ngữ danh từ đó.

Về mặt thủ tục, $L_{0}$ là danh sách các từ cần phân tích, và $L_{1}$ là danh sách các từ còn lại sau ngữ danh từ. $C_{1}$ là danh sách các điều kiện đi vào ngữ danh từ, và $C_{0}$ là $C_{1}$ cộng thêm các điều kiện bổ sung do ngữ danh từ tạo ra.

```prolog
det(L, L, O, C, C).
det(["a" | T], T, O, C, C).
det(["the" | T], T, O, C, C).

noun(["country" | L], L, Ind, [country(Ind) | C], C).
noun(["city" | L], L, Ind, [city(Ind) | C], C).
noun([N | L], L, Ind, C, C) :- name(Ind, N).

adj(["large" | L], L, Ind, [large(Ind) | C], C).
adj([LangName, "speaking" | L], L, Ind,
    [language(Ind, Lang), name(Lang, LangName) | C], C).

reln(["borders" | L], L, Sub, Obj, [borders(Sub, Obj) | C], C).
reln(["bordering" | L], L, Sub, Obj, [borders(Sub, Obj) | C], C).
reln(["next", "to" | L], L, Sub, Obj, [borders(Sub, Obj) | C], C).
reln(["the", "capital", "of" | L], L, Sub, Obj, [capital(Obj, Sub) | C], C).
reln(["the", "name", "of" | L], L, Sub, Obj, [name(Obj, Sub) | C], C).
```

*Hình 15.12: Từ điển dùng để xây dựng câu truy vấn.*

::: example Ví dụ 15.37: Xây dựng dạng logic trung gian cho câu hỏi
Câu truy vấn:

```prolog
ask noun_phrase(["a", "Spanish", "speaking", "country", "bordering", "Argentina"],
               [], E1, C0, []).
```

trả về danh sách điều kiện:

```prolog
C0 = [language(E1, A), name(A, "Spanish"), country(E1), borders(E1, argentina)].
```

Tương tự, câu truy vấn:

```prolog
ask mp(["the", "name", "of", "the", "capital", "of", "a", "country", "bordering", "Argentina"],
       [], Ind, C0, []).
```

trả về:

```prolog
C0 = [name(A, Ind), capital(B, A), country(B), borders(B, argentina)].
```

Nếu các phần tử của danh sách $C_{0}$ được gửi đi truy vấn cơ sở dữ liệu có các quan hệ và hằng số tương ứng, hệ thống có thể trả về một quốc gia nói tiếng Tây Ban Nha giáp Argentina hoặc tên thủ đô của một quốc gia giáp Argentina. Trong Prolog, vị từ dựng sẵn `call` được dùng để truy vấn một nguyên tử.
:::

## 15.7.4 So sánh với các mô hình ngôn ngữ lớn

Các văn phạm dựa trên mệnh đề xác định cung cấp một cách tiếp cận khác biệt để trả lời các câu hỏi bằng ngôn ngữ tự nhiên so với các mô hình ngôn ngữ lớn (Large Language Models — LLMs). Sự khác biệt về mục tiêu đã được phân tích ở phần đầu.

Các mô hình ngôn ngữ lớn, chẳng hạn như dòng mô hình GPT, cũng có thể được dùng để trả lời các câu hỏi về địa lý Nam Mỹ. Những điểm khác biệt chủ yếu bao gồm:

- Các mô hình GPT đưa ra dự đoán xác suất về từ tiếp theo. Từ tiếp theo có thể được lấy mẫu ngẫu nhiên, và quá trình dự đoán này được lặp lại để tạo thành một câu trả lời bằng ngôn ngữ tự nhiên. Ngược lại, văn phạm ở phần trước trả lời câu hỏi bằng cách đưa ra câu trả lời mang tính biểu tượng, được thiết kế để phục vụ cho các bước suy luận logic tiếp theo.
- Văn phạm ở trên có thể được sử dụng để tìm kiếm tất cả các câu trả lời thỏa mãn và sau đó dừng lại khi không còn câu trả lời nào nữa (với giả định không gian tìm kiếm là hữu hạn và cơ sở tri thức đúng đắn), trong khi các mô hình GPT dự đoán câu trả lời kèm theo xác suất hoặc lấy mẫu từ phân phối các câu trả lời.
- Các mô hình GPT cung cấp câu trả lời mà không phân biệt rõ ràng giữa các cách phân tích cú pháp khác nhau, tương tự như văn phạm trả lời trực tiếp ở Hình 15.10. Ngược lại, văn phạm ở Hình 15.11 có thể tách bạch các cách phân tích cú pháp và cung cấp riêng câu trả lời cho từng cách phân tích, điều này rất hữu ích trong một số ứng dụng chuyên biệt.
- Các mô hình ngôn ngữ lớn hiện đại có thể sinh ra các câu truy vấn có cấu trúc trông rất tự nhiên, chẳng hạn bằng SQL hoặc Datalog. Tuy nhiên, để thực sự sử dụng câu truy vấn được sinh ra nhằm giao tiếp với cơ sở dữ liệu, mô hình ngôn ngữ cần được tiếp cận lược đồ cơ sở dữ liệu (schema) để biết được tên các vị từ, số lượng đối số và ý nghĩa của chúng, đồng thời cần truy cập vào chính cơ sở dữ liệu để khử nhập nhằng các hằng số (chẳng hạn như "Chile" có thể là tên một quốc gia, một đội bóng đá, hoặc một cách viết của quả ớt).
- Văn phạm mệnh đề xác định có thể thất bại nếu người dùng không sử dụng đúng ngữ pháp và vốn từ vựng được quy định trước, trong khi các mô hình GPT rất linh hoạt và dễ tha thứ trước cách dùng từ tự do của người dùng.
- Các mô hình GPT có độ bao phủ rộng hơn rất nhiều và có thể trò chuyện về các chủ đề tùy ý, trong khi các văn phạm mệnh đề xác định cần phải được thiết kế và tinh chỉnh thủ công cho từng miền ứng dụng cụ thể.

Tùy thuộc vào nhu cầu thực tế, vào việc hệ thống có sẵn sàng cho công sức kỹ nghệ hóa riêng cho từng miền hay không, và người dùng có thể được đào tạo để sử dụng văn phạm quy ước hay không, mỗi kỹ thuật trên sẽ có những thế mạnh và giá trị sử dụng riêng.

## Tài liệu tham khảo

- Poole, D. L., & Mackworth, A. K. (2023). *Artificial Intelligence: Foundations of Computational Agents* (3rd ed.). Cambridge University Press. Bản điện tử: [https://artint.info/3e/html/ArtInt3e.Ch15.S7.html](https://artint.info/3e/html/ArtInt3e.Ch15.S7.html).
- Chomsky, N. (1957). *Syntactic Structures*. Mouton & Co.
