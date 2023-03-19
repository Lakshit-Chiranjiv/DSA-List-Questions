class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp = {}
        for i in magazine:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1

        for i in ransomNote:
            if mp.get(i,0) == 0:
                return False
            mp[i] -= 1


        return True