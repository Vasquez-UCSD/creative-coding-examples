import py5
import config
import random

EMOTION_MAP = {
    "Neutral": 1.0,
    "Surprised": 1.4,
    "Scared": 1.5,
    "Angry": 0.8,
    "Focused": 0.9,
    "Sleepy": 1.1,
    "Love": 2.0
}

def update_behavior():
    # Randomly shift emotion
    if random.random() < 0.005:
        config.current_emotion = random.choice(list(EMOTION_MAP.keys()))
    
    # --- COMPLEX BEHAVIOR: TARGET LOCK-ON ---
    # If tracking, move faster (0.4) to 'lock on'. If drifting, move slower (0.05).
    lerp_speed = 0.4 if config.is_tracking else 0.05
    
    config.current_x += (config.target_x - config.current_x) * lerp_speed
    config.current_y += (config.target_y - config.current_y) * lerp_speed

    # Idle drift logic
    if not config.is_tracking:
        config.target_x += py5.noise(py5.frame_count() * 0.01) * 10 - 5
        config.target_y += py5.noise(py5.frame_count() * 0.01 + 100) * 10 - 5

    # Blink logic
    if random.random() < 0.01 and config.blink_progress <= 0:
        config.blink_progress = 1.0
    if config.blink_progress > 0:
        config.blink_progress -= 0.1