""" Filtering

3. Using filter - reduce the list to only odd values with the is_odd predicate. """


def is_odd(n: int) -> bool:
    """ Predicate for use with filter """
    return n % 2 != 0


if __name__ == '__main__':
    arr = list(range(10))
    print(arr)
    print(list(filter(is_odd, arr)))
