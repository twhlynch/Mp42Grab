import json

with open('out.npy', 'r') as f:
    video = json.load(f)

nodes = []

TIME = 25

for frame in range(len(video)):
    print(frame)
    for row in range(len(video[frame])):
        nodes.append({
            "levelNodeGroup": {
                "scale": {
                    "x": 1.0,
                    "y": 1.0,
                    "z": 1.0
                },
                "rotation": {
                    "w": 1.0
                },
                "childNodes": [
            
                ]
            }
        })
        for pixel in range(len(video[frame][row])):
            nodes[row]["levelNodeGroup"]["childNodes"].append({
    "levelNodeStatic": {
        "color": {
            "a": 1.0,
            "b": 0.0000024,
            "g": 0.0000024,
            "r": 0.0000024
        },
        "material": "DEFAULT_COLORED",
        "position": {
            "x": 0.0,
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
            "name": "idle",
            "speed": 1.0
        }
    ]

            })

for frame in range(len(video)):
    print(frame)
    for row in range(len(video[frame])):
        for pixel in range(len(video[frame][row])):
            nodes[row]["levelNodeGroup"]["childNodes"][pixel]["animations"][0]["frames"].append({
                "position": { "x": video[frame][row][pixel] },
                "time": frame
            })
    TIME += 1/24

with open('json.json', 'x+') as json_file:
    json_file.write(json.dumps(nodes, indent=4))
