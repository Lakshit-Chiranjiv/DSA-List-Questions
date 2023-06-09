class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        while i < len(letters) and letters[i] <= target:
            i += 1
        if i >= len(letters):
            return letters[0]
        return letters[i]
    
# intuition:
# 1. Simply iterate through the list and find the first element greater than target. 
# 2. Can also use binary search to find the first element greater than target as the list is sorted.

# solution:
# 1. Create a iterator variable i = 0
# 2. Run a while loop till i < len(letters) and letters[i] <= target. Increment i by 1 in each iteration.
# 3. If i >= len(letters), return letters[0] as the there is no element greater than target in the list.
# 4. Else return letters[i] as it is the first element greater than target.

# Time Complexity: O(n)
# Space Complexity: O(1)