# boundary traversal of binary tree - anti-clockwise
from Node import Node

def leftTraversal(root, res):
    if not root:
        return
    if root.left:
        res.append(root.data)
        leftTraversal(root.left, res)
    elif root.right:
        res.append(root.data)
        leftTraversal(root.right, res)

def rightTraversal(root, res):
    if not root:
        return
    if root.right:
        rightTraversal(root.right, res)
        res.append(root.data)
    elif root.left:
        rightTraversal(root.left, res)
        res.append(root.data)

def leafTraversal(root, res):
    if not root:
        return
    leafTraversal(root.left, res)
    if not root.left and not root.right:
        res.append(root.data)
    leafTraversal(root.right, res)

def boundaryTraversal(root):
    if not root:
        return []
    res = []
    res.append(root.data)
    leftTraversal(root.left, res)
    leafTraversal(root, res)
    rightTraversal(root.right, res)
    return res

Node1 = Node(20)
Node1.left = Node(8)
Node1.right = Node(22)
Node1.left.left = Node(4)
Node1.left.right = Node(12)
Node1.left.right.left = Node(10)
Node1.left.right.right = Node(14)
Node1.right.right = Node(25)
print(boundaryTraversal(Node1))