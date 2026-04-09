def setup():
    size(800, 600, P3D)
    smooth(8)

def draw():
    background(10)
    
    # 1. Setup Camera and Lights
    # Position the camera so we look down at the terrain
    translate(width/2, height/2 + 50, -200)
    rotateX(radians(60)) # Changed from rotate_x
    lights() 
    
    # 2. Define Terrain Parameters
    grid_size = 20
    spacing = 40
    offset = (grid_size * spacing) / 2 
    
    # 3. Draw the Terrain
    noFill()
    stroke(0, 255, 150, 100) 
    
    for y in range(grid_size - 1):
        beginShape(TRIANGLE_STRIP)
        for x in range(grid_size):
            # Calculate height for current row
            # frameCount is the Processing global for frame_count
            z1 = noise(x * 0.1, y * 0.1, frameCount * 0.01) * 150
            vertex(x * spacing - offset, y * spacing - offset, z1)
            
            # Calculate height for next row
            z2 = noise(x * 0.1, (y + 1) * 0.1, frameCount * 0.01) * 150
            vertex(x * spacing - offset, (y + 1) * spacing - offset, z2)
        endShape()
        
    # 4. Logic for the "Surfing" Ball
    # remap() is just map() in Processing
    ball_grid_x = map(mouseX, 0, width, 0, grid_size - 1)
    ball_grid_y = map(mouseY, 0, height, 0, grid_size - 1)
    
    # Calculate the ball's Z height using the SAME noise logic
    ball_z = noise(ball_grid_x * 0.1, ball_grid_y * 0.1, frameCount * 0.01) * 150
    
    # Convert grid units back to world pixels
    ball_world_x = ball_grid_x * spacing - offset
    ball_world_y = ball_grid_y * spacing - offset
    
    # 5. Draw the Ball
    pushMatrix()
    translate(ball_world_x, ball_world_y, ball_z + 20) 
    noStroke()
    fill(255, 50, 50) 
    sphere(20) 
    popMatrix()
