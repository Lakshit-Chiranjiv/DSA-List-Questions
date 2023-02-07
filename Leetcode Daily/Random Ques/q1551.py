def minOperations(self, n: int) -> int:
    lim = 2*(n-1) + 1
    eq = (lim//2) + 1
    ans = 0
    for i in  range(1,eq,2):
        ans += (eq-i)

    return ans