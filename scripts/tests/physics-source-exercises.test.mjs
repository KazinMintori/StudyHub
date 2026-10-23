import test from 'node:test'
import assert from 'node:assert/strict'
import {numberedExerciseIds} from '../verification/physics-source-exercises.mjs'

test('PDF coordinate artifacts and references are not exercise headings', () => {
  const text = '10.5 •  One force acting on a machine part\n' +
    'S ∙1-0.450 m2dn ∙10.150 m2en. (a) In a sketch\n' +
    'Compare problem 10.199 and Fig. E10.200.\n' +
    'VP10.12.4  A guided variation\n' +
    '10.96  A doubling of the torque produces a greater acceleration.\n' +
    '10.97  If the body’s center of mass were not on the axis\n'
  assert.deepEqual(numberedExerciseIds(text, 10), [5, 96, 97])
})

test('Unicode spaces, difficulty bullets and MCAT headings are retained', () => {
  assert.deepEqual(numberedExerciseIds('9.2 ••  CALC A wheel\n 9.1 • A disk\n9.95  Which statement is correct?\n9.2 • Repeated answer\n', 9), [1, 2, 95])
  assert.deepEqual(numberedExerciseIds('11.1 • Different chapter\n', 10), [])
})
