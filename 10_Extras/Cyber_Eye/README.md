### Cyber Eye: Biologically Inspired Computer Vision Sketch

This project implements a responsive, "living" eye that tracks faces in real-time using py5 and OpenCV. Unlike static animations, this system uses multi-threaded computer vision to drive organic behaviors, including light-reactive pupil dilation and physiological emotional states.

#### 🚀 Features
* **Threaded Vision Processing**: Decouples heavy OpenCV face detection from the animation loop to maintain a smooth 60 FPS.
* **Biological Dilation**: Pupils realistically contract in bright light and dilate in darkness by analyzing average frame brightness.
* **Physiological Emotion Mapping**: Eye dilation is further modified by emotional states such as "Scared" (high arousal dilation) or "Angry" (focused constriction).
* **Organic Movement**: Uses Linear Interpolation (Lerp) and Perlin noise to create fluid, lifelike eye tracking and "idle" wandering.
* **Cyber-HUD**: A dedicated UI engine provides real-time diagnostic data on tracking status and emotional offsets.

#### 🛠️ System Architecture
The project is built on a modular multi-engine architecture to ensure clean code and high performance:

| Component | Description |
| :--- | :--- |
| **`main.py`** | The entry point that orchestrates the engines and sets the drawing canvas. |
| **`config.py`** | The "Central Nervous System" storing global variables like target coordinates and dilation states. |
| **`vision_engine.py`** | The sensory input. Uses a background thread to process camera frames for faces and light levels. |
| **`behavior_engine.py`** | The "Brain." Decides how the eye should move, when to blink, and transitions between emotions. |
| **`eye_engine.py`** | The "Body." Handles the visual rendering of the iris, pupil, and eyelids. |
| **`ui_engine.py`** | The "Dashboard." Renders the cybernetic HUD overlays and tracking data. |

#### 📂 Usage
1.  **Installation**: Ensure you have `py5`, `opencv-python`, and `numpy` installed in your Thonny environment.
2.  **Execution**: Run `main.py` to start the sketch.
3.  **Interaction**:
    * **Face Tracking**: Move in front of your webcam; the eye will "lock on" and follow you.
    * **Light Sensitivity**: Shine a light at the camera to watch the pupil contract.
    * **Emotions**: Observe the HUD to see the eye's current emotional state and how it affects pupil size.

---
*Note: This project was developed iteratively as part of a systems design study in real-time interactive visuals.*