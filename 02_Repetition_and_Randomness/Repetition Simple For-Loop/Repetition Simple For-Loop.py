def setup():
    size(800, 400)
    background(255)
    for i in range(0, width, 40):
        line(i, 0, i, height) # Vertical bars