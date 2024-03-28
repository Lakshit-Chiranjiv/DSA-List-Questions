class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        mp = {}
        l = 0

        for r in range(len(nums)):
            mp[nums[r]] = mp.get(nums[r],0)+1
            while l <= r and mp.get(nums[r],0) > k:
                mp[nums[l]] -= 1
                l += 1
            
            ans = max((r-l+1), ans)
        return ans
    
# 2958. Length of Longest Subarray With at Most K Frequency
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We maintain a pointer l which denotes the left end of the window and a pointer r which denotes the right end of the window. We maintain a dictionary mp which stores the frequency of the elements in the window. We iterate through the list and keep updating the frequency of the elements in the window. If the frequency of an element exceeds k, we increment l and decrement the frequency of the element at the left end of the window. We keep track of the length of the longest subarray with at most k frequency and return the length.