# start: Stack
class Stack:
    def __init__(self):
        self._data = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
# end: Stack


# start: is_balanced
def is_balanced(s: str) -> bool:
    """Return True if all brackets in s are correctly matched and nested."""
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()
# end: is_balanced


if __name__ == '__main__':
    print(is_balanced("({[]})"))   # True
    print(is_balanced("({[})"))    # False
    print(is_balanced(""))         # True
