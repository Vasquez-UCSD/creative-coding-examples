# The Architectural Masking Tool - Processing (Python Mode)
### Difficulty Level 10

![Python](https://img.shields.io/badge/Processing-py5%20%2F%20Python-orange)
![Python](https://img.shields.io/badge/Concept-Architectural%20Masking-purple)
![Python](https://img.shields.io/badge/Use%20Case-Projection%20Mapping-blue)
![Python](https://img.shields.io/badge/Level-Advanced-brightgreen)


### 📌 Overview
The Architectural Masking Tool is an advanced projection‑mapping utility designed to help align and control projected visuals on non‑rectangular architectural surfaces.
Rather than acting as a finished artwork, this sketch functions as a tool—one that supports calibration, masking, and setup workflows commonly required in installation art, stage design, and spatial projection.
The focus is on controlling where light appears and where it does not.


### 🖼 Screenshot   
![Alt Text](assets/amss.gif)   


### 🏛️ Concept Focus: Architectural Masking
In real‑world projection, walls are rarely perfect rectangles. Doors, windows, columns, and irregular edges often need to be excluded from projection.
This tool introduces:
- Mask regions that block projected light
- Calibration modes for setup vs runtime
- Keyboard‑driven tool control
- A dark background optimized for projectors

Rather than shaping visuals to the screen, this system shapes visuals to the space.


### 🛠 Requirements
- Processing / py5 (Python Mode)
- P3D renderer (required for future expansion)
- Mouse and keyboard input

⚠️ This sketch is intended for desktop execution in a projection or installation context.


### ▶️ How to Run
1. Open Processing
2. Switch to Python Mode
3. Open The_Architectural_Masking_Tool.py
4. Click Run ▶

Keyboard Controls  
- C - Toggle calibration mode
- M - Enable / disable masking
- X - Clear all mask rectangles

Mouse Interaction
- Click & drag corner handles to adjust calibration
- Click & drag to define mask rectangles (when mask mode is enabled)


### 📂 Project Structure
```
.
├── The_Architectural_Masking_Tool.py
├── README.md
├──The_Architectural_Masking_Tool/
│	├──The_Architectural_Masking_Tool.pyde
│	└──The_Architectural_Masking_Tool.properties
└── assets/
	└── amss.gif
```


### 🧠 Code Breakdown
#### Global Tool State
```python
mask_rects = []
is_mask_enabled = True
is_adding_mask = False
is_calibrating = True
selected_idx = -1
corners = []
canvas = None
```
These variables separate tool state from drawing logic, which is critical in installation workflows.

#### Setup & Rendering
```python
def setup():
    size(1200, 800, P3D)
```
- Large canvas suitable for projection
- P3D enables future geometric transforms
```python
def draw():
    background(0)
```
- Black background ensures no unintended light
- Essential for projector‑based systems

#### Calibration UI
```python
def draw_calibration_ui():
    no_stroke()
    fill(255, 255, 0, 150)
    for p in corners:
        circle(p.x, p
```
- Yellow handles are highly visible in dark rooms
- Designed for fast manual alignment
- UI elements intentionally minimal

#### Interaction Logic
- Keyboard input controls tool modes
- Mouse input adjusts spatial parameters
- Keystone control takes priority over masking
- States are explicitly tracked to avoid ambiguity

This structure mirrors professional projection software, where setup and runtime modes are clearly separated.


### 🎯 Learning Objectives
This sketch reinforces advanced creative‑coding concepts:
- Designing tools, not artworks
- Separating setup vs runtime logic
- Managing global system state safely
- Thinking architecturally instead of screen‑based
- Building workflows for real‑world constraints
- Preparing for projection mapping and installation art


### ⚠️ Current Limitations (Intentional)
This version focuses on infrastructure, not polish:
- Mask rectangles are stored but not yet rendered as blackout regions
- Keystone transforms are UI‑level, not yet applied to content
- The tool is designed to be extended, not finalized

This mirrors real development practice:   
*tools evolve through use.*


### ✨ Ideas for Extension
- Apply mask rectangles as true blackout regions
- Save / load calibration presets
- Support polygon or freehand masks
- Apply keystone warping to drawn content
- Integrate live visuals, images, or video
- Export calibration data for reuse
- Use the tool in a real projection test


### 👤 Author / Context   
Created as part of an advanced creative coding / digital art curriculum, focusing on projection mapping tools, architectural masking, and installation‑ready workflows in Processing.