"""Materialize immutable, checksum-verified local course objects in an isolated QA checkout.

Fallback for a shared workspace being changed by another task. Does not read or
modify the other task's course working files/index, fetch, switch or clean it.
"""
import hashlib
import json
import subprocess
import sys
import tarfile
from pathlib import Path

root = Path.cwd().resolve()
cache_root = Path(sys.argv[1]).resolve()
include_markdown = '--markdown' in sys.argv[2:]
lock = json.loads((root / 'config/course-repositories.json').read_text(encoding='utf-8'))
for course in lock['courses']:
    repo = cache_root / course['id']
    revision = course['revision']
    metadata = subprocess.check_output(['git', '-C', str(repo), 'show', f'{revision}:studyhub-course.json'])
    manifest = json.loads(metadata)
    assert manifest['id'] == course['id']
    # Only the modules needed by the production theme, plus this course's pages.
    # Do not duplicate embedded libraries, other course pages or source archives.
    expected = {name: digest for name, digest in manifest['files'].items()
                if name.startswith(('src/content/courses/', 'docs/.vitepress/'))
                or (course['id'] == 'toan-cho-ai' and name.startswith('docs/toan-cho-ai/'))
                or (include_markdown and name.endswith('.md'))}
    preserved = set()
    # Check the whole destination boundary before writing any file in this course.
    for name, digest in expected.items():
        dest = (root / name).resolve()
        assert dest.is_relative_to(root) and '/.git/' not in dest.as_posix()
        if dest.exists() and hashlib.sha256(dest.read_bytes()).hexdigest() != digest:
            if '--preserve-authored' not in sys.argv[2:]:
                raise RuntimeError(f'Preserve changed destination: {name}')
            preserved.add(name)
    prefixes = [p for p in (['docs', 'src/content/courses', 'raw_materials', 'examples', 'materials'] if include_markdown else ['src/content/courses', 'docs/.vitepress', 'docs/toan-cho-ai'])
                if any(name.startswith(p + '/') for name in expected)]
    process = subprocess.Popen(['git', '-C', str(repo), 'archive', '--format=tar', revision, *prefixes], stdout=subprocess.PIPE)
    seen = set()
    with tarfile.open(fileobj=process.stdout, mode='r|') as archive:
        for member in archive:
            if member.name not in expected:
                continue
            assert member.isfile(), member.name
            data = archive.extractfile(member).read()
            assert hashlib.sha256(data).hexdigest() == expected[member.name], member.name
            if member.name in preserved:
                seen.add(member.name)
                continue
            dest = root / member.name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            seen.add(member.name)
    # Drain tar padding before wait: A full stdout pipe can otherwise keep Git
    # alive after the tar reader has already reached its end marker.
    process.stdout.read()
    assert process.wait() == 0 and seen == set(expected), sorted(set(expected)-seen)
    print(f"Verified immutable {course['id']} @ {revision[:12]}: {len(seen)} files, {len(preserved)} authored changes preserved", flush=True)
