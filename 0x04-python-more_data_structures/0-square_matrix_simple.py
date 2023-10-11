#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for out in matrix:
        innerMatrix = []
        for inner in range(len(out)):
            innerMatrix.append(out[inner] ** 2)
        newMatrix.append(innerMatrix)
    print(len(newMatrix))
