import math
import random

MIN: int = 100
MAX: int = 2000


def jump_search(collection: list[int], target: int) -> int:
    """
    Search for a target value in a sorted list using the jump search algorithm.

    This algorithm jumps ahead in fixed block sizes (sqrt of list length) instead
    of checking every element. Once a block is found where the target might exist
    (current element >= target or end of list), it performs linear search within
    that block.

    The input list must be sorted in ascending order for jump search to work
    correctly.

    :param collection: The sorted list of integers to search through.
    :type collection: list[int]
    :param target: The value to search for.
    :type target: int
    :return: The index of the target if found, otherwise -1.
    :rtype: int

    :Example:

    >>> jump_search([11, 15, 23, 45, 70], 45)
    3
    >>> jump_search([11, 15, 23, 45, 70], 99)
    -1

    :Time Complexity: O(sqrt n) - jumps of sqrt(n) plus linear search in one block.
    :Space Complexity: O(1) - no extra space used.
    """
    length: int = len(collection)
    if length == 0:
        return -1

    block_size: int = int(math.sqrt(length))
    prev_index: int = 0
    step_index: int = 0

    while step_index < length and collection[step_index] < target:
        prev_index = step_index
        step_index = min(step_index + block_size, length)

    end_index: int = min(step_index + 1, length)
    for index in range(prev_index, end_index):
        if collection[index] == target:
            return index

    return -1


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    collection.sort()
    print(collection)

    target: int = int(input())

    result: int = jump_search(collection, target)

    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in collection")


if __name__ == "__main__":
    main()
