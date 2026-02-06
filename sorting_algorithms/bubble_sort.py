import random

MIN: int = 100
MAX: int = 2000


def bubble_sort(collection: list[int]) -> None:
    swapped: bool = True
    swap_counter: int = 0

    while swapped:
        swapped = False

        for index in range(0, len(collection) - 1 - swap_counter):
            if collection[index] > collection[index + 1]:
                collection[index], collection[index + 1] = (
                    collection[index + 1],
                    collection[index],
                )
                swapped = True

        swap_counter += 1


def main() -> None:
    size: int = int(input())

    collection: list[int] = [random.randint(MIN, MAX) for _ in range(size)]
    print(collection)

    bubble_sort(collection)
    print(collection)

    assert collection == sorted(collection)

    print("Ascending")


if __name__ == "__main__":
    main()
