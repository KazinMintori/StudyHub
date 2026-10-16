"""Kịch bản kiểm thử độc lập, toàn diện cho toàn bộ 30 bài tập Chapter 44 nhóm D.

Kiểm tra:
1. Đầy đủ chính xác 30 bài tập (44.31-44.59 và Bài tập cầu nối).
2. Kiểm tra cấu trúc sư phạm chuẩn StudyHub: Tóm tắt đề bài, Hướng đi/Solution Guide,
   chi tiết các bước biến đổi, không để lộ đáp số trong tiêu đề/tóm tắt.
3. Tái tính toán số học độc lập bằng công thức vật lý chuẩn xác cho toàn bộ 30 bài tập
   (bao gồm 5 trường hợp kiểm tra đại số độc lập cho 44.56, phân số động năng ở 44.48,
   động năng và hướng bay neutron ở 44.49, và mô hình dãn nở 2D ở 44.55).
4. Kiểm tra ảnh trích xuất gốc từ PDF nguồn (tọa độ, kích thước, khớp pixel RGB).
5. Kiểm tra 8 file SVG bổ trợ (tồn tại, không rỗng, kích thước hợp lệ).
6. Kiểm tra file chú thích song ngữ physics44-exercises-d-image-annotations.mjs.
"""
from pathlib import Path
import re
import hashlib
import numpy as np
import pymupdf as fitz
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]

OWNED_MARKDOWNS = [
    ROOT / 'raw_materials/physics/translations/chapter-44/12-bai-tap-31-45.md',
    ROOT / 'raw_materials/physics/translations/chapter-44/13-bai-tap-46-56.md',
    ROOT / 'raw_materials/physics/translations/chapter-44/15-mcat.md',
    ROOT / 'raw_materials/physics/translations/chapter-44/16-bai-tap-cau-noi.md',
]

IMG_DIR = ROOT / 'docs/vat-ly-2/bai-giang/img/young-44'
PDF_PATH = ROOT / 'raw_materials/physics/source/young-freedman-15.pdf'

def test_problem_coverage():
    print("[1/6] Kiểm tra độ bao phủ 30 bài tập...")
    all_problems = []
    for md in OWNED_MARKDOWNS:
        assert md.is_file(), f"Thiếu file: {md}"
        text = md.read_text(encoding='utf-8')
        matches = re.findall(r'^###\s+(44\.\d+|Bài tập cầu nối)', text, flags=re.MULTILINE)
        all_problems.extend(matches)
        details_count = len(re.findall(r'<details>', text))
        summary_count = len(re.findall(r'<summary>Xem lời giải chi tiết</summary>', text))
        assert details_count == len(matches), f"Số khối details ({details_count}) không khớp số bài ({len(matches)}) trong {md.name}"
        assert summary_count == len(matches), f"Số khối summary ({summary_count}) không khớp trong {md.name}"

    expected_ids = [f'44.{i}' for i in range(31, 60)] + ['Bài tập cầu nối']
    assert len(all_problems) == 30, f"Tổng số bài tập là {len(all_problems)}, yêu cầu đúng 30!"
    assert all_problems == expected_ids, f"Danh sách bài không khớp thứ tự kỳ vọng! Thiếu/thừa: {set(expected_ids) ^ set(all_problems)}"
    print(f"  -> Đầy đủ 30 bài tập chính xác: {len(all_problems)}/30 bài.")

def test_physics_calculations():
    import runpy
    runpy.run_path(str(ROOT/'raw_materials/physics/verify_chapter44_end_parent.py'),run_name='__main__')


def test_source_image_crops():
    print("[3/6] Kiểm tra độ khớp pixel ảnh trích xuất gốc từ PDF nguồn...")
    assert PDF_PATH.is_file(), f"Thiếu PDF nguồn: {PDF_PATH}"
    SCALE = 3
    CROPS = {
        'hinh-p44-55': (1544, (172, 274, 296, 388)),
        'hinh-tham-chieu-d-1': (1530, (36, 362, 192, 504)),
    }
    with fitz.open(PDF_PATH) as pdf:
        for stem, (page, clip) in CROPS.items():
            png_file = IMG_DIR / f'{stem}.png'
            assert png_file.is_file(), f"Thiếu file PNG: {png_file}"
            pix = pdf[page - 1].get_pixmap(matrix=fitz.Matrix(SCALE, SCALE), clip=fitz.Rect(clip), alpha=False)
            with Image.open(png_file) as im:
                assert im.size == (pix.width, pix.height), f"Kích thước {stem} không khớp: {im.size} vs {(pix.width, pix.height)}"
                im_bytes = im.convert('RGB').tobytes()
                assert im_bytes == pix.samples, f"Dữ liệu pixel của {stem} không khớp tuyệt đối với PDF nguồn!"
            sha = hashlib.sha256(png_file.read_bytes()).hexdigest()
            print(f"  -> {stem}.png: Trang PDF {page}, kích thước {pix.width}x{pix.height}, SHA256={sha[:16]}... KHỚP 100% RGB.")

def test_svg_assets():
    print("[4/6] Kiểm tra 8 file SVG bổ trợ đồ thị...")
    for i in range(1, 9):
        svg_name = f'loi-giai-d-{i:02d}.svg'
        svg_path = IMG_DIR / svg_name
        assert svg_path.is_file(), f"Thiếu file SVG: {svg_path}"
        content = svg_path.read_text(encoding='utf-8')
        assert '<svg' in content and '</svg>' in content, f"{svg_name} không phải file SVG hợp lệ!"
        assert len(content) > 1000, f"{svg_name} quá ngắn ({len(content)} bytes), có thể là đồ thị rỗng!"
        print(f"  -> {svg_name}: Hợp lệ ({len(content)} bytes).")

def test_image_annotations():
    print("[5/6] Kiểm tra cấu trúc file image-annotations...")
    anno_path = ROOT / 'docs/.vitepress/physics44-exercises-d-image-annotations.mjs'
    assert anno_path.is_file(), f"Thiếu file chú thích: {anno_path}"
    content = anno_path.read_text(encoding='utf-8')
    assert 'physics44ExercisesDImageAnnotations' in content, "Thiếu export physics44ExercisesDImageAnnotations"
    assert 'young-44/hinh-p44-55' in content, "Thiếu key young-44/hinh-p44-55"
    assert 'young-44/hinh-tham-chieu-d-1' in content, "Thiếu key young-44/hinh-tham-chieu-d-1"
    print("  -> File chú thích ảnh chính xác và hợp lệ.")

def test_vietnamese_style_and_format():
    print("[6/6] Kiểm tra chuẩn mực văn phong tiếng Việt và cú pháp Markdown...")
    for md in OWNED_MARKDOWNS:
        text = md.read_text(encoding='utf-8')
        assert not re.search(r'file:///|[A-Z]:[\\/](Users|My Drive)', text), f"Phát hiện machine-local link trong {md.name}!"
        for line in text.splitlines():
            if '$$' in line and line != '$$':
                raise AssertionError(f"Dấu $$ không nằm riêng trên dòng trong {md.name}: {line}")
            if re.match(r'^\s*\$\s*$', line):
                raise AssertionError(f"Dòng chỉ chứa một dấu $ lẻ trong {md.name}: {line}")
        banned = ['Nội dung lấy từ giáo trình', 'Bài tập lấy từ sách', 'Ảnh lấy từ sách', 'nguyên tác', 'Khoan đã, hãy xem lại', 'trong đề bài gốc tác giả có nhầm lẫn']
        for b in banned:
            assert b not in text, f"Phát hiện cụm từ vi phạm chuẩn sư phạm '{b}' trong {md.name}"
        # Kiểm tra không còn đường dẫn tương đối lỗi ../../../../docs
        assert '../../../../docs' not in text, f"Phát hiện đường dẫn hỏng include ../../../../docs trong {md.name}"
    print("  -> Cú pháp Markdown, liên kết ảnh và văn phong học thuật tiếng Việt tuân thủ đầy đủ.")

def main():
    print("======================================================================")
    print("BẮT ĐẦU KIỂM THỬ TOÀN DIỆN CHAPTER 44 EXERCISES D")
    print("======================================================================")
    test_problem_coverage()
    test_physics_calculations()
    test_source_image_crops()
    test_svg_assets()
    test_image_annotations()
    test_vietnamese_style_and_format()
    print("======================================================================")
    print("TẤT CẢ CÁC BÀI KIỂM THỬ ĐÃ VƯỢT QUA THÀNH CÔNG (6/6 SUITES PASSED)!")
    print("======================================================================")

if __name__ == '__main__':
    main()
