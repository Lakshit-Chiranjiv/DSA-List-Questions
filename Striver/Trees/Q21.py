# check if binary tree is symmetric or not

from Node import Node

def isSymmetric(root):
    if root is None:
        return True
    return areSymmetricSubtrees(root.left, root.right)

def areSymmetricSubtrees(leftSubtree, rightSubtree):
    if leftSubtree is None or rightSubtree is None:
        return leftSubtree == rightSubtree
    
    if leftSubtree.data != rightSubtree.data:
        return False
    
    return areSymmetricSubtrees(leftSubtree.left, rightSubtree.right) and areSymmetricSubtrees(leftSubtree.right, rightSubtree.left)

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(6)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.left = Node(6)
root.right.right = Node(4)
root.right.left.left = Node(9)
root.right.left.right = Node(8)

print("Symmetric" if isSymmetric(root) else "Not symmetric")