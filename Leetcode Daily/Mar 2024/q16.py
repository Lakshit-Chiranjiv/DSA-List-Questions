class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        z, o, ans = 0, 0, 0
        diff = {}

        for i, n in enumerate(nums):
            if n == 0:
                z += 1
            else:
                o += 1
            if diff.get((o-z), -1) == -1:
                diff[o-z] = i
            
            if o == z:
                ans = o+z
            else:
                idx = diff[o-z]
                ans = max(ans, i - idx)
        return ans

# 525. Contiguous Array
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We maintain a dictionary to store the difference between the number of 0s and 1s encountered so far and the index at which this difference was encountered. We iterate through the array and keep updating the difference and the index at which this difference was encountered for the first time. We also keep track of the maximum length of the subarray with equal number of 0s and 1s encountered so far. We return the maximum length at the end.