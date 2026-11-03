"""Execute published examples, including negative and backtracking cases."""
from pathlib import Path
import json
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "docs/bieu-dien-tri-thuc/bai-giang"
OUTPUT = ROOT / "qa/knowledge-09-11"
OUTPUT.mkdir(parents=True, exist_ok=True)
FENCE = chr(96) * 3


def blocks(lesson, topic, language):
    source = (BASE / lesson / (topic + ".md")).read_text(encoding="utf8")
    return re.findall(r"^\s*" + FENCE + language + r"\s*\n(.*?)^\s*" + FENCE, source, re.M | re.S)


def run_prolog(name, program, tests):
    with tempfile.TemporaryDirectory(prefix="studyhub-prolog-") as directory:
        target = Path(directory) / "example.pl"
        target.write_text(program + "\n:- begin_tests(lecture).\n" + tests +
                          "\n:- end_tests(lecture).\n", encoding="utf8")
        result = subprocess.run(
            ["swipl", "-q", "-s", str(target), "-g", "run_tests,halt", "-t", "halt(1)"],
            text=True, capture_output=True, timeout=30, encoding="utf8")
        if result.returncode:
            raise AssertionError(name + "\n" + result.stdout + result.stderr)
        return {"example": name, "status": "passed", "output": result.stderr.strip()}


results = []
arithmetic = blocks("09-prolog", "so-hoc-va-dieu-kien", "prolog")
gcd = next(code for code in arithmetic if re.search(r"^gcd\(", code, re.M))
results.append(run_prolog("published Euclid", gcd, """
test(gcd_forward) :- findall(G, gcd(10,15,G), [5]).
test(gcd_zero) :- findall(G, gcd(15,0,G), [15]).
test(gcd_both_zero) :- findall(G, gcd(0,0,G), [0]).
test(gcd_negative, [fail]) :- gcd(-1,3,_).
"""))
lists = blocks("09-prolog", "danh-sach-va-de-quy", "prolog")
last = next(code for code in lists if "findLast(" in code)
results.append(run_prolog("published last element", last, """
test(last) :- findall(X, findLast([2,3,5,7],X), [7]).
test(empty, [fail]) :- findLast([], _).
"""))
dedup = [code for code in lists if "removeDups" in code]
for index, code in enumerate(dedup):
    query = ("test(no_spurious) :- findall(R, removeDups([a,b,a],R), [[b,a]]).\n"
             "test(empty) :- findall(R, removeDups([],R), [[]]).") if index > 0 else """
    test(counterexample) :- findall(R, removeDups_unsafe([a,b,a],R), Answers),
                        member([a,b,a], Answers).
"""
    if index > 0:
        query += "\ntest(guarded) :- findall(R,removeDups_guarded([a,a,a],R),[[a]])."
    results.append(run_prolog("published dedup variant " + str(index), code, query))
diff = next(code for code in lists if re.search(r"^diff\(", code, re.M))
results.append(run_prolog("published difference", diff, """
test(difference) :- findall(R,diff([a,b,a,c],[b],R),[[a,a,c]]).
test(empty) :- findall(R,diff([],[],R),[[]]).
"""))
io = blocks("09-prolog", "dau-cat-va-nhap-xuat", "prolog")
hanoi = next(code for code in io if re.search(r"^move\(", code, re.M))
results.append(run_prolog("published Hanoi", hanoi, """
test(three_disks) :- with_output_to(string(S), move(3,a,c,b)),
                    split_string(S, "\\n", "\\n", Lines), length(Lines, 7).
test(one_disk) :- with_output_to(string(S), move(1,a,c,b)),
                 sub_string(S, _, _, _, "a").
test(invalid, [fail]) :- move(-1,a,c,b).
"""))
facts = blocks("09-prolog", "sld-va-quay-lui", "prolog")[0] + """
student_cut(X) :- teaches(kirke,C), !, studies(X,C), eligible(X).
"""
results.append(run_prolog("cut trace agrees with real SWI-Prolog", facts, """
test(ordinary) :- findall(X,student(X),[charlie,olivia,jack]).
test(cut) :- findall(X,student_cut(X),[charlie,olivia]).
test(negation_unbound, [fail]) :- _X \\= _Y.
test(dif_delayed) :- dif(X,Y), X=a, Y=b.
test(arithmetic) :- X is 2+3, X=:=5.
test(unification) :- X=2+3, X\\==5.
"""))
family = blocks("09-prolog", "cu-phap-va-truy-van", "prolog")[0]
results.append(run_prolog("published family", family, """
test(mother) :- mother(marge,lisa).
test(descendants) :- findall(X,ancestor(homer,X),[bart,lisa,maggie]).
"""))
factorial = next(code for code in arithmetic if "factorial(" in code)
results.append(run_prolog("published factorial", factorial, """
test(five) :- findall(X,factorial(5,X),[120]).
test(zero) :- findall(X,factorial(0,X),[1]).
test(negative, [fail]) :- factorial(-1,_).
"""))
flatten = next(code for code in lists if "flatten_list(" in code)
results.append(run_prolog("published flatten", flatten, """
test(nested) :- findall(X,flatten_list([a,[b,[c,d]],e],X),[[a,b,c,d,e]]).
test(empty) :- findall(X,flatten_list([],X),[[]]).
"""))
dynamic = blocks("09-prolog", "tri-thuc-dong", "prolog")
pacman = next(code for code in dynamic if "at(pacman" in code)
results.append(run_prolog("published state update", pacman, """
test(update) :- up, findall([X,Y],at(pacman,X,Y),[[1,2]]).
test(no_undo) :- (up,fail;true), findall([X,Y],at(pacman,X,Y),[[1,3]]).
"""))
path = next(code for code in dynamic if "find_path(" in code)
results.append(run_prolog("published path cleanup", path, """
test(path) :- find_path(a,d,[a,b,c,d]), \\+ visited(_).
test(failure_cleanup) :- \\+ find_path(a,z,_), \\+ visited(_).
test(repeat) :- find_path(a,d,_), find_path(a,d,_), \\+ visited(_).
"""))
for lesson in ["09-prolog", "10-bieu-dien-tri-thuc", "11-mdp"]:
    for file in (BASE / lesson).glob("*.md"):
        for code in blocks(lesson, file.stem, "python"):
            exec(compile(code, str(file), "exec"), {})
            results.append({"example": str(file.relative_to(ROOT)), "status": "passed"})
(OUTPUT / "examples.json").write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf8")
print(json.dumps({"passed": len(results), "results": results}, ensure_ascii=False))
