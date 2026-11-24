class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Insert node
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    # Search node
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Preorder traversal
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # Find minimum value
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

    # Delete node
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            # Node with no child
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            # Node with two children
            temp = self.find_min(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# Main program
tree = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    tree.root = tree.insert(tree.root, value)

print("Inorder Traversal:")
tree.inorder(tree.root)

print("\nPreorder Traversal:")
tree.preorder(tree.root)

print("\nPostorder Traversal:")
tree.postorder(tree.root)

print("\n\nSearch 40:")
print("Found" if tree.search(tree.root, 40) else "Not Found")

print("\nDelete 30:")
tree.root = tree.delete(tree.root, 30)

print("Inorder after deletion:")
tree.inorder(tree.root)