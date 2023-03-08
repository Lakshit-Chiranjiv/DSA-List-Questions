import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l+r)//2
            hrs = 0 #hrs needed to eat at speed m/hr
            for i in piles:
                hrs += math.ceil(i/m)
            if hrs > h:
                l = m+1
            else:
                r = m

        return l