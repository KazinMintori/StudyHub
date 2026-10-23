export const publishedPhysicsExerciseChapters = [4,9,10,11,17,18,19,20]
export const physicsExerciseConfigs = {
 4:{numbered:60,total:111,guided:12,discussion:38,half:30,files:[
  ['guided','parent-09-luyen-tap-huong-dan.md'],
  ['discussion','parent-10-cau-hoi-thao-luan.md'],
  ['numbered-a','parent-11-bai-tap-001-030.md'],
  ['numbered-b','parent-12-bai-tap-031-060.md'],
  ['bridge','parent-16-bai-tap-cau-noi.md']
 ]},
 9:{numbered:95,total:130,guided:12,discussion:22,half:48},
 10:{numbered:97,total:140,guided:12,discussion:30,half:75},
 11:{numbered:95,total:133,guided:12,discussion:25,half:48},
 17:{numbered:119,total:160,guided:12,discussion:28,half:60},
 18:{numbered:87,total:130,guided:12,discussion:30,half:44},
 19:{numbered:66,total:103,guided:12,discussion:24,half:33},
 20:{numbered:62,total:98,guided:12,discussion:23,half:31}
}
export function physicsExerciseFiles(chapter) {
 const config=physicsExerciseConfigs[chapter]
 if(!config)throw Error('Unconfigured exercise chapter: '+chapter)
 if(config.files)return config.files
 const pad=value=>String(value).padStart(3,'0')
 return [
  ['guided','09-luyen-tap-huong-dan.md'],
  ['discussion','10-cau-hoi-thao-luan.md'],
  ['numbered-a','11-bai-tap-001-'+pad(config.half)+'.md'],
  ['numbered-b','12-bai-tap-'+pad(config.half+1)+'-'+pad(config.numbered)+'.md'],
  ['bridge','16-bai-tap-cau-noi.md']
 ]
}
export function validatePhysicsExerciseIds(chapter,groups) {
 const config=physicsExerciseConfigs[chapter]
 if(!config)throw Error('Unconfigured exercise chapter')
 const all=groups.flatMap(group=>group.ids)
 const actual=all.filter(id=>new RegExp('^'+chapter+'\\.\\d+$').test(id))
 const expected=Array.from({length:config.numbered},(_,i)=>chapter+'.'+(i+1))
 if(JSON.stringify(actual)!==JSON.stringify(expected))throw Error('Missing/duplicate numbered prompts')
 const questions=all.filter(id=>id.startsWith('Q'+chapter+'.'))
 if(JSON.stringify(questions)!==JSON.stringify(Array.from({length:config.discussion},(_,i)=>'Q'+chapter+'.'+(i+1))))throw Error('Missing/duplicate discussion prompts')
 if(all.filter(id=>id.startsWith('VP'+chapter+'.')).length!==config.guided)throw Error('Missing guided prompts')
 if(all.filter(id=>id==='Bài tập cầu nối').length!==1)throw Error('Missing bridge')
 if(new Set(all).size!==all.length||all.length!==config.total)throw Error('Missing/duplicate source prompts')
 return all.length
}
