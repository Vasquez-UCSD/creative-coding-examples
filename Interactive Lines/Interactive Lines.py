def setup():
    size(800, 600)
    background(255)

def draw():
    stroke_weight(2)
    # Connects current mouse to previous mouse position
    line(mouse_x, mouse_y, pmouse_x, pmouse_y)