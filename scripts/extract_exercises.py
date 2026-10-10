import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('raw_materials/extracted/Convex_Optimization_Boyd.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for exercises: e.g. "Exercises 113", "Exercises 273", etc.
# In the book, each chapter ends with "Exercises" and subheadings like:
# "Basic properties and examples", "Operations that preserve convexity", "Conjugate functions", etc.

def get_exercise_sections(ch_num):
    # Find chapter start
    ch_pat = rf"\n{ch_num}\s+[A-Z][a-z]+"
    m_ch = re.search(ch_pat, text)
    if not m_ch:
        return
    pos = m_ch.start()
    # Find next chapter
    next_ch = ch_num + 1
    m_next = re.search(rf"\n{next_ch}\s+[A-Z][a-z]+", text[pos:])
    end_pos = pos + m_next.start() if m_next else len(text)
    ch_text = text[pos:end_pos]
    
    # Find "Exercises"
    ex_idx = ch_text.rfind("\nExercises\n")
    if ex_idx == -1:
        ex_idx = ch_text.rfind("Exercises")
    if ex_idx != -1:
        ex_text = ch_text[ex_idx:]
        # Find all exercise numbers like "3.1", "3.24"
        ex_list = re.findall(rf"(\b{ch_num}\.\d+\b[^\n\.]+)", ex_text)
        print(f"\n================ CHAPTER {ch_num} EXERCISES (Tổng cộng: {len(ex_list)}) ================")
        # Find subsection headers in exercises
        subheaders = re.findall(r"\n([A-Z][A-Za-z\s,–—\-]+)\n\n(?=\d+\.\d+)", ex_text)
        print("Các nhóm bài tập:", subheaders)
        for ex in ex_list[:15]:
            print("  *", ex.strip())
        if len(ex_list) > 15:
            print(f"  ... và {len(ex_list) - 15} bài tập khác từ {ex_list[15].strip()} đến {ex_list[-1].strip()}")

for ch in [3, 5, 6, 7, 8, 9, 10, 11]:
    get_exercise_sections(ch)
