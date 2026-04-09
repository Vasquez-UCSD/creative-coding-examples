# Trigonometric Movement Circular Paths - Processing (Python Mode)
### Difficulty Level 6

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Trigonometric%20Movement-purple)
![Python](https://img.shields.io/badge/Technique-Sine%20%26%20Cosine-orange)
![Python](https://img.shields.io/badge/Status-Complete-brightgreen)


### 📌 Overview
Trig Movement Circular Paths is an animated sketch written in Processing (Python Mode) that uses trigonometric functions (sin and cos) to create smooth circular motion.
The sketch demonstrates how mathematical functions can be used to generate predictable, continuous paths, forming the foundation for orbital motion, waves, and complex generative systems.


### 🖼 Screenshot   
![Alt Text](assets/tmss.gif)


### 🔵 Motion Concept
This sketch creates circular movement by:
- Using an angle that increases over time
- Mapping cosine to horizontal motion
- Mapping sine to vertical motion
- Offsetting motion from the center of the canvas
- Applying a partially transparent background to create motion trails

The result is a point that continuously orbits around the center of the screen.


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
3. Open Trig_Movement_Circular_Paths.py
4. Click Run ▶
5. Observe the circular motion and trailing effect


### 📂 Project Structure
```
.
├── Trig_Movement_Circular_Paths.py
├── README.md
├──Trig_Movement_Circular_Paths/
│	├──Trig_Movement_Circular_Paths.pyde
│	└──Trig_Movement_Circular_Paths.properties
└── assets/
	└── tmss.png
```

### 🧠 Code Breakdown
```python
angle = 0

def setup():
	size(400,400)

def draw():
    global angle
    background(255, 10)  # Trail effect

    x = width / 2 + cos(angle) * 100
    y = height / 2 + sin(angle) * 100

    circle(x, y, 20)

    angle += 0.05
```


### Key Concepts
- Angle variable (angle)   
Acts as the input to the trigonometric functions.

- cos(angle) & sin(angle)   
Calculate x and y positions on a circle.

- Radius (100)   
Controls the size of the circular path.

- background(255, 10)   
Uses transparency to fade previous frames, creating a trail effect.

- Incrementing the angle   
Moves the point smoothly along the circular path.


### 🎯 Learning Objectives
- Use trigonometry for motion
- Understand circular coordinate systems
- Create orbital movement
- Apply transparency for motion trails
- Combine math with animation
- Move beyond linear motion patterns


### ✨ Ideas for Extension
- Add multiple orbiting points
- Vary radius using Perlin noise
- Change speed dynamically
- Create spiral motion by increasing radius
- Add color variation based on angle
- Connect multiple points to form rotating structures


### 👤 Author / Context   
Created as part of an introductory creative coding / digital art assignment, focusing on trigonometry, circular motion, and mathematical animation in Processing.