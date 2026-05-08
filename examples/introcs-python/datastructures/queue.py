from collections import deque


# start: Queue
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)
# end: Queue


if __name__ == '__main__':
    q = Queue()
    for name in ("Alice", "Bob", "Carol"):
        q.enqueue(name)
    while not q.is_empty():
        print(q.dequeue())
