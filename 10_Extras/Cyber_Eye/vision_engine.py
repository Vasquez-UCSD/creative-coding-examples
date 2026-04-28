import cv2
import config
import threading
import numpy as np
import behavior_engine

class VisionThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                gray = cv2.cvtColor(cv2.resize(frame, (320, 240)), cv2.COLOR_BGR2GRAY)
                avg_bright = np.mean(gray)
                
                # Base light dilation (0.15 to 0.7)
                light_base = 1.0 - (avg_bright / 255.0)
                light_base = max(0.15, min(0.7, light_base))
                
                # Emotional Adjustment
                emotion_mult = behavior_engine.EMOTION_MAP.get(config.current_emotion, 1.0)
                
                # --- COMPLEX BEHAVIOR: FACE INTEREST ---
                # Dilation increases by 1.2x if a face is actively tracked
                interest_mult = 1.2 if config.is_tracking else 1.0
                
                config.pupil_dilation = max(0.1, min(1.0, light_base * emotion_mult * interest_mult))

                faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
                if len(faces) > 0:
                    (x, y, w, h) = faces[0]
                    config.target_x = (320 - (x + w/2)) * (1200 / 320)
                    config.target_y = (y + h/2) * (800 / 240)
                    config.is_tracking = True
                else:
                    config.is_tracking = False

tracker = VisionThread()
tracker.start()