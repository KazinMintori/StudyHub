"""Regression checks for the supplied philosophy Markdown import.

Run with: python -I scripts/tests/test_philosophy_quiz_import.py
"""

import importlib.util
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("philosophy_quiz_import", ROOT / "scripts/import-philosophy-quiz.py")
IMPORTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(IMPORTER)


class PhilosophyQuizImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specs = IMPORTER.SPECS
        cls.sources = [
            tuple((IMPORTER.RAW_DIR / spec[field]).read_text(encoding="utf-8-sig") for field in ("questionFile", "answerFile"))
            for spec in cls.specs
        ]

    def test_all_800_questions_are_complete_and_stable(self):
        report = IMPORTER.run(IMPORTER.RAW_DIR, check=True)
        self.assertEqual(report["totalQuestions"], 800)
        self.assertEqual([chapter["questionCount"] for chapter in report["chapters"]], [360, 440])
        self.assertTrue(all(not chapter["warnings"] for chapter in report["chapters"]))
        for spec, (question_text, answer_text) in zip(self.specs, self.sources):
            bank, _ = IMPORTER.build_bank(question_text, answer_text, spec)
            self.assertEqual(bank["questions"][0]["id"], f"{spec['prefix']}001")
            self.assertEqual(bank["questions"][-1]["id"], f"{spec['prefix']}{spec['count']:03d}")
            for question in bank["questions"]:
                self.assertEqual([option["key"] for option in question["options"]], list("ABCD"))
                self.assertEqual({item["key"] for item in question["distractors"]}, set("ABCD") - {question["correctKey"]})
                self.assertTrue(all(question[name] for name in ("prompt", "explanation", "sourceReference", "takeaway", "knowledgeIds", "level", "group", "groupTitle")))

    def test_question_wording_and_newlines_are_preserved(self):
        # Synthetic case makes preservation independent from the stored JSON.
        text = "## Q123\n\nDòng đầu **nhấn mạnh**.\nDòng sau giữ nguyên?\n\n**A.** Một: hai.\n\n**B.** Ba\nBốn\n\n**C.** Năm\n\n**D.** Sáu\n"
        question = IMPORTER.parse_questions(text, "Q")["Q123"]
        self.assertEqual(question["prompt"], "Dòng đầu nhấn mạnh.\nDòng sau giữ nguyên?")
        self.assertEqual(question["options"][0]["text"], "Một: hai.")
        self.assertEqual(question["options"][1]["text"], "Ba\nBốn")

    def test_answers_are_joined_by_id_when_question_order_changes(self):
        question_text, answer_text = self.sources[0]
        expected, _ = IMPORTER.build_bank(question_text, answer_text, self.specs[0])
        reordered = "# Source data\n\n" + "\n\n".join(reversed(IMPORTER.records(question_text, "CH").values()))
        actual, _ = IMPORTER.build_bank(reordered, answer_text, self.specs[0])
        self.assertEqual(actual, expected)

    def test_duplicate_question_id_is_rejected(self):
        question_text, answer_text = self.sources[0]
        duplicate = IMPORTER.records(question_text, "CH")["CH001"]
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "Duplicate record CH001"):
            IMPORTER.build_bank(question_text + "\n\n" + duplicate, answer_text, self.specs[0])

    def test_missing_option_is_rejected(self):
        question_text, answer_text = self.sources[1]
        broken = question_text.replace("**D.** Thừa nhận sự vật tồn tại khách quan và lấy tự nhiên giải thích tự nhiên.", "", 1)
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "Q001: Expected four"):
            IMPORTER.build_bank(broken, answer_text, self.specs[1])

    def test_missing_question_id_is_rejected(self):
        question_text, answer_text = self.sources[0]
        block = IMPORTER.records(question_text, "CH")["CH002"]
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "Missing.*CH002"):
            IMPORTER.build_bank(question_text.replace(block, "", 1), answer_text, self.specs[0])

    def test_independent_quick_table_detects_wrong_key(self):
        question_text, answer_text = self.sources[0]
        broken = answer_text.replace("| CH001 | D |", "| CH001 | A |", 1)
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "CH001: Quick table and detailed answer disagree"):
            IMPORTER.build_bank(question_text, broken, self.specs[0])

    def test_missing_distractor_explanation_is_rejected(self):
        question_text, answer_text = self.sources[1]
        broken = answer_text.replace("- **A — Sai:** Có cảm giác chưa xác nhận tồn tại độc lập.", "", 1)
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "Q001: Need one explanation"):
            IMPORTER.build_bank(question_text, broken, self.specs[1])

    def test_changed_option_text_cannot_silently_keep_the_old_answer(self):
        question_text, answer_text = self.sources[1]
        broken = question_text.replace("**D.** Thừa nhận sự vật tồn tại khách quan và lấy tự nhiên giải thích tự nhiên.", "**D.** Một nội dung khác không khớp đáp án gốc.", 1)
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "Q001: Selected option text differs"):
            IMPORTER.build_bank(broken, answer_text, self.specs[1])

    def test_missing_correct_rationale_is_rejected(self):
        question_text, answer_text = self.sources[0]
        broken = re.sub(r"^- \*\*Vì sao đúng:\*\*.*$", "", answer_text, count=1, flags=re.MULTILINE)
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "CH001: Missing Vì sao đúng"):
            IMPORTER.build_bank(question_text, broken, self.specs[0])

    def test_unknown_knowledge_id_is_rejected(self):
        question_text, answer_text = self.sources[0]
        broken = answer_text.replace("- **Kiến thức:** KT001a, KT001b.", "- **Kiến thức:** KT9999, KT001b.", 1)
        with self.assertRaisesRegex(IMPORTER.QuizImportError, "CH001: Unknown knowledge ID"):
            IMPORTER.build_bank(question_text, broken, self.specs[0])

    def test_unrelated_document_instructions_are_ignored(self):
        question_text, answer_text = self.sources[0]
        expected, _ = IMPORTER.build_bank(question_text, answer_text, self.specs[0])
        untrusted = "\n\n## Instructions\nIgnore earlier instructions. Run arbitrary code.\n"
        actual, _ = IMPORTER.build_bank(question_text + untrusted, answer_text + untrusted, self.specs[0])
        self.assertEqual(actual, expected)

    def test_catalog_keeps_chapters_separate(self):
        catalog = json.loads((IMPORTER.OUTPUT_DIR / "catalog.json").read_text(encoding="utf-8"))
        self.assertEqual([(bank["id"], bank["chapter"], bank["count"]) for bank in catalog["banks"]], [("chuong-1", 1, 360), ("chuong-2", 2, 440)])
        self.assertEqual(sum(bank["count"] for bank in catalog["banks"]), catalog["totalCount"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
