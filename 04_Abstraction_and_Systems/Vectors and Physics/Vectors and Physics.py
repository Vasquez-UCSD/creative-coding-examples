pos = Py5Vector(100, 100)
vel = Py5Vector(2, 5)

def draw():
    global pos
    background(240)
    pos += vel
    if pos.x > width or pos.x < 0: vel.x *= -1
    circle(pos.x, pos.y, 30)