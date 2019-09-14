def afficher_x_nombres_decimaux(n):
    print('{0:.3f}'.format(n)) # Afficher 3 chiffres après la virgule


def ecart_age_exercice(m, n, y):
    """
    M, N et Y sont donnés. Il y a Y années, Alice était M fois plus agée que Bob. Aujourd'hui, ils ont N années d'écart. Quels sont les âges
    d'Alice et Bob ?
    """
    alice_age = (m*(-n-y) +y)/(1-m)
    bob_age = alice_age - n
    return int(alice_age), int(bob_age)


def int_to_binary(integer_input):
    return "{0:b}".format(integer_input)


def int_to_hex(integer_input):
    # return hex(integer_input)  # --> '0x9f
    return "{0:x}".format(integer_input)  # --> '9f'


def annee_bissextile(year):
    """
    Une année bissextile (contient 366 jours) si elle est multiple de 4, sauf les années de début de siècle (qui se terminent par 00) qui ne sont
    bissextiles que si elles sont divisibles par 400
    """
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0)


if __name__ == '__main__':
    print('{0:.5f}'.format(5))
    print([[1, 2, 3], [4, 5, 6]])
    print(ecart_age_exercice(3, 14, 18))
    print(int_to_binary(37))
    print(sum([int(elem) for elem in int_to_binary(37)]))
    print(int_to_hex(159))
    print(annee_bissextile(2020))

