# maximum width of binary tree

from Node import Node

def widthOfBinaryTree(root):
    if not root:
        return 0
    queue = [(root, 0)]
    max_width = 0
    while queue:
        mn = queue[0][1]
        size = len(queue)
        start = 0
        end = 0

        for i in range(size):
            curr = queue[0][1] - mn
            temp = queue[0][0]  
            queue.pop(0)
            if i == 0:
                start = curr
            if i == size - 1:
                end = curr

            if temp.left:
                queue.append((temp.left, 2 * curr + 1))
            if temp.right:
                queue.append((temp.right, 2 * curr + 2))

        max_width = max(max_width, end - start + 1)
    return max_width

root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.right = Node(9)
print(widthOfBinaryTree(root))