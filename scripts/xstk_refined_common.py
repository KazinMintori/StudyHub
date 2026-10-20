"""Reserved typography gutters for reproducible classical XSTK figures."""
from io import BytesIO
from html import escape
from pathlib import Path
import re
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from xstk_figure_style import configure_matplotlib, polish_svg, PALETTE
configure_matplotlib()
P,T,C,R=[PALETTE[k] for k in ("primary","teal","copper","alert")]
INK,MUTED,RULE=[PALETTE[k] for k in ("ink","muted","rule")]
COLORS=[P,T,C,R]

def save(fig,directory,filename):
    data=BytesIO();fig.savefig(data,format="svg",metadata={"Date":None});plt.close(fig)
    source=data.getvalue().decode()
    source=re.sub(r'width="[\d.]+pt" height="[\d.]+pt"', 'width="100%" height="auto"', source, count=1)
    (Path(directory)/filename).write_text(polish_svg(source),encoding="utf-8")

def chart(title,subtitle="",rows=1,footer="",height=6.2):
    fig=plt.figure(figsize=(9,height),facecolor="white")
    fig.text(.5,.955,title,ha="center",va="top",fontsize=19,weight=600)
    if subtitle:fig.text(.5,.885,subtitle,ha="center",va="top",fontsize=14,color=MUTED)
    bottom=.28 if footer else .18;top=.75-max(0,rows-1)*.064
    ax=fig.add_axes([.15,bottom,.79,top-bottom]);ax.grid(axis="y",alpha=.32,linewidth=.65)
    ax.set_axisbelow(True);ax.tick_params(length=4,pad=9)
    if footer:fig.text(.5,.045,footer,ha="center",va="bottom",fontsize=14,color=MUTED)
    return fig,ax

def legend(ax,columns=1):
    ax.legend(loc="lower center",bbox_to_anchor=(.5,1.045),ncol=columns,borderaxespad=0,handlelength=2.3,columnspacing=1.7,labelspacing=.6)

def panels(title,subtitles,nrows=1,footer="",height=6.0):
    ncols=len(subtitles)//nrows;fig=plt.figure(figsize=(9,height),facecolor="white")
    fig.text(.5,.965,title,ha="center",va="top",fontsize=19,weight=600)
    axes=[];bottom,top=(.25 if footer else .18),.77;hgap,vgap=.16,.21
    width=(.82-(ncols-1)*hgap)/ncols;hh=(top-bottom-(nrows-1)*vgap)/nrows
    for i,label in enumerate(subtitles):
        row,col=divmod(i,ncols);ax=fig.add_axes([.13+col*(width+hgap),top-(row+1)*hh-row*vgap,width,hh])
        ax.set_title(label,fontsize=14,pad=17);ax.tick_params(pad=8,labelsize=14)
        ax.grid(axis="y",alpha=.25,linewidth=.65);ax.set_axisbelow(True);axes.append(ax)
    if footer:fig.text(.5,.04,footer,ha="center",va="bottom",fontsize=14,color=MUTED)
    return fig,axes

class Diagram:
    def __init__(self,title,subtitle="",height=420):
        self.height=height;self.parts=[f'<rect width="720" height="{height}" fill="white"/>']
        self.text(360,31,title,size=20,weight=600,anchor="middle")
        if subtitle:self.text(360,59,subtitle,size=14,color=MUTED,anchor="middle")
    def text(self,x,y,label,size=15,color=INK,anchor="start",weight=400):
        self.parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}">{escape(str(label))}</text>')
    def lines(self,x,y,labels,step=25,**kwargs):
        for i,label in enumerate(labels):self.text(x,y+i*step,label,**kwargs)
    def rect(self,x,y,width,height,fill=None,stroke=RULE,radius=9):
        self.parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill or PALETTE["canvas"]}" stroke="{stroke}" stroke-width="1.2"/>')
    def line(self,x1,y1,x2,y2,color=RULE,width=1.5,dash=""):
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>')
    def circle(self,x,y,radius,fill=P,stroke="none",opacity=1):
        self.parts.append(f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.6" fill-opacity="{opacity}"/>')
    def polygon(self,points,fill,stroke=RULE,opacity=1):
        self.parts.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.6" fill-opacity="%s"/>'%(' '.join(f'{x},{y}' for x,y in points),fill,stroke,opacity))
    def arrow(self,x1,y1,x2,y2,color=P):
        self.line(x1,y1,x2,y2,color,2);dx,dy=x2-x1,y2-y1;length=np.hypot(dx,dy);ux,uy=dx/length,dy/length
        self.polygon([(x2,y2),(x2-9*ux+4*uy,y2-9*uy-4*ux),(x2-9*ux-4*uy,y2-9*uy+4*ux)],color,"none")
    def write(self,directory,filename):
        source=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 {self.height}" width="100%">'+''.join(self.parts)+'</svg>'
        (Path(directory)/filename).write_text(polish_svg(source),encoding="utf-8")
