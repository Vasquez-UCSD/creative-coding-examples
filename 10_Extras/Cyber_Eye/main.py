from py5 import *
import config
import eye_engine
import behavior_engine
import vision_engine
import ui_engine

def setup():
    size(1200, 800)
    
def draw():
    background(30)
    behavior_engine.update_behavior()
    eye_engine.draw_eye(600, 400, 150)
    ui_engine.draw_hud()
    
run_sketch()