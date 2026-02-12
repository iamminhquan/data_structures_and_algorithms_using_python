import random

MIN: int = 100
MAX: int = 2000


def recursive_binary_search(
    collection: list[int], target: int, left_index: int, right_index: int
) -> int:
    """
    Search for a target value in a sorted list using the recursive binary search algorithm.

    This algorithm recursively divides the search interval in half. It compares the
    target value to the middle element of the current interval. If they are equal,
    the search is complete. If the target is smaller, the search continues on the
    left half; if larger, on the right half.

    The input list must be sorted in ascending order for binary search to work
    correctly.

    :param collection: The sorted list of integers to search through.
    :type collection: list[int]
    :param target: The value to search for.
    :type target: int
    :param left_index: The left boundary of the current search interval.
    :type left_index: int
    :param right_index: The right boundary of the current search interval.
    :type right_index: int
    :return: The index of the target if found, otherwise -1.
    :rtype: int

    :Example:

    >>> recursive_binary_search([11, 15, 23, 45, 70], 45, 0, 4)
    3
    >>> recursive_binary_search([11, 15, 23, 45, 70], 99, 0, 4)
    -1

    :Time Complexity: O(log n) in the best, average, and worst case.
    :Space Complexity: O(log n) due to recursive call stack.
    """
    if left_index > right_index:
        return -1

    middle_index: int = (left_index + right_index) // 2
    middle_element: int = collection[middle_index]

    if middle_element == target:
        return middle_index

    if middle_element < target:
        return recursive_binary_search(
            collection, target, middle_index + 1, right_index
        )

    return recursive_binary_search(collection, target, left_index, middle_index - 1)


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    collection.sort()
    print(collection)

    target: int = int(input())

    result: int = recursive_binary_search(collection, target, 0, len(collection) - 1)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in collection")


if __name__ == "__main__":
    main()
