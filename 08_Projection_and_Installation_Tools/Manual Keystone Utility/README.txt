Manual Keystone Utility - Processing (Python Mode)
Difficulty Level 8
https://img.shields.io/badge/Processing-Python%20Mode-blue
https://img.shields.io/badge/Concept-Projection%20Mapping-purple
https://img.shields.io/badge/Technique-Interactive%20Calibration-orange
https://img.shields.io/badge/Status-Complete-brightgreen

📌 Overview
Manual Keystone Utility is an advanced Processing (Python Mode) utility designed for manual keystone calibration, a technique commonly used in projection mapping, installation art, and interactive media environments.
The sketch provides an interactive calibration interface that allows the user to reposition corner control points directly on screen, enabling alignment of projected visuals with real‑world surfaces.

🧱 Concept Focus: Projection Mapping & Calibration
This sketch shifts from generative visuals to tool‑building:

The sketch acts as a utility, not just an artwork
Users interact with control handles to adjust geometry
Visuals are designed for projector environments
Global state tracks calibration mode and selection

This represents professional‑grade creative coding practice often used in live visuals, gallery installations, and stage design.

🛠 Requirements

Processing (latest version recommended)
Python Mode enabled
P3D renderer (required for future keystone transforms)

Installation

Download Processing:
👉 https://processing.org/download
Open Processing
Switch to Python Mode


▶️ How to Run

Open Processing
Set mode to Python
Open Manual_Keystone_Utility.py
Click Run ▶
Click and drag corner handles to reposition them
Press C to toggle calibration mode on/off


📂 Project Structure
Plain Text.├── Manual_Keystone_Utility.py└── README.md``Show more lines

🧠 Code Breakdown
Global Calibration State
Pythoncanvas = Nonecorners = []selected_idx = -1is_calibrating = TrueShow more lines

Stores projector mapping data
Tracks selected control handle
Allows toggling calibration mode
Centralized global state for transformation logic


Setup & Rendering
Pythondef setup():    size(1200, 800, P3D)``Show more lines

Uses a widescreen canvas suitable for projection
P3D prepares the sketch for 3D transformations

Pythondef draw():    background(0)Show more lines

Black background for optimal projector contrast
Prevents residual light bleed


Calibration UI
Pythondef draw_calibration_ui():    for i, p in enumerate(corners):        if i == selected_idx:            fill(255, 0, 0)        else:            fill(0, 255, 255, 150)        circle(p.x, p.y, 20)Show more lines
Key ideas:

Visual control handles
Selected handle highlighted in red
Semi‑transparent handles for usability
Direct spatial feedback for the user


Mouse Interaction
Pythondef mouse_pressed():    for i, p in enumerate(corners):        if dist(mouse_x, mouse_y, p.x, p.y) < 25:            selected_idx = i``Show more lines

Detects proximity to corner handles
Enables click‑to‑select behavior

Pythondef mouse_dragged():    corners[selected_idx].x = mouse_x    corners[selected_idx].y = mouse_y``Show more lines

Updates corner positions in real time
Enables intuitive drag‑based calibration


Keyboard Control
Pythondef key_pressed():    if key.lower() == 'c':        is_calibrating = not is_calibrating``Show more lines

Toggles calibration mode
Prepares the system for live runtime vs setup modes


🎯 Learning Objectives

Build interactive utility tools
Manage complex global state
Understand calibration workflows
Design UI elements for non‑mouse users (projection)
Separate visualization logic from control logic
Work toward projection‑mapped systems


✨ Ideas for Extension

Apply perspective transforms to mapped content
Save and load calibration presets
Use control points to warp textures
Add grid overlays for alignment accuracy
Integrate live visuals or camera input
Support multiple projector surfaces
Transition from 2D to full quad warping


👤 Author / Context
Created as part of an advanced creative coding / digital art workflow, focusing on projection mapping tools, calibration systems, and interactive utilities in Processing.