class Solution:
    def convertToTitle(self, c: int) -> str:
        ans = []
        while c > 0:
            c -= 1
            ans.append(chr(c%26 + 65))
            c //= 26

        return ''.join(reversed(ans))
