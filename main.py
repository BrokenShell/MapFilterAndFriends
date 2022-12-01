""" Introduction: Map & Filter
What do the implementations for Map and Filter look like under the hood?
While it is unwise to implement these ourselves, it can be helpful to see how
these builtins work.

1. Define the most likely implementations for Map and Filter. """
from typing import Callable, Iterable, Iterator


def my_map(transform: Callable, iterable: Iterable) -> Iterator:
    return (transform(item) for item in iterable)


def my_filter(predicate: Callable, iterable: Iterable) -> Iterator:
    return (item for item in iterable if predicate(item))


if __name__ == '__main__':
    arr = range(10)
    result = my_map(lambda x: x+1, arr)
    print(*result)
