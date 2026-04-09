# Image Manipulation - Processing (Python Mode)
### Difficulty Level 8

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Image%20Manipulation-purple)
![Python](https://img.shields.io/badge/Technique-Pixel%20Sampling-orange)
![Python](https://img.shields.io/badge/Status-Complete-brightgreen)


### 📌 Overview
Image Manipulation is a Processing (Python Mode) sketch that introduces image loading, display, and pixel sampling as interactive inputs for visual output.
The sketch reads color data directly from an image based on mouse position and uses that information to dynamically generate new visual elements.


### 🖼 Screenshot   
![Alt Text](assets/imss.gif)


###🖼️ Concept Focus
This sketch explores how images can be treated as data, not just visuals:
- Images are loaded into memory
- Individual pixels can be sampled
- Color information can be reused elsewhere
- User interaction determines which data is accessed

This marks a shift from purely procedural graphics to media‑driven generative systems.


### 🛠 Requirements
- Processing (latest version recommended)
- Python Mode enabled in Processing
- An image file placed inside the sketch’s data/ folder
⚠️ The sketch will not run correctly unless the image file exists in the data folder.


### ▶️ How to Run
1. Open Processing
2. Set mode to Python
3. Ensure 'your image'.png is inside the data directory
4. Open Image_Manipulation.py
5. Update image name in the script
6. Click Run ▶
7. Move the mouse across the image to sample colors


📂 Project Structure
```
.
├── Image_Manipulation.py
├── README.md
├──Image_Manipulation/
│	├──Image_Manipulation.pyde
│	└──Image_Manipulation.properties
└── assets/
	└── imss.gif
```


### 🧠 Code Breakdown
#### Image Loading
```python
img = None

def setup():
    global img
    size(600, 600)
    img = load_image("your image.png or jpg")
```
- Loads the image into memory
- Makes the image available globally
 Image must exist in the data folder

#### Drawing and Sampling
```python
def draw():
    image(img, 0, 0)
    c = get(mouse_x, mouse_y)
    fill(c)
    rect(0, 0, 100, 100)
```

### Key Concepts:
- image(img, 0, 0)   
Displays the image on the canvas

- get(mouse_x, mouse_y)   
Samples the color of the pixel under the mouse

- fill(c)   
Applies the sampled color

- rect()   
Visualizes pixel data as a new shape


### 🎯 Learning Objectives
-Load and display images
-Understand images as pixel grids
-Sample individual pixel color values
-Use mouse interaction to access image data
-Translate image data into generative visuals
-Bridge media and computation


### ✨ Ideas for Extension
- Create a color‑palette extractor
- Sample multiple pixels simultaneously
- Build a mosaic or pixel‑sorting effect
- Animate shapes using image data
- Use average color sampling over an area
- Combine with particles or vectors
- Manipulate RGB values directly
- Apply filters or color transformations


### 👤 Author / Context   
Created as part of an advanced stage of an introductory creative coding / digital art assignment, focusing on image processing fundamentals, interaction, and data‑driven visuals in Processing.