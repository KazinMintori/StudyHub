#!/usr/bin/env python3
"""Suggest Vietnamese teaching-language edits; never certifies semantics or authorship.

Reads a Markdown/text file (e.g. a StudyHub Notes page) or a slide-deck JSON spec and
reports *locations to re-read*. Every finding is a suggestion: keep the text when it is
a sourced quotation or a correct technical term.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

# Phrases that usually signal a translation or terminology slip in authored prose.
PHRASES = {
    "ánh xạ hợp đồng": "Trong lý thuyết điểm bất động, xem contraction mapping có nghĩa ánh xạ co; so định nghĩa trước khi sửa.",
    "hợp đồng tensor": "Phân biệt phép co tensor với nghĩa thỏa thuận; giữ chỉ số/miền tổng.",
    "biến miễn phí": "Trong toán, kiểm tra free variable theo lĩnh vực; không dịch theo nghĩa giá tiền.",
    "điều kiện tính dừng": "Kiểm tra thuật ngữ điều kiện dừng và hàm đang xét.",
    "hợp đồng nội dung": "Dùng yêu cầu cho phần nội dung hoặc kế hoạch giảng; đây là nhãn nội bộ, không phải thuật ngữ bài học.",
    "điểm hiện hành": "Gọi đúng điểm đang xét hoặc ký hiệu đã biết.",
    "chứng minh và vị trí dùng giả thiết": "Đặt câu hỏi và chỉ đúng bước dùng giả thiết.",
    "tạo bước đi": "Phân biệt hướng cập nhật, độ dài bước và độ dời.",
    "tự do dấu": "Trong lời giảng có thể nói 'không bị giới hạn dấu'; kiểm tra quy ước.",
    "thực hiện việc": "Xem có thể dùng động từ trực tiếp không.",
    "tiến hành": "Xem có thể dùng động từ trực tiếp không; giữ trích dẫn/thuật ngữ đúng.",
    "đóng vai trò then chốt": "Nêu tác dụng cụ thể thay lời đánh giá.",
    "mang lại cái nhìn sâu sắc": "Chỉ ra điều người học thực sự nhận ra.",
    "một cách tự nhiên": "Kiểm tra bước suy ra có đang bị giấu không.",
}

# Evaluation used instead of explanation (seen on StudyHub pages). Word-boundary matched.
EVALUATIVE = {
    "cực kỳ": "Đánh giá thay giải thích: nói tác dụng hoặc lý do cụ thể.",
    "vô cùng": "Đánh giá thay giải thích: nói tác dụng hoặc lý do cụ thể.",
    "đây chính là": "Xem câu có đang khẳng định thay vì chỉ ra quan hệ không.",
    "then chốt": "Nêu bước này làm được gì, thay vì gọi nó then chốt.",
    "tinh hoa": "Cụ thể hóa thành câu hỏi hoặc phương pháp của môn.",
}

# Claims about how often learners err, which need evidence.
FREQUENCY = (
    "cực kỳ phổ biến", "rất phổ biến", "lỗi thường gặp", "sai lầm thường gặp", "thường gặp nhất",
    "hay nhầm", "hay mắc", "rất nhiều sinh viên", "nhiều sinh viên", "phần lớn sinh viên", "đa số sinh viên",
)

# Labels that promise depth ("Bản chất: …") before a general claim.
LABEL_RE = re.compile(r"^(?:#{2,6}\s+|:::\s*\w+\s+|\*\*)?(?:bản chất|tinh hoa|trực giác then chốt|chân lý)\b", re.IGNORECASE)
OPENERS = ("ta có thể thấy rằng", "điều quan trọng ở đây", "điều đáng chú ý là", "trực giác đằng sau")
# A blockquote that attributes words to a named person: “…” — Name / "…" — Name / "... đã nói"
QUOTE_ATTRIBUTION_RE = re.compile(r"[\"“”«].{8,}[\"“”»].*(?:—|–|-{2})\s*\S|(?:đã nói|từng nói|đã nghĩ|từng viết)", re.IGNORECASE)
INLINE_MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$\n]+\$|`[^`\n]+`")
BOLD_RE = re.compile(r"\*\*[^*\n]+\*\*")
OVERLOAD_WORDS = 55
BOLD_LIMIT = 4


def strip_frontmatter(text):
    """Return text with a leading YAML frontmatter replaced by blank lines (line numbers kept)."""
    match = re.match(r"\A﻿?---\r?\n.*?\r?\n---\r?\n", text, re.DOTALL)
    if not match:
        return text
    return "\n" * match.group(0).count("\n") + text[match.end():]


def markdown_lines(text, include_quotes=False):
    """Yield (line_number, raw, is_quote) for prose lines outside code fences."""
    fence = None
    for line_number, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        match = re.match(r"^(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = (marker[0], len(marker))
            elif marker[0] == fence[0] and len(marker) >= fence[1]:
                fence = None
            continue
        if fence or not line:
            continue
        quote = line.startswith(">")
        if quote and not include_quotes:
            continue
        yield (line_number, raw, quote) if include_quotes else (line_number, raw)


def authored_sections(data):
    if not isinstance(data, dict) or not isinstance(data.get("slides"), list):
        raise ValueError("JSON input must be a course spec with a slides array; raw source is not linted.")
    for n, slide in enumerate(data["slides"]):
        if not isinstance(slide, dict):
            raise ValueError(f"slides[{n}] must be an object.")
        ident = slide.get("id", f"slides[{n}]")
        for key in ("title", "speaker_notes", "next_bridge", "study_note", "study_text"):
            if isinstance(slide.get(key), str):
                yield f"{ident}.{key}", slide[key]
        for k, block in enumerate(slide.get("body", [])):
            if isinstance(block, dict) and block.get("type") == "text" and isinstance(block.get("text"), str):
                yield f"{ident}.body[{k}].text", block["text"]
        checkpoint = slide.get("checkpoint", {})
        if isinstance(checkpoint, dict):
            for key in ("prompt", "answer", "rationale", "feedback"):
                if isinstance(checkpoint.get(key), str):
                    yield f"{ident}.checkpoint.{key}", checkpoint[key]


def _has_word(lower, phrase):
    return re.search(rf"(?<![\w]){re.escape(phrase)}(?![\w])", lower) is not None


def review(sections):
    findings, opener_locations = [], {phrase: [] for phrase in OPENERS}
    for section, text in sections:
        text = strip_frontmatter(unicodedata.normalize("NFC", text))
        for line_number, raw, quote in markdown_lines(text, include_quotes=True):
            where = f"{section}:line {line_number}"
            lower = raw.casefold()
            if quote:
                # Quotations are not edited for voice, but an attributed quote must have a checkable source.
                if QUOTE_ATTRIBUTION_RE.search(raw):
                    findings.append({"code": "CHECK_QUOTE_SOURCE", "where": where, "text": raw.strip(),
                                     "suggestion": "Câu trích gán cho một người: giữ chỉ khi dẫn được nguồn kiểm chứng; không thì bỏ hoặc mở bài bằng câu hỏi của bài học."})
                continue
            for phrase, suggestion in PHRASES.items():
                if phrase in lower:
                    findings.append({"code": "CONTEXTUAL_PHRASE", "where": where, "phrase": phrase, "suggestion": suggestion})
            for phrase, suggestion in EVALUATIVE.items():
                if _has_word(lower, phrase):
                    findings.append({"code": "EVALUATIVE_PHRASE", "where": where, "phrase": phrase, "suggestion": suggestion})
            for phrase in FREQUENCY:
                if _has_word(lower, phrase):
                    findings.append({"code": "UNSUPPORTED_FREQUENCY", "where": where, "phrase": phrase,
                                     "suggestion": "Khẳng định tần suất cần căn cứ; có thể viết 'một cách hiểu dễ nhầm là…' kèm ví dụ."})
                    break
            if LABEL_RE.search(raw.strip()):
                findings.append({"code": "DEPTH_LABEL", "where": where, "text": raw.strip(),
                                 "suggestion": "Nhãn hứa chiều sâu: thay bằng câu hỏi cụ thể mà khái niệm trả lời, rồi trả lời nó."})
            bold = BOLD_RE.findall(raw)
            if len(bold) >= BOLD_LIMIT:
                findings.append({"code": "BOLD_DENSITY", "where": where, "count": len(bold),
                                 "suggestion": "In đậm tên khái niệm khi định nghĩa hoặc điều kiện quyết định; bớt phần còn lại."})
            for phrase in OPENERS:
                if phrase in lower:
                    opener_locations[phrase].append(where)
            prose = INLINE_MATH_RE.sub(" X ", raw)
            for sentence in re.split(r"(?<=[.!?])\s+", prose):
                if len(sentence.split()) > OVERLOAD_WORDS:
                    findings.append({"code": "POSSIBLE_OVERLOAD", "where": where, "text": sentence.strip(),
                                     "suggestion": "Xem câu có đổi nhiệm vụ tư duy không; ngưỡng từ chỉ là heuristic (công thức tính là một từ)."})
    for phrase, locations in opener_locations.items():
        if len(locations) >= 3:
            findings.append({"code": "REPEATED_OPENER", "phrase": phrase, "where": locations,
                             "suggestion": "Xem mật độ lặp và lý do; không thay bằng khuôn sáo mới."})
    return {"status": "review-suggestions-only",
            "scope": "Heuristics for Vietnamese authored prose; code is skipped, quotations are only checked for attribution. No semantic, pedagogy, authorship or render certification.",
            "findings": findings}


def as_text(report):
    findings = report["findings"]
    if not findings:
        return "Không có gợi ý nào. Điều này KHÔNG có nghĩa lời giảng đã đạt: vẫn phải đọc lại nghĩa và bước nối.\n"
    lines = [f"{len(findings)} vị trí nên đọc lại (chỉ là gợi ý, không phải lỗi chắc chắn):"]
    for f in findings:
        where = ", ".join(f["where"]) if isinstance(f["where"], list) else f["where"]
        detail = f.get("phrase") or f.get("text") or f.get("count", "")
        detail = str(detail)
        if len(detail) > 110:
            detail = detail[:107] + "…"
        lines.append(f"- [{f['code']}] {where}: {detail}\n    → {f['suggestion']}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args()
    try:
        raw = args.input.read_text(encoding="utf-8-sig")
        sections = authored_sections(json.loads(raw)) if args.input.suffix.lower() == ".json" else [(args.input.name, raw)]
        report = review(sections)
        rendered = as_text(report) if args.format == "text" else json.dumps(report, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        else:
            print(rendered, end="")
    except (OSError, ValueError, TypeError) as exc:
        print(f"Input/output error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
