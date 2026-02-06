# Python DSA Project Rules

This project is focused on learning Data Structures and Algorithms.
Code must prioritize clarity, correctness, and educational value.

## General Principles

- Prefer readability over clever tricks
- Write code that is easy for beginners to understand
- Avoid unnecessary optimizations unless explicitly requested
- Keep implementations clean and minimal

---

## Function Rules

- Each algorithm must be implemented as a standalone function
- Functions and parameters must have type hints
- Functions must include a docstring explaining:
  - what the algorithm does
  - parameters list
  - return type
  - time complexity
  - space complexity

Example:

def interchange_sort(collection: list[int]) -> None:
    """
    Sort a list of integers in ascending order using the interchange sort algorithm.

    This algorithm compares each element with all subsequent elements and swaps
    them if they are in the wrong order. Also known as naive sort or exchange sort.

    :param collection: The list of integers to be sorted.
    :type collection: list[int]
    :return: None. The list is sorted in-place.
    :rtype: None

    :Example:

    >>> collection = [64, 34, 25, 12, 22, 11, 90]
    >>> interchange_sort(collection)
    >>> collection
    [11, 12, 22, 25, 34, 64, 90]

    :Time Complexity: O(n^2) in all cases (best, average, worst).
    :Space Complexity: O(1) - sorts in-place.
    """

---

## Naming Conventions

- Use snake_case for variables and functions
- Use descriptive names:
  ❌ i, j, tmp
  ✅ index, left_pointer, pivot

- Avoid single-letter variables except loop counters

---

## Code Style

- Follow Black code formatter
- No unnecessary comments
- Add comments only to explain logic, not obvious syntax
- Keep line length reasonable
- Avoid nested logic deeper than 3 levels

---

## Algorithm Style

- Do not use Python built-in sort for sorting algorithms
- Implement algorithms manually
- Avoid shortcuts that hide the core logic
- Show the real algorithm steps

---

## Testing

- Include a simple example usage after each algorithm
- Use small readable test data
- Output must clearly show before/after states

---

## Educational Focus

- Avoid list comprehensions when they hide algorithm steps
- Comprehensions are allowed for simple initialization and others
- Avoid advanced Python features unless necessary
- Code should teach algorithm thinking, not Python tricks

---

## Pythonic Style Guidelines

Code should remain educational, but still follow idiomatic Python style.

- Prefer clear Python constructs when they do not hide the algorithm
- Use tuple unpacking for swaps:
  a, b = b, a

- Use enumerate() instead of manual index counters when appropriate
- Use meaningful boolean expressions instead of comparing to True/False
- Prefer early returns to reduce nesting
- Avoid redundant temporary variables

Good:
if not arr:
    return

Bad:
if len(arr) == 0:
    return

---

### Loop Style

- Use `for` loops instead of manual index control when possible
- Avoid modifying loop counters manually
- Keep loop logic simple and explicit

---

### Function Behavior

- Mutating functions must be clearly documented
- Return values should be explicit
- Avoid implicit behavior

---

### Python Features Allowed

These Python features are encouraged:

- tuple unpacking
- enumerate
- range with clear bounds
- list append patterns
- simple slicing when it does not hide logic

These features should be avoided:

- dense list comprehensions that hide algorithm steps
- chained expressions that reduce readability
- overly clever Python tricks

---

### Readability First Rule

If a Pythonic shortcut makes the algorithm harder to understand,
do not use it.

Educational clarity always wins over clever syntax.

---

## Output Rules

When generating algorithms:

- Only output valid Python code
- No extra explanation unless requested
- Code must follow all rules above
