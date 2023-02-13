class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high&1 == 1:
            return ((high//2) - (low//2) + 1)
        else:
            return ((high//2) - (low//2))