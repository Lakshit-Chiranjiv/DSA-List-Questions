class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s) // 2):
            sub = s[:i + 1]
            ys = 1
            if len(s) % len(sub) != 0:
                continue
            for j in range(0, len(s), len(sub)):
                if s[j:j + len(sub)] != sub:
                    ys = 0
                    break
            if ys == 1:
                return True
        return False
