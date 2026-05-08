class Node:
    def __init__(self, data, next_node: "Node | None" = None):
        self.data = data
        self.next = next_node


# start: print_list
def print_list(head: "Node | None") -> None:
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
# end: print_list


# start: SinglyLinkedList
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data) -> None:
        self.head = Node(data, self.head)

    def append(self, data) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove(self, data) -> None:
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        return " -> ".join(str(x) for x in self) + " -> None"
# end: SinglyLinkedList


if __name__ == '__main__':
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.append(30)
    lst.prepend(5)
    print(lst)
    lst.remove(20)
    print(lst)
