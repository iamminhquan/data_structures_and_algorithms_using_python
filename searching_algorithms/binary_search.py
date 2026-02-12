import random

MIN: int = 100
MAX: int = 2000


def binary_search(collection: list[int], target: int) -> int:
    """
    Search for a target value in a sorted list using the binary search algorithm.

    This algorithm repeatedly divides the search interval in half. It compares the
    target value to the middle element of the list. If they are equal, the search
    is complete. If the target is smaller, the search continues on the left half;
    if larger, on the right half.

    The input list must be sorted in ascending order for binary search to work
    correctly.

    :param collection: The sorted list of integers to search through.
    :type collection: list[int]
    :param target: The value to search for.
    :type target: int
    :return: The index of the target if found, otherwise -1.
    :rtype: int

    :Example:

    >>> binary_search([11, 15, 23, 45, 70], 45)
    3
    >>> binary_search([11, 15, 23, 45, 70], 99)
    -1

    :Time Complexity: O(log n) in the best, average, and worst case.
    :Space Complexity: O(1) - no extra space used.
    """
    left_index: int = 0
    right_index: int = len(collection) - 1

    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_element: int = collection[middle_index]

        if middle_element == target:
            return middle_index

        if middle_element < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1

    return -1


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    collection.sort()
    print(collection)

    target: int = int(input())

    result: int = binary_search(collection, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in collection")


if __name__ == "__main__":
    main()
