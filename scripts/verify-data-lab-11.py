"""Bộ kiểm định chất lượng và tính đúng đắn cho Lab 11.

Kiểm tra:
1. Định dạng văn bản: span id, ::: exercise, ::: solution, bảng Markdown.
2. Quy chuẩn văn phong: không em dash, không dấu chấm phẩy văn xuôi, viết hoa sau dấu hai chấm.
3. Không dùng từ cấm: 'hợp đồng', 'lấy từ giáo trình', 'lấy từ slide', 'sinh viên rất hay nhầm', v.v.
4. Thực thi tuần tự toàn bộ code blocks từ Markdown trên môi trường thực tế, kiểm tra đầu ra và các ca biên.
5. Kiểm tra tính đầy đủ của file ánh xạ coverage-11.json.
"""

from io import StringIO
from pathlib import Path
import re
import sys
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
LAB_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/lab-11.md"
COVERAGE_FILE = ROOT / "raw_materials/xu-ly-du-lieu/labs/coverage-11.json"

BANNED_WORDS = [
    "hợp đồng",
    "lấy từ giáo trình",
    "lấy từ slide",
    "lấy từ sách",
    "do người soạn thêm",
    "không gán cho tác giả",
    "khoan đã, hãy xem lại",
    "à không, thay vào đó",
    "sinh viên rất hay nhầm",
    "lỗi phổ biến nhất của sinh viên",
    "đa số sinh viên đều mắc",
    "bẫy thi cử",
    "nguyên tác",
    "tiến độ bản dịch",
    "bản dịch của"
]

def check_file_structure(content: str):
    print("--- 1. Kiểm tra cấu trúc file và thẻ bài tập ---")
    required_spans = [f"data-lab-11-{i:02d}" for i in range(1, 9)]
    for span in required_spans:
        assert f'id="{span}"' in content or f"id='{span}'" in content, f"Thiếu thẻ định danh {span}"
    print(f"Đã tìm thấy đủ {len(required_spans)} thẻ định danh span id.")

    exercise_count = content.count("::: exercise")
    solution_count = content.count("::: solution")
    close_count = content.count(":::")
    assert exercise_count == 8, f"Số lượng ::: exercise mong đợi 8, thực tế: {exercise_count}"
    assert solution_count == 8, f"Số lượng ::: solution mong đợi 8, thực tế: {solution_count}"
    assert close_count == exercise_count + solution_count + (8 * 2), f"Đóng mở container không khớp: {close_count}"
    print("Cấu trúc container ::: exercise và ::: solution hoàn toàn cân đối.")

def check_prose_rules(content: str):
    print("--- 2. Kiểm tra quy tắc văn phong tiếng Việt ---")
    lines = content.splitlines()
    in_code_block = False

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Kiểm tra từ cấm
        lower_line = line.lower()
        for banned in BANNED_WORDS:
            assert banned not in lower_line, f"Dòng {idx} chứa từ ngữ không phù hợp '{banned}': {line}"

        # Bỏ qua dòng bảng Markdown
        if stripped.startswith("|"):
            continue

        # Bỏ qua dòng kẻ ngang Markdown và container VitePress
        if stripped == "---" or stripped.startswith(":::"):
            continue

        # Kiểm tra em dash (— hoặc --)
        assert "—" not in line, f"Dòng {idx} chứa dấu gạch ngang dài (em dash): {line}"
        if not stripped.startswith("- "):
            assert "--" not in line, f"Dòng {idx} chứa ký hiệu '--': {line}"

        # Kiểm tra dấu chấm phẩy trong văn xuôi
        cleaned_line = re.sub(r"&[a-zA-Z0-9#]+;", "", line)
        assert ";" not in cleaned_line, f"Dòng {idx} chứa dấu chấm phẩy trong văn xuôi: {line}"

        # Kiểm tra viết hoa sau dấu hai chấm
        colon_matches = re.finditer(r":\s+([a-zA-Z\u00C0-\u1EF9])", line)
        for m in colon_matches:
            char = m.group(1)
            start_pos = m.start()
            prefix = line[:start_pos]
            if "http" in prefix or "https" in prefix or prefix.count("`") % 2 == 1:
                continue
            assert char.isupper(), f"Dòng {idx} không viết hoa chữ cái sau dấu hai chấm (': {char}'): {line}"

    print("Văn phong tiếng Việt chuẩn mực: Không em dash, không dấu chấm phẩy, viết hoa sau dấu hai chấm.")

def extract_python_blocks(content: str):
    pattern = r"```python\r?\n(.*?)```"
    return re.findall(pattern, content, re.DOTALL)

def run_code_verifications(content: str):
    print("--- 3. Thực thi tuần tự toàn bộ code blocks Markdown ---")
    all_blocks = extract_python_blocks(content)
    print(f"Tổng số khối code Python tìm thấy: {len(all_blocks)}")
    assert len(all_blocks) == 17, f"Mong đợi đúng 17 khối code (1 dữ liệu + 8 bài x 2 cách), tìm thấy {len(all_blocks)}"

    # Chạy tuần tự từ trên xuống dưới trong cùng một namespace như người đọc
    namespace = {"__name__": "__main__"}
    for idx, block in enumerate(all_blocks, start=1):
        try:
            exec(block, namespace)
        except Exception as exc:
            raise AssertionError(f"Lỗi thực thi khối code {idx}: {exc}") from exc

    # Kiểm tra biến cơ sở
    assert "DEMO_RV" in namespace
    assert "REVIEWS" in namespace
    assert "GOLD" in namespace
    assert "LLM_OUT" in namespace
    assert "LLM_RUN_2" in namespace

    # Bài 1: choose_sample và choose_sample_robust
    assert "choose_sample" in namespace
    assert "choose_sample_robust" in namespace
    mau_1 = namespace["choose_sample"](namespace["DEMO_RV"], do_dai_min=50, n=100, seed=42)
    mau_2 = namespace["choose_sample_robust"](namespace["DEMO_RV"], do_dai_min=50, n=100, seed=42)
    assert len(mau_1) == 100
    assert len(mau_2) == 100
    assert mau_1["id"].head(3).tolist() == [5089, 5096, 5009]
    pd.testing.assert_frame_equal(mau_1, mau_2)
    # Kiểm tra ca biên không đủ dòng
    try:
        namespace["choose_sample_robust"](namespace["DEMO_RV"], do_dai_min=1000, n=10)
        assert False, "Phải ném ValueError khi số dòng không đủ n"
    except ValueError:
        pass
    # Kiểm tra ca biên thiếu cột comments
    try:
        namespace["choose_sample_robust"](pd.DataFrame({"id": [1, 2]}))
        assert False, "Phải ném KeyError khi thiếu cột comments"
    except KeyError:
        pass

    # Bài 2: estimate_cost và estimate_cost_vectorized
    assert "estimate_cost" in namespace
    assert "estimate_cost_vectorized" in namespace
    test_series = pd.Series(["abcdefg", "abcd", "abc"])
    res_cost_1 = namespace["estimate_cost"](test_series, gia_moi_trieu=0.25)
    res_cost_2 = namespace["estimate_cost_vectorized"](test_series, gia_moi_trieu=0.25)
    assert res_cost_1 == {"tong_token": 2, "chi_phi": 2 * 0.25 / 1_000_000}
    assert res_cost_2 == res_cost_1
    assert namespace["estimate_cost"](mau_1["comments"])["tong_token"] == 1589
    # Ca biên Series rỗng
    empty_series = pd.Series([], dtype=str)
    assert namespace["estimate_cost_vectorized"](empty_series) == {"tong_token": 0, "chi_phi": 0.0}

    # Bài 3: ReviewInfo và ReviewInfoStrict
    assert "ReviewInfo" in namespace
    assert "ReviewInfoStrict" in namespace
    ReviewInfo = namespace["ReviewInfo"]
    valid_json = '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["noise"], "language": "en"}'
    obj_valid = ReviewInfo.model_validate_json(valid_json)
    assert obj_valid.sentiment == "mixed"
    assert obj_valid.aspects_positive == ["location"]
    assert obj_valid.aspects_negative == ["noise"]
    assert obj_valid.language == "en"
    # Kiểm tra chặn nhãn ngoài enum và thiếu trường
    for invalid_json in [
        '{"sentiment": "happy", "aspects_positive": [], "aspects_negative": [], "language": "en"}',
        '{"sentiment": "mixed", "aspects_positive": ["photos"], "aspects_negative": [], "language": "en"}',
        '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": []}',
        '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": 123}'
    ]:
        try:
            ReviewInfo.model_validate_json(invalid_json)
            assert False, f"Lẽ ra phải chặn: {invalid_json}"
        except ValidationError:
            pass

    # Bài 4: validate_outputs và validate_outputs_with_audit
    assert "validate_outputs" in namespace
    assert "validate_outputs_with_audit" in namespace
    val_res = namespace["validate_outputs"](namespace["LLM_OUT"])
    assert set(val_res) == {"hop_le", "loi_schema"}
    assert len(val_res["hop_le"]) == 8
    assert val_res["loi_schema"] == [2, 5]
    assert all(isinstance(v, ReviewInfo) for v in val_res["hop_le"].values())
    # Hỗ trợ string id và JSON hỏng
    broken_test = {"str_a": '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": [], "language": "en"}', "str_b": "{invalid json"}
    val_broken = namespace["validate_outputs"](broken_test)
    assert "str_a" in val_broken["hop_le"]
    assert val_broken["loi_schema"] == ["str_b"]

    # Bài 5: sentiment_accuracy và sentiment_accuracy_df
    assert "sentiment_accuracy" in namespace
    assert "sentiment_accuracy_df" in namespace
    test_preds = {rid: obj.sentiment for rid, obj in val_res["hop_le"].items()}
    acc_res = namespace["sentiment_accuracy"](test_preds, namespace["GOLD"])
    acc_df_res = namespace["sentiment_accuracy_df"](test_preds, namespace["GOLD"])
    assert acc_res["so_dung"] == 5
    assert acc_res["acc"] == 0.625
    assert acc_res["sai"] == [4, 9, 10]
    assert acc_df_res["so_dung"] == 5
    assert acc_df_res["acc"] == 0.625
    assert acc_df_res["sai"] == [4, 9, 10]
    # Ca biên đơn lẻ
    single_res = namespace["sentiment_accuracy"]({"x": "positive"}, {"x": {"sentiment": "positive"}, "y": {"sentiment": "negative"}})
    assert single_res["acc"] == 1.0 and single_res["so_dung"] == 1 and single_res["sai"] == []

    # Bài 6: diagnose_semantic_errors và analyze_error_patterns
    assert "diagnose_semantic_errors" in namespace
    assert "analyze_error_patterns" in namespace
    diag_df = namespace["diagnose_semantic_errors"](acc_res["sai"], namespace["REVIEWS"], test_preds, namespace["GOLD"])
    assert isinstance(diag_df, pd.DataFrame)
    assert len(diag_df) == 3
    assert set(diag_df.columns) == {"id", "gold", "llm", "kieu_loi", "ngu_canh_ngan"}

    # Bài 7: contradictions và contradictions_functional
    assert "contradictions" in namespace
    assert "contradictions_functional" in namespace
    dump_dict = {rid: obj.model_dump() for rid, obj in val_res["hop_le"].items()}
    contra_res = namespace["contradictions"](dump_dict)
    contra_fn_res = namespace["contradictions_functional"](dump_dict)
    assert contra_res == [9, 10]
    assert contra_fn_res == [9, 10]
    # Ca biên mâu thuẫn đơn lẻ và mixed không bao giờ vi phạm
    test_contra = {
        "k1": {"sentiment": "positive", "aspects_positive": [], "aspects_negative": ["noise"]},
        "k2": {"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": []},
        "k3": {"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["noise"]}
    }
    assert namespace["contradictions"](test_contra) == ["k1", "k2"]

    # Bài 8: evaluate_llm_run và evaluate_llm_pipeline
    assert "evaluate_llm_run" in namespace
    assert "evaluate_llm_pipeline" in namespace
    bc_1 = namespace["evaluate_llm_run"](namespace["LLM_OUT"], namespace["GOLD"])
    bc_2 = namespace["evaluate_llm_run"](namespace["LLM_RUN_2"], namespace["GOLD"])
    assert bc_1["loi_schema_count"] == 2
    assert bc_1["acc_hop_le"] == 0.625
    assert bc_1["acc_toan_bo"] == 0.5
    assert bc_1["id_10_status"] == "Sai"
    assert bc_2["loi_schema_count"] == 0
    assert bc_2["acc_hop_le"] == 1.0
    assert bc_2["acc_toan_bo"] == 1.0
    assert bc_2["id_10_status"] == "Chính xác"
    assert bc_2["mau_thuan_ids"] == []

    pipeline_df = namespace["evaluate_llm_pipeline"](
        {"Run 1": namespace["LLM_OUT"], "Run 2": namespace["LLM_RUN_2"]},
        namespace["GOLD"]
    )
    assert isinstance(pipeline_df, pd.DataFrame)
    assert len(pipeline_df) == 2

    print("Tất cả 17 khối code đều thực thi chính xác và đạt 100% assertions!")

def check_coverage_json():
    print("--- 4. Kiểm tra file coverage-11.json ---")
    assert COVERAGE_FILE.exists(), f"Không tìm thấy file {COVERAGE_FILE}"
    import json
    data = json.loads(COVERAGE_FILE.read_text(encoding="utf-8"))
    assert "template_cells" in data, "Thiếu trường template_cells"
    assert "course_cells" in data, "Thiếu trường course_cells"
    assert len(data["template_cells"]) == 41, f"Template có 41 cell (0-40), ghi nhận: {len(data['template_cells'])}"
    assert len(data["course_cells"]) == 26, f"Course có 26 cell (0-25), ghi nhận: {len(data['course_cells'])}"

    # Kiểm tra tính hợp lệ của status và exercise_id
    valid_statuses = {"included", "merged", "excluded"}
    for idx, c in enumerate(data["template_cells"]):
        assert c["status"] in valid_statuses, f"Template cell {idx} có status không hợp lệ: {c['status']}"
        if c["status"] in {"included", "merged"}:
            assert c["exercise_id"] is not None and c["exercise_id"].startswith("data-lab-11-"), f"Template cell {idx} thiếu exercise_id hợp lệ"
        else:
            assert c["exercise_id"] is None, f"Template cell {idx} bị loại trừ nhưng vẫn có exercise_id"

    for idx, c in enumerate(data["course_cells"]):
        assert c["status"] in valid_statuses, f"Course cell {idx} có status không hợp lệ: {c['status']}"
        if c["status"] in {"included", "merged"}:
            assert c["exercise_id"] is not None and c["exercise_id"].startswith("data-lab-11-"), f"Course cell {idx} thiếu exercise_id hợp lệ"
        else:
            assert c["exercise_id"] is None, f"Course cell {idx} bị loại trừ nhưng vẫn có exercise_id"

    print(f"Coverage JSON đầy đủ: {len(data['template_cells'])} template cells và {len(data['course_cells'])} course cells.")

def main():
    print(f"=== BẮT ĐẦU KIỂM ĐỊNH LAB 11 ({LAB_FILE.name}) ===")
    assert LAB_FILE.exists(), f"Không tìm thấy file {LAB_FILE}"
    content = LAB_FILE.read_text(encoding="utf-8")
    check_file_structure(content)
    check_prose_rules(content)
    run_code_verifications(content)
    check_coverage_json()
    print("=== TOÀN BỘ KIỂM ĐỊNH LAB 11 ĐẠT 100% ===")

if __name__ == "__main__":
    main()
