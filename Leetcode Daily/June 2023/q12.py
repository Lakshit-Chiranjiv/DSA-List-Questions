class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        s = str(nums[0])
        prev = nums[0]
        if nums[-1] != -2 and nums[-1] != 0:
            nums.append(-1)
        else:
            nums.append(2**31)
        for i in nums[1:]:
            if abs(i - prev) != 1:
                if int(s) != prev:
                    s += '->'+str(prev)
                ans.append(s)
                s = str(i)
            prev = i
        return ans
    
# intuition:
# 1. Append a number that is not in the array to the end of the array to account for the last range comparison.
# 2. If the difference between the current number and the previous number is not 1, then we have reached the end of a range. Append the range to the answer array and reset the range string.
# 3. If the difference between the current number and the previous number is 1, then we are still in the same range. Update the previous number and continue.

# solution:
# 1. Initialize an empty array to store the answer.
# 2. Initialize a string to store the current range.
# 3. If the array is empty, return the answer array.
# 4. If the last number in the array is not -2 or 0, then append -1 to the array. Else, append 2^31 to the array.
# 5. Initialize a variable to store the previous number. Set it to the first number in the array.
# 6. Iterate over the array from the second number to the last number. If the difference between the current number and the previous number is not 1, then we have reached the end of a range. If integer value of the range string is not equal to the previous number, then append the previous number to the range string. Append the range string to the answer array. Reset the range string to the current number. Else, we are still in the same range. Update the previous number to the current number and continue.
# 7. Return the answer array.

# Time Complexity: O(n)
# Space Complexity: O(n)