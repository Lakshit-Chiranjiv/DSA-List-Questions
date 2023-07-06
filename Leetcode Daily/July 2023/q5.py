class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        curr = 0
        prev = 0
        z = 0
        for i in nums:
            if i == 0:
                z = 1
            if i == 1 and prev == 1:
                curr += 1
                prev = 1
            elif i == 0 and prev == 1:
                arr.append(curr)
                curr = 0
                prev = 0
            elif i == 0 and prev == 0:
                arr.append(0)
                prev = 0
            else:
                curr += 1
                prev = 1
        
        if curr > 0:
            arr.append(curr)
        if z == 0:
            return len(nums)-1
        i = 0
        j = 1
        m = 0
        while j < len(arr):
            m = max(arr[i]+arr[j],m)
            i += 1
            j += 1
        m = max(m,arr[-1])
        return m