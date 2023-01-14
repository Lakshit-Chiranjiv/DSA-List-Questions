class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sa = sorted(list(s))
        ta = sorted(list(t))
        return sa == ta