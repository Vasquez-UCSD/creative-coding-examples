# --- Global Calibration Data ---
canvas = None
corners = [] # List of Py5Vectors
selected_idx = -1
is_calibrating = True

def setup():
    size(1200, 800, P3D)
    global canvas, corners
    
    # 1. Create the 'Virtual' ivy wall
    # This matches the aspect ratio of your projection
    canvas = create_graphics(1200, 800, P3D)
    
    # 2. Define 4 corners (Normalized positions)
    # P0: Top-Left, P1: Top-Right, P2: Bottom-Right, P3: Bottom-Left
    corners = [
        Py5Vector(100, 100),
        Py5Vector(width - 100, 100),
        Py5Vector(width - 100, height - 100),
        Py5Vector(100, height - 100)
    ]

def draw():
    background(0) # Keep background black for projectors
    
    # --- 1. Update Simulation on the Canvas ---
    canvas.begin_draw()
    canvas.background(0) # Ivy background
    # [YOUR IVY GROWTH LOGIC GOES HERE]
    # Example:
    canvas.stroke(0, 255, 0)
    canvas.line(0, 0, canvas.width, canvas.height) 
    canvas.end_draw()
    
    # --- 2. Render the Warped Surface ---
    # We use the canvas as a texture for a quad
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL) # Use 0.0 to 1.0 for UV mapping
    
    # Map corners to UV coordinates: vertex(x, y, z, u, v)
    vertex(corners[0].x, corners[0].y, 0, 0, 0) # Top-Left
    vertex(corners[1].x, corners[1].y, 0, 1, 0) # Top-Right
    vertex(corners[2].x, corners[2].y, 0, 1, 1) # Bottom-Right
    vertex(corners[3].x, corners[3].y, 0, 0, 1) # Bottom-Left
    end_shape()
    
    # --- 3. UI for Calibration ---
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    fill(255, 100)
    no_stroke()
    for i, p in enumerate(corners):
        # Highlight selected handle
        if i == selected_idx: fill(255, 0, 0)
        else: fill(0, 255, 255, 150)
        circle(p.x, p.y, 20)
    
    fill(255)
    text("CALIBRATION MODE: Drag corners to align. Press 'C' to hide UI.", 20, 30)

# --- Interaction Handlers ---

def mouse_pressed():
    global selected_idx
    # Check if we clicked near a corner handle
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i
            return

def mouse_dragged():
    if selected_idx != -1:
        corners[selected_idx].x = mouse_x
        corners[selected_idx].y = mouse_y

def mouse_released():
    global selected_idx
    selected_idx = -1

def key_pressed():
    global is_calibrating
    if key.lower() == 'c':
        is_calibrating = not is_calibrating