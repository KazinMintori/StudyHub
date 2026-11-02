"""Flatten simple graphic CSS for MuPDF's SVG reader, then rasterize.

This intentionally uses a static SVG renderer, not a browser. Browser layout,
CSS fidelity, exact font metrics and inputs remain unverified.
"""
from pathlib import Path
from copy import deepcopy
import json,re,sys
from lxml import html,etree
import tinycss2
import pymupdf

output=Path('qa/math-ai-visuals/static-previews')
def declarations(source):
    return [(d.lower_name,tinycss2.serialize(d.value).strip(),d.important)
            for d in tinycss2.parse_declaration_list(source,skip_comments=True,skip_whitespace=True)
            if d.type=='declaration']

def simple(element,selector):
    if not isinstance(element.tag,str):return False
    if ':' in selector:return False
    tag=re.match(r'^[a-zA-Z][\w-]*',selector)
    if tag and element.tag!=tag.group():return False
    if any(name not in (element.get('class') or '').split() for name in re.findall(r'\.([\w-]+)',selector)):return False
    for attr,value in re.findall(r'\[([\w-]+)(?:=["\']?([^\]"\']+)["\']?)?\]',selector):
        if attr not in element.attrib or value and element.get(attr)!=value:return False
    return True

def matches(element,selector):
    if any(symbol in selector for symbol in [':','+','~']):return False
    pieces=selector.replace('>',' ').split()
    if not pieces or not simple(element,pieces[-1]):return False
    ancestor=element.getparent()
    for part in reversed(pieces[:-1]):
        while ancestor is not None and not simple(ancestor,part):ancestor=ancestor.getparent()
        if ancestor is None:return False
        ancestor=ancestor.getparent()
    return True

for name in sys.argv[1:]:
    record=json.loads((output/(name+'.json')).read_text(encoding='utf-8'))
    for dark in [False,True]:
        tokens={}
        for selector in [':root']+(['.dark'] if dark else []):
            block=re.search(re.escape(selector)+r'\s*\{([^}]+)\}',record['tokens']).group(1)
            tokens.update({key:value for key,value,_ in declarations(block) if key.startswith('--')})
        def resolve(value):
            for _ in range(10):
                updated=re.sub(r'var\((--[\w-]+)\)',lambda m:tokens.get(m.group(1),m.group()),value)
                if updated==value:break
                value=updated
            return value
        rules=[]
        for rule in tinycss2.parse_stylesheet(record['css'],skip_comments=True,skip_whitespace=True):
            if rule.type!='qualified-rule':continue
            for selector in tinycss2.serialize(rule.prelude).split(','):
                selector=selector.strip()
                specificity=(len(re.findall(r'\.[\w-]+|\[[^]]+\]',selector)),len(re.findall(r'(?:^|\s)[a-z]+',selector)))
                rules.append((selector,specificity,declarations(tinycss2.serialize(rule.content))))
        doc=html.fragment_fromstring(record['html'],create_parent='div')
        diagrams=doc.xpath('.//svg[not(ancestor::svg)]')
        for index,svg in enumerate(diagrams):
            for element in svg.iter():
                if not isinstance(element.tag,str):continue
                style={}
                for order,(selector,specificity,items) in enumerate(rules):
                    if matches(element,selector):
                        for key,value,important in items:
                            priority=(important,specificity,order)
                            if key not in style or priority>=style[key][0]:style[key]=(priority,resolve(value))
                for key,value,important in declarations(element.get('style','')):
                    style[key]=((important,(1000,0),100000),resolve(value))
                for key,(_,value) in style.items():
                    if key in ['fill','stroke','stroke-width','stroke-dasharray','stroke-linecap','fill-opacity','stroke-opacity','opacity','font-size','font-weight','text-anchor']:
                        normalized=value.replace('!important','').strip()
                        if normalized=='transparent' and key in ['fill','stroke']:normalized='none'
                        element.set(key,normalized)
                    if key=='font':
                        size=re.search(r'([\d.]+)px',value)
                        if size:element.set('font-size',size.group(1))
                if element.tag=='text':element.set('font-family','sans-serif')
                element.attrib.pop('style',None)
                if element.tag=='clippath':element.tag='clipPath'
            svg.set('xmlns','http://www.w3.org/2000/svg')
            svg.set('fill',tokens['ink'] if 'ink' in tokens else tokens['--ink'])
            for width in [294,400]:
                raster=deepcopy(svg)
                _,_,vb_width,vb_height=map(float,raster.get('viewbox',raster.get('viewBox')).split())
                raster.attrib.pop('viewbox',None);raster.set('viewBox',f'0 0 {vb_width:g} {vb_height:g}')
                raster.set('width',str(width));raster.set('height',str(width*vb_height/vb_width))
                background=etree.Element('rect',x='0',y='0',width=str(vb_width),height=str(vb_height),fill=tokens['--paper'])
                raster.insert(0,background)
                data=etree.tostring(raster,encoding='utf-8')
                target=output/f'{name}-{index}-{width}-{ "dark" if dark else "light"}'
                target.with_suffix('.svg').write_bytes(data)
                document=pymupdf.open(stream=data,filetype='svg')
                document[0].get_pixmap().save(target.with_suffix('.png'))
        print(name,'dark' if dark else 'light',len(diagrams),'diagrams: static SVG only')
