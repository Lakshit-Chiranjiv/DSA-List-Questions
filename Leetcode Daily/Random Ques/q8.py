class Solution:
    def myAtoi(self, s: str) -> int:
        l = -2**31
        h = 2**31 - 1
        ts = s.strip()
        if(len(ts) == 0): return 0
        if len(ts) == 1 and 48<=ord(ts[0])<=57: return int(ts)
        if len(ts) == 1 and (ts[0] == '-' or ts[0] == '+'): return 0
        if ts[0] != '-' and ts[0] != '+' and (57<ord(ts[0]) or ord(ts[0])<48):
            return 0
        
        if ts[1] == '+' or ts[1] == '-':
            return 0

        idx = -1
        for i in range(1,len(ts)):
            if 57 < ord(ts[i]) or ord(ts[i]) < 48:
                idx = i
                break
        ans = 0
        if idx == -1:
            ans = int(ts)
        else:
            c = ts[0:idx]
            if len(c) == 1 and (c[0] == '-' or c[0] == '+'): return 0
            ans = int(c)

        if ans > h: return h
        if ans < l: return l
        return ans