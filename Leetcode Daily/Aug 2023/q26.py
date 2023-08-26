class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: x[1])
        ans = 1
        end = pairs[0][1]
        for i in pairs[1:]:
            if end < i[0]:
                end = i[1]
                ans += 1
        return ans