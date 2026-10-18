"""Tests for explicit lab composition, without optional data-science packages."""
import importlib.util
from pathlib import Path
import sys
import unittest

MODULE = Path(__file__).resolve().parents[1] / "complete-data-lab-code.py"
SPEC = importlib.util.spec_from_file_location("complete_data_lab_code", MODULE)
composer = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = composer
SPEC.loader.exec_module(composer)


def document(code, exercise="data-lab-test-01", setup="", newline="\n"):
    text = "Introduction.\n"
    if setup:
        text += f"```python\n{setup}\n```\n"
    text += f'''<span id="{exercise}"></span>
::: exercise
Problem with illustrative code, not a solution:
```python
illustration = missing_name
```
:::
::: solution
#### Cách 1: First method
```python
{code}
```
Explanation kept exactly.
```text
expected output
```
:::
Final prose.\n'''
    return text.replace("\n", newline)


class ExtractionTests(unittest.TestCase):
    def test_only_python_in_solution_and_ignore_fake_headings(self):
        text = document('print("hello")')
        text = '```text\n<span id="data-lab-fake"></span>\n#### Cách 2: Fake\n```\n' + text
        methods = composer.extract_methods(text)
        self.assertEqual([(m.exercise, m.way) for m in methods], [("data-lab-test-01", 1)])
        self.assertEqual(methods[0].code, 'print("hello")\n')

    def test_preserve_every_non_method_byte_and_crlf(self):
        key = ("data-lab-test-01", 1)
        composer.REGISTRY[key] = composer.Plan(output='print("additional")')
        try:
            text = document('print("original")', newline="\r\n")
            method = composer.extract_methods(text)[0]
            result, programs = composer.compose_document(text)
            new_method = composer.extract_methods(result)[0]
            # Compare exact prefix/suffix outside the fence body.
            self.assertEqual(text[:method.start], result[:new_method.start])
            self.assertEqual(text[method.end:], result[new_method.end:])
            self.assertNotIn("\n", result.replace("\r\n", ""))
            again, _ = composer.compose_document(result)
            self.assertEqual(again, result)
        finally:
            del composer.REGISTRY[key]

    def test_unknown_dependencies_fail_without_replaying_setup(self):
        with self.assertRaisesRegex(composer.CompositionError, "Unconfigured.*fixture"):
            composer.compose_document(document("print(fixture)", setup="fixture = 10"))
        result, _ = composer.compose_document(document('print("independent")'))
        self.assertIn('print("independent")', result)

    def test_nested_global_audit_respects_function_locals(self):
        code = 'def transform(value):\n    local = value + fixture\n    return local\nprint(transform(2))'
        self.assertEqual(composer.external_names(code), {"fixture"})


class HelperTests(unittest.TestCase):
    def test_select_exact_helper_version_and_no_demo_call(self):
        text = document('def calculate(x):\n    return x + 1\nprint(calculate(3))')
        text += '''<span id="data-lab-test-02"></span>
::: solution
#### Cách 1: Different version
```python
def calculate(x):
    return x + 99
print(calculate(8))
```
:::
'''
        source = composer.Source(text)
        helper = source.select(composer.helper("data-lab-test-01", "calculate"))
        self.assertIn("return x + 1", helper)
        self.assertNotIn("99", helper)
        self.assertNotIn("print", helper)
        self.assertNotIn("calculate(3)", helper)

    def test_fixture_mutations_are_explicit(self):
        source = composer.Source(document('print("ok")', setup='items = []\nitems.append(1)\nprint("do not copy")'))
        self.assertNotIn("append", source.select(composer.setup("items")))
        prepared = source.select(composer.setup("items", mutations=["items"]))
        self.assertIn("items.append(1)", prepared)
        self.assertNotIn("print", prepared)

    def test_fixture_loop_mutations_require_explicit_root(self):
        source = composer.Source(document('print("ok")', setup='rows = []\nfor value in range(3):\n    rows.append(value)'))
        self.assertNotIn("for value", source.select(composer.setup("rows")))
        fixture = source.select(composer.setup("rows", mutations=["rows"]))
        namespace = {}
        exec(fixture, namespace)
        self.assertEqual(namespace["rows"], [0, 1, 2])

    def test_selected_class_keeps_no_instance_demo(self):
        source = composer.Source(document('class Schema:\n    field = "value"\nprint(Schema.field)'))
        definition = source.select(composer.helper("data-lab-test-01", "Schema"))
        self.assertIn("class Schema:", definition)
        self.assertNotIn("print", definition)

    def test_prelude_import_runs_before_authored_body_import(self):
        key = ("data-lab-test-01", 1)
        composer.ASSETS["test.path"] = composer.Asset(code='fixture = Path("sample.csv")')
        composer.REGISTRY[key] = composer.Plan(("test.path",))
        try:
            _, programs = composer.compose_document(document('from pathlib import Path\nprint(fixture.name)'))
            record = composer.execute_program(programs[0][1])
            self.assertTrue(record["passed"], record)
        finally:
            del composer.REGISTRY[key]
            del composer.ASSETS["test.path"]


class ExecutionTests(unittest.TestCase):
    def test_processes_have_fresh_namespaces_and_working_directories(self):
        first = composer.execute_program('from pathlib import Path\nsecret = 7\nPath("state.txt").write_text("private")\nprint(secret)')
        self.assertTrue(first["passed"])
        self.assertIn("state.txt", first["artifacts"])
        second = composer.execute_program('from pathlib import Path\nassert "secret" not in globals()\nassert not Path("state.txt").exists()\nassert "display" not in globals()\nprint("clean")')
        self.assertTrue(second["passed"], second)
        missing = composer.execute_program('display("must not receive an injected stub")')
        self.assertFalse(missing["passed"])
        self.assertIn("NameError", missing["stderr"])

    def test_explicit_file_preparation_produces_runnable_program(self):
        key = ("data-lab-test-01", 1)
        composer.ASSETS["test.csv"] = composer.Asset(code='from pathlib import Path\nPath("input.csv").write_text("value\\n7\\n", encoding="utf-8")')
        composer.REGISTRY[key] = composer.Plan(("test.csv",))
        try:
            text = document('import csv\nwith open("input.csv", encoding="utf-8") as stream:\n    print(next(csv.DictReader(stream))["value"])')
            _, programs = composer.compose_document(text)
            record = composer.execute_program(programs[0][1])
            self.assertTrue(record["passed"], record)
            self.assertEqual(record["stdout"].strip(), "7")
        finally:
            del composer.REGISTRY[key]
            del composer.ASSETS["test.csv"]

    def test_silent_assignment_is_not_visible_output(self):
        self.assertFalse(composer.execute_program("value = 3")["passed"])


if __name__ == "__main__":
    unittest.main()
