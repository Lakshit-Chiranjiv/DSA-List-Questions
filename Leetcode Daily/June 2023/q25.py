class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        M = 10**9+7
        n = len(locations)
        @cache
        def solve(s,e,f):
            if f < 0:
                return 0
            x = 0
            if s == e and f >= 0:
                x = 1
            for i in range(n):
                if i == s:
                    continue
                x += solve(i,e,f-(abs(locations[i] - locations[s])))
            return x%M
        return solve(start,finish,fuel)%M