class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        mx = 0
        mn = float('inf')
        mx = max(mx,weights[0]+weights[-1])
        mn = min(mn,weights[0]+weights[-1])
        arr = []
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        for i in range(k-1):
            mn += arr[i]
        
        for i in range(1,k):
            mx += arr[-i]
        return abs(mx-mn)