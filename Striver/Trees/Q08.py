# Iterative Postorder Traversal of Binary Tree using 1 Stack
from Node import Node

def postOrder(root):
    ans = []
    if root is None:
        return ans
    
    curr = root
    stack = []

    while curr is not None or len(stack) > 0:
        if curr is not None:
            stack.append(curr)
            curr = curr.left
        else:
            temp = stack[-1].right
            if temp is None:
                temp = stack.pop()
                ans.append(temp.data)
                while len(stack) > 0 and temp == stack[-1].right:
                    temp = stack.pop()
                    ans.append(temp.data)
            else:
                curr = temp

    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(postOrder(root))