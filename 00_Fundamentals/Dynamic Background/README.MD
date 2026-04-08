Dynamic Background — Processing (Python Mode) 
Difficulty Level 1

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Interaction-Mouse%20Input-purple)
![Python](https://img.shields.io/badge/Status-Complete-brightgreen)
![Python](https://img.shields.io/badge/Type-Dynamic%20Sketch-orange)

📌 Overview
Dynamic Background is a simple interactive sketch written in Processing (Python Mode).
It demonstrates how the draw() function and mouse input can be used to create a dynamic background that updates continuously in real time.
This sketch introduces foundational animation and interaction concepts in creative coding.

🖼 Screenshot

  assets/dbss.png

Description:
- The background color changes continuously
- The red color channel responds to the horizontal position of the mouse
- Moving the mouse left to right alters the background’s tint

🛠 Requirements
- Processing (latest version recommended)
- Python Mode enabled in Processing

Installation
1. Download Processing:
👉 https://processing.org/download
2. Open Processing
3. Switch to Python Mode using the mode selector

▶️ How to Run
1. Open Processing
2. Set mode to Python
3. Open Dynamic_Background.py
4. Click Run ▶
5. Move your mouse horizontally across the canvas to see the interaction

📂 Project Structure
```
.
├── Dynamic_Background.py
├── README.md
├──Dynamic_Background/
│	├──Dynamic_Background.pyde
│	└──Dynamic_Background.properties
└── assets/
    └── dbss.png
```

🧠 Code Breakdown
```python
def draw():
    # Background in draw "clears" the screen every frame
    background(mouseX / 2, 100, 200)
```

Key Concepts
- draw()
Runs continuously (approximately 60 frames per second).

- background()
Clears and redraws the screen each frame.

- mouse_x / 2
Uses mouse position to control the red color channel, creating real‑time interaction.

- Fixed green and blue values (100, 200)
Ensure smooth, readable color variation.

🎯 Learning Objectives
- Understand the difference between setup() and draw()
- Use mouse input for interactivity
- Control color dynamically
- Learn how real‑time rendering works in Processing

✨ Ideas for Extension
- Map color to mouseY
- Animate gradients or patterns
- Add shapes on top of the dynamic background
- Smooth transitions with map() or lerp()
- Combine with setup() to define window size and frame rate


👤 Author / Context
Created as part of an introductory creative coding / digital art assignment, focusing on interactivity, animation, and user input in Processing.
