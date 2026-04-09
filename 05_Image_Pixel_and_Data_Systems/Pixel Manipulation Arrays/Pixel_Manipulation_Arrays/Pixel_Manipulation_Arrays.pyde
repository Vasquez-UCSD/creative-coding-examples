def setup():
    size(400, 400)
    # Lower frame rate makes the static easier to see, 
    # but remove this for "fast" noise.
    frameRate(30) 

def draw():
    # 1. Load the display window pixels into the pixels[] array
    loadPixels()
    
    # 2. Loop through every pixel
    # len(pixels) is equal to width * height
    for i in range(len(pixels)):
        # Generates a random grayscale value
        pixels[i] = color(random(255))
    
    # 3. Update the display window with the modified array
    updatePixels()
