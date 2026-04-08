# --- New Global State for Masking ---
mask_rects = [] # List of [top_left_vector, bottom_right_vector]
is_mask_enabled = True
is_adding_mask = False # Track if we are currently "drawing" a new mask

def setup():
    size(1200, 800, P3D)
    global canvas, corners, mask_rects
    canvas = create_graphics(1200, 800, P3D)
    
    # Default corners for calibration
    corners = [Py5Vector(100, 100), Py5Vector(1100, 100), 
               Py5Vector(1100, 700), Py5Vector(100, 700)]
    
    # Pre-define a "Doorway" mask for testing
    mask_rects.append([Py5Vector(400, 300), Py5Vector(600, 800)])

def draw():
    background(0)
    
    # 1. Update and Draw Simulation to Canvas
    canvas.begin_draw()
    canvas.background(0) 
    
    # --- [INSERT YOUR IVY SYSTEM HERE] ---
    # For now, a placeholder to show the mask works:
    canvas.stroke(0, 255, 100)
    canvas.stroke_weight(5)
    for i in range(0, canvas.width, 20):
        canvas.line(i, 0, canvas.width - i, canvas.height)
    
    # 2. Apply the Mask (If enabled)
    if is_mask_enabled:
        canvas.no_stroke()
        canvas.fill(0) # Blackout color
        for m in mask_rects:
            # Draw a rectangle between the two stored points
            w = m[1].x - m[0].x
            h = m[1].y - m[0].y
            canvas.rect(m[0].x, m[0].y, w, h)
    
    canvas.end_draw()
    
    # 3. Render the Keystone Warped Surface
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL)
    vertex(corners[0].x, corners[0].y, 0, 0, 0)
    vertex(corners[1].x, corners[1].y, 0, 1, 0)
    vertex(corners[2].x, corners[2].y, 0, 1, 1)
    vertex(corners[3].x, corners[3].y, 0, 0, 1)
    end_shape()
    
    # 4. Calibration UI
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    # ... previous corner drawing code ...
    
    # Draw existing masks as semi-transparent red for visibility
    fill(255, 0, 0, 100)
    stroke(255, 0, 0)
    for m in mask_rects:
        rect(m[0].x, m[0].y, m[1].x - m[0].x, m[1].y - m[0].y)
    
    fill(255)
    msg = f"MASKING: {'ON' if is_mask_enabled else 'OFF'} (Press 'M' to Toggle)\n"
    msg += "Hold 'N' and Drag to create a new Mask. Press 'X' to clear all."
    text(msg, 20, 30)

# --- Updated Interaction Logic ---

def key_pressed():
    global is_calibrating, is_mask_enabled, mask_rects
    if key.lower() == 'c':
        is_calibrating = not is_calibrating
    if key.lower() == 'm':
        is_mask_enabled = not is_mask_enabled
    if key.lower() == 'x':
        mask_rects = []

def mouse_pressed():
    global selected_idx, is_adding_mask
    # Check corners first
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i
            return
            
    # If holding 'N', start a new mask
    if is_key_pressed and key.lower() == 'n':
        # Start a mask at current mouse pos
        mask_rects.append([Py5Vector(mouse_x, mouse_y), Py5Vector(mouse_x, mouse_y)])
        is_adding_mask = True

def mouse_dragged():
    if selected_idx != -1:
        corners[selected_idx].set(mouse_x, mouse_y)
    elif is_adding_mask:
        # Update the bottom-right corner of the last mask
        mask_rects[-1][1].set(mouse_x, mouse_y)

def mouse_released():
    global selected_idx, is_adding_mask
    selected_idx = -1
    is_adding_mask = False