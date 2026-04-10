# --- Global Configuration ---
canvas = None
corners = [] 
selected_idx = -1
is_calibrating = True

# Ivy State Variables
ivy_pos = None 

def setup():
    size(1200, 800, P3D)
    smooth(8)
    
    global canvas, corners, ivy_pos
    
    # 1. Initialize the Virtual Canvas
    canvas = createGraphics(1200, 800, P3D)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    
    # 2. Starting position for the Ivy (Bottom Center)
    # Using PVector for Processing
    ivy_pos = PVector(600, 800)
    
    # 3. Define 4 corners for the projection surface
    corners = [
        PVector(100, 100),                
        PVector(width - 100, 100),        
        PVector(width - 100, height - 100), 
        PVector(100, height - 100)         
    ]

def draw():
    global ivy_pos
    background(0) 
    
    # --- 1. DYNAMIC INPUT MAPPING ---
    mx = constrain(mouseX, 0, width)
    my = constrain(mouseY, 0, height)
    
    # map() replaces remap()
    wind = map(mx, 0, width, -3, 3)
    upward_force = map(my, 0, height, 5, 0.2)
    g_channel = map(mx, 0, width, 120, 255)
    
    # --- 2. UPDATE IVY SIMULATION ---
    canvas.beginDraw()
    
    new_x = ivy_pos.x + random(-4, 4) + wind
    new_y = ivy_pos.y - random(0, upward_force)
    
    thickness = map(ivy_pos.y, 0, 800, 0.5, 4) # Thinner at top
    
    canvas.stroke(34, g_channel, 34, 180)
    canvas.strokeWeight(thickness)
    canvas.line(ivy_pos.x, ivy_pos.y, new_x, new_y)
    
    # Update PVector properties
    ivy_pos.x = new_x
    ivy_pos.y = new_y
    
    # Reset Logic
    if ivy_pos.y < 0 or ivy_pos.x < -100 or ivy_pos.x > 1300:
        ivy_pos.x = random(width)
        ivy_pos.y = height
        
    canvas.endDraw()
    
    # --- 3. RENDER WARPED SURFACE ---
    beginShape(QUADS)
    texture(canvas)
    textureMode(NORMAL)
    
    vertex(corners[0].x, corners[0].y, 0, 0, 0) 
    vertex(corners[1].x, corners[1].y, 0, 1, 0) 
    vertex(corners[2].x, corners[2].y, 0, 1, 1) 
    vertex(corners[3].x, corners[3].y, 0, 0, 1) 
    endShape()
    
    # --- 4. CALIBRATION UI ---
    if is_calibrating:
        draw_ui()

def draw_ui():
    for i, p in enumerate(corners):
        stroke(255)
        if i == selected_idx:
            fill(255, 0, 0)
        else:
            fill(0, 255, 255, 150)
        ellipse(p.x, p.y, 25, 25)
    
    fill(255)
    textSize(16)
    text("CALIBRATION MODE", 25, 40)
    text("- DRAG circles to match your wall corners", 25, 65)
    text("- PRESS 'C' to toggle UI | PRESS 'R' to clear", 25, 85)

# --- Event Handlers (Using camelCase) ---

def mousePressed():
    global selected_idx
    for i, p in enumerate(corners):
        if dist(mouseX, mouseY, p.x, p.y) < 30:
            selected_idx = i
            return

def mouseDragged():
    if selected_idx != -1:
        corners[selected_idx].x = mouseX
        corners[selected_idx].y = mouseY

def mouseReleased():
    global selected_idx
    selected_idx = -1

def keyPressed():
    global is_calibrating
    if key == 'c' or key == 'C':
        is_calibrating = not is_calibrating
    if key == 'r' or key == 'R':
        canvas.beginDraw()
        canvas.background(0)
        canvas.endDraw()
