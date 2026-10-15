"""Inventory the complete manifest page range; this does not certify source coverage."""
from pathlib import Path
import argparse,re,json
import pymupdf as fitz
root=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser();parser.add_argument('chapter',type=int);args=parser.parse_args()
manifest=json.loads((root/'raw_materials/physics/translation-manifest.json').read_text(encoding='utf-8-sig'))
ch=next(c for c in manifest['chapters'] if c['chapter']==args.chapter)
prefix=str(args.chapter)
pages=[]
with fitz.open(root/'raw_materials/physics/source/young-freedman-15.pdf') as pdf:
 for number in range(ch['pdfStart'],ch['pdfEnd']+1):
  text=pdf[number-1].get_text();pages.append(text)
  target=root/f'qa/physics/full-source/pdf-{number:04d}.txt'
  target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text,encoding='utf-8')
 next_text=pdf[ch['pdfEnd']].get_text() if ch['pdfEnd']<len(pdf) else ''
text='\n'.join(pages)
def find(pattern):
 values=set(re.findall(pattern,text,re.M))
 return sorted(values,key=lambda s:[int(x) for x in re.findall(r'\d+',s)])
examples=find(r'EXAMPLE\s+('+prefix+r'\.\d+)\b')
figures=find(r'Figure\s+('+prefix+r'\.\d+)\b')
problemfigures=find(r'Figure\s+([EP]'+prefix+r'\.\d+)\b')
discussion=find(r'^\s*(Q'+prefix+r'\.\d+)\s')
variation=find(r'^\s*(VP'+prefix+r'\.\d+\.\d+)\s')
exercise_text=text.split('EXERCISES',1)[-1]
exercises=set(re.findall(r'^\s*('+prefix+r'\.\d+)\s',exercise_text,re.M))
exercises=sorted((s for s in exercises if int(s.split('.')[1])>0),key=lambda s:int(s.split('.')[1]))
report={'status':'full-page-range-inventory-only','chapter':args.chapter,'printedPages':[ch['printedStart'],ch['printedEnd']],'pdfPages':[ch['pdfStart'],ch['pdfEnd']],'examples':examples,'numberedFigures':figures,'exerciseFigures':problemfigures,'discussion':discussion,'guidedPractice':variation,'numberedExercises':exercises,'endSolutionsIncludingBridge':len(discussion)+len(variation)+len(exercises)+1,'nextPageStarts':next_text[:150],'humanSourceReviewRequired':True}
out=root/f'qa/physics/chapter{args.chapter}/full-source-inventory.json';out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
