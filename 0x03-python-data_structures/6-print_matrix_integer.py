#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        rowLen = len(arr)
        for num in range(len(arr)):
            if num == (rowLen - 1):
                print(f"{arr[num]}", end="")
            else:
                print(f"{arr[num]}", end=" ")
        print(end="\n")
