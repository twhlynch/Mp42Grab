try:
    import sys
    import json
    import itertools
    import cv2
    import numpy as np
except ImportError:
    print("Error: Did you forget to run 'bin/pip install -r requirements.txt'?")
    sys.exit(1)

def videoToPixelArray(path, x_len, y_len):
    video = cv2.VideoCapture(path)
    pixel_array = []
    
    while True:
        
        ret, frame = video.read()
        if not ret:
            break
        
        resized_frame = cv2.resize(frame, (x_len, y_len), interpolation=cv2.INTER_AREA)
        gray_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
        
        normalized_frame = gray_frame.astype(np.float32) / 255.0
        
        pixel_array.append(normalized_frame.tolist())
    
    video.release()
    
    pixel_list = np.array(pixel_array).tolist()
    
    return pixel_list

def createNodeForPixel(x, y, pixels):
    node = {
        "levelNodeStatic": {
            "material": 8,
            "color1": {
                "a": 1
            },
            "position": {
                "x": x,
                "y": y
            },
            "rotation": {
                "w": 1
            },
            "scale": {
                "x": 1,
                "y": 1,
                "z": 1
            },
            "shape": 1001
        },
        "animations": [
            {
                "frames": [
                    {
                        "position": {},
                        "rotation": {
                            "w": 1.0
                        }
                    }
                ],
                "name": "idle",
                "speed": 1
            }
        ]
    }

    time = 0
    for state in pixels:
        time += 0.04
        
        frame = {
            "position": {
                "z": round(state[y][x] / 2, 3)
            },
            "rotation": {
                "w": 1
            },
            "time": time
        }
        
        node['animations'][0]['frames'].append(frame)

    return node

def pixelsToLevelJSON(pixels, x_len, y_len):
    level = {
        "ambienceSettings": {
            "skyHorizonColor": {
                "a": 1.0,
                "b": 0.9574,
                "g": 0.9574,
                "r": 0.916
            },
            "skyZenithColor": {
                "a": 1.0,
                "b": 0.73,
                "g": 0.476,
                "r": 0.28
            },
            "sunAltitude": 45.0,
            "sunAzimuth": 315.0,
            "sunSize": 1.0
        },
        "formatVersion": 7,
        "levelNodes": [],
        "maxCheckpointCount": 10,
        "title": "VIDEO BY .INDEX"
    }
    
    for x, y in itertools.product(range(x_len), range(y_len)):
        node = createNodeForPixel(x, y, pixels)
        level['levelNodes'].append(node)

    return level

def main():
    args = sys.argv
    
    video_path = 'video.mp4'
    x, y = 30, 30
    
    if len(args) > 1: video_path = args[1]
    if len(args) > 2: x = int(args[2])
    if len(args) > 3: y = int(args[3])
    
    print(f"Running on {video_path} at {x}x{y}..")
    
    pixels_json = videoToPixelArray('video.mp4', x, y)
    print('Read video data\nConverting to JSON..')
    
    level_json = pixelsToLevelJSON(pixels_json, x, y)
    print('Converted to level JSON\nWriting JSON file..')
    
    output_file = 'video_level.json'
    with open(output_file, 'w') as f:
        json.dump(level_json, f)

    print('Created video_level.json')

if __name__ == '__main__':
    main()