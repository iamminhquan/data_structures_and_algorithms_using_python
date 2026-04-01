from __future__ import annotations

from typing import Generic, Iterable, Iterator, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    """
    A basic LIFO (Last In, First Out) stack implementation.

    :param values: Optional initial values to preload the stack.
    :type values: Iterable[T]
    :return: None
    :rtype: None
    """

    def __init__(self, values: Iterable[T] = ()) -> None:
        self.__items: list[T] = list(values)

    def __len__(self) -> int:
        """
        Return current number of elements in the stack.
        """
        return len(self.__items)

    def __iter__(self) -> Iterator[T]:
        """
        Iterate from top to bottom of the stack.
        """
        return reversed(self.__items)

    def __repr__(self) -> str:
        values: list[str] = [repr(value) for value in self.__items]
        return f"Stack([{', '.join(values)}])"

    def is_empty(self) -> bool:
        """
        Check whether the stack has no elements.
        """
        return len(self.__items) == 0

    def push(self, value: T) -> None:
        """
        Push a new value onto the top of the stack.
        """
        self.__items.append(value)

    def pop(self) -> T:
        """
        Remove and return the top value of the stack.

        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.__items.pop()

    def peek(self) -> T:
        """
        Return the top value without removing it.

        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.__items[-1]

    def clear(self) -> None:
        """
        Remove all elements from the stack.
        """
        self.__items.clear()
