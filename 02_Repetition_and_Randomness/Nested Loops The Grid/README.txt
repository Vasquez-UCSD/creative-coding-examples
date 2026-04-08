Nested Loops The Grid - Processing (Python Mode)
Difficulty Level 5
https://img.shields.io/badge/Processing-Python%20Mode-blue
https://img.shields.io/badge/Concept-Nested%20Loops-purple
https://img.shields.io/badge/Technique-Grid%20Generation-orange
https://img.shields.io/badge/Status-Complete-brightgreen

📌 Overview
Nested Loops The Grid is a generative sketch written in Processing (Python Mode) that uses nested for loops to create a grid‑based composition.
Each cell in the grid is drawn individually, allowing for structured repetition while introducing variation through random color values.

🧩 Visual Concept
This sketch explores the balance between structure and randomness:

A consistent grid layout provides order
Random grayscale fills introduce variation
Negative space between shapes enhances clarity
The entire composition is generated algorithmically

Every run produces a unique grid, while maintaining a recognizable overall structure.

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
Open Nested_Loops_The_Grid.py
Click Run ▶
Rerun to generate a new randomized grid


📂 Project Structure
Python.├── Nested_Loops_The_Grid.py└── README.md``Show more lines

🧠 Code Breakdown
Pythondef setup():    size(600, 600)    for x in range(0, width, 50):        for y in range(0, height, 50):            fill(random(255))            rect(x, y, 45, 45)``Show more lines
Key Concepts


Nested loops
One loop controls horizontal placement (x), the other vertical placement (y).


Grid step size (50)
Determines spacing and number of grid cells.


rect(x, y, 45, 45)
Slightly smaller rectangles create visible gaps between cells.


random(255)
Assigns a random grayscale value to each grid element.


setup()
Generates the full composition once at launch.



🎯 Learning Objectives

Understand nested iteration
Generate two‑dimensional patterns
Work with grids and spatial systems
Combine repetition with randomness
Learn algorithmic layout strategies


✨ Ideas for Extension

Animate the grid using draw()
Use color instead of grayscale
Add interaction (mouse or keyboard)
Change cell sizes dynamically
Apply Perlin noise for smoother variation
Create responsive grids based on window size


👤 Author / Context
Created as part of an introductory creative coding / digital art assignment, focusing on nested loops, grid systems, and generative pattern design in Processing.