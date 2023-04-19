# iterative inorder traversal of a binary tree using stack

from Node import Node

def inOrder(root):
    ans = []
    stack = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        ans.append(curr.data)
        curr = curr.right

    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(inOrder(root))