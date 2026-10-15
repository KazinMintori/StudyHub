# StudyHub architecture refactor

Status: IMPLEMENTED_AND_VERIFIED
Created: 2026-10-14
Project: C:/Users/Ai/Documents/StudyHub
Task risk class: Code changes
Authorization: The user explicitly requested multiple Antigravity MCP workers, granted tool control, and instructed implementation of this refactor in this chat.

## Baseline and boundaries

Baseline HEAD: abe13ca3edc03eadb72e28e54d3409e31dfa2d66 on main.
Existing dirty physics chapter-02/chapter-30 files and all raw_materials are protected.
Physics chat: Soạn bài Vật lý đại cương 1 và 2, active on chapter 30.
Preserve qa/physics/chapter30, full-source, all QA scripts/reports/snapshots and the two physics30 AGY worktrees.
AGY receives isolated worktrees under C:/Users/Ai/.codex/worktrees/studyhub-refactor-20261014, created by the collaboration MCP bridge from the committed plan baseline. Codex remains in the primary checkout.

## Shared architecture

Frontend lives under src/ with app, features, core, config. Features contain controllers (Vue composables and event orchestration), services (rules and transformations), components (rendering), and data where appropriate. Browser persistence belongs to core/storage. Controllers may branch for event handling and lifecycle, views may branch for rendering. Domain rules belong to services.
Keep all URLs, anchors, component public names, CSS classes, appearance behavior, localStorage keys and payload shapes. Existing theme files act as temporary compatibility entries. Do not change lecture text, published data, math, physics modules, or existing tests.
Codex owns global relocation, VitePress entry/config, content manifests and architecture docs, build/export changes, QA cleanup and final verification.

## Worker ownership

1. progress: Own theme StudyHome.vue, LessonActions.vue, progress.js, progress-migration.js, storage.js and new src/features/study-progress/**, src/core/storage/**. Extract resume resolution and progress rules into pure services, persistence into core, and heading tracking/lifecycle into controllers. Keep public exports through compatibility modules.
2. tools: Own theme StudyWorkspace.vue, FocusTimer.vue, data.js and new src/features/study-tools/**. Split notebook, flashcard and timer logic into services/controllers. Preserve templates and existing keys. Storage imports must use existing theme/storage.js bridge until parent integration. Do not own core/storage.
3. navigation: Own theme Layout.vue, lecture-state.js and new src/features/navigation/**, src/config/navigation.mjs. Extract sidebar responsive lifecycle, tab/hash handling and routing state into controllers, rules/config into services/config. Preserve rendering, breakpoints, focus/scroll restoration and public lecture-state exports. Do not change LecturePanels.vue or catalog.

## Permissions and forbidden operations

Permission mode: dangerously_skip_permissions=true, authorized by the user's explicit grant for these isolated trusted refactor worktrees and only the declared tasks.
No deletion, no cleanup, no production operations, no network, no credentials, no dependency installs, no commits, no work outside the assigned worktree, no writes outside owned paths. Do not alter the plan or another worker's files. Do not touch .agents, .claude, raw_materials, docs lecture content, physics QA, package files or scripts.

## Acceptance and verification

Preserve exact UI behavior and persistence compatibility. All new pure service modules pass node --check. Add meaningful node:test tests within owned src feature directories for resume fallback/migration, flashcard/timer state boundaries and hash classification as applicable. Run them with node --test. Source contains no secrets or absolute machine imports. Report changed paths, commands and full outcomes, blockers and permission errors.
Workers do not run full builds concurrently. Codex integrates only reviewed owned diffs and runs npm run dev, npm run ci:build, node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all and python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py plus browser checks.

## Lifecycle

One initial AGY call and at most two bounded corrections per worker. Stop on timeout, unknown status, forbidden mutations or authentication errors. Preserve uncertain worktrees. Review git status, diff --check and file boundaries before integrating. Archive/remove successful worktrees only after verified integration.

## Verified result

The three workers produced owned code but their MCP runner failed when returning output. Codex audited stable file hashes, ownership and diffs, completed integration manually, and preserved the worktrees. Full build and an isolated final build exited 0. Verification passed 108 feature tests, 24 source tests, 39 skill tests, 25 static browser checks and all lecture checks. All 779 previously published Markdown routes remain present. The isolated verification website was removed after success. Reports and cleanup manifests are under output/project-audit-2026-10-14, with the architecture guide at ARCHITECTURE.md.
