class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if sorted(s) != sorted(goal):
            return False
        mp = {}
        for i in s:
            if mp.get(i,0) == 0:
                mp[i] = 1
            else:
                mp[i] += 1

        i = 0
        j = 0
        d = 0
        while i < len(s):
            if s[i] != goal[j]:
                d += 1
            i += 1
            j += 1
        y = 0
        for i in mp:
            if mp[i] >= 2:
                y = 1
                break
        if s==goal and y == 1:
            return True
        return d == 2