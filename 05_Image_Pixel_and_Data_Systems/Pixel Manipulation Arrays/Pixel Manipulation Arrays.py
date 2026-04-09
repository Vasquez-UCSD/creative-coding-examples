def setup():
    size(400, 400)
    # Lower frame rate makes the static easier to see, 
    # but remove this for "fast" noise.
    frame_rate(90)
def draw():
    load_pixels()
    for i in range(len(pixels)):
        pixels[i] = color(random(255)) # Generates static
    update_pixels()