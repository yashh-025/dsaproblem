
def solution():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new = Node(data)
            if not self.head:
                self.head = new
                return
            t = self.head
            while t.next:
                t = t.next
            t.next = new

        def display(self):
            t = self.head
            while t:
                print(t.data, end=" ")
                t = t.next
            print()

        def insert(self, data, pos):
            if pos < 1:
                return
            new = Node(data)
            if pos == 1:
                new.next = self.head
                self.head = new
                return
            t = self.head
            for _ in range(pos - 2):
                if not t:
                    return
                t = t.next
            if not t:
                return
            new.next = t.next
            t.next = new

        def middle(self):
            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            if slow:
                print("Middle:", slow.data)

        def delete(self, value):
            t = self.head
            if t and t.data == value:
                self.head = t.next
                return
            while t and t.next:
                if t.next.data == value:
                    t.next = t.next.next
                    return
                t = t.next

        def reverse(self):
            prev = None
            t = self.head
            while t:
                nxt = t.next
                t.next = prev
                prev = t
                t = nxt
            self.head = prev

        def pair_sum(self):
            t = self.head
            while t and t.next:
                print(t.data + t.next.data)
                t = t.next

    ll = LinkedList()

    n = int(input("Enter number of nodes: "))
    values = []
    while len(values) < n:
        line = input("Enter node values: ").strip()
        if line:
            values.extend(map(int, line.split()))

    for x in values[:n]:
        ll.append(x)

    print("Original list:")
    ll.display()

    pos = int(input("Enter insertion position: "))
    data = int(input("Enter value to insert: "))
    ll.insert(data, pos)
    ll.display()

    ll.middle()

    value = int(input("Enter value to delete: "))
    ll.delete(value)
    ll.display()

    ll.reverse()
    print("Reversed list:")
    ll.display()

    print("Consecutive sums:")
    ll.pair_sum()


if __name__ == "__main__":
    solution()

