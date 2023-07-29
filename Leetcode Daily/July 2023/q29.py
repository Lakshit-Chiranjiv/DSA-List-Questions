class Solution:
    def soupServings(self, n: int) -> float:
        m = ceil(n/25)
        @cache
        def calc(i,j):
            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1.0
            if j <= 0:
                return 0.0

            return (calc(i-4,j)+calc(i-3,j-1)+calc(i-2,j-2)+calc(i-1,j-3))/4.0

        for k in range(1,m+1):
            if calc(k,k) > 1 - 1e-5:
                return 1.0
            
        return calc(m,m)