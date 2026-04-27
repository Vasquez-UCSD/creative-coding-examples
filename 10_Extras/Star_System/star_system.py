from py5 import *

class Star:
    def __init__(self, canvas_w, canvas_h, freq_bin):
        self.canvas_w = canvas_w
        self.canvas_h = canvas_h
        self.freq_bin = freq_bin
        self.shape_type = "CIRCLE"
        self.chaos_shape = "CIRCLE" 
        self.reset()

    def reset(self):
        self.x = random(self.canvas_w)
        self.y = random(self.canvas_h)
        self.vx = random(-1.2, 1.2)
        self.vy = random(-1.2, 1.2)
        self.accel = 1.0
        self.life = 255.0
        self.base_size = random(2, 5)
        self.current_size = self.base_size
        self.base_hue = remap(self.freq_bin, 0, 60, 180, 320)
        self.chaos_shape = random_choice(["CIRCLE", "SQUARE", "TRIANGLE", "STAR_POLY", "HEXAGON"])

    def apply_swipe(self, hx, hy, hvx, hvy):
        """Calculates distance to hand and adds a velocity kick based on hand movement."""
        d = dist(self.x, self.y, hx, hy)
        # Interaction radius: 180 pixels
        if d < 180:
            # Strength falls off as distance increases
            strength = remap(min(d, 180), 0, 180, 2.0, 0)
            # Apply a fraction of the hand's movement to the star's velocity
            self.vx += hvx * strength * 0.08
            self.vy += hvy * strength * 0.08

    def update(self, energy):
        normalized_energy = energy * 0.3
        if normalized_energy > 1.0:
            self.accel = remap(min(normalized_energy, 10), 1, 10, 1.1, 3.0)
            self.current_size = self.base_size + (normalized_energy * 5)
        
        # Physics update
        self.x += self.vx * self.accel
        self.y += self.vy * self.accel
        
        # Friction: slowly return to normal speeds
        self.vx *= 0.96
        self.vy *= 0.96
        self.accel *= 0.95 
        
        self.life -= 2.5 
        
        if self.life <= 0 or self.x < 0 or self.x > self.canvas_w or self.y < 0 or self.y > self.canvas_h:
            self.reset()

    def draw_ngon(self, canvas, x, y, r, n):
        canvas.begin_shape()
        angle = TWO_PI / n
        for i in range(n):
            px = x + cos(i * angle) * r
            py = y + sin(i * angle) * r
            canvas.vertex(px, py)
        canvas.end_shape(CLOSE)

    def draw_star_poly(self, canvas, x, y, r, n):
        angle = TWO_PI / n
        half_angle = angle / 2.0
        canvas.begin_shape()
        for i in range(n):
            canvas.vertex(x + cos(i * angle) * r, y + sin(i * angle) * r)
            canvas.vertex(x + cos(i * angle + half_angle) * (r * 0.4), y + sin(i * angle + half_angle) * (r * 0.4))
        canvas.end_shape(CLOSE)

    def draw(self, canvas, global_scale):
        canvas.push_style()
        canvas.no_stroke()
        s_bright = remap(self.accel, 1.0, 3.0, 60, 100) 
        sz = self.current_size * global_scale
        
        active_shape = self.chaos_shape if self.shape_type == "CHAOS" else self.shape_type
        canvas.fill(self.base_hue, 70, s_bright, self.life)

        if active_shape == "CIRCLE":
            canvas.circle(self.x, self.y, sz)
        elif active_shape == "SQUARE":
            canvas.rect_mode(CENTER); canvas.square(self.x, self.y, sz)
        elif active_shape == "TRIANGLE":
            self.draw_ngon(canvas, self.x, self.y, sz, 3)
        elif active_shape == "STAR_POLY":
            self.draw_star_poly(canvas, self.x, self.y, sz, 5)
        elif active_shape == "HEXAGON":
            self.draw_ngon(canvas, self.x, self.y, sz, 6)
            
        canvas.pop_style()