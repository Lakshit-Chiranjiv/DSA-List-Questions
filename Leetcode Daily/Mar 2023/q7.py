class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 1
        r = min(time)*totalTrips

        while l < r:
            m = (l+r)//2
            trips_in_m = 0
            for i in time:
                trips_in_m += (m//i)
            if trips_in_m >= totalTrips:
                r = m
            else:
                l = m+1

        return l