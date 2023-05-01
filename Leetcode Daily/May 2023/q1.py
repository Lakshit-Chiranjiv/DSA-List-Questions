class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:len(salary)-1])/(len(salary)-2)
    
# intuition:
# 1. Easiest way is to sort the array and then take the average of the elements from index 1 to n-2.

# solution:
# 1. Sort the array.
# 2. Take the sum of the elements from index 1 to n-2 and divide it by n-2.
# 3. Return the result.

# Time Complexity: O(nlogn) where n is the length of the array. Sorting takes O(nlogn) time.
# Space Complexity: O(1) since we do not use any extra space.