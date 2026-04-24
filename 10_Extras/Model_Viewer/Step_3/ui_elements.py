# PY5 IMPORTED MODE CODE

def draw_ui(mode, x_off, y_off, rot_x, rot_y, params):
    # Now all py5 functions will work here
    camera()
    hint(DISABLE_DEPTH_TEST)

def draw_axis(x_off, y_off, rot_x, rot_y ):
    """Draws a coordinate crosshair in the top right, offset by dragging"""
    push_matrix()
    
    # Reset to 2D view for the UI
    camera()
    hint(DISABLE_DEPTH_TEST)
    
    # Position in top right, but influenced by dragging
    translate(width - 100 + x_off, 100 + y_off)
    
    stroke(255, 0, 0) # Red X-axis
    line(-50, 0, 50, 0)
    stroke(0, 255, 0) # Green Y-axis
    line(0, -50, 0, 50)
    
    fill(255)
    text_size(14)
    
    #Display the 3D rotation values
    text(f"ROT_X: {degrees(rot_x) : .1}°", 10, 25)
    text(f"ROT_Y: {degrees(rot_y) : .1}°", 10, 40)
    
    hint(ENABLE_DEPTH_TEST)
    pop_matrix()