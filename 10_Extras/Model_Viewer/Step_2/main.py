from ui_elements import draw_axis
from camera_sensor import get_activity
from audio_sensor import get_noise_level
from model_loader import load_asset, draw_asset
import cv2

# Global State
cap = None
prev_gray = None
my_model = None
rot_x, rot_y = 0, 0

def setup():
    global cap, my_model
    # CRITICAL: We must add P3D to enable the 3D engine
    size(1200, 800, P3D) 
    
    cap = cv2.VideoCapture(0)
    
    # Place your .obj file in the same folder as your script
    # Example: my_model = load_asset("cube.obj")
    my_model = load_asset("Phone.obj") #Change this to match the name of your obj file 

def draw():
    global prev_gray, rot_x, rot_y
    background(10) # Darker for 3D depth
    
    # 1. Get Sensor Data
    activity, prev_gray = get_activity(cap, prev_gray)
    
    # 2. Lighting (Essential for 3D depth)
    lights()
    ambient_light(50, 50, 50)
    
    # 3. Render 3D Model
    # We can use 'activity' from the camera to influence rotation!
    rot_y += 0.01 + (activity * 0.00001)
    draw_asset(my_model, rot_x, rot_y, 100)
    
    # 4. Draw 2D UI on top of 3D
    # To draw 2D over 3D, we must disable depth testing temporarily
    hint(DISABLE_DEPTH_TEST)
    camera() # Reset camera to default 2D view
    no_lights()
    
    draw_axis(0, 0) # Your previous UI logic
    
    fill(255)
    text(f"MODEL_ROT_Y: {round(rot_y, 2)}", 20, height - 20)
    hint(ENABLE_DEPTH_TEST)