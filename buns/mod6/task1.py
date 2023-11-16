class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0 or not self.head:
            return None

        current = self.head
        for _ in range(index):
            if current.next:
                current = current.next
            else:
                return None

        return current.value

    def remove(self, index):
        if index < 0 or not self.head:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        for _ in range(index):
            if current.next:
                prev = current
                current = current.next
            else:
                return

        prev.next = current.next

    def insert(self, index, value):
        if index < 0:
            return

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        prev = None
        for _ in range(index):
            if current.next:
                prev = current
                current = current.next
            else:
                break

        new_node.next = current
        prev.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()


linked_list = LinkedList()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(5)

linked_list.display()

linked_list.insert(3, 4)
linked_list.display()

print(linked_list.get(2))

linked_list.remove(1)
linked_list.display()
