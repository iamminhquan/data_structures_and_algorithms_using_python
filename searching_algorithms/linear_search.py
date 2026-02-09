import random

MIN: int = 100
MAX: int = 2000


def linear_search(collection: list[int], target: int) -> int:
    """
    Search for a target value in a list using the linear search algorithm.

    This algorithm sequentially checks each element in the list from the
    beginning until the target is found or the entire list has been traversed.

    :param collection: The list of integers to search through.
    :type collection: list[int]
    :param target: The value to search for.
    :type target: int
    :return: The index of the target if found, otherwise -1.
    :rtype: int

    :Example:

    >>> linear_search([10, 23, 45, 70, 11, 15], 70)
    3
    >>> linear_search([10, 23, 45, 70, 11, 15], 99)
    -1

    :Time Complexity: O(n) in the worst and average case, O(1) in the best case.
    :Space Complexity: O(1) - no extra space used.
    """
    for index, element in enumerate(collection):
        if element == target:
            return index

    return -1


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    target: int = int(input())

    result: int = linear_search(collection, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in collection")


if __name__ == "__main__":
    main()
