class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        mp = {}
        for i in s:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1
        mx = float('-inf')
        mn = float('inf')
        
        for i in mp:
            x = int(s.replace(i,'9'))
            if x > mx:
                mx = x
        
        for i in mp:
            x = int(s.replace(i,'0'))
            if x < mn:
                mn = x 
                
        return mx - mn