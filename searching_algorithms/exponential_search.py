import random

MIN: int = 100
MAX: int = 2000


def exponential_search(collection: list[int], target: int) -> int:
    """
    Search for a target value in a sorted list using the exponential search algorithm.

    This algorithm first finds a range where the target might exist by jumping
    ahead in exponentially increasing steps (1, 2, 4, 8, ...). Once a bound is
    found, it performs binary search within that range.

    The input list must be sorted in ascending order. Exponential search is
    particularly useful when the target is likely to be near the beginning.

    :param collection: The sorted list of integers to search through.
    :type collection: list[int]
    :param target: The value to search for.
    :type target: int
    :return: The index of the target if found, otherwise -1.
    :rtype: int

    :Example:

    >>> exponential_search([11, 15, 23, 45, 70], 45)
    3
    >>> exponential_search([11, 15, 23, 45, 70], 99)
    -1

    :Time Complexity: O(log n) when target is in range, O(log i) where i is
        the index of target (best case O(1)).
    :Space Complexity: O(1) - no extra space used.
    """
    length: int = len(collection)
    if length == 0:
        return -1

    if collection[0] == target:
        return 0

    bound_index: int = 1
    while bound_index < length and collection[bound_index] < target:
        bound_index *= 2

    left_index: int = bound_index // 2
    right_index: int = min(bound_index, length - 1)

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

    result: int = exponential_search(collection, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in collection")


if __name__ == "__main__":
    main()
