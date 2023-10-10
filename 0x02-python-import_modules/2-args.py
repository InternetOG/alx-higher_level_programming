#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv
    if len(argv) == 1:
        print("{}".format("0 arguments"))
    else:
        print("{} arguments".format((len(argv) - 1)))
        for arg in range(len(argv)):
            if arg > 0:
                print("{}: {}".format(arg, argv[arg]))

