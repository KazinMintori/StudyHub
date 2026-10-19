/** Adapt plain philosophy text to the shared exam renderer without interpreting it as HTML. */
const escapeHtml = value => String(value ?? '').replace(/[&<>"']/g, character => ({
  '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
})[character])
const paragraph = value => value ? `<p>${escapeHtml(value).replace(/\n/g, '<br>')}</p>` : ''

export function toExamBank(bank) {
  return {
    id: bank.id,
    title: bank.title,
    questions: (bank.questions || []).map(question => ({
      id: question.id,
      kind: 'quiz',
      correctKey: question.correctKey,
      promptHtml: paragraph(question.prompt),
      options: question.options.map(option => ({
        key: option.key,
        html: paragraph(option.text),
        explanationHtml: paragraph(option.key === question.correctKey
          ? question.explanation
          : question.distractors?.find(item => item.key === option.key)?.explanation),
      })),
      answerHtml: paragraph(question.takeaway),
    })),
  }
}
