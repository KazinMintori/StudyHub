const binary=(op,left,right)=>({op,left,right})
export function parseFormula(source){
 if(typeof source!=='string'||source.length>500)throw Error('Công thức dài tối đa 500 ký tự.')
 const text=source.replaceAll('⇔','<->').replaceAll('↔','<->').replaceAll('⇒','->').replaceAll('→','->').replaceAll('¬','!').replaceAll('∧','&').replaceAll('∨','|').replaceAll('⊤','TRUE').replaceAll('⊥','FALSE')
 const tokens=[];let pos=0
 while(pos<text.length){
  const m=/^\s*(<->|->|[!~&|()]|[A-Za-z][A-Za-z0-9_]*)/.exec(text.slice(pos))
  if(!m){if(!text.slice(pos).trim())break;throw Error('Ký hiệu không hợp lệ gần vị trí '+(pos+1)+'.')}
  tokens.push(m[1]);pos+=m[0].length
 }
 if(tokens.length>120)throw Error('Công thức có quá nhiều ký hiệu.')
 let i=0,depth=0
 const take=t=>tokens[i]===t?(i++,true):false
 function atom(){
  if(++depth>30)throw Error('Ngoặc lồng quá sâu.')
  let node
  if(take('!')||take('~'))node={op:'not',arg:atom()}
  else if(take('(')){node=iff();if(!take(')'))throw Error('Thiếu dấu đóng ngoặc.')}
  else{const t=tokens[i++];if(!t||!(/^[A-Za-z]/.test(t)))throw Error('Cần một ký hiệu mệnh đề hoặc dấu mở ngoặc.');node=t==='TRUE'||t==='FALSE'?{op:'constant',value:t==='TRUE'}:{op:'atom',name:t}}
  depth--;return node
 }
 function and(){let n=atom();while(take('&'))n=binary('and',n,atom());return n}
 function or(){let n=and();while(take('|'))n=binary('or',n,and());return n}
 function implies(){let n=or();if(take('->'))n=binary('implies',n,implies());return n}
 function iff(){let n=implies();while(take('<->'))n=binary('iff',n,implies());return n}
 const result=iff();if(i!==tokens.length)throw Error('Còn ký hiệu chưa ghép thành công thức.');return result
}
export function formulaSymbols(node){return [...new Set(node.op==='atom'?[node.name]:node.op==='constant'?[]:node.op==='not'?formulaSymbols(node.arg):[...formulaSymbols(node.left),...formulaSymbols(node.right)])].sort()}
export function evaluateFormula(node,model){
 if(node.op==='atom'){if(!(node.name in model))throw Error('Thiếu giá trị cho '+node.name);return Boolean(model[node.name])}
 if(node.op==='constant')return node.value
 if(node.op==='not')return !evaluateFormula(node.arg,model)
 const a=evaluateFormula(node.left,model),b=evaluateFormula(node.right,model)
 return node.op==='and'?a&&b:node.op==='or'?a||b:node.op==='implies'?!a||b:a===b
}
export function formatFormula(n){
 if(n.op==='atom')return n.name
 if(n.op==='constant')return n.value?'⊤':'⊥'
 if(n.op==='not')return '¬'+(n.arg.op==='atom'?formatFormula(n.arg):'('+formatFormula(n.arg)+')')
 return '('+formatFormula(n.left)+' '+{and:'∧',or:'∨',implies:'⇒',iff:'⇔'}[n.op]+' '+formatFormula(n.right)+')'
}
export function allModels(symbols){if(symbols.length>12)throw Error('Tối đa 12 ký hiệu cho phép tính này.');return Array.from({length:2**symbols.length},(_,i)=>Object.fromEntries(symbols.map((s,j)=>[s,Boolean(i&(1<<(symbols.length-j-1)))])))}
export function analyzeKnowledge(sentences,query,maxSymbols=6){
 if(sentences.length>12)throw Error('Tối đa 12 câu trong bộ xem.')
 const kb=sentences.map(parseFormula),q=parseFormula(query),symbols=[...new Set([...kb.flatMap(formulaSymbols),...formulaSymbols(q)])].sort()
 if(symbols.length>maxSymbols)throw Error('Bộ bảng chân lý hỗ trợ tối đa '+maxSymbols+' ký hiệu.')
 const rows=allModels(symbols).map(model=>{const values=kb.map(n=>evaluateFormula(n,model)),k=values.every(Boolean),v=evaluateFormula(q,model);return {model,values,kb:k,query:v,counter:k&&!v}})
 const models=rows.filter(r=>r.kb),entails=!rows.some(r=>r.counter),entailsNegation=models.every(r=>!r.query)
 return {symbols,rows,modelCount:models.length,consistent:models.length>0,entails,entailsNegation,status:!models.length?'inconsistent':entails?'entailed':entailsNegation?'negated':'unknown'}
}
export const modelExamples=[
 {id:'rain',title:'Mưa và đường ướt',kb:['P','P -> Q'],query:'Q'},
 {id:'models',title:'Hai mô hình, một hệ quả',kb:['A','B -> C','A -> (B | C)'],query:'C'},
 {id:'unknown',title:'Chưa suy ra được B hoặc phủ định B',kb:['A','B -> C','A -> (B | C)'],query:'B'},
 {id:'converse',title:'Không được đảo chiều kéo theo',kb:['P -> Q','Q'],query:'P'},
 {id:'inconsistent',title:'Tri thức mâu thuẫn',kb:['P','!P'],query:'Q'},
 {id:'negated',title:'Truy vấn bị phủ định',kb:['!P'],query:'P'}
]
export function eliminateArrows(n){
 if(['atom','constant'].includes(n.op))return n
 if(n.op==='not')return {op:'not',arg:eliminateArrows(n.arg)}
 const a=eliminateArrows(n.left),b=eliminateArrows(n.right)
 if(n.op==='implies')return binary('or',{op:'not',arg:a},b)
 if(n.op==='iff')return binary('and',binary('or',{op:'not',arg:a},b),binary('or',{op:'not',arg:b},a))
 return binary(n.op,a,b)
}
export function negationNormal(n,negative=false,budget={nodes:0}){
 if(++budget.nodes>2048)throw Error('Phép biến đổi mở rộng quá lớn. Hãy dùng công thức ngắn hơn trong bộ xem.')
 if(n.op==='constant')return {op:'constant',value:negative?!n.value:n.value}
 if(n.op==='atom')return negative?{op:'not',arg:n}:n
 if(n.op==='not')return negationNormal(n.arg,!negative,budget)
 const op=negative?(n.op==='and'?'or':'and'):n.op
 return binary(op,negationNormal(n.left,negative,budget),negationNormal(n.right,negative,budget))
}
export const negateLiteral=x=>x.startsWith('!')?x.slice(1):'!'+x
export function normalizeClause(clause){const c=[...new Set(clause)].sort();return c.some(x=>c.includes(negateLiteral(x)))?null:c}
export function normalizeCnf(clauses){const map=new Map();for(const c of clauses){const n=normalizeClause(c);if(n)map.set(n.join('|'),n)}return [...map.values()]}
export function cnfText(clauses){return !clauses.length?'⊤':clauses.map(c=>c.length?'('+c.map(l=>l.replace('!','¬')).join(' ∨ ')+')':'□').join(' ∧ ')}
export function convertCnf(source){
 const original=parseFormula(source),symbols=formulaSymbols(original)
 if(symbols.length>6)throw Error('Bộ chuyển CNF hỗ trợ tối đa 6 ký hiệu.')
 const eliminated=eliminateArrows(original),nnf=negationNormal(eliminated)
 function clauses(n){
  if(n.op==='constant')return n.value?[]:[[]]
  if(n.op==='atom')return [[n.name]]
  if(n.op==='not')return [['!'+n.arg.name]]
  const a=clauses(n.left),b=clauses(n.right)
  if(n.op==='and')return normalizeCnf([...a,...b])
  if(a.length*b.length>128)throw Error('Phân phối tạo quá nhiều clause, hãy dùng ví dụ nhỏ hơn.')
  return normalizeCnf(a.flatMap(x=>b.map(y=>[...x,...y])))
 }
 const cnf=clauses(nnf)
 const rows=allModels(symbols).map(model=>({model,before:evaluateFormula(original,model),after:cnf.every(c=>c.some(l=>l.startsWith('!')?!model[l.slice(1)]:model[l]))}))
 return {symbols,original,eliminated,nnf,clauses:cnf,rows,equivalent:rows.every(r=>r.before===r.after),steps:[{label:'Công thức ban đầu',text:formatFormula(original)},{label:'Khử tương đương và kéo theo',text:formatFormula(eliminated)},{label:'Đẩy phủ định tới ký hiệu',text:formatFormula(nnf)},{label:'Phân phối, bỏ lặp và clause hằng đúng',text:cnfText(cnf)}]}
}
