import cv2

def process_video(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    average_brightness = gray_frame.mean()
    return average_brightness
