"""Keep IAI's label/output fixture, without republishing third-party review prose."""
import ast
import json
import re
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'raw_materials/xu-ly-du-lieu/practice'


def main():
    text = (Path(tempfile.gettempdir()) / 'studyhub-data-sources/iai-notebook-lab-11.txt').read_text(encoding='utf-8')
    values = {}
    for code in re.findall(r'^```python\n(.*?)^```', text, re.M | re.S):
        try:
            tree = ast.parse(code)
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                name = node.targets[0].id
                if name in ['GOLD', 'LLM_OUT']:
                    values[name] = ast.literal_eval(node.value)
    assert set(values) == {'GOLD','LLM_OUT'} and len(values['GOLD']) == len(values['LLM_OUT']) == 10
    payload = json.dumps(values, ensure_ascii=False, indent=2)
    (FOLDER / 'llm-fixture.json').write_text(payload + '\n', encoding='utf-8')
    body = '''## Thực hành kiểm tra văn bản đã chuyển thành bảng

### Chọn mẫu và nêu phạm vi đánh giá

::: exercise Lọc trước khi lấy mẫu
Giữ đánh giá có nội dung, thay đúng `<br/>` bằng dấu cách, chọn đoạn từ 50 ký tự rồi lấy 100 đoạn với seed 42. Khi đó kết quả đánh giá mô hình đại diện cho miền nào? Việc lọc có loại các đoạn ngắn nhưng vẫn có thông tin không?
:::

::: solution
```python
import pandas as pd
def chon_mau_van_ban(rv, n=100):
    c = rv.dropna(subset=["comments"]).copy()
    c["comments"] = c["comments"].str.replace("<br/>", " ", regex=False)
    du_dai = c.loc[c["comments"].str.len().ge(50)]
    if len(du_dai) < n:
        raise ValueError("Không đủ đoạn theo điều kiện lấy mẫu")
    return du_dai.sample(n=n, random_state=42)
```

Điểm chất lượng trên mẫu này chỉ nói về các đoạn qua bộ lọc độ dài và phạm vi thu thập. Các đoạn ngắn có thể vẫn chứa lời khen hoặc chê rõ ràng. Seed giúp chạy lại việc chọn mẫu, không làm mẫu tự đại diện cho mọi đánh giá.
:::

### Schema và nhãn tham chiếu đo hai điều khác nhau

::: exercise Kiểm tra mười phản hồi JSON
Với bộ nhãn tham chiếu và mười phản hồi mô phỏng dưới đây, viết schema gồm bốn trường. Cảm xúc nhận `positive`, `mixed`, `negative`. Khía cạnh nhận `location`, `cleanliness`, `host`, `noise`, `amenities`, `value`. `language` là chuỗi bắt buộc.

1. Tách ID lỗi cấu trúc khỏi các phản hồi hợp lệ.
2. Trong nhóm hợp lệ, tính tỷ lệ sentiment trùng nhãn tham chiếu và liệt kê ID không trùng.
3. Gắn cờ để đọc lại khi sentiment là positive nhưng có khía cạnh chê, hoặc là negative nhưng có khía cạnh khen. Cờ này có thay được nhãn tham chiếu không?

```python
import json
DU_LIEU_KIEM = json.loads(r\'''FIXTURE\''')
GOLD = {int(k):v for k,v in DU_LIEU_KIEM["GOLD"].items()}
LLM_OUT = {int(k):v for k,v in DU_LIEU_KIEM["LLM_OUT"].items()}
```
:::

::: solution
```python
from pydantic import BaseModel, ConfigDict, ValidationError
from typing import Literal
Aspect = Literal["location","cleanliness","host","noise","amenities","value"]
class ReviewInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")
    sentiment: Literal["positive","mixed","negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str

def danh_gia_json(outputs, gold):
    hop_le, loi_schema = {}, {}
    for rid, raw in outputs.items():
        try:
            hop_le[rid] = ReviewInfo.model_validate_json(raw)
        except ValidationError as error:
            loi_schema[rid] = error.errors()
    sai = [rid for rid,result in hop_le.items() if result.sentiment != gold[rid]["sentiment"]]
    accuracy = (len(hop_le)-len(sai))/len(hop_le) if hop_le else None
    co_doc_lai = [rid for rid,result in hop_le.items()
        if (result.sentiment == "positive" and result.aspects_negative)
        or (result.sentiment == "negative" and result.aspects_positive)]
    return hop_le, loi_schema, sai, accuracy, co_doc_lai

hop_le, loi_schema, sai, accuracy, co_doc_lai = danh_gia_json(LLM_OUT,GOLD)
assert sorted(loi_schema) == [2,5] and len(hop_le) == 8
assert sorted(sai) == [4,9,10] and accuracy == 0.625
assert sorted(co_doc_lai) == [9,10]
```

ID 2 có khía cạnh `photos` ngoài danh mục. ID 5 thiếu trường `language`. Trong tám phản hồi qua schema, năm phản hồi có sentiment trùng nhãn tham chiếu. Vì vậy điểm 62,5% phải được báo cùng tỷ lệ qua schema, không được hiểu thành tỷ lệ đúng trên cả mười đầu vào.

Các trường hợp 4, 9 và 10 minh họa ba vấn đề khác nhau: Bỏ sót ý chê giữa lời khen, bất đồng về cách gán nhãn cho nội dung pha trộn, và hiểu sai phủ định. Cụm “not a bad place” không đồng nghĩa với chê nơi ở là xấu. Khi người gán nhãn bất đồng, cần thống nhất quy tắc và đọc lại nội dung, không xem nhãn tham chiếu là chân lý không thể sửa.

Quy tắc hậu kiểm chỉ tạo cờ đọc lại. Một đánh giá tổng thể tiêu cực vẫn có thể khen một khía cạnh, nên hai trường cùng xuất hiện chưa phải mâu thuẫn logic trong mọi cách định nghĩa sentiment. Schema cũng chỉ kiểm tra cấu trúc và miền nhãn, không xác nhận mọi thông tin trích xuất là đúng.
:::
'''
    body = body.replace('FIXTURE', payload)
    (FOLDER / 'iai-bc-schema-chapter-7.md').write_text(body, encoding='utf-8')
    print('Prepared the 10-output IAI schema fixture and solved evaluation practice')


if __name__ == '__main__':
    main()
