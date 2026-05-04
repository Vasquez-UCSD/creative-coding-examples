from py5 import *
import config

class Star:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.reset()

    def reset(self):
        self.x = random(self.w)
        self.y = random(self.h)
        self.size = random(2, 6)
        self.hue = random(180, 280) # Blues and purples
        
    def update(self):
        if config.is_mask_active and config.silhouette_mask is not None:
            ix, iy = int(self.x), int(self.y)
            # Boundary check
            if 0 <= ix < self.w and 0 <= iy < self.h:
                # If the mask is black (0), the star is outside the fabric
                if config.silhouette_mask[iy, ix] < 127:
                    self.reset() 

    def draw_to_buffer(self, pg):
        pg.no_stroke()
        pg.fill(self.hue, 80, 100, 200)
        pg.circle(self.x, self.y, self.size)