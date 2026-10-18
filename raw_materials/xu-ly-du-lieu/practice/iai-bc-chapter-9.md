## Thực hành tạo và kiểm tra biểu đồ

### Ba hình từ cùng một bản dữ liệu

::: exercise Tạo hình có thể chạy lại
Dùng listing và review Santiago ngày 29/06/2026, giữ `id` và `listing_id` cùng kiểu chuỗi.

1. Lọc review thuộc Providencia đến mốc chụp, đếm theo tháng và loại tháng chưa kết thúc. Vẽ đường, ghi trục ngày, số đánh giá, nguồn và lưu `providencia_thang.png`.
2. Theo từng quận có ít nhất 300 listing, tính tỷ lệ nguyên căn. Vẽ thanh ngang theo tỷ lệ phần trăm, trục đo bắt đầu từ 0 và ghi số trên thanh.
3. Vẽ histogram `availability_365` với 40 khoảng. Đếm riêng số listing có giá trị 0 và từ 360 trở lên, rồi đối chiếu hình. Không tự đồng nhất số ngày không mở lịch với số ngày đã có khách.
4. Vẽ lại tỷ lệ nguyên căn của Providencia, Vitacura, La Florida, Las Condes với trục cột từ 0. So với hình bị giới hạn trục trong khoảng 70–85%, lời mô tả nào cần thay đổi?
:::

::: solution
```python
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def tao_ba_hinh(ds, rv, folder, quan="Providencia", moc=pd.Timestamp("2026-06-29"), toi_thieu=300):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    ids = ds.loc[ds["neighbourhood"].eq(quan), "id"]
    date = pd.to_datetime(rv["date"], format="%Y-%m-%d")
    mask = rv["listing_id"].isin(ids) & date.le(moc)
    dem = pd.Series(1, index=date.loc[mask]).resample("ME").sum()
    dem = dem.loc[dem.index <= moc]
    fig1, ax1 = plt.subplots(figsize=(8,3.5))
    ax1.plot(dem.index, dem.values)
    ax1.set(title=f"Số đánh giá theo tháng tại {quan}, chỉ gồm tháng đã kết thúc",
            xlabel="Tháng", ylabel="Số đánh giá")
    fig1.text(.02,.01,"Nguồn: Inside Airbnb, Santiago, 29/06/2026",fontsize=9)
    fig1.savefig(folder/"providencia_thang.png",dpi=150,bbox_inches="tight")
    data = ds.assign(nguyen_can=ds["room_type"].eq("Entire home/apt").fillna(False))
    tk = data.groupby("neighbourhood").agg(n=("id","size"),pct=("nguyen_can","mean"))
    chon = tk.loc[tk["n"].ge(toi_thieu)].sort_values("pct")
    fig2, ax2 = plt.subplots(figsize=(7,4))
    bars = ax2.barh(chon.index, chon["pct"]*100)
    ax2.bar_label(bars,fmt="%.0f%%",padding=3)
    ax2.set(xlim=(0,105),xlabel="Tỷ lệ nguyên căn (%)",ylabel="Quận",
            title="Tỷ lệ nguyên căn tại các quận đủ quy mô")
    fig2.savefig(folder/"pct_nguyen_can.png",dpi=150,bbox_inches="tight")
    gia_tri = ds["availability_365"].dropna()
    if (~gia_tri.between(0,365)).any():
        raise ValueError("Số ngày mở lịch ngoài miền 0–365")
    fig3, ax3 = plt.subplots(figsize=(8,3.5))
    ax3.hist(gia_tri,bins=40,range=(0,365))
    ax3.set(title="Phân phối số ngày mở lịch trong 365 ngày tới",
            xlabel="Số ngày mở lịch",ylabel="Số chỗ ở")
    fig3.savefig(folder/"availability_hist.png",dpi=150,bbox_inches="tight")
    for ax in [ax1,ax2,ax3]:
        assert ax.get_title() and ax.get_xlabel() and ax.get_ylabel()
    assert ax2.get_xlim()[0] == 0 and len(ax2.patches) == len(chon)
    assert len(ax3.patches) == 40
    return [fig1,fig2,fig3], dem, chon, (int(gia_tri.eq(0).sum()),int(gia_tri.ge(360).sum()))

def sua_truc_cot(ds, cac_quan):
    p = ds.assign(nc=ds["room_type"].eq("Entire home/apt")).groupby("neighbourhood")["nc"].mean()
    p = p.loc[cac_quan].sort_values()*100
    fig, ax = plt.subplots(figsize=(7,4))
    ax.bar(p.index,p.values)
    ax.set(ylim=(0,100),ylabel="Tỷ lệ nguyên căn (%)",xlabel="Quận",
           title="So sánh tỷ lệ nguyên căn trên cùng thang phần trăm")
    ax.tick_params(axis="x",labelrotation=20)
    assert ax.get_ylim()[0] == 0
    return fig, ax
```

Các assertion kiểm tra thành phần và số đối tượng vẽ, chưa đánh giá được thông điệp có đúng hay nhãn có dễ đọc không. Cần mở hình và đọc lại cùng dữ liệu. Tiêu đề dài hơn 15 ký tự cũng không tự bảo đảm tiêu đề chính xác. Với một bản dữ liệu khác, giữ cùng mã xử lý nhưng thay bảng đầu vào và ghi đúng nguồn, mốc chụp của bản đó.
:::

### Boxplot với hue và thang log

::: exercise Đọc phân phối theo hai cách chia nhóm
Theo quy ước số listing từ 5 trở lên, chia quy mô quản lý thành hai nhóm. Vẽ boxplot giá theo loại phòng, dùng màu cho nhóm quy mô và trục giá log. Kiểm tra chú giải. Giải thích phần chồng lấn và giới hạn của cách phân nhóm, không suy hiệu quả kinh doanh từ số đánh giá.
:::

::: solution
```python
def boxplot_quy_mo(ds):
    data = ds.loc[ds["price"].gt(0).fillna(False)].copy()
    data["kieu_host"] = data["calculated_host_listings_count"].ge(5).map(
        {True:"Từ 5 listing",False:"Dưới 5 listing"})
    fig, ax = plt.subplots(figsize=(8.5,4))
    sns.boxplot(data=data,x="price",y="room_type",hue="kieu_host",ax=ax)
    ax.set_xscale("log")
    ax.set(title="Phân phối giá dương theo loại phòng và quy mô quản lý",
           xlabel="Giá niêm yết (CLP/đêm), thang log",ylabel="Loại phòng")
    assert ax.get_xscale() == "log" and ax.get_legend() is not None
    return fig, ax, len(ds)-len(data)
```

Thang log chỉ dùng được với các giá dương. Hàm trả thêm số hàng không được vẽ để báo rõ phạm vi. Khoảng hộp chồng lấn cho thấy một biến chia nhóm chưa tách được hai phân phối hoàn toàn. Cần xem cỡ mẫu và các biến khác trước khi diễn giải nguyên nhân.
:::

### Bản đồ giá đặt cạnh quy mô nguồn cung

::: exercise Ghép ranh giới và giải thích giá trị thiếu
Với GeoDataFrame có khóa `neighbourhood`, tính số listing và trung vị giá từng quận, ghép trái vào bản đồ. Giữ các vùng không có listing. Chỉ điền 0 vào số lượng khi đã xác nhận bảng listing là toàn bộ bản chụp và mọi tên quận đều khớp. Trung vị giá ở vùng không có quan sát phải giữ thiếu.

Vẽ hai choropleth cạnh nhau, gồm giá trung vị và số listing, có chú giải và cỡ mẫu. Vì sao vùng tô màu lớn chưa chắc đóng góp nhiều listing?
:::

::: solution
```python
def cap_ban_do(geo, ds):
    if not geo["neighbourhood"].is_unique:
        raise ValueError("Khóa ranh giới cần duy nhất")
    if ds["neighbourhood"].isna().any() or (~ds["neighbourhood"].isin(geo["neighbourhood"])).any():
        raise ValueError("Cần xử lý tên quận chưa khớp trước khi điền 0")
    kpi = ds.groupby("neighbourhood",as_index=False).agg(n=("id","size"),gia_tv=("price","median"))
    ban_do = geo.merge(kpi,on="neighbourhood",how="left",validate="1:1")
    ban_do["n"] = ban_do["n"].fillna(0).astype(int)
    assert ban_do["n"].sum() == len(ds)
    fig, axes = plt.subplots(1,2,figsize=(10,5))
    ban_do.plot(column="gia_tv",legend=True,cmap="Purples",ax=axes[0],
                 missing_kwds={"color":"lightgrey","label":"Chưa có giá"})
    ban_do.plot(column="n",legend=True,cmap="Blues",ax=axes[1])
    axes[0].set_title("Trung vị giá niêm yết (CLP/đêm)")
    axes[1].set_title("Số chỗ ở trong từng quận")
    for ax in axes:
        ax.set_axis_off()
    fig.text(.02,.02,f"Tổng số listing: {len(ds):,}. Vùng không có listing nhận số lượng 0.")
    return ban_do, fig, axes
```

Diện tích vùng là hình học địa lý, còn màu là đại lượng trong bảng. Chỉ nhìn diện tích mảng màu có thể làm người đọc đánh giá quá cao vai trò của một quận rộng nhưng ít listing. Hai bản đồ bổ sung hai thông tin khác nhau, không thay thế việc đọc số liệu theo khóa.
:::

### Kỳ gốc và điểm dữ liệu tương tác

::: exercise Sửa phạm vi thời gian và xem từng điểm
1. Một đồ thị bắt đầu ở năm 2020 để mô tả mức tăng đến 2025. Vẽ lại dữ liệu 2016–2025, bỏ năm 2026 chưa trọn, đánh dấu giai đoạn 2020–2021 và chọn lời diễn giải dựa trên toàn hình. So kết quả khi lấy 2019 và 2020 làm gốc.
2. Dùng `plotly.express.scatter` vẽ kinh độ, vĩ độ của tối đa 5.000 listing với tên, quận và giá khi rê chuột. Xem năm giá cao nhất trong mẫu. Vì sao một báo cáo PDF vẫn cần hình tĩnh có đủ nhãn và chú thích?
:::

::: solution
```python
def sua_ky_goc(rv):
    dates = pd.to_datetime(rv["date"],format="%Y-%m-%d")
    nam = pd.Series(1,index=dates).resample("YE").sum()
    nam = nam.reindex(pd.date_range("2016-12-31","2025-12-31",freq="YE"),fill_value=0)
    fig, ax = plt.subplots(figsize=(8,3.5))
    ax.plot(nam.index.year,nam.values,marker="o")
    ax.axvspan(2020,2021,color="grey",alpha=.2,label="Giai đoạn 2020–2021")
    ax.set(title="Số đánh giá theo năm, 2016–2025",xlabel="Năm",ylabel="Số đánh giá")
    ax.legend()
    n2025 = nam.loc["2025-12-31"]
    ratios = {year:(n2025/nam.loc[f"{year}-12-31"]-1 if nam.loc[f"{year}-12-31"] else np.nan)
              for year in [2019,2020]}
    return fig, ax, ratios

def diem_tuong_tac(ds, n=5000):
    import plotly.express as px
    mau = ds.sample(min(n,len(ds)),random_state=42)
    fig = px.scatter(mau,x="longitude",y="latitude",hover_name="name",
                     hover_data=["neighbourhood","price"],
                     title="Các chỗ ở trong mẫu và thông tin từng điểm")
    return fig, mau.nlargest(5,"price")
```

Kỳ gốc thấp có thể làm phần trăm tăng lớn hơn mà không thay đổi giá trị cuối kỳ. Chú thích một giai đoạn chưa tự chứng minh nguyên nhân biến động. Hình tương tác giúp đọc thông tin của từng điểm, nhưng PDF không giữ đầy đủ thao tác ấy. Bản tĩnh cần chứa những thông tin cần thiết để người đọc hiểu mà không phải rê chuột.
:::
