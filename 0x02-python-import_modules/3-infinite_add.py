#!/usr/bin/python3
def sumM(arr):
    result = 0
    for i in arr:
        result += int(i)
    return result


if __name__ == "__main__":
    import sys

    argv = sys.argv
    result = 0
    arr = []
    for i in range(len(argv)):
        if i > 0:
            arr.append(argv[i])
    print("{}".format(sumM(arr)))
