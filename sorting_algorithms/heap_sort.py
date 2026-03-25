import random

MIN: int = 100
MAX: int = 2000


def heap_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the heap sort algorithm.

    Heap sort first builds a max-heap from the input list. It then repeatedly
    moves the current maximum element to the end of the list and restores the
    heap property for the remaining elements.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> arr = [64, 34, 25, 12, 22, 11]
    >>> heap_sort(arr)
    >>> arr
    [11, 12, 22, 25, 34, 64]

    :Time Complexity:
        - Best: O(n log n) - building and extracting from the heap takes
          O(n log n) in all cases.
        - Average: O(n log n).
        - Worst: O(n log n).
    :Space Complexity: O(1) - sorts in-place.
    """

    n: int = len(collection)
    if n <= 1:
        return

    def sift_down(start: int, end: int) -> None:
        """
        Restore max-heap property from `start` up to `end` (inclusive).
        """

        root: int = start

        while True:
            left_child: int = 2 * root + 1
            right_child: int = 2 * root + 2
            largest: int = root

            if (
                left_child <= end
                and collection[left_child] > collection[largest]
            ):
                largest = left_child

            if (
                right_child <= end
                and collection[right_child] > collection[largest]
            ):
                largest = right_child

            if largest == root:
                return

            collection[root], collection[largest] = (
                collection[largest],
                collection[root],
            )
            root = largest

    # Build a max heap (largest value at index 0).
    for start in range((n // 2) - 1, -1, -1):
        sift_down(start, n - 1)

    # Extract elements from the heap one by one.
    for end in range(n - 1, 0, -1):
        collection[0], collection[end] = collection[end], collection[0]
        sift_down(0, end - 1)


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    heap_sort(collection)
    print(collection)

    assert collection == sorted(collection)
    print("Ascending")


if __name__ == "__main__":
    main()
