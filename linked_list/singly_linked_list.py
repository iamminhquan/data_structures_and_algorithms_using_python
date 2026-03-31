from __future__ import annotations
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """
    A node used in a singly linked list.

    Each node stores a value and a reference to the next node.

    :param value: The value held by the node.
    :type value: T
    :param next: Reference to the next node (or None if this is the last node).
    :type next: Optional[Node[T]]
    :return: None
    :rtype: None
    """

    def __init__(self, value: T, next: Optional[Node[T]] = None) -> None:
        # Use name mangling for "private" fields in Python.
        self.__value: T = value
        self.__next: Optional[Node[T]] = next

    @property
    def value(self) -> T:
        """
        Get the value stored in the node.
        """
        return self.__value

    @value.setter
    def value(self, new_value: T) -> None:
        """
        Set the value stored in the node.
        """
        self.__value = new_value

    @property
    def next(self) -> Optional[Node[T]]:
        """
        Get a reference to the next node (or None if this is the last node).
        """
        return self.__next

    @next.setter
    def next(self, next_node: Optional[Node[T]]) -> None:
        """
        Set a reference to the next node.
        """
        self.__next = next_node


class SinglyLinkedList(Generic[T]):
    """
    A basic singly linked list structure.

    This class currently provides only the essential skeleton (constructor and
    a few dunder methods). Core operations (insert, delete, search, etc.) will
    be added later.

    :return: None
    :rtype: None
    """

    def __init__(self) -> None:
        """
        Create an empty singly linked list.

        :return: None
        :rtype: None
        """
        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__size: int = 0

    @property
    def head(self) -> Optional[Node[T]]:
        """
        Get the first node of the list.
        """
        return self.__head

    @property
    def tail(self) -> Optional[Node[T]]:
        """
        Get the last node of the list.
        """
        return self.__tail

    def __len__(self) -> int:
        """
        Return the number of elements in the list.

        :return: The list size.
        :rtype: int
        """
        return self.__size

    def __iter__(self):
        """
        Iterate over values from head to tail.

        :return: An iterator of node values.
        :rtype: iterator
        """
        current: Optional[Node[T]] = self.__head
        while current is not None:
            yield current.value
            current = current.next

    def __repr__(self) -> str:
        values: list[str] = [repr(value) for value in self]
        return f"SinglyLinkedList([{', '.join(values)}])"


def main() -> None:
    """
    Demonstrate `Node` and the basic behavior of `SinglyLinkedList`.

    :return: None
    :rtype: None
    """
    first: Node[int] = Node(1)
    second: Node[int] = Node(2)
    third: Node[int] = Node(3)

    first.next = second
    second.next = third

    if first.next is not None:
        print(f"{first.value} -> {first.next.value}")

    if second.next is not None:
        print(f"{second.value} -> {second.next.value}")

    empty_list: SinglyLinkedList[int] = SinglyLinkedList()
    print("empty_list:", empty_list)
    print("len(empty_list):", len(empty_list))
    print("iter(empty_list):", list(empty_list))
    print("head(empty_list) is None:", empty_list.head is None)
    print("tail(empty_list) is None:", empty_list.tail is None)

    # This skeleton list class does not yet include insertion methods.
    # For demo purposes only, we populate private fields via name-mangling.
    linked_list: SinglyLinkedList[int] = SinglyLinkedList()
    n1: Node[int] = Node(10)
    n2: Node[int] = Node(20)
    n3: Node[int] = Node(30)
    n1.next = n2
    n2.next = n3

    linked_list._SinglyLinkedList__head = n1
    linked_list._SinglyLinkedList__tail = n3
    linked_list._SinglyLinkedList__size = 3

    print("linked_list:", linked_list)
    print("len(linked_list):", len(linked_list))
    print("iter(linked_list):", list(linked_list))

    if linked_list.head is not None:
        print("head value:", linked_list.head.value)
    if linked_list.tail is not None:
        print("tail value:", linked_list.tail.value)


if __name__ == "__main__":
    main()
