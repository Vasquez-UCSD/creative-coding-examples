t = 0
def draw():
    global t
    background(255)
    n = noise(t) * width # Smooth, correlated 'random'
    circle(n, height / 2, 50)
    t += 0.01
