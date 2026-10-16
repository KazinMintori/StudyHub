from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'axes.labelsize':14,'axes.titlesize':16,'xtick.labelsize':14,'ytick.labelsize':14,'legend.fontsize':14,'svg.fonttype':'none','svg.hashsalt':'StudyHub-final-exercises'})
def graph(ch,i,title,xlabel,ylabel):
 fig,ax=plt.subplots(figsize=(8.6,5.4));ax.set_title(title,pad=18);ax.set_xlabel(xlabel,labelpad=12);ax.set_ylabel(ylabel,labelpad=12);ax.grid(alpha=.2)
 return fig,ax
def save(ch,i,fig):
 out=ROOT/f'docs/vat-ly-2/bai-giang/img/young-{ch}';out.mkdir(parents=True,exist_ok=True)
 fig.tight_layout(pad=1.8);p=out/f'loi-giai-c-{i:02}.svg';fig.savefig(p,bbox_inches='tight',pad_inches=.25,facecolor='white',metadata={'Date':None});plt.close(fig)
 p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
import pymupdf as fitz
CROPS={'hinh-tham-chieu-c-1':(1467,(75,75,575,430)),'hinh-tham-chieu-c-2':(1469,(350,84,615,275)),'hinh-tham-chieu-c-3':(1478,(250,60,525,495))}
SCALE=3
def main():
 with fitz.open(ROOT/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
  for name,(page,rect) in CROPS.items():pdf[page-1].get_pixmap(matrix=fitz.Matrix(SCALE,SCALE),clip=fitz.Rect(rect),alpha=False).save(ROOT/f'docs/vat-ly-2/bai-giang/img/young-43/{name}.png')
 fig,ax=graph(43,1,'Hai mức spin proton trong từ trường','Từ trường B (T)','Năng lượng tương tác (neV)')
 B=np.linspace(0,.65,100);mu=1.4106e-26/1.602176634e-19*1e9
 ax.plot(B,mu*B,label='Spin đối song: Năng lượng tăng');ax.plot(B,-mu*B,label='Spin song song: Năng lượng giảm');ax.axvline(.5331,color='#64748b',ls='--',label='Cộng hưởng ở 22,7 MHz');ax.legend();save(43,1,fig)
 fig,ax=graph(43,2,'Năng lượng liên kết hai hạt nhân gương','Hạt nhân','Năng lượng liên kết (MeV)')
 ax.bar(['Bo-11 (5 proton)','Cacbon-11 (6 proton)'],[76.2055,73.4399],color=['#2563eb','#dc2626']);ax.set_ylim(0,90)
 for j,v in enumerate([76.2055,73.4399]):ax.text(j,v+2,f'{v:.3f}',ha='center')
 save(43,2,fig)
 fig,ax=graph(43,3,'Năng lượng liên kết của cacbon và ba hạt alpha','Trạng thái','Năng lượng liên kết (MeV)')
 ax.bar(['Ba alpha riêng rẽ','Hạt nhân cacbon-12'],[84.888,92.162],color=['#64748b','#2563eb']);ax.set_ylim(0,110)
 for j,v in enumerate([84.888,92.162]):ax.text(j,v+2,f'{v:.3f}',ha='center')
 save(43,3,fig)
 fig,ax=graph(43,4,'Phân chia năng lượng khi urani-238 phân rã alpha','Sản phẩm','Động năng (MeV)')
 Q=(238.050788-234.043601-4.002603)*931.494;ka=Q*234.043601/(234.043601+4.002603)
 ax.bar(['Hạt alpha','Thori-234 giật lùi'],[ka,Q-ka],color=['#dc2626','#2563eb']);ax.set_ylim(0,5)
 for j,v in enumerate([ka,Q-ka]):ax.text(j,v+.1,f'{v:.4f}',ha='center')
 save(43,4,fig)
 fig,ax=graph(43,5,'Phổ beta: Hình dạng minh họa định tính','Động năng electron chia năng lượng khả dụng','Mật độ tương đối, đã chuẩn hóa')
 x=np.linspace(0,1,300);y=x**1.5*(1-x)**2;y/=y.max();ax.plot(x,y);ax.text(.5,.7,'Bỏ qua giật lùi',ha='center');save(43,5,fig)
 fig,ax=graph(43,6,'Tốc độ phân rã của mẫu cacbon-14','Thời gian (năm)','Số phân rã trên phút')
 t=np.linspace(0,50000,300);ax.semilogy(t,184*2**(-t/5730));ax.scatter([1000,50000],184*2**(-np.array([1000,50000])/5730),color='#dc2626');save(43,6,fig)
 fig,ax=graph(43,7,'Định tuổi mẫu gỗ chứa 500 g cacbon','Tuổi mẫu (năm)','Số phân rã trên phút')
 t=np.linspace(0,20000,300);age=5730/math.log(2)*math.log(7650/2690);ax.plot(t,7650*2**(-t/5730));ax.scatter([age],[2690],color='#dc2626',label=f'Mẫu đo: Tuổi khoảng {age:.0f} năm');ax.legend();save(43,7,fig)
 fig,ax=graph(43,8,'Ước lượng liên kết bằng mô hình giọt chất lỏng','Hạt nhân','Năng lượng liên kết trên mỗi nuclôn (MeV)')
 ax.bar(['Ruteni-100','Thủy ngân-200'],[868.071527345873/100,1584.4615007212885/200],color=['#2563eb','#059669']);ax.set_ylim(0,10);save(43,8,fig)
if __name__=='__main__':main()
