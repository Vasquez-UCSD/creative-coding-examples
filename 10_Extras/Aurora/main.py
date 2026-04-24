from py5 import *
import config
import audio_engine
import visual_engine
import calibration
import time
import numpy as np
import soundfile as sf
import sounddevice as sd

def on_file_selected(file_path):
    if file_path:
        config.audio_data, config.sample_rate = sf.read(file_path)
        config.audio_mode = "FILE"

def setup():
    size(1200, 800, P3D)
    config.canvas = create_graphics(1200, 800, P3D)
    config.corners = [Py5Vector(100,100), Py5Vector(1100,100), Py5Vector(1100,700), Py5Vector(100,700)]
    config.stars = [visual_engine.Star(1200, 800, i % 60) for i in range(180)]
    config.aurora = visual_engine.Aurora(1200, 800)
    color_mode(HSB, 360, 100, 100)

def draw():
    background(0)
    # Audio Update
    if config.audio_mode == "FILE" and config.is_playing:
        elapsed = time.time() - config.start_time
        idx = int(elapsed * config.sample_rate)
        chunk_size = 2048
        if idx < len(config.audio_data) - chunk_size:
            chunk = config.audio_data[idx:idx+chunk_size].mean(axis=1) if config.audio_data.ndim > 1 else config.audio_data[idx:idx+chunk_size]
            config.spectrum = np.abs(np.fft.rfft(chunk))[:60]
            config.rms_volume = np.sqrt(np.mean(chunk**2))
        else:
            config.is_playing = False; config.audio_mode = "MIC"
    
    config.smoothed_rms = (0.8 * config.smoothed_rms) + (0.2 * config.rms_volume)
    
    # Rendering
    config.canvas.begin_draw()
    config.canvas.background(0, 15)
    config.canvas.color_mode(HSB, 360, 100, 100)
    
    peak = np.max(config.spectrum)
    norm_spec = config.spectrum / peak if peak > 0 else config.spectrum
    
    # Call as functions
    config.aurora.draw(config.canvas, frame_count(), config.smoothed_rms, norm_spec)
    for s in config.stars: s.draw(config.canvas, norm_spec[s.freq_bin], frame_count())
    config.canvas.end_draw()

    # Keystone & Masking
    begin_shape(QUADS); texture(config.canvas); texture_mode(NORMAL)
    for i, p in enumerate(config.corners): vertex(p.x, p.y, 0, *[(0,0), (1,0), (1,1), (0,1)][i])
    end_shape()
    
    if config.is_mask_enabled:
        fill(0); no_stroke()
        for m in config.mask_rects: rect(min(m[0].x, m[1].x), min(m[0].y, m[1].y), abs(m[1].x-m[0].x), abs(m[1].y-m[0].y))
    
    if config.is_calibrating: calibration.draw_ui()

def mouse_pressed():
    if 700 < mouse_y < 750:
        if 20 < mouse_x < 120: select_input("Load File", callback=on_file_selected)
        elif 130 < mouse_x < 230: 
            sd.stop(); sd.play(config.audio_data, config.sample_rate); config.is_playing = True; config.start_time = time.time()
        elif 240 < mouse_x < 340: sd.stop(); config.is_playing = False; config.audio_mode = "MIC"
        elif 350 < mouse_x < 450: exit_sketch()
    for i, p in enumerate(config.corners):
        if dist(mouse_x, mouse_y, p.x, p.y) < 25: config.selected_idx = i; return
    if is_key_pressed and key.lower() == 'n':
        config.mask_rects.append([Py5Vector(mouse_x, mouse_y), Py5Vector(mouse_x, mouse_y)])
        config.is_adding_mask = True

def mouse_dragged():
    if config.selected_idx != -1: config.corners[config.selected_idx] = Py5Vector(mouse_x, mouse_y)
    elif config.is_adding_mask: config.mask_rects[-1][1] = Py5Vector(mouse_x, mouse_y)

def mouse_released():
    config.selected_idx = -1; config.is_adding_mask = False

def key_pressed():
    if key.lower() == 'c': config.is_calibrating = not config.is_calibrating
    if key.lower() == 'm': config.is_mask_enabled = not config.is_mask_enabled
    if key.lower() == 'x': config.mask_rects = []

if __name__ == "__main__":
    run_sketch()