import py5
import config

class Star:
    def __init__(self, w, h, freq_bin):
        self.freq_bin = freq_bin
        self.x = py5.remap(freq_bin, 0, 60, 0, w) + py5.random(-w/20, w/20)
        self.y = py5.random(h * 0.1, h * 0.8)
        self.size = py5.random(2, 4)
        self.noise_offset = py5.random(1000)
        self.base_hue = py5.remap(freq_bin, 0, 60, 200, 360)

    def draw(self, canvas, energy, frame):
        flicker = py5.noise(self.noise_offset + frame * 0.05)
        normalized_energy = min(energy * 0.2, 1.0)
        
        # Increased baseline brightness (min 60) and full saturation (100)
        brightness = py5.remap(normalized_energy, 0, 1, 60, 100) * flicker
        
        canvas.no_stroke()
        
        # 1. BLOOM / GLOW EFFECT
        # Draw a larger, softer circle behind the star
        canvas.fill(self.base_hue, 80, brightness * 0.5, 50)
        canvas.circle(self.x, self.y, self.size * 4)
        
        # 2. CORE STAR
        if normalized_energy > 0.8:
            canvas.fill(self.base_hue, 10, 100, 255) # Intense hot white
        else:
            canvas.fill(self.base_hue, 100, brightness, 255) # Vibrant saturation
            
        canvas.circle(self.x, self.y, self.size + (normalized_energy * 8))