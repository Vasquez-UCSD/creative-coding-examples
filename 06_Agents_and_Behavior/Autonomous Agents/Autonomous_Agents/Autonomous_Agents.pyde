def setup():
    size(600, 400)
    global pos, vel
    # In Processing Python, we use PVector
    pos = PVector(width / 2, height / 2)
    vel = PVector(0, 0)

def draw():
    background(240)
    global pos, vel
    
    # mouse_x and mouse_y become mouseX and mouseY
    target = PVector(mouseX, mouseY)
    
    # Calculate desired vector (Target - Position)
    # Using PVector.sub() or vector subtraction
    desired = target - pos
    
    # Check magnitude
    d_mag = desired.mag()
    if d_mag > 0:
        # 1. SET MAGNITUDE: Using the built-in setMag() method
        desired.setMag(5)
        
        # 2. STEERING: Steering = Desired - Velocity
        steering = desired - vel
        
        # 3. LIMIT: Using the built-in limit() method
        steering.limit(0.2)
        
        # 4. APPLY PHYSICS
        vel += steering
        pos += vel
    
    # Draw the object
    fill(50, 150, 255)
    noStroke()
    circle(pos.x, pos.y, 20)
