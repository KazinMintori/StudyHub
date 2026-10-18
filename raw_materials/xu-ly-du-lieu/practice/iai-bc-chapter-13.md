## Thực hành diễn đạt và thẩm định kết luận

### Sắp kết luận, bằng chứng, giới hạn và cách tính

::: exercise Tổ chức một đoạn báo cáo để người đọc đối chiếu được
Sắp bốn nội dung theo thứ tự kết luận, bằng chứng, giới hạn rồi chi tiết phương pháp:

- A. Thống kê dùng 17.688 listing có giá trong bản chụp 29/06/2026, đồng thời ghi nhận 846 listing chưa có giá.
- B. Trung vị giá niêm yết là 59.000 CLP/đêm, thấp hơn trung bình khoảng 118.200 CLP/đêm.
- C. Khi tạm bỏ 177 giá trên P99, trung bình còn khoảng 82.298 CLP, còn trung vị là 58.400 CLP. Điều đó cho thấy trung bình nhạy với phần đuôi phải hơn trong bảng này.
- D. Kết luận mô tả giá niêm yết một đêm, không phải toàn bộ khoản khách thực trả và không suy rộng sang các listing chưa có giá.

Sau khi sắp, nêu thông tin nào cần kiểm lại bằng mã trước khi dùng trong báo cáo.
:::

::: solution
Thứ tự theo yêu cầu là B, C, D, A. B cho người đọc biết kết quả chính. C cung cấp phép đối chiếu, D giữ đúng phạm vi, còn A cho biết tập dữ liệu được tính. Đây là cách tổ chức đoạn báo cáo của bài, không phải thứ tự bắt buộc cho mọi loại văn bản học thuật.

```python
import pandas as pd
import numpy as np
def so_lieu_gia_bao_cao(ds):
    gia = ds["price"].dropna()
    p99 = gia.quantile(.99)
    duoi = gia.loc[gia.le(p99)]
    return {"so_co_gia":len(gia), "so_thieu":int(ds["price"].isna().sum()),
            "trung_vi":gia.median(), "trung_binh":gia.mean(),
            "so_tren_p99":int(gia.gt(p99).sum()),
            "tb_bo_tren_p99":duoi.mean(), "tv_bo_tren_p99":duoi.median()}
```

Phép bỏ phần đuôi ở C dùng để kiểm tra độ nhạy. Nó không tự cấp lý do loại các giá đó khỏi báo cáo chính. Cần kiểm lại bản dữ liệu, ngưỡng, số hàng, đơn vị và các phép tính trước khi sử dụng các con số.
:::

### Số đúng chưa đủ cho lời đúng

::: exercise Sửa năm lời diễn giải
Với mỗi cặp số liệu và lời viết, chỉ ra đại lượng được đo rồi viết lại trong đúng phạm vi:

1. Số đánh giá tháng 5 tăng 53,7% so cùng kỳ, lời viết gọi đó là thị trường tăng trưởng mạnh.
2. Mức tăng 3,0% so tháng trước được mô tả là “Bứt phá thần tốc”.
3. Hệ số tương quan 0,081 được dùng để nói nhiệt độ ảnh hưởng rõ rệt đến lượng đánh giá.
4. Bảng có đúng một listing yêu cầu tối thiểu 730 đêm, lời viết gọi là “Một vài ca cực đoan”.
5. Có 16.772 trong 18.534 listing liệt kê Wifi, lời viết kết luận mạng ổn định ở 90% chỗ ở.
:::

::: solution
1. Viết “Số đánh giá tháng 5 tăng 53,7% so cùng kỳ trong phạm vi dữ liệu đã chọn”. Một chỉ số số lượng đánh giá chưa đo trực tiếp toàn bộ thị trường.
2. Nêu mức tăng 3,0% và kỳ gốc. Từ “Bứt phá” chưa có tiêu chí đối chiếu, chẳng hạn biến động lịch sử hoặc ngưỡng đã định trước.
3. Nêu tương quan tuyến tính nhỏ trong mẫu đang xét. Không suy ra quan hệ nhân quả hoặc kết luận về mọi dạng liên hệ chỉ từ hệ số ấy.
4. Nên ghi đúng “Một listing có điều kiện tối thiểu 730 đêm cần được kiểm tra”. Sau đó xem quy tắc nhập liệu và loại hình lưu trú trước khi kết luận lỗi.
5. Viết “Khoảng 90,5% listing liệt kê Wifi”. Danh sách tiện nghi không đo chất lượng mạng thực tế.

```python
assert round(16772/18534*100,1) == 90.5
```

Không nên dùng các nhãn đúng/quá mức một cách máy móc. Phải giữ rõ biến được đo, tập hàng, kỳ so sánh và sức mạnh của kết luận. Một lời diễn giải nghe vừa phải vẫn có thể đổi từ số đánh giá sang một đại lượng khác.
:::

### Hai nhóm cùng tăng nhưng trung bình gộp giảm

::: exercise Kiểm tra trọng số trước khi nói giá giảm
Hai phân khúc cao và rẻ có trung bình 60 và 30 nghìn CLP tại T9, mỗi nhóm 100 quan sát. Tại T6, hai trung bình tăng thành 66 và 33, nhưng số quan sát tương ứng là 80 và 220. Tính trung bình gộp và giải thích hai chiều biến động.
:::

::: solution
```python
bang_simpson = pd.DataFrame({"ky":["T9","T9","T6","T6"],
    "phan_khuc":["cao","re","cao","re"],"n":[100,100,80,220],
    "gia_tb":[60.,30.,66.,33.]})
tong = bang_simpson.assign(tong_gia=lambda d:d["n"]*d["gia_tb"]).groupby("ky").agg(
    tong_gia=("tong_gia","sum"),so_quan_sat=("n","sum"))
gop = tong["tong_gia"]/tong["so_quan_sat"]
assert gop.loc["T9"] == 45 and gop.loc["T6"] == 41.8
assert np.isclose(66/60-1,.1) and np.isclose(33/30-1,.1)
```

Tỷ trọng nhóm rẻ tăng từ một nửa lên 220 trên 300 quan sát, nên mức giá thấp của nhóm này có trọng số lớn hơn. Cả hai trung bình nhóm tăng 10%, nhưng trung bình gộp giảm từ 45 xuống 41,8. Không thể thay kết luận về từng phân khúc bằng kết luận về tổng gộp.
:::

### Thẩm định lời nói “Được yêu thích hơn”

::: exercise Tách số lượng đánh giá khỏi mức độ yêu thích
Một nhận xét nói nhóm chủ nhà quản lý từ năm listing “Được khách yêu thích hơn” vì có khoảng 15,5 đánh giá/năm, còn nhóm dưới ngưỡng có 12,7. Hãy tính lại hai số, kiểm đơn vị quan sát, kiểm phương pháp chia nhóm, rồi sửa kết luận. Chọn thêm hai kết luận trong một bản phân tích để áp dụng cùng quy trình.
:::

::: solution
```python
def kiem_quy_mo_host(ds):
    if ds["calculated_host_listings_count"].isna().any():
        raise ValueError("Cần xử lý quy mô chủ nhà bị thiếu")
    return ds.groupby(ds["calculated_host_listings_count"].ge(5))["number_of_reviews_ltm"].agg(
        so_listing="size",so_co_du_lieu="count",trung_binh="mean")
```

Mỗi hàng của bảng đầu vào là một listing, nên đây là số đánh giá trung bình trên listing trong 12 tháng, không phải trung bình trên các chủ nhà riêng biệt. Ngưỡng năm listing là quy ước phân nhóm của bài. Số đánh giá không trực tiếp đo mức yêu thích, vì còn phụ thuộc lượng khách, thời gian hoạt động và xác suất viết đánh giá.

Có thể viết “Trong bản dữ liệu này, listing thuộc nhóm quản lý từ năm listing có số đánh giá trung bình trong 12 tháng cao hơn”. Sau đó kiểm tra thêm theo loại phòng, vị trí và phạm vi thời gian. Với hai kết luận tự chọn, cần lần theo dữ liệu và cách tính, kiểm biến được đo, rồi nêu rõ giới hạn của câu cuối cùng.
:::
