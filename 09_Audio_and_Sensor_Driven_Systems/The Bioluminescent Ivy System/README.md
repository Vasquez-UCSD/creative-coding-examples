# The Bioluminescent Ivy System - Processing / py5 (Python Mode)
### Difficulty Level 10

![Python](https://img.shields.io/badge/Processing-py5%20%2F%20Python-orange)
![Python](https://img.shields.io/badge/Concept-Bio--Inspired%20Systems-purple)
![Python](https://img.shields.io/badge/Inputs-Audio%20%7C%20Vision%20%7C%203D%20Space-blue)
![Python](https://img.shields.io/badge/Status-Capstone-brightgreen)


### 📌 Overview
The Bioluminescent Ivy System is a large‑scale adaptive generative system that simulates glowing, plant‑like growth responding to environmental input and architectural context.
The system listens, watches, and reacts.
Instead of drawing a static object, the code defines a living organism that grows, climbs, branches, and glows in response to:
- 🔊 Sound (microphone amplitude)
- 👁 Light & motion (camera analysis)
- 🏛 Architecture (columns or imported 3D meshes)
- 🎥 Camera position & scale (spatial navigation)

This project represents a shift from creative visuals to responsive digital environments suitable for installation art and projection‑based work.


### 🖼 Screenshot   
![Alt Text](assets/biss1.gif)    
![Alt Text](assets/biss2.gif)   
![Alt Text](assets/biss3.gif)   


### 🌿 Concept Focus: Living Systems in Space
The project is inspired by:
- Bioluminescent organisms
- Ivy and climbing plant behavior
- Architectural lighting design
- Adaptive environments

Rather than reacting to a single input, the system integrates multiple sensor streams into a coherent behavioral model.

*The ivy does not “animate” — it responds.*


### 🧠 System Progression (Versions)
The project evolved through three major versions, each expanding the system’s complexity and scope.


### 🌱 Version 1 - Core Growth System
The Bioluminescent Ivy System.py
Focus:
- Core ivy strand logic
- Audio input via microphone
- Basic environmental sensing
- Growth along a cylindrical column

Key Concepts:
- Audio amplitude as energy input
- Procedural segment growth
- Architectural anchoring
- Object‑oriented strand behavior

This version establishes the idea of growth as behavior, not animation.


### 🌿 Version 2 - Environmental Awareness & Camera Control
The Bioluminescent Ivy System V2.py
Additions:
- Camera‑based brightness detection
- Motion sensing (frame difference)
- Multiple ivy strands
- Camera zoom via mouse wheel
- Heads‑Up Display (HUD)

New Behaviors:
- Light affects growth rate
- Motion affects sway and response
- Ivy strands differentiate via color and length
- The viewer’s position becomes part of the system

This version transforms the ivy from a growing object into an environment‑aware organism.


### 🌳 Version 3 - Architectural Integration & Mesh Climbing
The Bioluminescent Ivy System V3.py
Major Features:
- Load external OBJ meshes
- Ivy growth adapts to arbitrary geometry
- Dynamic camera focus and framing
- Mesh‑based spatial awareness
- Branching, climbing, and bridging behavior
- Expanded HUD and interaction logic

Key Conceptual Shift:   
*The ivy adapts to architecture, not the other way around.*

At this stage, the project becomes installation‑ready, supporting real spaces and custom structures.


### 🛠 Requirements
- Thonny / py5 (Python Mode)
- Python libraries:
	- opencv-python (camera input)
	- sounddevice (audio input)
	- numpy
- A working microphone
- A connected camera / webcam
- P3D renderer
- Optional: .obj 3D models (for V3)

⚠️ Intended for desktop execution, not browser environments.


### ▶️ How to Run
1. Ensure required Python libraries are installed:
	- opencv-python 
	- sounddevice
	- numpy
2. Open the sketch in Thonny (Python Mode / py5)
3. Connect a microphone and camera
4. Click Run ▶
5. Make sound, move in front of the camera, or adjust ambient lighting
6. Observe the ivy system respond organically


### ⌨️ Interaction Summary
Common Controls
- Sound → energy / glow / growth
- Light → growth behavior
- Motion → responsiveness or sway
- Mouse Wheel → camera zoom
- Mouse Click (V3) → load OBJ mesh
- Keyboard (V3) → re‑focus camera

The viewer becomes an active participant in the ecosystem.


### 📂 Project Structure
```
.
├── The Bioluminescent Ivy System.py
├──	The Bioluminescent Ivy System V2.py
├──	The Bioluminescent Ivy System V3.py
├── README.md
└── assets/
	├──biss1.gif
	├──biss2.gif
	└──biss3.gif
```


### 🧠 System Architecture
#### Environmental Sensors
```python
Audio  → mic_vol
Light  → room_brightness
Motion → motion_level
```
These signals act as a shared environmental state.
Ivy Strand Object Model
Each ivy strand:
- Stores its own segments
- Tracks growth limits
- Responds independently to sensory input
- Can branch, climb, or bridge surfaces

This allows emergent complexity without centralized control.

Architectural Substrate

- V1–V2: Cylindrical concrete columns
- V3: Arbitrary imported mesh geometry

The environment is treated as a habitat, not a background.

#### Ivy Strand Class
```python
class IvyStrand:
    def __init__(self, base_x, base_z, column_radius):
        self.segments = [Py5Vector(base_x, 0, base_z)]
        self.radius = column_radius
        self.max_segments = 100
        self.current_length = 10
        self.angle_offset = random(TWO_PI)
```
Each ivy strand is:
- An autonomous growth structure
- Anchored to architectural geometry
- Composed of connected segments
- Capable of expanding, curling, and glowing

This object‑oriented design allows many strands to coexist and respond independently.

#### Audio Input (Microphone)
```python
def audio_callback(indata, frames, time, status):
    global mic_vol
    mic_vol = np.linalg.norm(indata) * 0.1
```
- Captures live sound amplitude
- Converts pressure into usable scalar data
- Drives energy, glow intensity, or growth speed

#### Visual Input (Camera)
```python
cap = cv2.VideoCapture(0)
prev_frame = None
```
The camera system enables:
- Ambient brightness detection
- Motion sensing via frame comparison
- Behavioral modulation based on audience presence

#### Architectural Geometry
```python
def draw_column(r, h):
    begin_shape(QUAD_STRIP)
    ...
    end_shape()
```
- Column geometry acts as the habitat
- Ivy grows on architecture, not in empty space
- Reinforces installation‑ready thinking


### 🎯 Learning Objectives
- Combine multiple real‑world data streams
- Design systems instead of isolated effects
- Work with audio and vision simultaneously
- Build bio‑inspired growth behaviors
- Use object‑oriented design for complexity
- Think architecturally in 3D space
- Create installation‑scale responsive artwork
- Bridge art, code, biology, and environment


### ✨ Ideas for Extension
- Map brightness to color temperature
- Add photosynthesis‑like energy accumulation
- Use motion level to repel or attract growth
- Project onto real architectural columns
- Record and replay environmental states
- Introduce seasonal growth cycles
- Network multiple systems together
- Drive real LEDs or lighting hardware
- Add AI‑based perception (face or gesture detection)


### 👤 Author / Context   
Created as a final capstone project in an advanced creative coding / digital art curriculum, focusing on adaptive systems, sensor‑driven generative art, and installation‑ready computational design.