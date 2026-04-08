img = None
def setup():
    global img
    size(600, 600)
    img = load_image("Snork.png") # Needs to be in 'data' folder

def draw():
    image(img, 0, 0)
    c = get(mouse_x, mouse_y) # Sample color under mouse
    fill(c)
    rect(0, 0, 100, 100)