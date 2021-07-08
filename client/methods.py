from .matrix import Matrix
from json import loads
from methods import get_int


# ------------------------- Mathematical Operations Of Matrices ------------------------- #
# Add Two Matrix nxn
def add_matrix(matrix_01, matrix_02):
    row = matrix_01.get_dimension()

    # Create 0 Array For Result
    result = [[0 for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            result[i][j] = matrix_01.matrix[i][j] + matrix_02.matrix[i][j]

    return Matrix(result)


# Add Two Matrix nxn
def subtract_matrix(matrix_01, matrix_02):
    row = matrix_01.get_dimension()

    # Create 0 Array For Result
    result = [[0 for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            result[i][j] = matrix_01.matrix[i][j] - matrix_02.matrix[i][j]

    return Matrix(result)


# Normal Multiply Two Matrix nxn
def multiply_matrix(matrix_01, matrix_02):
    row = matrix_01.get_dimension()

    # Create 0 Array For Result
    result = [[0 for _ in range(row)] for _ in range(row)]

    for i in range(row):
        for j in range(row):
            for k in range(row):
                result[i][j] += (matrix_01.matrix[i][k] * matrix_02.matrix[k][j])

    return Matrix(result)


# ------------------------- Split Or Concat Matrices ------------------------- #
# Split Matrix To 4 Matrix 11, 12, 21, 22
def split_matrix(matrix_obj):
    matrix_11, matrix_12, matrix_21, matrix_22 = [], [], [], []

    row = matrix_obj.get_dimension()
    row_half = row // 2

    for i in range(row_half):
        matrix_11.append(matrix_obj.matrix[i][:row_half])
        matrix_12.append(matrix_obj.matrix[i][row_half:])

    for i in range(row_half, row):
        matrix_21.append(matrix_obj.matrix[i][:row_half])
        matrix_22.append(matrix_obj.matrix[i][row_half:])

    return Matrix(matrix_11), Matrix(matrix_12), Matrix(matrix_21), Matrix(matrix_22)


# Concat 4 Matrix To Create Result
def concat_matrices(matrix_11, matrix_12, matrix_21, matrix_22):
    matrix = []

    for i in range(matrix_11.get_dimension()):
        matrix.append(matrix_11.matrix[i] + matrix_12.matrix[i])

    for i in range(matrix_21.get_dimension()):
        matrix.append(matrix_21.matrix[i] + matrix_22.matrix[i])

    return Matrix(matrix)


# ------------------------- Interact With Client CLI ------------------------- #
# To Create Matrix With User Input
def get_matrix_from_user(name):
    row = get_int(f'Enter {name} Row Number')
    print('----- Separate Elements By Comma (,) -----')

    matrix = []
    for i in range(row):
        row_elements = input(f'Input Row({i + 1}): ').replace(' ', '').split(',')
        matrix.append([int(element) for element in row_elements])

    return Matrix(matrix)


# Read Matrix From File With Name
def read_matrix_from_file():
    file_name = get_int("Enter File Number (1, 2, 3, 4) ")

    file = open(f'./client/files/{file_name}.txt', 'r')

    data = file.read()
    data = loads(data)

    return Matrix(data[0]), Matrix(data[1])
