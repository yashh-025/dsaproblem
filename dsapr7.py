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
            new_node.prev = temp
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
    def delete(self, data):
        curr = self.head

        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next

                if curr.next:
                    curr.next.prev = curr.prev

                return

            curr = curr.next

    def occurance(self,data):
        curr = self.head
        count = 0
        while curr != None:
            if curr.data == data:
                count += 1
            curr = curr.next
        return count
    
    def swap(self):
        if self.head == None or self.head.next == None:
            return

        first = self.head
        last = self.head

        while last.next:
            last = last.next

        second = first.next
        second_last = last.prev

        if first.next == last:  # Only two nodes
            first.next = None
            first.prev = last
            last.next = first
            last.prev = None
            self.head = last
        else:
            last.prev = None
            last.next = second
            second.prev = last

            second_last.next = first
            first.prev = second_last
            first.next = None

            self.head = last
    def print(self):
        temp = self.head
        print("List elements: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
                
list1 = LinkedList()
list1.append(Node(10))
list1.insert(Node(5), 0)
list1.append(Node(20))
list1.insert(Node(14), 2)
list1.append(Node(30))
list1.insert(Node(25), 4)
list1.delete(25)
list1.delete(14)
list1.print()
print("\nOccurance of 10:" ,list1.occurance(10))

list1.swap()
list1.print()



