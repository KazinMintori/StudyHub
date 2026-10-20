"""Twenty-four exact probability figures for lessons 28–35."""
import math
import numpy as np
from scipy import integrate, stats
from xstk_refined_common import *

def verify_probability_math():
    assert math.comb(9,3)==84 and math.comb(13,3)==286
    assert sum([30,20,15,15,10,5,10,15])==120
    assert 65+50+40-25-20-15+10==105
    assert math.isclose(1-(45/60)**2,7/16)
    assert np.allclose([stats.geom.mean(.2),stats.geom.mean(.5)],[5,2])
    assert np.allclose([stats.nbinom.mean(3,.4),stats.nbinom.mean(5,.4)],[4.5,7.5])
    assert np.allclose(np.array([.5,.3,.2])@np.array([[140,330],[540,330],[340,100]]),[300,284])
    assert np.allclose(stats.expon.sf([2,5],scale=2),np.exp(-.5*np.array([2,5])))
    f=lambda x,y:6/5*(x+2*y)
    assert math.isclose(integrate.dblquad(f,0,1,lambda y:0,lambda y:y)[0],1)
    for x in np.linspace(0,1,9):
        assert math.isclose(integrate.quad(lambda y:f(x,y),x,1)[0],6/5*(1+x-2*x*x),abs_tol=1e-12)
    assert math.isclose(integrate.quad(lambda x:1+.625*x,0,.8)[0],1)
    u=np.linspace(-1,1,101);assert abs(np.corrcoef(u,u*u)[0,1])<1e-12
    assert math.isclose(integrate.quad(lambda z:min(z,2-z),0,2)[0],1)
    for order in (1,2,3):assert math.isclose(integrate.quad(lambda x:stats.beta.pdf(x,order,4-order),0,1)[0],1)
    assert (70/90,100/400)==(7/9,.25)
    assert .5*(1.5**2+4.5**2)==11.25 and 3**2==9
    assert np.allclose([stats.binom.pmf(50,100,.5),stats.norm.cdf(50.5,50,5)-stats.norm.cdf(49.5,50,5)],[.07958923738717877,.07965567455405798])
    # Characteristic functions verify Cauchy stability for averages.
    for n in (1,4,16):assert np.allclose(np.exp(-np.abs(u)/n)**n,np.exp(-np.abs(u)))
    print("PASS: Probability support, normalization, moments, transformations and numerical labels.")

def generate_all_probability_figures(out):
    out.mkdir(parents=True,exist_ok=True)
    d=Diagram("Vách ngăn Euler","10 phần thưởng giống nhau, 4 người nhận",340)
    for i in range(13):
        x=66+43*i
        if i in (2,6,8):d.rect(x-3,95,6,42,C,C,3)
        else:d.circle(x,116,11)
    for x,label in [(87,"2 phần"),(238,"3 phần"),(367,"1 phần"),(518,"4 phần")]:d.text(x,168,label,anchor="middle",color=P)
    d.rect(28,201,664,106)
    d.lines(48,230,["Mỗi người nhận ít nhất 1: C(9, 3) = 84 cách","Cho phép không nhận: C(13, 3) = 286 cách"],step=40)
    d.write(out,"hinh-28-1-stars-and-bars.svg")

    d=Diagram("Ba biến cố và nguyên lý bù trừ","Mỗi số nằm trong đúng một miền rời nhau",470)
    d.rect(28,82,664,350,fill="white")
    for x,y,c in [(265,210,P),(425,210,T),(345,310,C)]:d.circle(x,y,112,c,c,.10)
    d.text(48,109,"A: Python (65)",color=P);d.text(480,109,"B: C++ (50)",color=T)
    d.text(345,451,"C: Java (40)",anchor="middle",color=C)
    for x,y,n in [(208,206,30),(482,206,20),(345,380,15),(345,169,15),(265,296,10),(425,296,5),(345,249,10)]:d.text(x,y,n,anchor="middle",weight=600)
    d.text(48,402,"Ngoài cả ba: 15",color=MUTED)
    d.text(360,75,"|A ∪ B ∪ C| = 105 trong 120 người",anchor="middle",color=MUTED)
    d.write(out,"hinh-28-2-venn-ba-bien-co.svg")

    f,a=chart("Xác suất hình học của cuộc gặp","Hai thời điểm đến độc lập, đều trên [0, 60] phút",footer="Gặp khi |x − y| ≤ 15. Diện tích thuận lợi / 3600 = 7/16.")
    x=np.linspace(0,60,601)
    a.fill_between(x,np.maximum(0,x-15),np.minimum(60,x+15),color=T,alpha=.2,label="Miền gặp nhau")
    a.plot(x,np.maximum(0,x-15),color=T);a.plot(x,np.minimum(60,x+15),color=T)
    a.set(xlim=(0,60),ylim=(0,60),xlabel="Người thứ nhất đến x (phút)",ylabel="Người thứ hai đến y (phút)",xticks=[0,15,30,45,60],yticks=[0,15,30,45,60]);legend(a)
    save(f,out,"hinh-28-3-xac-suat-hinh-hoc-gap-go.svg")

    f,a=chart("Phân phối hình học","X là số phép thử đến thành công đầu tiên")
    k=np.arange(1,11)
    for p,shift,c in [(.2,-.18,P),(.5,.18,C)]:a.bar(k+shift,stats.geom.pmf(k,p),width=.34,color=c,label=f"p = {p}: E[X] = {1/p:g}")
    a.set(xlabel="Số phép thử k",ylabel="Xác suất P(X = k)",xticks=k,ylim=(0,.56));legend(a,2)
    save(f,out,"hinh-29-1-geometric-distributions.svg")

    f,a=chart("Phân phối nhị thức âm","Y là số thất bại trước thành công thứ r",rows=2)
    k=np.arange(0,19)
    for r,shift,c in [(3,-.18,T),(5,.18,P)]:a.bar(k+shift,stats.nbinom.pmf(k,r,.4),width=.34,color=c,label=f"r = {r}, p = 0.4: E[Y] = {r*.6/.4:g}")
    a.set(xlabel="Số lần thất bại y",ylabel="Xác suất P(Y = y)",xticks=np.arange(0,19,3),ylim=(0,.16));legend(a)
    save(f,out,"hinh-29-2-negative-binomial-pmf.svg")

    d=Diagram("Simplex xác suất","p₁ + p₂ + p₃ = 1 và mọi pᵢ ≥ 0",420)
    d.polygon([(140,330),(540,330),(340,100)],PALETTE["canvas"],P)
    for x,y,label in [(340,85,"(0, 0, 1)"),(140,361,"(1, 0, 0)"),(540,361,"(0, 1, 0)")]:d.text(x,y,label,anchor="middle",color=P)
    d.circle(300,284,6,C);d.text(300,259,"p = (0.5, 0.3, 0.2)",anchor="middle",color=C)
    d.text(360,402,"Trong tam giác: Ba xác suất dương. Trên cạnh: Có xác suất bằng 0.",size=14,anchor="middle",color=MUTED)
    d.write(out,"hinh-29-3-multinomial-simplex.svg")

    f,a=chart("Phân phối mũ và tính không nhớ","X có cường độ λ = 0.5/phút",rows=2,footer="P(X > 5 | X > 3) = P(X > 2) = e⁻¹ ≈ 0.368")
    x=np.linspace(0,12,601);y=stats.expon.pdf(x,scale=2)
    a.plot(x,y,color=P,label="Mật độ f(x) = 0.5 exp(−0.5x)")
    a.fill_between(x,y,where=x>=2,color=T,alpha=.2,label="Đuôi X > 2: 0.368")
    a.fill_between(x,y,where=x>=5,color=C,alpha=.5,label="Đuôi X > 5: 0.082")
    a.set(xlabel="Thời gian chờ x (phút)",ylabel="Mật độ",xlim=(0,12),ylim=(0,.54));legend(a,2)
    save(f,out,"hinh-30-1-exponential-memoryless.svg")

    f,a=chart("Họ phân phối Gamma","β là cường độ, giữ β = 1")
    x=np.linspace(0,12,601)
    for alpha,c,ls in [(1,C,"--"),(2,P,"-"),(5,T,"-")]:a.plot(x,stats.gamma.pdf(x,alpha),color=c,ls=ls,label=f"α = {alpha}, β = 1")
    a.set(xlabel="x",ylabel="Mật độ",xlim=(0,12),ylim=(0,1.05));legend(a,3)
    save(f,out,"hinh-30-2-gamma-distribution-family.svg")

    f,a=chart("Các hình dạng của phân phối Beta","Mọi phân phối có miền xác định [0, 1]",rows=2,footer="Beta(0.5, 0.5) tiến ra vô cùng tại hai biên.")
    x=np.linspace(.001,.999,1001)
    for aa,bb,c,ls in [(.5,.5,MUTED,":"),(2,2,P,"-"),(2,5,T,"-"),(5,2,C,"-")]:a.plot(x,stats.beta.pdf(x,aa,bb),color=c,ls=ls,label=f"Beta({aa:g}, {bb:g})")
    a.set(xlabel="x",ylabel="Mật độ",xlim=(0,1),ylim=(0,3.2));legend(a,2)
    save(f,out,"hinh-30-3-beta-distribution-shapes.svg")

    d=Diagram("Phân phối đồng thời rời rạc","Ô cuối mỗi hàng và cột biểu diễn phân phối lề",390)
    prob=np.array([[.40,.10],[.20,.10],[.10,.10]])
    for i,label in enumerate(["Y / X","0","1","P(Y = y)"]):d.text(111+i*166,108,label,anchor="middle",weight=600)
    for j,row in enumerate(prob):
        d.rect(28,125+j*48,664,44,fill=PALETTE["canvas"] if j%2==0 else "white")
        for i,label in enumerate([str(j)]+[f"{v:.2f}" for v in row]+[f"{sum(row):.2f}"]):d.text(111+i*166,153+j*48,label,anchor="middle",color=T if i==3 else INK)
    for i,label in enumerate(["P(X = x)"]+[f"{v:.2f}" for v in prob.sum(axis=0)]+["1.00"]):d.text(111+i*166,310,label,anchor="middle",weight=600,color=P)
    d.text(360,367,"Tổng các xác suất = 1",anchor="middle",color=MUTED)
    d.write(out,"hinh-31-1-discrete-joint-pmf.svg")

    f,a=chart("Miền xác định của mật độ đồng thời","f(x, y) = (6/5)(x + 2y) khi 0 < x < y < 1")
    x=np.linspace(0,1,501)
    a.fill_between(x,x,1,color=T,alpha=.2,label="Miền 0 < x < y < 1");a.plot(x,x,color=P,label="Biên y = x")
    a.set(xlabel="x",ylabel="y",xlim=(0,1),ylim=(0,1.04),xticks=[0,.25,.5,.75,1],yticks=[0,.25,.5,.75,1]);legend(a,2)
    save(f,out,"hinh-31-2-triangular-support-density.svg")

    f,a=chart("Mật độ lề và mật độ có điều kiện","Cùng mô hình f(x, y) = (6/5)(x + 2y)",rows=2)
    x=np.linspace(0,1,601);xx=np.linspace(0,.8,501)
    a.plot(x,6/5*(1+x-2*x*x),color=P,label="fX(x) = (6/5)(1 + x − 2x²)")
    a.plot(xx,1+.625*xx,color=C,label="fX|Y(x | 0.8) = 1 + 0.625x, 0 < x < 0.8")
    a.set(xlabel="x",ylabel="Mật độ",xlim=(0,1.02),ylim=(0,1.7));legend(a)
    save(f,out,"hinh-31-3-conditional-distributions.svg")

    rng=np.random.default_rng(20261020);z=rng.normal(size=55)
    data=[(z,.85*z+np.sqrt(1-.85**2)*rng.normal(size=55)),(z,-.85*z+np.sqrt(1-.85**2)*rng.normal(size=55)),(z,rng.normal(size=55))]
    titles=[f"Tương quan mẫu r = {np.corrcoef(x,y)[0,1]:.2f}" for x,y in data]+["X đều trên [−1, 1], Y = X²"]
    f,axes=panels("Tương quan tuyến tính và phụ thuộc",titles,2,footer="Mô hình đối xứng Y = X² có ρ = 0 nhưng X và Y phụ thuộc.",height=8.5)
    data.append((np.linspace(-1,1,61),np.linspace(-1,1,61)**2))
    for a,(x,y),c in zip(axes,data,COLORS):
        a.scatter(x,y,s=25,color=c,alpha=.7,edgecolors="none");a.set(xlabel="x",ylabel="y");a.locator_params(axis="both",nbins=3)
    save(f,out,"hinh-32-1-covariance-correlation-types.svg")

    d=Diagram("Luật kỳ vọng toàn phần","Y nhận y₁, y₂, y₃ với xác suất pᵢ = P(Y = yᵢ)",405)
    d.rect(28,172,148,66,fill="white",stroke=P);d.text(102,210,"E[X]",anchor="middle",weight=600,color=P,size=19)
    for i,y in enumerate([115,205,295]):
        d.line(176,205,340,y,color=P,width=1.7)
        d.text(265 if i==2 else 286,290 if i==2 else y-18,f"p{['₁','₂','₃'][i]}",anchor="middle",color=T)
        d.rect(340,y-28,352,56);d.text(516,y+6,f"m{['₁','₂','₃'][i]} = E[X | Y = y{['₁','₂','₃'][i]}]",anchor="middle")
    d.text(360,375,"E[X] = m₁p₁ + m₂p₂ + m₃p₃",anchor="middle",color=P,weight=600,size=18)
    d.write(out,"hinh-32-2-total-expectation-tree.svg")

    d=Diagram("Kỳ vọng có điều kiện là phép chiếu","Giả sử E[X²] < ∞. Xét các hàm g(Y) có momen bậc hai hữu hạn.",430)
    d.polygon([(80,321),(220,265),(606,265),(466,321)],PALETTE["canvas"],RULE)
    d.line(180,300,340,130,P,2.6);d.line(180,300,340,300,T,2.6);d.line(340,300,340,130,R,2,"5,5")
    d.line(340,282,358,282,INK);d.line(358,282,358,300,INK);d.circle(340,130,5,P);d.circle(340,300,5,T)
    d.text(340,112,"X",anchor="middle",color=P,weight=600,size=19);d.text(365,209,"X − E[X | Y]",color=R)
    d.text(340,346,"E[X | Y]",anchor="middle",color=T,weight=600);d.text(480,242,"Các hàm g(Y)",color=MUTED)
    d.text(360,395,"E[(X − g(Y))²] ≥ E[(X − E[X | Y])²]",anchor="middle",color=P,size=17)
    d.write(out,"hinh-32-3-mmse-projection.svg")

    f,a=chart("Biến đổi Y = X² bằng hàm phân phối","Y ≤ 2.25 tương đương −1.5 ≤ X ≤ 1.5")
    x=np.linspace(-2.3,2.3,601)
    a.plot(x,x*x,color=P,label="y = x²");a.axhline(2.25,color=C,ls="--",label="Mức y = 2.25");a.axvspan(-1.5,1.5,color=T,alpha=.1,label="Khoảng nghiệm theo x")
    a.set(xlabel="x",ylabel="y",xlim=(-2.3,2.3),ylim=(0,5.5));legend(a,3)
    save(f,out,"hinh-33-1-cdf-transform-parabola.svg")

    f,a=chart("Tổng hai biến đều độc lập","X₁, X₂ độc lập, cùng có phân phối U(0, 1)")
    x=np.linspace(0,2,601);y=np.minimum(x,2-x);a.plot(x,y,color=P,label="Mật độ Z = X₁ + X₂");a.fill_between(x,y,color=P,alpha=.12)
    a.set(xlabel="z",ylabel="Mật độ",xlim=(0,2),ylim=(0,1.12),xticks=[0,.5,1,1.5,2]);legend(a)
    save(f,out,"hinh-33-2-convolution-uniform.svg")

    f,a=chart("Thống kê thứ tự của ba quan sát","Mẫu độc lập cùng phân phối U(0, 1)",rows=3)
    x=np.linspace(0,1,601)
    for order,c,label in [(1,C,"Cực tiểu X₍₁₎: 3(1 − x)²"),(2,T,"Trung vị X₍₂₎: 6x(1 − x)"),(3,P,"Cực đại X₍₃₎: 3x²")]:a.plot(x,stats.beta.pdf(x,order,4-order),color=c,label=label)
    a.set(xlabel="x",ylabel="Mật độ",xlim=(0,1),ylim=(0,3.25));legend(a)
    save(f,out,"hinh-33-3-order-statistics-densities.svg")

    f,a=chart("Hàm sinh momen của N(0, 1)","M(t) = exp(t²/2)",rows=2,footer="M(0) = 1, M′(0) = E[X] = 0, M″(0) = E[X²] = 1")
    x=np.linspace(-1.9,1.9,601);a.plot(x,np.exp(x*x/2),color=P,label="MGF M(t)");a.plot([-1.5,1.5],[1,1],color=C,ls="--",label="Tiếp tuyến tại t = 0")
    a.scatter([0],[1],s=40,color=T,zorder=4,edgecolors="none");a.set(xlabel="t",ylabel="M(t)",xlim=(-2,2),ylim=(0,6.5));legend(a,2)
    save(f,out,"hinh-34-1-mgf-derivatives.svg")

    d=Diagram("Hai cách chặn xác suất đuôi","X ≥ 0, E[X] = 70, SD(X) = 10. Cần chặn P(X ≥ 90).",410)
    for y,title,lines,c,width in [(92,"Markov",["P(X ≥ 90) ≤ 70/90 = 7/9 ≈ 0.778"],P,467),(230,"Chebyshev",["P(X ≥ 90) ≤ P(|X − 70| ≥ 20)","P(|X − 70| ≥ 20) ≤ 100/20² = 0.25"],T,150)]:
        d.text(38,y,title,color=c,weight=600,size=18);d.lines(38,y+29,lines,step=25);by=y+65 if len(lines)==1 else y+88
        d.rect(38,by,600,13,fill=PALETTE["canvas"],stroke="none",radius=5);d.rect(38,by,width,13,fill=c,stroke="none",radius=5)
    d.text(360,390,"Trong ví dụ này, thông tin phương sai cho chặn nhỏ hơn.",anchor="middle",color=MUTED,size=14)
    d.write(out,"hinh-34-2-markov-chebyshev-bounds.svg")

    f,a=chart("Bất đẳng thức Jensen qua dây cung","X nhận 1.5 hoặc 4.5, mỗi giá trị có xác suất 1/2",rows=2,footer="g(E[X]) = 3² = 9 ≤ E[g(X)] = (1.5² + 4.5²)/2 = 11.25")
    x=np.linspace(1,5,601);a.plot(x,x*x,color=P,label="Hàm lồi g(x) = x²");a.plot([1.5,4.5],[2.25,20.25],color=C,ls="--",label="Dây cung")
    a.plot([3,3],[9,11.25],color=R);a.scatter([3,3],[9,11.25],color=[T,C],s=45,edgecolors="none",zorder=4)
    a.set(xlabel="x",ylabel="g(x)",xlim=(1,5),ylim=(0,26));legend(a,2);save(f,out,"hinh-34-3-jensen-inequality-geometric.svg")

    f,a=chart("Trung bình mẫu tập trung quanh kỳ vọng","Mẫu độc lập từ N(10, 4): X̄ₙ có phân phối N(10, 4/n)",rows=2)
    x=np.linspace(4,16,1201)
    for n,c,ls in [(1,MUTED,":"),(5,C,"-"),(20,T,"-"),(100,P,"-")]:a.plot(x,stats.norm.pdf(x,10,2/np.sqrt(n)),color=c,ls=ls,label=f"n = {n}: Var(X̄ₙ) = {4/n:g}")
    a.set(xlabel="Trung bình mẫu X̄ₙ",ylabel="Mật độ",xlim=(4,16),ylim=(0,2.15));legend(a,2);save(f,out,"hinh-35-1-wlln-convergence.svg")

    f,a=chart("Xấp xỉ nhị thức bằng phân phối chuẩn","X có phân phối B(100, 0.5), so với N(50, 25)",rows=2,footer="P(X = 50) = 0.079589. Xấp xỉ P(49.5 < Y < 50.5) = 0.079656.")
    k=np.arange(30,71);x=np.linspace(30,70,801)
    a.bar(k,stats.binom.pmf(k,100,.5),width=.8,color=RULE,label="Xác suất nhị thức");a.bar([50],stats.binom.pmf([50],100,.5),width=1,color=T,alpha=.65,label="Cột k = 50")
    a.plot(x,stats.norm.pdf(x,50,5),color=P,label="Mật độ chuẩn N(50, 25)")
    xx=np.linspace(49.5,50.5,301);a.fill_between(xx,stats.norm.pdf(xx,50,5),color=P,alpha=.3,label="Hiệu chỉnh [49.5, 50.5]")
    a.set(xlabel="Số lần thành công",ylabel="Xác suất / mật độ",xlim=(30,70),ylim=(0,.09));legend(a,2);save(f,out,"hinh-35-2-clt-binomial-continuity-correction.svg")

    f,axes=panels("Trung bình mẫu chuẩn và Cauchy",["Chuẩn N(0, 1/n)","Cauchy chuẩn với mọi n"],footer="Cauchy không có kỳ vọng và phương sai. Trung bình mẫu vẫn có cùng phân phối.",height=6.6)
    x=np.linspace(-4,4,801)
    for n,c,ls in [(1,MUTED,":"),(4,C,"--"),(16,P,"-")]:axes[0].plot(x,stats.norm.pdf(x,0,1/np.sqrt(n)),color=c,ls=ls,label=f"n = {n}")
    axes[1].plot(x,stats.cauchy.pdf(x),color=R,label="Mọi n ≥ 1")
    for a in axes:a.set(xlabel="X̄ₙ",ylabel="Mật độ",xlim=(-4,4),ylim=(0,1.75),xticks=[-4,0,4],yticks=[0,.8,1.6])
    handles,labels=axes[0].get_legend_handles_labels()
    f.legend(handles,labels,loc="upper center",bbox_to_anchor=(.5,.90),ncol=3)
    save(f,out,"hinh-35-3-cauchy-vs-normal-averages.svg")
    print("Generated 24 refined probability figures.")
