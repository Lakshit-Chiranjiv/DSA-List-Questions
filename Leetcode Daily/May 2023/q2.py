class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nc = 0
        for i in nums:
            if i < 0:
                nc += 1
            if i == 0:
                return 0
        return 1 if nc%2==0 else -1 
    
# intuition:
# 1. If we have the count of negative numbers in the array, we can easily determine the sign of the product.
# 2. If the count is even, the product is positive. If the count is odd, the product is negative.
# 3. If the array contains a zero, the product is zero.

# solution:
# 1. Initialize a variable nc to 0. This variable will store the count of negative numbers in the array.
# 2. Iterate over the array. If the current element is negative, increment nc by 1.
# 3. If the current element is zero, return 0.
# 4. After the loop completes, return 1 if nc is even, else return -1.

# Time Complexity: O(n) where n is the length of the array. We iterate over the array once.
# Space Complexity: O(1) since we do not use any extra space.