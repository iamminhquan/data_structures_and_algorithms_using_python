import random

MIN: int = 100
MAX: int = 2000


def interchange_sort(collection: list[int]) -> None:
    length: int = len(collection)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if collection[i] > collection[j]:
                collection[i], collection[j] = collection[j], collection[i]


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    interchange_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
