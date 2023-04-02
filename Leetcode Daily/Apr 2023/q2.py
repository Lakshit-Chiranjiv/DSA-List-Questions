class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = potions[len(potions)-1]
        arr = [0]*(n+2)
        j = len(potions)-1
        i = n

        while j >= 0:
            if i == potions[j]:
                if arr[i] > 0:
                    arr[i] += 1
                else:
                    arr[i] = (arr[i+1]+1)
                j -= 1
                if j < 0:
                    break
            
            while i > potions[j]:
                i -= 1
                if i != potions[j]:
                    arr[i] = arr[i+1]
        i -= 1
        while i >= 0:
            arr[i] = arr[i+1]
            i -= 1
        ans = []
        for x in spells:
            d = int(math.ceil(success/x))
            if d >= len(arr):
                ans.append(0)
                continue
            ans.append(arr[d])

        return ans

# intution: 
# 1. Here we need something which can tell us how many elements are greater than or equal to a given number.
# 2. Using this, we can iterate over the spells array , find the divisor of success and find the number of potions greater than or equal to that number.
# 3. We can use a prefix sum array to find the number of potions greater than or equal to a given number iterating from the end of the potions array.

# solution:
# 1. Sort the potions array.
# 2. Create a prefix sum array of size potions[len(potions)-1]+2 and initialize it with 0.
# 3. Initialize two pointers i and j to the last element of the potions array and the last element of the prefix sum array respectively.
# 4. Run a while loop until j >= 0.
# 5. If i == potions[j], then check if the value at arr[i] is greater than 0, if yes, then increment it by 1, else assign it the value of arr[i+1]+1.
# 6. Incrementing by 1 when value is greater than 0 tells that the same value is repeated in the potions array.
# 7. Then decrement j by 1.
# 8. If j < 0, then break the loop.
# 9. Run another while loop while i > potions[j] inside the first while loop.
# 10. Decrement i by 1.
# 11. If i != potions[j], then assign arr[i] the value of arr[i+1].
# 12. After the while loop, decrement i by 1.
# 13. Run another while loop while i >= 0 independent of the first while loop.
# 14. Assign arr[i] the value of arr[i+1] and decrement i by 1.
# 15. Now, iterate over the spells array and find the divisor of success.
# 16. If the divisor is greater than or equal to the length of the prefix sum array, then append 0 to the ans array.
# 17. Else, append the value at arr[divisor] to the ans array.
# 18. Return the ans array.


