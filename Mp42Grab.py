import cv2, json
import numpy as np
from google.protobuf import json_format
from generated import types_pb2, level_pb2

def createLevel(data, outputFile):
    level = level_pb2.Level()
    json_format.Parse(data, level)
    with open(outputFile, "wb") as f:
        f.write(level.SerializeToString())

def videoToPixelArray(path):
    video = cv2.VideoCapture(path)
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
    return pixel_array.tolist()

def pixelsToLevelJSON(pixels):
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
        "complexity": 0,
        "formatVersion": 7,
        "levelNodes": [],
        "maxCheckpointCount": 10,
        "title": "VIDEO BY .INDEX"
    }
    for x in range(30):
        for y in range(30):
            current = {
                "levelNodeStatic": {
                    "color": {
                        "a": 1.0,
                        "b": 0.001,
                        "g": 0.001,
                        "r": 0.001
                    },
                    "material": 8,
                    "position": {
                        "x": x,
                        "y": y
                    },
                    "rotation": {
                        "w": 1.0
                    },
                    "scale": {
                        "x": 1.0,
                        "y": 1.0,
                        "z": 1.0
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
                        "speed": 0.04
                        
                    }
                ]
            }
            time = 0
            for state in pixels:
                time += 1
                frame = {
                    "position": {
                        "z": round(state[y][x], 3)
                    },
                    "rotation": {
                        "w": 1.0
                    },
                    "time": round(time, 2)
                }
                current['animations'][0]['frames'].append(frame)
            level['levelNodes'].append(current)
            print(str(x)+','+str(y))
            print(len(current['animations'][0]['frames']))

    return level

pixels_json = videoToPixelArray('video.mp4')
level_json = pixelsToLevelJSON(pixels_json)
createLevel(json.dumps(level_json), 'video.level')
