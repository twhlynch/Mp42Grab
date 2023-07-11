import cv2
import numpy as np
import json

def video_to_pixel_array(video_path):
    video = cv2.VideoCapture(video_path)
    pixel_array = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (30, 30), interpolation=cv2.INTER_AREA)
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        normalized_frame = gray_frame.astype(np.float32) / 255.0
        pixel_array.append(normalized_frame.tolist())
    video.release()
    pixel_array = np.array(pixel_array)
    return pixel_array

video_path = 'video.mp4'
pixels = video_to_pixel_array(video_path)

output_path = 'pixel_data.json'
with open(output_path, 'w') as f:
    json.dump(pixels.tolist(), f)

print(f"Pixel data saved to {output_path}")
