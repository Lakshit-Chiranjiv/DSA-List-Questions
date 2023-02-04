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