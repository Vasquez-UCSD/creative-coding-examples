# Global positions for smooth camera tracking using PVector
cam_eye = PVector(0, 0, 0)

def setup():
    size(1000, 800, P3D)
    global cam_eye
    cam_eye = PVector(0, 300, 500) # Initial camera position

def draw():
    background(15)
    global cam_eye
    
    # 1. Define Terrain and Ball Logic
    grid_size, spacing = 40, 50
    offset = (grid_size * spacing) / 2
    
    # Calculate Ball position (driven by mouse)
    ball_grid_x = map(mouseX, 0, width, 0, grid_size - 1)
    ball_grid_y = map(mouseY, 0, height, 0, grid_size - 1)
    ball_z = noise(ball_grid_x * 0.1, ball_grid_y * 0.1, frameCount * 0.01) * 200
    
    # Use PVector instead of Py5Vector
    ball_world = PVector(
        ball_grid_x * spacing - offset, 
        ball_grid_y * spacing - offset, 
        ball_z
    )

    # 2. Update Follow Camera
    # Camera target relative to the ball
    target_eye = PVector(ball_world.x, ball_world.y + 400, ball_world.z + 200)
    
    # Smoothly move the camera (lerp is a method of PVector)
    # PVector.lerp(target, amount) modifies the vector in-place
    cam_eye.lerp(target_eye, 0.05)
    
    # Apply the Camera: Eye Position, Look-At Position, Up Vector
    # Note: Up Vector is 0, 0, -1 to match your original orientation
    camera(cam_eye.x, cam_eye.y, cam_eye.z, 
           ball_world.x, ball_world.y, ball_world.z, 
           0, 0, -1)

    # 3. Environment Lighting
    pointLight(255, 255, 255, ball_world.x, ball_world.y, ball_world.z + 100)
    ambientLight(50, 50, 50)

    # 4. Draw Terrain
    noFill()
    stroke(100, 100, 255, 150)
    for y in range(grid_size - 1):
        beginShape(TRIANGLE_STRIP)
        for x in range(grid_size):
            z = noise(x * 0.1, y * 0.1, frameCount * 0.01) * 200
            vertex(x * spacing - offset, y * spacing - offset, z)
            z2 = noise(x * 0.1, (y+1) * 0.1, frameCount * 0.01) * 200
            vertex(x * spacing - offset, (y+1) * spacing - offset, z2)
        endShape()

    # 5. Draw the Player Ball
    pushMatrix()
    translate(ball_world.x, ball_world.y, ball_world.z + 20)
    noStroke()
    fill(255, 200, 0)
    sphere(25)
    popMatrix()
