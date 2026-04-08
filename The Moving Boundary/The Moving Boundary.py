x = 0
speed = 5

def setup():
    size(800, 200)

def draw():
    global x, speed # Required to modify global variables in Python
    background(240)
    x += speed
    if x > width or x < 0:
        speed *= -1 # Reverse direction
    circle(x, height / 2, 50)