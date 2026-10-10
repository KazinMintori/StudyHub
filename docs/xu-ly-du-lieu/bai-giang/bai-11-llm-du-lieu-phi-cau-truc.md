---
course: xu-ly-du-lieu
lecture: bai-11-llm-du-lieu-phi-cau-truc
section: lecture
title: "Trích xuất dữ liệu văn bản bằng LLM"
prerequisites: ["dictionary","ham-lap-trinh","gia-tri-thieu"]
lessonStatus: ready
description: "Kỷ luật trích xuất dữ liệu từ văn bản bằng mô hình ngôn ngữ lớn: Thiết kế schema Pydantic, kiểm chứng mỏ neo bằng chứng, đo lường trên bộ nhãn chuẩn và quy tắc hậu kiểm tự động."
---

Trong các tổ chức và doanh nghiệp hiện đại, phần lớn tri thức và giá trị kinh doanh không nằm sẵn trong các bảng cơ sở dữ liệu quan hệ ngăn nắp. Chúng ẩn chứa trong khối lượng khổng lồ các văn bản tự nhiên phi cấu trúc: Ý kiến phản hồi của khách hàng, ghi chú của nhân viên chăm sóc khách hàng, hợp đồng thỏa thuận, tin nhắn trao đổi hay các báo cáo hiện trường. Để đưa nguồn tài nguyên này vào các đường ống tính toán định lượng và xây dựng báo cáo điều hành, ta bắt buộc phải chuyển đổi chúng thành các trường dữ liệu có cấu trúc với định dạng chuẩn mực.

Các công cụ so khớp mẫu truyền thống như biểu thức chính quy (regular expressions) hoạt động cực kỳ nhanh chóng và mang tính tất định tuyệt đối. Tuy nhiên, chúng hoàn toàn bất lực trước những câu văn đa nghĩa, các cấu trúc đảo ngữ, cách diễn đạt mỉa mai châm biếm hay ngữ cảnh khẩu ngữ phong phú. Sự xuất hiện của các mô hình ngôn ngữ lớn (Large Language Models - LLM) mang lại năng lực thấu cảm ngữ nghĩa vượt trội. Đổi lại, bản chất xác suất ngẫu nhiên của mô hình đặt ra một thách thức kỹ nghệ nghiêm trọng: Làm thế nào để tích hợp một thành phần bất định, có khả năng bịa đặt thông tin (ảo giác - hallucination), vào một hệ thống xử lý dữ liệu đòi hỏi tính chính xác và độ tin cậy tuyệt đối?

Bài học này xây dựng kỷ luật kỹ nghệ và phương pháp luận đo lường khoa học khi ứng dụng LLM trong xử lý dữ liệu: Từ khâu lấy mẫu tái lập được và ước tính chi phí token, thiết kế chuẩn giao tiếp dữ liệu bằng Pydantic Schema có ràng buộc enum, đến quy trình đo lường sai số trên bộ dữ liệu nhãn chuẩn (Gold Standard) và thiết lập các bộ quy tắc hậu kiểm tự động để ngăn ngừa dữ liệu lỗi thẩm thấu vào kho dữ liệu.

---

## 1. Thiết kế chuẩn giao tiếp dữ liệu (Data Schema) với Pydantic

Khi tích hợp mô hình ngôn ngữ vào một đường ống dữ liệu tự động, sai lầm sơ đẳng nhất là đưa ra những câu lệnh chung chung như *"Hãy tóm tắt và đánh giá cảm xúc của nhận xét này"*. Mô hình sẽ trả về một đoạn văn tự do bay bổng, khiến cho các đoạn mã phân tích phía sau hoàn toàn bị đổ vỡ.

Kỹ sư dữ liệu chuyên nghiệp luôn tiếp cận bài toán bằng tư duy **Đặc tả cấu trúc trước (Schema-First)**. Ta sử dụng thư viện `pydantic` để định nghĩa một khuôn mẫu dữ liệu chặt chẽ với các ràng buộc bất di bất dịch:

1. **Kiểu dữ liệu tường minh**: Mọi trường dữ liệu phải được khai báo kiểu rõ ràng (`str`, `int`, `float`, `list[str]`).
2. **Không gian nhãn đóng (Closed Label Sets)**: Thay vì cho phép mô hình tự do sáng tác từ ngữ, ta khóa chặt các lựa chọn bằng kiểu `Literal` (tương đương với `Enum`). Chẳng hạn, cảm xúc chỉ được phép là một trong ba giá trị: `positive`, `mixed`, hoặc `negative`. Mọi từ ngữ lạ lùng khác như `"happy"`, `"neutral"`, `"tuyet_voi"` đều bị chặn đứng ngay lập tức ở tầng kiểm định cấu trúc.
3. **Mỏ neo bằng chứng (Evidence Anchors)**: Buộc mô hình phải trích xuất nguyên văn đoạn câu làm căn cứ đưa ra nhận định.

```python
from typing import Literal
from pydantic import BaseModel, Field, ValidationError

# Định nghĩa tập các khía cạnh dịch vụ cho phép (không gian nhãn đóng)
Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]

class ReviewInfo(BaseModel):
    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str

# Thử nghiệm kiểm định một phản hồi JSON từ LLM
du_lieu_hop_le = {
    "sentiment": "mixed",
    "aspects_positive": ["location"],
    "aspects_negative": ["noise"],
    "language": "en"
}
ban_ghi = ReviewInfo(**du_lieu_hop_le)
print("Dữ liệu hợp lệ:", ban_ghi.model_dump())

# Thử nghiệm với dữ liệu chứa nhãn bịa đặt
du_lieu_sai = {
    "sentiment": "happy",  # 'happy' không nằm trong Literal quy định
    "aspects_positive": ["photos"],  # 'photos' là khía cạnh tự bịa
    "aspects_negative": [],
    "language": "en"
}
try:
    ReviewInfo(**du_lieu_sai)
except ValidationError as e:
    print("\nPydantic đã chặn đứng dữ liệu sai cấu trúc:")
    for err in e.errors():
        print(f" - Trường vi phạm: {err['loc'][0]} | Lỗi: {err['type']}")
```

Khi sử dụng các giao diện lập trình ứng dụng (API) của các mô hình hiện đại như Google Gemini (`gemini-2.5-flash-lite`, `gemini-1.5-pro`), ta có thể truyền trực tiếp `ReviewInfo.model_json_schema()` vào tham số `response_schema`. Khi đó, bộ giải mã của mô hình sẽ ép buộc sinh token tuân thủ 100% ngữ pháp JSON và lược đồ đã định nghĩa.

---

## 2. Kiểm định hai tầng: Cấu trúc cú pháp và Mỏ neo sự thật (Grounding)

Cần khắc sâu một nguyên lý cốt tử: **Đúng cú pháp chưa bao giờ đồng nghĩa với đúng sự thật**.
Một mô hình ngôn ngữ hoàn toàn có thể trả về một chuỗi JSON hợp lệ 100% theo chuẩn Pydantic, gán nhãn căn hộ là "cực kỳ sạch sẽ", nhưng trong văn bản gốc của khách hàng lại viết "phòng đầy gián và bụi bặm". 

Do đó, một đường ống xử lý dữ liệu nghiêm cẩn phải xây dựng cơ chế kiểm định hai tầng:

<DataDiagram name="llm-validation" />

- **Tầng 1 (Cấu trúc & Định dạng)**: Xác thực xem đối tượng trả về có thỏa mãn toàn bộ các trường bắt buộc, kiểu dữ liệu và giá trị enum hay không.
- **Tầng 2 (Mỏ neo sự thật - Citation Verification)**: Kiểm tra xem đoạn văn bản trích dẫn (`evidence`) do mô hình đưa ra có thực sự xuất hiện nguyên văn từng ký tự trong văn bản gốc hay không (`assert evidence in raw_text`). Nếu mô hình trích dẫn một câu không hề có trong nguồn, bản ghi lập tức bị gắn cờ cảnh báo ảo giác và chuyển sang hàng đợi kiểm duyệt thủ công.

---

## 3. Đo lường chất lượng bằng Bộ dữ liệu vàng (Gold Standard)

Đừng bao giờ đánh giá năng lực của một mô hình ngôn ngữ bằng cảm tính hay dựa trên vài ba ví dụ tự chạy thử trên giao diện web. Trong khoa học dữ liệu, chuẩn mực duy nhất để khẳng định độ tin cậy của một hệ thống trích xuất là **đo lường thống kê trên bộ dữ liệu nhãn chuẩn (Gold Standard)**.

Bộ dữ liệu vàng là một tập hợp đại diện (thường từ 100 đến 500 mẫu) được các chuyên gia con người gán nhãn thủ công độc lập theo một hướng dẫn chuẩn mực (Annotation Guidelines), sau đó đối thoại để giải quyết toàn bộ các trường hợp bất đồng ý kiến.

### Các chỉ số đánh giá từ Ma trận nhầm lẫn (Confusion Matrix)

Khi đối chiếu nhãn dự đoán của mô hình với nhãn chuẩn của con người đối với một lớp mục tiêu, ta có bốn trạng thái:
1. **Dương tính thật (True Positive - TP)**: Con người gán Nhãn A và mô hình dự đoán đúng là Nhãn A.
2. **Dương tính giả (False Positive - FP)**: Con người không gán Nhãn A, nhưng mô hình lại đoán nhầm thành Nhãn A (báo động nhầm).
3. **Âm tính giả (False Negative - FN)**: Con người gán Nhãn A, nhưng mô hình lại bỏ sót và đoán sang nhãn khác (bỏ sót).
4. **Âm tính thật (True Negative - TN)**: Cả con người và mô hình đều đồng thuận rằng không phải Nhãn A.

Các công thức đo lường cốt lõi:
$$
\text{Độ chính xác tổng thể (Accuracy)} = \frac{\text{Số mẫu dự đoán đúng}}{\text{Tổng số mẫu thử nghiệm}}
$$
$$
\text{Độ chuẩn xác (Precision)} = \frac{TP}{TP + FP}
$$
$$
\text{Độ bao phủ hay Độ nhạy (Recall)} = \frac{TP}{TP + FN}
$$
$$
\text{Điểm F1 điều hòa} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
$$

```python
# Minh họa tính toán các chỉ số đánh giá trên tập nhãn chuẩn
gold_labels = ["positive", "negative", "mixed", "positive", "negative"]
pred_labels = ["positive", "positive", "mixed", "positive", "mixed"]

# 1. Độ chính xác tổng thể (Accuracy)
so_dung = sum(g == p for g, p in zip(gold_labels, pred_labels))
acc = so_dung / len(gold_labels)
print(f"Accuracy: {acc:.1%}") # 3/5 = 60.0%

# 2. Xét riêng nhãn 'positive'
tp = sum(g == "positive" and p == "positive" for g, p in zip(gold_labels, pred_labels))
fp = sum(g != "positive" and p == "positive" for g, p in zip(gold_labels, pred_labels))
fn = sum(g == "positive" and p != "positive" for g, p in zip(gold_labels, pred_labels))

prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
f1 = 2 * (prec * rec) / (prec + rec) if (prec + rec) > 0 else 0.0

print(f"Nhãn positive -> Precision: {prec:.2f} | Recall: {rec:.2f} | F1: {f1:.2f}")
```

### Phân loại các dạng lỗi ngữ nghĩa phổ biến của LLM
Khi mổ xẻ các trường hợp mô hình đoán sai trên tập nhãn chuẩn, kỹ sư dữ liệu thường ghi nhận ba nhóm lỗi chính:
1. **Bỏ sót ý phụ (Subtle Negative Overlook)**: Khách hàng viết một đoạn văn rất dài khen ngợi vị trí và chủ nhà, nhưng ở cuối câu có một lời phàn nàn nhỏ: *"Tuy nhiên ban đêm đường phố hơi ồn ào"*. Mô hình thường bị ấn tượng mạnh bởi các từ khen ngợi áp đảo và nhắm mắt gán nhãn `positive`, bỏ sót sắc thái `mixed`.
2. **Hiểu sai ngữ cảnh phủ định (Negation Misinterpretation)**: Khách hàng nhận xét *"overall not a bad place"* (nhìn chung đây không phải là một chỗ ở tồi - mang hàm ý khen nhẹ). Mô hình nhận diện thấy từ *"bad"* và vội vã phân loại thành `negative`.
3. **Các trường hợp ranh giới khó phân định (Edge Cases)**: Những câu nhận xét mang tính nước đôi hoặc dùng tiếng lóng địa phương khiến ngay cả hai người gán nhãn cũng có thể bất đồng ý kiến.

---

## 4. Hậu kiểm tự động (Automated Post-Validation)

Trong thực tế vận hành sản xuất, ta không thể gán nhãn tay cho hàng trăm nghìn văn bản mới đổ về mỗi ngày. Để bắt các lỗi ngữ nghĩa của mô hình trên quy mô lớn, ta áp dụng tầng phòng ngự tiếp theo: **Hậu kiểm quy tắc nghiệp vụ (Automated Post-Validation)**.

Nguyên tắc của hậu kiểm là tìm ra những **mâu thuẫn nội tại** giữa các trường dữ liệu mà mô hình vừa sinh ra:
- Nếu mô hình kết luận `sentiment == "positive"`, thì danh sách các khía cạnh tiêu cực (`aspects_negative`) bắt buộc phải là một danh sách rỗng `[]`. Việc một căn hộ được khen toàn diện nhưng lại chứa khía cạnh tiêu cực là một mâu thuẫn logic rõ ràng.
- Ngược lại, nếu kết luận `sentiment == "negative"`, thì danh sách các khía cạnh tích cực (`aspects_positive`) cũng không được phép chứa phần tử nào.

Các quy tắc hậu kiểm này không đòi hỏi nhãn tay của con người và có thể chạy tự động với tốc độ hàng triệu bản ghi mỗi giây, giúp lọc ngay các bản ghi méo mó trước khi nạp vào kho dữ liệu.

---

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 11) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết và Đọc thêm

| Thành phần kỹ nghệ | Công cụ thực hiện | Ý nghĩa phương pháp luận |
| :--- | :--- | :--- |
| **Khuôn mẫu dữ liệu** | `pydantic.BaseModel`, `Literal` | Chặn đứng dữ liệu rác và nhãn lạ ngay tại cổng vào của hệ thống; không gian nhãn đóng. |
| **Mỏ neo sự thật** | Citation Verification (`assert c in src`) | Ngăn chặn hiện tượng bịa đặt trích dẫn; kiểm chứng tính xác thực của lý do. |
| **Đo lường nhãn chuẩn** | Gold Standard, Confusion Matrix | Chuẩn mực đánh giá định lượng; phân biệt rạch ròi giữa độ chính xác cấu trúc và độ chính xác ngữ nghĩa. |
| **Hậu kiểm tự động** | Rule-based Validation | Bộ lọc logic nhanh chóng trên quy mô lớn, phát hiện sự tự mâu thuẫn nội tại trong đầu ra của mô hình. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 6: Data Loading, Storage, and File Formats](https://wesmckinney.com/book/accessing-data).
- Tài liệu kỹ thuật: [Google Gemini API: Structured Outputs with JSON Schemas](https://ai.google.dev/gemini-api/docs/structured-output).
- Thư viện Pydantic: [Pydantic Official Documentation (v2)](https://docs.pydantic.dev/).
- Tom Fawcett, *An Introduction to ROC Analysis*, Pattern Recognition Letters, 2006.
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
