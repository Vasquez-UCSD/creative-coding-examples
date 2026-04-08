def setup():
    size(600, 600)
    no_stroke()

def draw():
    background(20)
    fill(255, 0, 100)
    circle(300, 300, 400)
    fill(255)
    circle(mouse_x, mouse_y, 50) # Contrast through scale and color