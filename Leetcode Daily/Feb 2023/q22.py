class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sm = weights[0]
        mx = weights[0]

        for i in weights[1:]:
            sm += i
            mx = max(i,mx)
        
        if days == 1:
            return sm
        l = mx
        r = sm
        while l < r:
            m = (l+r)//2
            curr = 0
            d = 1
            for i in weights:
                if curr+i > m:
                    d += 1
                    curr = i
                else:
                    curr += i

            if d <= days:
                r = m
            else:
                l = m + 1

        return l