/**
 * Exercise containers helper for StudyHub.
 *
 * Normalizes ::: exercise containers so that:
 * - Exactly one "Bài tập n: <đề bài>" label is rendered.
 * - Explicit labels like "Bài tập1: ...", "Bài tập 1: ...", "Bài 1: ...", "1. ..." are normalized to "Bài tập n: ...".
 * - Redundant prefixes and colons ("Bài tập: Bài tập 1: ...") are eliminated.
 * - When an external exercise heading already names the exercise (e.g. "## Bài 1: ..." above the container),
 *   repeated titles inside the container are avoided (rendered without duplicate title).
 * - For subject-only or unnamed containers without external exercise headings, sensible defaults are kept.
 * - Exercise containers are marked with the semantic class "exercise" (<div class="warning custom-block exercise">)
 *   while ordinary warnings remain unaffected.
 */

export function isSectionHeading(text) {
  const t = text.trim()
  if (/(?:hệ thống\s+)?bài\s*tập\s+(?:tự\s*luyện|rèn\s*luyện|tổng\s*hợp|chuyên\s*sâu|cuối\s*bài)/i.test(t)) {
    return true
  }
  if (/^(?:phần|chương|lab|chủ\s*đề)\s*\d+/i.test(t)) {
    return true
  }
  if (/^bài\s*tập\s*(?:tự\s*luyện|rèn\s*luyện|tổng\s*hợp)$/i.test(t)) {
    return true
  }
  return false
}

export function parseExerciseHeading(headingText) {
  let t = (headingText || '').trim().replace(/^#{1,6}\s*/, '').trim()
  if (isSectionHeading(t)) {
    return null
  }
  // Pattern 1: Bài 1: ..., Bài 1.2.1: ..., Bài tập 1: ..., Bài 1 — ...
  const m1 = t.match(/^(?:bài\s*(?:tập\s*)?|exercise\s*)(\d+(?:[.\-_]\d+)*)\s*[:.—-]?\s*(.*)$/i)
  if (m1) {
    return { number: m1[1], subject: m1[2].trim() }
  }
  // Pattern 2: 1. Bài tập mục tiêu bậc ba
  const m2 = t.match(/^(\d+(?:[.\-_]\d+)*)\.\s*bài\s*tập\s*[:.—-]?\s*(.*)$/i)
  if (m2) {
    return { number: m2[1], subject: m2[2].trim() }
  }
  return null
}

export function normalizeExerciseTitle(rawTitle, activeHeading = null) {
  const raw = (rawTitle || '').trim().replace(/^(?:bài\s*tập\s*:\s*)+/i, '')

  // 1. Explicit exercise number in rawTitle
  // e.g. Bài tập1: ..., Bài tập 1: ..., Bài 1: ..., Bài 1.2.1: ..., BT 1: ...
  const mBt = raw.match(/^(?:bài\s*(?:tập\s*)?|bt\s*)+(\d+(?:[.\-_]\d+)*)\s*[:.]?\s*(.*)$/i)
  if (mBt) {
    const num = mBt[1]
    let rest = mBt[2].trim()
    rest = rest.replace(/^(?:bài\s*tập\b|bt\b)[:.]?\s*/i, '').replace(/^[:.]\s*/, '').trim()
    return `Bài tập ${num}${rest ? `: ${rest}` : ''}`
  }

  // e.g. 1. subject, 1: subject, 1.2.1: subject
  const mNum = raw.match(/^(\d+(?:[.\-_]\d+)*)\s*(?::|\.(?=\s|$))\s*(.*)$/)
  if (mNum) {
    const num = mNum[1]
    const rest = mNum[2].trim()
    return `Bài tập ${num}${rest ? `: ${rest}` : ''}`
  }

  // A decimal identifier remains intact when followed by difficulty or a subject.
  // e.g. 1, 1.2.1, 21.45 ••• CALC
  const mNumber = raw.match(/^(\d+(?:[.\-_]\d+)*)(?:\s+(.*))?$/)
  if (mNumber) {
    return `Bài tập ${mNumber[1]}${mNumber[2] ? `: ${mNumber[2]}` : ''}`
  }

  // 2. Bare container (no rawTitle)
  if (!raw) {
    if (activeHeading) {
      // External exercise heading already names it -> avoid repeated title
      return null
    }
    return 'Bài tập'
  }

  // 3. Subject-only container
  // Clean redundant leading "Bài tập:" but do not strip "Bài toán"
  const clean = raw.replace(/^(?:bài\s*tập\b|bt\b)[:.]?\s*/i, '').replace(/^[:.]\s*/, '').trim()
  if (activeHeading) {
    if (clean.toLowerCase() === (activeHeading.subject || '').toLowerCase()) {
      return null
    }
    return `Bài tập ${activeHeading.number}: ${clean}`
  }
  return `Bài tập: ${clean}`
}

export function normalizeExerciseContainers(src) {
  const newline = src.includes('\r\n') ? '\r\n' : '\n'
  const lines = src.split(/\r?\n/)
  let activeHeading = null
  let fence = null

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]
    const delimiter = line.match(/^ {0,3}(`{3,}|~{3,})(.*)$/)
    if (fence) {
      if (delimiter && delimiter[1][0] === fence[0]
        && delimiter[1].length >= fence.length && !delimiter[2].trim()) fence = null
      continue
    }
    if (delimiter) {
      fence = delimiter[1]
      continue
    }
    const hm = line.match(/^(#{1,6})\s+(.*)$/)
    if (hm) {
      const parsed = parseExerciseHeading(hm[2])
      if (parsed) {
        activeHeading = parsed
      } else if (hm[1] === '#' || hm[1] === '##') {
        // Major section resets exercise heading
        activeHeading = null
      }
      continue
    }

    const em = line.match(/^([ \t]*)::: exercise(?:[\t ]+(.*))?$/)
    if (em) {
      const indent = em[1]
      const rawTitle = em[2]
      const resolved = normalizeExerciseTitle(rawTitle, activeHeading)
      if (resolved === null) {
        lines[i] = `${indent}::: warning exercise-notitle`
      } else {
        lines[i] = `${indent}::: warning exercise: ${resolved}`
      }
    }
  }

  return lines.join(newline)
}

export function setupExerciseRenderer(md) {
  if (md._exerciseRendererSetup) return
  md._exerciseRendererSetup = true

  const origWarningOpen = md.renderer.rules['container_warning_open']
  md.renderer.rules['container_warning_open'] = (tokens, idx, options, env, self) => {
    const token = tokens[idx]
    const info = token.info.trim().slice('warning'.length).trim()
    if (info.startsWith('exercise:') || info === 'exercise-notitle') {
      const titleText = info.startsWith('exercise:') ? info.slice('exercise:'.length).trim() : ''
      const attrs = md.renderer.renderAttrs(token)
      const titleHtml = titleText
        ? `<p class="custom-block-title">${md.renderInline(titleText, { references: env.references })}</p>\n`
        : ''
      return `<div class="warning custom-block exercise"${attrs}>${titleHtml}`
    }
    return origWarningOpen(tokens, idx, options, env, self)
  }
}
