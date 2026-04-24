import numpy as np

# Audio state
rms_volume = 0.0
smoothed_rms = 0.0  # Added missing attribute
spectrum = np.zeros(60)
audio_data = None
sample_rate = 44100
is_playing = False
audio_mode = "MIC" 
start_time = 0

# Visual/Calibration state
is_mask_enabled = True
is_calibrating = True
mask_rects = []
corners = []
canvas = None
stars = []
selected_idx = -1
is_adding_mask = False
aurora = None