def distinctNames(self, ideas: List[str]) -> int:
    ig = [set() for _ in range(26)]
    for idea in ideas:
        ig[ord(idea[0]) - ord('a')].add(idea[1:])
    
    ans = 0
    for i in range(25):
        for j in range(i + 1, 26):
            mutuals = len(ig[i] & ig[j]) 
            ans += 2 * (len(ig[i]) - mutuals) * (len(ig[j]) - mutuals)
            
    return ans