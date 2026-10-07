"""Package revised skill directories with one root folder and a verified file manifest."""
import hashlib
import json
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESEARCH = HERE.parent
PACKS = {"textbook-passage-explainer": "textbook-passage-explainer-v2.1.zip",
         "textbook-to-course-slides": "textbook-to-course-slides-v6.1.zip"}
ORIGINALS = {"textbook-passage-explainer": "textbook-passage-explainer.zip",
             "textbook-to-course-slides": "textbook-to-course-slides-v5.zip"}


def main():
    manifest = []
    for name, filename in PACKS.items():
        source = RESEARCH / "revised" / name
        target = RESEARCH / filename
        files = sorted(file for file in source.rglob("*") if file.is_file()
                       and "__pycache__" not in file.parts and file.suffix not in (".pyc", ".pyo"))
        expected = {file.relative_to(source.parent).as_posix(): hashlib.sha256(file.read_bytes()).hexdigest() for file in files}
        with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for file in files:
                archive.write(file, file.relative_to(source.parent).as_posix())
        with zipfile.ZipFile(target) as archive:
            assert archive.testzip() is None
            assert set(archive.namelist()) == set(expected)
            for path, digest in expected.items():
                assert hashlib.sha256(archive.read(path)).hexdigest() == digest
                assert path.startswith(name + "/") and ".." not in Path(path).parts
        original = RESEARCH / ORIGINALS[name]
        with zipfile.ZipFile(original) as archive:
            baseline = {path: hashlib.sha256(archive.read(path)).hexdigest() for path in archive.namelist() if not path.endswith("/")}
        manifest.append({"archive": filename, "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
                         "original_archive": original.name,
                         "original_sha256": hashlib.sha256(original.read_bytes()).hexdigest(),
                         "added": sorted(set(expected) - set(baseline)),
                         "changed": sorted(path for path in set(expected) & set(baseline) if expected[path] != baseline[path]),
                         "removed": sorted(set(baseline) - set(expected)),
                         "files": expected, "verified": "CRC, file list and every file hash match revised source"})
    (HERE / "package-manifest-v2.1-v6.1.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps([{"archive": item["archive"], "files": len(item["files"])} for item in manifest], indent=2))


if __name__ == "__main__":
    main()
