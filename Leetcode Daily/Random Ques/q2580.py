class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort()
        c = 0
        mey = ranges[0][1]
        for i in range(len(ranges)-1):
            fe = ranges[i][1]
            mey = max(fe,mey)
            ss = ranges[i+1][0]
            if mey < ss:
                c += 1
            
        c += 1
        mod = (10**9)+7
        
        ans = (2**c)%mod
        
        return ans