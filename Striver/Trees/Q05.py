# Iterative Preorder Traversal of a Binary Tree using Stack

from Node import Node

def preOrder(root):
    ans = []

    if root is None:
        return ans
    
    stack = []
    stack.append(root)

    while len(stack) > 0:
        curr = stack.pop()
        ans.append(curr.data)
        if curr.right is not None:
            stack.append(curr.right)
        if curr.left is not None:
            stack.append(curr.left)
    
    return ans

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(preOrder(root))