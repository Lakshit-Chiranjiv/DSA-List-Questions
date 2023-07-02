# count total number of nodes in a complete binary tree

from Node import Node

def countNodes(root):
    if root == None:
        return 0
    lh = 0
    node = root
    while node.left:
        lh += 1
        node = node.left
    rh = 0
    node = root
    while node.right:
        rh += 1
        node = node.right
    if lh == rh:
        return 2 ** (lh + 1) - 1
    return 1 + countNodes(root.left) + countNodes(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(countNodes(root))