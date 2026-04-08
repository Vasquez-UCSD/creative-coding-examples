# Simplified Agent: Seeking the mouse
def draw():
    target = Py5Vector(mouse_x, mouse_y)
    desired = target - pos
    desired.set_mag(5)
    # Steering = Desired - Velocity
    # [Logic continues for steering physics]