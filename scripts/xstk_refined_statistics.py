"""Twenty-seven statistics figures with exact distributions and reserved labels."""
import math
import numpy as np
from scipy import stats
from xstk_refined_common import *

SEED=20261020
CI_MEANS=np.random.default_rng(SEED).normal(50,1.2,20)
CI_MARGIN=stats.norm.ppf(.975)*1.2
CI_COVERS=np.abs(CI_MEANS-50)<=CI_MARGIN

def proportion_intervals():
    n,k,z=30,2,stats.norm.ppf(.975);p=k/n
    wald=np.array([p-z*np.sqrt(p*(1-p)/n),p+z*np.sqrt(p*(1-p)/n)])
    den=1+z*z/n;center=(p+z*z/(2*n))/den
    margin=z*np.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return wald,np.array([center-margin,center+margin])

def ks_details():
    sample=np.array([-1.2,-.4,.2,.8,1.5]);null=stats.norm.cdf(sample);n=len(sample)
    plus=np.arange(1,n+1)/n-null;minus=null-np.arange(n)/n
    if plus.max()>=minus.max():
        i=plus.argmax();end=np.arange(1,n+1)[i]/n
    else:i=minus.argmax();end=np.arange(n)[i]/n
    return sample,float(max(plus.max(),minus.max())),sample[i],null[i],end

def verify_statistics_math():
    assert 10/np.sqrt(16)==2.5
    assert math.isclose(stats.norm.ppf(.975),1.959963984540054)
    assert len(CI_MEANS)==20 and np.allclose((CI_MEANS+CI_MARGIN)-(CI_MEANS-CI_MARGIN),2*CI_MARGIN)
    assert np.allclose(proportion_intervals(),[[-.02259402,.15592735],[.01847702,.21323458]])
    assert np.allclose(stats.chi2.ppf([.025,.975],9),[2.7003895,19.0227678])
    assert math.isclose(2*stats.norm.sf(2.3),.02144822004335162)
    assert math.isclose(stats.norm.sf(stats.norm.ppf(.95)),.05)
    assert math.isclose(stats.norm.cdf(stats.norm.ppf(.95)-2.5),.1962350572,rel_tol=1e-6)
    obs=np.array([85,30,15,70]);exp=np.array([80,35,15,70]);stat=((obs-exp)**2/exp).sum()
    assert math.isclose(stat,1.0267857142857144)
    table=np.array([[20,30,10],[30,10,20]])
    expected=np.outer(table.sum(1),table.sum(0))/table.sum()
    assert np.allclose(expected,[[25,20,15],[25,20,15]])
    assert math.isclose(stats.f.ppf(.95,3,20),3.09839121214078)
    groups=[np.array(g) for g in [[2,3,4],[4,5,6],[6,7,8]]]
    grand=np.concatenate(groups).mean();ssb=sum(len(g)*(g.mean()-grand)**2 for g in groups);ssw=sum(((g-g.mean())**2).sum() for g in groups)
    assert (ssb,ssw,ssb+ssw,ssb/2/(ssw/6))==(24,6,30,12)
    assert stats.rankdata(np.abs([1.2,-2.5,4.8])).tolist()==[1,2,3]
    sample,D,*_=ks_details();assert math.isclose(D,stats.kstest(sample,stats.norm.cdf).statistic)
    assert math.isclose(D,.18814460141660336)
    print(f"PASS: Statistics numerical labels; coverage {int(CI_COVERS.sum())}/20, seed {SEED}; KS D={D:.9f}.")

def generate_all_statistics_figures(out):
    out.mkdir(parents=True,exist_ok=True)
    f,a=chart("Tổng thể và phân phối trung bình mẫu","Mẫu độc lập từ N(50, 100), cỡ mẫu n = 16")
    x=np.linspace(15,85,1001)
    a.plot(x,stats.norm.pdf(x,50,10),color=C,label="Quan sát X: SD = 10")
    a.plot(x,stats.norm.pdf(x,50,2.5),color=P,label="Trung bình X̄: SE = 2.5")
    a.set(xlabel="Giá trị",ylabel="Mật độ",xlim=(15,85),ylim=(0,.175));legend(a,2)
    save(f,out,"36-sampling-distribution-concept.svg")

    f,a=chart("Phân phối chi bình phương","Bậc tự do thay đổi hình dạng của mật độ",rows=2)
    x=np.linspace(0,35,1001)
    for df,c in zip([2,4,8,14],COLORS):a.plot(x,stats.chi2.pdf(x,df),color=c,label=f"df = {df}")
    a.set(xlabel="x",ylabel="Mật độ",xlim=(0,35),ylim=(0,.53));legend(a,2)
    save(f,out,"36-chi-square-pdf-degrees-of-freedom.svg")

    f,a=chart("Student t và chuẩn tắc","Phân phối t có đuôi dày hơn khi bậc tự do nhỏ",rows=1)
    x=np.linspace(-5,5,1001)
    a.plot(x,stats.norm.pdf(x),color=P,label="N(0, 1)")
    for df,c in [(5,T),(2,R)]:a.plot(x,stats.t.pdf(x,df),color=c,label=f"Student t, df = {df}")
    a.set(xlabel="t",ylabel="Mật độ",xlim=(-5,5),ylim=(0,.43));legend(a,3)
    save(f,out,"36-student-t-vs-normal.svg")

    f,axes=panels("Độ chệch và phương sai",["Không chệch, SD = 0.35","Không chệch, SD = 1","Chệch 1.5, SD = 0.35","Chệch 1.5, SD = 1"],2,footer="MSE = Bias² + Var. Vạch đứng là giá trị thật θ = 0.",height=8.4)
    x=np.linspace(-4,4,801)
    for a,(mu,sd),c in zip(axes,[(0,.35),(0,1),(1.5,.35),(1.5,1)],COLORS):
        a.plot(x,stats.norm.pdf(x,mu,sd),color=c);a.axvline(0,color=MUTED,ls="--",lw=1.2)
        a.set(xlim=(-4,4),ylim=(0,1.25),xlabel="Ước lượng",ylabel="Mật độ",xticks=[-3,0,3],yticks=[0,.6,1.2])
    save(f,out,"37-bias-variance-mse-tradeoff.svg")

    f,a=chart("Hợp lý cực đại cho mẫu Bernoulli","n = 10, có 7 thành công: ℓ(p) = 7 ln p + 3 ln(1 − p)",footer="Cực đại tại p̂ = 0.7, với ℓ′(0.7) = 0 và ℓ″(p) < 0 trên (0, 1).")
    p=np.linspace(.01,.99,1001);a.plot(p,7*np.log(p)+3*np.log1p(-p),color=P,label="Log hợp lý ℓ(p)")
    a.axvline(.7,color=T,ls="--",label="MLE p̂ = 0.7");a.scatter([.7],[7*np.log(.7)+3*np.log(.3)],color=T,s=40,edgecolors="none")
    a.set(xlabel="Xác suất p",ylabel="Log hợp lý",xlim=(0,1),ylim=(-34,-4));legend(a,2)
    save(f,out,"37-mle-log-likelihood-concavity.svg")

    f,a=chart("MLE của cận trên phân phối đều","Mẫu từ U(0, θ), n = 3, giá trị lớn nhất bằng 8.5",rows=2,footer="Hàm hợp lý bằng 0 khi θ < 8.5 và giảm theo θ khi θ ≥ 8.5.")
    th=np.linspace(8.5,16,601)
    a.plot([5,8.5],[0,0],color=R,lw=3,label="θ < 8.5: Không phù hợp mẫu")
    a.plot(th,(8.5/th)**3,color=P,label="Hợp lý tương đối (8.5/θ)³")
    a.scatter([8.5],[1],color=T,s=45,edgecolors="none",zorder=4)
    a.plot([8.5,8.5],[0,1],ls=":",color=T,lw=1)
    a.set(xlabel="Cận trên θ",ylabel="Hợp lý tương đối",xlim=(5,16),ylim=(-.03,1.12),xticks=[5,8.5,12,16]);legend(a)
    save(f,out,"37-uniform-mle-boundary.svg")

    d=Diagram("Tiêu chuẩn phân tích nhân tử Fisher–Neyman","Tính đủ được phát biểu trong mô hình có tham số cố định θ",430)
    d.rect(28,105,196,135,fill="white",stroke=P)
    d.lines(126,140,["Mẫu quan sát x","x = (x₁, …, xₙ)","Thống kê T(x)"],anchor="middle",step=36)
    d.arrow(238,172,291,172,T)
    d.rect(306,105,386,135)
    d.lines(499,140,["fθ(x) = gθ(T(x)) h(x)","h(x) không chứa θ","θ xuất hiện qua T(x) trong gθ"],anchor="middle",step=36)
    d.rect(28,281,664,111,fill="white",stroke=T)
    d.lines(360,313,["Luật của X khi biết T(X) không phụ thuộc θ.","Ví dụ Bernoulli: T = X₁ + X₂ + … + Xₙ.","Khi T = t, các cấu hình có t thành công có cùng xác suất."],anchor="middle",step=29)
    d.write(out,"38-fisher-factorization-diagram.svg")

    f,a=chart("Cận Cramér–Rao trong mô hình chuẩn","Xᵢ độc lập từ N(μ, 4), ước lượng không chệch của μ",rows=2,footer="Iₙ(μ) = n/4. Cận 1/Iₙ(μ) = 4/n đạt được bởi trung bình mẫu.")
    n=np.linspace(1,30,601)
    a.plot(n,4/n,color=P,label="Var(X̄) = 4/n: Đạt cận")
    a.plot(n,np.full_like(n,4),color=C,ls="--",label="Var(X₁) = 4: Không dùng hết mẫu")
    a.set(xlabel="Cỡ mẫu n",ylabel="Phương sai",xlim=(1,30),ylim=(0,4.5),xticks=[1,5,10,20,30]);legend(a)
    save(f,out,"38-cramer-rao-lower-bound.svg")

    f,a=chart("Rao–Blackwell giảm phương sai","X₁, …, X₄ độc lập Bernoulli(0.4), T = X₁ + … + X₄",rows=2,footer="E[X₁ | T] = T/4. Var(X₁) = 0.24 = Var(T/4) + 0.18.")
    k=np.arange(5)/4
    a.bar(k-.025,[.6,0,0,0,.4],width=.045,color=C,label="Ước lượng X₁: Var = 0.24")
    a.bar(k+.025,stats.binom.pmf(np.arange(5),4,.4),width=.045,color=P,label="Ước lượng T/4: Var = 0.06")
    a.set(xlabel="Giá trị ước lượng",ylabel="Xác suất",xlim=(-.12,1.12),ylim=(0,.67),xticks=k);legend(a)
    save(f,out,"38-rao-blackwell-variance-reduction.svg")

    f,a=chart("Khoảng tin cậy qua những lần lấy mẫu","20 trung bình độc lập từ N(50, 1.2²), cùng sai số chuẩn 1.2",rows=1,footer=f"Lần mô phỏng này: {int(CI_COVERS.sum())}/20 khoảng chứa μ = 50. Mức tin cậy dài hạn là 95%.",height=7.8)
    for i,(mean,covers) in enumerate(zip(CI_MEANS,CI_COVERS),1):
        color=P if covers else R
        a.plot([mean-CI_MARGIN,mean+CI_MARGIN],[i,i],color=color,lw=2)
        a.scatter([mean],[i],s=19,color=color,edgecolors="none",zorder=3)
    a.axvline(50,color=T,ls="--",lw=1.6,label="Giá trị thật μ = 50")
    a.set(xlabel="Khoảng X̄ ± 1.959964 × 1.2",ylabel="Lần lấy mẫu",ylim=(.3,20.7),yticks=[1,5,10,15,20]);a.grid(False);legend(a)
    save(f,out,"39-confidence-interval-coverage-concept.svg")

    wald,wilson=proportion_intervals()
    f,a=chart("Khoảng Wald và Wilson gần biên","n = 30, k = 2, p̂ = 2/30, mức tin cậy 95%",rows=1,footer=f"Wald: [{wald[0]:.4f}, {wald[1]:.4f}]     Wilson: [{wilson[0]:.4f}, {wilson[1]:.4f}]")
    for y,ends,c in [(2,wald,C),(1,wilson,P)]:
        a.plot(ends,[y,y],color=c,lw=4);a.scatter(ends,[y,y],s=30,color=c,edgecolors="none")
    a.axvline(0,color=R,ls=":",lw=1.5,label="Biên xác suất p = 0")
    a.axvline(2/30,color=T,ls="--",lw=1.5,label="Ước lượng p̂")
    a.set(xlabel="Xác suất p",xlim=(-.06,.26),ylim=(.5,2.5),yticks=[1,2],yticklabels=["Wilson","Wald"]);a.grid(False);legend(a,2)
    save(f,out,"39-wald-vs-wilson-proportion-interval.svg")

    lo,hi=stats.chi2.ppf([.025,.975],9)
    f,a=chart("Hai phân vị chi bình phương cho phương sai","Mẫu chuẩn, n = 10: Pivot 9S²/σ² có phân phối χ² với df = 9",rows=2,footer="Quy ước CDF trái: P(Q ≤ 2.7004) = 0.025, P(Q ≤ 19.0228) = 0.975.")
    x=np.sort(np.r_[np.linspace(0,30,1201),lo,hi]);y=stats.chi2.pdf(x,9)
    a.plot(x,y,color=P,label="Mật độ χ²(9)")
    a.fill_between(x,y,where=(x>=lo)&(x<=hi),color=T,alpha=.18,label="Miền giữa: 95%")
    a.fill_between(x,y,where=(x<=lo)|(x>=hi),color=C,alpha=.45,label="Mỗi đuôi: 2.5%")
    a.set(xlabel="Giá trị pivot Q",ylabel="Mật độ",xlim=(0,30),ylim=(0,.115),xticks=[0,lo,10,hi,30]);a.set_xticklabels(["0","2.700","10","19.023","30"]);legend(a,3)
    save(f,out,"39-chi-square-variance-confidence-interval.svg")

    zc=stats.norm.ppf(.975);pval=2*stats.norm.sf(2.3)
    f,a=chart("Kiểm định z hai phía","Dưới H₀, Z có phân phối N(0, 1). Mức ý nghĩa α = 0.05.",rows=3,footer=f"z quan sát = 2.30. p = P(|Z| ≥ 2.30) = {pval:.4f}.")
    x=np.sort(np.r_[np.linspace(-4,4,1201),-zc,zc,-2.3,2.3]);y=stats.norm.pdf(x)
    a.plot(x,y,color=P,label="Phân phối dưới H₀")
    a.fill_between(x,y,where=np.abs(x)>=zc,color=C,alpha=.25,label="Miền bác bỏ: |Z| ≥ 1.960")
    a.fill_between(x,y,where=np.abs(x)>=2.3,color=R,alpha=.5,label="Hai đuôi tính p: |Z| ≥ 2.30")
    a.axvline(2.3,color=R,ls=":",lw=1.6)
    a.set(xlabel="Thống kê Z",ylabel="Mật độ",xlim=(-4,4),ylim=(0,.43),xticks=[-4,-2,0,2,4]);legend(a)
    save(f,out,"40-hypothesis-test-decision-regions.svg")

    crit=stats.norm.ppf(.95);beta=stats.norm.cdf(crit-2.5)
    f,a=chart("Sai lầm loại I và loại II","Kiểm định một phía: Z ~ N(0, 1) dưới H₀, N(2.5, 1) dưới H₁",rows=2,footer=f"Bác bỏ nếu Z > {crit:.3f}. α = 0.050, β = {beta:.3f}, lực = {1-beta:.3f}.")
    x=np.sort(np.r_[np.linspace(-3.5,6,1001),crit]);y0=stats.norm.pdf(x);y1=stats.norm.pdf(x,2.5)
    a.plot(x,y0,color=P,label="H₀: N(0, 1)");a.plot(x,y1,color=T,label="H₁: N(2.5, 1)")
    a.fill_between(x,y0,where=x>=crit,color=P,alpha=.25,label="α: Bác bỏ khi H₀ đúng")
    a.fill_between(x,y1,where=x<=crit,color=C,alpha=.25,label="β: Không bác bỏ dưới H₁")
    a.axvline(crit,color=MUTED,ls="--",lw=1.2)
    a.set(xlabel="Thống kê Z",ylabel="Mật độ",xlim=(-3.5,6),ylim=(0,.43));legend(a,2)
    save(f,out,"40-type-i-type-ii-power-tradeoff.svg")

    f,a=chart("Hàm lực của kiểm định trung bình một phía","Mẫu chuẩn, biết σ = 1. H₀: μ = 0. H₁: μ > 0. α = 0.05.",rows=1,footer="Lực tại μ = 0 bằng 0.05. Với μ > 0, cỡ mẫu lớn hơn cho lực cao hơn.")
    mu=np.linspace(-.5,1.5,801)
    for n,c in [(9,P),(25,T)]:a.plot(mu,stats.norm.sf(crit-np.sqrt(n)*mu),color=c,label=f"n = {n}")
    a.set(xlabel="Trung bình thật μ",ylabel="Xác suất bác bỏ H₀",xlim=(-.5,1.5),ylim=(0,1.04));legend(a,2)
    save(f,out,"40-power-function-curve.svg")

    obs=np.array([85,30,15,70]);exp=np.array([80,35,15,70]);chi=((obs-exp)**2/exp).sum()
    f,a=chart("Kiểm định chi bình phương về độ phù hợp","Mô hình minh họa với bốn nhóm, tổng số quan sát 200",footer=f"χ² = {chi:.4f}. Nếu các xác suất đã được chỉ định: df = 4 − 1 = 3.")
    k=np.arange(4);a.bar(k-.19,obs,width=.36,color=P,label="Quan sát O");a.bar(k+.19,exp,width=.36,color=T,label="Kỳ vọng E")
    a.set(xlabel="Nhóm",ylabel="Tần số",xticks=k,xticklabels=["A","B","AB","O"],ylim=(0,95));legend(a,2)
    save(f,out,"41-chi-square-goodness-of-fit-bars.svg")

    d=Diagram("Tần số kỳ vọng khi hai thuộc tính độc lập","Eᵢⱼ = RᵢCⱼ/N. Ví dụ bảng 2 × 3 với N = 120.",405)
    rows=[["","Cột 1","Cột 2","Cột 3","Tổng"],["Hàng 1","20 (25)","30 (20)","10 (15)","60"],["Hàng 2","30 (25)","10 (20)","20 (15)","60"],["Tổng","50","40","30","120"]]
    for j,row in enumerate(rows):
        d.rect(28,92+j*54,664,50,fill=PALETTE["canvas"] if j in [0,3] else "white")
        for i,label in enumerate(row):d.text(90+i*132,123+j*54,label,anchor="middle",weight=600 if j in [0,3] else 400)
    d.lines(360,341,["Ô dữ liệu: Quan sát (kỳ vọng). E₁₁ = 60 × 50 / 120 = 25.","Khi cố định tổng biên: df = (2 − 1)(3 − 1) = 2."],anchor="middle",color=MUTED,step=29)
    d.write(out,"41-contingency-table-independence-flow.svg")

    d=Diagram("Khi xấp xỉ chi bình phương chưa phù hợp","Xem tần số kỳ vọng và thiết kế lấy mẫu trước khi chọn cách tính p.",455)
    d.rect(28,91,664,79,stroke=P)
    d.lines(360,121,["Hướng dẫn kinh nghiệm: Tránh E < 1, hạn chế số ô E < 5.","Đây là hướng dẫn cho xấp xỉ χ², không phải điều kiện phổ quát."],anchor="middle",step=28)
    d.arrow(210,183,210,218,T);d.arrow(510,183,510,218,C)
    d.rect(28,233,310,130,fill="white",stroke=T);d.rect(362,233,330,130,fill="white",stroke=C)
    d.lines(183,265,["Bảng liên hợp 2 × 2","Có thể dùng Fisher chính xác","khi mô hình lấy mẫu phù hợp."],anchor="middle",step=32)
    d.lines(527,265,["Độ phù hợp hoặc bảng khác","Dùng cách chính xác phù hợp","hoặc mô phỏng theo H₀."],anchor="middle",step=32)
    d.text(360,412,"Gộp nhóm chỉ khi có ý nghĩa và đã xác định trước khi xem kết quả.",anchor="middle",color=MUTED,size=14)
    d.write(out,"41-cochran-rule-and-fisher-exact.svg")

    d=Diagram("Phân rã biến thiên trong ANOVA một nhân tố","Ví dụ ba nhóm: (2, 3, 4), (4, 5, 6), (6, 7, 8)",447)
    d.rect(148,88,424,65,stroke=P);d.lines(360,114,["SST = 30, df = N − 1 = 8","Biến thiên toàn phần"],anchor="middle",step=25)
    d.arrow(260,166,210,203,T);d.arrow(460,166,510,203,C)
    d.rect(28,218,310,100,fill="white",stroke=T);d.rect(362,218,330,100,fill="white",stroke=C)
    d.lines(183,248,["SSB = 24, df = k − 1 = 2","MSB = 24/2 = 12","Biến thiên giữa các nhóm"],anchor="middle",step=25)
    d.lines(527,248,["SSW = 6, df = N − k = 6","MSW = 6/6 = 1","Biến thiên trong nhóm"],anchor="middle",step=25)
    d.lines(360,365,["SST = SSB + SSW và F = MSB/MSW = 12.","Quyết định kiểm định bằng phân phối F dưới H₀ và mức α đã chọn."],anchor="middle",step=31)
    d.write(out,"42-anova-variance-decomposition.svg")

    critf=stats.f.ppf(.95,3,20);fobs=4.5
    f,a=chart("Miền bác bỏ của kiểm định ANOVA","Dưới H₀, thống kê có phân phối F với df₁ = 3, df₂ = 20",rows=3,footer=f"α = 0.05, ngưỡng = {critf:.4f}. Ví dụ F quan sát = 4.5, p = {stats.f.sf(fobs,3,20):.4f}.")
    x=np.sort(np.r_[np.linspace(0,8,1201),critf]);y=stats.f.pdf(x,3,20)
    a.plot(x,y,color=P,label="Mật độ F(3, 20)");a.fill_between(x,y,where=x>=critf,color=R,alpha=.25,label="Đuôi phải: Xác suất 0.05")
    a.axvline(fobs,color=T,ls="--",label="F quan sát = 4.5")
    a.set(xlabel="Thống kê F",ylabel="Mật độ",xlim=(0,8),ylim=(0,.75));legend(a)
    save(f,out,"42-anova-f-distribution-critical-region.svg")

    f,axes=panels("Tương tác giữa hai nhân tố",["Hiệu ứng A giống nhau ở hai mức B","Hiệu ứng A phụ thuộc mức B"],footer="Đây là các trung bình mô hình minh họa. Kết luận thống kê còn cần ước lượng sai số.",height=6.5)
    for a,pairs in zip(axes,[([2,4],[4,6]),([2,6],[6,2])]):
        for y,c,label in zip(pairs,[P,T],["B₁","B₂"]):a.plot([1,2],y,color=c,marker="o",label=label)
        a.set(xlabel="Mức nhân tố A",ylabel="Trung bình đáp ứng",xlim=(.8,2.2),ylim=(1,7),xticks=[1,2],xticklabels=["A₁","A₂"],yticks=[2,4,6])
    handles,labels=axes[0].get_legend_handles_labels()
    f.legend(handles,labels,loc="upper center",bbox_to_anchor=(.5,.90),ncol=2)
    save(f,out,"42-two-way-anova-interaction-plot.svg")

    f,a=chart("Giả thiết chuẩn trong hồi quy","Y | X = x có phân phối N(2 + 0.8x, 0.8²)",rows=1,footer="Phân phối chuẩn được giả thiết có điều kiện theo x. X không cần có phân phối chuẩn.")
    x=np.linspace(0,10,601);a.plot(x,2+.8*x,color=P,label="Trung bình E[Y | X = x] = 2 + 0.8x")
    for x0 in [2,5,8]:
        ys=np.linspace(2+.8*x0-2.8,2+.8*x0+2.8,401);width=stats.norm.pdf(ys,2+.8*x0,.8)*.8
        a.fill_betweenx(ys,x0-width,x0+width,color=T,alpha=.16);a.plot(x0+width,ys,color=T,lw=1.5);a.plot(x0-width,ys,color=T,lw=1.5)
    a.set(xlabel="Biến giải thích x",ylabel="Đáp ứng y",xlim=(0,10),ylim=(0,12));legend(a)
    save(f,out,"43-regression-normality-conditional-spread.svg")

    f,a=chart("Khoảng tin cậy và khoảng dự báo","Khoảng 95% tại từng x, mô hình hồi quy tuyến tính chuẩn",rows=3,footer="n = 15, x̄ = 5, Sxx = 40, s = 0.8, t₀.₉₇₅,₁₃ = 2.1604. Các khoảng có tính điểm.")
    x=np.linspace(1,9,801);yh=2+.8*x;t=stats.t.ppf(.975,13);sem=.8*np.sqrt(1/15+(x-5)**2/40);sep=np.sqrt(.8**2+sem**2)
    a.fill_between(x,yh-t*sep,yh+t*sep,color=C,alpha=.1,label="Dự báo quan sát mới")
    a.plot(x,yh+t*sep,color=C,ls="--");a.plot(x,yh-t*sep,color=C,ls="--")
    a.fill_between(x,yh-t*sem,yh+t*sem,color=T,alpha=.25,label="Tin cậy cho trung bình tại x")
    a.plot(x,yh,color=P,label="Đường hồi quy")
    a.set(xlabel="x",ylabel="y",xlim=(1,9),ylim=(-1,12));legend(a)
    save(f,out,"43-confidence-band-vs-prediction-band.svg")

    f,axes=panels("Chẩn đoán phần dư trong hồi quy",["Phân tán quanh 0","Phương sai thay đổi","Cấu trúc cong còn sót","Đồ thị Q–Q chuẩn"],2,height=8.9)
    rng=np.random.default_rng(SEED);x=np.linspace(0,10,45)
    values=[rng.normal(0,.7,45),rng.normal(0,1,45)*(.15+.15*x),.15*(x-5)**2-1.4+rng.normal(0,.35,45)]
    for a,y,c in zip(axes[:3],values,[P,R,C]):
        a.scatter(x,y,color=c,s=19,alpha=.75,edgecolors="none");a.axhline(0,color=MUTED,lw=1,ls="--")
        a.set(xlabel="Giá trị khớp",ylabel="Phần dư",xticks=[0,5,10],ylim=(-4,4),yticks=[-3,0,3])
    osm,osr=stats.probplot(rng.normal(size=45),fit=False);axes[3].scatter(osm,osr,s=19,color=T,edgecolors="none")
    axes[3].plot([-2.5,2.5],[-2.5,2.5],color=MUTED,lw=1,ls="--")
    axes[3].set(xlabel="Phân vị chuẩn",ylabel="Phân vị phần dư",xticks=[-2,0,2],yticks=[-2,0,2])
    save(f,out,"43-residual-diagnostics-four-plots.svg")

    d=Diagram("Chọn kiểm định theo câu hỏi và thiết kế","Xác định đại lượng cần so sánh trước khi xem điều kiện của mô hình.",485)
    d.rect(28,89,664,72,stroke=P);d.lines(360,117,["Cần so sánh trung bình, phân phối hay xác suất thứ tự?","Dữ liệu ghép cặp hay độc lập? Có những điều kiện nào?"],anchor="middle",step=27)
    d.arrow(360,173,360,207,P)
    entries=[("Trung bình",["Kiểm định t hoặc Welch","khi mô hình và thiết kế phù hợp."],P),("Hiệu số ghép cặp",["Wilcoxon hạng dấu cần đối xứng","của phân phối hiệu số."],T),("Hai mẫu độc lập",["Mann–Whitney xét thứ tự/phân phối,","không tự động kiểm định trung vị."],C)]
    for j,(title,lines,c) in enumerate(entries):
        y=222+j*73;d.rect(28,y,664,62,fill="white",stroke=RULE);d.text(46,y+25,title,color=c,weight=600)
        d.lines(284,y+24,lines,step=24,size=14)
    d.text(360,470,"Không dùng kiểm định chuẩn tính như một công tắc tự động giữa t và hạng.",anchor="middle",color=MUTED,size=14)
    d.write(out,"44-parametric-vs-nonparametric-workflow.svg")

    d=Diagram("Xếp hạng có dấu Wilcoxon","Ví dụ các hiệu số: 1.2, −2.5, 4.8, 0. Loại hiệu số bằng 0.",410)
    rows=[["Hiệu số","Trị tuyệt đối","Hạng","Hạng có dấu"],["+1.2","1.2","1","+1"],["−2.5","2.5","2","−2"],["+4.8","4.8","3","+3"]]
    for j,row in enumerate(rows):
        d.rect(28,91+j*49,664,45,fill=PALETTE["canvas"] if j==0 else "white")
        for i,label in enumerate(row):d.text(111+i*166,120+j*49,label,anchor="middle",weight=600 if j==0 else 400)
    d.lines(360,322,["T⁺ = 1 + 3 = 4, T⁻ = 2, W = min(T⁺, T⁻) = 2.","Giả thiết: Phân phối hiệu số liên tục và đối xứng quanh tâm cần kiểm định."],anchor="middle",step=33)
    d.write(out,"44-wilcoxon-signed-rank-concept.svg")

    sample,D,xd,f0,end=ks_details()
    f,a=chart("Khoảng cách Kolmogorov–Smirnov","H₀ được chỉ định hoàn toàn: F₀ là CDF của N(0, 1)",rows=3,footer=f"D = {D:.6f}, đạt tại x = {xd:g} ở giới hạn trái của ECDF.")
    x=np.linspace(-3,3,1201);a.plot(x,stats.norm.cdf(x),color=P,label="CDF chuẩn F₀")
    a.step(np.r_[-3,sample,3],np.r_[0,np.arange(1,6)/5,1],where="post",color=R,label="ECDF Fₙ")
    a.plot([xd,xd],[f0,end],color=T,lw=3,label=f"Khoảng cách lớn nhất D = {D:.4f}")
    a.set(xlabel="x",ylabel="Xác suất tích lũy",xlim=(-3,3),ylim=(-.03,1.05),yticks=[0,.25,.5,.75,1]);legend(a)
    save(f,out,"44-kolmogorov-smirnov-statistic-ecdf.svg")
    print("Generated 27 refined statistics figures.")
