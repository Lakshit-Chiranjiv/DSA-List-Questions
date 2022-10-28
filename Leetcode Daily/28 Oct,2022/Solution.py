from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        wrds = defaultdict(lambda: [])
        for i in strs:
            p = ''.join(sorted(i))
            wrds[p].append(i) 
            
        for i in wrds:
            ans.append(wrds[i])
            
        return ans