class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([[root,1,0]])
        prevLvl = 0
        prevNum = 1

        while q:
            node, num, lvl = q.popleft()

            if lvl > prevLvl:
                prevLvl = lvl
                prevNum = num

            ans = max(ans, num - prevNum + 1)

            if node.left:
                q.append([node.left, 2*num, lvl+1])
            if node.right:
                q.append([node.right, 2*num+1, lvl+1])
        return ans
    
# intution:
# 1. BFS will be used to traverse the tree level by level.
# 2. The width of the tree at a level is the difference between the last node and the first node.
# 3. The first node is the node that is encountered first at a level.
# 4. The last node is the node that is encountered last at a level.
# 5. ans variable will be used to store the maximum width of the tree.
# 6. We don't need the node values so we will store the ordered nodes numbers in the nodes.

# solution:
# 1. Initialize ans to 0.
# 2. Initialize a queue with the root node, its number and level. The root node will have number 1 and level 0.
# 3. Initialize prevLvl to 0 and prevNum to 1.
# 4. While the queue is not empty:
# 5. Pop the first node from the queue.
# 6. If the level of the node is greater than the previous level:
# 7. Update prevLvl to the current level. Update prevNum to the current node number.
# 8. Update ans to the maximum of ans and the difference between the current node number and the previous node number.
# 9. If the left child of the node is not null, append it to the queue with its number, 2*current node number and level+1.
# 10. If the right child of the node is not null, append it to the queue with its number, 2*current node number+1 and level+1.
# 11. Return ans.

# time complexity:
# 1. The time complexity of the solution is O(n) where n is the number of nodes in the tree. We will traverse the tree once.

# space complexity:
# 1. The space complexity of the solution is O(n) where n is the number of nodes in the tree. We will store the nodes in the queue.