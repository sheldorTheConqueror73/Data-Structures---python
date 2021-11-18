from DS.node import Node


class Stack:
    def __init__(self):
        self.head = Node
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.size != 0:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def peek(self):
        return self.head.data

    def pop(self):
        if self.size == 0:
            raise ValueError(" Stack is empty")
        temp = self.head
        self.head = self.head.next
        self.size -= 1
        return temp

    def is_empty(self):
        return self.size == 0


    def printall(self):
        output = ""
        if self.size == 0:
            output = "Empty"
        else:
            current = self.head
            while current is not None:
                output += str(current.data) + "<-"
                current = current.next
            output = output[:-2]
        print(output)

