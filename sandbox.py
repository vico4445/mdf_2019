def rotate_matrix(matrix, direction):
    def rotate_right(matrix):
        return [list(tuple_) for tuple_ in list(zip(*reversed(matrix)))]

    if direction == 'right':
        return rotate_right(matrix)
    if direction == 'down':
        return rotate_right(rotate_right(matrix))
    if direction == 'left':
        return rotate_right(rotate_right(rotate_right(matrix)))
    if direction == 'up':
        return matrix


def print_matrice(matrix):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print_matrice(matrix)

    print('''''')
    mat = rotate_matrix(matrix, direction='right')
    print_matrice(mat)

    print('''''')
    mat = rotate_matrix(matrix, direction='left')
    print_matrice(mat)

    print('''''')
    mat = rotate_matrix(matrix, direction='down')
    print_matrice(mat)

    print('''''')
    mat = rotate_matrix(matrix, direction='up')
    print_matrice(mat)

