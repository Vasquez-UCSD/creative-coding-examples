from ui_elements import draw_ui
from camera_sensor import get_activity
from model_loader import load_asset, draw_asset
import cv2


# Global State
current_mode = "ROTATE"
cap = None
prev_gray = None
my_model = None
zoom_level = 1.0 # 1.0 is 100% size

# use global parameters for the size
screen_w, screen_h = 1200, 800

# 3D State
rot_x, rot_y = 0, 0

def setup():
    global cap, my_model
    
    size(screen_w, screen_h, P3D) 
    
    cap = cv2.VideoCapture(0)
    my_model = load_asset("Phone.obj") 

def draw():
    global prev_gray, rot_x, rot_y, zoom_level
    background(15)
    
    # DYNAMIC SCALE CALCULATION
    # We calculate the scale based on the current window height.
    # Adjust the '2.0' (200%) to make it fit tighter or looser.
    responsive_scale = height * 2.0 * zoom_level
    
    # Lights and 3D Rendering
    lights()
    
    # Pass our mouse-controlled rotations to the asset
    draw_asset(my_model, rot_x, rot_y, responsive_scale)
    
    # Draw the FIXED UI
    draw_ui(current_mode, rot_x, rot_y, zoom_level)

def mouse_dragged():
    # This line tells Python to use the variables from the top of the file
    global rot_x, rot_y
    
    sensitivity = 0.01
    diff_x = mouse_x - pmouse_x
    diff_y = mouse_y - pmouse_y
    
    # 3D Rotation Logic
    rot_y += diff_x * sensitivity
    rot_x -= diff_y * sensitivity
    
def mouse_wheel(event):
    global zoom_level
    # event.get_count() returns -1 for scroll up, 1 for scroll down
    # We subtract it to make "Scroll Up" mean "Zoom In"
    zoom_level -= event.get_count() * 0.05
    
    # Constrain the zoom so the model doesn't disappear or get too huge
    zoom_level = constrain(zoom_level, 0.1, 5.0)