import cv2
import time
import os
# Open the video file

cap = cv2.VideoCapture('testing.mp4')

# Create a directory to store the captured images
output_directory = 'output_images'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get video frame rate
frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

# Set interval to capture (in seconds)
capture_interval = 2

# Start capturing frames
frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame_count += 1
    
    # Capture and save frame every `capture_interval` seconds
    if frame_count % (frame_rate * capture_interval) == 0:
        image_filename = f"{output_directory}/frame_{frame_count}.jpg"
        cv2.imwrite(image_filename, frame)
        print(f"Captured frame {frame_count} at {time.strftime('%H:%M:%S')}")
    
    # Display the captured frame (optional)
    cv2.imshow('Frame', frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
