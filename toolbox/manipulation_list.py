def rotate_matrix(matrix, direction):
    def rotate_right(matrix_):
        return [list(tuple_) for tuple_ in list(zip(*reversed(matrix_)))]

    if direction == 'right':
        return rotate_right(matrix)
    if direction == 'down':
        return rotate_right(rotate_right(matrix))
    if direction == 'left':
        return rotate_right(rotate_right(rotate_right(matrix)))
    if direction == 'up':
        return matrix
