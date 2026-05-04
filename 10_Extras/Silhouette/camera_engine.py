import cv2
import numpy as np
import config

class CameraEngine:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        
    def capture_silhouette(self):
        success, frame = self.cap.read()
        if not success: return
        
        # 1. Standard Pre-processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (7, 7), 0)
        
        # 2. Use OTSU Thresholding for a more "solid" mask than Adaptive
        # This works best if your fabric is significantly lighter or darker than the floor
        _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        # 3. FILL HOLES: Find contours and fill the largest one
        # This ensures the "inside" of the fabric is solid white
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Create a blank black canvas for the clean mask
        solid_mask = np.zeros_like(mask)
        
        if contours:
            # Find the largest contour (the fabric)
            largest_cnt = max(contours, key=cv2.contourArea)
            # Draw and FILL the contour with white (255)
            cv2.drawContours(solid_mask, [largest_cnt], -1, 255, thickness=cv2.FILLED)
        
        # 4. Clean up the edges
        kernel = np.ones((5,5), np.uint8)
        solid_mask = cv2.morphologyEx(solid_mask, cv2.MORPH_CLOSE, kernel)
        
        # Match mask to sketch size
        config.silhouette_mask = cv2.resize(solid_mask, (1200, 800))
        config.is_mask_active = True

    def close(self):
        self.cap.release()