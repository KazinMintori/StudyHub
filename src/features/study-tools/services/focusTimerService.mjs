/**
 * Pure domain service for focus timer (Pomodoro) operations.
 */

export const VALID_TIMER_MINUTES = [25, 50, 5]
export const DEFAULT_TIMER_MINUTES = 25

const safeSessions = value => Number.isFinite(Number(value)) ? Math.max(0, Math.floor(Number(value))) : 0
const safeMinutes = value => isValidMinutes(value) ? Number(value) : DEFAULT_TIMER_MINUTES

export function isValidMinutes(minutes) {
  return VALID_TIMER_MINUTES.includes(Number(minutes))
}

export function formatTimerDisplay(remainingSeconds) {
  const safe = Number.isFinite(remainingSeconds) ? Math.max(0, Math.floor(remainingSeconds)) : 0
  const mins = String(Math.floor(safe / 60)).padStart(2, '0')
  const secs = String(safe % 60).padStart(2, '0')
  return `${mins}:${secs}`
}

export function calculateRemainingSeconds(deadline, now = Date.now()) {
  const diff = Number(deadline) - Number(now)
  return Number.isFinite(diff) ? Math.max(0, Math.ceil(diff / 1000)) : 0
}

export function restoreTimerState(state, now = Date.now()) {
  const defaultState = {
    minutes: DEFAULT_TIMER_MINUTES,
    remaining: DEFAULT_TIMER_MINUTES * 60,
    running: false,
    sessions: 0,
    deadline: 0,
    finished: false
  }

  if (!state || typeof state !== 'object') {
    return defaultState
  }

  if (!isValidMinutes(state.minutes) || !Number.isFinite(state.remaining)) {
    return defaultState
  }

  const minutes = Number(state.minutes)
  const sessions = safeSessions(state.sessions)
  const deadline = Number.isFinite(Number(state.deadline)) ? Number(state.deadline) : 0
  const wasRunning = state.running === true

  if (wasRunning && deadline > 0) {
    const remaining = Math.min(minutes * 60, calculateRemainingSeconds(deadline, now))
    if (remaining === 0) {
      return {
        minutes,
        remaining: 0,
        running: false,
        sessions: sessions + 1,
        deadline,
        finished: true
      }
    }
    return {
      minutes,
      remaining,
      running: true,
      sessions,
      deadline: Math.min(deadline, Number(now) + minutes * 60 * 1000),
      finished: false
    }
  }

  return {
    minutes,
    remaining: Math.min(minutes * 60, Math.max(0, Math.ceil(state.remaining))),
    running: false,
    sessions,
    deadline: 0,
    finished: false
  }
}

export function startTimer(minutes, remaining, now = Date.now()) {
  const validMins = safeMinutes(minutes)
  const currentRem = Number.isFinite(remaining) && remaining > 0 ? Math.min(validMins * 60, Math.ceil(remaining)) : validMins * 60
  const deadline = Number(now) + currentRem * 1000

  return {
    running: true,
    remaining: currentRem,
    deadline,
    finished: false
  }
}

export function pauseTimer(deadline, now = Date.now()) {
  const remaining = calculateRemainingSeconds(deadline, now)
  return {
    running: false,
    remaining,
    deadline: 0,
    finished: false
  }
}

export function resetTimer(minutes) {
  const validMins = safeMinutes(minutes)
  return {
    minutes: validMins,
    remaining: validMins * 60,
    running: false,
    deadline: 0,
    finished: false
  }
}

export function tickTimer(deadline, sessions, now = Date.now()) {
  const remaining = calculateRemainingSeconds(deadline, now)
  const currentSessions = safeSessions(sessions)

  if (!Number.isFinite(Number(deadline)) || Number(deadline) <= 0) {
    return { remaining: 0, running: false, sessions: currentSessions, finished: false }
  }

  if (remaining === 0) {
    return {
      remaining: 0,
      running: false,
      sessions: currentSessions + 1,
      finished: true
    }
  }

  return {
    remaining,
    running: true,
    sessions: currentSessions,
    finished: false
  }
}

export function getTimerButtonLabel(running, remaining, minutes) {
  if (running) return 'Tạm dừng'
  if (remaining === 0) return 'Phiên mới'
  if (remaining < minutes * 60) return 'Tiếp tục'
  return 'Bắt đầu'
}
