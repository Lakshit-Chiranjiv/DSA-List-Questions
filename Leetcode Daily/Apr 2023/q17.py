class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        mx = max(candies)
        for i in candies:
            if i+extraCandies >= mx:
                ans.append(True)
            else:
                ans.append(False)

        return ans
    
# intution:
# 1. Just iterate over the candies array and check if the current element + extraCandies >= max(candies) and append the result to the ans array.
# 2. Return the ans array.

# solution:
# 1. Create a variable ans and initialize it to an empty array.
# 2. Create a variable mx and initialize it to the maximum element in the candies array.
# 3. Create a for loop which iterates over the candies array and in each iteration, we check if the current element + extraCandies >= mx.
# 4. If yes, append True to the ans array else append False to the ans array.
# 5. Return the ans array.

# time complexity: O(n) where n is the length of the candies array as we iterate over the candies array once.
# space complexity: O(n) where n is the length of the candies array as we create an ans array of size n. If we don't consider the space taken by the ans array, then the space complexity is O(1) as we don't use any extra space.

