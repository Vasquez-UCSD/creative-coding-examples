def draw():
    background(255)
    if mouse_is_pressed:
        fill(0)
    else:
        fill(200)
    rect_mode(CENTER)
    square(width / 2, height / 2, 200)