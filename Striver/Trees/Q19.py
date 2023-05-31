# bottom view of a binary tree

from Node import Node

def bottomView(root):
    ans = []
    if root is None:
        return ans
    m = {}
    q = []
    q.append((root, 0)) # (node, col)
    while q:
        node, col = q.pop(0)
        m[col] = node.data
        if node.left:
            q.append((node.left, col - 1))
        if node.right:
            q.append((node.right, col + 1))

    for k in sorted(m.keys()):
        ans.append(m[k])
    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.right = Node(7)

print(bottomView(root))
