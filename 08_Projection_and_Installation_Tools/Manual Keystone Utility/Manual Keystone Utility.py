# --- Global Calibration Data ---
canvas = None
corners = [] 
selected_idx = -1
is_calibrating = True

# Ivy Variables
ivy_x, ivy_y = 600, 800 # Start at bottom center

def setup():
    size(1200, 800, P3D)
    global canvas, corners
    
    # 1. Create the 'Virtual' ivy wall
    canvas = create_graphics(1200, 800, P3D)
    canvas.begin_draw()
    canvas.background(0) # Initialize with black once
    canvas.end_draw()
    
    # 2. Define 4 corners for warping
    corners = [
        Py5Vector(100, 100),
        Py5Vector(width - 100, 100),
        Py5Vector(width - 100, height - 100),
        Py5Vector(100, height - 100)
    ]

def draw():
    global ivy_x, ivy_y
    background(0) 
    
    # --- 1. Update Simulation on the Canvas ---
    canvas.begin_draw()
    # REMOVED: canvas.background(0) 
    # Removing background(0) here allows the ivy to "stick" and grow
    
    # Simple Ivy Growth Logic
    canvas.stroke(34, 139, 34, 150) # Forest Green with slight transparency
    canvas.stroke_weight(2)
    
    # Wiggle movement
    new_x = ivy_x + random(-5, 5)
    new_y = ivy_y - random(1, 4) # Move upwards
    
    # Draw the growth segment
    canvas.line(ivy_x, ivy_y, new_x, new_y)
    
    # Update position
    ivy_x, ivy_y = new_x, new_y
    
    # Reset ivy if it goes off screen
    if ivy_y < 0:
        ivy_y = height
        ivy_x = random(width)
        
    canvas.end_draw()
    
    # --- 2. Render the Warped Surface ---
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL) 
    
    vertex(corners[0].x, corners[0].y, 0, 0, 0) 
    vertex(corners[1].x, corners[1].y, 0, 1, 0) 
    vertex(corners[2].x, corners[2].y, 0, 1, 1) 
    vertex(corners[3].x, corners[3].y, 0, 0, 1) 
    end_shape()
    
    # --- 3. UI ---
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    fill(0, 255, 255, 150)
    for i, p in enumerate(corners):
        if i == selected_idx: fill(255, 0, 0)
        else: fill(0, 255, 255, 150)
        circle(p.x, p.y, 20)
    fill(255)
    text("DRAG CORNERS. Press 'C' to toggle UI. Press 'R' to reset Ivy.", 20, 30)

def mouse_pressed():
    global selected_idx
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i
            return

def mouse_dragged():
    if selected_idx != -1:
        corners[selected_idx].x, corners[selected_idx].y = mouse_x, mouse_y

def mouse_released():
    global selected_idx
    selected_idx = -1

def key_pressed():
    global is_calibrating
    if key.lower() == 'c':
        is_calibrating = not is_calibrating
    if key.lower() == 'r': # Clear the ivy
        canvas.begin_draw()
        canvas.background(0)
        canvas.end_draw()