Status: READY_FOR_AGY

# Independent data exam answer review

Scope: Audit 46 uncertain quiz/essay items blind first, then compare current answers. Review only. Codex adjudicates changes.

Workdir: `C:/Users/Ai/.codex/worktrees/data-course-20261018-c` (existing detached worktree). Preserve all preexisting changes. Baseline SHA256 inventory is in the main checkout at `qa/data-exam-second-review/agy-baseline.json`.

AGY owns only `qa/data-exam-second-review/**` in that workdir for evidence scripts and reports. Inputs are read-only `qa/data-exam-second-review-input/blind-agy.json` and `key-agy.json`. Do not read old worktree answers: They may be stale.

Forbidden: Any other file writes, source edits, Git mutations, push, deploy, package installation, credentials, real API calls, deletion, unrelated worktrees. No full site build.

Authorization: User explicitly authorized full tools within worktree C for data course authoring and QA, reaffirmed permission and requested this independent Antigravity review. Permission mode: `dangerously_skip_permissions=true`. Risk: Bounded QA artifact writes, all project content read-only.

Acceptance: Save blind conclusions before opening keys. For every item record the independent result, method, exact evidence, then classify correct key, wrong key, wrong explanation, ambiguity, or unresolved. Arithmetic/code claims require actual Python execution. Where possible use a second independent calculation, counterexample, or official documentation. Identify version-dependent behavior explicitly. Do not treat agreement with keys or schema validity as proof. Do not claim an accuracy percentage.

Verification: Run each evidence script under the owned directory with Python, save interpreter/library versions and complete results. Run `git status --short`, `git diff --name-only`, and `git diff --check` to demonstrate boundaries. Codex compares baseline hashes and independently reproduces findings.

Output: Incremental `blind-conclusions.json`, `findings.json`, `report.md`, executable evidence scripts and result JSON under the owned directory. Report exact reviewed IDs, derived answer, key agreement, explanation errors, unresolved assumptions, changed files, test commands/results, final status and permission errors. Include official source URLs for documentary claims.

Stop: Preserve artifacts on timeout, authentication/permission failure or insufficient assumptions. Do not guess. One initial AGY call and at most two evidence-based corrections. No production work delegated.
