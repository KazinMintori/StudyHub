# Inventory of owned worktrees and retention requirements

Status: READY_FOR_AGY
Workdir: C:/Users/Ai/.codex/worktrees/physics1-remaining-ch08-theory-20261023/StudyHub
Primary READ ONLY: C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub
Owned outputs: qa/cleanup-retention-inventory-20261028/** only.

Task scope: Prepare an inventory for the cleanup requested by the human after the course work is complete. This task MUST NOT delete, archive, move or modify any worktree or existing file. The overall physics source audit remains active. The human wants cleanup of artifacts created for this goal, preserving anything still necessary.

Read primary AGENTS.md and agy-supervisor protocol. Use git worktree list --porcelain to obtain exact roots. Establish ownership ONLY from explicit workdir records in primary docs/agy-plans and qa/physics-global-audit/agy-efficient-review-20261028/jobs.json. A physics-looking folder name alone does not prove ownership. Do not inspect unrelated task contents, user projects, secrets, account/profile configuration or credentials.

For each proven owned root, record branch/HEAD, git status --short, unpushed commits if a matching remote reference exists, known private/ignored QA evidence and whether a parent snapshot is already recorded. Do not recursively measure whole drives or node_modules. Existing manifests and direct directory lists are sufficient. Unknown ownership or retained unaccepted work means KEEP, not disposable. Do not infer “fully merged” merely because a branch is detached.

Output inventory.json/md, changed-files.json, verification.txt and report.json within the owned output directory. Include exact ownership evidence path and concrete keep/remove-later recommendation, never execute it. Identify dependencies shared by other worktrees or user checkouts. Primary/user checkout/active source/only copies of original assets and ignored evidence must be retained. Original textbook PDF must be retained.

Efficiency: Save inventory after the first proven root, update incrementally. Target five minutes useful work; return honest partial coverage instead of a broad full-cleanup-ready claim. Limit verification to known owned physics roots. No full builds, servers, UI, network, Git mutations, commits, pushes, installations or other agents. Current account ONLY, no account switching.

Permission mode: dangerously_skip_permissions=true. Human standing authorization covers bounded trusted future Antigravity tasks/workdirs, and explicitly requested an agent for safe cleanup. This task only writes its private reports. Three calls maximum, no fourth call. Parent verifies every recommendation before any later cleanup.
