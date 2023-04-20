# Iterative Postorder Traversal of Binary Tree using 2 Stacks

from Node import Node

def postOrder(root):
    if root is None:
        return
    s1 = []
    s2 = []
    s1.append(root)
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        print(s2.pop().data, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrder(root)