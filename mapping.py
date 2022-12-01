""" Mapping

2. Using map - alter the values of the list with the add_one transformer. """


def add_one(n: int) -> int:
    """ Transformer for use with map """
    return n + 1


if __name__ == '__main__':
    arr = list(range(10))
    print(arr)
    print(list(map(add_one, arr)))
