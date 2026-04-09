# Initialize variables globally
# PVector is the standard vector class in Processing
pos = PVector(100, 100)
vel = PVector(2, 5)

def setup():
    size(600, 400) # Define your window size here
    background(240)

def draw():
    global pos, vel
    background(240)
    
    # In Processing Python Mode, use .add() instead of +=
    pos.add(vel)
    
    # Check boundaries for the x-axis
    if pos.x > width or pos.x < 0:
        vel.x *= -1
        
    # Check boundaries for the y-axis (added so it doesn't fly off screen)
    if pos.y > height or pos.y < 0:
        vel.y *= -1
        
    # Draw the circle at the vector's position
    fill(100, 150, 250)
    noStroke()
    circle(pos.x, pos.y, 30)
