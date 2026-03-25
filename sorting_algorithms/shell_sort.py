import random

MIN: int = 100
MAX: int = 2000


def shell_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the Shell sort algorithm.

    Shell sort is an optimization of insertion sort that allows exchanges of
    elements far apart. It repeatedly performs a "gapped" insertion sort with
    a decreasing gap size until the gap becomes 1 (regular insertion sort).

    This implementation uses a simple gap sequence: n//2, n//4, ..., 1.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> shell_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64]

    :Time Complexity:
        - Best: O(n log n) for some gap sequences (depends on data and gaps).
        - Average: depends on the chosen gap sequence.
        - Worst: O(n^2) for the simple halving gap sequence used here.
    :Space Complexity: O(1) - sorts in-place.
    """

    n: int = len(collection)
    if n <= 1:
        return

    gap: int = n // 2
    while gap > 0:
        for index in range(gap, n):
            current_value: int = collection[index]
            position: int = index

            while (
                position >= gap
                and collection[position - gap] > current_value
            ):
                collection[position] = collection[position - gap]
                position -= gap

            collection[position] = current_value

        gap //= 2


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    shell_sort(collection)
    print(collection)

    assert collection == sorted(collection)
    print("Ascending")


if __name__ == "__main__":
    main()
