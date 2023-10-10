#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    if len(argv) < 2:
        print("{}".format("0 arguments."))
    elif len(argv) > 1:
        print("{} argument:".format((len(argv) - 1)))
        for i in range(len(argv)):
            if i > 0:
                print("{}: {}".format(i, argv[i]))
