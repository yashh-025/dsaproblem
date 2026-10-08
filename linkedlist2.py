class node:
    def __init__(self, val):
        self.data = val
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def append(self, val):
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def del_node(self, value):
        temp = self.head
        prev = None
        if temp and temp.data == value:
            self.head = temp.next
            return
        while temp:
            if temp.data == value:
                prev.next = temp.next
                return
            prev = temp
            temp = temp.next
        print("Value not found")
    def insert(self, new_node, pos):
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        p = 1
        temp = self.head
        while temp and p != pos:
            temp = temp.next
            p += 1
        if temp is None:
            print("Invalid position")
            return
        new_node.next = temp.next
        temp.next = new_node
    def print(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
list = linkedlist()
list.append(2)
list.append(3)
list.append(44)
list.append(55)
list.insert(node(100), 2)
list.print()
print()
list.insert(node(200), 6)
list.print()
print()
list.del_node(100)

list.print()