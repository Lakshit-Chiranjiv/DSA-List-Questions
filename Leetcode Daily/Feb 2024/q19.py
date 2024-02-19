class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n & (n-1))==0

# 231. Power of Two
# Time complexity: O(1)
# Space complexity: O(1)
    
# first condtion checks if the number is positive and the second condition checks if the number is a power of 2. When a number is power of two, it will exactly have one bit set to 1. So, when we subtract 1 from the number, all the bits to the right of the set bit will be flipped. So, when we do a bitwise AND operation, it will be zero.
