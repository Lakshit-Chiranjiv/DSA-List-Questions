class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        mod = (10**9)+7
        @cache
        def f(target,i):
            if target == 0: return 1
            if i >= len(types) or target < 0: return 0
            
            return sum(f(target - j * types[i][1],i+1) for j in range(types[i][0] + 1))%mod
        
        ans = f(target,0)
        return ans