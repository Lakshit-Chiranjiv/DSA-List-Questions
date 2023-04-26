class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(map(int,list(str(num))))
        
        return num
    
# intuition:
# 1. We will keep adding the digits of the number till we get a single digit number.

# solution:
# 1. Take a while loop and keep running it till the length of the number is greater than 1.
# 2. In the while loop, we will add the digits of the number and update the number.
# 3. Finally, we will return the number after the while loop.

# Time complexity: O(n) where n is the number of digits in the number as we are iterating over the digits of the number.
# Space complexity: O(1) as we are not using any extra space.


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        return 9 if num % 9 == 0 else num % 9
    
# intuition:
# 1. We will use the fact that the sum of digits of a number is equal to the remainder of the number divided by 9.
# 2. If the number is divisible by 9, then the sum of digits will be 9.
# 3. If the number is not divisible by 9, then the sum of digits will be the remainder of the number divided by 9.

# solution:
# 1. If the number is 0, then we will return 0.
# 2. If the number is divisible by 9, then we will return 9.
# 3. If the number is not divisible by 9, then we will return the remainder of the number divided by 9.

# Time complexity: O(1) as we are just doing constant time operations.
# Space complexity: O(1) as we are not using any extra space.