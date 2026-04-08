def draw_target(x, y, size):
    fill(255, 0, 0)
    circle(x, y, size)
    fill(255)
    circle(x, y, size * 0.5)

def setup():
    size(800, 600)
    draw_target(200, 200, 100)
    draw_target(400, 300, 200)