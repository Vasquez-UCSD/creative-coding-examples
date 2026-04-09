pos = Py5Vector(100, 100)
vel = Py5Vector(2, 5)

def setup():
    size(600, 400) # Define your window size here
    background(240)

def draw():
    global pos, vel
    background(240)
    pos += vel
    if pos.x > width or pos.x < 0:
        vel.x *= -1
    if pos.y > height or pos.y < 0:
        vel.y *= -1
    circle(pos.x, pos.y, 30)