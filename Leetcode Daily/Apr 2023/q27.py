import math

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
    

# intuition:
# 1. We will use the fact that the number of times a bulb is toggled is equal to the number of factors of the number.
# 2. If the number of factors of a number is odd, then the bulb will be on and if the number of factors is even, then the bulb will be off.
# 3. Every prime number has 2 factors, 1 and the number itself. So, the bulb will be toggled 2 times so it will be off.
# 4. Every other number has even number of factors except for the perfect squares. So, the bulb will be toggled odd number of times and will be on.
# 5. So, we just need to find the number of perfect squares less than or equal to n and that is root(n).

# solution:
# 1. We will return the floor of the square root of n.

# Time complexity: O(1) as we are just doing constant time operations.
# Space complexity: O(1) as we are not using any extra space.



