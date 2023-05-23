# check binary tree is balanced or not

from Node import Node

def height(root):
    if not root:
        return 0
    lh = height(root.left)
    if lh == -1:
        return -1
    rh = height(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)

def isBalanced(root):
    if not root:
        return True
    return height(root) != -1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(isBalanced(root))