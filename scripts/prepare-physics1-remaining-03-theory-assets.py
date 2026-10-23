#!/usr/bin/env python3
"""Reproducible asset preparation for Young & Freedman Chapter 3 Theory.

Crops figures and diagrams from Young & Freedman 15th Edition PDF
to docs/vat-ly-1/bai-giang/img/young-03/ using PyMuPDF.
Scale: 2.25 for crisp vector rasterization.
"""

import os
import sys
import pymupdf

SCALE = 2.25
SOURCE_PDF = "raw_materials/physics/source/young-freedman-15.pdf"
OUTPUT_DIR = "docs/vat-ly-1/bai-giang/img/young-03"

CROPS = [('r-theory-mo-dau', 86, (210, 0, 648, 245), 'Cyclist leaning into a banked curve'),
 ('r-theory-hinh-03-01', 87, (454, 62, 614, 251), 'Figure 3.1: Position vector r'),
 ('r-theory-hinh-03-02', 87, (454, 278, 614, 438), 'Figure 3.2: Average velocity vector v_av'),
 ('r-theory-hinh-03-03', 87, (454, 470, 614, 651), 'Figure 3.3: Instantaneous velocity vector v'),
 ('r-theory-hinh-03-04', 88, (35, 62, 195, 215), 'Figure 3.4: Velocity components in xy-plane'),
 ('r-theory-hinh-03-05', 88, (311, 281, 570, 490), 'Figure 3.5: Robotic rover path and vectors'),
 ('r-theory-hinh-03-06', 89, (77, 567, 614, 749), 'Figure 3.6: Car on curved road from P1 to P2'),
 ('r-theory-hinh-03-07', 90, (35, 118, 196, 473), 'Figure 3.7: Instantaneous acceleration a at P1 and P2'),
 ('r-theory-hinh-03-08', 91, (455, 62, 614, 217), 'Figure 3.8: Arrow acceleration upon release'),
 ('r-theory-hinh-03-09', 91, (353, 241, 614, 455), 'Figure 3.9: Robotic rover acceleration vector'),
 ('r-theory-hinh-03-10', 92, (35, 62, 196, 242), 'Figure 3.10: Parallel and perpendicular components of acceleration'),
 ('r-theory-hinh-03-11', 92, (35, 264, 196, 488), 'Figure 3.11: Effect of acceleration components on velocity'),
 ('r-theory-hinh-03-12', 92, (78, 550, 575, 705), 'Figure 3.12: Velocity and acceleration in 3 curved path situations'),
 ('r-theory-hinh-03-13', 93, (353, 86, 614, 227), 'Figure 3.13: Rover parallel and perpendicular acceleration'),
 ('r-theory-hinh-03-14', 93, (353, 404, 614, 696), 'Figure 3.14: Skier path and acceleration vectors'),
 ('r-theory-hinh-03-15', 94, (35, 260, 195, 402), 'Figure 3.15: Idealized projectile trajectory'),
 ('r-theory-hinh-03-16', 94, (35, 435, 195, 741), 'Figure 3.16: Strobe photo: free-fall vs horizontal projection'),
 ('r-theory-hinh-03-17', 95, (77, 62, 614, 295), 'Figure 3.17: Parabolic trajectory with velocity and acceleration components'),
 ('r-theory-hinh-03-18', 95, (455, 332, 614, 553), 'Figure 3.18: Initial velocity components'),
 ('r-theory-hinh-03-19', 96, (35, 62, 194, 232), 'Figure 3.19: Nearly parabolic trajectories of a bouncing ball'),
 ('r-theory-hinh-03-20', 96, (35, 280, 194, 456), 'Figure 3.20: Air drag effect on baseball'),
 ('r-theory-hinh-03-21', 96, (35, 633, 570, 721), 'Figure 3.21: Skier jump trajectory'),
 ('r-theory-hinh-03-22', 97, (353, 383, 614, 527), 'Figure 3.22: Sketch for Example 3.6 (motorcycle off cliff)'),
 ('r-theory-hinh-03-23', 98, (311, 85, 570, 242), 'Figure 3.23: Sketch for Example 3.7 (batted baseball)'),
 ('r-theory-hinh-03-24', 99, (353, 89, 614, 231), 'Figure 3.24: Launch angle 45 degrees gives maximum range'),
 ('r-theory-hinh-03-25', 99, (353, 566, 614, 714), 'Figure 3.25: Sketch for Example 3.9 (thrown ball from window)'),
 ('r-theory-hinh-03-26', 100, (35, 465, 510, 741), 'Figure 3.26: Zookeeper and falling monkey dart collision'),
 ('r-theory-hinh-03-27', 101, (77, 580, 614, 750), 'Figure 3.27: Car on circular path'),
 ('r-theory-hinh-03-28', 102, (35, 62, 195, 493), 'Figure 3.28: Velocity change in circular motion'),
 ('r-theory-hinh-03-29', 102, (209, 595, 575, 741), 'Figure 3.29: Acceleration and velocity in uniform circular motion'),
 ('r-theory-hinh-03-30', 104, (35, 391, 195, 580), 'Figure 3.30: Nonuniform circular motion on vertical loop'),
 ('r-theory-hinh-03-31', 105, (455, 62, 648, 304), 'Figure 3.31: Airshow pilots looping'),
 ('r-theory-hinh-03-32', 105, (455, 326, 614, 619), 'Figure 3.32: Relative velocity in 1D: passenger in train'),
 ('r-theory-hinh-03-33', 106, (311, 314, 503, 497), 'Figure 3.33: Reference frames for observer and truck'),
 ('r-theory-hinh-03-34', 107, (77, 62, 614, 253), 'Figure 3.34: Relative velocity in 2D: passenger across railroad car'),
 ('r-theory-hinh-03-35', 108, (311, 88, 570, 310), 'Figure 3.35: Airplane in crosswind'),
 ('r-theory-hinh-03-36', 108, (311, 470, 570, 680), 'Figure 3.36: Pilot correcting for crosswind'),
 ('r-theory-tom-tat-01', 110, (460, 88, 614, 325), 'Summary sketch 1: Vectors r, v, a'),
 ('r-theory-tom-tat-02', 110, (460, 348, 614, 404), 'Summary sketch 2: Projectile motion trajectory'),
 ('r-theory-tom-tat-03', 110, (454, 427, 614, 537), 'Summary sketch 3: Circular motion'),
 ('r-theory-tom-tat-04', 110, (460, 580, 614, 701), 'Summary sketch 4: Relative velocity'),
 ('r-theory-ung-dung-ngua', 90, (0, 615, 192, 733), 'Horses on a curved path'),
 ('r-theory-ung-dung-sao-moc', 102, (0, 617, 192, 743), 'The moons of Jupiter'),
 ('r-theory-ung-dung-tau-luon', 104, (0, 176, 193, 329), 'Tight curves and apparent loads'),
 ('r-theory-ung-dung-tuong-doi', 107, (455, 643, 648, 755), 'High speed particle collision'),
 ('r-theory-tu-kiem-3-2', 94, (35, 64, 195, 144), 'Nine acceleration choices'),
 ('r-theory-tu-kiem-3-3', 101, (454, 211, 614, 334), 'Low-speed dart reaches its apex before hitting monkey')]

def main():
    if not os.path.exists(SOURCE_PDF):
        print(f"Error: {SOURCE_PDF} does not exist.")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = pymupdf.open(SOURCE_PDF)
    print(f"Opened {SOURCE_PDF} ({len(doc)} pages). Cropping {len(CROPS)} figures at scale {SCALE}...")

    matrix = pymupdf.Matrix(SCALE, SCALE)
    for crop_id, page_pno, rect_tuple, desc in CROPS:
        page = doc[page_pno - 1]
        rect = pymupdf.Rect(*rect_tuple)
        pix = page.get_pixmap(matrix=matrix, clip=rect)
        out_path = os.path.join(OUTPUT_DIR, f"{crop_id}.png")
        pix.save(out_path)
        print(f"  Cropped {crop_id}.png from PDF p.{page_pno} [{pix.width}x{pix.height}] - {desc}")

    print("All theory crops successfully created.")

if __name__ == "__main__":
    main()
