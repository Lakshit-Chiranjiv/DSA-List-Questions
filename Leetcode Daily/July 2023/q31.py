class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @cache
        def solve(i,j):
            if i < 0:
                t = 0
                for k in range(j+1):
                    t += ord(s2[k])
                return t

            if j < 0:
                t = 0
                for k in range(i+1):
                    t += ord(s1[k])
                return t
            if s1[i] == s2[j]:
                return solve(i-1,j-1)
            return min(solve(i-1,j)+ord(s1[i]), solve(i,j-1)+ord(s2[j]), solve(i-1,j-1)+ord(s1[i])+ord(s2[j]))
        return solve(len(s1)-1, len(s2)-1)