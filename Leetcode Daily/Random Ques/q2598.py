class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mp = {}
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                k = nums[i]//value
                f = k * value
                nums[i] -= f
                if mp.get(nums[i],0) == 0:
                    mp[nums[i]] = 1
                else:
                    mp[nums[i]] += 1
            elif nums[i] < 0:
                k = (nums[i]*-1)//value
                f = k * value
                nums[i] += f
                if nums[i] < 0:
                    nums[i] += value
                if mp.get(nums[i],0) == 0:
                    mp[nums[i]] = 1
                else:
                    mp[nums[i]] += 1
            else:
                if mp.get(nums[i],0) == 0:
                    mp[nums[i]] = 1
                else:
                    mp[nums[i]] += 1
        fmp = {}
        for i in mp:
            if mp[i] > 1:
                x = mp[i]
                z = i
                while x > 1:
                    z = z+value
                    if fmp.get(z,0) == 0:
                        fmp[z] = 1
                    else:
                        fmp[z] += 1
                    x -= 1
            if fmp.get(i,0) == 0:
                fmp[i] = 1
            else:
                fmp[i] += 1
        for i in range((10**9)+1):
            if fmp.get(i,0) == 0:
                return i
            
        return 0