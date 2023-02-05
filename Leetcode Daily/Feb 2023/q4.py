def checkInclusion(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    l1 = len(s1)
    l2 = len(s2)
    if l2 < l1:
        return False
    l = 0
    map = {}
    m = {}

    for i in range(l1):
        map[s1[i]] = map.get(s1[i], 0) + 1
        m[s1[i]] = map.get(s1[i], 0) + 1

    for i in range(l1):
        if m.get(s2[i], 0) > 0:
            map[s2[i]] = map.get(s2[i], 0) - 1
            if map.get(s2[i], 0) >= 0:
                l += 1

    if l == l1:
        return True

    for i in range(l1, l2):
        if l == l1:
            return True

        if m.get(s2[i], 0) > 0:
            map[s2[i]] = map.get(s2[i], 0) - 1
            if map.get(s2[i], 0) >= 0:
                l += 1

        if m.get(s2[i - l1], 0) > 0:
            map[s2[i - l1]] = map.get(s2[i - l1], 0) + 1
            if map.get(s2[i - l1], 0) <= m.get(s2[i - l1], 0) and map.get(s2[i - l1], 0) > 0:
                l -= 1

    if l == l1:
        return True

    return False


def checkInclusion2(self, s1: str, s2: str) -> bool:
    mp = {}
    c = len(s1)

    if len(s1) > len(s2):
        return False
    if s1 == s2:
        return True

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
        return True
    
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
            return True

    return False