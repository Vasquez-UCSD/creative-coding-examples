# PY5 IMPORTED MODE CODE

def draw_ui(mode, rot_x, rot_y, zoom, poly_count, mx, my, style_on):
    # Now all py5 functions will work here
    camera()
    hint(DISABLE_DEPTH_TEST)
    no_lights()
    
    # Top Left STATS - Tri Count
    fill(255)
    text_align(LEFT)
    text_size(18)
    text(f"TRIANGLE COUNT: {poly_count}", 20, 30)
    
    # Hot Box Buttons
    modes = ["ROTATE", "LIGHT", "SPOT", "STYLE"]
    button_y = height - 60
    button_w, button_h = 100, 40
    
    for i, m in enumerate(modes):
        bx = 20 + (i * 110)
        
        # Check if mouse is inside this button Hot Box
        is_hovering = (mx > bx and mx < bx + button_w and my > button_y and my < button_y + button_h)
        
        if m == "STYLE":
            # STYLE button turns green if override is ON
            fill(100, 200, 100) if style_on else fill(50)           
        elif mode == m:
            fill(100, 200, 100) # Green is Active
        elif is_hovering:
            fill(100) # Grey for Hover
        else:
            fill(50) # Dark for Inactive
            
        stroke(255)
        stroke_weight(2)
        rect(bx, button_y, button_w, button_h, 5) # 5 is the corner radius
        
        fill(255)
        text_align(CENTER, CENTER)
        text(m, bx + button_w/2, button_y + button_h/2)
    
    # Fixed Coordinate Axis (Top Right)
    push_matrix()
    translate(width - 80, 80)
    
    # Apply the SAME rotations used for the 3D model
    rotate_x(rot_x)
    rotate_y(rot_y)
    
    stroke_weight(3)
    # Red X-axis
    stroke(255, 0, 0)
    line(-40, 0, 40, 0)
    
    # Green Y-axis
    stroke(0, 255, 0)
    line(0, -40, 0, 40)
    
    # Z-Axis (Blue)
    stroke(0, 0, 255)
    line(0, 0, -40, 0, 0, 40)
    
    pop_matrix()
    
    # Text Data (Draw this AFTER pop_matrix so the text doesn't rotate!)
    fill(255)
    text_align(RIGHT)
    text_size(12)
    # Display the 3D rotation values in the UI
    text("COORDINATE_GAUGE", width - 20, 30)
    text(f"X-ROT: {degrees(rot_x):.1f}", width - 20, 140)
    text(f"Y-ROT: {degrees(rot_y):.1f}", width - 20, 155)
    
    #Mouse Operations HUD (Bottom Right)
    # We actually need to loop through the list to display it
    instructions = [
        "Controlls:",
        f"MODE: {mode}",
        "DRAG: Rotate",
        "WHEEL: Zoom (Scale)",
        "F: Fit Screen", 
        f"ZOOM LEVEL: {round(zoom * 100)}%"
    ]
    
    fill(255, 150) 
    for i, txt_line in enumerate(instructions):
        # Draw each line 20 pixels apart
        text(txt_line, width - 20, height - 120 + (i * 20))
    
    hint(ENABLE_DEPTH_TEST)