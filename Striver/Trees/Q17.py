# vertical order traversal of a binary tree
from Node import Node

def verticalOrder(root):
    if root is None:
        return []
    m = {}
    q = []
    q.append((root, 0, 0)) # (node, row, col)
    while q:
        node, row, col = q.pop(0)
        if col not in m:
            m[col] = [(row, node.data)]
        else:
            m[col].append((row, node.data))
        if node.left:
            q.append((node.left, row + 1, col - 1))
        if node.right:
            q.append((node.right, row + 1, col + 1))
    res = []
    for k in sorted(m.keys()):
        res.append([val for _, val in sorted(m[k])])
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
print(verticalOrder(root)) # [[2, 4, 5, 6], [1, 3]]