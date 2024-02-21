class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            i += 1
        return left << i
    
# 201. Bitwise AND of Numbers Range
# Time complexity: O(1)
# Space complexity: O(1)
    
# 