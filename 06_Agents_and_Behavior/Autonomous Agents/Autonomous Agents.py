def setup():
    size(600, 400)
    global pos, vel
    pos = Py5Vector(width / 2, height / 2)
    vel = Py5Vector(0, 0)

def draw():
    background(240)
    global pos, vel
    
    target = Py5Vector(mouse_x, mouse_y)
    desired = target - pos
    
    # Check magnitude using the property
    d_mag = desired.mag
    if d_mag > 0:
        # 1. SET MAGNITUDE: (vector / current_mag) * new_mag
        # This is the manual way to 'set_mag(5)'
        desired = (desired / d_mag) * 5
        
        # 2. STEERING: Steering = Desired - Velocity
        steering = desired - vel
        
        # 3. LIMIT: If steering is stronger than 0.2, scale it down
        s_mag = steering.mag
        if s_mag > 0.2:
            steering = (steering / s_mag) * 0.2
        
        # 4. APPLY PHYSICS
        vel += steering
        pos += vel
    
    fill(50, 150, 255)
    circle(pos.x, pos.y, 20)