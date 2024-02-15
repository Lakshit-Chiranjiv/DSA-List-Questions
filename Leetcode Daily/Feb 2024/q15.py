class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        total = 0
        for i in nums:
            if total > i:
                ans = total+i
            total += i
        return ans

# 2971. Find Polygon with the Largest Perimeter

# Time complexity: O(nlogn)
# Space complexity: O(1)
    
# We sort the list of numbers and then iterate through the list. We keep track of the total sum till the current index and if the total sum is greater than the current number, we update the answer. We then return the answer.
# Thinking: If we sort the list the first condition of a1 <= a2 <= a3 <= ... ak-1 <= ak is already fullfilled. Now we just need to make sure at each index whether it can form a valid polygon or not with the elements occuring before it having the sum greater than the current element. If it can, we update the answer. If it can't, we move to the next element. We keep doing this till we reach the end of the list and then return the answer.
    


