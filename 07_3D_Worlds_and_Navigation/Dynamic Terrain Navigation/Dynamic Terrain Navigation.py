def setup():
    size(800, 600, P3D)
    smooth(8)

def draw():
    background(10)
    
    # 1. Setup Camera and Lights
    # Position the camera so we look down at the terrain
    translate(width/2, height/2 + 50, -200)
    rotate_x(radians(60)) # Tilt the view
    lights() # Essential for seeing the 3D sphere shape
    
    # 2. Define Terrain Parameters
    grid_size = 20
    spacing = 40
    offset = (grid_size * spacing) / 2 # Centers the grid at 0,0
    
    # 3. Draw the Terrain
    no_fill()
    stroke(0, 255, 150, 100) # Subtle green wireframe
    
    for y in range(grid_size - 1):
        begin_shape(TRIANGLE_STRIP)
        for x in range(grid_size):
            # Calculate height for current row
            z1 = noise(x * 0.1, y * 0.1, frame_count * 0.01) * 150
            vertex(x * spacing - offset, y * spacing - offset, z1)
            
            # Calculate height for next row (to strip them together)
            z2 = noise(x * 0.1, (y + 1) * 0.1, frame_count * 0.01) * 150
            vertex(x * spacing - offset, (y + 1) * spacing - offset, z2)
        end_shape()
        
    # 4. Logic for the "Surfing" Ball
    # Map mouse input to grid coordinates (0 to grid_size)
    ball_grid_x = remap(mouse_x, 0, width, 0, grid_size - 1)
    ball_grid_y = remap(mouse_y, 0, height, 0, grid_size - 1)
    
    # IMPORTANT: Calculate the ball's Z height using the SAME noise logic
    ball_z = noise(ball_grid_x * 0.1, ball_grid_y * 0.1, frame_count * 0.01) * 150
    
    # Convert grid units back to world pixels
    ball_world_x = ball_grid_x * spacing - offset
    ball_world_y = ball_grid_y * spacing - offset
    
    # 5. Draw the Ball
    push_matrix()
    translate(ball_world_x, ball_world_y, ball_z + 20) # +20 so it sits ON the surface
    no_stroke()
    fill(255, 50, 50) # Hot red ball
    sphere(20) # Ball radius
    pop_matrix()