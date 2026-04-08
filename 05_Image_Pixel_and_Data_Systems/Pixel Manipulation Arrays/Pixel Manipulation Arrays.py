def draw():
    load_pixels()
    for i in range(len(pixels)):
        pixels[i] = color(random(255)) # Generates static
    update_pixels()