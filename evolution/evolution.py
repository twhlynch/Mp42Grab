import cv2, json
import numpy as np
from google.protobuf import json_format
from generated import types_pb2, level_pb2
from random import randint

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
        resized_frame = cv2.resize(frame, (200, 200), interpolation=cv2.INTER_AREA)
        pixel_array.append(resized_frame.tolist())
    video.release()
    pixel_array = np.array(pixel_array)
    return pixel_array.tolist()

def generate_json(pixels):
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
    # find most common colors
    colors = {}
    for frame in pixels:
        frame_colors = {}
        for row in frame:
            for pixel in row:
                if tuple(pixel) not in frame_colors:
                    frame_colors[tuple(pixel)] = 0
                frame_colors[tuple(pixel)] += 1
        frame_colors = sorted(frame_colors.items(), key=lambda x: x[1], reverse=True)
        for i in range(5):
            color = frame_colors[i][0]
            if color not in colors:
                colors[color] = 0
            colors[color] += 1
        

    # sort colors by most common
    colors = sorted(colors.items(), key=lambda x: x[1], reverse=True)

    for i in range(20):
        color = colors[i][0]

        for j in range(10):
            circle = {
                "levelNodeStatic": {
                    "material": 8,
                    "color": {
                        "a": 1,
                        "b": color[0]/255,
                        "g": color[1]/255,
                        "r": color[2]/255
                    },
                    "position": {
                        "x": 0,
                        "y": 0,
                        "z": 0
                    },
                    "rotation": {
                        "w": 1
                    },
                    "scale": {
                        "x": j*10,
                        "y": j*10,
                        "z": j*10
                    }
                }
            }

            level["levelNodes"].append(circle)

    final_frames = []

    for frame in pixels:
        
        frame_options = []
        for i in range(10): # frame attempts

            frame_attempts = []
            for j in range(100):

                objs = []
                objs_similarity = 0
                for k in range(10):

                    obj = randint(0, len(level["levelNodes"]))
                    random_position = {
                        "x": randint(0, 200),
                        "y": randint(0, 200),
                        "z": 0
                    }
                    node = level["levelNodes"][obj]
                    # node["levelNodeStatic"]["position"] = random_position
                    objs.append({
                        "object": node,
                    })
                
                # fun image stuff
                objs_similarity += 1

                frame_attempts.append({
                    "object": objs,
                    "similarity": objs_similarity
                })

            # save most similar attempt
            most_similar = frame_attempts[0]
            for attempt in frame_attempts:
                if attempt["similarity"] > most_similar["similarity"]:
                    most_similar = attempt

            frame_options.append(most_similar["object"])
        
        # save most similar frame
        most_similar = frame_options[0]
        for option in frame_options:
            if option["similarity"] > most_similar["similarity"]:
                most_similar = option
        
        final_frames.append(most_similar["object"])

        # make work for grab

    return level

pixels_json = videoToPixelArray('video.mp4')
level_json = generate_json(pixels_json)
createLevel(json.dumps(level_json), 'video.level')