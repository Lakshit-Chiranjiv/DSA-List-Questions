class Solution:
    def smallestWindow(self, s, p):
        start = 0
        minLen = float('inf')
        count = 0
        startIdx = -1
        sFreq = {}
        pFreq = {}
        for i in p:
            if i not in pFreq:
                pFreq[i] = 1
            else:
                pFreq[i] += 1
        
        for i in range(len(s)):
            if s[i] in pFreq:
                if s[i] not in sFreq:
                    sFreq[s[i]] = 1
                else:
                    sFreq[s[i]] += 1
                if sFreq[s[i]] <= pFreq[s[i]]:
                    count += 1
            if count == len(p):
                while s[start] not in pFreq or sFreq[s[start]] > pFreq[s[start]]:
                    if s[start] in pFreq:
                        sFreq[s[start]] -= 1
                    start += 1
                if minLen > i - start + 1:
                    minLen = i - start + 1
                    startIdx = start
        if startIdx == -1:
            return "-1"

        return s[startIdx:startIdx+minLen]