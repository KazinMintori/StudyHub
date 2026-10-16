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
def main():
 fig,ax=graph(44,1,'Quỹ đạo ion hydro âm trong cyclotron','Tọa độ x (m)','Tọa độ y (m)')
 theta=np.linspace(0,2*np.pi,300);r=1.67e-27*6e6/(1.602176634e-19*.460);ax.plot(r*np.cos(theta),r*np.sin(theta));ax.plot([0,r],[0,0],label=f'Bán kính {r:.3f} m');ax.axis('equal');ax.legend();save(44,1,fig)
 fig,ax=graph(44,2,'Ngưỡng tạo meson eta phẩy bằng bia proton tĩnh','Đại lượng','Năng lượng (MeV)')
 M=938;F=2*M+958;K=(F*F-4*M*M)/(2*M);ax.bar(['Năng lượng khối tâm','Động năng proton tới'],[F,K],color=['#2563eb','#dc2626']);save(44,2,fig)
 fig,ax=graph(44,3,'Tốc độ Doppler và độ dịch chuyển đỏ','Độ dịch chuyển đỏ z','Tỉ số tốc độ với tốc độ ánh sáng')
 z=np.linspace(0,.25,200);beta=((1+z)**2-1)/((1+z)**2+1);ax.plot(z,beta);z0=725/656.3-1;b0=((1+z0)**2-1)/((1+z0)**2+1);ax.scatter([z0],[b0],label='Vạch hydro 656,3 nm chuyển tới 725 nm');ax.legend();save(44,3,fig)
 fig,ax=graph(44,4,'Tạo cặp muon bằng hai photon đối đầu','Năng lượng mỗi photon chia năng lượng nghỉ muon','Tốc độ muon chia tốc độ ánh sáng')
 g=np.linspace(1,3,300);ax.plot(g,np.sqrt(1-1/g**2));ax.scatter([1,2],[0,np.sqrt(.75)],color='#dc2626');save(44,4,fig)
 fig,ax=graph(44,5,'Phân chia động năng khi nơtron chậm bị bắt','Sản phẩm','Động năng (MeV)')
 Q=(1.008665+10.012937-7.016003-4.002603)*931.494;ka=Q*7.016003/(7.016003+4.002603);ax.bar(['Liti-7','Hạt alpha'],[Q-ka,ka],color=['#2563eb','#dc2626']);save(44,5,fig)
 fig,ax=graph(44,6,'Đạt năng lượng khối tâm 2 TeV','Cấu hình chùm hạt','Động năng chùm (TeV), thang logarit')
 ax.bar(['Chùm phản proton, bia tĩnh','Mỗi chùm đối đầu'],[(2000**2-4*.938**2)/(2*.938)/1000,(1000-.938)/1000],color=['#dc2626','#2563eb']);ax.set_yscale('log');save(44,6,fig)
 fig,ax=graph(44,7,'Động lượng positron trong từ trường 0,40 T','Bán kính quỹ đạo (cm)','Động lượng (MeV/c)')
 r=np.linspace(0,.18,100);ax.plot(r*100,.4*r*299.792458);ax.scatter([7.5,15],[.4*.075*299.792458,.4*.15*299.792458],color='#dc2626',label='Hai cách hiểu kích thước 15 cm');ax.legend();save(44,7,fig)
 fig,ax=graph(44,8,'Số lượng tử khi omega âm phân rã yếu','Trạng thái','Độ lạ')
 ax.bar(['Omega âm','Xi âm và pion trung hòa'],[-3,-2],color=['#2563eb','#dc2626']);ax.set_ylim(-3.5,.5);ax.text(.5,.15,'Số baryon giữ nguyên bằng 1',ha='center');save(44,8,fig)
if __name__=='__main__':main()
