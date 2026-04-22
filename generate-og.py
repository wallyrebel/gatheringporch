"""Generate Open Graph image for The Gathering Porch website."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1200, 630

img = Image.new("RGB", (W, H), (245, 241, 237))  # warm cream background
draw = ImageDraw.Draw(img)

# Decorative border
border_color = (180, 160, 140)
gold = (185, 158, 115)
navy = (35, 55, 90)
soft_blue = (140, 170, 200)

# Outer border
draw.rectangle([20, 20, W-20, H-20], outline=gold, width=2)
draw.rectangle([30, 30, W-30, H-30], outline=gold, width=1)

# Corner decorative elements (small floral-like dots)
for cx, cy in [(50, 50), (W-50, 50), (50, H-50), (W-50, H-50)]:
    for angle in range(0, 360, 45):
        rad = math.radians(angle)
        dx = int(math.cos(rad) * 12)
        dy = int(math.sin(rad) * 12)
        draw.ellipse([cx+dx-3, cy+dy-3, cx+dx+3, cy+dy+3], fill=soft_blue)
    draw.ellipse([cx-5, cy-5, cx+5, cy+5], fill=gold)

# Decorative line accents at top and bottom
draw.line([(100, 60), (W-100, 60)], fill=gold, width=1)
draw.line([(100, H-60), (W-100, H-60)], fill=gold, width=1)

# Small diamond shapes along lines
for x in range(150, W-150, 80):
    for y_line in [60, H-60]:
        pts = [(x, y_line-5), (x+5, y_line), (x, y_line+5), (x-5, y_line)]
        draw.polygon(pts, fill=gold)

# Load fonts - try different sizes
try:
    font_the = ImageFont.truetype("arial", 28)
    font_gathering = ImageFont.truetype("arial", 80)
    font_porch = ImageFont.truetype("arial", 44)
    font_tagline = ImageFont.truetype("arial", 26)
    font_services = ImageFont.truetype("arial", 20)
    font_phone = ImageFont.truetype("arial", 28)
    font_location = ImageFont.truetype("arial", 18)
except:
    font_the = ImageFont.load_default()
    font_gathering = ImageFont.load_default()
    font_porch = ImageFont.load_default()
    font_tagline = ImageFont.load_default()
    font_services = ImageFont.load_default()
    font_phone = ImageFont.load_default()
    font_location = ImageFont.load_default()

# Soft decorative circles in background
for cx, cy, r, alpha_color in [
    (200, 300, 80, (200, 215, 230)),
    (1000, 200, 60, (220, 200, 210)),
    (900, 450, 70, (200, 220, 200)),
    (150, 150, 40, (220, 210, 200)),
    (1050, 500, 50, (210, 220, 230)),
]:
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=alpha_color)

# "the" text
bbox = draw.textbbox((0, 0), "the", font=font_the)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2 - 60, 140), "the", fill=navy, font=font_the)

# "Gathering" text - large and bold
try:
    font_gathering_bold = ImageFont.truetype("arialbd", 80)
except:
    font_gathering_bold = font_gathering

bbox = draw.textbbox((0, 0), "Gathering", font=font_gathering_bold)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 165), "Gathering", fill=navy, font=font_gathering_bold)

# "PORCH" text - spaced out
try:
    font_porch_bold = ImageFont.truetype("arialbd", 44)
except:
    font_porch_bold = font_porch

porch_text = "P O R C H"
bbox = draw.textbbox((0, 0), porch_text, font=font_porch_bold)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 250), porch_text, fill=navy, font=font_porch_bold)

# Decorative divider
y_div = 310
draw.line([(W//2 - 120, y_div), (W//2 - 20, y_div)], fill=gold, width=2)
draw.line([(W//2 + 20, y_div), (W//2 + 120, y_div)], fill=gold, width=2)
draw.ellipse([W//2 - 6, y_div - 6, W//2 + 6, y_div + 6], fill=gold)

# Tagline
try:
    font_tagline_italic = ImageFont.truetype("ariali", 26)
except:
    font_tagline_italic = font_tagline

tagline = '"Where Memories Take Root"'
bbox = draw.textbbox((0, 0), tagline, font=font_tagline_italic)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 330), tagline, fill=(120, 100, 80), font=font_tagline_italic)

# Services line
services = "Venue Rental  |  Catering  |  Wedding Coordination  |  Event Planning"
bbox = draw.textbbox((0, 0), services, font=font_services)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 390), services, fill=(100, 100, 100), font=font_services)

# Divider before contact
y_div2 = 430
draw.line([(W//2 - 80, y_div2), (W//2 + 80, y_div2)], fill=gold, width=1)

# Location
location = "Ripley, Mississippi"
bbox = draw.textbbox((0, 0), location, font=font_location)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 450), location, fill=(130, 130, 130), font=font_location)

# Phone
phone = "(662) 750-8394"
try:
    font_phone_bold = ImageFont.truetype("arialbd", 28)
except:
    font_phone_bold = font_phone
bbox = draw.textbbox((0, 0), phone, font=font_phone_bold)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 485), phone, fill=navy, font=font_phone_bold)

# Website
website = "GatheringPorchRipley.com"
bbox = draw.textbbox((0, 0), website, font=font_services)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 530), website, fill=gold, font=font_services)

img.save("C:/Users/myers/OneDrive/Desktop/gatheringporch/og-image.png", "PNG", quality=95)
print("OG image generated: og-image.png (1200x630)")
