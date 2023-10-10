#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    result = 0

    for i in range(len(argv)):
        if i > 0:
            result += int(argv[i])
    return result
