# main.py
from ui_elements import draw_ui
from camera_sensor import get_activity
from model_loader import load_asset, draw_asset
import cv2

# Global State
current_mode = "ROTATE"
cap = None
prev_gray = None
my_model = None
zoom_level = 1.0 
light_pos = [200, -200, 200]

# 3D State
rot_x, rot_y = 0, 0
screen_w, screen_h = 1200, 800

def setup():
    global cap, my_model
    size(screen_w, screen_h, P3D) 
    cap = cv2.VideoCapture(0)
    my_model = load_asset("Phone.obj") 

def draw():
    global prev_gray, rot_x, rot_y, zoom_level, current_mode
    background(15)
    
    # Get OpenCV Frame and Gesture Data
    ret, frame = cap.read()
    if ret:
        motion_x, activity, prev_gray = get_activity(frame, prev_gray)
        
        # Gesture Rotation Logic (Only in ROTATE mode)
        if current_mode == "ROTATE" and activity > 3000:
            gesture_offset = (motion_x - 320) / 320.0
            rot_y += gesture_offset * 0.05
    
    # Lighting System
    ambient_light(200, 200, 200)
    if current_mode == "SPOT":
        spot_light(255, 255, 255, mouse_x, mouse_y, 400, 0, 0, -1, PI/4, 2)
    elif current_mode == "LIGHT":
        point_light(255, 255, 255, light_pos[0], light_pos[1], light_pos[2])
        # Visualize Light
        push_matrix()
        translate(light_pos[0], light_pos[1], light_pos[2])
        emissive(255, 255, 0)
        sphere(5)
        pop_matrix()

    # Render 3D Content
    responsive_scale = height * 2.0 * zoom_level
    draw_asset(my_model, rot_x, rot_y, responsive_scale)
    
    # Draw HUD
    draw_ui(current_mode, rot_x, rot_y, zoom_level)

def mouse_dragged():
    global rot_x, rot_y, light_pos
    sensitivity = 0.01
    dx = mouse_x - pmouse_x
    dy = mouse_y - pmouse_y
    
    if current_mode == "ROTATE":
        rot_y += dx * sensitivity
        rot_x -= dy * sensitivity
    elif current_mode == "LIGHT":
        light_pos[0] += dx
        light_pos[1] += dy

def mouse_wheel(event):
    global zoom_level
    zoom_level -= event.get_count() * 0.05
    zoom_level = constrain(zoom_level, 0.1, 5.0)

def mouse_pressed():
    global current_mode
    # Detect Button Clicks (Bottom Left Area)
    if mouse_y > height - 60:
        if 20 < mouse_x < 120: current_mode = "ROTATE"
        elif 130 < mouse_x < 230: current_mode = "LIGHT"
        elif 240 < mouse_x < 340: current_mode = "SPOT"
        
def key_pressed():
    global zoom_level
    # Check if the key pressed is "f" or "F"
    if key == 'f' or key == 'F':
        zoom_level = 2.0
        print("View Reset to Fit Screen")