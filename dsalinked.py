class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node inserted at beginning.")

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print("Node inserted at end.")

    # Insert at a specific position
    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Position out of range.")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range.")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted successfully.")

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        self.head = self.head.next
        print("First node deleted.")

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.next is None:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        print("Last node deleted.")

    # Delete a node by value
    def delete_value(self, value):
        if self.head is None:
            print("Linked list is empty.")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted.")
                return
            temp = temp.next

        print("Value not found.")

    # Search an element
    def search(self, value):
        temp = self.head
        position = 1

        while temp is not None:
            if temp.data == value:
                print("Element found at position:", position)
                return

            temp = temp.next
            position += 1

        print("Element not found.")

    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous
        print("Linked list reversed.")

    # Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Total nodes:", count)

    # Display linked list
    def display(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        temp = self.head

        print("Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
ll = LinkedList()

while True:
    print("\n===== LINKED LIST MENU =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete by Value")
    print("7. Search Element")
    print("8. Reverse Linked List")
    print("9. Count Nodes")
    print("10. Display Linked List")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert_beginning(data)

    elif choice == 2:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        position = int(input("Enter position: "))
        ll.insert_position(data, position)

    elif choice == 4:
        ll.delete_beginning()

    elif choice == 5:
        ll.delete_end()

    elif choice == 6:
        value = int(input("Enter value to delete: "))
        ll.delete_value(value)

    elif choice == 7:
        value = int(input("Enter value to search: "))
        ll.search(value)

    elif choice == 8:
        ll.reverse()

    elif choice == 9:
        ll.count_nodes()

    elif choice == 10:
        ll.display()

    elif choice == 11:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")