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
    
    # createGraphics is camelCase in Processing
    canvas = createGraphics(1200, 800, P3D)
    
    # Use PVector instead of Py5Vector
    corners = [PVector(100, 100), PVector(1100, 100), 
               PVector(1100, 700), PVector(100, 700)]

def draw():
    background(0)
    
    # --- 1. Draw Simulation to Canvas ---
    canvas.beginDraw() # beginDraw()
    canvas.background(0) 
    
    canvas.stroke(0, 255, 100)
    canvas.strokeWeight(5) # strokeWeight()
    for i in range(0, canvas.width, 40):
        canvas.line(i, 0, canvas.width - i, canvas.height)
    canvas.endDraw() # endDraw()
    
    # --- 2. Render the Keystone Warped Surface ---
    beginShape(QUADS)
    texture(canvas)
    textureMode(NORMAL)
    vertex(corners[0].x, corners[0].y, 0, 0, 0)
    vertex(corners[1].x, corners[1].y, 0, 1, 0)
    vertex(corners[2].x, corners[2].y, 0, 1, 1)
    vertex(corners[3].x, corners[3].y, 0, 0, 1)
    endShape()
    
    # --- 3. The "True" Masking Layer ---
    if is_mask_enabled:
        noStroke()
        fill(0) 
        for m in mask_rects:
            x = min(m[0].x, m[1].x)
            y = min(m[0].y, m[1].y)
            w = abs(m[1].x - m[0].x)
            h = abs(m[1].y - m[0].y)
            rect(x, y, w, h)
    
    # --- 4. Calibration UI ---
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    noStroke()
    fill(255, 255, 0, 150)
    for p in corners:
        ellipse(p.x, p.y, 25, 25) # ellipse() or circle()
        
    noFill()
    stroke(255, 0, 0)
    strokeWeight(2)
    for m in mask_rects:
        x = min(m[0].x, m[1].x)
        y = min(m[0].y, m[1].y)
        w = abs(m[1].x - m[0].x)
        h = abs(m[1].y - m[0].y)
        rect(x, y, w, h)
    
    fill(255)
    textSize(16)
    
    # Using .format() instead of f-strings for Jython compatibility
    status = "ACTIVE" if is_mask_enabled else "OFF"
    msg = "MASKING: {}\n".format(status)
    msg += "HOLD 'N' + DRAG: Create Mask (Blackout)\n"
    msg += "PRESS 'X': Clear All Masks\n"
    msg += "PRESS 'C': Hide/Show UI for Projection"
    text(msg, 20, 30)

# --- Interaction Logic ---

def keyPressed(): # keyPressed()
    global is_calibrating, is_mask_enabled, mask_rects
    if key == 'c' or key == 'C':
        is_calibrating = not is_calibrating
    if key == 'm' or key == 'M':
        is_mask_enabled = not is_mask_enabled
    if key == 'x' or key == 'X':
        mask_rects = [] 

def mousePressed(): # mousePressed()
    global selected_idx, is_adding_mask
    for i, p in enumerate(corners):
        if dist(mouseX, mouseY, p.x, p.y) < 25:
            selected_idx = i
            return
            
    # keyPressed is a boolean in Processing to check if ANY key is held
    if keyPressed and (key == 'n' or key == 'N'):
        mask_rects.append([PVector(mouseX, mouseY), PVector(mouseX, mouseY)])
        is_adding_mask = True

def mouseDragged(): # mouseDragged()
    if selected_idx != -1:
        corners[selected_idx].x = mouseX
        corners[selected_idx].y = mouseY
    elif is_adding_mask:
        mask_rects[-1][1].x = mouseX
        mask_rects[-1][1].y = mouseY

def mouseReleased(): # mouseReleased()
    global selected_idx, is_adding_mask
    selected_idx = -1
    is_adding_mask = False
