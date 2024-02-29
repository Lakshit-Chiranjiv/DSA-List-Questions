# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        even = True
        q = deque([root])

        while q:
            prev = float('-inf') if even else float('inf')

            for _ in range(len(q)):
                node = q.popleft()

                if even and (node.val % 2 == 0 or node.val <= prev):
                    return False
                elif not even and (node.val % 2 == 1 or node.val >= prev):
                    return False
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                prev = node.val
            even = not even
        return True
            
# 1609. Even Odd Tree
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We perform BFS(level order traversal) by adding nodes of each level in the queue and traversing each level left to right with a for loop and checking if they are even/odd and greater/lesser than the previous node value based on the specified condition. If we find the condition to be wrong at any point, we return False. If we reach up till the last node at last level then we return True.