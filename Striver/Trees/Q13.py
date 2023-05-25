# max path sum from any node to any node

from Node import Node

def maxPathSum(root, res):
    if not root:
        return 0
    l = maxPathSum(root.left, res)
    r = maxPathSum(root.right, res)
    temp = max(max(l, r) + root.data, root.data)
    ans = max(temp, l + r + root.data)
    res[0] = max(res[0], ans)
    return temp

def maxPathSumUtil(root):
    if not root:
        return 0
    res = [float('-inf')]
    maxPathSum(root, res)
    return res[0]

root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)

print(maxPathSumUtil(root))