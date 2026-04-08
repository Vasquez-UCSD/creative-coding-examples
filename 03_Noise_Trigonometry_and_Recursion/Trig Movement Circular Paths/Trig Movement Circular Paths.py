angle = 0
def draw():
    global angle
    background(255, 10) # Trail effect
    x = width / 2 + cos(angle) * 100
    y = height / 2 + sin(angle) * 100
    circle(x, y, 20)
    angle += 0.05