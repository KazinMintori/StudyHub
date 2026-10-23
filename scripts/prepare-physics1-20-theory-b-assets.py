#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prepare assets for Physics 1 Chapter 20 Theory B.
Extracts original crops from raw_materials/physics/source/young-freedman-15.pdf.
"""

import os
import sys
import fitz
from PIL import Image

PDF_PATH = "raw_materials/physics/source/young-freedman-15.pdf"
OUTPUT_DIR = "docs/vat-ly-1/bai-giang/img/young-20"

SCALE = 2.0  # 144 DPI for crisp rendering

CROPS = {
    # 20.5
    "b-hinh-20-11": (672, (208, 355, 575, 746)),
    # 20.6
    "b-hinh-20-12": (673, (455, 600, 648, 742)),
    "b-hinh-20-13": (674, (170, 84, 615, 350)),
    "b-hinh-20-14": (675, (352, 440, 522, 574)),
    "b-hinh-20-15": (678, (215, 60, 575, 240)),
    "b-hinh-20-16": (678, (0, 465, 194, 632)),
    # 20.7
    "b-hinh-20-17": (679, (454, 584, 648, 745)),
    "b-hinh-20-18": (682, (34, 415, 298, 542)),
    "b-hinh-20-19": (683, (75, 620, 462, 746)),
    "b-ung-dung-20-01": (684, (0, 198, 194, 305)),
    # 20.8
    "b-hinh-20-20": (685, (90, 60, 425, 215)),
    "b-hinh-20-21": (686, (32, 150, 192, 746)),
    "b-hinh-20-22": (687, (350, 430, 615, 578)),
    "b-ung-dung-20-02": (688, (28, 235, 192, 545)),
    # Chapter 20 Summary (p. 689-690)
    "b-tt-thuan-nghich": (689, (485, 95, 612, 160)),
    "b-tt-dong-co-nhiet": (689, (485, 180, 612, 245)),
    "b-tt-chu-trinh-otto": (689, (485, 255, 612, 320)),
    "b-tt-may-lanh": (689, (485, 325, 612, 395)),
    "b-tt-nguyen-ly-2": (689, (485, 400, 612, 470)),
    "b-tt-chu-trinh-carnot": (689, (485, 475, 612, 575)),
    "b-tt-vi-mo-entropy": (690, (440, 265, 580, 345)),
}


def render_crop(doc, page_1based, bbox, scale):
    page = doc[page_1based - 1]
    rect = fitz.Rect(*bbox)
    mat = fitz.Matrix(scale, scale)
    pix = page.get_pixmap(matrix=mat, clip=rect, alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return img


def generate_all_crops(output_dir=OUTPUT_DIR, scale=SCALE):
    os.makedirs(output_dir, exist_ok=True)
    doc = fitz.open(PDF_PATH)
    results = {}
    print(f"Generating {len(CROPS)} crops with scale {scale}...")
    for name, (pno, bbox) in CROPS.items():
        img = render_crop(doc, pno, bbox, scale)
        out_path = os.path.join(output_dir, f"{name}.png")
        img.save(out_path, format="PNG", optimize=True)
        w, h = img.size
        results[name] = {"path": out_path, "size": (w, h), "page": pno, "bbox": bbox}
        print(f"  {name}.png: {w}x{h} px from page {pno}")
    doc.close()
    return results


if __name__ == "__main__":
    generate_all_crops()
