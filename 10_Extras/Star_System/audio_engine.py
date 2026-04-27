import sounddevice as sd
import numpy as np
import soundfile as sf
import time

class AudioEngine:
    def __init__(self):
        self.spectrum = np.zeros(60)
        self.audio_data = None
        self.sample_rate = 44100
        self.is_playing = False
        self.mode = "MIC"
        self.start_time = 0
        
        self.stream = sd.InputStream(callback=self._audio_callback, channels=2)
        self.stream.start()

    def _audio_callback(self, indata, frames, time_val, status):
        if self.mode == "MIC":
            data = indata.mean(axis=1) if indata.ndim > 1 else indata
            fft_data = np.fft.rfft(data)
            self.spectrum = np.abs(fft_data)[:60]

    def load_file(self, path):
        if path:
            self.audio_data, self.sample_rate = sf.read(path)
            self.mode = "FILE"

    def update_file_analysis(self):
        if self.mode == "FILE" and self.is_playing:
            elapsed = time.time() - self.start_time
            idx = int(elapsed * self.sample_rate)
            chunk_size = 2048
            if idx < len(self.audio_data) - chunk_size:
                chunk = self.audio_data[idx : idx + chunk_size]
                if self.audio_data.ndim > 1: chunk = chunk.mean(axis=1)
                fft_data = np.fft.rfft(chunk)
                self.spectrum = np.abs(fft_data)[:60]
            else:
                self.is_playing = False
                self.mode = "MIC"