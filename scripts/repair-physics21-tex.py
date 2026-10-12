from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
dirs=[ROOT/'raw_materials/physics/translations/chapter-21',ROOT/'raw_materials/physics/solutions/chapter-21']
bs=chr(92)
sep=bs*2+'\n'
commands=['begin','end','tag','times','frac','tfrac','mathrm','mathbf','mathbb','vec','hat','approx','cdot','quad','qquad','int','pi','varepsilon','lambda','sigma','rho','sqrt','sin','cos','tan','Delta','theta','varphi','mu','ln','arctan','kappa','omega','epsilon','le','ge','ll','gg','to','in','ne','pm','left','right','lim','infty','text','sum','dots','cdots','qquad','alpha','beta','gamma','delta','mathcal','tau','circ']
pattern=re.escape(sep)+r'[ \t]*(?=(?:'+ '|'.join(commands)+r')(?![A-Za-z])|[,;!])'
for directory in dirs:
 for file in directory.glob('*.md'):
  text=file.read_text(encoding='utf8')
  def repair(m):
   body=m[1]
   body=re.sub(pattern,lambda _:bs,body)
   body=re.sub(r'(?m)^([ \t]*)('+ '|'.join(commands)+r')(?![A-Za-z])',lambda m:m[1]+bs+m[2],body)
   body=re.sub('(?:'+re.escape(sep)+r'[ \t]*){2,}',lambda _:sep,body)
   body=body.replace('\n'+sep,'\n')
   body=body.replace('&'+sep+'&=',sep+'&=')
   return '$$'+body+'$$'
  result=re.sub(r'\$\$([\s\S]*?)\$\$',repair,text)
  file.write_text(result,encoding='utf8')
print('Restored separated TeX commands and removed empty equation rows.')
