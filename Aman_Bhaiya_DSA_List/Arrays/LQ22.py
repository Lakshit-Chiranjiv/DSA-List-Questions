class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        left = []
        right = []
        lmx = height[0]
        rmx = height[n-1]

        left.append(lmx)
        for i in height[1:]:
            lmx = max(lmx,i)
            left.append(lmx)

        right.append(rmx)
        for i in height[n-2::-1]:
            rmx = max(rmx,i)
            right.append(rmx)
        
        for i in range(0,n):
            mn = min(left[i], right[n-i-1])
            total = total + (mn - height[i])

        return total