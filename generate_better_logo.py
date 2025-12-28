from PIL import Image, ImageDraw

def create_better_logo():
    width = 500
    height = 500
    
    # Create valid image
    image = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Colors
    blue = (31, 119, 180)
    dark_grey = (50, 50, 50)
    light_grey = (220, 220, 220)
    white = (255, 255, 255)
    
    # 1. Draw Document Icon (Back)
    doc_x1, doc_y1 = 150, 100
    doc_x2, doc_y2 = 350, 400
    
    # Shadow/Outline
    draw.rectangle((doc_x1+5, doc_y1+5, doc_x2+5, doc_y2+5), fill=light_grey)
    # Main Doc
    draw.rectangle((doc_x1, doc_y1, doc_x2, doc_y2), fill=white, outline=dark_grey, width=3)
    
    # Lines representing text
    for y in range(doc_y1 + 40, doc_y2 - 30, 30):
        draw.line((doc_x1 + 30, y, doc_x2 - 30, y), fill=light_grey, width=5)
        
    # 2. Draw Magnifying Glass (Front)
    # Circle
    glass_center = (250, 250)
    glass_radius = 80
    glass_width = 15
    
    # Handle
    handle_len = 80
    handle_width = 20
    # 45 degree angle approx
    start_x = glass_center[0] + 50
    start_y = glass_center[1] + 50
    end_x = start_x + handle_len
    end_y = start_y + handle_len
    
    draw.line((start_x, start_y, end_x, end_y), fill=dark_grey, width=handle_width)
    
    # Glass Rim
    left_up = (glass_center[0] - glass_radius, glass_center[1] - glass_radius)
    right_down = (glass_center[0] + glass_radius, glass_center[1] + glass_radius)
    draw.ellipse((left_up, right_down), outline=blue, width=glass_width)
    
    # Glass Lens (Semi-transparent look - simulated by just being empty or light blue)
    # Since we are RGB, we can't do real alpha easily without saving as PNG with alpha, 
    # but let's just leave it clear (showing the doc lines behind) or add a tint if we had alpha.
    # We will just leave it open to see the document behind, which implies transparency.
    
    image.save('logo.png')
    print("Better logo created: logo.png")

if __name__ == "__main__":
    create_better_logo()
