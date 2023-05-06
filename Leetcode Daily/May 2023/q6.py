class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10**9 + 7
        l = 0
        r = len(nums)-1
        nums.sort()
        res = 0
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                l += 1
                res += (2**(r-l+1))%mod
        
        return res%mod

# intution:
# 1. As we only need the min and max value of the subsequence, we can sort the array because order doesn't matter.
# 2. Now we can use two pointer approach to find the subsequence with sum less than or equal to target.
# 3. Now we can use the formula 2**(r-l+1) to find the number of subsequences possible withing the range of l and r.
# 4. We can use mod to avoid overflow. Return the result.

# solution:
# 1. Sort the array.
# 2. Create two pointers l and r and initialize them to 0 and len(nums)-1 respectively.
# 3. Run a loop until l <= r.
# 4. If nums[l] + nums[r] > target, decrement r.
# 5. Else increment l and add (2**(r-l+1))%mod to res.
# 6. Return res%mod.

# Time: O(nlogn) + O(n) = O(nlogn) where n is the length of nums. O(nlogn) for sorting and O(n) for two pointer approach.

# Space: O(1) as we are not using any extra space.