import os
import re

files = [
    'raw_materials/physics/translations/chapter-37/01-bat-bien-dinh-luat.md',
    'raw_materials/physics/translations/chapter-37/11-luyen-tap-huong-dan.md',
    'raw_materials/physics/translations/chapter-37/18-bai-tap-du-lieu-nang-cao.md',
]

for p in files:
    if not os.path.exists(p):
        continue
    with open(p, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Normalize CRLF to LF
    content = content.replace('\r\n', '\n')
    
    # In 11-luyen-tap-huong-dan.md:
    content = content.replace(
        "$$\n\\begin{aligned}\nE_0&= mc^2\\\\\n&= 8{,}199\\times10^{-14}\\,\\mathrm J.\n\\end{aligned}\n$$",
        "$$\nE_0 = mc^2 = 8{,}199\\times10^{-14}\\,\\mathrm J.\n$$"
    )
    content = content.replace(
        "$$\n\\begin{aligned}\nK&= E-E_0\\\\\n&\\approx 3{,}18\\times10^{-13}\\,\\mathrm J.\n\\end{aligned}\n$$",
        "$$\nK = E - E_0 \\approx 3{,}18\\times10^{-13}\\,\\mathrm J.\n$$"
    )
    
    # In 18-bai-tap-du-lieu-nang-cao.md:
    content = content.replace(
        "$$\n\\begin{aligned}\nP&=U-2\\beta V+\\beta^2W,\\\\\nQ&=W-2\\beta V+\\beta^2U.\n\\end{aligned}\n$$",
        "$$\nP = U - 2\\beta V + \\beta^2W, \\quad Q = W - 2\\beta V + \\beta^2U.\n$$"
    )

    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
print("Updated chapter 37 math successfully.")
