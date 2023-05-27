class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def solve(i):
            if i >= len(stoneValue):
                return 0
            
            ans = float('-inf')
            for j in range(i,min(i+3,len(stoneValue))):
                ans = max(ans, sum(stoneValue[i:j+1])-solve(j+1))

            return ans

        return "Alice" if solve(0)>0 else ("Bob" if solve(0)<0 else "Tie")

# intuition:
# 1. A similar dp function can be used like in stone game 2. But this time we need to keep track of the score of both players.
# 2. Here we have to return the result of game, so basically we need to know the difference between the scores of both players.
# 3. That is exactly what our function will do. When it is Alice's turn, it will return Alice's score - Bob's score. And when it is Bob's turn, it will return Bob's score - Alice's score.
# 4. This can be achieved recursively by subtracting the result of the next player's turn from the current player's turn.
# 5. Finally, we will check if the result is positive, negative or zero and return the result accordingly.

# solution:
# 1. Create a function solve(i) which will return the difference between the scores of Alice and Bob if the game starts from index i.
# 2. In the function, we will check if the index is out of bounds. If it is, we will return 0.
# 3. If the index is not out of bounds, we will iterate over the next 3 indices and call the function recursively.
# 4. ans will be the maximum of ans and the difference between the sum of the current subarray and the result of the next player's turn.
# 5. Finally, we will return ans.
# 6. In the main function, we will call solve(0) and check if the result is positive, negative or zero and return the result accordingly.

# Time Complexity: O(n) where n is the length of the array. This is because we are using memoization and its a 1D dp with a for loop iterating over 3 elements at max which is constant and can be ignored.

# Space Complexity: O(n) where n is the length of the array. We are storing the result of each index in the dp array or map.