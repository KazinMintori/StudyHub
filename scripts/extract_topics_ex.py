import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('raw_materials/extracted/Convex_Optimization_Boyd.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the sections and their exercises for:
# Chapter 3: 3.3, 3.5, 3.6
# Chapter 5: 5.3, 5.4, 5.7, 5.8, 5.9
# Chapter 6: 6.1, 6.2, 6.4, 6.5
# Chapter 7: 7.2, 7.3, 7.4, 7.5
# Chapter 8: 8.1-8.6, 8.8
# Chapter 9: 9.1, 9.4, 9.7
# Chapter 10: 10.1, 10.4
# Chapter 11: 11.1-11.8
# Appendices A, B, C

def extract_ex_blocks(start_str, end_str):
    idx1 = text.find(start_str)
    idx2 = text.find(end_str, idx1) if end_str else idx1 + 15000
    if idx1 == -1:
        print(f"Not found: {start_str}")
        return ""
    chunk = text[idx1:idx2]
    return chunk

print("=== CHƯƠNG 3 BÀI TẬP ===")
ch3_ex = extract_ex_blocks("Exercises 113", "--- [Trang 140] ---")
for line in ch3_ex.splitlines():
    if re.match(r'^(Deﬁnition|Operations|Conjugate|Quasiconvex|Log-|Convexity with respect|\d+\.\d+)', line.strip()):
        print(" ", line.strip()[:80])

print("\n=== CHƯƠNG 5 BÀI TẬP ===")
ch5_ex = extract_ex_blocks("Exercises 273", "--- [Trang 304] ---")
for line in ch5_ex.splitlines():
    if re.match(r'^(Basic|Examples|Perturbation|Theorems of|Generalized|Saddle|\d+\.\d+)', line.strip()):
        print(" ", line.strip()[:80])

print("\n=== CHƯƠNG 6 BÀI TẬP ===")
ch6_ex = extract_ex_blocks("344 6 Approximation and", "--- [Trang 366] ---")
for line in ch6_ex.splitlines():
    if re.match(r'^(Norm|Robust|Function|\d+\.\d+)', line.strip()):
        print(" ", line.strip()[:80])

print("\n=== CHƯƠNG 7 BÀI TẬP ===")
ch7_ex = extract_ex_blocks("Exercises 393", "--- [Trang 412] ---")
for line in ch7_ex.splitlines():
    if re.match(r'^(Estimation|Optimal detector|Chebyshev|Experiment|\d+\.\d+)', line.strip()):
        print(" ", line.strip()[:80])

print("\n=== CHƯƠNG 8 BÀI TẬP ===")
ch8_ex = extract_ex_blocks("Exercises 447", "--- [Trang 469] ---")
for line in ch8_ex.splitlines():
    if re.match(r'^(Projection|Distance|Euclidean|Extremal|Centering|Classiﬁcation|Placement|Floor|\d+\.\d+)', line.strip()):
        print(" ", line.strip()[:80])
