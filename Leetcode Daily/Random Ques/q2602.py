class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        
        n = len(nums)
        sm = sum(nums)
        pref = [0]*n
        nums.sort()
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1] + nums[i]
            
        for i in queries:
            if i >= nums[n-1] or i <= nums[0]:
                ans.append(abs(sm - (n*i)))
                continue
            l = 0
            r = n-1
            idx = -1
            while l < r:
                m = (l+r)//2
                if nums[m] == i:
                    idx = m
                    break
                elif nums[m] < i:
                    l = m+1
                else:
                    r = m
                   
            if idx == -1:
                idx = l
            x = abs(pref[idx-1] - (idx*i))
            y = abs((pref[n-1]-pref[idx-1]) - ((n-idx)*i))
            ans.append(x+y)
            
            
        return ans