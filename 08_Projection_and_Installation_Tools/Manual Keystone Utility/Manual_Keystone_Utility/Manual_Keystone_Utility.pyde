# --- Global Calibration Data ---
canvas = None
corners = [] # List of PVectors
selected_idx = -1
is_calibrating = True

# Ivy Variables
ivy_x, ivy_y = 600, 800 # Start at bottom center

def setup():
    size(1200, 800, P3D)
    global canvas, corners
    
    # 1. Create the 'Virtual' ivy wall
    # createGraphics is camelCase in Processing
    canvas = createGraphics(1200, 800, P3D)
    canvas.beginDraw()
    canvas.background(0) # Initialize with black once
    canvas.endDraw()
    
    # 2. Define 4 corners for warping using PVector
    corners = [
        PVector(100, 100),
        PVector(width - 100, 100),
        PVector(width - 100, height - 100),
        PVector(100, height - 100)
    ]

def draw():
    global ivy_x, ivy_y
    background(0) 
    
    # --- 1. Update Simulation on the Canvas ---
    canvas.beginDraw()
    
    # Ivy Growth Logic
    canvas.stroke(34, 139, 34, 150) # Forest Green
    canvas.strokeWeight(2)          # Changed from stroke_weight
    
    # Wiggle movement
    new_x = ivy_x + random(-5, 5)
    new_y = ivy_y - random(1, 4)    # Move upwards
    
    # Draw the growth segment directly to the PGraphics object
    canvas.line(ivy_x, ivy_y, new_x, new_y)
    
    # Update position
    ivy_x, ivy_y = new_x, new_y
    
    # Reset ivy if it goes off screen
    if ivy_y < 0:
        ivy_y = height
        ivy_x = random(width)
        
    canvas.endDraw()
    
    # --- 2. Render the Warped Surface ---
    beginShape(QUADS)
    texture(canvas)
    textureMode(NORMAL) 
    
    # vertex(x, y, z, u, v)
    vertex(corners[0].x, corners[0].y, 0, 0, 0) 
    vertex(corners[1].x, corners[1].y, 0, 1, 0) 
    vertex(corners[2].x, corners[2].y, 0, 1, 1) 
    vertex(corners[3].x, corners[3].y, 0, 0, 1) 
    endShape()
    
    # --- 3. UI ---
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    noStroke()
    for i, p in enumerate(corners):
        if i == selected_idx: 
            fill(255, 0, 0)
        else: 
            fill(0, 255, 255, 150)
        ellipse(p.x, p.y, 20, 20)
    
    fill(255)
    text("DRAG CORNERS. Press 'C' to toggle UI. Press 'R' to reset Ivy.", 20, 30)

# --- Interaction Handlers ---

def mousePressed():
    global selected_idx
    for i, p in enumerate(corners):
        if dist(mouseX, mouseY, p.x, p.y) < 25:
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
    if key == 'r' or key == 'R': # Clear the ivy
        canvas.beginDraw()
        canvas.background(0)
        canvas.endDraw()
