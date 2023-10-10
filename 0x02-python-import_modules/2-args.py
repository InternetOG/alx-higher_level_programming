#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) > 1:
        print("{:d} argument:".format((len(argv) - 1)))
    for i in range(len(argv)):
        if i > 0:
            print("{:d}: {:s}".format(i, argv[i]))
