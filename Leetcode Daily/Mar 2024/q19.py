class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        mxc = 0
        for i in tasks:
            mp[i] = mp.get(i,0)+1
            mxc = max(mxc, mp[i])
        clk = (mxc-1)*(n+1)
        for i in mp:
            if mp[i] == mxc:
                clk += 1
        return max(clk, len(tasks))
    
# 621. Task Scheduler
# Time Complexity: O(n)
# Space Complexity: O(1)
    
# We keep track of the frequency of each task and the maximum frequency.