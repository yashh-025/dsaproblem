class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    def findmid_del(self):
        temp1 = self.head
        prev = None

        while temp1 and temp1.next:
            prev = temp1
            temp1 = temp1.next
            temp1 = temp1.next

        if prev:
            prev.next = None

    def print(self):
        print("List elements:")
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Create linked list
ll = LinkedList()

ll.head = Node(10)
ll.head.next = Node(20)
ll.head.next.next = Node(30)
ll.head.next.next.next = Node(40)
ll.head.next.next.next.next = Node(50)

print("Original list:")
ll.print()

ll.reverse()
print("Reversed list:")
ll.print()

ll.findmid_del()
print("After deleting the second half:")
ll.print()