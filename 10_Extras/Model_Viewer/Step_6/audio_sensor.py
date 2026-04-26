# PY5 IMPORTED MODE CODE
import sounddevice as sd
import numpy as np

try:
    stream = sd.InputStream(channels=1, samplerate=44100)
    stream.start()
except Exception as e:
    print(f"Could not open microphone: {e}")
    stream = None

def get_noise_level(time):
    """Return real-time amplitude from mic"""
    if stream is None:
        return 0.0
        
    # Read data chunk
    # 1024 frames is a good balance between responsiveness and smoothness
    data, overflowed = stream.read(1024)
    
    # Calculate amplitude (RMS - Root Mean Square)
    # Gives us a simgle "loudness" values
    amplitude = np.linalg.norm(data) * 20
    
    # Constrain the value so it does not flicker too widely
    return min(amplitude, 100.0)