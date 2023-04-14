#!/usr/bin/env python3

import sys
import json
from google.protobuf import json_format
from generated import types_pb2, level_pb2

def main():
	if len(sys.argv) < 3:
		print('python3 ConvertToJSON.py input.level output.json')
		return

	levelData = {}

	with open(sys.argv[1], 'rb') as inputFile:
		level = level_pb2.Level()
		level.ParseFromString(inputFile.read())
		levelData = json_format.MessageToDict(level)

	with open(sys.argv[2], "w") as outputFile:
		outputFile.write(json.dumps(levelData, sort_keys=True, indent=4))

if __name__ == '__main__':
	main()
