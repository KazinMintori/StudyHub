import mermaid from 'mermaid'
let sequence = 0, queue = Promise.resolve()
export function renderStudyDiagram(source) {
  const task = queue.then(async () => {
    const styles = getComputedStyle(document.documentElement)
    const token = name => styles.getPropertyValue(name).trim()
    const soft = token('--tim-soft'), ink = token('--ink'), purple = token('--tim')
    mermaid.initialize({ startOnLoad: false, securityLevel: 'strict', theme: 'base',
      themeVariables: {
        darkMode: document.documentElement.classList.contains('dark'), background: token('--paper'),
        primaryColor: soft, primaryBorderColor: purple, primaryTextColor: ink,
        secondaryColor: token('--canvas'), secondaryTextColor: ink, tertiaryColor: soft,
        lineColor: token('--ink-3'), textColor: ink, edgeLabelBackground: token('--paper'),
        fontFamily: 'Be Vietnam Pro, sans-serif', fontSize: '15px',
        ...Object.fromEntries(Array.from({ length: 12 }, (_, i) => [`cScale${i}`, soft])),
        ...Object.fromEntries(Array.from({ length: 12 }, (_, i) => [`cScaleLabel${i}`, ink]))
      }, flowchart: { htmlLabels: true, padding: 18, curve: 'basis' }
    })
    return (await mermaid.render(`study-diagram-${++sequence}`, source)).svg
  })
  queue = task.catch(() => {})
  return task
}
