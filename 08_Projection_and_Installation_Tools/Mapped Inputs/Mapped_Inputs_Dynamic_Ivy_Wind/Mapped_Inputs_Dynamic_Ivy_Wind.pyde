# --- Global Configuration ---
canvas = None
corners = [] 
selected_idx = -1
is_calibrating = True
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
    
    # 2. Ivy Start Position using PVector
    ivy_pos = PVector(600, 800)
    
    # 3. Corner Handles using PVector
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
    # noise() and frameCount are built-in
    wind_noise = noise(frameCount * 0.01) 
    wind_force = map(wind_noise, 0, 1, -10, 10) 
    
    mx = constrain(mouseX, 0, width)
    my = constrain(mouseY, 0, height)
    upward_force = map(my, 0, height, 5, 0.2)
    g_channel = map(mx, 0, width, 120, 255)
    
    # --- 2. UPDATE IVY SIMULATION ---
    canvas.beginDraw()
    wiggle = (noise(frameCount * 0.05) - 0.5) * 8
    new_x = ivy_pos.x + wiggle + wind_force
    new_y = ivy_pos.y - random(0, upward_force)
    
    thickness = map(constrain(ivy_pos.y, 0, 800), 0, 800, 0.5, 4)
    canvas.stroke(34, g_channel, 34, 180)
    canvas.strokeWeight(thickness)
    canvas.line(ivy_pos.x, ivy_pos.y, new_x, new_y)
    
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
    
    # --- 4. UI ---
    if is_calibrating:
        draw_ui(wind_force)

def draw_ui(w_force):
    # Draw Draggable Handles
    for i, p in enumerate(corners):
        stroke(255)
        if i == selected_idx:
            fill(255, 0, 0)
        else:
            fill(0, 255, 255, 150)
        ellipse(p.x, p.y, 25, 25)
    
    # HUD Background
    noStroke()
    fill(0, 150)
    rect(15, 15, 450, 110, 10)
    
    # Text Data (Formatted for Jython compatibility)
    fill(255)
    textSize(16)
    text("CALIBRATION MODE", 25, 40)
    text("Current Wind Force: {}".format(round(w_force, 2)), 25, 65)
    text("SPACE: Leaf | C: Hide UI | R: Reset", 25, 110)
    
    # Wind Gauge Visual
    stroke(255, 100)
    line(25, 85, 225, 85) # Base line
    line(125, 75, 125, 95) # Center marker
    
    noStroke()
    fill(0, 255, 0)
    ellipse(125 + (w_force * 10), 85, 10, 10) 

def keyPressed():
    global is_calibrating
    if key == ' ':
        canvas.beginDraw()
        canvas.noStroke()
        canvas.fill(random(40, 80), random(160, 255), 40, 220)
        canvas.pushMatrix()
        canvas.translate(ivy_pos.x, ivy_pos.y)
        canvas.rotate(random(TWO_PI))
        canvas.ellipse(0, 0, 18, 10)
        canvas.popMatrix()
        canvas.endDraw()
    if key == 'c' or key == 'C':
        is_calibrating = not is_calibrating
    if key == 'r' or key == 'R':
        canvas.beginDraw()
        canvas.background(0)
        canvas.endDraw()

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
