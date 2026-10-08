class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            p = 1

            while p < pos - 1 and temp != None:
                temp = temp.next
                p += 1

            if temp != None:
                new_node.next = temp.next
                temp.next = new_node

    def print(self):
        count = 0
        total = 0
        temp = self.head
        while temp:
            count += 1
            total += temp.data
            print(temp.data)
            temp = temp.next

        print("count is:", count)
        print("sum is:", total)


list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(55))

list.print()

list.insert(Node(25), 3)

list.print()