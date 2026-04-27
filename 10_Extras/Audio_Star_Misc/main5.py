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

def audio_callback(indata, frames, time_val, status):
    global spectrum
    if audio_mode == "MIC":
        if indata.ndim > 1:
            mono_data = indata.mean(axis=1)
        else:
            mono_data = indata
        fft_data = np.fft.rfft(mono_data)
        spectrum = np.abs(fft_data)[:60]

stream = sd.InputStream(callback=audio_callback, channels=2)
stream.start()

# --- Star Class: Explosive Particle System ---
class Star:
    def __init__(self, canvas_w, canvas_h, freq_bin):
        self.canvas_w = canvas_w
        self.canvas_h = canvas_h
        self.freq_bin = freq_bin
        self.reset()

    def reset(self):
        # Initial position based on frequency
        x_base = remap(self.freq_bin, 0, 60, 0, self.canvas_w)
        self.x = x_base + random(-30, 30)
        self.y = random(self.canvas_h * 0.2, self.canvas_h * 0.7)
        
        # Physics: Random initial burst direction
        self.vx = random(-1.5, 1.5)
        self.vy = random(-1.5, 1.5)
        self.accel = 1.0
        
        # Appearance
        self.life = 255.0  # Max opacity
        self.base_size = random(2, 5)
        self.current_size = self.base_size
        self.base_hue = remap(self.freq_bin, 0, 60, 180, 320) # Blue to Purple

    def update(self, energy):
        # Explosive trigger: if energy is high, push the particle
        # Scale factor (0.3) adjusts sensitivity
        normalized_energy = energy * 0.3
        
        if normalized_energy > 1.0:
            self.accel = remap(min(normalized_energy, 10), 1, 10, 1.1, 3.0)
            self.current_size = self.base_size + (normalized_energy * 5)
        
        # Move particle
        self.x += self.vx * self.accel
        self.y += self.vy * self.accel
        
        # Drag and Decay
        self.accel *= 0.95 
        self.life -= 1.5   # Fade out speed
        
        # Reset if dead or out of bounds
        if self.life <= 0 or self.x < 0 or self.x > self.canvas_w or self.y < 0 or self.y > self.canvas_h:
            self.reset()

    def draw_star(self, canvas):
        canvas.no_stroke()
        # star_brightness replaced to avoid reserved word 'brightness'
        s_bright = remap(self.accel, 1.0, 3.0, 60, 100) 
        canvas.fill(self.base_hue, 70, s_bright, self.life)
        canvas.circle(self.x, self.y, self.current_size)

# --- Global State ---
mask_rects = []
is_mask_enabled = True
is_adding_mask = False
is_calibrating = True
selected_idx = -1
corners = []
canvas = None
stars = []

def settings():
    size(1200, 800, P3D)

def setup():
    # Set resizable here after surface is ready
    window_resizable(True)
    global canvas, corners, stars
    
    canvas = create_graphics(1200, 800, P3D)
    
    # Create star field
    stars = [Star(canvas.width, canvas.height, i % 60) for i in range(180)]
        
    corners = [
        Py5Vector(width * 0.1, height * 0.1), 
        Py5Vector(width * 0.9, height * 0.1), 
        Py5Vector(width * 0.9, height * 0.8), 
        Py5Vector(width * 0.1, height * 0.8)
    ]
    
    color_mode(HSB, 360, 100, 100)

def on_file_selected(file_path):
    global audio_data, sample_rate, audio_mode
    if file_path:
        audio_data, sample_rate = sf.read(file_path)
        audio_mode = "FILE"

def draw():
    global spectrum, audio_mode, is_playing, start_time, audio_data, sample_rate, canvas, corners, mask_rects, is_mask_enabled, is_calibrating, stars
    background(0)
    
    # Audio Processing
    if audio_mode == "FILE" and is_playing:
        elapsed = time.time() - start_time
        idx = int(elapsed * sample_rate)
        chunk_size = 2048
        if idx < len(audio_data) - chunk_size:
            chunk = audio_data[idx : idx + chunk_size]
            if audio_data.ndim > 1: chunk = chunk.mean(axis=1)
            fft_data = np.fft.rfft(chunk)
            spectrum = np.abs(fft_data)[:60]
        else:
            is_playing = False
            audio_mode = "MIC"

    # Render Stars to Canvas
    canvas.begin_draw()
    canvas.color_mode(HSB, 360, 100, 100)
    canvas.fill(0, 25) # Nebula trail effect
    canvas.rect(0, 0, canvas.width, canvas.height)
    
    for s in stars:
        energy = spectrum[s.freq_bin]
        s.update(energy)
        s.draw_star(canvas)
    canvas.end_draw()
    
    # Keystone Mapping
    begin_shape(QUADS)
    texture(canvas)
    texture_mode(NORMAL)
    vertex(corners[0].x, corners[0].y, 0, 0, 0)
    vertex(corners[1].x, corners[1].y, 0, 1, 0)
    vertex(corners[2].x, corners[2].y, 0, 1, 1)
    vertex(corners[3].x, corners[3].y, 0, 0, 1)
    end_shape()
    
    # Masking & UI
    if is_mask_enabled:
        no_stroke(); fill(0)
        for m in mask_rects:
            rect(min(m[0].x, m[1].x), min(m[0].y, m[1].y), abs(m[1].x - m[0].x), abs(m[1].y - m[0].y))
    
    if is_calibrating:
        draw_ui()

def draw_ui():
    ui_y = height - 100
    stroke(255); stroke_weight(2); fill(40)
    for i in range(4):
        rect(20 + (i * 110), ui_y, 100, 50)
    
    fill(255); text_size(14)
    labels = ["LOAD", "PLAY", "STOP", "EXIT"]
    for i, label in enumerate(labels):
        text(label, 50 + (i * 110), ui_y + 30)
    
    fill(255, 255, 0, 150)
    for p in corners:
        circle(p.x, p.y, 20)
    text(f"MODE: {audio_mode} | FPS: {int(get_frame_rate())}", 20, ui_y - 15)

def mouse_pressed():
    global selected_idx, is_adding_mask, audio_mode, is_playing, start_time
    ui_y = height - 100
    
    if ui_y < mouse_y < ui_y + 50:
        if 20 < mouse_x < 120: select_input("Select File", on_file_selected)
        elif 130 < mouse_x < 230:
            if audio_data is not None:
                sd.stop(); sd.play(audio_data, sample_rate)
                is_playing = True; start_time = time.time()
        elif 240 < mouse_x < 340: sd.stop(); is_playing = False; audio_mode = "MIC"
        elif 350 < mouse_x < 450: exit_sketch()
        return 

    for i, p in enumerate(corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25:
            selected_idx = i; return
            
    if is_key_pressed and key.lower() == 'n':
        mask_rects.append([Py5Vector(mouse_x, mouse_y), Py5Vector(mouse_x, mouse_y)])
        is_adding_mask = True

def mouse_dragged():
    if selected_idx != -1: corners[selected_idx] = Py5Vector(mouse_x, mouse_y)
    elif is_adding_mask: mask_rects[-1][1] = Py5Vector(mouse_x, mouse_y)

def mouse_released():
    global selected_idx, is_adding_mask
    selected_idx = -1; is_adding_mask = False

def key_pressed():
    global is_calibrating, is_mask_enabled, mask_rects
    if key.lower() == 'c': is_calibrating = not is_calibrating
    if key.lower() == 'm': is_mask_enabled = not is_mask_enabled
    if key.lower() == 'x': mask_rects = []

if __name__ == '__main__':
    run_sketch()