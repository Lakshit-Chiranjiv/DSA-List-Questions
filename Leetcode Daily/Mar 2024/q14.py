class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        c, s = 0, 0
        frq = {}
        for i in nums:
            s += i
            if s == goal:
                c += 1
            if s-goal in frq:
                c += frq[s-goal]
            frq[s] = frq.get(s,0) + 1
        return c
    
# 930. Binary Subarrays With Sum
# Time Complexity: O(n)
# Space Complexity: O(n)
    
# We keep track of the frequency of the prefix sums. While iterating and cumulatively adding the elements, we check if the current prefix sum is equal to the goal. If it is, we increment the count. If the difference between the current prefix sum and the goal is present in the frequency dictionary, that means that the difference between the current prefix sum and the goal is present in the array as subarrays and when these subarrays are added to the current iterating element, the sum will be equal to the goal. So, we add the frequency of the difference to the count. We keep updating the frequency of the prefix sums and return the count at the end.