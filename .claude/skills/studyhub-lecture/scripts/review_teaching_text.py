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

# Passive citation or subordinate translation mindset: StudyHub lectures are independent, authoritative teaching material.
PASSIVE_CITATION = {
    "ảnh lấy từ sách": "Chủ quyền bài giảng: Bài giảng của bạn là độc lập, không phải nơi trích dẫn sách thụ động. Dùng 'Hình 1.1: ...' hoặc chú thích trực tiếp.",
    "ảnh nguyên gốc sách": "Chủ quyền bài giảng: Xóa bỏ cụm từ này; tư liệu và hình ảnh phải là một phần tự nhiên của bài giảng.",
    "hình trong sách": "Chủ quyền bài giảng: Dùng 'Quan sát hình...', 'Sơ đồ sau...' hoặc 'Hình 1.x: ...'.",
    "hình lấy từ sách": "Chủ quyền bài giảng: Dùng chú thích hình chuẩn mực sư phạm.",
    "dữ liệu này từ": "Chủ quyền bài giảng: Dữ liệu và ví dụ phải là một phần tự nhiên của bài giảng.",
    "theo sách": "Chủ quyền bài giảng: Không tự hạ thấp thành bản tóm tắt sách; diễn đạt trực tiếp kiến thức như một giáo sư.",
    "sách dùng": "Chủ quyền bài giảng: Trình bày quy ước trực tiếp, ví dụ 'Ta quy ước...', 'Trong khuôn khổ môn học, ta xét...'.",
    "nguyên tác": "Chủ quyền bài giảng: Xóa bỏ tâm thế dịch sách.",
    "bản dịch của": "Chủ quyền bài giảng: Đây là bài giảng độc lập, không phải bản dịch.",
    "tiến độ bản dịch": "Chủ quyền bài giảng: Đây là bài giảng độc lập, không phải bản dịch.",
    "mẹo thú vị:": "Không đóng khung máy móc thành nhãn 'Mẹo thú vị:'; hãy diễn đạt tự nhiên như 'Một cách người ta hay dùng trong thực tế là...', 'Để không bao giờ nhầm lẫn ở bước này...'.",
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
OPENERS = (
    "ta có thể thấy rằng", "điều quan trọng ở đây", "điều đáng chú ý là", "trực giác đằng sau",
    "điều này cho thấy", "điều này có nghĩa là", "cần lưu ý rằng", "hãy để ý rằng", "nói một cách đơn giản",
    "như đã đề cập", "như đã nói ở trên", "không chỉ", "một điều thú vị",
)

# Wording that reads as machine-written in Vietnamese teaching prose: slogans, inflated praise,
# calques of English filler. Matched on word boundaries; a correct technical use can be kept.
AI_LEXICON = {
    "hãy cùng": "Lối mở đầu kiểu quảng cáo; vào thẳng câu hỏi, ví dụ hoặc phép tính.",
    "hành trình": "Ẩn dụ sáo rỗng trong bài giảng; nói rõ bước học tiếp theo là gì.",
    "chìa khóa": "Nói cụ thể khái niệm này giúp giải quyết được việc gì.",
    "mở khóa": "Nói cụ thể khái niệm này giúp giải quyết được việc gì.",
    "vén màn": "Tránh giọng giật gân; nêu điều được chứng minh.",
    "bức tranh toàn cảnh": "Thay bằng nội dung cụ thể của phần tổng quan.",
    "mạnh mẽ": "Nói rõ mạnh ở điểm nào: giải được lớp bài nào, cần giả thiết gì.",
    "rất mạnh": "Nói rõ mạnh ở điểm nào: giải được lớp bài nào, cần giả thiết gì.",
    "tuyệt vời": "Đánh giá cảm tính; nói kết quả cụ thể.",
    "kỳ diệu": "Đánh giá cảm tính; nói kết quả cụ thể.",
    "thần kỳ": "Đánh giá cảm tính; nói kết quả cụ thể.",
    "đáng kinh ngạc": "Đánh giá cảm tính; nói kết quả cụ thể.",
    "không thể phủ nhận": "Khẳng định tuyệt đối thay cho lập luận.",
    "đóng vai trò quan trọng": "Nêu tác dụng cụ thể thay cho lời đánh giá.",
    "đóng một vai trò": "Nêu tác dụng cụ thể thay cho lời đánh giá.",
    "về cơ bản": "Thường là dịch máy của 'basically'; bỏ đi hoặc nói rõ phần nào là cơ bản.",
    "trong thế giới của": "Lối mở đầu sáo rỗng; vào thẳng đối tượng đang học.",
    "một cách hiệu quả": "Nói hiệu quả theo nghĩa nào: thời gian, bộ nhớ, số bước lặp.",
}
# Logical connectives. A long paragraph without any of them is often a list of claims, not an explanation.
CONNECTIVES = (
    "vì", "nên", "do", "nhưng", "mà", "tuy", "song", "nếu", "thì", "khi", "để", "còn", "rồi", "nhờ", "bởi",
    "tức", "nghĩa là", "chẳng hạn", "ví dụ", "ngược lại", "trong khi", "đồng thời", "hơn nữa", "vậy",
    "do đó", "vì thế", "vì vậy", "cho nên", "thế nhưng", "tuy nhiên", "mặc dù", "dù", "sau đó", "trước hết",
    "cuối cùng", "ngoài ra", "từ đó", "như vậy", "hay", "hoặc", "cũng", "lại",
)
CHOPPY_WORDS = 5          # câu từ chừng này từ trở xuống được xem là câu cụt
CHOPPY_RUN = 4            # số câu cụt liên tiếp trong một đoạn thì gợi ý viết lại
CONNECTIVE_SENTENCES = 5  # đoạn từ chừng này câu trở lên mà không có từ nối nào
QUESTION_LABEL_RE = re.compile(r"^\*\*Câu \d+\.\*\*\s*(.+)$|^<summary>\s*Thử trả lời:\s*(.+?)</summary>$")
REFERENCE_RE = re.compile(r"§|\btr\.\s*\d|https?://|Convex Optimization", re.IGNORECASE)
SUBLABEL_RE = re.compile(r"^\(?[a-h]\)\s")
ARROW_RE = re.compile(r"→|⇒|=>")
# "Vô cùng" là từ toán học khi chỉ giới hạn hay giá trị ("tiến ra vô cùng", "bằng vô cùng"); chỉ là từ đánh giá khi
# đứng trước một tính từ ("vô cùng quan trọng"). Bỏ các cách dùng toán học trước khi dò từ đánh giá.
MATH_INFINITY_RE = re.compile(r"\b(?:ra|tới|đến|về|bằng|là|của|lớn)\s+vô cùng\b|\bvô cùng\s+(?:lớn|bé|nhỏ)\b|\bvô cùng\s*$")
# Lời giải "nghĩ thành tiếng": dấu ba chấm rồi tự sửa, hay những cụm tự sửa sai đặc trưng của nháp.
THINKING_ALOUD_RE = re.compile(r"\.\.\.\s*(?:chính xác hơn|nói đúng hơn|thay vào đó|à|khoan|không phải)|\bà không\b|\bkhoan đã\b|\bnhầm rồi\b|\bthử lại nào\b|\bà mà\b|\bý tôi là\b", re.IGNORECASE)
# A blockquote that attributes words to a named person: “…” — Name / "…" — Name / "... đã nói"
QUOTE_ATTRIBUTION_RE = re.compile(r"[\"“”«].{8,}[\"“”»].*(?:—|–|-{2})\s*\S|(?:đã nói|từng nói|đã nghĩ|từng viết)", re.IGNORECASE)
INLINE_MATH_RE = re.compile(r"\$\$.*?\$\$|\$[^$\n]+\$|`[^`\n]+`")
BOLD_RE = re.compile(r"\*\*[^*\n]+\*\*")
OVERLOAD_WORDS = 55
BOLD_LIMIT = 4
PROTECTED_PUNCTUATION_RE = re.compile(
    r"\$\$[\s\S]*?\$\$|\$(?:\\.|[^$\n])+\$|`[^`\n]*`|"
    r"<!--[\s\S]*?-->|</?[A-Za-z][^>\n]*>|&(?:#\d+|#x[\da-fA-F]+|[A-Za-z]\w*);"
)


def punctuation_prose(text):
    """Hide technical punctuation while keeping the original line numbering."""
    return PROTECTED_PUNCTUATION_RE.sub(
        lambda match: re.sub(r"[^\n]", " ", match.group(0)), text
    )


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


def _sentences(prose_line):
    """Split one Markdown prose line into sentences; math becomes a one-word placeholder."""
    prose = INLINE_MATH_RE.sub(" X ", prose_line)
    prose = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", prose).replace("**", "")
    prose = re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", prose)
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", prose) if part.strip()]


def _has_connective(sentences):
    lower = " ".join(sentences).casefold()
    return any(_has_word(lower, word) for word in CONNECTIVES)


def review(sections):
    findings, opener_locations = [], {phrase: [] for phrase in OPENERS}
    question_openings = {}
    sections = list(sections)
    for section, text in sections:
        text = strip_frontmatter(unicodedata.normalize("NFC", text))
        punctuation_lines = dict(markdown_lines(punctuation_prose(text)))
        in_sources = False
        for line_number, raw, quote in markdown_lines(text, include_quotes=True):
            if raw.startswith("## "):
                # Mục nguồn là danh sách trích dẫn, không phải lời giảng: không đo câu cụt hay từ nối ở đó.
                in_sources = "nguồn" in raw.casefold()
            where = f"{section}:line {line_number}"
            lower = raw.casefold()
            if quote:
                # Quotations are not edited for voice, but an attributed quote must have a checkable source.
                if QUOTE_ATTRIBUTION_RE.search(raw):
                    findings.append({"code": "CHECK_QUOTE_SOURCE", "where": where, "text": raw.strip(),
                                     "suggestion": "Câu trích gán cho một người: giữ chỉ khi dẫn được nguồn kiểm chứng; không thì bỏ hoặc mở bài bằng câu hỏi của bài học."})
                continue
            if ";" in punctuation_lines.get(line_number, ""):
                findings.append({"code": "PROSE_SEMICOLON", "where": where, "text": raw.strip(),
                                 "suggestion": "Hạn chế dấu chấm phẩy trong lời giảng. Xác định quan hệ giữa các vế rồi dùng từ nối phù hợp hoặc tách thành câu đầy đủ. Xem references/tu-noi-va-dien-dat.md."})
            for phrase, suggestion in PHRASES.items():
                if phrase in lower:
                    findings.append({"code": "CONTEXTUAL_PHRASE", "where": where, "phrase": phrase, "suggestion": suggestion})
            for phrase, suggestion in PASSIVE_CITATION.items():
                if phrase in lower:
                    findings.append({"code": "PASSIVE_CITATION", "where": where, "phrase": phrase, "suggestion": suggestion})
            evaluative_text = MATH_INFINITY_RE.sub(" ", INLINE_MATH_RE.sub(" ", lower))
            for phrase, suggestion in EVALUATIVE.items():
                if _has_word(evaluative_text, phrase):
                    findings.append({"code": "EVALUATIVE_PHRASE", "where": where, "phrase": phrase, "suggestion": suggestion})
            if THINKING_ALOUD_RE.search(INLINE_MATH_RE.sub(" ", raw)):
                findings.append({"code": "THINKING_ALOUD", "where": where, "text": raw.strip(),
                                 "suggestion": "Câu tự sửa giữa chừng như trong nháp. Lời giải chỉ trình bày lập luận đúng cuối cùng: tính lại, rồi viết thẳng kết quả và lý do."})
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
            for phrase, suggestion in AI_LEXICON.items():
                if _has_word(lower, phrase):
                    findings.append({"code": "AI_LEXICON", "where": where, "phrase": phrase, "suggestion": suggestion})
            if ARROW_RE.search(punctuation_lines.get(line_number, "")) and not raw.lstrip().startswith(("|", "<")):
                findings.append({"code": "ARROW_IN_PROSE", "where": where, "text": raw.strip(),
                                 "suggestion": "Mũi tên là lối ghi chép tắt; viết thành câu có từ nối (nên, khi đó, dẫn tới…)."})
            question = QUESTION_LABEL_RE.match(raw.strip())
            if question:
                words = re.sub(r"[^\w\s]", " ", INLINE_MATH_RE.sub(" X ", question.group(1) or question.group(2)).casefold()).split()
                if len(words) >= 2:
                    question_openings.setdefault(" ".join(words[:2]), []).append((section, where))
            stripped = raw.strip()
            if not in_sources and not REFERENCE_RE.search(stripped) and not stripped.startswith(("|", "#", ":::", "<")):
                sentences = _sentences(stripped)
                run = longest = 0
                for sentence in sentences:
                    short = len(sentence.split()) <= CHOPPY_WORDS and not SUBLABEL_RE.match(sentence)
                    run = run + 1 if short else 0
                    longest = max(longest, run)
                if longest >= CHOPPY_RUN:
                    findings.append({"code": "CHOPPY_RUN", "where": where, "text": stripped,
                                     "suggestion": "Nhiều câu cụt liền nhau đọc như ghi chép tắt; nối chúng bằng quan hệ thật (vì, nên, khi đó, nhưng) để người học thấy lập luận."})
                if len(sentences) >= CONNECTIVE_SENTENCES and not _has_connective(sentences):
                    findings.append({"code": "LOW_CONNECTIVES", "where": where, "text": stripped,
                                     "suggestion": "Đoạn dài mà không có từ nối nào: xác định quan hệ giữa các câu (nguyên nhân, đối lập, ví dụ, hệ quả) rồi viết nó ra."})
            # Một dòng nguồn liệt kê nhiều mục là danh mục trích dẫn, độ dài của nó không nói gì về tải nhận thức.
            prose = "" if in_sources else INLINE_MATH_RE.sub(" X ", raw)
            for sentence in re.split(r"(?<=[.!?])\s+", prose):
                if len(sentence.split()) > OVERLOAD_WORDS:
                    findings.append({"code": "POSSIBLE_OVERLOAD", "where": where, "text": sentence.strip(),
                                     "suggestion": "Xem câu có đổi nhiệm vụ tư duy không; ngưỡng từ chỉ là heuristic (công thức tính là một từ)."})
    by_section = {}
    for opening, places in question_openings.items():
        for section, where in places:
            by_section.setdefault((opening, section), []).append(where)
    total_questions = sum(len(places) for places in question_openings.values())
    # Một trang: 3 câu cùng khuôn là đủ để đọc thấy lặp. Cả chương: khuôn chiếm từ 10% số câu hỏi trở lên.
    chapter_limit = max(4, -(-total_questions // 10))
    for opening, places in question_openings.items():
        local = max(len(v) for (o, _), v in by_section.items() if o == opening)
        if local >= 3 or len(places) >= chapter_limit:
            findings.append({"code": "QUESTION_TEMPLATE", "phrase": opening, "where": [w for _, w in places],
                             "suggestion": "Nhiều câu hỏi mở đầu cùng một khuôn; đổi cách đặt vấn đề: một phản ví dụ cần tìm, một dự đoán cần kiểm, một tình huống thực tế, một câu hỏi \"điều gì xảy ra nếu\"."})
    opener_limit = max(3, -(-len(sections) // 4))
    for phrase, locations in opener_locations.items():
        if len(locations) >= opener_limit:
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
    parser.add_argument("input", type=Path, nargs="+", help="Một hoặc nhiều file Markdown (rà cả chương để thấy khuôn lặp giữa các trang), hoặc một file JSON spec.")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--format", choices=("json", "text"), default="json")
    args = parser.parse_args()
    try:
        if len(args.input) == 1 and args.input[0].suffix.lower() == ".json":
            sections = list(authored_sections(json.loads(args.input[0].read_text(encoding="utf-8-sig"))))
        else:
            sections = [(path.name, path.read_text(encoding="utf-8-sig")) for path in args.input]
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
