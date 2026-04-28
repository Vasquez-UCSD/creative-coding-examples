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

    def draw_ui_panel(self, audio_mode, current_fps, active_shape, obj_sc, shp_sc, target):
        if not self.is_calibrating: return
        
        # Calculate centering
        panel_width = 1020
        start_x = (width() - panel_width) / 2
        ui_y = height() - 100
        
        # Draw Background Panel
        stroke(255); fill(10, 220)
        rect(start_x, ui_y - 45, panel_width, 105, 15) 
        
        labels = ["LOAD", "PLAY", "STOP", "SHAPE", "SC-MODE", "SIZE +", "SIZE -", "OBJ", "CLEAR"]
        for i, label in enumerate(labels):
            btn_x = start_x + 15 + (i * 110)
            
            if label == "SC-MODE":
                fill(100, 100, 255)
            elif label == "CLEAR":
                fill(150, 50, 50)
            else:
                fill(60)
                
            rect(btn_x, ui_y, 100, 50, 5)
            fill(255); text_align(CENTER, CENTER); text_size(10)
            text(label, btn_x + 50, ui_y + 25)
        
        # Center the status text relative to the panel
        text_align(CENTER, BOTTOM); fill(255); text_size(13)
        status_msg = f"AUDIO: {audio_mode} | OBJ: {round(obj_sc, 1)}x | SHAPE: {round(shp_sc, 1)}x | TARGET: {target}"
        text(status_msg, width() / 2, ui_y - 12)
        
        # Keystone corner handles
        fill(255, 255, 0, 180)
        for p in self.corners: circle(p.x, p.y, 20)

    def check_interaction(self, mx, my):
        panel_width = 1020
        start_x = (width() - panel_width) / 2
        ui_y = height() - 100
        
        if ui_y < my < ui_y + 50:
            # Check relative to start_x
            local_x = mx - (start_x + 15)
            btn_index = int(local_x // 110)
            
            if 0 <= btn_index < 9:
                # Ensure the click is actually within a button width (100px), not in the gap
                if local_x % 110 < 100:
                    actions = ["LOAD", "PLAY", "STOP", "SHAPE", "SC_MODE", "SIZE_UP", "SIZE_DOWN", "OBJ", "CLEAR"]
                    return actions[btn_index]
        
        for i, p in enumerate(self.corners):
            if dist(mx, my, p.x, p.y) < 20:
                self.selected_corner_idx = i
                return "CORNER"
        return None

    def update_drag(self, mx, my):
        if self.selected_corner_idx != -1: self.corners[self.selected_corner_idx] = Py5Vector(mx, my)

    def stop_drag(self):
        self.selected_corner_idx = -1