class Solution:
    def splitNum(self, num: int) -> int:
        s = str(num)
        s = ''.join(sorted(s))
        x = ""
        y = ""
        for i in range(len(s)):
            if i & 1:
                y += s[i]
            else:
                x += s[i]
        return int(x)+int(y)