from PIL import Image, ImageDraw, ImageFont
import os

def create_text_box(draw, x, y, w, h, text, bg_color, border_color):
    draw.rectangle([x, y, x+w, y+h], fill=bg_color, outline=border_color, width=2)
    # Simple centering approximation
    font = ImageFont.load_default()
    # For better centering we would use textbbox but detailed pil logic is lengthy.
    # We'll just pad.
    draw.text((x+10, y+h/2-5), text, fill=(0,0,0), font=font)

def generate_data_flow():
    # 800x400
    img = Image.new('RGB', (800, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # 1. User/PDF
    create_text_box(draw, 50, 150, 120, 80, "PDF Upload", (220, 230, 250), (30, 60, 114))
    
    # Arrow
    draw.line([(170, 190), (220, 190)], fill=(0,0,0), width=3)
    draw.polygon([(220, 190), (210, 185), (210, 195)], fill=(0,0,0))
    
    # 2. Extraction
    create_text_box(draw, 220, 150, 140, 80, "Text Extraction\n(Python/Streamlit)", (255, 240, 220), (200, 100, 0))
    
    # Arrow
    draw.line([(360, 190), (410, 190)], fill=(0,0,0), width=3)
    draw.polygon([(410, 190), (400, 185), (400, 195)], fill=(0,0,0))
    
    # 3. AI Agents
    create_text_box(draw, 410, 100, 180, 180, "AI Agents Engine\n(Gemini 2.0)", (230, 255, 230), (0, 100, 0))
    
    # Arrow
    draw.line([(590, 190), (640, 190)], fill=(0,0,0), width=3)
    draw.polygon([(640, 190), (630, 185), (630, 195)], fill=(0,0,0))
    
    # 4. Report
    create_text_box(draw, 640, 150, 120, 80, "Final Report\n(PDF/Dashboard)", (220, 230, 250), (30, 60, 114))

    img.save("data_flow_didactic.png")
    print("Generated data_flow_didactic.png")

def generate_dashboard_explainer():
    # 800x500
    img = Image.new('RGB', (800, 500), (250, 250, 250))
    draw = ImageDraw.Draw(img)
    
    # Sidebar
    draw.rectangle([0, 0, 200, 500], fill=(240, 240, 240), outline=(200,200,200))
    draw.text((20, 50), "Menu", fill=(0,0,0))
    draw.text((20, 100), "Upload PDF", fill=(0,0,0))
    draw.text((20, 140), "Run Audit", fill=(0,0,200))
    
    # Main Area
    # Header
    draw.rectangle([220, 20, 780, 80], fill=(255,255,255), outline=(0,0,0))
    draw.text((240, 40), "Auditor Orçamento - Results", fill=(0,0,0))
    
    # Metrics
    create_text_box(draw, 220, 120, 150, 100, "Risks Found\n  HIGH", (255, 200, 200), (255,0,0))
    create_text_box(draw, 400, 120, 150, 100, "Compliance\n  OK", (200, 255, 200), (0,255,0))
    create_text_box(draw, 580, 120, 150, 100, "Consistency\n  98%", (200, 200, 255), (0,0,255))
    
    # Callout
    draw.line([(295, 220), (295, 300)], fill=(255,0,0), width=2)
    draw.text((250, 310), "Red = Immediate Attention", fill=(255,0,0))

    img.save("dashboard_explainer.png")
    print("Generated dashboard_explainer.png")

if __name__ == "__main__":
    generate_data_flow()
    generate_dashboard_explainer()
