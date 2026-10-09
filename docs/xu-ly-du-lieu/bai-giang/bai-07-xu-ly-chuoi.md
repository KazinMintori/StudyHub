---
course: xu-ly-du-lieu
lecture: bai-07-xu-ly-chuoi
section: lecture
title: "Xử lý dữ liệu chuỗi"
prerequisites: ["bien-kieu","gia-tri-thieu","vector-hoa"]
lessonStatus: ready
description: "Chuẩn hóa chuỗi, phân biệt văn bản literal và regex, trích xuất trường và giữ dữ liệu thiếu."
---

Trong mọi nguồn dữ liệu thực tế, dữ liệu chuỗi ký tự (văn bản) luôn là vùng đất hỗn loạn và nhiều cạm bẫy nhất. Con người gõ phím với muôn vàn thói quen dị biệt: lúc viết hoa, lúc viết thường, gõ thừa dấu cách, chèn nhầm khoảng trắng không ngắt, và đặc biệt là hệ thống dấu thanh phức tạp của tiếng Việt.

Nếu chỉ nhìn bằng mắt thường trên màn hình, hai chuỗi văn bản có thể trông giống hệt nhau từng nét chữ. Nhưng dưới đáy bộ nhớ máy tính, chúng có thể mang các mã nhị phân hoàn toàn khác biệt. Nếu đưa thẳng dữ liệu thô này vào các phép toán tổng hợp, hệ thống sẽ coi chúng là những thực thể riêng biệt, dẫn đến sự phân mảnh số liệu nghiêm trọng.

Bài học này cung cấp phương pháp tiếp cận khoa học và chuẩn mực đối với dữ liệu văn bản: kỹ thuật chuẩn hóa đa tầng, giải mã bản chất bảng mã Unicode tiếng Việt, sử dụng biểu thức chính quy (Regex) phòng thủ, và chuyển đổi an toàn các định dạng số liệu đa quốc gia.

## 1. Chuẩn hóa đa tầng và bài toán Unicode tiếng Việt

Hãy xem xét một ví dụ thực tế về cột địa danh:

```python
import pandas as pd

raw = pd.Series(["  Hà Nội ", "HÀ NỘI", "Hà  Nội", None], dtype="string")
clean = (raw.str.normalize("NFC").str.strip()
         .str.replace(r"\s+", " ", regex=True).str.casefold())
print(clean.tolist())            # ['hà nội', 'hà nội', 'hà nội', <NA>]
print(clean.nunique())           # 1
```

Nếu không chuẩn hóa, ba dòng đầu tiên sẽ bị đếm thành 3 nhóm địa danh hoàn toàn khác nhau. Bằng chuỗi xử lý bốn bước trên, ta đưa toàn bộ về duy nhất 1 giá trị chuẩn mực `'hà nội'`.

Bản chất của từng mắt xích trong chuỗi biến đổi:

1. **Chuẩn hóa Unicode NFC (`.str.normalize("NFC")`)**: 
   Đây là bước xử lý đặc biệt quan trọng đối với dữ liệu tiếng Việt. Trong chuẩn quốc tế Unicode, một chữ cái có dấu tiếng Việt (như chữ "à" hay "ệ") có thể được mã hóa theo hai trường phái:
   - **NFC (Dựng sẵn - Precomposed)**: Ký tự "à" được gán một mã điểm duy nhất (`U+00E0`).
   - **NFD (Tổ hợp - Decomposed)**: Ký tự "à" được ghép từ chữ cái gốc "a" (`U+0061`) đi kèm một ký tự dấu huyền rời (`U+0300`).
   Trên màn hình, mắt người không thể phân biệt được hai cách viết này. Nhưng toán tử so sánh `==` của máy tính sẽ trả về `False` vì các byte nhị phân bên dưới hoàn toàn khác nhau. Việc gọi `.str.normalize("NFC")` giúp ép toàn bộ ký tự tổ hợp về dạng dựng sẵn đồng nhất, triệt tiêu tận gốc hiện tượng trùng lặp ma quái.
2. **Cắt tỉa hai đầu (`.str.strip()`)**: Loại bỏ khoảng trắng vô nghĩa ở đầu và cuối chuỗi.
3. **Thu gọn khoảng trắng nội bộ (`.str.replace(r"\s+", " ", regex=True)`)**: Biểu thức `\s+` nhận diện mọi chuỗi gồm một hoặc nhiều khoảng trắng (kể cả phím Tab hay ký tự xuống dòng) ở giữa các từ và nén chúng lại thành đúng một dấu cách đơn.
4. **Hạ cỡ chữ toàn năng (`.str.casefold()`)**: Phương thức `casefold()` mạnh hơn `lower()` tiêu chuẩn. Nó được thiết kế theo chuẩn Unicode để xử lý triệt để việc so khớp không phân biệt hoa thường trên mọi bảng chữ cái của các ngôn ngữ khác nhau.

Toàn bộ chuỗi thao tác được thực hiện thông qua bộ định tuyến **`.str`** của pandas. Điểm ưu việt của `.str` là tính năng bảo tồn dữ liệu khuyết thiếu: khi gặp ô `None` hay `<NA>`, các phương thức tự động bỏ qua mà không ném ra ngoại lệ `AttributeError`.

## 2. Phân định rạch ròi giữa chuỗi nguyên bản (Literal) và mẫu Regex

Biểu thức chính quy (Regular Expression - Regex) là ngôn ngữ mô tả quy luật của chuỗi ký tự. Trong Regex, một số ký tự đặc biệt (gọi là metacharacters) mang ý nghĩa cú pháp riêng chứ không đại diện cho chính nó.

Một trong những sai lầm kinh điển nhất là tìm kiếm dấu chấm câu:

```python
s = pd.Series(["a.b", "axb", None], dtype="string")
print(s.str.contains(".", regex=False, na=False).tolist())
print(s.str.contains(r"\.", regex=True, na=False).tolist())
# Cả hai: [True, False, False]
```

- Trong Regex, dấu chấm `.` đại diện cho **bất kỳ ký tự nào** (trừ ký tự xuống dòng). Do đó, nếu bạn viết `s.str.contains(".")` mà quên đặt `regex=False`, cả chuỗi `"a.b"` lẫn `"axb"` đều sẽ được đánh giá là khớp (`True`)!
- Để tìm đúng dấu chấm thực sự, bạn có hai lựa chọn: tắt chế độ regex bằng `regex=False`, hoặc sử dụng ký tự gạch chéo ngược để thoát nghĩa: `r"\."`.

| Ký hiệu Regex | Bản chất ngữ nghĩa | Ví dụ ứng dụng trong kiểm định dữ liệu |
| :--- | :--- | :--- |
| `[0-9]` hoặc `\d` | Một chữ số đơn lẻ từ 0 đến 9. | Kiểm tra ký tự số trong căn cước hoặc số điện thoại. |
| `+` | Lặp lại ít nhất một lần trở lên. | `\d+` nhận diện một khối số có độ dài bất kỳ. |
| `{n}` | Lặp lại chính xác đúng $n$ lần. | `[0-9]{3}` yêu cầu đúng 3 chữ số liên tiếp. |
| `(...)` | Nhóm bắt (Capturing Group). | Cô lập phần thông tin cần trích xuất ra khỏi mẫu khớp. |
| `^` và `$` | Neo giữ biên đầu (`^`) và biên cuối (`$`). | Bảo đảm toàn bộ chuỗi phải khớp từ đầu đến chân. |

pandas cung cấp ba hàm kiểm tra khớp mẫu với cấp độ chặt chẽ tăng dần:
- **`.str.contains()`**: Chỉ cần chuỗi con xuất hiện ở bất kỳ ngóc ngách nào trong văn bản là trả về `True`.
- **`.str.match()`**: Bắt buộc mẫu phải khớp bắt đầu từ ký tự đầu tiên của chuỗi, nhưng phần đuôi phía sau có thể chứa ký tự thừa.
- **`.str.fullmatch()`**: Toàn bộ chuỗi từ ký tự đầu tiên đến ký tự cuối cùng phải khớp hoàn hảo với mẫu. Khi cần kiểm định định dạng mã sản phẩm hay số hóa đơn, **`fullmatch`** là chuẩn mực bắt buộc để ngăn chặn dữ liệu rác lọt lưới.

## 3. Trích xuất trường thông tin và phát hiện bản ghi dị biệt

Trong nhiều hệ thống kế thừa, dữ liệu có cấu trúc thường bị nhồi nhét chung vào một cột ghi chú tự do. Ta sử dụng nhóm bắt trong biểu thức chính quy để bóc tách thông tin chuẩn xác.

```python
ma = pd.Series(["SP-001", "SP-012", "ghi chu SP-003", "SP-x"], dtype="string")
dung = ma.str.fullmatch(r"SP-[0-9]{3}", na=False)
so = ma.where(dung).str.extract(r"SP-([0-9]{3})", expand=False)
print(dung.tolist())             # [True, True, False, False]
print(so.dropna().tolist())       # ['001', '012']
```

Quy trình hai bước thể hiện tính kỷ luật cao:
1. **Kiểm định trước khi trích xuất**: Dòng `"ghi chu SP-003"` mặc dù có chứa cụm `SP-003`, nhưng nó bị lẫn tạp chất văn bản và không phải là một mã hàng thuần túy. Hàm `fullmatch` gắn cờ đánh dấu dòng này là không hợp lệ (`False`).
2. **Trích xuất trên tập hợp đã xác thực**: Phương thức `ma.where(dung)` lọc giữ lại các dòng đạt chuẩn trước khi gọi `.str.extract()`. Cặp dấu ngoặc đơn `([0-9]{3})` báo cho pandas biết ta chỉ muốn lấy riêng 3 chữ số phía sau. Kết quả trả về được giữ nguyên kiểu chuỗi để bảo tồn các số 0 ở đầu.

## 4. Chuyển đổi định dạng số và tiền tệ đa quốc gia

Chuyển đổi văn bản chứa tiền tệ thành số thực để tính toán là thao tác tiềm ẩn nhiều rủi ro sai số nhất do sự xung đột về quy ước quốc tế:
- **Quy ước Anh - Mỹ**: Dấu phẩy `,` phân cách hàng nghìn, dấu chấm `.` là dấu thập phân (Ví dụ: `1,200.50`).
- **Quy ước Việt Nam - Châu Âu**: Dấu chấm `.` phân cách hàng nghìn, dấu phẩy `,` là dấu thập phân (Ví dụ: `1.200,50`).

Nếu bạn tiếp cận một tệp dữ liệu Việt Nam ghi `1.200,50` mà áp dụng máy móc câu lệnh của người Mỹ bằng cách xóa bỏ dấu phẩy:
```python
# HẬU QUẢ TAI HẠI:
gia_sai = float("1.200,50".replace(",", ""))  # Trở thành 1.20050 = 1.2005!
```
Một món hàng có giá 1.200 nghìn đồng (1,2 triệu) đã bị biến thành 1,2 nghìn đồng (hụt mất 1.000 lần giá trị!). Luôn xác định rõ quy ước địa phương trước khi viết mã làm sạch.

Giả sử tệp dữ liệu tuân theo quy ước chuẩn của Mỹ:

```python
gia = pd.Series(["1,200.50", " 900.00 ", "N/A", None], dtype="string")
gia_text = gia.str.strip().str.replace(",", "", regex=False)
gia_so = pd.to_numeric(gia_text, errors="coerce")
loi_doc = gia.notna() & gia_so.isna()
print(gia_so.dropna().tolist())   # [1200.5, 900.0]
print(loi_doc.tolist())          # [False, False, True, False]
```

Kỹ thuật lập biên bản lỗi bằng mặt nạ Boolean:
- Hàm `pd.to_numeric(..., errors="coerce")` biến các chuỗi không đọc được (như `"N/A"`) thành giá trị khuyết thiếu `NaN` thay vì ném lỗi làm sập chương trình.
- Biểu thức `loi_doc = gia.notna() & gia_so.isna()` phân biệt rạch ròi giữa hai bản chất: ô ban đầu vốn đã rỗng (`None`) với ô có dữ liệu nhưng đọc thất bại (`"N/A"`). Dòng thứ ba là lỗi đọc dữ liệu cần chuyển cho đội ngũ nhập liệu rà soát lại, hoàn toàn không được trộn lẫn với dữ liệu rỗng thông thường.

## 5. Tách trường danh mục và mã hóa One-Hot

Khi một trường văn bản chứa nhiều thuộc tính ngăn cách bởi dấu phân tách (như danh sách nhãn mác hoặc thẻ phân loại), ta có hai hướng xử lý tùy thuộc vào mục đích phân tích:

```python
tags = pd.Series(["sach|moi", "vo|moi", None], dtype="string")
tach = tags.str.split("|", regex=False, expand=True)
print(tach.iloc[0].tolist())      # ['sach', 'moi']
flags = tags.str.get_dummies(sep="|")
print(flags.loc[0, "sach"], flags.loc[1, "vo"])  # 1 1
```

- **`str.split(..., expand=True)`**: Tách chuỗi thành nhiều cột độc lập. Cột 0 chứa nhãn thứ nhất, cột 1 chứa nhãn thứ hai.
- **`str.get_dummies(sep="|")`**: Kỹ thuật mã hóa One-Hot Encoding trực tiếp từ chuỗi. pandas tự động quét toàn bộ các nhãn phân biệt và tạo ra các cột nhị phân tương ứng. Nếu dòng dữ liệu có chứa nhãn đó, ô sẽ nhận giá trị 1; ngược lại nhận giá trị 0. Đây là bước chuẩn bị dữ liệu kinh điển trước khi đưa các thuộc tính danh mục vào các mô hình học máy.

## 6. Bài tập tự luyện

::: exercise Thẩm định cấp độ khớp của biểu thức chính quy
Để xác thực một chuỗi mã đơn hàng bắt buộc phải có đúng 2 chữ cái Latin in hoa đứng đầu, theo sau bởi đúng 3 chữ số (ví dụ `"HD123"`), ta nên chọn phương thức nào giữa `contains`, `match` và `fullmatch` với mẫu `r"[A-Z]{2}[0-9]{3}"`? Phân tích nguy cơ nếu chọn sai phương thức.
:::

::: solution
Bắt buộc phải chọn phương thức **`.str.fullmatch()`**.

Phân tích nguy cơ:
- Nếu dùng `.str.contains()`: Chuỗi rác như `"ma loi HD123 va du lieu thua"` vẫn sẽ trả về `True` vì nó tìm thấy cụm `"HD123"` nằm lọt thỏm ở giữa.
- Nếu dùng `.str.match()`: Chuỗi rác như `"HD123-tam-thoi"` vẫn sẽ trả về `True` vì phần đầu chuỗi khớp mẫu.
- Chỉ có `.str.fullmatch()` mới bảo đảm toàn bộ chuỗi từ đầu đến cuối chỉ chứa đúng 2 chữ hoa và 3 chữ số, bảo vệ hệ thống trước các bản ghi không đạt chuẩn.
:::

::: exercise Nguy cơ khi ép kiểu chuỗi mù quáng
Trong ví dụ mở đầu bài học, vì sao ta không dùng cú pháp `raw.astype(str)` trước khi tiến hành làm sạch các giá trị `None`?
:::

::: solution
Vì phương thức `raw.astype(str)` của Python thuần sẽ biến giá trị rỗng `None` thành một chuỗi ký tự chữ thực sự mang nội dung `'None'`.

Khi đó, hệ thống sẽ hiểu lầm rằng đây là một từ hợp lệ có độ dài 4 ký tự. Khi thực hiện các phép đếm hay phân nhóm sau này, chuỗi `'None'` sẽ bị tính là một danh mục hàng hóa thực tế. Sử dụng kiểu `string` chuyên dụng của pandas cùng bộ định tuyến `.str` giúp bảo tồn nguyên vẹn bản chất khuyết thiếu của ô dữ liệu.
:::

::: exercise Cạm bẫy chuyển đổi dấu phân cách số thực
Một bảng dữ liệu doanh thu của một doanh nghiệp châu Âu ghi nhận chuỗi `"1.200,50"`. Nếu một lập trình viên thực hiện lệnh `float(text.replace(",", ""))`, kết quả thu được là bao nhiêu? Cần viết lại thao tác này như thế nào để nhận được con số chính xác 1200.5?
:::

::: solution
- Kết quả thu được là `1.2005` (do lệnh chỉ xóa dấu phẩy, chuỗi trở thành `"1.20050"`, ép kiểu float thành `1.2005`). Doanh thu bị sụt giảm 1.000 lần so với thực tế.
- Để xử lý chính xác theo quy ước châu Âu (dấu chấm phân cách hàng nghìn, dấu phẩy phân cách thập phân), ta phải thực hiện hai bước:
  1. Xóa bỏ dấu chấm phân cách hàng nghìn: `text.replace(".", "")` -> trở thành `"1200,50"`.
  2. Thay dấu phẩy thập phân thành dấu chấm: `.replace(",", ".")` -> trở thành `"1200.50"`.
  3. Cuối cùng mới ép kiểu sang float để nhận giá trị chuẩn xác `1200.5`.
:::

::: exercise Làm sạch chuỗi giá tiền tệ đa dạng và bóc tách tiện ích với get_dummies
Cho bảng dữ liệu khảo sát khách sạn lưu trong một DataFrame:
```python
import pandas as pd

df_ks = pd.DataFrame({
    "ma_ks": ["KS01", "KS02", "KS03", "KS04", "KS05"],
    "gia_niem_yet": [" $1,250.00 ", " 450.50 USD ", "Lien_he", " $90.00 ", " -50.00 "],
    "tien_ich": ["Wifi, Bể bơi, Ăn sáng", "Wifi, Chỗ đỗ xe", "Ăn sáng, Bể bơi", "Wifi", "Bể bơi, Chỗ đỗ xe"]
})
```
Yêu cầu:
1. Chuẩn hóa cột `gia_niem_yet` thành cột số thực `gia_chuan`. Các giá trị chữ không đọc được số hoặc số âm phải được đưa về `NaN` an toàn.
2. Từ cột `tien_ich`, hãy tạo ra các cột chỉ báo nhị phân ($0$ và $1$) cho từng tiện ích riêng biệt (One-Hot Encoding) để phục vụ mô hình hồi quy giá phòng.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Chuỗi hàm replace lồng nhau và xử lý chuỗi thủ công)
Một cách người ta hay làm khi mới tiếp cận là gọi nhiều lần `.str.replace()` để gọt từng ký tự một:

```python
# 1. Làm sạch giá bằng chuỗi replace
gia_c1 = df_ks["gia_niem_yet"].astype(str)
gia_c1 = gia_c1.str.replace("$", "", regex=False)
gia_c1 = gia_c1.str.replace("USD", "", regex=False)
gia_c1 = gia_c1.str.replace(",", "", regex=False)
gia_c1 = gia_c1.str.strip()

gia_so_c1 = pd.to_numeric(gia_c1, errors="coerce")
gia_so_c1.loc[gia_so_c1 < 0] = float("nan")
df_ks["gia_chuan"] = gia_so_c1

# 2. Bóc tách tiện ích thủ công qua vòng lặp
cac_tien_ich = ["Wifi", "Bể bơi", "Ăn sáng", "Chỗ đỗ xe"]
for ti in cac_tien_ich:
    df_ks[f"has_{ti}"] = df_ks["tien_ich"].apply(lambda s: 1 if ti in str(s) else 0)

print("Bảng khách sạn căn bản:\n", df_ks[["ma_ks", "gia_chuan", "has_Wifi", "has_Bể bơi"]])
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Mẫu Regex phủ định tổng quát và `str.get_dummies`)
Lập trình viên chuyên nghiệp sẽ tận dụng sức mạnh của biểu thức chính quy phủ định để dọn sạch mọi ký tự lạ chỉ bằng một dòng lệnh, kết hợp phương thức vector hóa `str.get_dummies`:

```python
# 1. Làm sạch siêu tốc: Xóa bỏ mọi ký tự KHÔNG PHẢI là chữ số hoặc dấu chấm
# Mẫu [^0-9.] phủ định giúp loại bỏ cùng lúc $, USD, dấu phẩy, khoảng trắng và chữ
df_ks["gia_chuan"] = pd.to_numeric(
    df_ks["gia_niem_yet"].astype(str).str.replace(r"[^0-9.]", "", regex=True),
    errors="coerce"
)
# Lọc bỏ miền giá trị vi phạm (âm hoặc bằng 0 nếu nghiệp vụ yêu cầu)
df_ks.loc[df_ks["gia_niem_yet"].astype(str).str.contains("-"), "gia_chuan"] = float("nan")

# 2. Vector hóa nhãn đa trị thành các cột nhị phân chuẩn tắc trong 1 bước
dummies_tien_ich = df_ks["tien_ich"].str.get_dummies(sep=", ")

# Ghép trực tiếp vào bảng phân tích
df_ks_hoan_chinh = pd.concat([df_ks[["ma_ks", "gia_chuan"]], dummies_tien_ich], axis=1)
print("Bảng khách sạn tối ưu:\n", df_ks_hoan_chinh)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Ưu thế của mẫu Regex phủ định `r'[^0-9.]'`**: Nếu dùng cách cơ bản xóa từng chữ (`"$"`, `"USD"`, `","`), chương trình sẽ sụp đổ ngay khi xuất hiện đơn vị mới như `"EUR"`, `"VND"` hay `"¥"`. Biểu thức phủ định `[^0-9.]` mang tính phòng thủ tuyệt đối: nó giữ lại cốt lõi số học và triệt tiêu toàn bộ rác định dạng ngoại lai.
- **Sức mạnh của `str.get_dummies(sep=', ')`**: Phương thức này tự động thu thập từ điển toàn bộ các tiện ích xuất hiện trong cột dữ liệu, tự động xử lý khoảng trắng sau dấu phân cách và trả về ma trận thưa nhị phân $0/1$ tối ưu bộ nhớ, sẵn sàng đưa vào các mô hình Machine Learning hoặc phân tích tương quan thống kê.
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 7, mục 7.4: String Manipulation](https://wesmckinney.com/book/data-cleaning).
- Hướng dẫn chính thức: [pandas User Guide — Working with text data](https://pandas.pydata.org/docs/user_guide/text.html).
- Tài liệu thư viện chuẩn Python về biểu thức chính quy: [Python re Module](https://docs.python.org/3/library/re.html).
- Chuẩn quốc tế về chuẩn hóa văn bản: [Unicode Standard Annex #15 — Unicode Normalization Forms](https://unicode.org/reports/tr15/).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-07-xu-ly-chuoi.html).
