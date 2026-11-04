export function bellmanPotentials(shortcut){
  const graph={S:[['A',1],['B',shortcut]],A:[['B',2],['T',5]],B:[['T',1]],T:[]}
  const stages=['T','B','A','S']
  const values={T:0}
  const decisions={}
  for(const node of stages.slice(1)){
    const candidates=graph[node].map(([next,cost])=>({next,total:cost+values[next]}))
    values[node]=Math.min(...candidates.map(candidate=>candidate.total))
    decisions[node]=candidates.filter(candidate=>candidate.total===values[node]).map(candidate=>candidate.next)
  }
  return {graph,stages,values,decisions}
}

export function potentialSlacks(graph,potentials){
  return Object.entries(graph).flatMap(([from,edges])=>edges.map(([to,cost])=>({
    from,to,cost,slack:cost-potentials[from]+potentials[to],
  })))
}
