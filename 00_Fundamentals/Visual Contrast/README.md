Visual Contrast — Processing (Python Mode) 
Difficulty Level 2

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Visual%20Contrast-purple)
![Python](https://img.shields.io/badge/Interaction-Mouse%20Input-orange)
![Python](https://img.shields.io/badge/Status-Complete-brightgreen)

📌 Overview
Visual Contrast is an interactive sketch written in Processing (Python Mode) that explores the concept of visual contrast using scale, color, and motion.
The sketch layers static and dynamic elements to demonstrate how contrast can guide visual attention and spatial hierarchy in a composition.

🖼 Screenshot

  assets/vcss.png


🎨 Visual Concept
The sketch features:
- A dark background to enhance brightness contrast
- A large, static circle centered in the frame
- A small, bright circle that follows the mouse
- Contrast created through:
-- Size (large vs small)
-- Color saturation
-- Motion vs stillness

The viewer’s eye is naturally drawn to the moving element despite its smaller size.

🛠 Requirements
- Processing (latest version recommended)
- Python Mode enabled in Processing

Installation
1. Download Processing: 
👉 https://processing.org/download
2. Open Processing
3. Switch to Python Mode

▶️ How to Run
1. Open Processing
2. Set mode to Python
3. Open Visual_Contrast.py
4. Click Run ▶
5. Move your mouse around the window to interact with the sketch

📂 Project Structure
```
.
├── Visual_Contrast.py
├── README.md
├──Visual_Contrast/
│	├──Visual_Contrast.pyde
│	└──Visual_Contrast.properties
└── assets/
	└── vcss.png
```

🧠 Code Breakdown
```python
def setup():
    size(600, 600)
    no_stroke()

def draw():
    background(20)
    fill(255, 0, 100)
    circle(300, 300, 400)

    fill(255)
    circle(mouse_x, mouse_y, 50)  # Contrast through scale and color
```

Key Concepts
- setup() 
Initializes the canvas and disables outlines for cleaner shapes.

- draw() 
Continuously refreshes the canvas for real‑time interaction.

- background(20) 
Creates a dark field to enhance contrast.

- Large stationary circle 
Acts as a visual anchor.

- Small mouse‑controlled circle 
Creates contrast through motion, scale, and brightness.


🎯 Learning Objectives
- Understand visual contrast principles
- Explore scale and color relationships
- Combine motion with static elements
- Reinforce use of setup() vs draw()
- Practice interactive composition design


✨ Ideas for Extension
- Change colors based on mouse speed
- Add transparency (alpha) for layering effects
- Introduce multiple moving elements
- Explore contrast using shape instead of size
- Animate the background for shifting visual tension


👤 Author / Context 
Created as part of an introductory creative coding or digital art assignment, focusing on visual principles and interactive design in Processing.