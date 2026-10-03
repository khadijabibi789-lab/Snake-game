from PIL import Image, ImageDraw, ImageFont
import math

SIZE = 512
img = Image.new("RGB", (SIZE, SIZE), (15, 15, 15))
draw = ImageDraw.Draw(img)

GRID = 16
CELL = SIZE // GRID


def cell(x, y, color):
    draw.rectangle(
        [x * CELL + 2, y * CELL + 2, (x + 1) * CELL - 2, (y + 1) * CELL - 2],
        fill=color,
    )


snake_body = [
    (2, 12), (3, 12), (4, 12), (4, 11), (4, 10),
    (5, 10), (6, 10), (7, 10), (7, 11), (7, 12),
    (8, 12), (9, 12), (10, 12), (10, 11), (10, 10),
    (11, 10), (12, 10), (13, 10),
]
for i, (x, y) in enumerate(snake_body):
    shade = 200 if i == 0 else (160 if i % 2 == 0 else 120)
    cell(x, y, (0, shade, 0))

head_x, head_y = snake_body[0]
draw.ellipse(
    [head_x * CELL + CELL // 4, head_y * CELL + CELL // 4,
     head_x * CELL + 3 * CELL // 4, head_y * CELL + 3 * CELL // 4],
    fill=(255, 255, 255),
)
draw.ellipse(
    [head_x * CELL + CELL // 2, head_y * CELL + CELL // 4,
     head_x * CELL + 5 * CELL // 8, head_y * CELL + 3 * CELL // 8],
    fill=(0, 0, 0),
)

cell(13, 4, (220, 30, 30))
draw.ellipse(
    [13 * CELL + CELL // 3, 4 * CELL + CELL // 3,
     13 * CELL + 2 * CELL // 3, 4 * CELL + 2 * CELL // 3],
    fill=(255, 80, 80),
)

try:
    font = ImageFont.truetype("arial.ttf", 56)
except OSError:
    font = ImageFont.load_default()

title = "SNAKE"
bbox = draw.textbbox((0, 0), title, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text(((SIZE - tw) // 2, 18), title, fill=(0, 255, 0), font=font)

img.save("logo.png", "PNG")
img.save("logo.ico", format="ICO", sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
print("Logo created: logo.png, logo.ico")