# Acoustic Brutalism Data Sonification - Processing (Python Mode)
### Difficulty Level 10

![Python](https://img.shields.io/badge/Processing-Python%20Mode-blue)
![Python](https://img.shields.io/badge/Concept-Data%20Sonification-purple)
![Python](https://img.shields.io/badge/Input-Live%20Audio-blue)
![Python](https://img.shields.io/badge/Status-Capstone-brightgreen)


### 📌 Overview
Acoustic Brutalism is a real‑time audio‑reactive generative system that translates live microphone input into a jagged, architectural visual form.
Instead of treating sound as something to illustrate, this sketch treats sound as structural data. Volume becomes force. Noise becomes distortion. Form becomes an architectural response to acoustic energy.
The result is a continuously evolving, circular structure whose roughness reflects the intensity of sound in the room.


### 🖼 Screenshot   
![Alt Text](assets/abss.gif)  


### 🔊 Concept Focus: Sound as Data
This sketch explores data sonification in reverse:  
*Instead of turning data into sound, sound is turned into geometry.*

Key ideas include:
- Audio amplitude as a continuously sampled data stream
- Controlled randomness bound by sound energy
- Symmetry disrupted by environmental input
- Form that feels constructed rather than decorative

The aesthetic draws inspiration from brutalist architecture — heavy, raw, non‑ornamental forms shaped by underlying forces.


### 🛠 Requirements
- Processing (latest version recommended)
- Python Mode
- Processing Sound library
- A working microphone input

#### Enable the Sound Library
In Processing:
1. Go to Sketch → Import Library… → Sound
2. Make sure microphone permissions are enabled on your system


### ▶️ How to Run
1. Open Processing
2. Switch to Python Mode
3. Ensure the Sound library is installed
4. Open Acoustic_Brutalism_Data_Sonification.py
5. Click Run ▶
6. Make sound near your microphone and observe the form react in real time


### ⌨️ Interaction
- Sound level = primary input
- No mouse or keyboard input required
- Louder environments produce more aggressive geometry
- Quiet environments produce smoother, more stable forms

This makes the sketch suitable for:
- live performance
- installation
- audience‑driven interaction


### 📂 Project Structure
```
.
├── Acoustic_Brutalism_Data_Sonification.py
├── README.md
├──Acoustic_Brutalism_Data_Sonification/
│	├──Acoustic_Brutalism_Data_Sonification.pyde
│	└──Acoustic_Brutalism_Data_Sonification.properties
└── assets/
	└── abss.gif
```

### 🧠 Code Breakdown
#### Audio Input & Analysis
```python
mic = sound.AudioIn(this, 0)
mic.start()

analyzer = sound.Amplitude(this)
analyzer.input(mic)

```
- Captures live microphone input
- Measures amplitude (overall sound energy)
- Produces a normalized floating‑point value per frame

#### Motion Blur Background
```python
background(20, 50)
```
- Semi‑transparent redraw creates visual persistence
- Reinforces motion and sonic continuity

#### Form Generation
```python
volume = analyzer.analyze()
roughness = volume * 1000
```
- Louder sound = greater geometric distortion
- Quiet sound = more stable form

#### Brutalist Shape Construction
```python
for a in range(0, 361, 5):
    roughness = volume * 1000
    r = 200 + random(-roughness, roughness)
```

### Key ideas:
- Circular topology
- Jagged perimeter
- Controlled randomness
- Symmetry broken by audio data
- Architecture driven by sound energy


### 🎯 Learning Objectives
- Capture and analyze live audio input
- Treat sound as continuous data
- Map amplitude to visual behavior
- Combine randomness with structure
- Create responsive, performative systems
- Explore audio‑visual translation
- Design visuals for live input environments


### ⚠️ Known Limitations (Intentional)
- Uses amplitude only (no frequency analysis)
- Geometry is 2D (no extrusion yet)
- Single data stream drives all variation

These constraints are intentional to keep the focus on mapping clarity.


# ✨ Ideas for Extension
- Use FFT for frequency‑based distortion
- Create multi‑layered sound‑responsive forms
- Map bass vs treble to different geometries
- Add color response to sound spectrum
- Record and replay acoustic data
- Drive 3D extrusion using audio amplitude
- Use external audio streams (music, radio)
- Combine with projection mapping tools from earlier sketches


### 👤 Author / Context   
Created as a capstone work in an advanced creative coding / digital art curriculum, focusing on audio‑driven generative systems, real‑time data visualization, and performative digital form in Processing.