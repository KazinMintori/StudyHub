import test from 'node:test'
import assert from 'node:assert/strict'
import {
  VALID_TIMER_MINUTES,
  DEFAULT_TIMER_MINUTES,
  isValidMinutes,
  formatTimerDisplay,
  calculateRemainingSeconds,
  restoreTimerState,
  startTimer,
  pauseTimer,
  resetTimer,
  tickTimer,
  getTimerButtonLabel
} from '../services/focusTimerService.mjs'

test('focusTimerService: isValidMinutes validates allowed pomodoro durations', () => {
  assert.equal(isValidMinutes(25), true)
  assert.equal(isValidMinutes(50), true)
  assert.equal(isValidMinutes(5), true)
  assert.equal(isValidMinutes(10), true)
  assert.equal(isValidMinutes(null), false)
})

test('focusTimerService: formatTimerDisplay pads minutes and seconds properly', () => {
  assert.equal(formatTimerDisplay(1500), '25:00')
  assert.equal(formatTimerDisplay(65), '01:05')
  assert.equal(formatTimerDisplay(9), '00:09')
  assert.equal(formatTimerDisplay(0), '00:00')
  assert.equal(formatTimerDisplay(-5), '00:00')
  assert.equal(formatTimerDisplay(NaN), '00:00')
})

test('focusTimerService: calculateRemainingSeconds rounds up ceiling of remaining time', () => {
  const now = 1000000
  assert.equal(calculateRemainingSeconds(now + 15000, now), 15)
  assert.equal(calculateRemainingSeconds(now + 14001, now), 15) // ceiling
  assert.equal(calculateRemainingSeconds(now - 1000, now), 0) // past deadline
})

test('focusTimerService: restoreTimerState falls back to safe defaults on missing or corrupt state', () => {
  const defaultExpected = {
    minutes: DEFAULT_TIMER_MINUTES,
    remaining: DEFAULT_TIMER_MINUTES * 60,
    running: false,
    sessions: 0,
    deadline: 0,
    finished: false
  }

  assert.deepEqual(restoreTimerState(null), defaultExpected)
  assert.deepEqual(restoreTimerState({}), defaultExpected)
  assert.deepEqual(restoreTimerState({ minutes: 241, remaining: 100 }), defaultExpected)
  assert.deepEqual(restoreTimerState({ minutes: 25, remaining: 'corrupt' }), defaultExpected)
})

test('focusTimerService: restoreTimerState restores active running timer when deadline is in the future', () => {
  const now = 1000000
  const deadline = now + 420000 // 420 seconds left = 7 minutes
  const savedState = {
    minutes: 25,
    remaining: 500, // old cached remaining
    running: true,
    deadline,
    sessions: 3
  }

  const restored = restoreTimerState(savedState, now)
  assert.equal(restored.minutes, 25)
  assert.equal(restored.remaining, 420)
  assert.equal(restored.running, true)
  assert.equal(restored.sessions, 3)
  assert.equal(restored.deadline, deadline)
  assert.equal(restored.finished, false)
})

test('focusTimerService: restoreTimerState detects session completed while user was away', () => {
  const now = 1000000
  const deadline = now - 5000 // deadline passed 5 seconds ago
  const savedState = {
    minutes: 25,
    remaining: 100,
    running: true,
    deadline,
    sessions: 2
  }

  const restored = restoreTimerState(savedState, now)
  assert.equal(restored.minutes, 25)
  assert.equal(restored.remaining, 0)
  assert.equal(restored.running, false)
  assert.equal(restored.sessions, 3) // session count incremented!
  assert.equal(restored.finished, true) // completed state flagged
})

test('focusTimerService: restoreTimerState restores paused timer accurately', () => {
  const savedState = {
    minutes: 50,
    remaining: 1800,
    running: false,
    deadline: 0,
    sessions: 4
  }

  const restored = restoreTimerState(savedState)
  assert.equal(restored.minutes, 50)
  assert.equal(restored.remaining, 1800)
  assert.equal(restored.running, false)
  assert.equal(restored.sessions, 4)
  assert.equal(restored.finished, false)
})

test('focusTimerService: startTimer computes target deadline from remaining time', () => {
  const now = 1000000
  const fresh = startTimer(25, 0, now)
  assert.equal(fresh.running, true)
  assert.equal(fresh.remaining, 1500)
  assert.equal(fresh.deadline, now + 1500 * 1000)
  assert.equal(fresh.finished, false)

  const resumed = startTimer(25, 300, now)
  assert.equal(resumed.remaining, 300)
  assert.equal(resumed.deadline, now + 300 * 1000)
})

test('focusTimerService: pauseTimer recalculates remaining time at pause point', () => {
  const now = 1000000
  const deadline = now + 120000
  const paused = pauseTimer(deadline, now)
  assert.equal(paused.running, false)
  assert.equal(paused.remaining, 120)
  assert.equal(paused.deadline, 0)
})

test('focusTimerService: resetTimer restores initial duration', () => {
  const reset = resetTimer(5)
  assert.equal(reset.minutes, 5)
  assert.equal(reset.remaining, 300)
  assert.equal(reset.running, false)
  assert.equal(reset.deadline, 0)
  assert.equal(reset.finished, false)
})

test('focusTimerService: tickTimer handles countdown and completion threshold', () => {
  const now = 1000000

  // Still ticking
  const ongoing = tickTimer(now + 10000, 1, now)
  assert.equal(ongoing.remaining, 10)
  assert.equal(ongoing.running, true)
  assert.equal(ongoing.sessions, 1)
  assert.equal(ongoing.finished, false)

  // Finished at deadline
  const completed = tickTimer(now, 1, now)
  assert.equal(completed.remaining, 0)
  assert.equal(completed.running, false)
  assert.equal(completed.sessions, 2)
  assert.equal(completed.finished, true)
})

test('focusTimerService: getTimerButtonLabel provides contextual user action text', () => {
  assert.equal(getTimerButtonLabel(true, 1000, 25), 'Tạm dừng')
  assert.equal(getTimerButtonLabel(false, 0, 25), 'Phiên mới')
  assert.equal(getTimerButtonLabel(false, 1000, 25), 'Tiếp tục')
  assert.equal(getTimerButtonLabel(false, 1500, 25), 'Bắt đầu')
})

test('Custom durations reject invalid input and survive reset, start and reload', () => {
  for (const value of [1, 17, 240, '17']) assert.equal(isValidMinutes(value), true)
  for (const value of [0, -1, 241, 2.5, NaN, Infinity, '', null, true, [25], {}]) {
    assert.equal(isValidMinutes(value), false)
  }
  assert.equal(resetTimer(17).remaining, 1020)
  assert.equal(startTimer(17, 0, 1000).deadline, 1021000)
  const restored = restoreTimerState({minutes:'17',remaining:840,running:false,sessions:2})
  assert.equal(restored.minutes, 17)
  assert.equal(restored.remaining, 840)
  const active = restoreTimerState({minutes:17,remaining:840,running:true,deadline:121000},1000)
  assert.equal(active.minutes, 17)
  assert.equal(active.remaining, 120)
  assert.equal(active.running, true)
})
