class Solution:
    def reverseBits(self, n: int) -> int:
        bn = bin(n).replace("0b","")
        l = len(bn)
        k = 32-l
        pad = "0"*k
        bn = pad+bn
        rbn = "".join(reversed(bn))
        ans = int(rbn,2)
        return ans