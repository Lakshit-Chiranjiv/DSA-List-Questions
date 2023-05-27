# zigzag traversal of a binary tree
from Node import Node

def zigzag(root):
    ans = []
    if root == None:
        return ans
    q = []
    q.append(root)
    flag = 0
    while len(q) > 0:
        size = len(q)
        temp = []
        for i in range(size):
            node = q.pop(0)
            temp.append(node.data)
            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)
        if flag == 0:
            ans.append(temp)
            flag = 1
        else:
            ans.append(temp[::-1])
            flag = 0
    return ans

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)

print(zigzag(root))