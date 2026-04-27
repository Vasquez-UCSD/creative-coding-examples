from py5 import *
import sounddevice as sd
import numpy as np
import soundfile as sf
import time

# --- Audio State ---
rms_volume = 0.0
smoothed_rms = 0.0 
audio_data = None
sample_rate = 44100
is_playing = False
audio_mode = "MIC" 
start_time = 0      
GAIN = 50.0  # <--- INCREASE THIS if bars are too small (e.g., 100, 200)

def audio_callback(indata, frames, time, status):
    global rms_volume
    if audio_mode == "MIC":
        # Calculate RMS and apply basic amplification
        rms_volume = np.sqrt(np.mean(indata**2))

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
    corners = [Py5Vector(100, 100), Py5Vector(1100, 100), 
               Py5Vector(1100, 700), Py5Vector(100, 700)]
    color_mode(HSB, 360, 100, 100)

def on_file_selected(file_path):
    global audio_data, sample_rate, audio_mode
    if file_path:
        audio_data, sample_rate = sf.read(file_path)
        audio_mode = "FILE"

def draw():
    global rms_volume, smoothed_rms, audio_mode, is_playing, start_time, audio_data, sample_rate, canvas, corners, mask_rects, is_mask_enabled, is_calibrating
    background(0)
    
    # DEBUG: Print volume to console to verify audio is working
    # print(f"Raw Volume: {rms_volume:.4f}") 

    if audio_mode == "FILE" and is_playing:
        elapsed = time.time() - start_time
        idx = int(elapsed * sample_rate)
        if idx < len(audio_data) - 1024:
            chunk = audio_data[idx : idx + 1024]
            rms_volume = np.sqrt(np.mean(chunk**2))
        else:
            is_playing = False
            audio_mode = "MIC"

    # Smoothing logic
    smoothed_rms = (0.8 * smoothed_rms) + (0.2 * rms_volume)

    canvas.begin_draw()
    canvas.color_mode(HSB, 360, 100, 100)
    canvas.background(0) 
    
    # --- UPDATED INTENSITY CALCULATION ---
    # We use (smoothed_rms * GAIN) to normalize the signal range
    intensity = (smoothed_rms * GAIN)
    
    num_bars = 60
    bar_width = canvas.width / num_bars
    
    for i in range(num_bars):
        hue_val = remap(i, 0, num_bars, 0, 360)
        h = intensity * canvas.height * (0.5 + 0.5 * sin(i * 0.1))
        h = min(h, canvas.height)
        
        canvas.no_stroke()
        canvas.fill(hue_val, 80, 100)
        canvas.rect(i * bar_width, canvas.height - h, bar_width, h)
    canvas.end_draw()
    
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL)
    vertex(corners[0].x, corners[0].y, 0, 0, 0)
    vertex(corners[1].x, corners[1].y, 0, 1, 0)
    vertex(corners[2].x, corners[2].y, 0, 1, 1)
    vertex(corners[3].x, corners[3].y, 0, 0, 1)
    end_shape()
    
    if is_mask_enabled:
        no_stroke()
        fill(0)
        for m in mask_rects:
            rect(min(m[0].x, m[1].x), min(m[0].y, m[1].y), 
                 abs(m[1].x - m[0].x), abs(m[1].y - m[0].y))
    
    if is_calibrating:
        draw_ui()

def draw_ui():
    global corners, rms_volume, audio_mode
    stroke(255)
    stroke_weight(2)
    fill(80) 
    rect(20, 700, 100, 50) 
    rect(130, 700, 100, 50) 
    rect(240, 700, 100, 50) 
    fill(255)
    text_size(16)
    text("LOAD", 45, 730)
    text("PLAY", 160, 730)
    text("STOP", 270, 730)
    fill(255, 255, 0, 150)
    for p in corners: circle(p.x, p.y, 25)
    text(f"MODE: {audio_mode} | VOL: {rms_volume:.4f}", 20, 680)

def mouse_pressed():
    global selected_idx, is_adding_mask, audio_mode, is_playing, audio_data, sample_rate, start_time, corners, mask_rects
    if 700 < mouse_y < 750:
        if 20 < mouse_x < 120: select_input("Select an audio file", callback=on_file_selected)
        elif 130 < mouse_x < 230: 
            if audio_data is not None:
                sd.stop()
                sd.play(audio_data, sample_rate)
                is_playing = True
                start_time = time.time()
        elif 240 < mouse_x < 340: 
            sd.stop()
            is_playing = False
            audio_mode = "MIC" 
        return 
    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i
            return
    if is_key_pressed and key.lower() == 'n':
        mask_rects.append([Py5Vector(mouse_x, mouse_y), Py5Vector(mouse_x, mouse_y)])
        is_adding_mask = True

def mouse_dragged():
    global selected_idx, is_adding_mask, corners, mask_rects
    if selected_idx != -1: corners[selected_idx] = Py5Vector(mouse_x, mouse_y)
    elif is_adding_mask: mask_rects[-1][1] = Py5Vector(mouse_x, mouse_y)

def mouse_released():
    global selected_idx, is_adding_mask
    selected_idx = -1
    is_adding_mask = False

def key_pressed():
    global is_calibrating, is_mask_enabled, mask_rects
    if key.lower() == 'c': is_calibrating = not is_calibrating
    if key.lower() == 'm': is_mask_enabled = not is_mask_enabled
    if key.lower() == 'x': mask_rects = []

if __name__ == '__main__':
    run_sketch()