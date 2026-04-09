# Pixel Manipulation Arrays - Processing (Python Mode)
### Difficulty Level 9

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Pixel%20Manipulation-purple)
![Python](https://img.shields.io/badge/Technique-Pixel%20Arrays-orange)
![Python](https://img.shields.io/badge/Status-Advanced-brightgreen)


### 📌 Overview
Pixel Manipulation Arrays is an advanced Processing (Python Mode) sketch that directly accesses and modifies the pixel buffer using array‑based manipulation.
Instead of drawing shapes or lines, this sketch works at the lowest visual level—individual pixels—demonstrating how images and the screen itself are fundamentally data structures that can be processed algorithmically.


### 🖼 Screenshot   
![Alt Text](assets/pmss.gif)


### 🧬 Concept Focus: Pixels as Data
This sketch introduces a critical creative‑coding insight:  
	*The screen is an array.*
By accessing the pixels[] array directly, the sketch treats every pixel as a manipulable data element, enabling effects that are impossible (or inefficient) using standard drawing commands.


### 🛠 Requirements
- Processing (latest version recommended)
- Python Mode
- A graphics context that supports pixel manipulation


### ▶️ How to Run
1. Open Processing
2. Switch to Python Mode
3. Open Pixel_Manipulation_Arrays.py
4. Click Run ▶

The screen will fill with fast‑updating grayscale noise resembling analog TV static.


### 📂 Project Structure
```
.
├── Pixel_Manipulation_Arrays.py
├── README.md
├──Pixel_Manipulation_Arrays/
│	├──Pixel_Manipulation_Arrays.pyde
│	└──Pixel_Manipulation_Arrays.properties
└── assets/
	└── pmss.gif
```


### 🧠 Code Breakdown
```python
def setup():
    size(400, 400)
    # Lower frame rate makes the static easier to see, 
    # but remove this for "fast" noise.
    frame_rate(90)
def draw():
    load_pixels()
    for i in range(len(pixels)):
        pixels[i] = color(random(255)) # Generates static
    update_pixels()
```


### Key Concepts
- load_pixels()   
Loads the current screen’s pixel data into the pixels[] array.

- pixels[] array   
A one‑dimensional array representing every pixel onscreen.

- Direct indexing (pixels[i])   
Allows modification of each pixel individually.

- random(255)   
Assigns random grayscale values, producing visual noise.

- update_pixels()   
Pushes modified pixel data back to the display.


### 🎯 Learning Objectives
- Understand the screen as a pixel array
- Manipulate images at the data level
- Learn the relationship between pixels and performance
- Generate procedural textures (noise/static)
- Build a foundation for filters and image effects
- Shift from shape‑based drawing to raster processing


### ✨ Ideas for Extension
- Color static using RGB channel control
- Animate noise patterns over time
- Build glitch or datamosh effects
- Apply pixel sorting algorithms
- Combine with image loading (pixels + loadImage)
- Use Perlin noise instead of random values
- Create feedback or trail‑based effects
- Mask or warp pixel regions interactively


### 👤 Author / Context   
Created as part of an advanced creative coding / digital art curriculum, focusing on low‑level raster manipulation, algorithmic image generation, and performance‑aware visual systems in Processing.