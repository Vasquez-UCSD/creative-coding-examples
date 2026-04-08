def setup():
    size(600, 600)
    for x in range(0, width, 50):
        for y in range(0, height, 50):
            fill(random(255))
            rect(x, y, 45, 45)