Status: REVIEWED_WITH_TRANSPORT_LIMITATION

# Student comprehension review of the Airbnb assignment

Scope: A new independent read-through in the role explicitly requested by the user, who knows basic Python and has just started data processing. First assess the existing website explanation alone. Identify concrete points where the reader still cannot act. Codex separately reads the Google Docs reference and preserves the complete original assignment.

Workdir: `C:/Users/Ai/.codex/worktrees/data-course-20261018-b`. Owned files: Only `qa/airbnb-student-review-20261019/**`. Read-only input: `qa/airbnb-student-input-20261019/assignment-before-review.md` and `cities.json`. All other files and worktrees are forbidden writes. Baseline: Main checkout `qa/airbnb-student-review-20261019/agy-baseline.json`.

Authorization: The human directly requested this Antigravity student review and previously authorized full tools in this exact worktree B for data-course authoring and QA. Permission mode: `dangerously_skip_permissions=true`. Risk: Bounded QA artifact writes, no website edits.

Acceptance: Read the entire assigned page as a beginner. Save `student-first-read.md` before reading official sources, reference notes or prior author/reviewer reports. Explain the assignment back, list what to do first and what files to make, then identify exact confusing passages and missing explanations. Distinguish needing instruction from a genuine decision intentionally left to the group. Do not claim this is an empirical human study or award a fabricated clarity percentage.

Second phase: Root may supply an updated draft plus reference comparison for a targeted reread. Check whether the concrete blockers were resolved while avoiding new mandatory rules absent from the official assignment. Do not implement the worked project, obtain data, use API keys, or invent results.

Verification: Read local inputs, optionally inspect the existing page at `http://127.0.0.1:5187/xu-ly-du-lieu/bai-tap-lon/` in a browser. Do not claim rendering checks unless actually performed. Run `git status --short`, `git diff --name-only`, `git diff --check`. No package installation, Git mutation, push, deploy, credentials, real LLM calls or full build.

Output: Incremental `student-first-read.md`, `findings.json`, and `report.md`. Every finding names a passage, the student's unanswered question, why it prevents action, proposed explanation and whether it is a blocker or optional improvement. Report exact input hashes, files written, checks performed, limits and permission errors. Codex reads and adjudicates every finding.

Stop: Preserve worktree on failure or timeout. One initial call plus at most two evidence-based corrections in the same scope. All preexisting files must remain unchanged.

Result: Both calls saved usable first-read and reread artifacts but the bridge returned a NoneType transport error. Codex independently verified reported input hashes, preserved original read artifacts and 48 baseline files. Ten initial concerns yielded nine explained points and one teacher-specific baseline evaluation scope still pending source detail. Report overclaims were rejected. Added complete seven-file Inside Airbnb schema explanations, Google Docs claim comparison and beginner action guidance. Original official assignment coverage (54 mapped groups plus exact26cities/104dates) remains verified. No third call needed.
