class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = 0
        stack = [(root, 0, None)]
        while stack:
            node, n, left = stack.pop()
            if node:
                ans = max(ans, n)
                stack.append((node.left, 1 if left else n + 1, 1))
                stack.append((node.right, n + 1 if left else 1, 0))
        return ans
    
# intuition:
# 1. The longest zigzag path can be found by traversing the tree in a depth first manner and keeping track of the longest zigzag path seen so far.
# 2. A stack is used to keep track of the nodes in the tree and the number of zigzags seen so far.
# 3. The stack is initialized with the root node and the number of zigzags seen so far is 0.
# 4. The stack is popped until it is empty. At each iteration, the current node, the number of zigzags seen so far and a boolean left is popped from the stack.
# 5. If the current node is not None, the longest zigzag path seen so far is updated by comparing it with the number of zigzags seen so far.
# 6. The left child and the right child of the current node are pushed to the stack with the number of zigzags seen so far as 1 if left is True and n + 1 if left is False.
# 7. The longest zigzag path seen so far is returned.

# solution:
# 1. Initialize ans to 0.
# 2. Initialize a stack and push the root node and the number of zigzags seen so far as 0 to the stack.
# 3. While the stack is not empty, pop the current node, the number of zigzags seen so far and a boolean left from the stack.
# 4. If the current node is not None, update ans by maximum of ans and n.
# 5. Push the left child of the current node to the stack with the number of zigzags seen so far as 1 if left is True and n + 1 if left is False. The boolean left is set to True.
# 6. Push the right child of the current node to the stack with the number of zigzags seen so far as n + 1 if left is True and 1 if left is False. The boolean left is set to False.
# 7. Return ans.