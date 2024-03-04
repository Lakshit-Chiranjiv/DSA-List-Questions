class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        ans = score = 0
        l, r = 0, len(tokens)-1
        tokens.sort()
        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                ans = max(score, ans)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        return ans

# 948. Bag of Tokens
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
    
# We take a greedy approach to solve this problem. We can sort the tokens and then use two pointers l and r to iterate through the tokens. We can then use the power to buy tokens and increase the score. We can then use the score to buy power and decrease the score. We can then return the maximum score. We can also handle the edge cases where the power is less than the smallest token or the score is 0. Also we keep track of the maximum score using the variable ans to avoid returning a score where we played a remaining token being greedy and hence decreasing the score.