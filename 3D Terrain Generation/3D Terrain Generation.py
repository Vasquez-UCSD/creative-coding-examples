def setup():
    size(800, 600, P3D)

def draw():
    background(0)
    translate(width/2, height/2, -200)
    rotate_x(PI/3)
    no_fill()
    stroke(0, 255, 100)
    
    for y in range(20):
        begin_shape(TRIANGLE_STRIP)
        for x in range(20):
            # Z height determined by noise
            z = noise(x * 0.1, y * 0.1, frame_count * 0.01) * 150
            vertex(x * 40 - 400, y * 40 - 400, z)
            z2 = noise(x * 0.1, (y+1) * 0.1, frame_count * 0.01) * 150
            vertex(x * 40 - 400, (y+1) * 40 - 400, z2)
        end_shape()