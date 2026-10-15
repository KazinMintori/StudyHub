import test from 'node:test'
import assert from 'node:assert/strict'
import { mathSegments } from '../../src/core/math/services/math-text.mjs'

test('Currency escapes cannot start a display formula spanning later prose', () => {
  const source = String.raw`Giá $0.15\$$ đầu vào, $0.60\$$ đầu ra và VNĐ/\$.`
  assert.deepEqual(mathSegments(source).filter((_, i) => i % 2), [String.raw`$0.15\$$`, String.raw`$0.60\$$`])
})
test('Inline and multiline display formulas keep their exact TeX', () => {
  assert.deepEqual(mathSegments('A $x$ B $$\nx+y\n$$ C'), ['A ', '$x$', ' B ', '$$\nx+y\n$$', ' C'])
})
