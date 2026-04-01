from __future__ import annotations

from stack import Stack


def main() -> None:
    stack: Stack[int] = Stack()

    print("Initial stack:", stack)
    print("is_empty():", stack.is_empty())
    print("length:", len(stack))
    print()

    print("Push 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after push:", stack)
    print("Top (peek):", stack.peek())
    print("length:", len(stack))
    print()

    print("Pop one value:", stack.pop())
    print("Stack after pop:", stack)
    print("Top (peek):", stack.peek())
    print("length:", len(stack))
    print()

    print("Iterate from top to bottom:", list(stack))
    print()

    print("Clear stack")
    stack.clear()
    print("Stack after clear:", stack)
    print("is_empty():", stack.is_empty())
    print("length:", len(stack))


if __name__ == "__main__":
    main()
