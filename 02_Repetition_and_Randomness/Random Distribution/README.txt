Random Distribution — Processing (Python Mode)
Difficulty Level 4
https://img.shields.io/badge/Processing-Python%20Mode-blue
https://img.shields.io/badge/Concept-Randomness-purple
https://img.shields.io/badge/Technique-Random()%20Function-orange
https://img.shields.io/badge/Status-Complete-brightgreen

📌 Overview
Random Distribution is a generative sketch created in Processing (Python Mode) that explores random distribution through point placement and color variation.
The sketch uses randomness to produce an emergent visual pattern, demonstrating how simple rules can lead to complex and unpredictable results.

🎲 Visual Concept
This sketch creates a star‑field–like composition by:

Randomly placing points across the canvas
Randomizing color values for each point
Using repetition combined with randomness
Drawing all elements once during setup()

Each execution produces a unique composition, even though the code remains the same.

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
Open Random_Distribution.py
Click Run ▶
Rerun the sketch to generate a new random composition


📂 Project Structure
Plain Text.├── Random_Distribution_Diff_4.py└── README.mdShow more lines

🧠 Code Breakdown
Pythondef setup():    size(800, 800)    background(0)    for _ in range(500):        stroke(random(255), 100, 255)        point(random(width), random(height))``Show more lines
Key Concepts


setup()
Runs once, generating the entire composition at launch.


for _ in range(500)
Repeats the drawing process 500 times.


random(width) / random(height)
Places points at unpredictable positions across the canvas.


stroke(random(255), 100, 255)
Randomizes the red channel while holding green and blue constant, creating visual cohesion within randomness.


point()
Draws minimal marks, emphasizing density and distribution.



🎯 Learning Objectives

Understand how randomness affects visual outcomes
Use random() for position and color
Combine repetition with unpredictability
Create generative artwork using simple rules
Recognize randomness as a design tool, not chaos


✨ Ideas for Extension

Increase or decrease point count
Animate random placement over time using draw()
Use Perlin noise instead of pure randomness
Change background color dynamically
Introduce shapes instead of points
Save multiple outputs as a generative series


👤 Author / Context
Created as part of an introductory creative coding or digital art assignment, focusing on randomness, generative design, and algorithmic aesthetics in Processing.