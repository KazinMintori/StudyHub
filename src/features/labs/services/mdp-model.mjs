export const directions = [
  { id: 'N', label: '↑', dx: 0, dy: 1 },
  { id: 'E', label: '→', dx: 1, dy: 0 },
  { id: 'S', label: '↓', dx: 0, dy: -1 },
  { id: 'W', label: '←', dx: -1, dy: 0 }
]

export function gridModel({ noise = 0.2, living = 0, convention = 'exit' } = {}) {
  if (!Number.isFinite(noise) || noise < 0 || noise > 1 || !Number.isFinite(living)) throw Error('Invalid grid parameters')
  if (!['entry', 'exit'].includes(convention)) throw Error('Invalid reward convention')
  const cells = []
  for (let y = 0; y < 3; y++) {
    for (let x = 0; x < 4; x++) {
      if (x !== 1 || y !== 1) cells.push({ id: x + ',' + y, x, y })
    }
  }
  const ids = new Set(cells.map(cell => cell.id))
  const rewards = { '3,2': 1, '3,1': -1 }
  const states = [...ids, 'terminal']
  const actions = Object.fromEntries(states.map(id => [
    id,
    id === 'terminal' || (convention === 'entry' && id in rewards)
      ? [] : id in rewards ? ['exit'] : directions.map(direction => direction.id)
  ]))
  const transitions = {}
  for (const cell of cells) {
    transitions[cell.id] = {}
    for (const action of actions[cell.id]) {
      if (action === 'exit') {
        transitions[cell.id][action] = [{ next: 'terminal', probability: 1, reward: rewards[cell.id] }]
        continue
      }
      const index = directions.findIndex(direction => direction.id === action)
      const outcomes = new Map()
      for (const [turn, probability] of [[0, 1 - noise], [-1, noise / 2], [1, noise / 2]]) {
        if (!probability) continue
        const direction = directions[(index + turn + 4) % 4]
        const target = (cell.x + direction.dx) + ',' + (cell.y + direction.dy)
        const next = ids.has(target) ? target : cell.id
        outcomes.set(next, (outcomes.get(next) ?? 0) + probability)
      }
      transitions[cell.id][action] = [...outcomes].map(([next, probability]) => ({
        next, probability, reward: convention === 'entry' && next in rewards ? rewards[next] : living
      }))
    }
  }
  return { states, actions, transitions, cells, convention }
}

export function tinyModel() {
  return {
    states: ['alive', 'terminal'],
    actions: { alive: ['stay', 'exit'], terminal: [] },
    transitions: { alive: {
      stay: [{ next: 'alive', probability: 1, reward: 1 }],
      exit: [{ next: 'terminal', probability: 1, reward: 3 }]
    } }
  }
}

export function actionValue(model, state, action, values, gamma) {
  return model.transitions[state][action].reduce(
    (sum, outcome) => sum + outcome.probability * (outcome.reward + gamma * values[outcome.next]), 0
  )
}

export function greedyAction(model, state, values, gamma, current) {
  const actions = model.actions[state]
  if (!actions.length) return null
  let selected = actions.includes(current) ? current : actions[0]
  let best = actionValue(model, state, selected, values, gamma)
  for (const action of actions) {
    const score = actionValue(model, state, action, values, gamma)
    if (score > best + 1e-10) { selected = action; best = score }
  }
  return selected
}

export function valueIterations(model, gamma, count = 100) {
  if (!(gamma >= 0 && gamma < 1)) throw Error('Use a discount below one')
  let values = Object.fromEntries(model.states.map(state => [state, 0]))
  const frames = [{ values, delta: 0, iteration: 0 }]
  for (let iteration = 1; iteration <= count; iteration++) {
    const next = {}
    for (const state of model.states) {
      const action = greedyAction(model, state, values, gamma)
      next[state] = action === null ? 0 : actionValue(model, state, action, values, gamma)
    }
    const delta = Math.max(...model.states.map(state => Math.abs(next[state] - values[state])))
    frames.push({ values: next, delta, iteration })
    values = next
  }
  return frames
}

export function evaluatePolicy(model, policy, gamma) {
  if (!(gamma >= 0 && gamma < 1)) throw Error('Use a discount below one')
  const states = model.states
  const rows = states.map((state, index) => {
    const row = [...states.map((_, column) => Number(column === index)), 0]
    for (const outcome of model.transitions[state]?.[policy[state]] ?? []) {
      row[states.indexOf(outcome.next)] -= gamma * outcome.probability
      row[states.length] += outcome.probability * outcome.reward
    }
    return row
  })
  for (let column = 0; column < states.length; column++) {
    let pivot = column
    for (let row = column + 1; row < states.length; row++) {
      if (Math.abs(rows[row][column]) > Math.abs(rows[pivot][column])) pivot = row
    }
    const swapped = rows[column]
    rows[column] = rows[pivot]
    rows[pivot] = swapped
    const divisor = rows[column][column]
    if (Math.abs(divisor) < 1e-12) throw Error('Singular policy system')
    for (let j = column; j <= states.length; j++) rows[column][j] /= divisor
    for (let row = 0; row < states.length; row++) {
      if (row === column) continue
      const factor = rows[row][column]
      for (let j = column; j <= states.length; j++) rows[row][j] -= factor * rows[column][j]
    }
  }
  return Object.fromEntries(states.map((state, index) => [state, rows[index][states.length]]))
}

export function policyIterations(model, gamma) {
  let policy = Object.fromEntries(model.states.map(state => [state, model.actions[state].at(-1) ?? null]))
  const frames = []
  for (let iteration = 0; iteration < 100; iteration++) {
    const values = evaluatePolicy(model, policy, gamma)
    frames.push({ phase: 'Đánh giá', policy, values, iteration })
    const improved = Object.fromEntries(model.states.map(state => [
      state, greedyAction(model, state, values, gamma, policy[state])
    ]))
    const stable = model.states.every(state => policy[state] === improved[state])
    frames.push({ phase: stable ? 'Chính sách ổn định' : 'Cải tiến', policy: improved, values, iteration })
    if (stable) return frames
    policy = improved
  }
  throw Error('Policy iteration exceeded the observation budget')
}
