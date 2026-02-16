import random

MIN: int = 100
MAX: int = 2000


def merge(left: list[int], right: list[int]) -> list[int]:
    """
    Merge two sorted lists into a single sorted list.

    :param left: The first sorted list.
    :param right: The second sorted list.
    :return: A new sorted list containing all elements from both lists.
    """
    result: list[int] = []
    i: int = 0
    j: int = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(collection: list[int]) -> list[int]:
    """
    Sort a list of integers in ascending order using the merge sort algorithm.

    This algorithm uses the divide-and-conquer strategy: it divides the list into
    two halves, recursively sorts each half using merge sort, then merges the two
    sorted halves into a single sorted list.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: A new sorted list. Does not modify the original list.
    :rtype: list[int]

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> merge_sort(arr)
    [11, 12, 22, 25, 34, 64]

    :Time Complexity: O(n log n) in all cases (best, average, worst).
    :Space Complexity: O(n) - additional space for temporary arrays during merge.
    :Note: Merge sort is a stable sort (preserves relative order of equal elements).
    """
    if len(collection) <= 1:
        return collection.copy()

    mid: int = len(collection) // 2
    left: list[int] = merge_sort(collection[:mid])
    right: list[int] = merge_sort(collection[mid:])

    return merge(left, right)


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    collection[:] = merge_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
