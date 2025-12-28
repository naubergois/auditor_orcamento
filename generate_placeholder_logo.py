from PIL import Image, ImageDraw, ImageFont

def create_placeholder_logo():
    width = 200
    height = 200
    image = Image.new('RGB', (width, height), color = (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw a blue circle
    draw.ellipse((20, 20, 180, 180), fill=(31, 119, 180), outline=None)
    
    # Draw a simple text or shape
    # We don't rely on fonts being present, so just draw a rectangle simulating a document
    draw.rectangle((70, 60, 130, 140), fill=(255, 255, 255))
    
    image.save('logo.png')
    print("Placeholder logo created: logo.png")

if __name__ == "__main__":
    create_placeholder_logo()
