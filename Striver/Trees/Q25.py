# implement children sum property in a binary tree by incrementing value of nodes

from Node import Node

def ChildrenSumProperty(root):
    if not root:
        return
    child = 0
    if root.left:
        child += root.left.data
    if root.right:
        child += root.right.data
    if child > root.data:
        root.data = child
    else:
        if root.left:
            root.left.data = root.data
        elif root.right:
            root.right.data = root.data
    ChildrenSumProperty(root.left)
    ChildrenSumProperty(root.right)

    total = 0
    if root.left:
        total += root.left.data
    if root.right:
        total += root.right.data
    if root.left or root.right:
        root.data = total

root = Node(50)
root.left = Node(7)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(30)

ChildrenSumProperty(root)

q = [root]
while q:
    curr = q.pop(0)
    print(curr.data, end=" ")
    if curr.left:
        q.append(curr.left)
    if curr.right:
        q.append(curr.right)
print()

