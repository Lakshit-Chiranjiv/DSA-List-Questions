class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        @cache
        def solve(s):
            if s == target:
                return 1
            if s > target:
                return 0
            sm = 0
            for i in nums:
                sm += solve(s+i)

            return sm

        return solve(0)
            