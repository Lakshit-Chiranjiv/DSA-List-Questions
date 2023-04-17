# level order traversal of a tree
from Node import Node

def levelOrder(root):
    ans = []

    if root is None:
        return ans
    
    queue = []
    queue.append(root)

    while len(queue) > 0:
        level = []
        for i in range(len(queue)):
            curr = queue.pop(0)
            level.append(curr.data)
            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        ans.append(level)
    
    return ans

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)

print(levelOrder(root))