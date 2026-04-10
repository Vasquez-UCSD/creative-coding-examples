import cv2
import sounddevice as sd
import numpy as np
from pathlib import Path 

# --- Global Sensors & State ---
mic_vol = 0
room_brightness = 0
motion_level = 0
ivy_list = []
cap = cv2.VideoCapture(0)
prev_frame = None
stream = None

# --- Mesh & HUD Globals ---
cam_zoom = 1800
cam_target_y = -600
use_obj = False
loaded_mesh = None
mesh_points = [] 
max_model_y = 0 

# --- Ivy Logic ---
class IvyStrand:
    def __init__(self, base_x, base_y, base_z, radius, id_seed, hue_off=0):
        self.segments = [Py5Vector(base_x, base_y, base_z)]
        self.radius = radius
        self.max_segments = random(350, 550) 
        self.current_length = 10 
        self.id_seed = id_seed 
        self.hue_offset = hue_off + random(-20, 20)
        self.current_angle = atan2(base_z, base_x)
        self.has_branched = False
        self.is_climbing = False 
        self.is_bridging = False 
        self.search_dir = -1 # -1 Up, 1 Down

    def update(self):
        global room_brightness, ivy_list, use_obj, mesh_points, max_model_y
        growth_step = remap(room_brightness, 0, 1, -0.4, 0.8)
        self.current_length = constrain(self.current_length + growth_step, 2, self.max_segments)
        
        if len(self.segments) < int(self.current_length):
            last = self.segments[-1]
            dist_to_center = dist(last.x, last.z, 0, 0)
            
            if dist_to_center <= self.radius + 25:
                self.is_climbing = True

            if not self.is_climbing:
                # GROUND CRAWL
                dir_to_center = (Py5Vector(0, 0, 0) - Py5Vector(last.x, 0, last.z)).normalize()
                wander = Py5Vector(noise(len(self.segments)*0.1, self.id_seed)-0.5, 0, noise(len(self.segments)*0.1, self.id_seed+100)-0.5)
                self.segments.append(last + (dir_to_center + wander * 0.4).normalize() * 12)
            
            elif use_obj and len(mesh_points) > 0:
                # --- IMMEDIATE SURFACE SENSING ---
                best_dist = 140 if self.is_bridging else 110
                best_pt = None
                
                # Force descent if we've passed the top of the model
                if last.y < max_model_y: self.search_dir = 1 

                for _ in range(130): 
                    p = random_choice(mesh_points)
                    d = dist(last.x, last.y, last.z, p.x, p.y, p.z)
                    is_correct_y = (p.y < last.y) if self.search_dir == -1 else (p.y > last.y)
                    
                    if is_correct_y and d < best_dist:
                        best_dist = d
                        best_pt = p
                
                if best_pt:
                    self.is_bridging = False
                    self.search_dir = -1 
                    # Magnetic snap to surface
                    new_pos = last.lerp(best_pt, 0.35)
                    surface_push = (Py5Vector(new_pos.x, 0, new_pos.z)).normalize() * 3
                    self.segments.append(new_pos + surface_push)
                else:
                    # NO SURFACE: Immediate downward search
                    self.is_bridging = True
                    self.search_dir = 1 
                    
                    if last.y >= -5:
                        self.is_climbing = False
                        self.search_dir = -1
                    
                    # Dropping spiral
                    rad_osc = (10 + noise(frame_count*0.1, self.id_seed)*15) * sin(len(self.segments) * 0.15)
                    search_x = sin(len(self.segments)*0.3 + self.id_seed) * rad_osc
                    search_z = cos(len(self.segments)*0.3 + self.id_seed) * rad_osc
                    self.segments.append(last + Py5Vector(search_x, 18, search_z))
            
            else:
                # PILLAR MODE
                step = len(self.segments)
                self.current_angle += (noise(step * 0.05, self.id_seed) - 0.5) * 0.3
                new_x = (self.radius+8) * cos(self.current_angle)
                new_z = (self.radius+8) * sin(self.current_angle)
                new_y = last.y - remap(step, 0, self.max_segments, 14, 7)
                self.segments.append(Py5Vector(new_x, new_y, new_z))
            
            # Branching Logic
            if len(self.segments) > 85 and not self.has_branched and random(1) < 0.06:
                if len(ivy_list) < 110: 
                    child = IvyStrand(self.segments[-1].x, self.segments[-1].y, self.segments[-1].z, 
                                     self.radius, random(9999), self.hue_offset)
                    child.is_climbing = self.is_climbing
                    ivy_list.append(child)
                    self.has_branched = True

    def display(self):
        global mic_vol, motion_level
        color_mode(HSB, 360, 100, 100)
        sway = sin(frame_count * 0.1) * (motion_level * 120)
        
        for i in range(len(self.segments) - 1):
            v1, v2 = self.segments[i], self.segments[i+1]
            age = i / float(len(self.segments))
            current_hue = (self.hue_offset + remap(mic_vol, 0, 0.3, 120, 310)) % 360
            
            wt = 1.0 if self.is_bridging else remap(age, 0, 1, 9, 1.5)
            sat = 15 if self.is_bridging else 85 # Ghostly when bridging
            
            stroke_weight(wt)
            stroke(current_hue, sat, remap(age, 0, 1, 35, 100), 160)
            
            s_mult = age if (self.is_climbing and not self.is_bridging) else 0
            line(v1.x + sway*s_mult, v1.y, v1.z, v2.x + sway*s_mult, v2.y, v2.z)
            
            if i % 16 == 0:
                push_matrix()
                translate(v1.x + sway*s_mult, v1.y, v1.z)
                if self.is_climbing: rotate_y(atan2(v1.x, v1.z))
                else: rotate_x(HALF_PI)
                fill(current_hue, sat-5, 95, 120)
                no_stroke()
                l_size = (14 * (1-age) + (mic_vol * 130)) * (0.8 + noise(i, self.id_seed) * 0.4)
                if self.is_bridging: l_size *= 0.2 
                ellipse(0, 0, l_size, l_size * 0.6)
                pop_matrix()
        color_mode(RGB, 255)

# --- Mesh & IO Helpers ---
def file_selected(selection):
    global loaded_mesh, use_obj, mesh_points, ivy_list, cam_target_y, max_model_y
    if selection is not None:
        path_str = str(selection) 
        if path_str.lower().endswith(".obj"):
            try:
                loaded_mesh = load_shape(path_str)
                mesh_points = []
                min_y, max_y = 0, 0
                def extract_verts(sh):
                    nonlocal min_y, max_y
                    for j in range(sh.get_vertex_count()):
                        v = sh.get_vertex(j); mesh_points.append(v)
                        if v.y < min_y: min_y = v.y 
                        if v.y > max_y: max_y = v.y
                    for k in range(sh.get_child_count()): extract_verts(sh.get_child(k))
                extract_verts(loaded_mesh)
                cam_target_y = (min_y + max_y) / 2
                max_model_y = min_y 
                use_obj = True
                reset_ivy()
            except Exception as e: print(f"Error loading OBJ: {e}")

def reset_ivy():
    global ivy_list
    ivy_list = []
    for i in range(15):
        a = random(TWO_PI); d = random(400, 800)
        ivy_list.append(IvyStrand(cos(a)*d, 0, sin(a)*d, 120, i*137, 120))

def key_pressed():
    global cam_zoom, cam_target_y, use_obj
    if key == 'f' or key == 'F':
        if use_obj and len(mesh_points) > 0:
            ys = [p.y for p in mesh_points]; h = abs(max(ys) - min(ys))
            cam_zoom = h * 2.3 
        else: cam_zoom = 1800; cam_target_y = -1000

def mouse_pressed():
    if 25 < mouse_x < 325 and 140 < mouse_y < 195: 
        select_input("Select an OBJ file:", file_selected)

def mouse_wheel(event):
    global cam_zoom
    cam_zoom = constrain(cam_zoom + event.get_count() * 100, 100, 9500)

def audio_callback(indata, frames, time, status):
    global mic_vol
    mic_vol = np.linalg.norm(indata) * 0.1

def setup():
    size(1200, 900, P3D)
    global stream
    random_seed(42); noise_seed(42)
    try:
        stream = sd.InputStream(callback=audio_callback); stream.start()
    except: print("Mic Error")
    reset_ivy()

def draw():
    background(8)
    global cap, prev_frame, room_brightness, motion_level, cam_zoom, cam_target_y, use_obj, loaded_mesh
    
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(cv2.resize(frame, (160, 120)), cv2.COLOR_BGR2GRAY)
        room_brightness = np.mean(gray) / 255.0
        if prev_frame is not None:
            motion_level = np.mean(cv2.absdiff(prev_frame, gray)) / 255.0
        prev_frame = gray

    hint(ENABLE_DEPTH_TEST)
    camera(0, cam_target_y, cam_zoom, 0, cam_target_y, 0, 0, 1, 0)
    rotate_y(remap(mouse_x, 0, width, -PI, PI))
    
    ambient_light(80, 80, 100)
    directional_light(140, 140, 150, -1, 1, -1)
    point_light(220, 220, 255, 0, cam_target_y, 600)

    if use_obj and loaded_mesh: shape(loaded_mesh)
    else: draw_concrete_column(110, 2200)

    # Ground
    fill(35); no_stroke()
    push_matrix(); rotate_x(HALF_PI); rect(-8000, -8000, 16000, 16000); pop_matrix()

    for ivy in ivy_list:
        ivy.update(); ivy.display()
    draw_hud()

def draw_concrete_column(r, h):
    no_stroke(); specular(30); shininess(0.5)
    begin_shape(QUAD_STRIP)
    for i in range(41):
        angle = TWO_PI / 40 * i
        x, z = cos(angle) * r, sin(angle) * r
        fill(remap(noise(x*0.05, z*0.05), 0, 1, 95, 135))
        vertex(x, 0, z); vertex(x, -h, z)
    end_shape()

def draw_hud():
    reset_matrix(); camera(); no_lights()
    fill(0, 225); stroke(140, 255, 140, 200); stroke_weight(2)
    rect(25, 25, 300, 210, 15)
    fill(use_obj and 80 or 40, 140, 40); rect(45, 140, 260, 45, 10)
    fill(255); text_size(15)
    text(f"LIGHT: {round(room_brightness, 2)}", 50, 60)
    text(f"ZOOM: {int(cam_zoom)}", 50, 95)
    text("LOAD .OBJ MESH", 110, 168); text("PRESS 'F' TO FOCUS", 90, 210)

def exiting():
    if cap: cap.release()
    if stream: stream.stop()