from ui_elements import draw_axis
from camera_sensor import get_activity
from audio_sensor import get_noise_level
import cv2

# Global State
cap = None
prev_gray = None
axis_x, axis_y = 0, 0
drag_start_x, drag_start_y = 0, 0

def setup():
    global cap
    size(800, 600)
    cap = cv2.VideoCapture(0)
    background(20)

def draw():
    global prev_gray, axis_x, axis_y
    background(20)
    
    # 1. Get Sensor Data
    activity, prev_gray = get_activity(cap, prev_gray)
    noise_val = get_noise_level(frame_count * 0.05)
    
    # 2. Draw UI Readouts
    fill(255)
    text_size(16)
    text(f"CAMERA_ACTIVITY: {activity}", 20, 40)
    
    # Draw a "Noise Bar"
    fill(255, 200, 0)
    rect(20, 60, noise_val * 2, 20)
    text("NOISE_LEVEL", 20, 100)
    
    # 3. Draw the Interactive Axis
    draw_axis(axis_x, axis_y)

def mouse_dragged():
    global axis_x, axis_y
    # Move the axis based on mouse movement
    axis_x += mouse_x - pmouse_x
    axis_y += mouse_y - pmouse_y

def mouse_pressed():
    # Visual feedback for click
    stroke(255)
    no_fill()
    circle(mouse_x, mouse_y, 40)