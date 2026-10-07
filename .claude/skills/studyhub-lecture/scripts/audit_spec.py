#!/usr/bin/env python3
"""Audit declared course structure; does not certify pedagogy or visual quality."""
import argparse
import hashlib
import json
import math
import sys
import unicodedata
from pathlib import Path


def audit(spec, asset_root=None):
    errors, warnings = [], []

    def problem(code, where, message, warning=False):
        (warnings if warning else errors).append(
            {"code": code, "where": where, "message": message})

    def nonempty(value):
        return isinstance(value, str) and bool(value.strip())

    def string(row, key, where):
        if not nonempty(row.get(key)):
            problem("MISSING_TEXT", where, f"Expected nonempty {key}.")

    def rows(key):
        value = spec.get(key)
        if not isinstance(value, list):
            problem("BAD_LIST", key, "Expected a list.")
            return []
        valid = []
        for n, row in enumerate(value):
            if not isinstance(row, dict):
                problem("BAD_RECORD", f"{key}[{n}]", "Expected an object.")
            else:
                valid.append(row)
        return valid

    def ids(row, key, where):
        value = row.get(key, [])
        if not isinstance(value, list):
            problem("BAD_ID_LIST", where, f"{key} must be a list.")
            return []
        valid = []
        for item in value:
            if not nonempty(item):
                problem("BAD_ID", where, f"Invalid item in {key}.")
            elif item in valid:
                problem("DUPLICATE_REFERENCE", where, f"Repeated {item} in {key}.")
            else:
                valid.append(item)
        return valid

    def index(records, name):
        result = {}
        for n, row in enumerate(records):
            ident = row.get("id")
            if not nonempty(ident):
                problem("MISSING_ID", f"{name}[{n}]", "Expected a nonempty id.")
            elif ident in result:
                problem("DUPLICATE_ID", name, f"Duplicate id: {ident}.")
            else:
                result[ident] = row
        return result

    def enum(row, key, allowed, where):
        value = row.get(key)
        if not isinstance(value, str) or value not in allowed:
            problem("BAD_ENUM", where, f"{key} must be one of {sorted(allowed)}.")

    root = Path(asset_root).resolve() if asset_root else None

    def asset(value, where):
        if not nonempty(value):
            problem("MISSING_ASSET", where, "Expected a nonempty asset reference.")
            return
        if root is None:
            return
        if value.startswith(("https://", "http://", "data:")):
            problem("EXTERNAL_ASSET_UNCHECKED", where,
                    "External asset availability was not checked.", True)
            return
        target = (root / value).resolve()
        if not target.is_relative_to(root):
            problem("ASSET_OUTSIDE_ROOT", where, "Asset resolves outside asset root.")
        elif not target.is_file():
            problem("ASSET_NOT_FOUND", where, f"Missing asset: {value}.")

    string(spec, "skill_version", "root")
    config = spec.get("config")
    if not isinstance(config, dict):
        problem("BAD_CONFIG", "config", "Expected an object.")
        config = {}
    string(config, "target_language", "config")
    enum(config, "delivery_mode",
         {"live-with-study-companion", "live-only", "self-study"}, "config")
    lecture_rows, source_rows, figure_rows, term_rows, slide_rows = (
        rows(k) for k in ("lectures", "source_units", "source_visuals", "glossary", "slides"))
    lectures = index(lecture_rows, "lectures")
    sources = index(source_rows, "source_units")
    figures = index(figure_rows, "source_visuals")
    terms = index(term_rows, "glossary")
    slides = index(slide_rows, "slides")
    order = {ident: n for n, ident in enumerate(slides)}
    if not slide_rows:
        problem("EMPTY_COURSE", "slides", "No slides.")
    for ident, row in terms.items():
        string(row, "canonical", ident)
    known_core = set(ids(config, "assumed_term_ids", "config"))
    for ident in known_core - set(terms):
        problem("UNKNOWN_ASSUMED_TERM", "config", f"Unknown term: {ident}.")
    known_all = set(known_core)
    source_usage = {ident: set() for ident in sources}
    figure_usage = {ident: set() for ident in figures}
    duration = {ident: 0.0 for ident in lectures}
    missing_duration = set()

    for ident, row in lectures.items():
        string(row, "title", ident)
        minutes = row.get("session_minutes")
        if minutes is not None and (isinstance(minutes, bool)
                or not isinstance(minutes, (float, int))
                or not math.isfinite(minutes) or minutes <= 0):
            problem("BAD_SESSION_TIME", ident, "session_minutes must be positive or null.")

    for sid, slide in slides.items():
        for key in ("lecture_id", "title", "learning_goal", "role"):
            string(slide, key, sid)
        enum(slide, "layer", {"core", "appendix"}, sid)
        lecture_id = slide.get("lecture_id")
        if not isinstance(lecture_id, str) or lecture_id not in lectures:
            problem("UNKNOWN_LECTURE", sid, "lecture_id does not resolve.")
        for source_id in ids(slide, "source_unit_ids", sid):
            if source_id not in sources:
                problem("UNKNOWN_SOURCE", sid, f"Unknown source: {source_id}.")
            else:
                source_usage[source_id].add(sid)
        for prereq in ids(slide, "prerequisite_slide_ids", sid):
            if prereq not in slides:
                problem("UNKNOWN_PREREQUISITE", sid, f"Unknown slide: {prereq}.")
            elif order[prereq] >= order[sid]:
                problem("FORWARD_PREREQUISITE", sid, f"Prerequisite {prereq} is not earlier.")
            elif slide.get("layer") == "core" and slides[prereq].get("layer") != "core":
                problem("CORE_DEPENDS_ON_APPENDIX", sid, f"Prerequisite {prereq} is in appendix.")

        introduced = set(ids(slide, "introduced_term_ids", sid))
        used = set(ids(slide, "used_term_ids", sid))
        for tid in (introduced | used) - set(terms):
            problem("UNKNOWN_TERM", sid, f"Unknown term: {tid}.")
        available = known_core if slide.get("layer") == "core" else known_all
        for tid in used - available - introduced:
            problem("TERM_BEFORE_INTRODUCTION", sid, f"Term {tid} is used before introduction.")
        if slide.get("layer") == "core":
            known_core.update(introduced)
        known_all.update(introduced)

        body = slide.get("body", [])
        visuals = slide.get("visuals", [])
        if not isinstance(body, list):
            problem("BAD_BODY", sid, "body must be a list.")
            body = []
        if not isinstance(visuals, list):
            problem("BAD_VISUALS", sid, "visuals must be a list.")
            visuals = []
        checkpoint = slide.get("checkpoint")
        if not body and not visuals and not isinstance(checkpoint, dict):
            problem("EMPTY_SLIDE", sid, "No body, visual, or checkpoint.")
        for n, block in enumerate(body):
            where = f"{sid}.body[{n}]"
            if not isinstance(block, dict):
                problem("BAD_BLOCK", where, "Expected an object.")
                continue
            provenance = block.get("provenance")
            if not isinstance(provenance, str) or provenance not in {
                    "source-adaptation", "pedagogical-addition"}:
                problem("MISSING_PROVENANCE", where,
                        "Set provenance to source-adaptation or pedagogical-addition.")
            block_sources = ids(block, "source_unit_ids", where)
            for source_id in block_sources:
                if source_id not in sources:
                    problem("UNKNOWN_BLOCK_SOURCE", where, f"Unknown source: {source_id}.")
                elif source_id not in slide.get("source_unit_ids", []):
                    problem("BLOCK_SOURCE_OUTSIDE_SLIDE", where,
                            f"{source_id} is not mapped to this slide.")
            if provenance == "source-adaptation" and not block_sources:
                problem("MISSING_BLOCK_SOURCE", where,
                        "A source-adaptation block needs at least one source unit.")
            if provenance == "pedagogical-addition":
                if not nonempty(block.get("rationale")):
                    problem("MISSING_PROVENANCE_RATIONALE", where,
                            "A pedagogical addition needs its instructional rationale.")
            enum(block, "type", {"text", "equation", "code", "table", "quote"}, where)
            kind = block.get("type")
            field = {"text": "text", "equation": "latex", "code": "code", "quote": "text"}.get(
                kind if isinstance(kind, str) else "")
            if field:
                string(block, field, where)
            if kind == "quote":
                string(block, "attribution", where)
            if kind == "table" and (not isinstance(block.get("rows"), list) or not block["rows"]):
                problem("EMPTY_TABLE", where, "Table needs rows.")

        visual_ids = set()
        for n, visual in enumerate(visuals):
            where = f"{sid}.visuals[{n}]"
            if not isinstance(visual, dict):
                problem("BAD_VISUAL", where, "Expected an object.")
                continue
            string(visual, "id", where)
            vid = visual.get("id")
            if isinstance(vid, str):
                if vid in visual_ids:
                    problem("DUPLICATE_VISUAL", where, f"Repeated visual: {vid}.")
                visual_ids.add(vid)
            string(visual, "claim", where)
            enum(visual, "kind", {"source", "supplementary"}, where)
            asset(visual.get("asset_ref"), where)
            if visual.get("kind") == "source":
                fid = visual.get("source_visual_id")
                if not isinstance(fid, str) or fid not in figures:
                    problem("UNKNOWN_SOURCE_VISUAL", where, "source_visual_id does not resolve.")
                else:
                    figure_usage[fid].add(sid)
                enum(visual, "preservation", {"original", "faithful-redraw"}, where)
                if visual.get("preservation") == "faithful-redraw":
                    string(visual, "verification_note", where)
            elif visual.get("kind") == "supplementary":
                string(visual, "provenance", where)

        if slide.get("role") == "checkpoint" and not isinstance(checkpoint, dict):
            problem("MISSING_CHECKPOINT", sid, "Checkpoint role needs checkpoint data.")
        if checkpoint is not None:
            if not isinstance(checkpoint, dict):
                problem("BAD_CHECKPOINT", sid, "checkpoint must be an object.")
            else:
                for key in ("prompt", "answer", "rationale", "anticipated_error", "feedback"):
                    string(checkpoint, key, f"{sid}.checkpoint")
                checkpoint_provenance = checkpoint.get("provenance")
                if not isinstance(checkpoint_provenance, str) or checkpoint_provenance not in {
                        "source-adaptation", "pedagogical-addition"}:
                    problem("MISSING_PROVENANCE", f"{sid}.checkpoint",
                            "Set checkpoint provenance to source-adaptation or pedagogical-addition.")
                checkpoint_sources = ids(checkpoint, "source_unit_ids", f"{sid}.checkpoint")
                for source_id in checkpoint_sources:
                    if source_id not in sources:
                        problem("UNKNOWN_BLOCK_SOURCE", f"{sid}.checkpoint",
                                f"Unknown source: {source_id}.")
                    elif source_id not in slide.get("source_unit_ids", []):
                        problem("BLOCK_SOURCE_OUTSIDE_SLIDE", f"{sid}.checkpoint",
                                f"{source_id} is not mapped to this slide.")
                if checkpoint_provenance == "source-adaptation" and not checkpoint_sources:
                    problem("MISSING_BLOCK_SOURCE", f"{sid}.checkpoint",
                            "A source-adaptation checkpoint needs at least one source unit.")
                if checkpoint_provenance == "pedagogical-addition" and not nonempty(
                        checkpoint.get("provenance_rationale")):
                    problem("MISSING_PROVENANCE_RATIONALE", f"{sid}.checkpoint",
                            "A pedagogical addition needs its instructional rationale.")
                enum(checkpoint, "answer_placement", {"next_slide", "after_response", "notes"}, sid)
                placement = checkpoint.get("answer_placement")
                if placement == "next_slide":
                    target = checkpoint.get("answer_slide_id")
                    following = [other for other in slides if order[other] > order[sid]
                                 and slides[other].get("lecture_id") == lecture_id
                                 and slides[other].get("layer") == slide.get("layer")]
                    if not isinstance(target, str) or not following or target != following[0]:
                        problem("BAD_ANSWER_TARGET", sid,
                                "Answer must be on the next slide in the same lecture and layer.")
                if placement == "notes":
                    if not nonempty(slide.get("speaker_notes")) and not nonempty(checkpoint.get("note_ref")):
                        problem("MISSING_ANSWER_NOTES", sid, "No answer note location.")
                    if config.get("delivery_mode") == "self-study":
                        problem("SELF_STUDY_HIDDEN_ANSWER", sid,
                                "Answer in instructor notes is inaccessible for self-study.")

        minutes = slide.get("estimated_minutes")
        if slide.get("layer") == "core" and isinstance(lecture_id, str) and lecture_id in lectures:
            if isinstance(minutes, (float, int)) and not isinstance(minutes, bool):
                if math.isfinite(minutes) and minutes >= 0:
                    duration[lecture_id] += minutes
                else:
                    problem("BAD_SLIDE_TIME", sid, "estimated_minutes must be finite and nonnegative.")
            elif minutes is not None:
                problem("BAD_SLIDE_TIME", sid, "estimated_minutes must be numeric.")
            else:
                missing_duration.add(lecture_id)

    for collection, usage, name in (
            (sources, source_usage, "source"), (figures, figure_usage, "source_visual")):
        for ident, row in collection.items():
            string(row, "location", ident)
            enum(row, "treatment", {"core", "appendix", "notes", "omitted"}, ident)
            treatment = row.get("treatment")
            listed = set(ids(row, "slide_ids", ident))
            actual = usage[ident]
            if name == "source":
                enum(row, "priority", {"essential", "important", "supporting", "optional"}, ident)
            if treatment != "core":
                string(row, "reason", ident)
            if listed != actual:
                problem("COVERAGE_MISMATCH", ident,
                        f"Declared {sorted(listed)}; actual {sorted(actual)}.")
            for sid in listed:
                if sid not in slides:
                    problem("UNKNOWN_COVERAGE_SLIDE", ident, f"Unknown slide: {sid}.")
            if treatment in {"core", "appendix"}:
                if not actual:
                    problem("UNCOVERED_UNIT", ident, f"{name} has no slide destination.")
                if not any(slides[sid].get("layer") == treatment for sid in actual):
                    problem("WRONG_COVERAGE_LAYER", ident,
                            f"No destination in {treatment} layer.")
            elif treatment in {"notes", "omitted"} and actual:
                problem("WRONG_TREATMENT", ident, "Notes/omitted unit is referenced on slides.")
            if treatment == "notes":
                string(row, "note_ref", ident)
            if name == "source" and row.get("priority") == "essential":
                if treatment != "core" or not any(slides[sid].get("layer") == "core" for sid in actual):
                    problem("ESSENTIAL_NOT_IN_CORE", ident, "Essential unit is missing from core.")
            if name == "source_visual" and actual:
                asset(row.get("original_asset_ref"), ident)

    for ident, lecture in lectures.items():
        limit = lecture.get("session_minutes")
        if isinstance(limit, (float, int)) and not isinstance(limit, bool) and limit > 0:
            if ident in missing_duration:
                problem("INCOMPLETE_TIME_ESTIMATE", ident,
                        "Core slides are missing time estimates.")
            if duration[ident] > limit:
                problem("SESSION_OVERLOAD", ident,
                        f"Estimated {duration[ident]:g} min exceeds {limit:g} min.")
        if not any(slide.get("lecture_id") == ident for slide in slides.values()):
            problem("EMPTY_LECTURE", ident, "No slides assigned.")
    if not any(isinstance(slide.get("checkpoint"), dict) for slide in slides.values()):
        problem("NO_DECLARED_CHECKPOINT", "slides",
                "No declared checkpoint; review goal-aligned practice manually.", True)
    if root is None:
        problem("ASSETS_NOT_CHECKED", "assets",
                "Pass --asset-root to check local asset files.", True)

    def normalize(value):
        if isinstance(value, str):
            return unicodedata.normalize("NFC", value)
        if isinstance(value, list):
            return [normalize(item) for item in value]
        if isinstance(value, dict):
            return {unicodedata.normalize("NFC", key): normalize(item)
                    for key, item in value.items()}
        return value

    canonical = json.dumps(normalize(spec), ensure_ascii=False, sort_keys=True,
                           separators=(",", ":"), allow_nan=False)
    return {
        "status": "structural-errors" if errors else "no-structural-errors-detected",
        "scope": "Declared structure only; semantic, language, and render QA remain required.",
        "spec_sha256": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
        "counts": {"lectures": len(lectures), "slides": len(slides),
                   "source_units": len(sources), "source_visuals": len(figures),
                   "errors": len(errors), "warnings": len(warnings)},
        "estimated_core_minutes": duration,
        "errors": errors,
        "warnings": warnings,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("--asset-root", type=Path)
    args = parser.parse_args()
    try:
        raw = args.spec.read_text(encoding="utf-8-sig")
        spec = json.loads(raw, parse_constant=lambda text: (_ for _ in ()).throw(
            ValueError(f"Nonstandard JSON constant: {text}")))
        if not isinstance(spec, dict):
            raise ValueError("Top-level JSON must be an object.")
        report = audit(spec, args.asset_root)
    except (OSError, ValueError, TypeError, RecursionError) as exc:
        print(json.dumps({"status": "input-error", "message": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(main())
