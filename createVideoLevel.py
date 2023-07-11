import json

WIDTH = 30
HEIGHT = 30
FPS = 24
INCREMENT = 0.04166666666

with open('pixel_data.json') as f:
    arr = json.load(f)
    FRAMES = len(arr)

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
    "maxCheckpointCount": 420,
    "title": "BAD APPLE"
}
cube = {
    "levelNodeStatic": {
        "color": {
            "a": 1.0,
            "b": 0.0000024,
            "g": 0.0000024,
            "r": 0.0000024
        },
        "material": "DEFAULT_COLORED",
        "position": {
            "x": 1.0,
            "y": 1.0,
            "z": 1.0
        },
        "rotation": {
            "w": 1.0
        },
        "scale": {
            "x": 1.0,
            "y": 1.0,
            "z": 1.0
        },
        "shape": "CUBE"
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
            "name": "idle"
        }
    ]
}
for x in range(WIDTH):
    for y in range(HEIGHT):
        current = {
    "levelNodeStatic": {
        "color": {
            "a": 1.0,
            "b": 0.0000024,
            "g": 0.0000024,
            "r": 0.0000024
        },
        "material": "DEFAULT_COLORED",
        "position": {
            "x": x,
            "y": y,
            "z": 1.0
        },
        "rotation": {
            "w": 1.0
        },
        "scale": {
            "x": 1.0,
            "y": 1.0,
            "z": 1.0
        },
        "shape": "SPHERE"
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
            "name": "idle"
        }
    ]
}
        time = 0.01
        for state in arr:
            time += INCREMENT
            frame = {
                "position": {
                    "z": state[y][x]
                },
                "rotation": {
                    "w": 1.0
                },
                "time": round(time, 2)
            }
            current['animations'][0]['frames'].append(frame)
        level['levelNodes'].append(current)
        print(str(x)+','+str(y))
        print(len(json.dumps(current)))

with open('video.json', 'w') as f:
    json.dump(level, f)







