import test from 'node:test'
import assert from 'node:assert/strict'
import { gridModel, tinyModel, valueIterations, policyIterations, actionValue, evaluatePolicy } from './mdp-model.mjs'
const close = (actual, expected, tolerance = 1e-8) => assert(Math.abs(actual - expected) < tolerance, actual + ' vs ' + expected)

test('tiny MDP agrees with geometric-series optimum and policy improvement', () => {
  for (const gamma of [0, 0.5, 0.9]) {
    const model = tinyModel()
    const result = policyIterations(model, gamma).at(-1)
    close(result.values.alive, Math.max(3, 1 / (1 - gamma)))
    const vi = valueIterations(model, gamma, 300)
    close(vi.at(-1).values.alive, result.values.alive)
  }
  const trace = valueIterations(tinyModel(), 0.9, 3)
  assert.deepEqual(trace.map(frame => Number(frame.values.alive.toFixed(2))), [0, 3, 3.7, 4.33])
})

test('all grid transitions normalize, walls aggregate and terminal rewards occur once', () => {
  for (const noise of [0, 0.2, 0.5, 1]) {
    for (const convention of ['entry', 'exit']) {
      const model = gridModel({ noise, convention })
      for (const state of model.states) {
        for (const action of model.actions[state]) {
          const outcomes = model.transitions[state][action]
          close(outcomes.reduce((sum, outcome) => sum + outcome.probability, 0), 1)
          assert.equal(new Set(outcomes.map(outcome => outcome.next)).size, outcomes.length)
          assert(outcomes.every(outcome => outcome.next !== '1,1'))
        }
      }
      assert.deepEqual(model.actions.terminal, [])
      if (convention === 'entry') assert.deepEqual(model.actions['3,2'], [])
      else assert.equal(model.transitions['3,2'].exit[0].reward, 1)
    }
  }
  const outcomes = gridModel().transitions['0,0'].S
  close(outcomes.find(outcome => outcome.next === '0,0').probability, 0.9)
})

test('synchronous grid wave agrees with source example and both reward timings', () => {
  const model = gridModel()
  const frames = valueIterations(model, 0.9, 100)
  close(frames[1].values['3,2'], 1)
  close(frames[1].values['2,2'], 0)
  close(frames[2].values['2,2'], 0.72)
  close(frames[3].values['1,2'], 0.5184)
  close(frames.at(-1).values['0,2'], 0.644969, 0.000001)
  const entry = valueIterations(gridModel({ convention: 'entry' }), 0.9, 1)
  close(entry[1].values['2,2'], 0.8)
  close(entry[1].values['3,2'], 0)
})

test('policy evaluation satisfies its linear equations and agrees with optimal VI', () => {
  for (const noise of [0, 0.2, 0.5]) {
    for (const living of [0, -0.03, -0.4, -2]) {
      const model = gridModel({ noise, living })
      const trace = policyIterations(model, 0.9)
      const final = trace.at(-1)
      const values = evaluatePolicy(model, final.policy, 0.9)
      const optimal = valueIterations(model, 0.9, 300).at(-1).values
      for (const state of model.states) {
        close(values[state], optimal[state])
        if (!model.actions[state].length) continue
        close(values[state], actionValue(model, state, final.policy[state], values, 0.9))
      }
      for (let i = 2; i < trace.length; i += 2) {
        for (const state of model.states) assert(trace[i].values[state] >= trace[i - 2].values[state] - 1e-8)
      }
    }
  }
})
