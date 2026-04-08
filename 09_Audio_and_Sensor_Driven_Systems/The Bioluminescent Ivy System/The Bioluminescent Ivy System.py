import cv2
import sounddevice as sd
import numpy as np

# --- Global Sensors ---
mic_vol = 0
room_brightness = 0
motion_level = 0
ivy_list = []

# --- Ivy Logic ---
class IvyStrand:
    def __init__(self, base_x, base_z, column_radius):
        self.segments = [Py5Vector(base_x, 0, base_z)]
        self.radius = column_radius
        self.max_segments = 100
        self.current_length = 10 # Starting size
        self.angle_offset = random(TWO_PI)

    def update(self):
        global room_brightness, motion_level
        
        # 1. Growth/Shrink Logic based on Light
        # If brightness > 0.4, grow. Else, shrink.
        growth_step = remap(room_brightness, 0, 1, -0.5, 0.8)
        self.current_length = constrain(self.current_length + growth_step, 5, self.max_segments)
        
        # 2. Add segments if growing
        if len(self.segments) < int(self.current_length):
            last = self.segments[-1]
            # Spiral up the column
            new_x = self.radius * cos(len(self.segments) * 0.2 + self.angle_offset)
            new_z = self.radius * sin(len(self.segments) * 0.2 + self.angle_offset)
            new_y = last.y - 8 # Growing upwards
            self.segments.append(Py5Vector(new_x, new_y, new_z))
        
        # 3. Remove segments if shrinking
        elif len(self.segments) > int(self.current_length) and len(self.segments) > 1:
            self.segments.pop()

    def display(self):
        global mic_vol, motion_level
        
        # 4. Color Logic (Sound -> Hue)
        color_mode(HSB, 360, 100, 100)
        leaf_hue = remap(mic_vol, 0, 0.5, 120, 300) # Green to Purple
        stroke(leaf_hue, 80, 90)
        no_fill()
        
        # 5. Motion Logic (Webcam -> Sway)
        sway = sin(frame_count * 0.1) * (motion_level * 50)
        
        begin_shape()
        for i, v in enumerate(self.segments):
            # Apply physics sway to higher segments
            x_off = sway * (i / len(self.segments))
            vertex(v.x + x_off, v.y, v.z)
            
            # Draw Leaves every 5 segments
            if i % 5 == 0:
                push_matrix()
                translate(v.x + x_off, v.y, v.z)
                fill(leaf_hue, 70, 80, 150)
                rotate_y(i * 0.5)
                ellipse(0, 0, 15, 10)
                pop_matrix()
        end_shape()
        color_mode(RGB, 255)

# --- External Input Callbacks ---
def audio_callback(indata, frames, time, status):
    global mic_vol
    mic_vol = np.linalg.norm(indata) * 0.1

cap = cv2.VideoCapture(0)
prev_frame = None

def setup():
    size(1000, 900, P3D)
    global stream
    stream = sd.InputStream(callback=audio_callback)
    stream.start()
    
    # Initialize 8 strands around the column
    for a in range(0, 360, 45):
        rad = 100
        x = cos(radians(a)) * rad
        z = sin(radians(a)) * rad
        ivy_list.append(IvyStrand(x, z, rad))

def draw():
    background(5)
    global cap, prev_frame, room_brightness, motion_level
    
    # --- Sensor Processing (CV) ---
    ret, frame = cap.read()
    if ret:
        small = cv2.resize(frame, (160, 120))
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
        
        # Light Sensor: Average Brightness
        room_brightness = np.mean(gray) / 255.0
        
        # Motion Sensor: Frame Differencing
        if prev_frame is not None:
            diff = cv2.absdiff(prev_frame, gray)
            motion_level = np.mean(diff) / 255.0
        prev_frame = gray

    # --- Scene Rendering ---
    translate(width/2, height - 100, -200)
    rotate_y(mouse_x * 0.01) # Manual camera orbit
    lights()
    
    # Draw the Column (The Projection Surface)
    no_stroke()
    fill(30)
    with push_matrix():
        # Processing draws cylinders from the center
        translate(0, -400, 0)
        # Custom cylinder helper
        draw_column(100, 800)

    # Update and Draw Ivy
    for ivy in ivy_list:
        ivy.update()
        ivy.display()

def draw_column(r, h):
    """ Helper to draw a simple column """
    begin_shape(QUAD_STRIP)
    for i in range(31):
        angle = TWO_PI / 30 * i
        x = cos(angle) * r
        z = sin(angle) * r
        vertex(x, 0, z)
        vertex(x, h, z)
    end_shape()