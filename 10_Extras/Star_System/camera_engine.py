import cv2
import numpy as np

class CameraEngine:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.prev_frame = None
        self.hand_x = 0
        self.hand_y = 0
        self.vx = 0
        self.vy = 0
        self.is_active = False

    def update(self, w, h):
        success, frame = self.cap.read()
        if not success: return

        # 1. Pre-process: Resize (to speed up), Flip, and Grayscale
        frame = cv2.flip(frame, 1)
        frame_small = cv2.resize(frame, (320, 240))
        gray = cv2.cvtColor(frame_small, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return

        # 2. Frame Differencing: Find the pixels that changed
        frame_delta = cv2.absdiff(self.prev_frame, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        self.prev_frame = gray

        # 3. Find the "Center of Mass" of the motion
        coords = cv2.findNonZero(thresh)
        if coords is not None:
            self.is_active = True
            # Calculate mean position of all moving pixels
            avg_pos = np.mean(coords, axis=0)[0]
            
            # Map coordinates to screen size
            new_x = (avg_pos[0] / 320) * w
            new_y = (avg_pos[1] / 240) * h
            
            # Calculate Swipe Velocity
            self.vx = new_x - self.hand_x
            self.vy = new_y - self.hand_y
            self.hand_x = new_x
            self.hand_y = new_y
        else:
            self.is_active = False
            self.vx *= 0.5
            self.vy *= 0.5

    def close(self):
        self.cap.release()