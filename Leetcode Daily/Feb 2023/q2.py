def isAlienSorted(self, words: List[str], order: str) -> bool:
    mp = {}
    c = 97
    for i in order:
        mp[i] = chr(c)
        c += 1

    wrds = []
    for i in words:
        x = list(i)
        j = ''.join(map(lambda z: mp[z], x))
        wrds.append(j)


    for i in range(len(wrds)):
        for j in range(i+1,len(wrds)):
            if wrds[i] > wrds[j]:
                return False

    return True