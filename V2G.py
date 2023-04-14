import cv2
import json
import numpy as np
import sys

# Parse command-line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input video file
cap = cv2.VideoCapture(input_file)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error opening video file")
    sys.exit()

# Get the original frame rate and resolution
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the desired resolution and frame rate
desired_width = 20
desired_height = 20
desired_fps = 10

# Check if resizing is necessary
if width > desired_width or height > desired_height or fps > desired_fps:
    # Resizing is necessary
    print(f"Warning: resizing from {width}x{height} at {fps} fps to {desired_width}x{desired_height} at {desired_fps} fps")
else:
    # Resizing is not necessary
    print(f"Warning: video is already at {width}x{height} at {fps} fps")

# Calculate the resize ratio
resize_ratio = min(desired_width / width, desired_height / height)

# Calculate the new width and height after resizing
new_width = int(width * resize_ratio)
new_height = int(height * resize_ratio)

# Initialize an empty list to hold the grayscale frames
grayscale_frames = []

# Loop over all the frames in the video
while True:
    # Read the next frame from the video file
    ret, frame = cap.read()

    # Break if the frame could not be read
    if not ret:
        break

    # Resize the frame
    frame = cv2.resize(frame, (new_width, new_height))

    # Convert the frame to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Normalize the pixel values to the range [0, 1]
    frame_gray = frame_gray / 255.0

    # Append the grayscale frame to the list
    grayscale_frames.append(frame_gray.tolist())

# Release the video file
cap.release()

# Convert the list of grayscale frames to a JSON string
json_str = json.dumps(grayscale_frames)

# Write the JSON string to the output file
with open(output_file, "w") as f:
    f.write(json_str)
