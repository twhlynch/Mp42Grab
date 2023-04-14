import cv2
import numpy as np

# Define the video dimensions
width = 100
height = 100
fps = 30

# Create a VideoWriter object to output the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('black_white_screen.mp4', fourcc, fps, (width, height), isColor=True)

# Create a black image and a white image to use as frames
black_frame = 255 * np.zeros((height, width, 3), dtype=np.uint8)
white_frame = 255 * np.ones((height, width, 3), dtype=np.uint8)

# Write the black and white frames to the output video
for i in range(4):
    if i % 2 == 0:
        out.write(black_frame)
    else:
        out.write(white_frame)

# Release the output video and close any windows
out.release()
cv2.destroyAllWindows()
