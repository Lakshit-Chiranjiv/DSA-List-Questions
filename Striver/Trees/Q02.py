# inorder traversal of a binary tree

from Node import Node

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data, end=" ")
    inOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder(root)
