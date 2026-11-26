# BST using Linked List

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:  # Left subtree
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:  # Right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.cnt += 1
            self.inorder(rt.right)

    def level_order(self, rt):
        if rt is None:
            print("BST is empty")
            return

        arr = []
        cnt = 0
        level = 0

        arr.append(rt)

        while cnt < len(arr):
            node_count = len(arr) - cnt
            print("\nLevel", level, ":", end=" ")

            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1

                print(temp.data, end=" ")

                if temp.left:
                    arr.append(temp.left)

                if temp.right:
                    arr.append(temp.right)

            level += 1

        print("\nHeight of the tree:", level - 1)


# Creating BST
b1 = BST()

# Inserting nodes
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(500))
b1.insert(Node(70))

# Inorder Traversal
print("\nInorder:")
b1.inorder(b1.root)

# Level Order Traversal
print("\n\nLevel Order Traversal:")
b1.level_order(b1.root)