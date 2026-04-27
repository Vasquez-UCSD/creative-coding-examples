from py5 import *
import sounddevice as sd
import numpy as np
import soundfile as sf
import time

# --- Audio State ---
spectrum = np.zeros(60) 
audio_data = None
sample_rate = 44100
is_playing = False
audio_mode = "MIC" 
start_time = 0      

def audio_callback(indata, frames, time, status):
    global spectrum
    if audio_mode == "MIC":
        mono_data = indata.mean(axis=1) if indata.ndim > 1 else indata
        fft_data = np.fft.rfft(mono_data)
        spectrum = np.abs(fft_data)[:60]

stream = sd.InputStream(callback=audio_callback, channels=2)
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
    global spectrum, audio_mode, is_playing, start_time, audio_data, sample_rate, canvas, corners, mask_rects, is_mask_enabled, is_calibrating
    background(0)
    
    if audio_mode == "FILE" and is_playing:
        elapsed = time.time() - start_time
        idx = int(elapsed * sample_rate)
        if idx < len(audio_data) - 2048:
            chunk = audio_data[idx : idx + 2048].mean(axis=1) if audio_data.ndim > 1 else audio_data[idx:idx+2048]
            fft_data = np.fft.rfft(chunk)
            spectrum = np.abs(fft_data[:60])
        else:
            is_playing = False
            audio_mode = "MIC"

    canvas.begin_draw()
    canvas.color_mode(HSB, 360, 100, 100)
    canvas.background(0) 
    
    # Normalize spectrum
    peak = np.max(spectrum)
    normalized_spectrum = spectrum / peak if peak > 0 else spectrum
    
    num_bars = len(normalized_spectrum)
    bar_width = canvas.width / num_bars
    
    for i in range(num_bars):
        hue_val = remap(i, 0, num_bars, 0, 360)
        h = normalized_spectrum[i] * (canvas.height * 0.9)
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
    global corners, audio_mode
    stroke(255); stroke_weight(2); fill(80) 
    # Buttons: Load, Play, Stop, Exit
    rect(20, 700, 100, 50); rect(130, 700, 100, 50); rect(240, 700, 100, 50); rect(350, 700, 100, 50)
    fill(255); text_size(16)
    text("LOAD", 45, 730); text("PLAY", 160, 730); text("STOP", 270, 730); text("EXIT", 380, 730)
    fill(255, 255, 0, 150)
    for p in corners: circle(p.x, p.y, 25)
    text(f"MODE: {audio_mode}", 20, 680)

def mouse_pressed():
    global selected_idx, is_adding_mask, audio_mode, is_playing, audio_data, sample_rate, start_time, corners, mask_rects
    
    # Button Detection
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
        elif 350 < mouse_x < 450: # EXIT
            exit_sketch() # Gracefully close the window
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