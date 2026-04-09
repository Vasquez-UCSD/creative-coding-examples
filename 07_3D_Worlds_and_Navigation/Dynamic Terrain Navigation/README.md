# Dynamic Terrain Navigation - Processing (Python Mode)
### Difficulty Level 10

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Terrain%20Navigation-purple)
![Python](https://img.shields.io/badge/Technique-Noise%20%2B%203D%20Interaction-orange)
![Python](https://img.shields.io/badge/Status-Capstone-brightgreen)


### 📌 Overview
Dynamic Terrain Navigation is a sophisticated Processing (Python Mode) sketch that combines procedural 3D terrain generation with real‑time interactive navigation.
A wireframe landscape is generated using Perlin noise, and a spherical object (“the ball”) dynamically moves across and rides the terrain surface, accurately matching the terrain’s elevation beneath it based on mouse input.
This sketch demonstrates how consistent data models allow multiple systems (terrain + agent) to coexist coherently in a shared world.


### 🖼 Screenshot   
![Alt Text](assets/dtss.gif)


### 🧭 Concept Focus: Navigation on Procedural Systems
This work moves beyond visualization into spatial interaction:
- The terrain is not static scenery
- The ball is not arbitrarily placed
- Both are driven by the same underlying noise function

This guarantees:
- Physical plausibility
- Visual coherence
- Believable “contact” between object and environment

This is a core idea in simulations, games, and interactive 3D environments.


### 🛠 Requirements
- Processing (latest version recommended)
- Python Mode
- P3D renderer (required for 3D graphics)
- remap() utility function available in your environment


### ▶️ How to Run
1. Open Processing
2. Switch to Python Mode
3. Open Dynamic_Terrain_Navigation.py
4. Click Run ▶
5. Move the mouse around the window
6. Observe the red sphere navigate the terrain surface in real time


### 📂 Project Structure
```
.
├── Dynamic_Terrain_Navigation.py
├── README.md
├──Dynamic_Terrain_Navigation/
│	├──Dynamic_Terrain_Navigation.pyde
│	└──Dynamic_Terrain_Navigation.properties
└── assets/
	└── dtss.gif
```


### 🧠 Code Breakdown
#### Camera & Scene Setup
```python
translate(width/2, height/2 + 50, -200)
rotate_x(radians(60))
lights()
```
- Centers the terrain in view
- Tilts the camera for depth perception
- Enables lighting for true 3D form visibility

#### Terrain Definition
```python
grid_size = 20
spacing = 40
offset = (grid_size * spacing) / 2
```
- Grid‑based terrain structure
- Spacing controls terrain resolution
- Offset ensures terrain is centered at the origin

#### Procedural Terrain Mesh
```python
z = noise(x * 0.1, y * 0.1, frame_count * 0.01) * 150
```
- Perlin noise creates smooth elevation
- Time (frame_count) animates the terrain
- Triangle strips efficiently form a continuous mesh

### Input‑Driven Navigation
```python
ball_grid_x = remap(mouse_x, 0, width, 0, grid_size - 1)
ball_grid_y = remap(mouse_y, 0, height, 0, grid_size - 1)
```
- Mouse position mapped to terrain grid coordinates
- Decouples screen space from world space
- Makes navigation intuitive and precise

### Terrain‑Aware Agent Positioning
```python
ball_z = noise(ball_grid_x * 0.1,
               ball_grid_y * 0.1,
               frame_count * 0.01) * 150
```

✅ Critical idea:   
The ball’s height is computed using the exact same noise function as the terrain.   
This ensures the ball:
- Always sits on the surface
- Never floats or clips through terrain
- Reacts dynamically as the terrain animates

### Rendering the Navigating Ball
```python
translate(ball_world_x, ball_world_y, ball_z + 20)
sphere(20)
```
- World‑space conversion from grid coordinates
- Height offset keeps the sphere visibly above the surface
- Lighting reveals true volume and curvature


### 🎯 Learning Objectives
- Generate and animate 3D procedural terrain
- Maintain consistency across multiple systems
- Convert between screen, grid, and world coordinates
- Use Perlin noise as a shared data model
- Integrate user input into 3D environments
- Implement terrain‑aware navigation
- Think in terms of world logic, not isolated visuals


### ✨ Ideas for Extension
- Add momentum and slope‑based acceleration
- Implement collision or falling behavior
- Add multiple navigating agents
- Visualize surface normals for physics
- Add camera follow or orbit controls
- Shade terrain based on slope or elevation
- Integrate autonomous agents instead of mouse control
- Combine with audio or data‑driven terrain modulation


### 👤 Author / Context   
Created as part of an advanced creative coding / digital art curriculum, focusing on procedural worlds, interactive navigation, and coordinated generative systems in Processing.