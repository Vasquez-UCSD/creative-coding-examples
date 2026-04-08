class Particle:
    def __init__(self):
        self.x = random(width)
        self.y = random(height)
    def display(self):
        circle(self.x, self.y, 10)

particles = []

def setup():
    size(400, 400)
    for _ in range(50):
        particles.append(Particle())

def draw():
    for p in particles:
        p.display()