class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        dst = [0] * k
        
        def solve(i):
            nonlocal ans, dst
            
            if i == len(cookies):
                ans = min(ans, max(dst))
                return
            if ans <= max(dst):
                return
            
            for j in range(k):
                dst[j] += cookies[i]
                solve(i + 1)
                dst[j] -= cookies[i]
        
        solve(0)
        return ans