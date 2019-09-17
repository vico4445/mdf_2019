import sys


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


def print_matrice(matrice):
    for l in matrice:
        sys.stdout.write((' '.join(map(str, l)) + '\n'))


def neighbor_tab(tab, i, j):
    """
        A partir de coordonnées (i, j), je valide que je suis bien dans le tableau et je donne tous les voisins valides
    """
    # Index Voisin en croix
    n = len(tab)
    m = len(tab[0])

    l = []
    for k in {-1,1}:
        if (i + k) % n == i + k:
            l += [(i+k,j)]

        if (j + k) % m == j + k:
            l += [(i,j+k)]
    return l


def neighbor_diag(tab, i, j):
    # Index Voisin en diagonal
    n = len(tab)
    m = len(tab[0])

    l = []
    for k in {-1,1}:
        for il in {-1,0,1}:
            if (i + k) % n == i + k and (j + il) % m == j + il:
                l += [(i+k,j+il)]

        if (j + k) % m == j + k:
            l += [(i,j+k)]

    return l


def get_next_elem(tab, i, j, i_previous, j_previous, direction='left'):
    """
        From two previous points in matrice, get next point in wanted direction
    :param tab: matrice
    :param i: actual point x
    :param j: actual point y
    :param i_previous: previous point x
    :param j_previous: previous point y
    :param direction: <'left', 'right', 'front''>
    :return:
    """
    x, y = i - i_previous, j - j_previous
    if direction == 'left':
        elem = (i - y, j + x)
    elif direction == 'right':
        elem = (i + y, j - x)
    elif direction == 'front':
        elem = (i + x, j + y)
    else:
        raise
    if elem[0] >= len(tab) or elem[0] < 0 or elem[1] >= len(tab[0]) or elem[1] < 0:
        return None
    return elem


def manipulation_list_example():
    l = [12, 9, 5, 8]
    print(l.index(min(l)))


if __name__ == '__main__':
    tab = [[3, 3, 4], [4, 2, 1], [4, 2, 1], [4, 2, 1]]
    print_matrice(tab)
    print(neighbor_tab(tab, 1, 1))
    print(neighbor_diag(tab, 1, 1))
    manipulation_list_example()
