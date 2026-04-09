img = None

def setup():
    global img
    size(600, 600)
    # Processing uses loadImage (camelCase)
    # Ensure "Your Image" is inside a folder named 'data' in your sketch folder
    img = loadImage("your image.png or jpg") 

def draw():
    global img
    # If the image failed to load, don't try to draw it
    if img:
        image(img, 0, 0)
    
    # Processing uses mouseX and mouseY (camelCase)
    c = get(mouseX, mouseY) # Sample color under mouse
    
    # Draw the preview square
    stroke(255) # White border so you can see it on dark colors
    fill(c)
    rect(0, 0, 100, 100)
