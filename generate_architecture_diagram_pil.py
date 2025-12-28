from PIL import Image, ImageDraw, ImageFont

def create_architecture_diagram_pil():
    # Setup
    width = 800
    height = 500
    bg_color = (255, 255, 255)
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Colors
    blue = (13, 71, 161)
    light_blue = (227, 242, 253)
    border = (25, 118, 210)
    text_color = (0, 0, 0)
    white = (255, 255, 255)
    
    def draw_box(x, y, w, h, text, bg=light_blue, outline=border):
        draw.rectangle((x, y, x+w, y+h), fill=bg, outline=outline, width=2)
        # Simple centering for text (approximate)
        text_bbox = draw.textbbox((0, 0), text)
        text_w = text_bbox[2] - text_bbox[0]
        text_h = text_bbox[3] - text_bbox[1]
        draw.text((x + (w - text_w)/2, y + (h - text_h)/2), text, fill=text_color)
        return (x + w/2, y + h/2) # Return center
    
    # Central Node: Orchestrator
    orch_center = draw_box(300, 200, 200, 80, "Orchestrator\n(Coordenador)", bg=blue, outline=blue)
    # Re-draw text in white for Orchestrator
    draw.text((355, 230), "Orchestrator", fill=white)
    
    # Agents
    # Top Left
    auditor_center = draw_box(50, 50, 180, 60, "Auditor Agent\n(Risco Fiscal)")
    # Top Right
    compliance_center = draw_box(570, 50, 180, 60, "Compliance Agent\n(Legal)")
    # Bottom Left
    consistency_center = draw_box(50, 390, 180, 60, "Consistency Agent\n(Dados)")
    # Bottom Right
    explain_center = draw_box(570, 390, 180, 60, "Explainability Agent\n(Explicação)")
    
    # Connections
    for center in [auditor_center, compliance_center, consistency_center, explain_center]:
        draw.line((orch_center[0], orch_center[1], center[0], center[1]), fill=border, width=2)
    
    # Inputs/Outputs
    # Input
    draw_box(350, 50, 100, 40, "Input: PDF", bg=(255, 253, 231), outline=(251, 192, 45))
    draw.line((400, 90, 400, 200), fill=(251, 192, 45), width=2)
    
    # Output
    draw_box(350, 410, 100, 40, "Output: Relatório", bg=(232, 245, 233), outline=(56, 142, 60))
    draw.line((400, 280, 400, 410), fill=(56, 142, 60), width=2)
    
    img.save('architecture_v2.png')
    print("Architecture diagram created with PIL: architecture_v2.png")

if __name__ == "__main__":
    create_architecture_diagram_pil()
