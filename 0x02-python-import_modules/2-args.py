#!/usr/bin/python3
if __name__ == "__main__":
	sum = 0
	import sys
	for arg in range(len(sys.argv)):
		if arg == 0:
			print(f"{arg} arguments")
		elif arg == 1:
			print(f"{arg} argument")
			print(f"{arg}: {sys.argv[arg]}")
		elif arg > 1:
			print(f"{len(sys.argv)} arguments")
			print(f"{arg}: {sys.argv[arg]}")
