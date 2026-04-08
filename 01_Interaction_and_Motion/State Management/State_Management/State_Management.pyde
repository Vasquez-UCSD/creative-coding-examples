def setup():
    size(400,400)

def draw():
    background(255)
    if mousePressed:
        fill(0)
    else:
        fill(200)
    rectMode(CENTER)
    square(width / 2, height / 2, 200)
