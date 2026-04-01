from __future__ import annotations

from singly_linked_list import SinglyLinkedList


def main() -> None:
    singly_linked_list: SinglyLinkedList[int] = SinglyLinkedList()

    print("Initial list:", singly_linked_list)
    print("is_empty():", singly_linked_list.is_empty())
    print("length:", len(singly_linked_list))
    print()

    print("Append 10, 20, 30")
    singly_linked_list.append(10)
    singly_linked_list.append(20)
    singly_linked_list.append(30)
    print("List after append:", singly_linked_list)
    print("length:", len(singly_linked_list))
    print()

    print("Prepend 5")
    singly_linked_list.prepend(5)
    print("List after prepend:", singly_linked_list)
    print("length:", len(singly_linked_list))
    print()

    print("Insert 15 at index 2")
    singly_linked_list.insert(2, 15)
    print("List after insert:", singly_linked_list)
    print("length:", len(singly_linked_list))
    print()

    print("Get value at index 2:", singly_linked_list.get(2))
    print("List via iteration:", list(singly_linked_list))
    print()

    print("Contains 20?", singly_linked_list.contains(20))
    print("Contains 999?", singly_linked_list.contains(999))
    print()

    print("Remove value 15")
    removed_success: bool = singly_linked_list.remove(15)
    print("Removed:", removed_success)
    print("List after remove(15):", singly_linked_list)
    print("length:", len(singly_linked_list))
    print()

    print("Remove_at index 0")
    removed_head: int = singly_linked_list.remove_at(0)
    print("Removed head value:", removed_head)
    print("List after remove_at(0):", singly_linked_list)
    print("length:", len(singly_linked_list))
    print()

    print("Clear the list")
    singly_linked_list.clear()
    print("List after clear:", singly_linked_list)
    print("is_empty():", singly_linked_list.is_empty())
    print("length:", len(singly_linked_list))


if __name__ == "__main__":
    main()
