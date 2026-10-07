from PIL import Image
import numpy as np

# Load the user-uploaded image for dark backgrounds
im = Image.open(r'C:/Users/Ai/.gemini/antigravity/brain/6e242531-482a-4de3-85a7-11b25e63ed47/.user_uploaded/media_1791362591178.png').convert('RGBA')
arr = np.array(im, dtype=np.float32)

# Corner background color is ~ (20, 24, 23)
bg_color = np.array([20.0, 24.0, 23.0])

rgb = arr[:, :, :3]
diff = np.linalg.norm(rgb - bg_color, axis=2)

# Smooth alpha calculation
t_low = 14.0
t_high = 40.0
alpha = np.clip((diff - t_low) / (t_high - t_low), 0.0, 1.0) * 255.0

# Ensure background noise is 0
max_ch = rgb.max(axis=2)
alpha[max_ch < 32] = 0.0

arr[:, :, 3] = alpha
result = Image.fromarray(arr.astype(np.uint8))

# Find content bounding box
mask = alpha > 10
rows = np.any(mask, axis=1)
cols = np.any(mask, axis=0)
rmin, rmax = np.where(rows)[0][[0, -1]]
cmin, cmax = np.where(cols)[0][[0, -1]]

pad = 12
cmin = max(0, cmin - pad)
rmin = max(0, rmin - pad)
cmax = min(im.width - 1, cmax + pad)
rmax = min(im.height - 1, rmax + pad)

cropped = result.crop((cmin, rmin, cmax + 1, rmax + 1))

# Save official logo-dark.png
cropped.save('docs/public/logo-dark.png')
print('docs/public/logo-dark.png generated. Size:', cropped.size)

# Generate previews on different dark backgrounds
for bg_hex in ['#161918', '#202624', '#0d1117']:
    bg_c = tuple(int(bg_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    canvas = Image.new('RGB', (cropped.width + 40, cropped.height + 40), bg_c)
    canvas.paste(cropped, (20, 20), cropped)
    canvas.save(f'qa/preview-dark-{bg_hex.lstrip("#")}.png')

print('Previews generated in qa/')
