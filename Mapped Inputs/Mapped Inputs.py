def draw():
    # Maps mouse from 0-width to 10-200 stroke weight
    w = remap(mouse_x, 0, width, 10, 200)
    background(255)
    stroke_weight(w)
    line(100, 300, 700, 300)