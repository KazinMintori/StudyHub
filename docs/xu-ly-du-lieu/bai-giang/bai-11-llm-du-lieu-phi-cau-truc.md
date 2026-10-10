---
course: xu-ly-du-lieu
lecture: bai-11-llm-du-lieu-phi-cau-truc
section: lecture
title: "Trích xuất dữ liệu văn bản bằng LLM"
prerequisites: ["dictionary","ham-lap-trinh","gia-tri-thieu"]
lessonStatus: ready
description: "Kỷ luật trích xuất dữ liệu từ văn bản bằng mô hình ngôn ngữ lớn: thiết kế schema Pydantic, kiểm chứng mỏ neo bằng chứng, đo lường trên bộ nhãn chuẩn và quy tắc hậu kiểm tự động."
---

Trong các tổ chức và doanh nghiệp hiện đại, phần lớn tri thức và giá trị kinh doanh không nằm sẵn trong các bảng cơ sở dữ liệu quan hệ ngăn nắp. Chúng ẩn chứa trong khối lượng khổng lồ các văn bản tự nhiên phi cấu trúc: ý kiến phản hồi của khách hàng, ghi chú của nhân viên chăm sóc khách hàng, hợp đồng thỏa thuận, tin nhắn trao đổi hay các báo cáo hiện trường. Để đưa nguồn tài nguyên này vào các đường ống tính toán định lượng và xây dựng báo cáo điều hành, ta bắt buộc phải chuyển đổi chúng thành các trường dữ liệu có cấu trúc với định dạng chuẩn mực.

Các công cụ so khớp mẫu truyền thống như biểu thức chính quy (regular expressions) hoạt động cực kỳ nhanh chóng và mang tính tất định tuyệt đối. Tuy nhiên, chúng hoàn toàn bất lực trước những câu văn đa nghĩa, các cấu trúc đảo ngữ, cách diễn đạt mỉa mai châm biếm hay ngữ cảnh khẩu ngữ phong phú. Sự xuất hiện của các mô hình ngôn ngữ lớn (Large Language Models - LLM) mang lại năng lực thấu cảm ngữ nghĩa vượt trội. Đổi lại, bản chất xác suất ngẫu nhiên của mô hình đặt ra một thách thức kỹ nghệ nghiêm trọng: làm thế nào để tích hợp một thành phần bất định, có khả năng bịa đặt thông tin (ảo giác - hallucination), vào một hệ thống xử lý dữ liệu đòi hỏi tính chính xác và độ tin cậy tuyệt đối?

Bài học này xây dựng kỷ luật kỹ nghệ và phương pháp luận đo lường khoa học khi ứng dụng LLM trong xử lý dữ liệu: từ khâu lấy mẫu tái lập được và ước tính chi phí token, thiết kế chuẩn giao tiếp dữ liệu bằng Pydantic Schema có ràng buộc enum, đến quy trình đo lường sai số trên bộ dữ liệu nhãn chuẩn (Gold Standard) và thiết lập các bộ quy tắc hậu kiểm tự động để ngăn ngừa dữ liệu lỗi thẩm thấu vào kho dữ liệu.

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
1. **Bỏ sót ý phụ (Subtle Negative Overlook)**: Khách hàng viết một đoạn văn rất dài khen ngợi vị trí và chủ nhà, nhưng ở cuối câu có một lời phàn nàn nhỏ: *"tuy nhiên ban đêm đường phố hơi ồn ào"*. Mô hình thường bị ấn tượng mạnh bởi các từ khen ngợi áp đảo và nhắm mắt gán nhãn `positive`, bỏ sót sắc thái `mixed`.
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

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 11)

Hệ thống bài tập dưới đây xây dựng toàn bộ quy trình kiểm soát chất lượng đầu ra của mô hình ngôn ngữ lớn trên bài toán phân tích nhận xét của khách du lịch tại Santiago. Bộ bài tập bao gồm từ việc chọn mẫu dữ liệu đại diện, ước lượng chi phí token, thiết kế schema Pydantic, kiểm tra lỗi hàng loạt, tính toán độ chính xác trên nhãn chuẩn, đến việc cài đặt bộ quy tắc hậu kiểm tự động phát hiện mâu thuẫn logic.

### Dữ liệu thực hành mẫu và Bộ nhãn chuẩn (Gold Standard)

```python
import json
import numpy as np
import pandas as pd

# Tập 10 nhận xét thực tế tiêu biểu
REVIEWS = {
    1: "Place is great for a family, all clean, good location, bit noisy as the main avenue is behind, but we had a great time.",
    2: "Apartment was irrelevant with pictures and not clean too so we cancelled our reservation. Alvaro helped us about cancellation process.",
    3: "Cristian fue muy amable en todo momento, el lugar como se describia. La zona con muy buena movilidad. Muy recomendable. Gracias Cristian",
    4: "Hermoso alojamiento! Lo pasamos re bien mi hija y yo. Es un poco ruidosa la zona si se abre la ventana. La vista es bella y esta muy bien ubicado. Sin duda volveriamos",
    5: "Great location but apartment needs some attention to detail. Cable TV and wifi was out of service. Communication with host was poor. Bedding was not optimal.",
    6: "Good WiFi, great location and centrally located. Shower was hot and had good pressure and there was enough space for two people for 6 days.",
    7: "Es tal cual las fotos, buena ubicacion, tranquilo y sin ruido. Es en un piso 15 por si le temen a las alturas.",
    8: ".",
    9: "Nice place in cool region. Very noisy environment and apartment is not very clean.",
    10: "location was great, wifi was spotty. But overall not a bad place.",
}

# Bộ nhãn chuẩn (GOLD) do chuyên gia con người thẩm định
# Quy ước: nhận xét vô nghĩa hoặc quá ngắn -> mixed, không khía cạnh, ngôn ngữ "und" (undetermined)
GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}

# 10 chuỗi JSON thô do LLM sinh ra (đã được cài cắm lỗi thực tế có chủ đích)
LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}', # Lỗi enum 'photos'
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}', # Thiếu trường 'language'
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}
```

---

### Bài 1: Chọn mẫu dữ liệu tái lập được

::: exercise Yêu cầu nghiệp vụ
Khi tập dữ liệu thực tế có hàng trăm nghìn dòng, việc gửi toàn bộ dữ liệu lên mô hình là cực kỳ lãng phí và vượt ngưỡng hạn mức gọi API. Ta cần chọn ra một mẫu dữ liệu đại diện có độ dài đủ lớn để phục vụ phân tích.
Hãy viết hàm `choose_sample(rv: pd.DataFrame, do_dai_min: int = 50, n: int = 100, seed: int = 42) -> pd.DataFrame` nhận vào bảng `rv` có cột `comments`.

Hàm thực hiện:
- Lọc các dòng có độ dài chuỗi bình luận `>= do_dai_min`.
- Lấy mẫu ngẫu nhiên đúng `n` dòng từ bảng đã lọc bằng phương thức `.sample(n, random_state=seed)`.
- Trả về DataFrame mẫu gồm đầy đủ các cột, giữ nguyên chỉ mục gốc. Tuyệt đối không làm thay đổi bảng dữ liệu đầu vào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def choose_sample_co_ban(rv: pd.DataFrame, do_dai_min: int = 50, n: int = 100, seed: int = 42) -> pd.DataFrame:
    # 1. Tính độ dài từng chuỗi bình luận và lọc
    do_dai = rv["comments"].str.len()
    hop_le = rv.loc[do_dai >= do_dai_min]
    
    # 2. Lấy mẫu ngẫu nhiên có cố định hạt giống số học
    mau = hop_le.sample(n=n, random_state=seed)
    return mau
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Biểu thức nối hàm tinh gọn)

```python
def choose_sample(rv: pd.DataFrame, do_dai_min: int = 50, n: int = 100, seed: int = 42) -> pd.DataFrame:
    return (
        rv.loc[rv["comments"].str.len().ge(do_dai_min)]
        .sample(n=n, random_state=seed)
    )
```

#### Phân tích so sánh & Trực giác bản chất
- **Ý nghĩa của `random_state=seed`**: Việc cố định hạt giống sinh số ngẫu nhiên là yêu cầu sống còn của tính tái lập khoa học (Reproducibility). Bất kỳ đồng nghiệp nào khi chạy lại đoạn mã này trên cùng một tệp dữ liệu cũng sẽ thu được đúng 100 dòng quan sát giống hệt nhau, bảo đảm kết quả đo lường không bị sai lệch do sự may rủi khi lấy mẫu.
:::

---

### Bài 2: Ước lượng số lượng Token và Chi phí trước khi gọi API

::: exercise Yêu cầu nghiệp vụ
Theo quy tắc ngón tay cái tiêu chuẩn trong xử lý ngôn ngữ tự nhiên: trung bình khoảng 4 ký tự văn bản tương đương với 1 token.
Với đơn giá của mô hình `gemini-2.5-flash-lite` là $0.25$ USD cho mỗi 1 triệu token đầu vào, hãy viết hàm `estimate_cost(comments: pd.Series, gia_moi_trieu: float = 0.25) -> dict`.

Hàm nhận vào Series các chuỗi bình luận và đơn giá, trả về từ điển gồm hai khóa:
- `"tong_token"`: Số nguyên là **tổng của `len(binh_luan) // 4`** được tính trên từng dòng riêng lẻ rồi mới cộng dồn (thao tác chia nguyên trên từng dòng trước khi cộng).
- `"chi_phi"`: Số thực `float` biểu thị chi phí ước tính tính bằng USD theo công thức:
  $$
  \text{chi\_phi} = \frac{\text{tong\_token} \times \text{gia\_moi\_trieu}}{1\,000\,000}
  $$
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Duyệt vòng lặp danh sách)

```python
def estimate_cost_co_ban(comments: pd.Series, gia_moi_trieu: float = 0.25) -> dict:
    tong = 0
    for text in comments:
        tong += len(str(text)) // 4
        
    chi_phi = float(tong * gia_moi_trieu / 1_000_000)
    return {
        "tong_token": tong,
        "chi_phi": chi_phi
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Vector hóa bằng phép toán Series)

```python
def estimate_cost(comments: pd.Series, gia_moi_trieu: float = 0.25) -> dict:
    # Vector hóa phép chia nguyên trên toàn bộ cột chuỗi
    tong_token = int((comments.str.len() // 4).sum())
    chi_phi = float(tong_token * gia_moi_trieu / 1_000_000)
    return {
        "tong_token": tong_token,
        "chi_phi": chi_phi
    }
```

#### Phân tích so sánh & Trực giác bản chất
- Chú ý chi tiết kỹ thuật: `sum(len // 4)` hoàn toàn khác với `sum(len) // 4` do phần dư bị cắt bỏ ở từng câu ngắn. Việc chia nguyên từng câu phản ánh đúng cơ chế làm tròn tối thiểu khi chia khối token trong các bộ tokenizer thực tế.
:::

---

### Bài 3: Khai báo Schema Pydantic có ràng buộc Literal

::: exercise Yêu cầu nghiệp vụ
Hãy định nghĩa kiểu dữ liệu `Aspect` và lớp mô hình `ReviewInfo` kế thừa từ `pydantic.BaseModel` thỏa mãn các ràng buộc nghiêm ngặt:
- `Aspect`: Là một `Literal` gồm đúng 6 giá trị: `"location"`, `"cleanliness"`, `"host"`, `"noise"`, `"amenities"`, `"value"`.
- `ReviewInfo` gồm đúng 4 trường, **không có giá trị mặc định**:
  - `sentiment`: Kiểu `Literal["positive", "mixed", "negative"]`.
  - `aspects_positive`: Kiểu `list[Aspect]`.
  - `aspects_negative`: Kiểu `list[Aspect]`.
  - `language`: Kiểu `str`.

Mọi trường hợp nhãn nằm ngoài danh mục, thiếu trường bắt buộc, hoặc sai kiểu dữ liệu đều phải kích hoạt ngoại lệ `pydantic.ValidationError`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
from typing import Literal
from pydantic import BaseModel, ValidationError

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]

class ReviewInfo(BaseModel):
    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str
```

#### Phân tích sư phạm chuyên sâu
- Bằng cách không cung cấp giá trị mặc định (`default`), Pydantic sẽ bắt buộc toàn bộ 4 trường này phải hiện diện trong JSON trả về từ LLM. Nếu mô hình lười biếng bỏ quên trường `language`, hệ thống sẽ ném lỗi ngay thay vì âm thầm điền giá trị ngầm định.
:::

---

### Bài 4: Kiểm tra tính hợp lệ hàng loạt và phân tích lỗi Schema

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `validate_outputs(llm_out: dict) -> dict` nhận vào từ điển `llm_out` chứa `{id: chuỗi_JSON_thô}`.
Với từng phần tử theo đúng thứ tự của từ điển:
- Gọi hàm `ReviewInfo.model_validate_json(raw_json)`.
- Nếu hợp lệ: lưu đối tượng mô hình vào từ điển `hop_le[id]`.
- Nếu phát sinh ngoại lệ `pydantic.ValidationError` (do nhãn ngoài danh mục, thiếu trường, hoặc chuỗi JSON bị gãy cú pháp): đưa mã `id` đó vào danh sách `loi_schema`.

Hàm trả về từ điển gồm đúng hai khóa: `"hop_le"` và `"loi_schema"`. Giữ nguyên kiểu dữ liệu của mã `id`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def validate_outputs_co_ban(llm_out: dict) -> dict:
    hop_le = {}
    loi_schema = []
    
    for rid, raw_text in llm_out.items():
        try:
            mo_hinh = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = mo_hinh
        except (ValidationError, Exception):
            loi_schema.append(rid)
            
    return {
        "hop_le": hop_le,
        "loi_schema": loi_schema
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Bắt lỗi chính xác theo chuẩn kỹ nghệ)

```python
def validate_outputs(llm_out: dict) -> dict:
    hop_le = {}
    loi_schema = []
    
    for rid, raw_json in llm_out.items():
        try:
            # Khởi tạo và kiểm định trực tiếp từ chuỗi JSON
            hop_le[rid] = ReviewInfo.model_validate_json(raw_json)
        except ValidationError:
            # Chỉ bắt đúng ValidationError để không che giấu các lỗi hệ thống khác
            loi_schema.append(rid)
            
    return {
        "hop_le": hop_le,
        "loi_schema": loi_schema
    }
```

#### Phân tích sư phạm chuyên sâu: Schema đã chặn được những gì?
Áp dụng trên 10 đầu ra của `LLM_OUT`, kết quả phát hiện `loi_schema == [2, 5]`:
- **Tại ID 2**: Mô hình trả về `aspects_negative: ["photos", "cleanliness"]`. Giá trị `"photos"` không nằm trong danh mục 6 khía cạnh cho phép của `Aspect`. Pydantic lập tức từ chối và chặn đứng việc đưa nhãn lạ vào bảng phân tích.
- **Tại ID 5**: Mô hình trả về JSON hoàn toàn thiếu vắng trường `"language"`. Pydantic phát hiện thiếu trường bắt buộc và từ chối bản ghi.
- **Trong đường ống thực tế, ta nên xử lý các bản ghi này thế nào?**
  Không được vứt bỏ dữ liệu. Các bản ghi này được đẩy vào **Hàng đợi kiểm duyệt lại (Dead Letter Queue - DLQ)**. Hệ thống có thể tự động gọi lại mô hình lần thứ hai kèm lời nhắc sửa lỗi (Self-Correction Prompt): *"Đầu ra trước của bạn bị thiếu trường language, hãy trả lại đầy đủ"*. Nếu sau 3 lần gọi lại vẫn thất bại, bản ghi sẽ được chuyển cho chuyên viên thẩm định.
:::

---

### Bài 5: Đo lường độ chính xác nhãn cảm xúc trên Bộ dữ liệu vàng

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `sentiment_accuracy(du_doan: dict, gold: dict) -> dict` nhận vào:
- `du_doan`: Từ điển `{id: nhan_cam_xuc_LLM}` chỉ gồm các bản ghi đã vượt qua tầng kiểm định schema.
- `gold`: Từ điển nhãn chuẩn của chuyên gia `{id: {"sentiment": ...}}`.

Hàm trả về từ điển gồm ba khóa:
- `"so_dung"`: Số nguyên là số lượng ID có nhãn dự đoán trùng khớp hoàn toàn với `gold[id]["sentiment"]`.
- `"acc"`: Số thực `float` là tỷ lệ chính xác: `so_dung / len(du_doan)`.
- `"sai"`: Danh sách các mã ID dự đoán sai, bảo toàn đúng thứ tự xuất hiện ban đầu trong `du_doan`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def sentiment_accuracy_co_ban(du_doan: dict, gold: dict) -> dict:
    so_dung = 0
    danh_sach_sai = []
    
    for rid, pred in du_doan.items():
        that = gold[rid]["sentiment"]
        if pred == that:
            so_dung += 1
        else:
            danh_sach_sai.append(rid)
            
    acc = so_dung / len(du_doan) if len(du_doan) > 0 else 0.0
    return {
        "so_dung": so_dung,
        "acc": acc,
        "sai": danh_sach_sai
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def sentiment_accuracy(du_doan: dict, gold: dict) -> dict:
    sai = [rid for rid, p in du_doan.items() if p != gold[rid]["sentiment"]]
    so_dung = len(du_doan) - len(sai)
    return {
        "so_dung": so_dung,
        "acc": float(so_dung / len(du_doan)),
        "sai": sai
    }
```

#### Phân tích sư phạm chuyên sâu: Bàn luận về Mẫu số đo lường
- **Chỉ số 62.5% được tính trên mẫu số nào?**
  Chỉ số $\text{Accuracy} = 5 / 8 = 62.5\%$ được tính trên **8 bản ghi vượt qua kiểm định schema**.
- **Nếu tính trên toàn bộ 10 bản ghi thì sao?**
  Nếu ta coi 2 bản ghi bị lỗi schema (ID 2 và 5) là các ca thất bại hoàn toàn của mô hình, thì độ chính xác trên toàn bộ dữ liệu ban đầu là $\text{End-to-End Accuracy} = 5 / 10 = 50.0\%$.
- **Khuyến nghị báo cáo khoa học**:
  Báo cáo chuyên nghiệp luôn phải trình bày tách bạch cả hai con số:
  1. *Tỷ lệ tuân thủ lược đồ (Schema Compliance Rate)*: $8/10 = 80\%$.
  2. *Độ chính xác ngữ nghĩa trên tập hợp lệ (Conditional Semantic Accuracy)*: $5/8 = 62.5\%$.
  3. *Hiệu suất tổng thể từ đầu đến cuối (Pipeline End-to-End Accuracy)*: $5/10 = 50.0\%$.
:::

---

### Bài 6: Xây dựng Bộ quy tắc Hậu kiểm tự động (Phát hiện tự mâu thuẫn)

::: exercise Yêu cầu nghiệp vụ
Một đầu ra bị coi là **tự mâu thuẫn về mặt logic** nếu:
- Nhãn tổng thể là `"positive"` nhưng danh sách khía cạnh tiêu cực `aspects_negative` lại có phần tử (không rỗng).
- Hoặc nhãn tổng thể là `"negative"` nhưng danh sách khía cạnh tích cực `aspects_positive` lại có phần tử (không rỗng).
Nhãn `"mixed"` được phép chứa cả hai chiều ý kiến nên không bao giờ vi phạm quy tắc này.

Hãy viết hàm `contradictions(outputs: dict) -> list` nhận vào từ điển `outputs` chứa `{id: du_lieu_dict}` (dữ liệu đã bung từ `model_dump()`).
Hàm trả về danh sách các mã `id` vi phạm quy tắc trên theo đúng thứ tự xuất hiện trong từ điển. Hàm hoàn toàn không cần nhãn tay và không làm biến đổi dữ liệu đầu vào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def contradictions_co_ban(outputs: dict) -> list:
    vi_pham = []
    for rid, item in outputs.items():
        s = item["sentiment"]
        pos = item.get("aspects_positive", [])
        neg = item.get("aspects_negative", [])
        
        if s == "positive" and len(neg) > 0:
            vi_pham.append(rid)
        elif s == "negative" and len(pos) > 0:
            vi_pham.append(rid)
            
    return vi_pham
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Biểu thức lọc điều kiện logic tinh gọn)

```python
def contradictions(outputs: dict) -> list:
    return [
        rid for rid, d in outputs.items()
        if (d["sentiment"] == "positive" and bool(d.get("aspects_negative")))
        or (d["sentiment"] == "negative" and bool(d.get("aspects_positive")))
    ]
```

#### Phân tích sư phạm chuyên sâu: Mối quan hệ giữa Nhãn tay và Hậu kiểm
- **Quy tắc hậu kiểm bắt được những ca sai nào và bỏ sót ca nào?**
  - Hậu kiểm đã tóm được chính xác **ID 9** và **ID 10**: Mô hình gán nhãn tổng thể là `negative` nhưng bên trong lại liệt kê `aspects_positive: ["location"]`. Đây là sự tự mâu thuẫn lộ liễu.
  - Tuy nhiên, hậu kiểm hoàn toàn **bỏ sót ID 4**: Mô hình gán `positive`, các khía cạnh tích cực có `"location"` và khía cạnh tiêu cực rỗng `[]`. Về mặt hình thức logic, bản ghi này hoàn hảo 100%. Nhưng đối chiếu với văn bản gốc, khách hàng có phàn nàn tiếng ồn khi mở cửa sổ. Mô hình đã tự ý bỏ qua ý chê này.
- **Bài học cốt lõi**:
  Hậu kiểm tự động là một bộ lọc rẻ tiền và nhanh chóng để quét sạch các lỗi ngớ ngẩn trên quy mô lớn, nhưng **không bao giờ có thể thay thế hoàn toàn bộ nhãn chuẩn của con người**. Một hệ thống xử lý dữ liệu AI đáng tin cậy bắt buộc phải kết hợp cả hai: dùng nhãn tay để đo lường năng lực cốt lõi định kỳ, và dùng hậu kiểm để canh gác dòng chảy dữ liệu hàng ngày.
:::

---

### Bài tự làm mở rộng: Triển khai pipeline gọi API thực tế với cơ chế gọi lại và lưu đệm

::: exercise Đề bài mở rộng
Hãy thiết kế một quy trình hoàn chỉnh để gọi mô hình Gemini thực tế trên một nhận xét mẫu:
1. Thiết lập cơ chế Structured Output với Pydantic Schema.
2. Cài đặt cơ chế gọi lại khi gặp lỗi (Exponential Backoff / Retry) phòng trường hợp nghẽn mạng hoặc quá tải hạn mức (Rate Limit).
3. Đóng gói kết quả với đầy đủ dấu vết kiểm toán: văn bản gốc, phản hồi thô, đối tượng đã kiểm định, và thời gian thực thi.
:::

::: solution
#### Mã nguồn thiết kế Pipeline hoàn chỉnh

```python
import time
import json
from typing import Literal
from pydantic import BaseModel, Field

# 1. Định nghĩa Schema
class PhanTichDanhGia(BaseModel):
    sentiment: Literal["positive", "mixed", "negative"] = Field(description="Cảm xúc tổng thể")
    diem_hai_long: int = Field(ge=1, le=5, description="Thang điểm từ 1 đến 5")
    trich_dan_chung_minh: str = Field(description="Đoạn văn trích nguyên văn làm bằng chứng")

# 2. Hàm giả lập bộ điều phối gọi LLM có xử lý lỗi và kiểm chứng trích dẫn
def pipeline_trich_xuat_llm(van_ban_goc: str, max_retries: int = 3) -> dict:
    ket_qua_kiem_toan = {
        "van_ban_goc": van_ban_goc,
        "trang_thai": "that_bai",
        "du_lieu_sach": None,
        "loi": None
    }
    
    # Mô phỏng quá trình gọi API có thể gặp lỗi tạm thời
    for lan_thu in range(1, max_retries + 1):
        try:
            # Giả lập phản hồi từ Gemini API với structured output
            phan_hoi_mo_phong = {
                "sentiment": "mixed",
                "diem_hai_long": 3,
                "trich_dan_chung_minh": "phòng hơi ồn"
            }
            
            # Tầng 1: Kiểm định Pydantic Schema
            doi_tuong = PhanTichDanhGia(**phan_hoi_mo_phong)
            
            # Tầng 2: Mỏ neo bằng chứng (Grounding)
            if doi_tuong.trich_dan_chung_minh not in van_ban_goc:
                raise ValueError("Ảo giác: Đoạn trích dẫn không có trong văn bản gốc!")
                
            ket_qua_kiem_toan["trang_thai"] = "thanh_cong"
            ket_qua_kiem_toan["du_lieu_sach"] = doi_tuong.model_dump()
            return ket_qua_kiem_toan
            
        except Exception as e:
            ket_qua_kiem_toan["loi"] = str(e)
            time.sleep(1 * lan_thu) # Chờ lũy tiến trước khi thử lại
            
    return ket_qua_kiem_toan

# Thử nghiệm trên nhận xét thực tế
vb_test = "Vị trí rất đẹp và thuận tiện, tuy nhiên phòng hơi ồn về đêm."
ket_qua = pipeline_trich_xuat_llm(vb_test)
print("KẾT QUẢ VẬN HÀNH ĐƯỜNG ỐNG:")
print(json.dumps(ket_qua, ensure_ascii=False, indent=2))
```

#### Bình luận chuyên môn
Quy trình trên thiết lập một chuẩn mực công nghiệp cho việc tích hợp AI vào xử lý dữ liệu: hệ thống không chỉ quan tâm đến kết quả cuối cùng mà ghi nhận toàn diện nhật ký vận hành, bảo đảm rằng bất kỳ sai sót nào cũng có thể truy vết và tái lập được trong môi trường kiểm toán độc lập.
:::

---

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
