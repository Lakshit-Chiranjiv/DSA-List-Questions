def totalFruit(self, fruits: List[int]) -> int:
    mp = {}
    mx = 0
    w = 0
    t = 0

    for i in range(len(fruits)):
        if mp.get(fruits[i],0) == 0:
            mp[fruits[i]] = 1
            w += 1
            t += 1
            if t > 2:
                while t > 2:
                    if mp[fruits[i-w + 1]] == 1:
                        t -= 1
                    mp[fruits[i-w + 1]] -= 1
                    w -= 1
        else:
            mp[fruits[i]] += 1
            w += 1

        mx = max(mx,w)

    return mx