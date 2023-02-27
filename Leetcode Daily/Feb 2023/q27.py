"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def quad(n,r,c):
            flag = 1
            x = grid[r][c]
            for i in range(n):
                for j in range(n):
                    if grid[r+i][c+j] != x:
                        flag = 0
                        break

            if flag:
                return Node(x,True)
            else:
                n = n//2
                topLeft = quad(n,r,c)
                topRight = quad(n,r,c+n)
                bottomLeft = quad(n,r+n,c)
                bottomRight = quad(n,r+n,c+n)

                return Node(1,False,topLeft,topRight,bottomLeft,bottomRight)
        return quad(len(grid),0,0)
        




