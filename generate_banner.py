from PIL import Image, ImageDraw, ImageFont

def create_banner():
    # Dimensions: 1200x300 (standard banner size)
    width, height = 1200, 300
    
    # Gradient Background (Blue to Dark Blue)
    img = Image.new('RGB', (width, height), (30, 60, 114)) # fallback base
    draw = ImageDraw.Draw(img)
    
    # Simulate gradient
    for y in range(height):
        # Interpolate color
        r = int(30 + (42 - 30) * y / height)
        g = int(60 + (82 - 60) * y / height)
        b = int(114 + (152 - 114) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
        
    # Draw "Tech Nodes" (Circles and lines)
    fill_node = (255, 255, 255, 30) # Transparent white
    
    # Draw simple network pattern
    nodes = [(100, 150), (200, 50), (200, 250), (1000, 100), (1100, 200)]
    for x, y in nodes:
         # draw.ellipse not supporting alpha directly on RGB image easily without conversion
         # Let's simple draw semi-transparent lines if possible, or just solid light blue
         draw.ellipse((x-10, y-10, x+10, y+10), fill=(100, 149, 237), outline=None)

    # Text "AUDITOR ORÇAMENTO"
    # Using default font large size if possible, or basic simple placement
    # PIL default font is tiny, let's try to load a system font or just scale basic logic (hard without font file)
    # We will simply draw multiple times for thickness or use simple text
    
    try:
        # Try loading a truetype font if available
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 80)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 40)
    except:
        font = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        # Scale is too small, but it's a fallback.
        
    text = "AUDITOR ORÇAMENTO"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    fw = text_bbox[2] - text_bbox[0]
    fh = text_bbox[3] - text_bbox[1]
    
    draw.text(((width - fw) / 2, (height - fh) / 2 - 20), text, font=font, fill=(255, 255, 255))
    
    subtext = "Inteligência Artificial Aplicada à Fiscalização"
    sub_bbox = draw.textbbox((0, 0), subtext, font=font_sub)
    sw = sub_bbox[2] - sub_bbox[0]
    
    draw.text(((width - sw) / 2, (height - fh) / 2 + 80), subtext, font=font_sub, fill=(200, 200, 200))

    img.save('app_banner.png')
    print("app_banner.png created")

if __name__ == "__main__":
    create_banner()
