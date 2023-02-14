class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            g = a
            s = b
        else:
            g = b
            s = a
        c = 0
        ans = ""
        gc = len(g)-1
        sc = len(s)-1

        while sc >= 0:
            x = int(g[gc]) + int(s[sc]) + c
            if x == 3:
                ans = "1" + ans
                c = 1
            elif x == 2:
                ans = "0" + ans
                c = 1
            else:
                ans = str(x) + ans
                c = 0
            sc -= 1
            gc -= 1

        while gc >= 0:
            x = int(g[gc]) + c
            if x == 2:
                ans = "0" + ans
                c = 1
            else:
                ans = str(x) + ans
                c = 0
            gc -= 1

        if c == 1:
            ans = "1" + ans
        
        return ans
