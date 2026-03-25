import random

MIN: int = 100
MAX: int = 2000


def gnome_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the gnome sort algorithm.

    Gnome sort is similar to insertion sort, but it uses a "gnome" walk:
    it moves forward while elements are in the correct order; otherwise it
    swaps the out-of-order elements and steps back.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> gnome_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64]

    :Time Complexity:
        - Best: O(n) - when the list is already sorted.
        - Average: O(n^2).
        - Worst: O(n^2) - when the list is sorted in reverse order.
    :Space Complexity: O(1) - sorts in-place.
    """
    index: int = 0
    n: int = len(collection)

    if n <= 1:
        return

    while index < n:
        if index == 0 or collection[index] >= collection[index - 1]:
            index += 1
        else:
            collection[index], collection[index - 1] = (
                collection[index - 1],
                collection[index],
            )
            index -= 1


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    gnome_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()