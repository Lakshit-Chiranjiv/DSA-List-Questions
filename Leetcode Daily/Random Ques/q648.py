def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    sent = sentence.split()
    ans = ""
    mnl = len(dictionary[0])
    mxl = len(dictionary[0])
    dc = {}
    dc[dictionary[0]] = 1
    for i in dictionary[1:]:
        if len(i) > mxl:
            mxl = len(i)
        if len(i) < mnl:
            mnl = len(i)
        if dc.get(i,-1) == -1:
            dc[i] = 1
        else:
            dc[i] += 1
    print(dc)

    for i in sent:
        x = 0
        for j in range(mnl,mxl+1):
            if dc.get(i[:j],-1) != -1:
                ans += i[:j]
                x = 1
                break
        if x == 0:
            ans += i
        ans += " "

    ans = ans[:len(ans)-1]
    return ans