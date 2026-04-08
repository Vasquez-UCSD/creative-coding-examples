Trigonometric Movement Circular Paths - Processing (Python Mode)
Difficulty Level 6
https://img.shields.io/badge/Processing-Python%20Mode-blue
https://img.shields.io/badge/Concept-Trigonometric%20Movement-purple
https://img.shields.io/badge/Technique-Sine%20%26%20Cosine-orange
https://img.shields.io/badge/Status-Complete-brightgreen

📌 Overview
Trig Movement Circular Paths is an animated sketch written in Processing (Python Mode) that uses trigonometric functions (sin and cos) to create smooth circular motion.
The sketch demonstrates how mathematical functions can be used to generate predictable, continuous paths, forming the foundation for orbital motion, waves, and complex generative systems.

🔵 Motion Concept
This sketch creates circular movement by:

Using an angle that increases over time
Mapping cosine to horizontal motion
Mapping sine to vertical motion
Offsetting motion from the center of the canvas
Applying a partially transparent background to create motion trails

The result is a point that continuously orbits around the center of the screen.

🛠 Requirements

Processing (latest version recommended)
Python Mode enabled in Processing

Installation

Download Processing:
👉 https://processing.org/download
Open Processing
Switch to Python Mode


▶️ How to Run

Open Processing
Set mode to Python
Open Trig_Movement_Circular_Paths.py
Click Run ▶
Observe the circular motion and trailing effect


📂 Project Structure
Plain Text.├── Trig_Movement_Circular_Paths.py└── READMEShow more lines

🧠 Code Breakdown
Pythonangle = 0def draw():    global angle    background(255, 10)  # Trail effect    x = width / 2 + cos(angle) * 100    y = height / 2 + sin(angle) * 100    circle(x, y, 20)    angle += 0.05Show more lines
Key Concepts


Angle variable (angle)
Acts as the input to the trigonometric functions.


cos(angle) & sin(angle)
Calculate x and y positions on a circle.


Radius (100)
Controls the size of the circular path.


background(255, 10)
Uses transparency to fade previous frames, creating a trail effect.


Incrementing the angle
Moves the point smoothly along the circular path.



🎯 Learning Objectives

Use trigonometry for motion
Understand circular coordinate systems
Create orbital movement
Apply transparency for motion trails
Combine math with animation
Move beyond linear motion patterns


✨ Ideas for Extension

Add multiple orbiting points
Vary radius using Perlin noise
Change speed dynamically
Create spiral motion by increasing radius
Add color variation based on angle
Connect multiple points to form rotating structures


👤 Author / Context
Created as part of an introductory creative coding / digital art assignment, focusing on trigonometry, circular motion, and mathematical animation in Processing.