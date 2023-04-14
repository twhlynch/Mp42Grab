#!/usr/bin/env python3

import sys
import json
from google.protobuf import json_format
from generated import types_pb2, level_pb2

def main():
	if len(sys.argv) < 3:
		print('python3 ConvertToLevel.py input.json output.level')
		return

	level = level_pb2.Level()
	with open(sys.argv[1], 'r') as inputFile:
		json_format.Parse(inputFile.read(), level)

	with open(sys.argv[2], "wb") as outputFile:
		outputFile.write(level.SerializeToString())


if __name__ == '__main__':
	main()
