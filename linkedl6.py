class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = new_node
        else:
            self.head = new_node
    def insert(self, new_node, position):
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            temp = self.head
            for _ in range(position - 1):
                if temp is None:
                    raise IndexError("Position out of bounds")
                temp = temp.next
            new_node.next = temp.next
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    def print(self):
        temp = self.head
        print("List elements: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(20))
list1.insert(Node(14), 2)
list1.append(Node(30))
list1.print()