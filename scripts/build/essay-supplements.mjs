import {sourceCodeLiterals} from './exam-code-integrity.mjs'
import {execFileSync} from 'node:child_process'

const codeCache=new Map()
const pythonBlocks=text=>[...text.matchAll(/^```(?:python|py|python-error)[ \t]*\n([\s\S]*?)^```[ \t]*$/gm)].map(m=>m[1].replace(/\n$/,''))
export function canonicalPythonBlocks(markdowns){
  const pending=[...new Set(markdowns.flatMap(pythonBlocks))].filter(code=>!codeCache.has(code))
  if(pending.length){
    // Parse only; exercise code is never executed. Python itself resolves quotes and whitespace.
    const program='import ast,io,json,sys,tokenize\nitems=json.load(sys.stdin)\nresult=[]\nfor code in items:\n try:\n  tree=ast.dump(ast.parse(code),include_attributes=False)\n  comments=[t.string for t in tokenize.generate_tokens(io.StringIO(code).readline) if t.type==tokenize.COMMENT]\n  result.append("ast:"+tree+json.dumps(comments))\n except (SyntaxError,ValueError,tokenize.TokenError): result.append("literal:"+code)\njson.dump(result,sys.stdout,ensure_ascii=True)'
    const result=JSON.parse(execFileSync('python',['-c',program],{input:JSON.stringify(pending),encoding:'utf8',maxBuffer:8*1024*1024}))
    pending.forEach((code,i)=>codeCache.set(code,result[i]))
  }
  return codeCache
}

// Work on Markdown blocks, never on rendered HTML or characters inside code.
export function legacyExplanation(answer) {
  const lines=answer.replace(/\r\n?/g,'\n').split('\n'),kept=[]
  let fence=null
  for(const line of lines){
    const boundary=line.match(/^\s{0,3}(`{3,}|~{3,})/)
    if(boundary){
      if(fence&&boundary[1][0]===fence[0]&&boundary[1].length>=fence.length)fence=null
      else if(!fence)fence=boundary[1]
      kept.push(line);continue
    }
    if(!fence&&/^(?:#{1,6}\s+|\*\*)[^\n]*(?:hướng dẫn chấm|chấm\s+\d+\s*điểm|rubric)/i.test(line))break
    if(!fence&&/^\*\*(?:Kiểm chứng|Đối chiếu|Đọc lại|Mục tiêu|Hồ sơ câu|Nhãn|Sai lầm(?: được)? kiểm tra|Kiến thức\/bẫy):/i.test(line))continue
    kept.push(line)
  }
  return kept.join('\n').trim()
}
export function composeLegacySupplement(primary,answer,review='',codeKeys=new Map()) {
  let explanation=legacyExplanation(answer)
  const knownBlocks=new Set(sourceCodeLiterals(primary).blocks)
  const knownPython=new Set(pythonBlocks(primary).map(code=>codeKeys.get(code)||code))
  explanation=explanation.replace(/^(?:[a-c]\)[ \t]*\n\n)?```([^\n]*)\n([\s\S]*?)^```[ \t]*$/gm,(block,language,code)=>{
    const clean=code.replace(/\n$/,'')
    const samePython=/^(python|py|python-error)\s*$/.test(language)&&knownPython.has(codeKeys.get(clean)||clean)
    return knownBlocks.has(clean)||samePython?'':block
  })
  const paragraphs=new Set(primary.split(/\n\s*\n/).map(p=>p.trim()))
  const filterText=text=>text.split(/\n\s*\n/).filter(p=>!paragraphs.has(p.trim())).join('\n\n')
  const parts=[]
  let start=0
  for(const block of explanation.matchAll(/^(?:```[^\n]*\n[\s\S]*?^```[ \t]*$|~~~[^\n]*\n[\s\S]*?^~~~[ \t]*$)/gm)){
    parts.push(filterText(explanation.slice(start,block.index)),block[0])
    start=block.index+block[0].length
  }
  parts.push(filterText(explanation.slice(start)))
  explanation=parts.join('')
  const note=legacyExplanation(review).replace(/^Lưu ý quy chuẩn:\s*/,'')
  if(note&&!explanation.includes(note)&&!primary.includes(note))explanation+='\n\n'+note
  return explanation.replace(/\n{3,}/g,'\n\n').trim()
}
