def maximumWealth(self, accounts: List[List[int]]) -> int:
    mxw = 0
    for i in accounts:
        w = 0
        for j in i:
            w += j
        mxw = max(mxw,w)
    
    return mxw