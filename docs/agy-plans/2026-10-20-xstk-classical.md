# Rà soát XSTK và bổ trợ chương trình cổ điển

Status: READY_FOR_AGY
Created: 2026-10-20
Project: C:/Users/Ai/Documents/StudyHub
Task risk class: Reversible content changes
Authorization: Người dùng yêu cầu dùng Antigravity qua MCP với toàn quyền tùy chọn cho việc đọc, rà soát, sửa môn XSTK và bổ sung kiến thức cổ điển. Quyền này áp dụng cho ba worktree tin cậy được liệt kê dưới đây.

## Baseline

Branch main, commit e4c1a9ab, working tree clean. Existing unrelated worktrees are preserved.

## Shared requirements

Read AGENTS.md, .agents/skills/studyhub-lecture/SKILL.md and references/repo-format.md before editing. Follow professor-voice, writing-vi, lecture-blueprint and visuals references. No full build, push, network publication, secrets, destructive operations, or unrelated changes. Use Python to verify every numerical example, exercise and counterexample. Use supported example/exercise/solution/proof containers. No math in headings, broken TeX, long inline math, or horizontal math scrollbars. All prose after colons starts with an uppercase letter. Use natural academic Vietnamese. All lecture references use the final heading Tài liệu tham khảo.

Preserve original 27 lesson slugs and learner progress. New content uses ordinary lecture technical integration (section: lecture), but the visible group is Bổ trợ xác suất thống kê cổ điển. Codex owns central catalog integration and navigation.

## Codex track

Worktree: C:/Users/Ai/Documents/StudyHub
Owns central course.mjs, course overview/navigation, Wiki integration if needed, supplement index/coverage report, final numerical and browser verification. Incorporates reviewed worker files, without overwriting user changes.

## AGY audit track

Worktree: C:/Users/Ai/.codex/worktrees/xstk-audit-20261020
Branch: codex/xstk-audit-20261020
Owned files: Existing docs/xac-suat-thong-ke Markdown files, existing lectures 01 through 27 lesson.mjs and slides.mjs, scripts/qa/xstk-audit*.py, and raw_materials/xac-suat-thong-ke/qa-audit-20261020.md. Existing figures may be corrected only when needed for factual accuracy.
Task: Read ALL existing course content (27 Notes, slides, problem set, supporting pages and redirects), correct substantive and presentation problems, record concrete findings and a classical curriculum gap matrix against MIT 18.05, Penn State STAT 414/415 and NIST. Do not author the new supplement lessons.

## AGY probability track

Worktree: C:/Users/Ai/.codex/worktrees/xstk-probability-20261020
Branch: codex/xstk-probability-20261020
Owned files: New docs/xac-suat-thong-ke/bai-giang/28-*.md through 35-*.md, matching src/content/courses/xac-suat-thong-ke/lectures/28-* through 35-*, docs/xac-suat-thong-ke/bai-giang/img/co-dien-xac-suat/, scripts/qa/xstk-classical-probability.py, scripts/generate-xstk-probability-figures.py, raw_materials/xac-suat-thong-ke/classical-probability-coverage.md.
Task: Read the existing course before writing. Supply eight substantial complementary lessons with 3–5 worked examples and 4–6 exercises with full folded solutions per lesson, 2–3 meaningful SVG figures per lesson, 3–6 review slides per lesson. Include complete frontmatter, lesson.mjs and slides.mjs. Existing prerequisite IDs only, no central catalog edits. The eight slugs and scope are fixed in the handoff prompt.

## AGY statistics track

Worktree: C:/Users/Ai/.codex/worktrees/xstk-statistics-20261020
Branch: codex/xstk-statistics-20261020
Owned files: New docs/xac-suat-thong-ke/bai-giang/36-*.md through 44-*.md, matching src/content/courses/xac-suat-thong-ke/lectures/36-* through 44-*, docs/xac-suat-thong-ke/bai-giang/img/co-dien-thong-ke/, scripts/qa/xstk-classical-statistics.py, scripts/generate-xstk-statistics-figures.py, raw_materials/xac-suat-thong-ke/classical-statistics-coverage.md.
Task: Read existing course before writing. Supply nine substantial complementary lessons with 3–5 worked examples and 4–6 exercises with full folded solutions per lesson, 2–3 meaningful SVG figures per lesson, 3–6 review slides per lesson. Include complete frontmatter, lesson.mjs and slides.mjs. Existing prerequisite IDs only, no central catalog edits. The nine slugs and scope are fixed in the handoff prompt.

## Permissions and verification

Tool: agy_start with dangerously_skip_permissions=true. Headless execution, no visible terminals. Each track has one initial implementation call and at most two corrections within the same ownership.

Workers run their Python numerical verification and git diff --check, report changed files, counts, exact checks, unresolved issues and permission errors. Codex integrates modules, runs check_lecture for every XSTK lesson, Python skill test_tools.py, relevant repository tests, and browser QA through the local dev server. npm run ci:build and other full-build aliases are forbidden locally.

## Acceptance and review

Complete reading and gap mapping, corrected existing content, separate visible supplemental group below existing material, 17 coherent supplemental lessons with verified mathematics, figures, examples and solved exercises. Every file stays within ownership. Do not commit worker changes. Codex reviews numerical evidence, source claims, diffs and rendering before accepting files. Retain unverified worktrees on timeout or failure. Cleanup occurs only after reviewed changes are safely integrated.
