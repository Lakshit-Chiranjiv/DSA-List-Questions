# diameter of a binary tree

from Node import Node

def height(root, ans):
    if not root:
        return 0
    lh = height(root.left, ans)
    rh = height(root.right, ans)
    ans[0] = max(ans[0], 1 + lh + rh)
    return 1 + max(lh, rh)

def diameter(root):
    if not root:
        return 0
    ans = [float('-inf')]
    height(root, ans)
    return ans[0]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(diameter(root))