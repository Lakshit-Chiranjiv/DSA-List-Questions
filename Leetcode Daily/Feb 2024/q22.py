class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = defaultdict(int)
        outg = defaultdict(int)

        for i in trust:
            inc[i[1]] += 1
            outg[i[0]] += 1
        
        for i in range(1,n+1):
            if inc[i] == n-1 and outg[i] == 0:
                return i
        return -1
    
# 997. Find the Town Judge
# Time complexity: O(N)
# Space complexity: O(N)
    
# Approach: Its a simple graph problem. We can use two dictionaries to keep track of the incoming and outgoing edges of each node. According to the given criteria, the judge will have n-1 incoming edges and 0 outgoing edges. We can iterate through the nodes and check for the judge. If we find a judge, we return the node. If we don't find a judge, we return -1.