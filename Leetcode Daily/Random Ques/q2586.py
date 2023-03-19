class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        v = 'aeiou'
        ans = 0
        for i in range(left,right+1):
            n = len(words[i])
            if words[i][0] in v and words[i][n-1] in v:
                ans += 1
        
        return ans