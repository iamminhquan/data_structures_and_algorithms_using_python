import random

MIN: int = 100
MAX: int = 2000


def selection_sort(collection: list[int]) -> None:
    length: int = len(collection)

    for i in range(length - 1):
        min_index = i

        for j in range(i + 1, length):
            if collection[min_index] > collection[j]:
                min_index = j

        collection[i], collection[min_index] = collection[min_index], collection[i]


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    selection_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
