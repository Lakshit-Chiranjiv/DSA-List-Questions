class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2*n
        ans = 1
        while slots > 0:
            ch = (slots * (slots-1)) // 2
            slots -= 2
            ans *= ch
        return ans%(10**9+7)