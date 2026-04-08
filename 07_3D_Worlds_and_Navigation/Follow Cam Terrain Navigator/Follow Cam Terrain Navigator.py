# Global positions for smooth camera tracking
cam_eye = Py5Vector(0, 0, 0)

def setup():
    size(1000, 800, P3D)
    global cam_eye
    cam_eye = Py5Vector(0, 300, 500) # Initial camera position

def draw():
    background(15)
    global cam_eye
    
    # 1. Define Terrain and Ball Logic
    grid_size, spacing = 40, 50
    offset = (grid_size * spacing) / 2
    
    # Calculate Ball position (driven by mouse)
    ball_grid_x = remap(mouse_x, 0, width, 0, grid_size - 1)
    ball_grid_y = remap(mouse_y, 0, height, 0, grid_size - 1)
    ball_z = noise(ball_grid_x * 0.1, ball_grid_y * 0.1, frame_count * 0.01) * 200
    
    ball_world = Py5Vector(
        ball_grid_x * spacing - offset, 
        ball_grid_y * spacing - offset, 
        ball_z
    )

    # 2. Update Follow Camera
    # We want the camera to be 400 units behind and 200 units above the ball
    target_eye = Py5Vector(ball_world.x, ball_world.y + 400, ball_world.z + 200)
    
    # Smoothly move the camera toward the target (Spring effect)
    cam_eye.lerp(target_eye, 0.05)
    
    # Apply the Camera: Eye Position, Look-At Position, Up Vector
    camera(cam_eye.x, cam_eye.y, cam_eye.z, 
           ball_world.x, ball_world.y, ball_world.z, 
           0, 0, -1)

    # 3. Environment Lighting
    point_light(255, 255, 255, ball_world.x, ball_world.y, ball_world.z + 100)
    ambient_light(50, 50, 50)

    # 4. Draw Terrain
    no_fill()
    stroke(100, 100, 255, 150)
    for y in range(grid_size - 1):
        begin_shape(TRIANGLE_STRIP)
        for x in range(grid_size):
            z = noise(x * 0.1, y * 0.1, frame_count * 0.01) * 200
            vertex(x * spacing - offset, y * spacing - offset, z)
            z2 = noise(x * 0.1, (y+1) * 0.1, frame_count * 0.01) * 200
            vertex(x * spacing - offset, (y+1) * spacing - offset, z2)
        end_shape()

    # 5. Draw the Player Ball
    push_matrix()
    translate(ball_world.x, ball_world.y, ball_world.z + 20)
    no_stroke()
    fill(255, 200, 0)
    sphere(25)
    pop_matrix()