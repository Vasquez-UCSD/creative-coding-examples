def setup():
    size(800, 800)
    background(0)
    for _ in range(500):
        stroke(random(255), 100, 255)
        point(random(width), random(height))
