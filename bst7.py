class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        break
                    else:
                        temp = temp.left

                else:
                    if temp.right is None:
                        temp.right = new_node
                        break
                    else:
                        temp = temp.right

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root is not None:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


# Main program
b = BST()

b.insert(50)
b.insert(30)
b.insert(70)
b.insert(20)
b.insert(40)
b.insert(60)
b.insert(80)

print("Inorder Traversal:")
b.inorder(b.root)

print("\nPreorder Traversal:")
b.preorder(b.root)

print("\nPostorder Traversal:")
b.postorder(b.root)