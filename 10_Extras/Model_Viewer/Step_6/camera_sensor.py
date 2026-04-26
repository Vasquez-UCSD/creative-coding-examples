# PY5 IMPORTED MODE CODE
# camera_sensor.py
import cv2

def get_gesture_data(frame, prev_gray):
    """
    Processes an OpenCV frame to find motion center.
    Returns: motion_x (int), activity_count (int), current_gray (frame)
    """
    # Convert to grayscale for movement detection
    current_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    motion_sum_x = 0
    motion_count = 0
    
    if prev_gray is not None:
        # Calculate absolute difference between frames
        diff = cv2.absdiff(current_gray, prev_gray)
        # Threshold to ignore background noise
        _, thresh = cv2.threshold(diff, 40, 255, cv2.THRESH_BINARY)
        
        # Find center of motion
        # We look for non-zero pixels in the thresholded frame
        # np.nonzero() is standard, but we can do this via loops for simplicity
        # or use numpy (recommended for performance)
        import numpy as np
        coords = np.column_stack(np.where(thresh > 0))
        
        if coords.size > 0:
            motion_count = len(coords)
            motion_sum_x = np.sum(coords[:, 1]) # Column index
            center_x = motion_sum_x / motion_count
        else:
            center_x = frame.shape[1] / 2
            
        return center_x, motion_count, current_gray
    
    return frame.shape[1] / 2, 0, current_gray