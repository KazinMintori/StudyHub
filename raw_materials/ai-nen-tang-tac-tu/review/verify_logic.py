"""Independent checks of specific source examples, not translation certification.

Sources: ArtInt3e.Ch5.S3, Ch5.S6, Ch15.S5. Run without external packages.
"""
from itertools import combinations, product


def assignments(names):
    return [dict(zip(names, values)) for values in product([False, True], repeat=len(names))]


def rule(head, *premises):
    return not all(premises) or head


# §5.3: Definite clause a <- b ∧ c ∧ d has exactly one positive literal.
for model in assignments("abcd"):
    a, b, c, d = (model[x] for x in "abcd")
    assert rule(a, b, c, d) == (a or not b or not c or not d)

# Example 5.17: false <- a ∧ b; a <- c; b <- c entails ¬c.
models_517 = [m for m in assignments("abc")
              if rule(False, m["a"], m["b"]) and rule(m["a"], m["c"]) and rule(m["b"], m["c"])]
assert models_517 and all(not m["c"] for m in models_517)

# Example 5.18: Cannot conclude ¬c or ¬d individually from their disjunction.
models_518 = [m for m in assignments("abcde") if
              rule(False, m["a"], m["b"]) and rule(m["a"], m["c"])
              and rule(m["b"], m["d"]) and rule(m["b"], m["e"])]
assert models_518 and all(not m["c"] or not m["d"] for m in models_518)
assert any(m["c"] for m in models_518) and any(m["d"] for m in models_518)


def substitute(expression, bindings):
    """Simultaneous application: Do not re-substitute a replacement term."""
    if isinstance(expression, tuple):
        return tuple(substitute(term, bindings) for term in expression)
    return bindings.get(expression, expression)


# Examples 15.15–15.16: Repeated variables bind consistently, all at once.
assert substitute(("borders", "peru", "X"), {"X": "chile"}) == ("borders", "peru", "chile")
assert substitute(("p", "X", "X", "Y", "Y", "Z"), {"X": "Z", "Y": "brazil"}) == (
    "p", "Z", "Z", "brazil", "brazil", "Z")
bindings = {"X": "chile", "Y": "peru"}
assert substitute(("borders", "peru", "X"), bindings) == substitute(("borders", "Y", "chile"), bindings)
assert substitute(("t", "a", "Y", "c"), {"X": "a", "Y": "b"}) == substitute(
    ("t", "X", "b", "c"), {"X": "a", "Y": "b"})

# ∀x∃y R(x,y) and ∃y∀x R(x,y) are different even in a two-element domain.
domain = [0, 1]
relation = {(0, 0), (1, 1)}
assert all(any((x, y) in relation for y in domain) for x in domain)
assert not any(all((x, y) in relation for x in domain) for y in domain)

# Example 5.5: Four indicator variables need six pairwise exclusions plus
# one covering clause. The five extra clauses encode A < B exactly.
assert len(list(combinations(range(4), 2))) + 1 == 7
legal = set()
for av in product([False, True], repeat=4):
    for bv in product([False, True], repeat=4):
        if (sum(av) == sum(bv) == 1 and not av[3] and not bv[0]
                and not (av[1] and bv[1]) and not (av[2] and bv[2])
                and not (av[2] and bv[1])):
            legal.add((av.index(True) + 1, bv.index(True) + 1))
assert legal == {(a, b) for a in range(1, 5) for b in range(1, 5) if a < b}

print("PASS: Definite-clause equivalence (16 assignments), Horn examples 5.17/5.18,")
print("      simultaneous substitutions and unifiers 15.15/15.16, quantifier order.")
print("      seven exactly-one clauses and five-clause encoding of A < B (5.5).")
