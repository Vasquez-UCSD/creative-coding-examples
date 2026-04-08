# The Moving Boundary - Processing (Python Mode)
### Difficulty Level 3

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Motion%20%26%20Boundaries-purple)
![Python](https://img.shields.io/badge/Technique-State%20%26%20Conditionals-orange)
![Python](https://img.shields.io/badge/Status-Complete-brightgreen)

### 📌 Overview
The Moving Boundary is an animated sketch written in Processing (Python Mode) that demonstrates motion, boundaries, and directional change using variables and conditional logic.
A circle moves horizontally across the canvas and reverses direction when it reaches the edges, visually illustrating how programs can respond to spatial limits.
 
 
### 🖼 Screenshot

![Alt Text](assets/mbss.png)
 
 
### 🔄 Motion Concept
This sketch introduces continuous motion controlled by:
- A position variable (x)
- A velocity variable (speed)
- Boundary detection using width
- Direction reversal when limits are reached

The result is a predictable but visually clear animation loop.


### 🛠 Requirements
- Processing (latest version recommended)
- Python Mode enabled in Processing


#### Installation
1. Download Processing: 
👉 https://processing.org/download
2. Open Processing
3. Switch to Python Mode


### ▶️ How to Run
1. Open Processing
2. Set mode to Python
3. Open The_Moving_Boundary.py
4. Click Run ▶
5. Watch the circle move back and forth across the screen


### 📂 Project Structure
```
.
├── The Moving Boundary.py
├── README.md
├──Moving Boundary/
│	├──Moving_Boundary.pyde
│	└──Moving_Boundary.properties
└── assets/
	└── mbss.png
```


🧠 Code Breakdown
```python
x = 0
speed = 5

def setup():
    size(800, 200)

def draw():
    global x, speed  # Required to modify global variables in Python
    background(240)

    x += speed

    if x > width or x < 0:
        speed *= -1  # Reverse direction

    circle(x, height / 2, 50)
```


### Key Concepts
- Global variables 
x controls position, speed controls movement direction and rate.

- draw() loop 
Updates the animation every frame.

- x += speed 
Moves the circle horizontally.

- Boundary conditions 
When x exceeds the canvas width or goes below zero, the direction reverses.

- speed *= -1 
A simple yet powerful way to flip movement direction.


### 🎯 Learning Objectives
- Understand basic animation using variables
- Work with global variables in Python Mode
- Detect and respond to boundaries
- Use conditionals to control behavior
- Visualize repetition and motion over time


### ✨ Ideas for Extension
- Add vertical movement for 2D motion
- Change speed dynamically
- Modify color when direction changes
- Add easing or acceleration
- Introduce multiple moving objects
- Make boundaries visible with guide lines


### 👤 Author / Context

Created as part of an introductory creative coding or digital art assignment, focusing on animation fundamentals, motion control, and boundary logic in Processing.