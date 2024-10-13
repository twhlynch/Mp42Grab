# Mp42Grab

Put videos into GRAB!

Recommended to use videos less than 1 minute long, and dimensions of 30x30.

### Setup

- Get [Python](https://www.python.org/).
- Run `python3 -m venv .` to initialize a python environment.
- Run `bin/pip install -r requirements.txt` to install requirements.

### Run

- Run `bin/python Mp42Grab.py VIDEO.mp4 XX YY`

> VIDEO is the path to the mp4 file.
> 
> XX is the number of pixels to generate across the x axis
> 
> YY is the number of pixels to generate across the y axis

### Usage

The script should output file called `video_level.json`. You can convert it to a level file with any json to level tool such as any of the following tools:

- [JSON editor]()

> View > Performance > Toggle editor
> 
> File > Open > JSON File

- [Level JSON Tool](https://grab-tools.live/tools?tab=JSONButton)

- [Slin/GRAB-Level-Format](https://github.com/Slin/GRAB-Level-Format/tree/main) (main/tools)