import random

MIN: int = 100
MAX: int = 2000


def insertion_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the insertion sort algorithm.

    This algorithm builds the sorted list one element at a time by picking each
    element and inserting it into its correct position among the previously sorted
    elements. It is similar to how most people sort playing cards in their hands.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> insertion_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64]

    :Time Complexity:
        - Best: O(n) - when the list is already sorted.
        - Average: O(n^2).
        - Worst: O(n^2) - when the list is sorted in reverse order.
    :Space Complexity: O(1) - sorts in-place.
    """
    for index in range(1, len(collection)):
        current_value: int = collection[index]
        current_position: int = index - 1

        while current_position >= 0 and collection[current_position] > current_value:
            collection[current_position + 1] = current_value
            current_position -= 1

        collection[current_position + 1] = current_value


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    insertion_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
