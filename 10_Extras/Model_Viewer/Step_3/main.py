from ui_elements import draw_axis
from camera_sensor import get_activity
from model_loader import load_asset, draw_asset
import cv2

# Global State
cap = None
prev_gray = None
my_model = None
rot_x, rot_y = 0,0
axis_x, axis_y = 0,0

def setup():
    global cap, my_model
    # CRITIAL: We must add P3D to enable the 3D Engine
    size(1200, 800, P3D)
    
    cap = cv2.VideoCapture(0)
    
    my_model = load_asset("Phone.obj") # <-- Change the name to match your file name

def draw():
    global prev_gray, rot_x, rot_y, axis_x, axis_y
    background(20) # Adjust Background for Contrast
    
    # Lighting for 3D Depth
    lights()
    ambient_light(50, 50, 50)
    
    # Render 3D Model
    # Using Mouse to influence rotation
    draw_asset(my_model, rot_x, rot_y, 50)
    
    # Pass the same rotation variable so the UI label updates
    draw_axis(axis_x, axis_y, rot_x, rot_y)
    
def mouse_dragged():
    global rot_x, rot_y, axis_x, axis_y
    
    # Sensitivity factor for rotation (radius)
    sensitivity = 0.01
    
    # Calc how much the mouse moved since last time
    diff_x = mouse_x - pmouse_x
    diff_y = mouse_y - pmouse_y
    
    # 3D Rotation Logic
    # Moving mouse X rotates around Y axis, moving mouse Y rotates around x axis
    rot_y += diff_x * sensitivity
    rot_x -= diff_y * sensitivity
    
    # 2D Logic
    # Updates the screen position of the top-right axis
    axis_x += diff_x
    axis_y += diff_y