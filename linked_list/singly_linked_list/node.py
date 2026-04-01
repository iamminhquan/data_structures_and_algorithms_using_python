from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    """
    A node used in a singly linked list.

    Each node stores a value and a reference to the next node.

    :param value: The value held by the node.
    :type value: T
    :param next: Reference to the next node (or None if there is no next node).
    :type next: Optional[Node[T]]
    :return: None
    :rtype: None
    """

    def __init__(self, value: T, next: Optional[Node[T]] = None) -> None:
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
        Get a reference to the next node (or None).
        """
        return self.__next

    @next.setter
    def next(self, next_node: Optional[Node[T]]) -> None:
        """
        Set a reference to the next node (or None).
        """
        self.__next = next_node

    def __repr__(self) -> str:
        """
        Return a debug-friendly string representation of the node.
        """
        return f"Node(value={self.__value!r})"
