class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        @cache
        def solve(i,j,e):
            if i == len(events) or j == 0:
                return 0
            if events[i][0] <= e:
                return solve(i+1,j,e)
            
            attend = solve(i+1,j-1,events[i][1])+events[i][2]
            not_attend = solve(i+1,j,e)
            return max(attend,not_attend)
        
        return solve(0,k,0)