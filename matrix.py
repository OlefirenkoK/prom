"""Use `create_matrix` to initialize matrix with given parameters.
   Function `calculate_matrix` returns a dictionary with to keys, the first
   one is the max sum of  perpendicular columns elements, the second is the
   point of intersection those perpendicular columns.
"""


from random import randrange


SIZEX = 0
SIZEY = 0
SIZEZ = 0
sum_col_keeper = {}
_max_point = {
    'coordinates': None,
    'sum': 0
}


def create_matrix(sizex=10, sizey=10, sizez=10):
    global SIZEX, SIZEZ, SIZEY
    SIZEX, SIZEY, SIZEZ = sizex, sizey, sizez
    return [[[randrange(0, 9) for _ in range(sizex)]
        for _ in range(sizey)] for _ in range(sizez)]


def matrix_print(matrix):
    for plane in matrix:
        for line in plane:
            print(line)
        print('x ' * SIZEX)


def get_sum_perpend_col(x, y, z):
    col_x = 0
    col_y = 0
    col_z = 0
    global counter
    if ((z, y, 0), (z, y, SIZEX)) not in sum_col_keeper:
        for i in range(SIZEX):
            col_x += MATRIX[z][y][i]
        sum_col_keeper[((z, y, 0), (z, y, SIZEX))] = col_x
    else:
        counter += 1
        col_x = sum_col_keeper[((z, y, 0), (z, y, SIZEX))]
    if ((z, 0, x), (z, SIZEY, x)) not in sum_col_keeper:
        for i in range(SIZEY):
            col_y += MATRIX[z][i][x]
        sum_col_keeper[((z, 0, x), (z, SIZEY, x))] = col_y
    else:
        counter += 1
        col_y = sum_col_keeper[((z, 0, x), (z, SIZEY, x))]
    if ((0, y, x), (SIZEZ, y, x)) not in sum_col_keeper:
        for i in range(SIZEZ):
            col_z += MATRIX[i][y][x]
        sum_col_keeper[((0, y, x), (SIZEZ, y, x))] = col_z
    else:
        counter += 1
        col_z = sum_col_keeper[((0, y, x), (SIZEZ, y, x))]
    column_sum = col_x + col_y + col_z
    return column_sum


def calculate_matrix():
    for z in range(SIZEZ):
        for y in range(SIZEY):
            for x in range(SIZEX):
                sum_perpend_col = get_sum_perpend_col(x, y, z)
                if _max_point['sum'] < sum_perpend_col:
                    _max_point['coordinates'] = (x, y, z)
                    _max_point['sum'] = sum_perpend_col
    return _max_point


MATRIX = create_matrix(10, 10, 10)
matrix_print(MATRIX)
counter = 0

if __name__ == '__main__':
    print(calculate_matrix())
