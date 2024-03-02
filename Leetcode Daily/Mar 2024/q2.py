class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(list(map(lambda x: (x*x), nums)))

# 977. Squares of a Sorted Array
# Time Complexity: O(nlogn)
# Space Complexity: O(n)
    
# We simply create a new list of squares of the elements of the given list and then sort it.