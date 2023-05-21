# preorder, inorder, postorder traversal of a tree in a single iteration using single stack

from Node import Node

def preInPost(root):
    st = []
    st.append([root, 1])

    if not root:
        return

    pre = []
    ino = []
    post = []

    while len(st) > 0:
        top = st[-1]
        if top[1] == 1:
            pre.append(top[0].data)
            top[1] += 1
            if top[0].left:
                st.append([top[0].left, 1])
        elif top[1] == 2:
            ino.append(top[0].data)
            top[1] += 1
            if top[0].right:
                st.append([top[0].right, 1])
        else:
            post.append(top[0].data)
            st.pop()

    print("Preorder: ", pre)
    print("Inorder: ", ino)
    print("Postorder: ", post)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

preInPost(root)