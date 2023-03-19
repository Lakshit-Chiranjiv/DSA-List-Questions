class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b = bin(n)[2:]
        ans = [0,0]
        i = 0
        j = len(b) - 1
        while j >= 0:
            if b[j] == '1' and i%2 == 0:
                ans[0] += 1
            elif b[j] == '1' and i%2 == 1:
                ans[1] += 1
            j -= 1
            i += 1
                
        return ans