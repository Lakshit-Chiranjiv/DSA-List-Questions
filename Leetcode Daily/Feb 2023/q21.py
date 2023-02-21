class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l = 0
        r = n-1

        while l <= r:
            m = (l+r)//2

            if m != n-1 and m != 0 and nums[m+1] != nums[m] and nums[m-1] != nums[m]:
                return nums[m]

            elif m == 0 and nums[m+1] != nums[m]:
                return nums[m]

            elif m == n-1 and nums[m-1] != nums[m]:
                return nums[m]
            
            elif nums[m+1] == nums[m]:
                if m & 1 == 1:
                    r = m - 1
                else:
                    l = m + 2
                    
            elif nums[m-1] == nums[m]:
                if (m-1) & 1 == 1:
                    r = m - 2
                else:
                    l = m + 1

        return -1