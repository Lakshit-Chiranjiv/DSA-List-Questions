class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        mp = {}
        for i in banned:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
        ans = 0
        sm = 0
        for i in range(1,n+1):
            if sm+i <= maxSum and mp.get(i,0) == 0:
                ans += 1
                sm += i
                
        return ans