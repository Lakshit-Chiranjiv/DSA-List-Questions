# maximum depth of binary tree

from Node import Node

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(maxDepth(root))