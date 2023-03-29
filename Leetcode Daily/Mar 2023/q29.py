class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction.sort()

        @cache
        def solve(i,t):
            if i == len(satisfaction):
                return 0

            pick = solve(i+1,t+1) + (t*satisfaction[i])
            not_pick = solve(i+1,t)

            return max(pick,not_pick)

        return solve(0,1)
    
# intution:
# 1. Its obvious we will sort the array in ascending order to have the time factor as high as possible for the higher satisfaction values
# 2. We will use a recursive function to solve this problem picking and not picking the current value at each step and return the max of the two
# 3. We will use memoization to store the results of the subproblems to avoid recomputation
# 4. Starting from first index and time as 1, we will return the max of the two cases (pick and not pick)
# 5. We will return 0 if we reach the end of the array

# solution:
# 1. Sort the array
# 2. Define a recursive function with memoization using cache decorator
# 3. The recursive function will take the index and time as parameters
# 4. If we reach the end of the array, we will return 0
# 5. Pick case will be the recursive call with index+1 and time+1 added to the product of the current satisfaction value and time
# 6. Not pick case will be the recursive call with index+1 and time
# 7. We will return the max of the two cases
# 8. We will return the recursive call with index 0 and time 1