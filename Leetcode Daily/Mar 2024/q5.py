class Solution:
    def minimumLength(self, s: str) -> int:
        st, ed = 0, len(s)-1
        while st < ed:
            if s[st] != s[ed]:
                break
            x = s[st]
            y = s[ed]
            while s[st] == x:
                st += 1
                if st >= ed:
                    break
            while s[ed] == y:
                ed -= 1
                if st >= ed:
                    break
        return ed-st+1