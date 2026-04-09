def setup():
    # P3D enables the 3D renderer
    size(800, 600, P3D)

def draw():
    background(0)
    
    # Move to the center and tilt the view
    translate(width/2, height/2, -200)
    rotateX(PI/3) # Changed from rotate_x
    
    noFill()
    stroke(0, 255, 100)
    
    # Mesh generation
    for y in range(20):
        beginShape(TRIANGLE_STRIP) # Changed from begin_shape
        for x in range(20):
            # Calculate Perlin noise for the current row
            # frameCount (changed from frame_count) provides the animation
            z = noise(x * 0.1, y * 0.1, frameCount * 0.01) * 150
            vertex(x * 40 - 400, y * 40 - 400, z)
            
            # Calculate Perlin noise for the next row to bridge the strip
            z2 = noise(x * 0.1, (y + 1) * 0.1, frameCount * 0.01) * 150
            vertex(x * 40 - 400, (y + 1) * 40 - 400, z2)
        endShape() # Changed from end_shape
