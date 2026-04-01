from __future__ import annotations

from doubly_linked_list import DoublyLinkedList


def main() -> None:
    doubly_linked_list: DoublyLinkedList[int] = DoublyLinkedList()

    print("Initial list:", doubly_linked_list)
    print("is_empty():", doubly_linked_list.is_empty())
    print("length:", len(doubly_linked_list))
    print()

    print("Append 10, 20, 30")
    doubly_linked_list.append(10)
    doubly_linked_list.append(20)
    doubly_linked_list.append(30)
    print("List after append:", doubly_linked_list)
    print("length:", len(doubly_linked_list))
    print("reverse order:", list(reversed(doubly_linked_list)))
    print()

    print("Prepend 5")
    doubly_linked_list.prepend(5)
    print("List after prepend:", doubly_linked_list)
    print("length:", len(doubly_linked_list))
    print()

    print("Insert 15 at index 2")
    doubly_linked_list.insert(2, 15)
    print("List after insert:", doubly_linked_list)
    print("length:", len(doubly_linked_list))
    print()

    print("Get value at index 2:", doubly_linked_list.get(2))
    print("List via iteration:", list(doubly_linked_list))
    print()

    print("Contains 20?", doubly_linked_list.contains(20))
    print("Contains 999?", doubly_linked_list.contains(999))
    print()

    print("Remove value 15")
    removed_success: bool = doubly_linked_list.remove(15)
    print("Removed:", removed_success)
    print("List after remove(15):", doubly_linked_list)
    print("length:", len(doubly_linked_list))
    print()

    print("Remove_at index 0")
    removed_head: int = doubly_linked_list.remove_at(0)
    print("Removed head value:", removed_head)
    print("List after remove_at(0):", doubly_linked_list)
    print("length:", len(doubly_linked_list))
    print()

    print("Clear the list")
    doubly_linked_list.clear()
    print("List after clear:", doubly_linked_list)
    print("is_empty():", doubly_linked_list.is_empty())
    print("length:", len(doubly_linked_list))


if __name__ == "__main__":
    main()
