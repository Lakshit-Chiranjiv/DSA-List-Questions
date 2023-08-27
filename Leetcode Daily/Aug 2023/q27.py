class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        mp = {}
        for i in range(len(stones)):
            mp[stones[i]] = i
        @cache
        def solve(i,k):
            if i == len(stones)-1:
                return True
            fc = False
            if i != 0 and k-1 != 0 and mp.get(stones[i]+(k-1), -1) != -1:
                fc = solve(mp[stones[i]+(k-1)], k-1)
            sc = False
            if mp.get(stones[i]+(k), -1) != -1:
                sc = solve(mp[stones[i]+k], k)
            tc = False
            if i != 0 and mp.get(stones[i]+(k+1), -1) != -1:
                tc = solve(mp[stones[i]+(k+1)], k+1)
            return (fc or sc or tc)

        return solve(0,1)