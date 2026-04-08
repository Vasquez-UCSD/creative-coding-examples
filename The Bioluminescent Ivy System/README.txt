The Bioluminescent Ivy System - Processing / py5 (Python Mode)
Difficulty Level 10
https://img.shields.io/badge/Processing-py5%20%2F%20Python-blue
https://img.shields.io/badge/Concept-Bio--Inspired%20Systems-purple
https://img.shields.io/badge/Inputs-Audio%20%7C%20Vision%20%7C%20Movement-orange
https://img.shields.io/badge/Status-Final%20Capstone-brightgreen

📌 Overview
The Bioluminescent Ivy System is a large‑scale sensor‑driven generative system that simulates bioluminescent ivy growing along architectural columns in response to live environmental input.
The system ingests:

Audio (microphone amplitude)
Visual data (camera brightness & motion)
Spatial logic (3D geometry and growth systems)

These inputs collectively drive the behavior, growth, and visual intensity of a virtual “living” organism.
This sketch represents a transition from interactive visuals to responsive architectural ecosystems.

🌿 Concept Focus: Bio‑Inspired Adaptive Systems
The project is inspired by:

Bioluminescent organisms
Climbing plants and ivy growth patterns
Architectural lighting systems
Responsive installations and environments

Rather than reacting to a single input, the system behaves like a living organism, interpreting multiple signals from its surroundings to determine how it grows and glows.

🛠 Requirements

Processing / py5 (Python Mode)
OpenCV (cv2) for camera input
sounddevice for live audio input
NumPy
A connected microphone
A connected camera / webcam
P3D renderer

⚠️ This sketch is intended for desktop execution, not browser‑based environments.

▶️ How to Run

Ensure required Python libraries are installed:

opencv-python
sounddevice
numpy


Open the sketch in Processing (Python Mode / py5)
Connect a microphone and camera
Click Run ▶
Make sound, move in front of the camera, or adjust ambient lighting
Observe the ivy system respond organically


📂 Project Structure
Python.├── The_Bioluminescent_Ivy_System.py└── README.mdShow more lines

🧠 System Architecture
Global Environmental Sensors
Pythonmic_vol = 0room_brightness = 0motion_level = 0Show more lines
These variables represent the environmental state of the space:

Sound intensity
Ambient light level
Movement detected by the camera

They act as shared inputs across the entire system.

Ivy Strand Class
Pythonclass IvyStrand:    def __init__(self, base_x, base_z, column_radius):        self.segments = [Py5Vector(base_x, 0, base_z)]        self.radius = column_radius        self.max_segments = 100        self.current_length = 10        self.angle_offset = random(TWO_PI)``Show more lines
Each ivy strand is:

An autonomous growth structure
Anchored to architectural geometry
Composed of connected segments
Capable of expanding, curling, and glowing

This object‑oriented design allows many strands to coexist and respond independently.

Audio Input (Microphone)
Pythondef audio_callback(indata, frames, time, status):    global mic_vol    mic_vol = np.linalg.norm(indata) * 0.1Show more lines

Captures live sound amplitude
Converts pressure into usable scalar data
Drives energy, glow intensity, or growth speed


Visual Input (Camera)
Pythoncap = cv2.VideoCapture(0)prev_frame = NoneShow more lines
The camera system enables:

Ambient brightness detection
Motion sensing via frame comparison
Behavioral modulation based on audience presence


Architectural Geometry
Pythondef draw_column(r, h):    begin_shape(QUAD_STRIP)    ...    end_shape()Show more lines

Column geometry acts as the habitat
Ivy grows on architecture, not in empty space
Reinforces installation‑ready thinking


🎯 Learning Objectives

Combine multiple real‑world data streams
Design systems instead of isolated effects
Work with audio and vision simultaneously
Build bio‑inspired growth behaviors
Use object‑oriented design for complexity
Think architecturally in 3D space
Create installation‑scale responsive artwork
Bridge art, code, biology, and environment


✨ Ideas for Extension

Map brightness to color temperature
Add photosynthesis‑like energy accumulation
Use motion level to repel or attract growth
Project onto real architectural columns
Record and replay environmental states
Introduce seasonal growth cycles
Network multiple systems together
Drive real LEDs or lighting hardware
Add AI‑based perception (face or gesture detection)


👤 Author / Context
Created as a final capstone project in an advanced creative coding / digital art curriculum, focusing on adaptive systems, sensor‑driven generative art, and installation‑ready computational design.