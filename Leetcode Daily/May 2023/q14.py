class Solution:
    def maxScore(self, nums: List[int]) -> int:

        @cache
        def solve(mask,op):
            mx = 0
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if ((1<<i) & mask) or ((1<<j) & mask):
                        continue

                    newMask = mask | (1<<i) | (1<<j)

                    score = op*math.gcd(nums[i],nums[j])
                    mx = max(mx,score+solve(newMask,op+1))
            
            return mx

        return solve(0,1)

# intution: 
# 1. We need to keep track of what elements we have used so far, so we use a bitmask for that. And for the number of operations we use a variable op.
# 2. We iterate over all possible pairs of numbers and check if we have used them before or not. If we have used them before we skip them else we use them and recurse for the next operation.
# 3. We also use memoization to avoid recomputing the same state again and again and finally return the maximum score we can get.

# solution
# 1. Define a function solve(mask,op) which returns the maximum score we can get if we have used the elements in the mask and we are currently on the opth operation. Initialize a mx variable to 0 which will store the maximum score we can get.
# 2. Take a nested for loop and check if this ith and jth index have been used before or not by shifting 1 to the ith and jth position and doing a bitwise and with the mask. If they have been used before we skip them by using the continue statement.
# 3. Else we create a new mask by using the bitwise or operator on the mask and the shifted value of i and j.
# 4. Then we calculate the score we will get by using the opth operation and the gcd of the ith and jth element.
# 5. We update the mx variable by taking the maximum of the mx and the score we just calculated and the solve function with the new mask and op+1.
# 6. Finally we return the mx variable.
# 7. We call the solve function with the initial mask as 0 and the initial op as 1.

# Time Complexity: O(2^n * n^2) where n is the length of the nums array. We have 2^n states and for each state we iterate over all possible pairs of numbers which takes n^2 time.

# Space Complexity: O(2^n) where n is the length of the nums array. We use memoization so we need space for the 2^n states.