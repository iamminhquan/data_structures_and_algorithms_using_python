import random

MIN: int = 100
MAX: int = 2000


def _radix_sort_non_negative(arr: list[int]) -> list[int]:
    """
    Radix sort for non-negative integers.

    Uses base 10 and a stable counting-sort per digit.
    """
    if len(arr) <= 1:
        return arr.copy()

    max_value: int = max(arr)
    exp: int = 1  # 1, 10, 100, ...
    output: list[int] = arr

    while max_value // exp > 0:
        counts: list[int] = [0] * 10

        for value in output:
            digit: int = (value // exp) % 10
            counts[digit] += 1

        for i in range(1, 10):
            counts[i] += counts[i - 1]

        next_output: list[int] = [0] * len(output)
        for i in range(len(output) - 1, -1, -1):
            digit = (output[i] // exp) % 10
            counts[digit] -= 1
            next_output[counts[digit]] = output[i]

        output = next_output
        exp *= 10

    return output


def radix_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the Radix sort algorithm.

    This implementation uses base 10. Since Radix sort naturally works with
    non-negative integers, it handles negative values by:
    - sorting the absolute values of negatives with radix sort
    - reversing the negative part after converting back to negatives

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:
    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> radix_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64]

    :Time Complexity:
        - Best: O(d * (n + k)) where d is number of digits.
        - Average: O(d * (n + k)).
        - Worst: O(d * (n + k)).
      Here k is the base (10).
    :Space Complexity: O(n + k) - extra space for counting and stable output.
    """
    n: int = len(collection)
    if n <= 1:
        return

    negatives_abs: list[int] = []
    non_negatives: list[int] = []

    for value in collection:
        if value < 0:
            negatives_abs.append(-value)
        else:
            non_negatives.append(value)

    sorted_non_negatives: list[int] = _radix_sort_non_negative(
        non_negatives
    )
    sorted_negatives_abs: list[int] = _radix_sort_non_negative(
        negatives_abs
    )

    # For negatives: larger absolute value means smaller actual value.
    sorted_negatives: list[int] = [-x for x in reversed(sorted_negatives_abs)]

    collection[:] = sorted_negatives + sorted_non_negatives


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    radix_sort(collection)
    print(collection)

    assert collection == sorted(collection)
    print("Ascending")


if __name__ == "__main__":
    main()