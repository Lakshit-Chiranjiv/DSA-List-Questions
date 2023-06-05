# print root to node path in binary tree

from Node import Node

def printPath(root, arr, target):
    if root == None:
        return False
    arr.append(root.data)
    if root.data == target:
        return True
    if printPath(root.left, arr, target) or printPath(root.right, arr, target):
        return True
    arr.pop()
    return False

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
arr = []
printPath(root, arr, 40)
print(arr)