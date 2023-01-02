class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for i in range(0,n-1):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                l = i+1
                r = n-1
                sum = 0 - nums[i]

                while l < r:
                    if nums[l] + nums[r] == sum:
                        lst = [nums[i],nums[l],nums[r]]
                        ans.append(lst)

                        while l < r and nums[l] == nums[l+1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r-1]: 
                            r = r - 1
                        l = l + 1
                        r = r - 1
                    elif nums[l] + nums[r] < sum:
                        l = l + 1
                    else:
                        r = r - 1

        return ans
