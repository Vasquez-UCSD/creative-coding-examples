import cv2
import sounddevice as sd
import numpy as np

# --- Global Sensors ---
mic_vol = 0
room_brightness = 0
motion_level = 0
ivy_list = []
cap = cv2.VideoCapture(0)
prev_frame = None
stream = None

# --- Camera Globals ---
cam_zoom = 1500 # Adjusted starting zoom for centered view

# --- Ivy Logic ---
class IvyStrand:
    def __init__(self, base_x, base_y, base_z, column_radius, id_seed, hue_off=0):
        self.segments = [Py5Vector(base_x, base_y, base_z)]
        self.radius = column_radius
        self.max_segments = random(80, 160)
        self.current_length = 10 
        self.id_seed = id_seed 
        self.hue_offset = hue_off + random(-20, 20)
        self.current_angle = atan2(base_z, base_x)
        self.has_branched = False

    def update(self):
        global room_brightness, ivy_list
        growth_step = remap(room_brightness, 0, 1, -0.4, 0.7)
        self.current_length = constrain(self.current_length + growth_step, 2, self.max_segments)
        
        if len(self.segments) < int(self.current_length):
            last = self.segments[-1]
            step = len(self.segments)
            
            gravity_pull = remap(step, 0, self.max_segments, 14, 7) 
            drift = (noise(step * 0.05, self.id_seed) - 0.5) * 0.4
            self.current_angle += drift
            self.current_angle += (0 - self.current_angle) * 0.015
            
            draw_rad = self.radius + 8 + (noise(step * 0.1, self.id_seed) * 8)
            new_x = draw_rad * cos(self.current_angle)
            new_z = draw_rad * sin(self.current_angle)
            new_y = last.y - gravity_pull
            
            self.segments.append(Py5Vector(new_x, new_y, new_z))
            
            if step > 45 and not self.has_branched and random(1) < 0.12:
                if len(ivy_list) < 45: 
                    new_branch = IvyStrand(new_x, new_y, new_z, self.radius, random(5000), self.hue_offset)
                    new_branch.current_angle = self.current_angle + random(-0.6, 0.6)
                    ivy_list.append(new_branch)
                    self.has_branched = True
        
        elif len(self.segments) > int(self.current_length) and len(self.segments) > 2:
            self.segments.pop()

    def display(self):
        global mic_vol, motion_level
        color_mode(HSB, 360, 100, 100)
        sway = sin(frame_count * 0.1) * (motion_level * 100)
        
        for i in range(len(self.segments) - 1):
            v1, v2 = self.segments[i], self.segments[i+1]
            age_factor = i / float(len(self.segments))
            current_hue = (self.hue_offset + remap(mic_vol, 0, 0.3, 120, 310)) % 360
            leaf_brt = remap(age_factor, 0, 1, 50, 100)
            
            s1, s2 = sway * age_factor, sway * ((i+1) / float(len(self.segments)))
            
            stroke_weight(remap(age_factor, 0, 1, 9, 2))
            stroke(current_hue, 85, leaf_brt)
            line(v1.x + s1, v1.y, v1.z, v2.x + s2, v2.y, v2.z)
            
            if i % 8 == 0:
                push_matrix()
                translate(v1.x + s1, v1.y, v1.z)
                rotate_y(atan2(v1.x, v1.z))
                rotate_z(noise(i*10, self.id_seed) - 0.5)
                fill(current_hue, 80, leaf_brt, 220)
                no_stroke()
                l_size = (24 * (1-age_factor) + (mic_vol * 120)) * (0.8 + noise(i, self.id_seed) * 0.4)
                ellipse(0, 0, l_size, l_size * 0.5)
                pop_matrix()
        color_mode(RGB, 255)

def mouse_wheel(event):
    global cam_zoom
    cam_zoom += event.get_count() * 100
    cam_zoom = constrain(cam_zoom, 300, 3500)

def audio_callback(indata, frames, time, status):
    global mic_vol
    mic_vol = np.linalg.norm(indata) * 0.1

def setup():
    size(1200, 900, P3D)
    global stream, ivy_list
    random_seed(42)
    noise_seed(42)
    try:
        stream = sd.InputStream(callback=audio_callback)
        stream.start()
    except: print("Audio Input Error")
    
    for i in range(8):
        angle = random(TWO_PI)
        rad = 110
        ivy_list.append(IvyStrand(cos(angle)*rad, 0, sin(angle)*rad, rad, i*137, 120))

def draw():
    background(10)
    global cap, prev_frame, room_brightness, motion_level, cam_zoom
    
    # Process Webcam
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(cv2.resize(frame, (160, 120)), cv2.COLOR_BGR2GRAY)
        room_brightness = np.mean(gray) / 255.0
        if prev_frame is not None:
            motion_level = np.mean(cv2.absdiff(prev_frame, gray)) / 255.0
        prev_frame = gray

    hint(ENABLE_DEPTH_TEST)
    
    # --- CENTERED CAMERA LOGIC ---
    # Camera eye position: (0, -1000, cam_zoom)
    # Camera look-at position: (0, -1000, 0) - This is the vertical center of the pillar
    camera(0, -1000, cam_zoom, 0, -1000, 0, 0, 1, 0)
    
    # Mouse rotation still orbits around the center origin
    rotate_y(remap(mouse_x, 0, width, -PI, PI))
    
    ambient_light(80, 80, 95)
    directional_light(140, 140, 150, -1, 1, -1)
    point_light(200, 200, 255, 0, -1000, 500)

    # Pillar (Centered at 0,0,0 and drawn upwards)
    push_matrix()
    draw_concrete_column(110, 2200)
    pop_matrix()

    # Ground (Aligned with pillar base at y=0)
    fill(40); no_stroke()
    push_matrix(); rotate_x(HALF_PI); rect(-3000, -3000, 6000, 6000); pop_matrix()

    for ivy in ivy_list:
        ivy.update()
        ivy.display()

    draw_hud()

def draw_concrete_column(r, h):
    no_stroke(); specular(30); shininess(0.5)
    begin_shape(QUAD_STRIP)
    for i in range(41):
        angle = TWO_PI / 40 * i
        x, z = cos(angle) * r, sin(angle) * r
        n = noise(x * 0.05, z * 0.05)
        gray = remap(n, 0, 1, 95, 140) + (noise(x*0.5, z*0.5)*20)
        fill(gray if i % 10 != 0 else gray - 25, gray + 3, gray + 6)
        vertex(x, 0, z); vertex(x, -h, z)
    end_shape()
    
    # Top Cap
    fill(110); begin_shape(TRIANGLE_FAN); vertex(0,-h,0)
    for i in range(41):
        angle = TWO_PI / 40 * i
        vertex(r*cos(angle), -h, r*sin(angle))
    end_shape()

def draw_hud():
    reset_matrix(); camera(); no_lights()
    fill(0, 200); stroke(100, 255, 100, 150); stroke_weight(2)
    rect(25, 25, 300, 130, 15)
    fill(255); text_size(15)
    text(f"LIGHT (Growth): {round(room_brightness, 2)}", 45, 60)
    text(f"MOTION (Sway): {round(motion_level, 2)}", 45, 90)
    text(f"ZOOM (Distance): {int(cam_zoom)}", 45, 120)

def exiting():
    if cap: cap.release()
    if stream: stream.stop()