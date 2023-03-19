class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        t = 0
        tasks.sort(key=lambda x: x[1])
        
        ts = {} #time slice map
        
        for i in tasks:
            usedTime = 0
            for j in range(i[0],i[1]+1):
                if ts.get(j,0) != 0:
                    usedTime += 1
                    
            k = i[1]
            while usedTime < i[2]:
                if ts.get(k,0) == 0:
                    usedTime += 1
                    t += 1
                    ts[k] = 1
                k -= 1
        return t