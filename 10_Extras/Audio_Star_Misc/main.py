from py5 import *
import sounddevice as sd
import numpy as np

# --- Audio State ---
rms_volume = 0.0

def audio_callback(indata, frames, time, status):
    """Callback function to process audio in the background."""
    global rms_volume
    # Calculate Root Mean Square (RMS) for the volume level
    rms_volume = np.sqrt(np.mean(indata**2))

# Start the audio stream
stream = sd.InputStream(callback=audio_callback)
stream.start()

# --- Global State ---
mask_rects = []         
is_mask_enabled = True
is_adding_mask = False  
is_calibrating = True   
selected_idx = -1       
corners = []            
canvas = None           

def setup():
    size(1200, 800, P3D)
    global canvas, corners
    
    canvas = create_graphics(1200, 800, P3D)
    
    # Default corners
    corners = [Py5Vector(100, 100), Py5Vector(1100, 100), 
               Py5Vector(1100, 700), Py5Vector(100, 700)]
    
    color_mode(HSB, 360, 100, 100)

def draw():
    background(0)
    
    # Draw Spectrum to Canvas
    canvas.begin_draw()
    canvas.color_mode(HSB, 360, 100, 100)
    canvas.background(0, 0, 0) 
    
    # Map volume to intensity
    # We multiply by 10 to boost sensitivity; adjust as needed
    intensity = rms_volume * 10 
    
    num_bars = 60
    bar_width = canvas.width / num_bars
    
    for i in range(num_bars):
        hue_val = remap(i, 0, num_bars, 0, 360)
        # Use intensity to grow the bars
        h = intensity * canvas.height * (0.5 + 0.5 * sin(i * 0.1))
        
        canvas.no_stroke()
        canvas.fill(hue_val, 80, 100)
        canvas.rect(i * bar_width, canvas.height - h, bar_width, h)
        
    canvas.end_draw()
    
    # Render Keystone Surface
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL)
    vertex(corners[0].x, corners[0].y, 0, 0, 0)
    vertex(corners[1].x, corners[1].y, 0, 1, 0)
    vertex(corners[2].x, corners[2].y, 0, 1, 1)
    vertex(corners[3].x, corners[3].y, 0, 0, 1)
    end_shape()
    
    # 3. Apply Masking (Blackout)
    if is_mask_enabled:
        no_stroke()
        fill(0) 
        for m in mask_rects:
            x = min(m[0].x, m[1].x)
            y = min(m[0].y, m[1].y)
            w = abs(m[1].x - m[0].x)
            h = abs(m[1].y - m[0].y)
            rect(x, y, w, h)
    
    if is_calibrating:
        draw_calibration_ui()

def draw_calibration_ui():
    no_stroke()
    fill(255, 255, 0, 150)
    for p in corners:
        circle(p.x, p.y, 25)
        
    no_fill()
    stroke(255, 0, 0)
    stroke_weight(2)
    for m in mask_rects:
        rect(min(m[0].x, m[1].x), min(m[0].y, m[1].y), 
             abs(m[1].x - m[0].x), abs(m[1].y - m[0].y))
    
    fill(255)
    text_size(16)
    text(f"VOLUME: {rms_volume:.3f}\nPRESS 'C' TO HIDE UI", 20, 30)

def key_pressed():
    global is_calibrating, is_mask_enabled, mask_rects
    if key.lower() == 'c': is_calibrating = not is_calibrating
    if key.lower() == 'm': is_mask_enabled = not is_mask_enabled
    if key.lower() == 'x': mask_rects = []

def mouse_pressed():
    global selected_idx, is_adding_mask
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i
            return
    if is_key_pressed and key.lower() == 'n':
        mask_rects.append([Py5Vector(mouse_x, mouse_y), Py5Vector(mouse_x, mouse_y)])
        is_adding_mask = True

def mouse_dragged():
    global selected_idx, is_adding_mask
    if selected_idx != -1:
        corners[selected_idx] = Py5Vector(mouse_x, mouse_y)
    elif is_adding_mask:
        mask_rects[-1][1] = Py5Vector(mouse_x, mouse_y)

def mouse_released():
    global selected_idx, is_adding_mask
    selected_idx = -1
    is_adding_mask = False

if __name__ == '__main__':
    run_sketch()