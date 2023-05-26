# check if both the trees are identical or not

from Node import Node

def isIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    elif root1 == None or root2 == None:
        return False
    else:
        return root1.data == root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)

print(isIdentical(root, root2))