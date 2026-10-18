## Thực hành ghép bảng phí theo phân khúc

::: exercise Giữ số dòng và giải thích những giá trị không ghép được
Bảng chỗ ở đã có cột `phan_khuc`, với ba giá trị `re`, `trung`, `cao`. Giá thiếu chưa được gán phân khúc. Bảng phí tương ứng là 10%, 13%, 15%. Hãy ghép trái với `validate="m:1"`, kiểm tra số dòng, đếm phí thiếu và tính giá sau phí. Giải thích vì sao phí thiếu không mặc nhiên có nghĩa là miễn phí.
:::

::: solution
```python
import pandas as pd
def ghep_phi(df):
    phi = pd.DataFrame({"phan_khuc":["re", "trung", "cao"],
                        "phi_dich_vu":[0.10, 0.13, 0.15]})
    result = df.merge(phi, on="phan_khuc", how="left", validate="m:1", indicator=True)
    assert len(result) == len(df)
    result["gia_tong"] = result["price"] * (1 + result["phi_dich_vu"])
    return result
```

Bảng phí có tối đa một hàng cho mỗi phân khúc, nên ghép không nhân số dòng của bảng trái. Cột `_merge` cho biết hàng chưa tìm được khóa. Nếu phân khúc chưa biết vì giá thiếu thì chưa xác định được phí, cần giữ giá sau phí là thiếu. Điền 0 vào phí ở đây sẽ tự thêm một quy tắc nghiệp vụ không có trong đề.
:::
