import py5
import numpy as np
import config

class Aurora:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.noise_offset = py5.random(1000)

    def draw(self, canvas, frame, smoothed_rms, norm_spec):
        canvas.no_stroke()
        canvas.begin_shape(py5.QUAD_STRIP)
        dom_freq = np.max(norm_spec)
        hue = py5.remap(dom_freq, 0, 1, 160, 240)
        resolution = 20 
        for i in range(resolution):
            x = py5.remap(i, 0, resolution - 1, 0, self.w)
            n = py5.noise(self.noise_offset + (i * 0.1) + (frame * 0.005) + (smoothed_rms * 2.0))
            y_base = py5.remap(n, 0, 1, self.h * 0.2, self.h * 0.5)
            canvas.fill(hue, 80, 100, py5.remap(n, 0, 1, 10, 60))
            canvas.vertex(x, y_base)
            canvas.fill(hue, 90, 80, py5.remap(n, 0, 1, 5, 30))
            canvas.vertex(x, y_base + self.h * 0.4)
        canvas.end_shape()

class Star:
    def __init__(self, w, h, freq_bin):
        self.freq_bin = freq_bin
        self.x = py5.remap(freq_bin, 0, 60, 0, w) + py5.random(-w/20, w/20)
        self.y = py5.random(h * 0.1, h * 0.8)
        # Increased base size for better visibility
        self.size = py5.random(3, 6) 
        self.noise_offset = py5.random(1000)
        self.base_hue = py5.remap(freq_bin, 0, 60, 180, 360)

    def draw(self, canvas, energy, frame):
        flicker = py5.noise(self.noise_offset + frame * 0.05)
        normalized_energy = min(energy * 0.2, 1.0)
        
        # Boosted base brightness to 70
        brightness = py5.remap(normalized_energy, 0, 1, 70, 100) * flicker
        
        canvas.no_stroke()
        # Larger Glow/Bloom
        canvas.fill(self.base_hue, 80, brightness * 0.6, 70)
        canvas.circle(self.x, self.y, self.size * 6)
        
        # Brighter Core
        if normalized_energy > 0.5:
            canvas.fill(self.base_hue, 10, 100, 255)
        else:
            canvas.fill(self.base_hue, 100, brightness, 255)
        canvas.circle(self.x, self.y, self.size + (normalized_energy * 15))