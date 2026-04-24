import numpy as np
import sounddevice as sd
import config

def audio_callback(indata, frames, time, status):
    if config.audio_mode == "MIC":
        mono = indata.mean(axis=1) if indata.ndim > 1 else indata
        fft = np.fft.rfft(mono)
        config.spectrum = np.abs(fft)[:60]

stream = sd.InputStream(callback=audio_callback, channels=2)
stream.start()