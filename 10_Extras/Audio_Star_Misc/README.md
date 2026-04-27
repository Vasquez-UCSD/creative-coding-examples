### Overview
This README explains the differences and progression between the five Python scripts in this project (main.py → main5.py).
Unlike a single finished sketch, these files represent iterative development of an audio‑reactive, projection‑oriented system built with py5, microphone input, and interactive calibration tools. Each script adds capability, structure, or conceptual clarity.
The goal across all versions is the same: Create a live audio‑driven visual system that can be calibrated to physical space, masked to architectural regions, and controlled in real time.
What changes is how far the system goes, how interactive it is, and how installation‑ready it becomes.


#### Script‑by‑Script Breakdown
1️⃣ main.py — Minimal Audio Spectrum Prototype   
Purpose: Prove that live audio input can drive usable frequency data inside py5.   
What it does:
- Captures microphone input using sounddevice
- Converts audio into a simple FFT spectrum
- Stores a small slice of frequency bins for visualization logic

What it does not do:
- No UI
- No spatial calibration
- No masking
- No file playback   

Why this exists: This is the foundation. It answers one question only: Can we reliably get real‑time frequency data into a py5 sketch?   

Think of this as the electrical test bench before anything visual or interactive is built.


2️⃣ main2.py — Basic Visualization + State Handling   
Purpose: Move from raw audio data to structured visual behavior.   
What’s new:
- Introduces persistent global state
- Begins mapping spectrum bins to screen behavior
- Establishes consistent frame‑based updates   

Key shift: Audio is no longer just data — it becomes a driver of motion or intensity.   

Still missing:
- No calibration
- No masking
- No spatial controls   

This version proves that the spectrum output is artistically usable, not just technically valid.


3️⃣ main3.py — Spatial Calibration & Interactive Corners   
Purpose: Prepare the system for real‑world projection.   
Major additions:
- Draggable corner points
- Calibration mode toggle
- Explicit separation between drawing logic and calibration state      

Why this matters: This is the first version that acknowledges a hard truth: Real installations are crooked, off‑axis, and imperfect.   

By allowing the user to move corner points, the system can now:
- Align visuals to screens, walls, or surfaces
- Compensate for projector distortion
- Support non‑rectangular display regions      

This is where the sketch stops being “a visual” and starts becoming a tool.


4️⃣ main4.py — Masking, UI, and Audio File Control   
Purpose: Add operator control and installation usability.   
New capabilities:
- On‑screen UI buttons (Load / Play / Stop / Exit)
- Toggleable calibration and masking modes
- Support for audio file playback in addition to live mic input
- Mask rectangles for excluding regions of the display   

Key conceptual leap: The system now assumes: Someone will be running this work in public.   
Masking allows visuals to be constrained around:
- Architectural obstacles
- Windows
- Pillars or dead zones   

Audio file support makes the system usable when microphones are noisy, unreliable, or inappropriate.   
This version is gallery‑functional.


5️⃣ main5.py — Particle Systems and Explosive Visual Response   
Purpose: Turn the calibrated, masked system into a high‑impact visual experience.   
Major additions:
- Star class and particle‑based visual logic
- Frequency‑bin‑driven particle behavior
- More aggressive motion tied to audio energy
- Cleaner separation between UI, calibration, and visual systems   

What changed philosophically: Earlier versions focused on control and alignment. This version focuses on expression.   
Audio no longer just scales visuals, it detonates them. Particles respond explosively to frequency bands, producing motion that feels alive, reactive, and intentional.   

This is the version you would most likely:
- Project large‑scale
- Use in performance
- Deploy as a final installation sketch   


Progression Summary

|Version	|Focus	              |Role in the System        |
|-----------|---------------------|--------------------------|
|main.py	|Audio input	      |Technical proof of concept|
|main2.py	|Audio‑driven visuals |Behavior validation       | 
|main3.py	|Calibration	      |Real‑world alignment      |
|main4.py	|Masking + UI	      |Installation control      |
|main5.py	|Particles + impact	  |Final expressive system   |


Why These Scripts Exist Separately
These files are not redundant. They are checkpoints.   

Keeping them separate allows you to:
- Revisit earlier logic without untangling newer features
- Teach or demonstrate system evolution
- Debug performance issues by stepping backward
- Adapt the level of complexity to the venue or hardware   

This is iterative systems design, not version clutter.


Intended Use
- Desktop execution (not browser)
- Live audio or pre‑composed sound
- Projection‑mapped environments
- Interactive or generative installations   

If you are running this in the real world, you start testing with main3.py, operate with main4.py, and present with main5.py.   

That division is intentional.
