import test from 'node:test'
import assert from 'node:assert/strict'
import { chooseRoute, traceDecision, decisionPresets, decisionCode } from '../../src/features/labs/services/agent-decision.mjs'

test('decision agrees with the independent closed-form comparison, including ties and endpoints', () => {
  const displayedDecision = new Function(`${decisionCode.join('\n')}; return chooseRoute`)()
  for (const loss of [-20, -5, 0]) for (let percent = 0; percent <= 100; percent++) {
    const p = percent / 100
    const short = p * 10 + (1 - p) * loss
    const best = chooseRoute(p, loss)
    assert.equal(best.name, short >= 6 - 1e-9 ? 'Đường ngắn' : 'Đường vòng')
    assert.ok(Math.abs(best.score - Math.max(short, 6)) < 1e-9)
    assert.deepEqual(displayedDecision(p, loss), best)
  }
})

test('all presets produce a stable trace whose last result is the executed decision', () => {
  for (const { p, loss } of decisionPresets) {
    const trace = traceDecision(p, loss)
    assert.equal(trace[0].best, null)
    assert.deepEqual(trace.at(-1).best, chooseRoute(p, loss))
    assert.equal(trace.at(-1).phase, 'done')
    assert.deepEqual(trace, traceDecision(p, loss))
    assert.ok(trace.every(frame => frame.line >= 1 && frame.line <= decisionCode.length))
    // Snapshots can be visited in either direction without carrying future state.
    const first = trace[0]
    assert.deepEqual(first.scores, [null, null])
    trace.at(-1).scores[0] = 999
    assert.deepEqual(first.scores, [null, null])
    assert.notEqual(traceDecision(p, loss).at(-1).scores[0], 999)
  }
})

test('changing consequences can reverse the choice without changing the probability', () => {
  assert.deepEqual(chooseRoute(.8, 0), { name: 'Đường ngắn', score: 8 })
  assert.deepEqual(chooseRoute(.8, -20), { name: 'Đường vòng', score: 6 })
  assert.deepEqual(chooseRoute(.6, 0), { name: 'Đường ngắn', score: 6 })
})

test('invalid models are rejected before a trace starts', () => {
  for (const [p, loss] of [[-1, 0], [1.1, 0], [NaN, 0], [.8, Infinity]]) {
    assert.throws(() => traceDecision(p, loss), RangeError)
  }
})
