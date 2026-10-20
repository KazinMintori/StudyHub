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
Owns central course.mjs, course overview/navigation, Wiki integration, supplement index/coverage report, final numerical and browser verification. Also authors lesson45-suy-luan-bayes-va-du-doan, its module/slides, co-dien-bayes figures and numerical generation script to close the additional Bayesian-inference gap identified by the audit. This brings the supplement to18 topics. Incorporates reviewed worker files, without overwriting user changes.

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

## Refined figures track (Added at the user's explicit request)

User steering: Eliminate text/text and graphic/text collisions, use even spacing, improve fonts, colors and smoothness, then delegate GitHub push after completion.

Worktree: C:/Users/Ai/.codex/worktrees/xstk-figures-20261020
Branch: codex/xstk-figures-20261020
Task scope: Redesign51 probability/statistics supplement figures. The3 Bayes figures remain Codex-owned and establish the shared visual direction.
Owned files: New scripts/generate-xstk-refined-figures.py, scripts/xstk_refined_*.py, docs/xac-suat-thong-ke/bai-giang/img/co-dien-refined/*.svg, raw_materials/xac-suat-thong-ke/visual-review-20261020.md. These paths do not overlap any running source worker.
Read-only inputs: Snapshot copies of lessons28..45, the original probability/statistics figure generators and assets, scripts/xstk_figure_style.py, scripts/qa/xstk-figure-gallery.mjs, the existing numerical verification scripts, and the Be Vietnam Pro font package. Never edit these inputs.
Shared design: Embedded Be Vietnam Pro through the Codex-owned xstk_figure_style helper, the site's purple ink with teal/copper accents, restrained grid lines, smooth exact-function curves, rounded joins, at least14px source labels, legends outside data regions,20–24px structural gutters, and short wrapped headings. No text clipping, no text/text intersections, no curve/stroke across text. Use existing filenames in the new directory for a deterministic final image-path remap by Codex.
Verification: Render all51 SVGs, run bounding-box and text/stroke collision inventory, inspect each rendered image, and verify every numerical chart and probability/interval label against its actual generating model. Gallery reports may be written under C:/Users/Ai/.codex/tmp/xstk-refined-qa. Preserve this worktree on tool failure. No Notes, catalog, UI, original generators/assets, commit, push or full build changes in this worker.

The user explicitly authorizes a separate final push task after all reviewed work is committed. That task is limited to a normal fast-forward push of the verified final commit to origin/main, with no force push, deletion or unrelated changes. It is dispatched only after QA and review.

Tool: agy_start with dangerously_skip_permissions=true. Headless execution, no visible terminals. Each track has one initial implementation call and at most two corrections within the same ownership.

Workers run their Python numerical verification and git diff --check, report changed files, counts, exact checks, unresolved issues and permission errors. Codex integrates modules, runs check_lecture for every XSTK lesson, Python skill test_tools.py, relevant repository tests, and browser QA through the local dev server. npm run ci:build and other full-build aliases are forbidden locally.

## Acceptance and review

Complete reading and gap mapping, corrected existing content, separate visible supplemental group below existing material, 18 coherent supplemental lessons with verified mathematics, figures, examples and solved exercises. Every file stays within ownership. Do not commit worker changes. Codex reviews numerical evidence, source claims, diffs and rendering before accepting files. Retain unverified worktrees on timeout or failure. Cleanup occurs only after reviewed changes are safely integrated.
