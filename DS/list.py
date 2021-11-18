from DS.node import Node


class Single_Linked_List:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        self.tail = head

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def search(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                return index, current
            current = current.next
            index += 1
        return -1, None

    def remove(self, data):
        current = self.head
        found = False
        previous = None
        while current is not None:
            if current.data == data:
                found = True
                break
            previous = current
            current = current.next
        if found is False:
            return False
        if self.size == 1:
            self.head = None
        elif current == self.head:
            self.head = self.head.next
        elif current == self.tail:
            previous.next = None
            self.tail = previous
        else:
            previous.next = current.next
        self.size -= 1
        return True

    def to_array(self):
        current = self.head
        result = []
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def printall(self):
        output = ""
        if self.size == 0:
            output = "Empty"
        else:
            current = self.head
            while current is not None:
                output += str(current.data) + "->"
                current = current.next
            output = output[:-2]
        print(output)


