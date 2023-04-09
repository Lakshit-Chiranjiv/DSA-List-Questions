class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        mp = {}
        occ = {}
        n = len(nums)
        for i in range(n):
            if mp.get(nums[i],-1) == -1:
                mp[nums[i]] = i
                occ[nums[i]] = 1
            else:
                mp[nums[i]] += i
                occ[nums[i]] += 1
        arr = [0 for i in range(n)] 
        for i,x in enumerate(nums):
            arr[i] = mp[x] - occ[x]*i
            mp[x] -= (2*i)
            occ[x] -= 2
            
        return arr