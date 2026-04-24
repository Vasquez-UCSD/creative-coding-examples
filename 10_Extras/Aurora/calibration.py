from py5 import *
import config

def draw_ui():
    stroke(255); stroke_weight(2); fill(80) 
    rect(20, 700, 100, 50); rect(130, 700, 100, 50) 
    rect(240, 700, 100, 50); rect(350, 700, 100, 50)
    fill(255); text_size(16)
    text("LOAD", 45, 730); text("PLAY", 160, 730); text("STOP", 270, 730); text("EXIT", 380, 730)
    fill(255, 255, 0, 150)
    for p in config.corners: circle(p.x, p.y, 25)
    text(f"MODE: {config.audio_mode}", 20, 680)