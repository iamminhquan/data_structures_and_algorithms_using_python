from __future__ import annotations

from typing import Generic, Iterable, Iterator, Optional, TypeVar

from node import Node

T = TypeVar("T")


class DoublyLinkedList(Generic[T]):
    """
    A doubly linked list with head and tail pointers.

    Supports append, prepend, insert, indexed access, removal, and clear.

    :param values: Optional iterable used to initialize the list.
    :type values: Optional[Iterable[T]]
    :return: None
    :rtype: None
    """

    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        """
        Create an empty doubly linked list, optionally populated from values.

        :param values: Optional iterable of initial values.
        :type values: Optional[Iterable[T]]
        :return: None
        :rtype: None
        """
        self.__head: Optional[Node[T]] = None
        self.__tail: Optional[Node[T]] = None
        self.__size: int = 0

        if values is not None:
            previous: Optional[Node[T]] = None
            for value in values:
                new_node: Node[T] = Node(value=value, prev=previous, next=None)

                if previous is None:
                    self.__head = new_node
                else:
                    previous.next = new_node

                previous = new_node
                self.__size += 1

            self.__tail = previous

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

    def __bool__(self) -> bool:
        """
        Return True if the list is non-empty, otherwise False.
        """
        return self.__size > 0

    def __iter__(self) -> Iterator[T]:
        """
        Iterate over values from head to tail.

        :return: An iterator of node values.
        :rtype: iterator
        """
        current: Optional[Node[T]] = self.__head
        while current is not None:
            yield current.value
            current = current.next

    def __reversed__(self) -> Iterator[T]:
        """
        Iterate over values from tail to head.

        :return: A reverse iterator of node values.
        :rtype: iterator
        """
        current: Optional[Node[T]] = self.__tail
        while current is not None:
            yield current.value
            current = current.prev

    def __contains__(self, value: object) -> bool:
        """
        Check whether a value exists in the list.

        :param value: The value to search for.
        :type value: object
        :return: True if found, otherwise False.
        :rtype: bool
        """
        for item in self:
            if item == value:
                return True

        return False

    def __repr__(self) -> str:
        values: list[str] = [repr(value) for value in self]
        return f"DoublyLinkedList([{', '.join(values)}])"

    def append(self, value: T) -> None:
        """
        Append a new value at the end of the list.

        :param value: The value to append.
        :type value: T
        :return: None. The list is modified in-place.
        :rtype: None
        """
        new_node: Node[T] = Node(value=value, prev=self.__tail, next=None)

        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            assert self.__tail is not None
            self.__tail.next = new_node
            self.__tail = new_node

        self.__size += 1

    def prepend(self, value: T) -> None:
        """
        Prepend a new value at the beginning of the list.

        :param value: The value to prepend.
        :type value: T
        :return: None. The list is modified in-place.
        :rtype: None
        """
        new_node: Node[T] = Node(value=value, prev=None, next=self.__head)

        if self.__head is None:
            self.__tail = new_node
        else:
            self.__head.prev = new_node

        self.__head = new_node
        self.__size += 1

    def insert(self, index: int, value: T) -> None:
        """
        Insert a value at the given index.

        Valid indices are in range [0, size]. Inserting at index == size
        appends to the end.

        :param index: The position where the new node should be inserted.
        :type index: int
        :param value: The value to insert.
        :type value: T
        :return: None. The list is modified in-place.
        :rtype: None

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index > self.__size:
            raise IndexError("index out of bounds")

        if index == 0:
            self.prepend(value)
            return

        if index == self.__size:
            self.append(value)
            return

        previous: Optional[Node[T]] = self.__head
        for _ in range(index - 1):
            assert previous is not None
            previous = previous.next

        assert previous is not None and previous.next is not None
        successor: Node[T] = previous.next
        new_node: Node[T] = Node(value=value, prev=previous, next=successor)
        previous.next = new_node
        successor.prev = new_node
        self.__size += 1

    def get(self, index: int) -> T:
        """
        Get the value at the specified index.

        :param index: The index of the element to retrieve.
        :type index: int
        :return: The value at index.
        :rtype: T

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index >= self.__size:
            raise IndexError("index out of bounds")

        current: Optional[Node[T]] = self.__head
        for _ in range(index):
            assert current is not None
            current = current.next

        assert current is not None

        return current.value

    def remove(self, value: T) -> bool:
        """
        Remove the first occurrence of a value.

        :param value: The value to remove.
        :type value: T
        :return: True if a node was removed, otherwise False.
        :rtype: bool
        """
        current: Optional[Node[T]] = self.__head

        while current is not None:
            if current.value == value:
                if current.prev is None:
                    self.__head = current.next
                else:
                    current.prev.next = current.next

                if current.next is None:
                    self.__tail = current.prev
                else:
                    current.next.prev = current.prev

                self.__size -= 1
                return True

            current = current.next

        return False

    def remove_at(self, index: int) -> T:
        """
        Remove the node at the specified index and return its value.

        :param index: The index of the element to remove.
        :type index: int
        :return: The removed value.
        :rtype: T

        :raises IndexError: If index is out of bounds.
        """
        if index < 0 or index >= self.__size:
            raise IndexError("index out of bounds")

        current: Optional[Node[T]] = self.__head
        for _ in range(index):
            assert current is not None
            current = current.next

        assert current is not None
        removed_value: T = current.value

        if current.prev is None:
            self.__head = current.next
        else:
            current.prev.next = current.next

        if current.next is None:
            self.__tail = current.prev
        else:
            current.next.prev = current.prev

        self.__size -= 1
        return removed_value

    def contains(self, value: T) -> bool:
        """
        Check whether the list contains a given value.

        :param value: The value to search for.
        :type value: T
        :return: True if the value exists in the list, otherwise False.
        :rtype: bool
        """
        current: Optional[Node[T]] = self.__head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def clear(self) -> None:
        """
        Remove all nodes from the list.

        :return: None. The list is cleared in-place.
        :rtype: None
        """
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self) -> bool:
        """
        Check whether the list is empty.

        :return: True if the list has no elements, otherwise False.
        :rtype: bool
        """
        return self.__size == 0
