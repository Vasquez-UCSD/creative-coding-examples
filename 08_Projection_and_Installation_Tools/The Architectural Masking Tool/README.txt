The Architectural Masking Tool - Processing (Python Mode)
Difficulty Level 8
https://img.shields.io/badge/Processing-Python%20Mode-blue
https://img.shields.io/badge/Concept-Architectural%20Masking-purple
https://img.shields.io/badge/Technique-Interactive%20Projection%20Tools-orange
https://img.shields.io/badge/Status-Capstone-brightgreen

📌 Overview
The Architectural Masking Tool is an advanced projection‑mapping utility built in Processing (Python Mode).
It extends prior keystone calibration work by introducing interactive masking, allowing users to define rectangular regions where projected visuals should be hidden or revealed.
This sketch functions not as a standalone artwork, but as a professional‑grade tool for working with architectural surfaces, irregular environments, and real‑world projection constraints.

🏛️ Concept Focus: Architectural Masking
Architectural masking is a critical technique in:

Projection mapping
Installation art
Theatre and stage design
Live visuals for irregular surfaces

This tool allows the user to:

Define masked regions directly on the canvas
Toggle masking on and off
Clear and redraw mask regions dynamically
Combine masking with calibration and keystone workflows


🛠 Requirements

Processing (latest version recommended)
Python Mode
P3D renderer (required for offscreen graphics and future transformations)


▶️ How to Run

Open Processing
Switch to Python Mode
Open The_Architectural_Masking_Tool.py
Click Run ▶

Keyboard Controls

C — Toggle calibration mode
M — Enable / disable masking
X — Clear all mask rectangles

Mouse Interaction

Click & drag corner handles to adjust calibration
Click & drag to define mask rectangles (when mask mode is enabled)


📂 Project Structure
Plain Text.├── The_Architectural_Masking_Tool.py└── README.mdShow more lines

🧠 Code Breakdown
Global Masking State
Plain Textmask_rects = []   # List of [top_left_vector, bottom_right_vector]is_mask_enabled = Trueis_adding_mask = False``Show more lines

Stores all defined mask regions
Tracks whether masking is active
Tracks whether a new mask is currently being drawn


Offscreen Canvas
Pythoncanvas = create_graphics(1200, 800, P3D)Show more lines

Enables advanced rendering workflows
Allows masking and transforms to be applied before projection
Mirrors real‑world projection pipelines


Interaction Logic (Keyboard)
Pythonif key.lower() == 'm':    is_mask_enabled = not is_mask_enabledif key.lower() == 'x':    mask_rects = []``Show more lines

Enables dynamic control during setup
Allows quick iteration during installation or alignment
Designed for rapid testing in dark environments


Interaction Logic (Mouse)
Pythonelif is_adding_mask:    mask_rects[-1][1].set(mouse_x, mouse_y)Show more lines

Allows freeform drawing of rectangular masks
Updates mask boundaries in real time
Provides immediate visual feedback


🎯 Learning Objectives

Build tool‑oriented creative code
Combine multiple interaction systems (keyboard + mouse)
Manage complex global state safely
Model real‑world projection workflows
Separate calibration, masking, and rendering logic
Design utilities for installation and production contexts


✨ Ideas for Extension

Apply masks directly to rendered content
Add polygon or freehand masking
Save/load masking presets
Layer multiple mask sets
Animate masks for dynamic reveals
Combine with live video or camera input
Apply perspective‑correct quad warping
Export calibration + mask data for reuse


👤 Author / Context
Created as part of an advanced creative coding / digital art curriculum, focusing on projection mapping tools, architectural masking, and installation‑ready workflows in Processing.