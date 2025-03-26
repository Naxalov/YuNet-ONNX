import cv2

# Capture the video from the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open the webcam.")
    exit()

# Get the width and height of the frame
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Print the width and height of the frame
print(f'Width: {width}, Height: {height}')

# Release the webcam
cap.release()
print("Webcam released successfully.")


