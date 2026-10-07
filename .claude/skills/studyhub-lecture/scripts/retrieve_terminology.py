#!/usr/bin/env python3
"""Retrieve local EN/VI term senses and teaching examples; no translation or network."""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

REFERENCES = Path(__file__).resolve().parents[1] / "references"


def normalized(value):
    return " ".join(unicodedata.normalize("NFC", value).casefold().split())


def read_memory(root=REFERENCES):
    memory = json.loads((root / "terminology-memory.json").read_text(encoding="utf-8-sig"))
    if not isinstance(memory, dict) or not isinstance(memory.get("terms"), list) or not isinstance(memory.get("sources"), dict):
        raise ValueError("Memory must have terms array and sources object.")
    ids = set()
    for term in memory["terms"]:
        if not isinstance(term, dict):
            raise ValueError("Term record must be an object.")
        for key in ("id", "domain", "technical_vi", "concept", "lecture_vi"):
            if not isinstance(term.get(key), str) or not term[key].strip():
                raise ValueError(f"Term needs nonempty {key}.")
        if term["id"] in ids:
            raise ValueError(f"Duplicate term id: {term['id']}")
        ids.add(term["id"])
        for key in ("english", "variants", "avoid_in_this_sense", "protected_meaning"):
            values = term.get(key)
            if not isinstance(values, list) or any(not isinstance(x, str) or not x.strip() for x in values):
                raise ValueError(f"{term['id']}: {key} must be a string array.")
        if not term["english"] or not term["protected_meaning"]:
            raise ValueError(f"{term['id']}: missing alias or protected meaning.")
        evidence = term.get("evidence")
        if not isinstance(evidence, dict) or not isinstance(evidence.get("vi_usage"), str):
            raise ValueError(f"{term['id']}: evidence required.")
        if not isinstance(evidence.get("source_ids"), list) or any(ref not in memory["sources"] for ref in evidence["source_ids"]):
            raise ValueError(f"{term['id']}: unknown source id.")
    examples = []
    for number, line in enumerate((root / "translation-examples.jsonl").read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        record = json.loads(line)
        if not isinstance(record, dict) or not isinstance(record.get("term_ids"), list):
            raise ValueError(f"Example line {number}: bad record.")
        if any(ref not in ids for ref in record["term_ids"]):
            raise ValueError(f"Example line {number}: unknown term id.")
        for key in ("id", "domain", "source_en", "technical_vi", "lecture_vi", "why_bad", "split"):
            if not isinstance(record.get(key), str) or not record[key].strip():
                raise ValueError(f"Example line {number}: missing {key}.")
        examples.append(record)
    return memory, examples


def retrieve(text, domain=None, limit=6, example_limit=3, root=REFERENCES):
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Expected nonempty text.")
    if domain is not None and (not isinstance(domain, str) or not domain.strip()):
        raise ValueError("domain must be a nonempty string when supplied.")
    for value in (limit, example_limit):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Limits must be nonnegative integers.")
    if limit == 0:
        raise ValueError("Term limit must be positive.")
    memory, examples = read_memory(root)
    terms = {term["id"]: term for term in memory["terms"]}
    aliases = {}
    for term in terms.values():
        for raw in term["english"] + [term["technical_vi"]]:
            aliases.setdefault(normalized(raw), set()).add(term["id"])
    value = normalized(text)
    matches = []
    for phrase, ids in aliases.items():
        for match in re.finditer(r"(?<!\w)" + re.escape(phrase) + r"(?!\w)", value):
            matches.append((match.start(), match.end(), phrase, ids))
    # Suppress a short alias contained in a more specific phrase before domain filtering.
    matches = [item for item in matches if not any(
        longer[0] <= item[0] and item[1] <= longer[1] and longer[1] - longer[0] > item[1] - item[0]
        for longer in matches)]
    hits, ambiguities, conflicts = {}, [], []
    for start, end, phrase, ids in sorted(matches, key=lambda item: (item[0], -(item[1] - item[0]))):
        candidates = sorted(ids)
        selected = [ident for ident in candidates if domain is None or terms[ident]["domain"] == domain]
        if not selected:
            conflict = {"phrase": phrase, "requested_domain": domain, "candidate_ids": candidates}
            if conflict not in conflicts:
                conflicts.append(conflict)
            continue
        if len(selected) > 1:
            ambiguity = {"phrase": phrase, "candidate_ids": selected, "action": "Resolve from source context before translating; do not silently choose."}
            if ambiguity not in ambiguities:
                ambiguities.append(ambiguity)
        for ident in selected:
            hits.setdefault(ident, set()).add(phrase)
    ordered = sorted(hits, key=lambda ident: (-max(len(x) for x in hits[ident]), ident))
    chosen = ordered[:limit]
    ambiguous_ids = {ident for item in ambiguities for ident in item["candidate_ids"]}
    retrieved = [dict(terms[ident], matched_phrases=sorted(hits[ident]),
                      selection_status="needs-context" if ident in ambiguous_ids else
                      ("candidate-from-phrase-and-domain" if domain is not None else "candidate-needs-domain-review"))
                 for ident in chosen]
    source_ids = {ref for term in retrieved for ref in term["evidence"]["source_ids"]}
    # Prompt examples only. Identical source texts are excluded; semantic near-duplicates still need human split review.
    example_candidates = [record for record in examples if record["split"] == "prompt-example"
                          and (domain is None or record["domain"] == domain)
                          and set(record["term_ids"]) & (set(chosen) - ambiguous_ids)
                          and normalized(record["source_en"]) not in value]
    example_candidates.sort(key=lambda record: (-len(set(record["term_ids"]) & set(chosen)), record["id"]))
    return {"status": "local-retrieval-only", "domain": domain, "terms": retrieved,
            "examples": example_candidates[:example_limit], "ambiguities": ambiguities, "domain_conflicts": conflicts,
            "truncated": len(chosen) < len(ordered), "total_matching_terms": len(ordered),
            "sources": {ref: memory["sources"][ref] for ref in sorted(source_ids)},
            "limits": "Lexical matching only; meaning, Vietnamese usage and semantic fidelity still require review. No automatic substitutions."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--text")
    group.add_argument("--input", type=Path)
    parser.add_argument("--domain", help="Explicit domain: optimization, fixed-point or tensor-algebra. Unknown domains do not fall back to another sense.")
    parser.add_argument("--limit", type=int, default=6)
    parser.add_argument("--example-limit", type=int, default=3)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = args.input.read_text(encoding="utf-8-sig") if args.input else args.text
        result = json.dumps(retrieve(raw, args.domain, args.limit, args.example_limit), ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(result, encoding="utf-8")
        else:
            print(result, end="")
    except (OSError, ValueError, TypeError) as exc:
        print(f"Input/output error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
