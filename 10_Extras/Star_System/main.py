from py5 import *
from audio_engine import AudioEngine
from star_system import Star
from ui_tools import UITools
from camera_engine import CameraEngine
import time

# --- Global Orchestrators ---
audio = AudioEngine()
cam = CameraEngine()
ui = None  
stars = []
canvas = None
current_model = None
show_model = False

shape_options = ["CIRCLE", "SQUARE", "TRIANGLE", "STAR_POLY", "HEXAGON", "CHAOS"]
current_shape_idx = 0

# --- Scaling Logic ---
scale_target = "OBJ" 
obj_scale = 1.0
shape_scale = 1.0

def settings():
    size(1200, 800, P3D)

def setup():
    window_resizable(True)
    global canvas, ui, stars
    # Primary 3D Canvas
    canvas = create_graphics(1200, 800, P3D)
    ui = UITools(width(), height())
    stars = [Star(canvas.width, canvas.height, i % 60) for i in range(250)]
    color_mode(HSB, 360, 100, 100)

def load_custom_model(selection):
    global current_model, show_model
    if selection is not None:
        try:
            model_path = str(selection)
            current_model = load_shape(model_path)
            show_model = True
            print(f"Model Loaded: {model_path}")
        except Exception as e:
            print(f"Error loading OBJ: {e}")

def draw():
    background(0)
    audio.update_file_analysis()
    cam.update(canvas.width, canvas.height)
    
    # Calculate Keystone Bounding Size for Scaling
    kw = dist(ui.corners[0].x, ui.corners[0].y, ui.corners[1].x, ui.corners[1].y)
    kh = dist(ui.corners[0].x, ui.corners[0].y, ui.corners[3].x, ui.corners[3].y)
    
    # 50% of the smallest dimension * manual obj_scale
    fit_size = min(kw, kh) * 0.5 * obj_scale
    
    canvas.begin_draw()
    # Explicitly clear the P3D depth buffer each frame to prevent ghosting
    canvas.background(0) 
    canvas.color_mode(HSB, 360, 100, 100)
    
    # Trail effect logic
    canvas.push_style()
    canvas.fill(0, 35)
    canvas.rect_mode(CORNER)
    canvas.rect(0, 0, canvas.width, canvas.height)
    canvas.pop_style()
    
    pulse = 1.0 + (audio.spectrum[10] * 0.4)
    current_hitbox = (fit_size * 0.45) * pulse if (current_model and show_model) else 0

    # Physics and Stars Render
    for s in stars:
        if cam.is_active: 
            s.apply_swipe(cam.hand_x, cam.hand_y, cam.vx, cam.vy)
        
        # Only collide if model is active and exists
        if current_model and show_model:
            s.apply_model_collision(canvas.width/2, canvas.height/2, current_hitbox)
            
        s.update(audio.spectrum[s.freq_bin])
        s.draw(canvas, shape_scale)
        
    # Render the 3D obstacle (Static Orientation)
    if current_model is not None and show_model:
        canvas.push_matrix()
        canvas.translate(canvas.width/2, canvas.height/2, 0)
        
        # Scale logic adjusted for typical OBJ units
        canvas.scale(fit_size * 0.1) 
        
        canvas.lights()
        canvas.ambient_light(0, 0, 50)
        canvas.directional_light(0, 0, 100, 0, 0, -1)
        
        canvas.shape(current_model)
        canvas.pop_matrix()
        
    canvas.end_draw()
    
    # Projection Mapping Output
    ui.draw_keystone_surface(canvas)
    ui.draw_masks()
    ui.draw_ui_panel(audio.mode, int(get_frame_rate()), 
                    shape_options[current_shape_idx], 
                    obj_scale, shape_scale, scale_target)

def mouse_pressed():
    global current_shape_idx, obj_scale, shape_scale, scale_target, show_model, current_model, canvas
    action = ui.check_interaction(mouse_x(), mouse_y())
    
    if action == "LOAD":
        select_input("Select an audio file", audio.load_file)
    elif action == "PLAY":
        if audio.audio_data is not None:
            import sounddevice as sd
            sd.stop(); sd.play(audio.audio_data, audio.sample_rate)
            audio.is_playing = True; audio.start_time = time.time()
    elif action == "STOP":
        import sounddevice as sd
        sd.stop(); audio.is_playing = False; audio.mode = "MIC"
    elif action == "SHAPE":
        current_shape_idx = (current_shape_idx + 1) % len(shape_options)
        for s in stars: s.shape_type = shape_options[current_shape_idx]
    
    elif action == "SC_MODE":
        scale_target = "SHAPE" if scale_target == "OBJ" else "OBJ"
        
    elif action == "SIZE_UP":
        if scale_target == "OBJ": obj_scale = min(obj_scale + 0.1, 4.0)
        else: shape_scale = min(shape_scale + 0.2, 5.0)
            
    elif action == "SIZE_DOWN":
        if scale_target == "OBJ": obj_scale = max(obj_scale - 0.1, 0.1)
        else: shape_scale = max(shape_scale - 0.2, 0.2)
            
    elif action == "OBJ":
        select_input("Select an .obj file", load_custom_model)
        
    elif action == "CLEAR":
        print("Hard Clearing GPU Context...")
        show_model = False
        current_model = None
        # Re-creating graphics object wipes the P3D cache
        canvas = create_graphics(1200, 800, P3D)
        print("Scene Reset.")
        
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
    sd.stop(); audio.stream.stop(); audio.stream.close()
    cam.close()

if __name__ == '__main__':
    run_sketch()