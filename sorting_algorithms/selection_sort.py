import random

MIN: int = 100
MAX: int = 2000


def selection_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the selection sort algorithm.

    This algorithm divides the list into a sorted and unsorted region. It repeatedly
    selects the smallest element from the unsorted region and moves it to the end
    of the sorted region.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 25, 12, 22, 11]
    >>> selection_sort(arr)
    >>> arr
    [11, 12, 22, 25, 64]

    :Time Complexity: O(n^2) in all cases (best, average, worst).
    :Space Complexity: O(1) - sorts in-place.
    :Note: Selection sort makes fewer swaps than interchange sort (at most n-1 swaps).
    """
    for i in range(len(collection) - 1):
        min_index = i

        for j in range(i + 1, len(collection)):
            if collection[min_index] > collection[j]:
                min_index = j

        if min_index != i:
            collection[i], collection[min_index] = collection[min_index], collection[i]


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    selection_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
