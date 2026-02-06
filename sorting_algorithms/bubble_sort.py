import random

MIN: int = 100
MAX: int = 2000


def bubble_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the bubble sort algorithm.

    This algorithm repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The pass through the list is
    repeated until no swaps are needed. Uses an early termination optimization
    to stop when the list is already sorted.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> bubble_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64]

    :Time Complexity:
        - Best: O(n) - when the list is already sorted (early termination).
        - Average: O(n^2).
        - Worst: O(n^2) - when the list is sorted in reverse order.
    :Space Complexity: O(1) - sorts in-place.
    """
    swapped: bool = True
    swap_counter: int = 0

    while swapped:
        swapped = False

        for index in range(0, len(collection) - 1 - swap_counter):
            if collection[index] > collection[index + 1]:
                collection[index], collection[index + 1] = (
                    collection[index + 1],
                    collection[index],
                )
                swapped = True

        swap_counter += 1


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    bubble_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
