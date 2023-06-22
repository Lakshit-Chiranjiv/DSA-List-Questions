# print all the nodes at distance k from the given node in a binary tree

from Node import Node

def markParents(root, parentsMap, target):
    q = []
    q.append(root)
    while len(q) > 0:
        curr = q.pop(0)
        if curr.left:
            parentsMap[curr.left] = curr
            q.append(curr.left)
        if curr.right:
            parentsMap[curr.right] = curr
            q.append(curr.right)

def printKNodes(root, target, k):
    parentsMap = {}
    markParents(root, parentsMap, target)
    q = []
    q.append(target)
    visited = set()
    visited.add(target)
    level = 0
    while len(q) > 0:
        if level == k:
            break
        size = len(q)
        for i in range(size):
            curr = q.pop(0)
            if curr.left and curr.left not in visited:
                q.append(curr.left)
                visited.add(curr.left)
            if curr.right and curr.right not in visited:
                q.append(curr.right)
                visited.add(curr.right)
            if parentsMap[curr] and parentsMap[curr] not in visited:
                q.append(parentsMap[curr])
                visited.add(parentsMap[curr])
        level += 1
    for i in q:
        print(i.data, end=" ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
target = root.left.left
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
printKNodes(root, target, 2)