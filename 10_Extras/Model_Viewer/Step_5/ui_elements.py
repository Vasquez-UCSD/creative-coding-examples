# PY5 IMPORTED MODE CODE

def draw_ui(mode, rot_x, rot_y, zoom):
    # Now all py5 functions will work here
    camera()
    hint(DISABLE_DEPTH_TEST)
    
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