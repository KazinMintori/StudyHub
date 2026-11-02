import {parseAtom,formatAtom,applyAtom,atomVariables,unifyAtoms,formatTheta,standardizeAtoms,renameAtoms} from './predicate-terms.mjs'
const displayFacts = facts => facts.map(formatAtom)
export const predicatePrograms = {
  kings:{title:'Vua tham lam',facts:['King(John)','Greedy(John)','Brother(Richard, John)'],rules:[{head:'Evil(?x)',body:['King(?x)','Greedy(?x)']}],query:'Evil(?z)'},
  students:{title:'Sinh viên và hai câu trả lời',facts:['Student(An)','Student(Binh)','Learns(An, Logic)','Learns(Binh, AI)'],rules:[{head:'Knows(?x, ?m)',body:['Student(?x)','Learns(?x, ?m)']}],query:'Knows(?who, ?what)'},
  shared:{title:'Hai tiền đề phải dùng cùng phép thế',facts:['King(John)','Greedy(Richard)'],rules:[{head:'Evil(?x)',body:['King(?x)','Greedy(?x)']}],query:'Evil(?z)'},
  backtrack:{title:'Nhánh đầu quay lui rồi tìm sự thực',facts:['Base(An)'],rules:[{head:'Good(?x)',body:['Missing(?x)']},{head:'Good(?x)',body:['Base(?x)']}],query:'Good(?z)'},
  cycle:{title:'Đệ quy đứng trước sự thực',facts:['Base(An)'],rules:[{head:'Good(?x)',body:['Good(?x)']},{head:'Good(?x)',body:['Base(?x)']}],query:'Good(?z)'},
  growing:{title:'Hàm tạo vô hạn hạng thức',facts:['P(A)'],rules:[{head:'P(f(?x))',body:['P(?x)']}],query:'Q(A)'}
}
export function validateProgram(input) {
  if (!input || !Array.isArray(input.facts) || !Array.isArray(input.rules) || input.facts.length>30 || input.rules.length>20) throw Error('Tối đa 30 sự thực và 20 luật khẳng định.')
  const facts=input.facts.map(parseAtom),rules=input.rules.map((r,i)=>{
    if(!r||!Array.isArray(r.body)||!r.body.length||r.body.length>5)throw Error('Mỗi luật có 1 đến 5 tiền đề. Viết sự thực trong facts.')
    const head=parseAtom(r.head),body=r.body.map(parseAtom),variables=new Set(body.flatMap(atomVariables))
    if(atomVariables(head).some(v=>!variables.has(v)))throw Error('Mọi biến ở đầu luật phải xuất hiện trong thân luật của bộ xem hữu hạn này.')
    return {head,body,id:i+1}
  }),query=parseAtom(input.query)
  if(facts.some(f=>atomVariables(f).length))throw Error('Sự thực đầu vào phải nền. Luật và truy vấn được chứa biến ?x.')
  const arities=new Map()
  for(const a of [...facts,query,...rules.flatMap(r=>[r.head,...r.body])]){if(arities.has(a.name)&&arities.get(a.name)!==a.args.length)throw Error('Một tên vị từ phải có cùng số đối số.');arities.set(a.name,a.args.length)}
  const functionArities=new Map()
  function check(t){if(t.type==='variable')return;const n=t.args?.length||0;if(functionArities.has(t.name)&&functionArities.get(t.name)!==n)throw Error('Một ký hiệu hằng hoặc hàm phải giữ nguyên số đối số.');functionArities.set(t.name,n);for(const arg of t.args||[])check(arg)}
  for(const a of [...facts,query,...rules.flatMap(r=>[r.head,...r.body])])for(const t of a.args)check(t)
  return {facts,rules,query}
}
export function queryAnswers(query, facts) {
  const vars=atomVariables(query),answers=[]
  for(const fact of facts){const theta=unifyAtoms(query,fact);if(theta!==null){const displayed=formatTheta(theta),answer=Object.fromEntries(vars.map(v=>['?'+v,displayed['?'+v]||'?'+v]));if(!answers.some(x=>JSON.stringify(x)===JSON.stringify(answer)))answers.push(answer)}}
  return answers
}
export function* forwardPredicateSteps(input,{maxFacts=60,maxEvents=600}={}) {
  const p=validateProgram(input),facts=[...new Map(p.facts.map(f=>[formatAtom(f),f])).values()]
  let events=0,round=0
  const snap=(phase,extra={})=>({phase,facts:displayFacts(facts),round,answers:queryAnswers(p.query,facts),...extra})
  yield snap('start')
  while(true){
    round++;let changed=false
    for(const rule of p.rules){
      const available=facts.slice()
      function* join(i,theta,parents){
        if(i===rule.body.length){yield {theta,parents};return}
        for(const fact of available){const next=unifyAtoms(rule.body[i],fact,theta);if(next!==null)yield*join(i+1,next,[...parents,formatAtom(fact)])}
      }
      for(const match of join(0,{},[])){
        if(++events>maxEvents||facts.length>=maxFacts){yield snap('budget');return}
        const head=applyAtom(rule.head,match.theta)
        yield snap('match',{rule:rule.id,theta:formatTheta(match.theta),parents:match.parents,head:formatAtom(head)})
        if(!facts.some(f=>formatAtom(f)===formatAtom(head))){facts.push(head);changed=true;yield snap('derive',{rule:rule.id,head:formatAtom(head),theta:formatTheta(match.theta),parents:match.parents})}
      }
    }
    if(!changed){yield snap('fixedpoint');return}
  }
}
export function* sldPredicateSteps(input,{maxDepth=12,maxEvents=500,maxAnswers=12}={}) {
  const p=validateProgram(input),queryVars=atomVariables(p.query),answers=[]
  const clauses=[...p.rules,...p.facts.map(head=>({head,body:[],id:'fact'}))]
  const usedVariables=new Set([p.query,...clauses.flatMap(c=>[c.head,...c.body])].flatMap(atomVariables))
  let serial=0,events=0,limited=false
  const snap=(phase,goals,theta,depth,extra={})=>({phase,goals:goals.map(g=>formatAtom(applyAtom(g,theta))),theta:formatTheta(theta),answers:structuredClone(answers),depth,...extra})
  yield snap('start',[p.query],{},0)
  function* prove(goals,theta,depth){
    if(++events>maxEvents||answers.length>=maxAnswers){limited=true;yield snap('budget',goals,theta,depth);return}
    if(!goals.length){
      const all=formatTheta(theta),answer=Object.fromEntries(queryVars.map(v=>['?'+v,all['?'+v]||'?'+v]))
      if(!answers.some(x=>JSON.stringify(x)===JSON.stringify(answer)))answers.push(answer)
      yield snap('answer',goals,theta,depth);return
    }
    if(depth>=maxDepth){limited=true;yield snap('depth',goals,theta,depth);return}
    const selected=applyAtom(goals[0],theta)
    yield snap('goal',goals,theta,depth,{selected:formatAtom(selected)})
    for(const clause of clauses){
      if(events>=maxEvents||answers.length>=maxAnswers){limited=true;return}
      let fresh
      do{fresh=standardizeAtoms([clause.head,...clause.body],'r'+(++serial)+'_')}while(fresh.flatMap(atomVariables).some(v=>usedVariables.has(v)))
      fresh.flatMap(atomVariables).forEach(v=>usedVariables.add(v))
      const [head,...body]=fresh
      const next=unifyAtoms(selected,head,theta)
      if(next===null)continue
      const nextGoals=[...body,...goals.slice(1)].map(g=>applyAtom(g,next))
      yield snap('resolve',nextGoals,next,depth,{selected:formatAtom(selected),clause:formatAtom(head),body:body.map(formatAtom),rule:clause.id})
      yield*prove(nextGoals,next,depth+1)
      yield snap('backtrack',goals,theta,depth,{rule:clause.id})
    }
  }
  yield*prove([p.query],{},0)
  yield snap(limited?'budget':'finished',[],{},0)
}
export function parseClause(source) {
  if(typeof source!=='string'||source.length>1200)throw Error('Clause phải là chuỗi tối đa 1200 ký tự.')
  if(source.trim()==='[]')return []
  const parts=source.split('|')
  if(parts.length>8)throw Error('Tối đa 8 literal mỗi clause.')
  return parts.map(s=>{const t=s.trim(),negative=t.startsWith('~')||t.startsWith('¬');return {negative,atom:parseAtom(negative?t.slice(1):t)}})
}
export const formatLiteral=l=>(l.negative?'¬':'')+formatAtom(l.atom)
export const formatClause=c=>c.length?c.map(formatLiteral).join(' ∨ '):'□'
function normalizeClause(clause){
  const unique=[...new Map(clause.map(l=>[formatLiteral(l),l])).values()]
  if(unique.some(a=>unique.some(b=>a.negative!==b.negative&&formatAtom(a.atom)===formatAtom(b.atom))))return null
  const vars=[...new Set(unique.flatMap(l=>atomVariables(l.atom)))],mapping=Object.fromEntries(vars.map((v,i)=>[v,'v'+i])),atoms=renameAtoms(unique.map(l=>l.atom),mapping)
  return unique.map((l,i)=>({...l,atom:atoms[i]}))
}
export function resolveClauses(a,b,i,j,prefix='s') {
  const leftAtoms=standardizeAtoms(a.map(l=>l.atom),prefix+'a'),rightAtoms=standardizeAtoms(b.map(l=>l.atom),prefix+'b')
  if(!a[i]||!b[j]||a[i].negative===b[j].negative)return null
  const theta=unifyAtoms(leftAtoms[i],rightAtoms[j]);if(theta===null)return null
  const rest=[...a.map((l,k)=>({...l,atom:leftAtoms[k]})).filter((_,k)=>k!==i),...b.map((l,k)=>({...l,atom:rightAtoms[k]})).filter((_,k)=>k!==j)].map(l=>({...l,atom:applyAtom(l.atom,theta)}))
  return {clause:normalizeClause(rest),theta:formatTheta(theta),pivot:[formatLiteral({...a[i],atom:leftAtoms[i]}),formatLiteral({...b[j],atom:rightAtoms[j]})]}
}
export const resolutionExamples={
 kings:{title:'Phản chứng Evil(John)',clauses:['~King(?x)|~Greedy(?x)|Evil(?x)','King(John)','Greedy(John)','~Evil(John)']},
 unknown:{title:'Không đủ tiền đề',clauses:['~King(?x)|~Greedy(?x)|Evil(?x)','King(John)','~Evil(John)']},
 factoring:{title:'Cần hợp nhất các literal cùng dấu',clauses:['P(?x)|P(?y)','~P(?u)|~P(?v)']},
 notTautology:{title:'Hai literal đối dấu chỉ hợp nhất được chưa tạo hằng đúng',clauses:['P(?x)|~P(?y)']}
}
export function* resolutionPredicateSteps(input,{maxClauses=40,maxEvents=400}={}) {
  if(!Array.isArray(input)||!input.length||input.length>12)throw Error('Nhập 1 đến 12 clause.')
  const clauses=input.map(parseClause).map(c=>normalizeClause(c)).filter(c=>c!==null),records=clauses.map((c,i)=>({id:i+1,text:formatClause(c),parents:[]})),keys=new Set(clauses.map(formatClause))
  let events=0,serial=0
  const snap=(phase,extra={})=>({phase,clauses:structuredClone(records),...extra})
  yield snap('start')
  if(clauses.some(c=>!c.length)){yield snap('success');return}
  function* add(candidate,parents,theta,pivot,type){
    if(candidate===null)return
    const key=formatClause(candidate)
    if(keys.has(key))return
    keys.add(key);clauses.push(candidate);records.push({id:records.length+1,text:key,parents,theta,pivot,type})
    yield snap(type,{parents,theta,pivot,derived:key})
  }
  for(let i=0;i<clauses.length;i++){
    const a=clauses[i]
    for(let x=0;x<a.length;x++)for(let y=x+1;y<a.length;y++)if(a[x].negative===a[y].negative){
      const theta=unifyAtoms(a[x].atom,a[y].atom)
      if(theta!==null){const candidate=normalizeClause(a.filter((_,k)=>k!==y).map(l=>({...l,atom:applyAtom(l.atom,theta)})));yield*add(candidate,[i+1],formatTheta(theta),[formatLiteral(a[x]),formatLiteral(a[y])],'factor')}
    }
    for(let j=0;j<=i;j++)for(let x=0;x<a.length;x++)for(let y=0;y<clauses[j].length;y++){
      if(++events>maxEvents||clauses.length>=maxClauses){yield snap('budget');return}
      const result=resolveClauses(a,clauses[j],x,y,'s'+(++serial)+'_')
      if(result){yield*add(result.clause,[i+1,j+1],result.theta,result.pivot,'resolve');if(result.clause?.length===0){yield snap('success');return}}
    }
  }
  yield snap('finished')
}
