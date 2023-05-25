class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0:
            return 1.0

        wsum = 0
        for i in range(k, k+maxPts):
            wsum += 1 if i <= n else 0

        dp = {}
        for i in range(k-1, -1, -1):
            dp[i] = wsum/maxPts
            rem = 0
            if i+maxPts <= n:
                rem = dp.get(i+maxPts,1)

            wsum += (dp[i] - rem)

        return dp[0]
    
# intuition:
# 1. Treating it as a sliding window problem, we can see that the window size is maxPts.
# 2. For each index, we have to ensure whether that index can suffice the condition of the problem i.e. it should be less than or equal to n. If it is, then we add 1 to the window sum, else we add 0.
# 3. Then we have to find the probability of each index. For that, we have to divide the window sum by maxPts for each index.
# 4. Now, we have to find the probability of each index from k-1 to 0. For that, we can use a dictionary to store the probability of each index. 
# 5. For each index, we have to find the window sum of the next index and subtract the probability of the next index from it. Then we have to add the probability of the current index to it.
# 6. We have to do this for each index from k-1 to 0.
# 7. Finally, we return the probability of the 0th index.

# solution:
# 1. Check if k is 0. If it is, then return 1.0 as the probability of reaching 0 is 1.
# 2. Run a loop from k to k+maxPts. If the index is less than or equal to n, then add 1 to the window sum, else add 0.
# 3. Create a dictionary to store the probability of each index.
# 4. Run a loop from k-1 to -1 with a step of -1. For each index, find the window sum and divide it by maxPts. Store it in the dictionary.
# 5. Initialize a variable rem to 0. If i+maxPts is less than or equal to n, then find the probability of i+maxPts from the dictionary and store it in rem. Else, store 1 in rem. 
# 6. This is checked to keep track of the window size. If the window size is less than maxPts, then we have to add the probability of the next index to the window sum. Else, we have to subtract the probability of the next index from the window sum.
# 7. Update the window sum by subtracting rem from it and adding the probability of the current index to it.
# 8. Return the probability of the 0th index from the dictionary.