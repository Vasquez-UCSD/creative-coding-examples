# --- Global Configuration ---
canvas = None
corners = [] 
selected_idx = -1
is_calibrating = True

# Ivy State Variables
ivy_pos = None 

def setup():
    smooth(8)
    size(1200, 800, P3D)
    
    global canvas, corners, ivy_pos
    
    # 1. Initialize the Virtual Canvas
    canvas = create_graphics(1200, 800, P3D)
    canvas.begin_draw()
    canvas.background(0)
    canvas.end_draw()
    
    # 2. Starting position for the Ivy (Bottom Center)
    ivy_pos = Py5Vector(600, 800)
    
    # 3. Define 4 corners for the projection surface
    corners = [
        Py5Vector(100, 100),                
        Py5Vector(width - 100, 100),        
        Py5Vector(width - 100, height - 100), 
        Py5Vector(100, height - 100)         
    ]

def draw():
    global ivy_pos
    background(0) 
    
    # --- 1. DYNAMIC INPUT MAPPING ---
    mx = constrain(mouse_x, 0, width)
    my = constrain(mouse_y, 0, height)
    
    wind = remap(mx, 0, width, -3, 3)
    upward_force = remap(my, 0, height, 5, 0.2)
    g_channel = remap(mx, 0, width, 120, 255)
    
    # --- 2. UPDATE IVY SIMULATION ---
    canvas.begin_draw()
    
    new_x = ivy_pos.x + random(-4, 4) + wind
    new_y = ivy_pos.y - random(0, upward_force)
    
    thickness = remap(ivy_pos.y, 0, 800, 0.5, 4) # Thinner at top
    
    canvas.stroke(34, g_channel, 34, 180)
    canvas.stroke_weight(thickness)
    canvas.line(ivy_pos.x, ivy_pos.y, new_x, new_y)
    
    # FIXED: Direct property assignment instead of .set()
    ivy_pos.x = new_x
    ivy_pos.y = new_y
    
    # Reset Logic
    if ivy_pos.y < 0 or ivy_pos.x < -100 or ivy_pos.x > 1300:
        ivy_pos.x = random(width)
        ivy_pos.y = height
        
    canvas.end_draw()
    
    # --- 3. RENDER WARPED SURFACE ---
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL)
    
    vertex(corners[0].x, corners[0].y, 0, 0, 0) 
    vertex(corners[1].x, corners[1].y, 0, 1, 0) 
    vertex(corners[2].x, corners[2].y, 0, 1, 1) 
    vertex(corners[3].x, corners[3].y, 0, 0, 1) 
    end_shape()
    
    # --- 4. CALIBRATION UI ---
    if is_calibrating:
        draw_ui()

def draw_ui():
    for i, p in enumerate(corners):
        stroke(255)
        fill(255, 0, 0) if i == selected_idx else fill(0, 255, 255, 150)
        circle(p.x, p.y, 25)
    
    fill(255)
    text_size(16)
    text("CALIBRATION MODE", 25, 40)
    text("• DRAG circles to match your wall corners", 25, 65)
    text("• PRESS 'C' to toggle UI | PRESS 'R' to clear", 25, 85)

def mouse_pressed():
    global selected_idx
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 30:
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
    if key.lower() == 'r':
        canvas.begin_draw()
        canvas.background(0)
        canvas.end_draw()