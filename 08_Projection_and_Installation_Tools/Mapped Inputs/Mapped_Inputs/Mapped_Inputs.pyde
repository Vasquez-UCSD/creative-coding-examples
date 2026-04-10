def setup():
    size(800, 600)

def draw():
    # 1. VISUALS
    # Processing uses map() instead of remap()
    # mouseX and width are the built-in variables
    w = map(mouseX, 0, width, 10, 200)
    background(255)
    
    stroke(0) # Black line
    strokeWeight(w) # Changed from stroke_weight
    line(100, 300, 700, 300)
    
    # 2. HUD (Heads-Up Display)
    draw_hud(w)

def draw_hud(current_weight):
    # Set text properties
    fill(0) # Black text
    noStroke() # Changed from no_stroke
    textSize(16) # Changed from text_size
    
    # Display Mouse Coordinates
    # Using .format() for compatibility with Processing's Python environment
    text("Mouse X: {}".format(mouseX), 20, 30)
    text("Mouse Y: {}".format(mouseY), 20, 50)
    
    # Display the mapped value
    text("Mapped Weight: {}".format(round(current_weight, 2)), 20, 70)
    
    # Visual indicator: a small dot at the mouse
    fill(255, 0, 0)
    ellipse(mouseX, mouseY, 10, 10) # circle(x, y, d) is also available in newer versions
