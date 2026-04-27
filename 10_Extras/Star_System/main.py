from py5 import *
from audio_engine import AudioEngine
from star_system import Star
from ui_tools import UITools
from camera_engine import CameraEngine
import time

# --- Orchestrators ---
audio = AudioEngine()
cam = CameraEngine()
ui = None  
stars = []
canvas = None
shape_options = ["CIRCLE", "SQUARE", "TRIANGLE", "STAR_POLY", "HEXAGON", "CHAOS"]
current_shape_idx = 0
global_scale = 1.0

def settings():
    size(1200, 800, P3D)

def setup():
    window_resizable(True)
    global canvas, ui, stars
    canvas = create_graphics(1200, 800, P3D)
    ui = UITools(width(), height())
    stars = [Star(canvas.width, canvas.height, i % 60) for i in range(200)]
    color_mode(HSB, 360, 100, 100)

def draw():
    background(0)
    audio.update_file_analysis()
    
    # Process Hand Tracking
    cam.update(canvas.width, canvas.height)
    
    canvas.begin_draw()
    canvas.color_mode(HSB, 360, 100, 100)
    canvas.rect_mode(CORNER)
    canvas.fill(0, 35); canvas.rect(0, 0, canvas.width, canvas.height)
    
    for s in stars:
        # Check if hand is visible to apply swipe physics
        if cam.is_active:
            s.apply_swipe(cam.hand_x, cam.hand_y, cam.vx, cam.vy)
            
        s.update(audio.spectrum[s.freq_bin])
        s.draw(canvas, global_scale)
        
    # Draw hand feedback indicator on the canvas
    if cam.is_active and ui.is_calibrating:
        canvas.no_stroke(); canvas.fill(0, 100, 100, 150)
        canvas.circle(cam.hand_x, cam.hand_y, 15)
        
    canvas.end_draw()
    
    ui.draw_keystone_surface(canvas)
    ui.draw_masks()
    ui.draw_ui_panel(audio.mode, int(get_frame_rate()), shape_options[current_shape_idx], global_scale)

def mouse_pressed():
    global current_shape_idx, global_scale
    action = ui.check_interaction(mouse_x(), mouse_y())
    
    if action == "LOAD":
        select_input("Select an audio file", audio.load_file)
    elif action == "PLAY":
        if audio.audio_data is not None:
            import sounddevice as sd
            sd.stop()
            sd.play(audio.audio_data, audio.sample_rate)
            audio.is_playing = True; audio.start_time = time.time()
    elif action == "STOP":
        import sounddevice as sd
        sd.stop(); audio.is_playing = False; audio.mode = "MIC"
    elif action == "SHAPE":
        current_shape_idx = (current_shape_idx + 1) % len(shape_options)
        for s in stars: s.shape_type = shape_options[current_shape_idx]
    elif action == "SIZE_UP":
        global_scale = min(global_scale + 0.1, 5.0)
    elif action == "SIZE_DOWN":
        global_scale = max(global_scale - 0.1, 0.1)
    elif action == "EXIT":
        exit_sketch()

def mouse_dragged(): ui.update_drag(mouse_x(), mouse_y())
def mouse_released(): ui.stop_drag()

def key_pressed():
    if key().lower() == 'c': ui.is_calibrating = not ui.is_calibrating
    if key().lower() == 'm': ui.is_mask_enabled = not ui.is_mask_enabled
    if key().lower() == 'x': ui.mask_rects = []

def exiting():
    import sounddevice as sd
    sd.stop()
    audio.stream.stop()
    audio.stream.close()
    cam.close() # Important: turn off webcam

if __name__ == '__main__':
    run_sketch()