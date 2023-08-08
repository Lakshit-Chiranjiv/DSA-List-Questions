class Solution:
    def search(self, nums: List[int], target: int) -> int:
        bi = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                bi = i
                break
        
        s = 0
        e = bi
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        
        s = bi + 1
        e = len(nums) - 1
        while s <= e:
            m = (s + e) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        
        return -1
