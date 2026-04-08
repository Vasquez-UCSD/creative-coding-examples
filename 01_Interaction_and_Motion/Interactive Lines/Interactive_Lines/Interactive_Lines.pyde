def setup():
    size(800, 600)
    background(255)

def draw():
    strokeWeight(2)
    # Connects current mouse to previous mouse position
    line(mouseX, mouseY, pmouseX, pmouseY)
