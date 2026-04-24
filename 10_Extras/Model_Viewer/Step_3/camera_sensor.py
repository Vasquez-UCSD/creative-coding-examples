# camera_sensor.py
import cv2

def get_activity(cap, prev_frame):
    """Returns a motion score and the current gray frame"""
    success, frame = cap.read()
    if not success:
        return 0, prev_frame
        
    current_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    activity = 0
    
    if prev_frame is not None:
        diff = cv2.absdiff(current_gray, prev_frame)
        _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
        activity = cv2.countNonZero(thresh)
        
    return activity, current_gray