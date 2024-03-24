class Solution:
    def findDuplicate(self, nums):
        fast, slow = 0, 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

# 287. Find the Duplicate Number
# Time Complexity: O(n)
# Space Complexity: O(1)
            
# We take 2 pointers fast and slow and iterate through the list. We then find the intersection point of the two pointers. The first intersection point denotes that cycle exists. Then there is always a rule that the distance between the start of the list and the start of the cycle is equal to the distance between the intersection point and the start of the cycle. We then iterate through the list to find the duplicate number which is the start of the cycle. So we take another slow2 pointer and start it from 0 and simultaneously move the slow and slow2 pointers until they meet. The point at which they meet is the duplicate number.