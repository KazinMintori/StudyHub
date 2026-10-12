from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
directories=[ROOT/'raw_materials/physics/translations/chapter-21',ROOT/'raw_materials/physics/solutions/chapter-21']
product=re.compile(r'\((-?\d+(?:\.\d+)?)\\times10\^\{(-?\d+)\}\)\((-?\d+(?:\.\d+)?)\\times10\^\{(-?\d+)\}\)')
for directory in directories:
 for file in directory.glob('*.md'):
  text=file.read_text(encoding='utf8')
  def reduce(m):
   body=m[1]
   body=product.sub(lambda x:'('+x[1]+')('+x[3]+')10^{'+str(int(x[2])+int(x[4]))+'}',body)
   # k was explicitly defined in the lesson; the shorter equivalent leaves room for equation numbers.
   body=body.replace(r'\frac{1}{4\pi\varepsilon_0}', 'k').replace(r'\frac{1}{2\pi\varepsilon_0}','2k')
   body=body.replace(r'F_{\mathrm{nguồn\ lên\ vòng}}','F')
   return '$$'+body+'$$'
  result=re.sub(r'\$\$([\s\S]*?)\$\$',reduce,text)
  file.write_text(result,encoding='utf8')
print('Combined powers in numeric products; used the defined Coulomb constant where equivalent.')
