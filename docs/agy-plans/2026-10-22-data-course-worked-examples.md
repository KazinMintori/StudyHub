Status: READY_FOR_AGY

# Worked examples and Vietnamese teaching prose across the data course

Scope: Enrich all thirteen current data-processing lectures and appendices A/B with runnable worked examples, visible results, practical use, parameter semantics and explanations of misleading interpretations. Preserve every existing exercise, source boundary, URL and question identifier. Do not use labels such as “Bẫy”, “Cạm bẫy”, “Lưu ý quan trọng” to replace an actual explanation.

Codex owns final Notes, executable checks, output tables/figures, integration, publication and all files in the primary checkout. Existing unrelated edits to application styles, Math AI and shared components are outside this task and must remain untouched.

Antigravity owns only the following isolated output directories. Inputs and every preexisting file are read-only.

- Track A: `C:/Users/Ai/.codex/worktrees/data-course-20261018-a/qa/data-teaching-20261022/output/`. Chapters 1–5: Environment, Python, structures/functions/files, NumPy and pandas foundations.
- Track B: `C:/Users/Ai/.codex/worktrees/data-course-20261018-b/qa/data-teaching-20261022/output/`. Chapters 6–10: Input/output, cleaning/strings, combining/reshaping, plotting and grouped operations.
- Track C: `C:/Users/Ai/.codex/worktrees/data-course-20261018-c/qa/data-teaching-20261022/output/`. Chapters 11–13 and appendices A/B: Time series, modeling, case studies, advanced arrays and IPython.

Task: Read the assigned current Notes snapshots, `manifest.json`, current `studyhub-lecture` skill and its pedagogy/writing/teaching-review references. Produce one JSON file per lesson, with eight to twelve insertion sections anchored to existing headings. Address functions that have a name or signature but no sufficiently clear input/output walkthrough. Each section has a concrete purpose, complete standalone code, `print` output and detailed Vietnamese reasoning. At least one example per lesson must explain a less prominent method. Never mutate code punctuation as prose. Save each lesson incrementally.

Output schema is specified in each task's `input/contract.json`. Use only the specified output files and a final report. No edits to primary Notes, application code, catalog, existing worktree files, Git history or plans. No installations, external messages, credentials, paid services, destructive commands, push/deploy, local full builds or use of private group documents.

Authorization: The user explicitly requested Antigravity to handle teaching prose and its review, granted full tool permission for this course, and previously authorized these exact three worktrees. `dangerously_skip_permissions=true` is limited to the owned output directory. All actions must stay reversible. Codex independently checks every adopted calculation, source claim and render.

Acceptance: All fifteen actual lessons receive concrete worked examples with independently reproduced output and clear discussion of the function's operation, parameters, return shape and conditions. Tables are real HTML/Markdown tables, mobile code retains indentation, math has no scrollbars and Vietnamese renders correctly. No course administration or unrelated IAI material. No blanket speed claims, no fake timing or statistical error-frequency claims.

Verification: AGY records changed files, source hashes, commands actually run and limitations. JSON must parse, every listed anchor must exist and every example must contain complete setup. Codex executes examples with Python, checks retained source/exercise content, reviews prose, runs lecture skill checks and browser QA. Baseline Git statuses and file hashes are recorded before each dispatch and compared afterward. Known NoneType transport errors are failures even if partial artifacts exist. At most one initial and two bounded corrective calls per track. Preserve worktrees and artifacts on timeout or uncertain status.
