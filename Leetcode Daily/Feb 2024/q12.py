class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = maj = 0
        for i in nums:
            if maj == 0:
                res = i
            if i == res:
                maj += 1
            else:
                maj -= 1
        return res
    
# Time complexity: O(n)
# Space complexity: O(1)
    
# Boyer-Moore Voting Algorithm
# The algorithm maintains a counter to keep track of a majority element. We take 2 variables, maj and res. maj is used to keep track of how many times the majority element has been seen so far w.r.t. the other elements. res is used to keep track of the majority element. We iterate through the array and if maj is 0, we update res to the current element. If the current element is equal to res, we increment maj, else we decrement maj. At the end, res will contain the majority element.