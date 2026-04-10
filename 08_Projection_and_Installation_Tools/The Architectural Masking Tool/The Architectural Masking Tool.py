from py5 import *

# --- Global State ---
mask_rects = []         
is_mask_enabled = True
is_adding_mask = False  
is_calibrating = True   
selected_idx = -1       
corners = []            
canvas = None           

def setup():
    size(1200, 800, P3D)
    global canvas, corners
    
    # Internal drawing buffer
    canvas = create_graphics(1200, 800, P3D)
    
    # Default corners for keystone calibration
    # These represent the 4 corners of your projection surface
    corners = [Py5Vector(100, 100), Py5Vector(1100, 100), 
               Py5Vector(1100, 700), Py5Vector(100, 700)]

def draw():
    # Keep the background black so the projector sends no light to the rest of the wall
    background(0)
    
    # --- 1. Draw Simulation to Canvas ---
    canvas.begin_draw()
    canvas.background(0) 
    
    # Placeholder: Green grid lines (Your Ivy/Acoustic system goes here)
    canvas.stroke(0, 255, 100)
    canvas.stroke_weight(5)
    for i in range(0, canvas.width, 40):
        canvas.line(i, 0, canvas.width - i, canvas.height)
    canvas.end_draw()
    
    # --- 2. Render the Keystone Warped Surface ---
    # This projects the 'canvas' onto the 'corners'
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL)
    vertex(corners[0].x, corners[0].y, 0, 0, 0)
    vertex(corners[1].x, corners[1].y, 0, 1, 0)
    vertex(corners[2].x, corners[2].y, 0, 1, 1)
    vertex(corners[3].x, corners[3].y, 0, 0, 1)
    end_shape()
    
    # --- 3. The "True" Masking Layer ---
    # Drawn ON TOP of everything else to ensure light is removed from the wall
    if is_mask_enabled:
        no_stroke()
        fill(0) # Pure black = No light from projector
        for m in mask_rects:
            # min/abs logic ensures the rect draws correctly even if dragged backwards
            x = min(m[0].x, m[1].x)
            y = min(m[0].y, m[1].y)
            w = abs(m[1].x - m[0].x)
            h = abs(m[1].y - m[0].y)
            rect(x, y, w, h)
    
    # --- 4. Calibration UI (Only visible when 'C' is toggled) ---
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    # Draw yellow corner handles for keystone dragging
    no_stroke()
    fill(255, 255, 0, 150)
    for p in corners:
        circle(p.x, p.y, 25)
        
    # Draw red outlines so you can see where your masks are while calibrating
    no_fill()
    stroke(255, 0, 0)
    stroke_weight(2)
    for m in mask_rects:
        x = min(m[0].x, m[1].x)
        y = min(m[0].y, m[1].y)
        w = abs(m[1].x - m[0].x)
        h = abs(m[1].y - m[0].y)
        rect(x, y, w, h)
    
    fill(255)
    text_size(16)
    msg = f"MASKING: {'ACTIVE' if is_mask_enabled else 'OFF'}\n"
    msg += "HOLD 'N' + DRAG: Create Mask (Blackout)\n"
    msg += "PRESS 'X': Clear All Masks\n"
    msg += "PRESS 'C': Hide/Show UI for Projection"
    text(msg, 20, 30)

# --- Interaction Logic ---

def key_pressed():
    global is_calibrating, is_mask_enabled, mask_rects
    if key.lower() == 'c':
        is_calibrating = not is_calibrating
    if key.lower() == 'm':
        is_mask_enabled = not is_mask_enabled
    if key.lower() == 'x':
        mask_rects = [] # This "brings the draw back" by removing the blackout zones

def mouse_pressed():
    global selected_idx, is_adding_mask
    # Check if we are selecting a corner to adjust the keystone
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i
            return
            
    # If holding 'N', start creating a new blackout mask
    if is_key_pressed and key.lower() == 'n':
        mask_rects.append([Py5Vector(mouse_x, mouse_y), Py5Vector(mouse_x, mouse_y)])
        is_adding_mask = True

def mouse_dragged():
    if selected_idx != -1:
        # Update keystone corner position
        corners[selected_idx] = Py5Vector(mouse_x, mouse_y)
    elif is_adding_mask:
        # Update the size of the mask being drawn
        mask_rects[-1][1] = Py5Vector(mouse_x, mouse_y)

def mouse_released():
    global selected_idx, is_adding_mask
    selected_idx = -1
    is_adding_mask = False
