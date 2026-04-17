# Change Log for Step 2 - Processing (Python Mode)


### 📌 Overview
Move into 3D territory with py5, we transition from 2D coordinates to $(x, y, z)$. py5 uses the P3D renderer for this.  
Importing 3D formats like .obj is built directly into py5 via the load_shape() function. However, .fbx is a complex proprietary format that standard Processing/py5 doesn't support natively. Sticking to .obj is the gold standard because it is text-based, widely available, and highly stable.


#### New Scripts
- The 3D Asset Manager: model_loader   
Creates a class to handle the loading and centering of the 3D object.


#### Updating Scripts
The 3D Viewport: main.py   
We need to change the size() call to use the P3D renderer and add variables to control the object's rotation.


### ⌨️ What Changed
The transition from the first script to the second represents a shift from a 2D interactive UI to a 3D hardware-accelerated environment.

1. Functional Scope and Imports
- 3D Capabilities: The second script imports model_loader (specifically load_asset and draw_asset) to handle external 3D geometry.

- Removed Audio: The audio sensor functionality and noise_level logic from the first script were removed to focus on the 3D model rendering.

2. Rendering Engine and Setup
- P3D Mode: The size() function was updated from size(800, 600) to size(1200, 800, P3D). Adding the P3D parameter is critical as it enables the 3D rendering engine.

- Asset Loading: The setup() function now includes load_asset("Phone.obj") to initialize a 3D model into the global my_model variable.

3. Visuals and Lighting
- Lighting Effects: The second script introduces lights() and ambient_light(50, 50, 50). These are essential for creating depth; without them, 3D models appear as flat silhouettes.

- Background: The background was darkened from 20 to 10 to enhance the 3D depth perception.

4. Interactive Logic
- Rotation vs. Position: The first script tracked position via axis_x and axis_y. The second script replaces these with rot_x and rot_y to control the model's orientation.

- Data Integration: In the second script, the activity value from the camera sensor now dynamically influences the model's rotation speed: rot_y += 0.01 + (activity * 0.00001).

5. UI Layering (2D Over 3D)
- Depth Management: To keep the UI visible over the 3D model, the second script uses hint(DISABLE_DEPTH_TEST) and camera() to reset the view to a 2D overlay before drawing the axis.

- Input Handling: The mouse interaction functions (mouse_dragged and mouse_pressed) from the first script were removed in favor of automated rotation based on camera activity


### 📂 Project Structure
```
.
├── audio_sensor.py
├── camera_sensor.py
├── main.py
├── model_loader.py
├── ui_elements.py
└── README.md
```

### 🧠 Code Breakdown
#### main
```python
# Import Sensor-Driven Interaction
from camera_sensor import get_activity
from audio_sensor import get_noise_level

# Window setup and rendering mode
size(1200, 800, P3D)

# Camera Usage (OpenCV)
cap = none
prev_gray = None

# Scene State Variable
rot_x, tor_y = 0, 0
my_model = None

# Asset Loading
from model_loader import load_asset, draw_asset

my_model = None

# Visual Intent $ Aesthetics
background(10) #Darker for 3D Depth

# Interaction model (mouse vs sensor)
def (mouse_dragged():
	axis_x += mouse_x - pmouse_x
	axis_y += mouse_y - pmouse_y
```


### 🧠 Fundamentally Different
- Step_1 main.py: Teaches the basic interaction and structure
- Step_2 main.py: Applies that knowledge to a sensor-driven 3D system



### 👤 Author / Context   
Created as a capstone work in an advanced creative coding / digital art curriculum, focusing on audio‑driven generative systems, real‑time data visualization, and performative digital form in Processing.