class Solution:
    def isSubsequence(self, s, t):
        sl = len(s)
        tl = len(t)
        p = 0

        if sl == 0:
            return True
        if tl < sl:
            return False
        if t == s:
            return True

        for c in t:
            if c == s[p]:
                p += 1
                if p == sl:
                    return True

        return p == sl
