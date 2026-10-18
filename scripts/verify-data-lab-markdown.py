"""Run the actual Python blocks readers see, in a temporary working directory."""
from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
import argparse
import ast
import json
import os
import re
import sys
import types

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+", type=Path)
parser.add_argument("--require-calls", action="store_true")
args = parser.parse_args()
records = []
os.environ["MPLBACKEND"] = "Agg"
for file in args.files:
    path = file.resolve()
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"^```python[^\n]*\n(.*?)^```\s*$", text, flags=re.M | re.S)
    namespace = {"__name__": "__lesson__", "display": lambda *objects, **kwargs: None}
    declared, called = set(), set()
    def profile(frame, event, arg):
        if event == "call" and frame.f_code.co_filename.startswith(f"{path.name}:block-"):
            called.add((frame.f_code.co_filename, frame.f_code.co_name, frame.f_code.co_firstlineno))
    previous = Path.cwd()
    with TemporaryDirectory(prefix="studyhub-lab-") as temporary:
        try:
            os.chdir(temporary)
            for index, code in enumerate(blocks, 1):
                tree = ast.parse(code, filename=f"{path.name}:block-{index}")
                output, errors = StringIO(), StringIO()
                try:
                    with redirect_stdout(output), redirect_stderr(errors):
                        sys.setprofile(profile)
                        exec(compile(tree, f"{path.name}:block-{index}", "exec"), namespace)
                except Exception as exc:
                    raise RuntimeError(f"{path.name}, Python block {index}: {type(exc).__name__}: {exc}") from exc
                finally:
                    sys.setprofile(None)
                # A completed program can include optional helper functions
                # used only on other inputs. Require a visible call for the
                # method being taught, not every helper copied into its prelude.
                lines = code.splitlines()
                first = lines.index("# Bắt đầu lời giải") + 2 if "# Bắt đầu lời giải" in lines else 1
                last = lines.index("# Kết thúc lời giải") + 1 if "# Kết thúc lời giải" in lines else len(lines) + 1
                for value in namespace.values():
                    if (isinstance(value, types.FunctionType)
                            and value.__code__.co_filename == f"{path.name}:block-{index}"
                            and first <= value.__code__.co_firstlineno < last):
                        declared.add((value.__code__.co_filename, value.__code__.co_name, value.__code__.co_firstlineno))
            if "plt" in namespace:
                namespace["plt"].close("all")
        finally:
            os.chdir(previous)
    uncalled = sorted(declared - called)
    assert not args.require_calls or not uncalled, f"Functions need visible example calls: {uncalled}"
    records.append({"file": path.name, "executedPythonBlocks": len(blocks), "declaredFunctions": len(declared), "calledFunctions": len(declared & called), "uncalledFunctions": uncalled})
print(json.dumps({"status": "passed", "records": records}, ensure_ascii=False, indent=2))
