# Follow Cam Terrain Navigator - Processing (Python Mode)
### Difficult Level 10

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Follow%20Camera-purple)
![Python](https://img.shields.io/badge/Technique-3D%20Navigation-orange)
![Python](https://img.shields.io/badge/Status-Capstone-brightgreen)


### 📌 Overview
Follow Cam Terrain Navigator is an advanced Processing (Python Mode) sketch that introduces a follow‑camera system for navigating 3D procedural environments.
Instead of a fixed camera, the viewpoint dynamically tracks a moving target, creating the foundation for world exploration, simulation cameras, and game‑engine‑style navigation.
This sketch shifts the role of the camera from a passive observer to an active participant in the system.


### 🖼 Screenshot   
![Alt Text](assets/tnss.gif)


### 🎥 Concept Focus: Camera as a System
In advanced 3D and interactive systems, the camera is not static — it is governed by logic just like any other object.
This sketch introduces:
- Camera position stored as a vector
- Smooth camera tracking
- Separation of camera state from world state
- The idea of “viewpoint as behavior”

This is critical in:
- Games
- Simulations
- Virtual environments
- Immersive installations
- Projection mapping workflows


### 🛠 Requirements
- Processing (latest version recommended)
- Python Mode
- P3D renderer
- Vector support (Py5Vector or Processing vector equivalent)


### ▶️ How to Run
1. Open Processing
2. Switch to Python Mode
3. Open Follow_Cam_Terrain_Navigator.py
4. Click Run ▶
5. Observe the camera positioning logic prepare for dynamic tracking

(This sketch establishes core infrastructure for camera control that can be expanded in later iterations.)


### 📂 Project Structure
```
.
├── Follow Cam Terrain Navigator.py
├── README.md
├──Follow_Cam_Terrain_Navigator/
│	├──Follow_Cam_Terrain_Navigator.pyde
│	└──Follow_Cam_Terrain_Navigator.properties
└── assets/
	└── tnss.gif
```


### 🧠 Code Breakdown
#### Camera State (Global)
```python
cam_eye = Py5Vector(0, 0, 0)
```
- Stores the camera’s current eye position
- Treated as a persistent system variable
- Enables smoothing, interpolation, and behavioral logic

### Setup: Initial Camera Placement
```python
def setup():
    size(1000, 800, P3D)
    cam_eye = Py5Vector(0, 300, 500)
```
- Establishes a starting vantage point
- Elevated and offset to give a terrain overview
- Mimics third‑person or drone‑style camera placement

### Draw Loop: Camera Readiness
```python
def draw():
    background(15)
```
- Clears the frame for continuous redraw
- Dark background emphasizes depth and geometry
- Prepares the camera system for terrain + target integration


### 🧭 Camera Design Philosophy
This sketch lays the groundwork for:
- Camera lag / smoothing
	*(interpolating camera position instead of snapping)*
- Target tracking
	*(following an agent or terrain‑riding object)*
- Offset cameras
	*(behind, above, or orbiting a subject)*
- Perspective storytelling
	*(what the viewer is allowed to see and from where)*

The camera becomes part of the world logic, not an afterthought.


### 🎯 Learning Objectives
- Treat the camera as a controllable entity
- Use vectors for viewpoint management
- Separate camera logic from rendering logic
- Prepare for smooth following and interpolation
- Think spatially in terms of viewpoint and navigation
- Build toward game‑engine camera architectures


### ✨ Ideas for Extension
- Smooth camera motion using lerp() or interpolation
- Camera follow with delay (cinematic lag)
- Mouse‑controlled camera orbit
- First‑person vs third‑person camera modes
- Camera collision with terrain
- Dynamic zoom based on speed
- Integrate with autonomous agents
- Switch between multiple cameras
- Use camera direction vectors (lookAt logic)


### 👤 Author / Context   
Created as part of an advanced creative coding / digital art curriculum, focusing on camera systems, 3D navigation, and world‑based interaction design in Processing.