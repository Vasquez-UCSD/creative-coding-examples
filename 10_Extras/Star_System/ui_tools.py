from py5 import *

class UITools:
    def __init__(self, w, h):
        self.corners = [
            Py5Vector(w * 0.1, h * 0.1), Py5Vector(w * 0.9, h * 0.1), 
            Py5Vector(w * 0.9, h * 0.8), Py5Vector(w * 0.1, h * 0.8)
        ]
        self.mask_rects = []
        self.is_calibrating = True
        self.is_mask_enabled = True
        self.selected_corner_idx = -1
        self.is_adding_mask = False

    def draw_keystone_surface(self, canvas):
        begin_shape(QUADS)
        texture(canvas); texture_mode(NORMAL)
        vertex(self.corners[0].x, self.corners[0].y, 0, 0, 0)
        vertex(self.corners[1].x, self.corners[1].y, 0, 1, 0)
        vertex(self.corners[2].x, self.corners[2].y, 0, 1, 1)
        vertex(self.corners[3].x, self.corners[3].y, 0, 0, 1)
        end_shape()

    def draw_masks(self):
        if self.is_mask_enabled:
            no_stroke(); fill(0)
            for m in self.mask_rects:
                rect(min(m[0].x, m[1].x), min(m[0].y, m[1].y), abs(m[1].x - m[0].x), abs(m[1].y - m[0].y))

    def draw_ui_panel(self, audio_mode, current_fps, active_shape, scale_val):
        if not self.is_calibrating: return
        ui_y = height() - 100
        
        stroke(255); fill(10, 200) # Slightly darker for visibility
        rect(20, ui_y - 45, 800, 105, 10) 
        
        labels = ["LOAD", "PLAY", "STOP", "SHAPE", "SIZE +", "SIZE -", "EXIT"]
        for i, label in enumerate(labels):
            fill(60); rect(30 + (i * 110), ui_y, 100, 50, 5)
            fill(255); text_align(CENTER, CENTER); text_size(11)
            text(label, 80 + (i * 110), ui_y + 25)
        
        text_align(LEFT, BOTTOM); fill(255); text_size(14)
        text(f"MODE: {audio_mode} | SHAPE: {active_shape} | SCALE: {round(scale_val, 1)}x | FPS: {current_fps}", 30, ui_y - 12)
        
        fill(255, 255, 0, 180)
        for p in self.corners: circle(p.x, p.y, 20)

    def check_interaction(self, mx, my):
        ui_y = height() - 100
        if ui_y < my < ui_y + 50:
            if 30 < mx < 130: return "LOAD"
            if 140 < mx < 240: return "PLAY"
            if 250 < mx < 350: return "STOP"
            if 360 < mx < 460: return "SHAPE"
            if 470 < mx < 570: return "SIZE_UP"
            if 580 < mx < 680: return "SIZE_DOWN"
            if 690 < mx < 790: return "EXIT"
        
        for i, p in enumerate(self.corners):
            if dist(mx, my, p.x, p.y) < 20:
                self.selected_corner_idx = i
                return "CORNER"
        
        if is_key_pressed() and key().lower() == 'n':
            self.mask_rects.append([Py5Vector(mx, my), Py5Vector(mx, my)])
            self.is_adding_mask = True
            return "MASK"
        return None

    def update_drag(self, mx, my):
        if self.selected_corner_idx != -1: self.corners[self.selected_corner_idx] = Py5Vector(mx, my)
        elif self.is_adding_mask: self.mask_rects[-1][1] = Py5Vector(mx, my)

    def stop_drag(self):
        self.selected_corner_idx = -1; self.is_adding_mask = False