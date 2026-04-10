def setup():
    size(800, 600)

def draw():
    # 1. VISUALS
    # Maps mouse from 0-width to 10-200 stroke weight
    w = remap(mouse_x, 0, width, 10, 200)
    background(255)
    
    stroke(0) # Black line
    stroke_weight(w)
    line(100, 300, 700, 300)
    
    # 2. HUD (Heads-Up Display)
    # We draw this last so it stays on top
    draw_hud(w)

def draw_hud(current_weight):
    # Set text properties
    fill(0) # Black text
    no_stroke() # Don't outline the letters
    text_size(16)
    
    # Display Mouse Coordinates
    # Using f-strings (Python 3) for clean formatting
    text(f"Mouse X: {mouse_x}", 20, 30)
    text(f"Mouse Y: {mouse_y}", 20, 50)
    
    # Display the mapped value
    text(f"Mapped Weight: {round(current_weight, 2)}", 20, 70)
    
    # Visual indicator: a small dot at the mouse
    fill(255, 0, 0)
    circle(mouse_x, mouse_y, 10)