import bisect

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        res = []
        dp = [10**8]*(len(obstacles)+1)

        for i in obstacles:
            idx = bisect.bisect(dp,i)
            res.append(idx+1)
            dp[idx] = i
        
        return res
    
# intuition:
# 1. We need to find the longest increasing subsequence in the array (obstacles) till the current index for each index.
# 2. We can use binary search to find the index of the first element in the dp array which is greater than the current element and the very next index will be the length of the longest increasing subsequence till the current index.


# solution:
# 1. Create a dp array of size n+1 and initialize it with 10^8, also create a res array.
# 2. Iterate over the obstacles array and for each element find the index of the first element in the dp array which is greater than the current element using binary search.
# 3. Append the index+1 to the res array and update the dp array at index idx with the current element.
# 4. Return the res array.