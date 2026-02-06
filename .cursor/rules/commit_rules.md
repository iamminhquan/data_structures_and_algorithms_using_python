# Git Commit Rules

This repository follows a strict commit convention.
All commit messages must follow the format below.

## Commit Format

<type>(scope): <short summary>

- summary must be lowercase
- summary must be <= 72 characters
- use imperative mood
- no trailing period

Example:
feat(sort): implement merge sort
fix(stack): handle empty pop case
docs(readme): update usage section

---

## Allowed Types

feat     → new algorithm or data structure
fix      → bug fix
refactor → code improvement without changing behavior
docs     → documentation changes
test     → add or update tests
style    → formatting or naming only
chore    → project maintenance

Do not invent new types.

---

## Scope Rules

Scope describes what part of DSA is affected.

Examples:
array
linked-list
stack
queue
tree
graph
sort
search
dp
recursion

If unsure, use:
core

---

## Commit Writing Rules

- Do not explain the commit format
- Do not include extra text
- Output only the commit message
- If invalid, rewrite until valid
- Never output emojis
- Never output multiple commit options

Always produce exactly one valid commit message.
