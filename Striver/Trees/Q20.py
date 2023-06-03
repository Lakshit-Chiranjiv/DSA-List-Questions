# right and left view of a binary tree

from Node import Node

# right view
def rightView(root, level, ans):
    if root is None:
        return
    if len(ans) == level:
        ans.append(root.data)
    rightView(root.right, level + 1, ans)
    rightView(root.left, level + 1, ans)

# left view
def leftView(root, level, ans):
    if root is None:
        return
    if len(ans) == level:
        ans.append(root.data)
    leftView(root.left, level + 1, ans)
    leftView(root.right, level + 1, ans)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.right = Node(7)

ans = []
rightView(root, 0, ans)
print("Right view:", ans)

ans = []
leftView(root, 0, ans)
print("Left view:", ans)