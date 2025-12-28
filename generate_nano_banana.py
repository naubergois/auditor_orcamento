from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_nano_banana_diagrams():
    # Helper to draw rounded box
    def draw_rounded_box(draw, x, y, w, h, radius, fill, outline, width=2):
        draw.rounded_rectangle((x, y, x+w, y+h), radius=radius, fill=fill, outline=outline, width=width)
        
    # --- Architecture Diagram ---
    width, height = 1000, 600
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Palette "Nano Banana" (Vibrant, SaaS)
    color_orch = (99, 102, 241) # Indigo
    color_agent = (16, 185, 129) # Emerald
    color_bg_box = (243, 244, 246) # Gray 100
    text_color = (17, 24, 39) # Gray 900
    white = (255, 255, 255)
    
    # Orchestrator (Center)
    orch_x, orch_y = 400, 250
    orch_w, orch_h = 200, 100
    
    # Agents (Orbiting)
    agents = [
        ("Auditoria", 100, 100),
        ("Compliance", 700, 100),
        ("Consistência", 100, 400),
        ("Explicação", 700, 400)
    ]
    
    # Connectors (Curved lines simulated)
    for name, ax, ay in agents:
        # Draw line from center to agent center
        draw.line((orch_x+orch_w/2, orch_y+orch_h/2, ax+100, ay+50), fill=(209, 213, 219), width=3)
        
    # Draw Nodes
    draw_rounded_box(draw, orch_x, orch_y, orch_w, orch_h, 20, color_orch, None)
    draw.text((orch_x + 50, orch_y + 40), "ORCHESTRATOR", fill=white)
    
    for name, ax, ay in agents:
        draw_rounded_box(draw, ax, ay, 200, 100, 15, color_agent, None)
        draw.text((ax + 50, ay + 40), name.upper(), fill=white)
        
    img.save('architecture_v3.png')
    print("architecture_v3.png created (Nano Banana Style)")
    
    # --- Code Flow Diagram ---
    # Not implementing v2 for now, keeping v1 or reusing similar logic if needed,
    # but architecture was the main request.

if __name__ == "__main__":
    create_nano_banana_diagrams()
