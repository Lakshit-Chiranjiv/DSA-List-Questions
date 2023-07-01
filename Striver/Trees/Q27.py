# time taken to burn entire binary tree starting from target node

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

def timeToBurn(root, target):
    if root == None:
        return 0
    parentsMap = {}
    markParents(root, parentsMap, target)
    q = []
    q.append(target)
    q.append(None)
    visited = set()
    visited.add(target)
    time = 0
    while len(q) > 0:
        curr = q.pop(0)
        if curr == None:
            if len(q) > 0:
                q.append(None)
                time += 1
        else:
            if curr.left and curr.left not in visited:
                q.append(curr.left)
                visited.add(curr.left)
            if curr.right and curr.right not in visited:
                q.append(curr.right)
                visited.add(curr.right)
            if parentsMap.get(curr, None) and parentsMap[curr] not in visited:
                q.append(parentsMap[curr])
                visited.add(parentsMap[curr])
    return time

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

target = root.left

print(timeToBurn(root, target))