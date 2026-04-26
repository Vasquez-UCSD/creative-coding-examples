# main.py
from ui_elements import draw_ui
from camera_sensor import get_gesture_data
from audio_sensor import get_noise_level
from model_loader import load_asset, draw_asset, get_poly_count
import cv2

# Global State
current_mode = "ROTATE"
cap = None
prev_gray = None
my_model = None
zoom_level = 1.0 
light_pos = [200, -200, 200]
style_override = False

rot_velocity = 0.0
last_motion_x = 320.0 #Start in the middle
friction = 0.95 # 1.0 = infinite spin, 0.9 = stop fast

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
    global rot_velocity, last_motion_x # for continuous motion
    background(15)
    
    # Incorp Mic Noise
    noise_val = get_noise_level(frame_count * 0.01)
    
    # Get Motion
    ret, frame = cap.read()
    if ret:
        motion_x, activity, prev_gray = get_gesture_data(frame, prev_gray)
    
    # Improve Logic - Add Dead Zone
    dead_zone_range = 50
    
    is_intentional = activity > 5000 # Increased from 1000
    is_outside_deadzone = abs(motion_x - 320) > dead_zone_range
    
    # Gesture Velocity Logic
    if current_mode == "ROTATE" and is_intentional and is_outside_deadzone:
        # 3. Lower Sensitivity: Reduce the multiplier from 0.05 to 0.01
        velocity = (motion_x - last_motion_x) * 0.01 
        
        # Smooth the transition: Don't add the full velocity at once
        # This is a basic "Low Pass Filter"
        rot_velocity = (rot_velocity * 0.8) + (velocity * 0.2)
        
        last_motion_x = motion_x
    else:
        # If no motion, slowly decay the velocity even faster to stop "jitter"
        rot_velocity *= 0.9 
        last_motion_x = motion_x
    
    # Apply Momentum and Friction
    rot_y += rot_velocity
    rot_velocity *= friction # Apply Friction to slow down
    
    # Lighting System
    # Example: Pulsing light based on mic input
    light_intensity = noise_val * 2.0
    
    ambient_light(150, 150, 150) # update from (40, 40, 40) to impact with noise
    
    if current_mode == "SPOT":
        spot_light(255, 255, 255, mouse_x, mouse_y, 400, 0, 0, -1, PI/4, 2)
    elif current_mode == "LIGHT":
        point_light(255 * light_intensity, 255 * light_intensity, 255 * light_intensity, light_pos[0], light_pos[1], light_pos[2])
        # Visualize Light
        push_matrix()
        translate(light_pos[0], light_pos[1], light_pos[2])
        emissive(255, 255, 0)
        sphere(5)
        pop_matrix()

    # Render 3D Content
    responsive_scale = height * 2.0 * zoom_level
    draw_asset(my_model, rot_x, rot_y, responsive_scale, style_override)
    
    # Get Count
    count = get_poly_count(my_model)
    
    # Draw HUD
    draw_ui(current_mode, rot_x, rot_y, zoom_level, count, mouse_x, mouse_y, style_override)

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
    global current_mode, style_override
    # Detect Button Clicks (Bottom Left Area)
    if mouse_y > height - 60:
        if 20 < mouse_x < 120: current_mode = "ROTATE"
        elif 130 < mouse_x < 230: current_mode = "LIGHT"
        elif 240 < mouse_x < 340: current_mode = "SPOT"
        elif 350 < mouse_x < 450: style_override = not style_override 
        
def key_pressed():
    global zoom_level
    # Check if the key pressed is "f" or "F"
    if key == 'f' or key == 'F':
        zoom_level = 2.0
        print("View Reset to Fit Screen")