class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        if index < 0:
            raise IndexError("index must not be negative")

        if index == 0:
            self.prepend(data)
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("index out of range")
            current = current.next

        if current is None:
            raise IndexError("index out of range")

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next

        return False

    def search(self, data):
        current = self.head
        index = 0

        while current is not None:
            if current.data == data:
                return index
            current = current.next
            index += 1

        return -1

    def display(self):
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next
        print(" -> ".join(values + ["None"]))


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    print("Original list:")
    linked_list.display()

    linked_list.prepend(5)
    linked_list.insert(2, 15)
    print("After adding 5 at the beginning and 15 at index 2:")
    linked_list.display()

    linked_list.delete(20)
    print("After deleting 20:")
    linked_list.display()

    print("Index of 30:", linked_list.search(30))