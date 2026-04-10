# --- Global Configuration ---
canvas = None
corners = [] 
selected_idx = -1
is_calibrating = True
ivy_pos = None 

def setup():
    smooth(8)
    size(1200, 800, P3D)
    global canvas, corners, ivy_pos
    
    canvas = create_graphics(1200, 800, P3D)
    canvas.begin_draw()
    canvas.background(0)
    canvas.end_draw()
    
    ivy_pos = Py5Vector(600, 800)
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
    wind_noise = noise(frame_count * 0.01) 
    wind_force = remap(wind_noise, 0, 1, -10, 10) # <--- Our Wind Value
    
    mx = constrain(mouse_x, 0, width)
    my = constrain(mouse_y, 0, height)
    upward_force = remap(my, 0, height, 5, 0.2)
    g_channel = remap(mx, 0, width, 120, 255)
    
    # --- 2. UPDATE IVY SIMULATION ---
    canvas.begin_draw()
    wiggle = (noise(frame_count * 0.05) - 0.5) * 8
    new_x = ivy_pos.x + wiggle + wind_force
    new_y = ivy_pos.y - random(0, upward_force)
    
    thickness = remap(constrain(ivy_pos.y, 0, 800), 0, 800, 0.5, 4)
    canvas.stroke(34, g_channel, 34, 180)
    canvas.stroke_weight(thickness)
    canvas.line(ivy_pos.x, ivy_pos.y, new_x, new_y)
    
    ivy_pos.x = new_x
    ivy_pos.y = new_y
    
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
    
    # --- 4. UI (Passing wind_force here) ---
    if is_calibrating:
        draw_ui(wind_force)

def draw_ui(w_force):
    # Draw Draggable Handles
    for i, p in enumerate(corners):
        stroke(255)
        fill(255, 0, 0) if i == selected_idx else fill(0, 255, 255, 150)
        circle(p.x, p.y, 25)
    
    # HUD Background
    no_stroke()
    fill(0, 150)
    rect(15, 15, 450, 110, 10)
    
    # Text Data
    fill(255)
    text_size(16)
    text("CALIBRATION MODE", 25, 40)
    text(f"Current Wind Force: {round(w_force, 2)}", 25, 65)
    text("• SPACE: Leaf | • C: Hide UI | • R: Reset", 25, 110)
    
    # Wind Gauge Visual
    # A center line with a bar that moves left/right
    stroke(255, 100)
    line(25, 85, 225, 85) # Base line
    line(125, 75, 125, 95) # Center marker
    
    no_stroke()
    fill(0, 255, 0)
    # The green dot shows where the wind is pushing
    circle(125 + (w_force * 10), 85, 10) 

def key_pressed():
    global is_calibrating
    if key == ' ':
        canvas.begin_draw()
        canvas.no_stroke()
        canvas.fill(random(40, 80), random(160, 255), 40, 220)
        canvas.push_matrix()
        canvas.translate(ivy_pos.x, ivy_pos.y)
        canvas.rotate(random(TWO_PI))
        canvas.ellipse(0, 0, 18, 10)
        canvas.pop_matrix()
        canvas.end_draw()
    if key.lower() == 'c':
        is_calibrating = not is_calibrating
    if key.lower() == 'r':
        canvas.begin_draw()
        canvas.background(0)
        canvas.end_draw()

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