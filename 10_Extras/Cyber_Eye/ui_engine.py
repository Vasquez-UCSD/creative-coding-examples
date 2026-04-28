from py5 import *
import config

def draw_hud():
    no_stroke()
    rect_mode(CORNER)
    
    # Status Indicators
    margin_x = 30
    if config.is_tracking:
        fill(255, 0, 0) # Red for aggressive 'Lock-On'
        text("TARGET ACQUIRED", margin_x, 40)
    else:
        fill(0, 255, 0)
        text(f"EMOTION: {config.current_emotion}", margin_x, 40)
    
    # Tracking Bar
    status_color = color(0, 255, 0) if config.is_tracking else color(255, 0, 0)
    fill(status_color)
    text(f"SYSTEM: {'LOCKED' if config.is_tracking else 'SCANNING'}", margin_x, 70)
    
    # Pupil Dilation Bar
    fill(0, 255, 0)
    text("DILATION:", margin_x, 100)
    no_fill()
    stroke(0, 255, 0)
    rect(140, 85, 100, 15)
    fill(0, 255, 0)
    no_stroke()
    rect(140, 85, config.pupil_dilation * 100, 15)