#!/usr/bin/env python3
"""Suggest Vietnamese teaching-language edits; never certifies semantics or authorship."""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

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
OPENERS = ("ta có thể thấy rằng", "điều quan trọng ở đây", "điều đáng chú ý là", "trực giác đằng sau")


def markdown_lines(text):
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
        if fence or line.startswith(">") or not line:
            continue
        yield line_number, raw


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


def review(sections):
    findings, opener_locations = [], {phrase: [] for phrase in OPENERS}
    for section, text in sections:
        for line_number, raw in markdown_lines(text):
            lower = unicodedata.normalize("NFC", raw).casefold()
            where = f"{section}:line {line_number}"
            for phrase, suggestion in PHRASES.items():
                if phrase in lower:
                    findings.append({"code": "CONTEXTUAL_PHRASE", "where": where, "phrase": phrase, "suggestion": suggestion})
            for phrase in OPENERS:
                if phrase in lower:
                    opener_locations[phrase].append(where)
            for sentence in re.split(r"(?<=[.!?])\s+", raw):
                if len(sentence.split()) > 55:
                    findings.append({"code": "POSSIBLE_OVERLOAD", "where": where, "text": sentence,
                                     "suggestion": "Xem câu có đổi nhiệm vụ tư duy không; ngưỡng từ chỉ là heuristic."})
    for phrase, locations in opener_locations.items():
        if len(locations) >= 3:
            findings.append({"code": "REPEATED_OPENER", "phrase": phrase, "where": locations,
                             "suggestion": "Xem mật độ lặp và lý do; không thay bằng khuôn sáo mới."})
    return {"status": "review-suggestions-only", "scope": "Heuristics for Vietnamese authored prose; quotes/code are skipped where recognized. No semantic, pedagogy, authorship or render certification.",
            "findings": findings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        raw = args.input.read_text(encoding="utf-8-sig")
        sections = authored_sections(json.loads(raw)) if args.input.suffix.lower() == ".json" else [(args.input.name, raw)]
        report = json.dumps(review(sections), ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(report, encoding="utf-8")
        else:
            print(report, end="")
    except (OSError, ValueError, TypeError) as exc:
        print(f"Input/output error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
