
def findAnagrams(self, s: str, p: str) -> List[int]:
    ans = []
    mp = {}
    s1 = p
    s2 = s
    c = len(s1)

    if len(s1) > len(s2):
        return ans
    if s1 == s2:
        ans.append(0)
        return ans

    for i in s1:
        if mp.get(i,0) == 0:
            mp[i] = 1
        else:
            mp[i] += 1

    cmp = mp.copy()
    
    for i in range(len(s1)):
        if cmp.get(s2[i],0) != 0:
            mp[s2[i]] -= 1
            if mp[s2[i]] >= 0:
                c -= 1
    
    if c == 0:
        ans.append(0)
    
    for i in range(len(s1), len(s2)):
        if cmp.get(s2[i],0) != 0:
            mp[s2[i]] -= 1
            if mp[s2[i]] >= 0:
                c -= 1
        if cmp.get(s2[i - len(s1)],0) != 0:
            mp[s2[i - len(s1)]] += 1
            if mp[s2[i - len(s1)]] > 0:
                c += 1
        if c == 0:
            ans.append(i - len(s1)+1)

    return ans