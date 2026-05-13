### HUD Examples

This project implements a modular, draggable, and animated Head-Up Display (HUD) system built with **py5**. It demonstrates core UI/UX principles for games and interactive applications, including event-driven state changes, animated transitions, and coordinate mapping.
#### 🚀 Features
* **Draggable Interface**: A multi-component panel system with a dedicated "header" hit-box for repositioning the entire UI group.
* **Animated Interactions**: Buttons utilize smooth linear interpolation (Lerp) for hover scaling, providing tactile feedback to the user.
* **State-Linked Components**: A dynamic Health Bar and Volume Slider that respond to both direct mouse interaction and global state changes.
* **Clamped Logic**: Robust handling of values (Health 0-100) to prevent UI overflow or logic errors during rapid interaction.
* **Hybrid Input**: Supports both high-precision mouse dragging and rapid-response keyboard hotkeys for "gameplay" simulation.

#### 🛠️ System Architecture
The project follows a clean, class-based approach to UI rendering and interaction:

| Component | Description |
| :--- | :--- |
| **`Global State`** | Manages shared variables like `health`, `slider_value`, and the `panel_x/y` coordinates. |
| **`Button Class`** | Handles localized hover detection, scale animations, and action-based callbacks (Heal/Damage/Reset). |
| **`Slider Class`** | Translates horizontal mouse movement into normalized 0-100 values with a visual "glow" knob. |
| **`HealthBar Class`** | A reactive visualizer that maps the current health percentage to a dynamic rectangle width. |
| **`Input Logic`** | Decoupled event handlers (`mouse_pressed`, `mouse_dragged`, `key_pressed`) that route interactions to the UI elements. |

#### 📂 Usage
1.  **Installation**: Ensure you have the `py5` library installed in your Python environment.
2.  **Execution**: Run `HUD_examples.py` to launch the interactive window.
3.  **Interaction**:
    * **Drag Panel**: Click and hold the header ("HUD PANEL") to move the interface across the canvas.
    * **Buttons**: Click "Heal" or "Damage" to update health. Use "Reset" to return to 100%.
    * **Slider**: Click and drag the pink knob to adjust the system "Volume" readout.
    * **Hotkeys**: 
        * `W`: Heal (+5)
        * `S`: Damage (-5)
        * `R`: Reset Health

#### 🧪 Design Highlights
* **Coordinate Offsets**: All UI elements are drawn relative to the `panel_x/y` variables, allowing the entire HUD to be repositioned without breaking individual component layout.
* **Visual Feedback**: Includes a scale-up effect on button hover and a glow effect on the active slider knob to enhance the "Cyber" aesthetic.

---
*Note: This project serves as a foundational example of creating custom interactive UI elements from scratch without external widget libraries.*
"""