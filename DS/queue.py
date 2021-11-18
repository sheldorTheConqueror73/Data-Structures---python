from DS.node import Node


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = self.head
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise ValueError("Queue is empty")
        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            current.next = None
            self.tail = current

    def front(self):
        if self.size == 0:
            raise ValueError("Queue is empty")
        return self.tail.data

    def is_empty(self):
        return self.size == 0
