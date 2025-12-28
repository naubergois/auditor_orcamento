from PIL import Image, ImageDraw, ImageFont

def create_code_flow_diagram():
    width = 800
    height = 400
    bg_color = (250, 250, 250)
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Colors
    line_color = (100, 100, 100)
    box_fill = (255, 255, 255)
    box_outline = (0, 0, 0)
    text_color = (0, 0, 0)
    
    # Lifelines
    actors = ["User", "Streamlit App", "Orchestrator", "Agents"]
    x_positions = [100, 300, 500, 700]
    y_start = 50
    y_end = 350
    
    for i, actor in enumerate(actors):
        x = x_positions[i]
        # Draw Actor Box
        draw.rectangle((x-60, y_start-30, x+60, y_start+10), fill=box_fill, outline=box_outline)
        
        # Draw Text (approx center)
        text_bbox = draw.textbbox((0, 0), actor)
        w = text_bbox[2] - text_bbox[0]
        draw.text((x - w/2, y_start-20), actor, fill=text_color)
        
        # Draw Lifeline
        draw.line((x, y_start+10, x, y_end), fill=line_color, width=1)
        # Dashed effect simulation not easy, just solid line
        
    # Messages
    def draw_msg(y, start_idx, end_idx, msg):
        x1 = x_positions[start_idx]
        x2 = x_positions[end_idx]
        if x1 < x2:
            x2 -= 5
        else:
            x2 += 5
            
        draw.line((x1, y, x2, y), fill=text_color, width=2)
        # Arrowhead
        if x1 < x2:
            draw.polygon([(x2, y), (x2-10, y-5), (x2-10, y+5)], fill=text_color)
        else:
            draw.polygon([(x2, y), (x2+10, y-5), (x2+10, y+5)], fill=text_color)
            
        # Text
        mid_x = (x1 + x2) / 2
        text_bbox = draw.textbbox((0, 0), msg)
        w = text_bbox[2] - text_bbox[0]
        draw.text((mid_x - w/2, y - 15), msg, fill=text_color)

    draw_msg(100, 0, 1, "Upload PDF")
    draw_msg(150, 1, 2, "run_audit(text)")
    draw_msg(200, 2, 3, "Parallel Execution")
    draw_msg(250, 3, 2, "Return Results")
    draw_msg(300, 2, 1, "Show Dashboard")

    img.save('code_diagram.png')
    print("Code flow diagram created: code_diagram.png")

if __name__ == "__main__":
    create_code_flow_diagram()
