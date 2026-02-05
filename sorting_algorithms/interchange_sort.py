import random

MIN: int = 100
MAX: int = 2000


def interchange_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the interchange sort algorithm.

    This algorithm compares each element with all subsequent elements and swaps
    them if they are in the wrong order. Also known as naive sort or exchange sort.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11, 90]
    >>> interchange_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64, 90]

    :Time Complexity: O(n^2) in all cases (best, average, worst).
    :Space Complexity: O(1) - sorts in-place.
    """
    for i in range(len(collection) - 1):
        for j in range(i + 1, len(collection)):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    interchange_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
