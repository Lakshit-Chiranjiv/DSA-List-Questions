# preorder traversal of a tree

from Node import Node

def preOrder(root):
    if not root:
        return
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preOrder(root)