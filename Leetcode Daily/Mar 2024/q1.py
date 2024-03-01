class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        o, z = 0, 0
        for i in s:
            if i == '0':
                z += 1
            else:
                o += 1
        ans = ""
        if o == 1:
            ans += (("0"*z)+"1")
            return ans
        ans = (("1"*(o-1))+("0"*z)+"1")
        return ans

# 2864. Maximum Odd Binary Number
# Time Complexity: O(n)
# Space Complexity: O(1)

# Approach: Count the number of 0's and 1's in the string. If there is only one 1, then the answer is 1 followed by z number of 0's. If there are more than one 1's, then the answer is (o-1) number of 1's followed by z number of 0's and 1. Because in case of a single 1, we need that 1 at the end of string to make it odd. In case of more than one 1's, we can utilize the extra 1's to make the number greater by placing them at the start of the string and a single 1 at the end to make it odd.
