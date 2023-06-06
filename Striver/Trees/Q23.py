# lowest common ancestor in a binary tree

from Node import Node

def lca(root, n1, n2):
    if root is None or root.data == n1 or root.data == n2:
        return root
    
    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left is None:
        return right
    
    if right is None:
        return left
    
    return root

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)

print(lca(root, 40, 50).data)