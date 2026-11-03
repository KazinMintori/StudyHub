import test from 'node:test'
import assert from 'node:assert/strict'
import { networkStep, attentionStep, beamSteps } from './learning-models.mjs'
test('all backprop derivatives agree with central differences using old weights', () => {
  const parameters = { w: 0.4, b: 0.1, v: -0.7, c: 0.2 }
  const result = networkStep(parameters)
  for (const parameter of Object.keys(parameters)) {
    const epsilon = 1e-5
    const positive = networkStep({ ...parameters, [parameter]: parameters[parameter] + epsilon }).loss
    const negative = networkStep({ ...parameters, [parameter]: parameters[parameter] - epsilon }).loss
    const derivative = (positive - negative) / (2 * epsilon)
    assert(Math.abs(result.gradient[parameter] - derivative) < 1e-9)
  }
  assert(networkStep(result.after).loss < result.loss)
})
test('attention normalizes valid positions and a mask makes the future contribution zero', () => {
  const balanced = attentionStep([1, 1])
  assert.deepEqual(balanced.probabilities, [0.5, 0.5])
  assert.deepEqual(balanced.result, [0.5, 1])
  const biased = attentionStep([2, 0])
  assert(Math.abs(biased.probabilities.reduce((a, b) => a + b) - 1) < 1e-12)
  assert(biased.probabilities[0] > biased.probabilities[1])
  const masked = attentionStep([2, 0], true)
  assert.deepEqual(masked.probabilities, [1, 0])
  assert.deepEqual(masked.result, [1, 0])
})
test('beam keeps completed sequences and can recover a sequence pruned by greedy search', () => {
  const greedy = beamSteps(1).at(-1).kept[0]
  const wider = beamSteps(2).at(-1).kept[0]
  assert.deepEqual(greedy.tokens, ['A', 'x', 'EOS'])
  assert.deepEqual(wider.tokens, ['B', 'z', 'EOS'])
  assert(Math.abs(Math.exp(greedy.log) - 0.18) < 1e-12)
  assert(Math.abs(Math.exp(wider.log) - 0.4) < 1e-12)
})
