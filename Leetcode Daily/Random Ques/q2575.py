class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        n = 0
        for i in word:
            n = (n*10 + int(i))
            if n%m == 0:
                ans.append(1)
            else:
                ans.append(0)
            n %= m
        return ans