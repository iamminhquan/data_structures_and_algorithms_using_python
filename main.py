import math
import os
import sys


def is_increment(collection: list) -> bool:
    length: int = len(collection)

    for i in range(length - 1):
        if collection[i] > collection[i + 1]:
            return False

    return True


def interchange_sort(collection: list) -> None:
    length: int = len(collection)

    for i in range(length):
        for j in range(length):
            if collection[i] < collection[j]:
                # Swap two elements.
                collection[i], collection[j] = collection[j], collection[i]


def main() -> None:
    # Init the collection.
    collection: list = [10, 9, 8, 7, 1, 2, 3, 4, 5, 6]
    print(collection)

    # Sorting the collection to ensure the collection is increment.
    interchange_sort(collection)

    # Print the collection after sorted.
    print(collection)

    # Check if the collection is not sorted, then print "NO" to the terminal.
    if is_increment(collection):
        print("Yes, the collection is already sorted.")
    else:
        print("No, the collection is not already sorted.")


if __name__ == "__main__":
    main()
