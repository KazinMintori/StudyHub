"""Audit AGY's exclusive file boundaries; optionally copy completed authored files."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = json.loads((ROOT / 'raw_materials/xu-ly-du-lieu/authoring-contract.json').read_text(encoding='utf-8'))
WORKTREES = Path('C:/Users/Ai/.codex/worktrees')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('group', choices=list('abc'))
    parser.add_argument('--copy', action='store_true', help='Use only after the corresponding job has finished and review has passed.')
    args = parser.parse_args()
    worktree = WORKTREES / f'data-course-20261018-{args.group}'
    assert worktree.is_dir()
    allowed = {f'scripts/verify-data-course-{args.group}.py', f'raw_materials/xu-ly-du-lieu/coverage-{args.group}.json'}
    for entry in CONTRACT['lessons']:
        if entry['group'] != args.group:
            continue
        allowed.add(f"docs/xu-ly-du-lieu/bai-giang/{entry['slug']}.md")
        allowed.update(f"src/content/courses/xu-ly-du-lieu/lectures/{entry['slug']}/{name}.mjs" for name in ['lesson', 'slides'])
    result = subprocess.run(['git', '-C', str(worktree), '-c', 'core.quotepath=false', 'status', '--porcelain', '--untracked-files=all'],
                            capture_output=True, text=True, encoding='utf-8', check=True)
    changed = []
    for line in result.stdout.splitlines():
        status, name = line[:2], line[3:]
        assert status in [' M', '??'], f'Unexpected status in AGY worktree: {line}'
        assert name in allowed, f'Out-of-scope file: {line}'
        changed.append(name)
    subprocess.run(['git', '-C', str(worktree), 'diff', '--check'], check=True)
    if args.copy:
        for name in sorted(allowed):
            source = worktree / name
            assert source.is_file(), f'Missing authored deliverable: {source}'
            destination = ROOT / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    print(json.dumps({'group': args.group, 'changedFiles': changed, 'expectedDeliverables': len(allowed), 'copied': args.copy}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
