from py5 import *
import config

def draw_eye(x, y, size):
    fill(255), no_stroke()
    circle(x, y, size * 2)
    
    # Map coordinates for iris movement
    off_x = remap(config.current_x, 0, 1200, -size/2, size/2)
    off_y = remap(config.current_y, 0, 800, -size/2, size/2)
    
    push_matrix()
    translate(x + off_x, y + off_y)
    fill(50, 100, 200) # Iris
    circle(0, 0, size)
    fill(0) # Pupil
    p_size = size * (0.1 + (config.pupil_dilation * 0.6))
    circle(0, 0, p_size)
    pop_matrix()
    
    # Eyelids
    if config.blink_progress > 0:
        fill(30)
        lid_h = (size * 1.1) * config.blink_progress
        rect_mode(CORNERS)
        rect(x - size, y - size, x + size, (y - size) + lid_h)
        rect(x - size, y + size, x + size, (y + size) - lid_h)