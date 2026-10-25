Status: READY_FOR_AGY

# Chapter 13: Discussion questions Q13.1–Q13.21

Tool: agy_start. Risk: Bounded content proposal, no public writes.

Workdir: `C:/Users/Ai/.codex/worktrees/physics1-ch06-audit-20261024/StudyHub`.
Baseline: Detached `4d37da52135889f08c3242c80019eb64f456625d`, no tracked changes.
Earlier chapter 6 QA artifacts are frozen and forbidden to modify.

## Scope and ownership

Write ONLY within `qa/ch13-agy-discussion/output/` in the assigned workdir:

- `discussion.md`: All 21 original discussion prompts faithfully in Vietnamese, each followed by exactly one CLOSED details block. Each solution contains Tóm tắt đề bài, Hướng đi (properties/formulas and WHY), and Lời giải. Preserve all question subparts and qualifications. No source-process prose in learner content.
- `checks.py`, `numeric-results.json`: Meaningful independent numerical/physics checks for all applicable claims, including inverse-cube central force orbital scaling, elliptical acceleration, orbit plane geometry and free-fall apparent weight.
- `source-unit-ledger.json`: One record per Q13.1–21, actual page, source prompt summary, corresponding heading, figures if needed, checks and limits.
- `report.json`, `report.md`: Changed paths, exact verification commands and results, assumptions, unresolved questions, permission errors and honest status. Include SHA256 of frozen outputs.

Read-only inputs: `qa/ch13-agy-discussion/input/` in assigned workdir. Original full PDF is also read-only at `C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/raw_materials/physics/source/young-freedman-15.pdf`. Source PDF pages 441–442, printed 421–422. Q13.1–13 on page441, Q13.14–21 on442. Inspect the actual page images, not OCR alone. Existing reviewed theory may be read in PRIMARY raw_materials/physics/chapter-13/.

Forbidden: All files outside owned output directory, other QA, docs, src, scripts, Git index/history, secrets, account settings, dependencies, browser/UI, network, full build, commit, push, deployment, other worktrees and other agents. Do not mutate any source inputs or textbook figures. No symlinks to writable locations. No cleanup.

## Acceptance and verification

All 21 actual prompts complete, academically correct solutions, no invented values, no silently changed source data. Exactly one closed details block per question. Natural academic Vietnamese, capitalization after colons, no thinking-aloud, no unsupported claims about error frequency. Short formulas single-line. Long chains break only at outer relations, never after equals or at plus/minus. Display and inline delimiters correct, no prose in TeX, no horizontal math scrollbar workaround. Explain elliptical/parabolic local approximation precisely. Inverse-cube force does not preserve general Kepler ellipses, but central force still preserves area law. A stationary sub-satellite latitude45N orbit plane excluding planet center is impossible with gravity alone. No universal full-accuracy claim.

Run `C:/Users/Ai/miniconda3/python.exe -I -X utf8 qa/ch13-agy-discussion/output/checks.py` from assigned workdir and save actual results. Parent will independently source-review, measure math, render and verify before accepting. Do not install dependencies or run a build.

## Authorization, mode and stop conditions

Permission mode: `dangerously_skip_permissions=true`. The human user explicitly authorized future Antigravity tasks/workdirs and automatic permission acceptance in this conversation. This does not authorize production, secrets or forbidden writes.

One initial call and at most two evidence-based corrective calls for this exact task. Stop on authentication errors, permission errors, ownership uncertainty, timeout or three-call exhaustion. Report exact blocker and preserve outputs. A process exit or a passing arithmetic script does not establish source fidelity.
