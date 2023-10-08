#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for num in range(len(arr)):
            if num == 2:
                print("{:d}".format(arr[num]), end="")
            else:
                print("{:d}".format(arr[num]), end=" ")
        print("{}".format("\n"))
