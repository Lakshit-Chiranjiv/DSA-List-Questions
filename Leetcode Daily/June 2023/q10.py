class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def calc_sum(cnt, end):
            if cnt == 0:
                return 0
            start = max(end - cnt, 0)
            sum1 = end * (1 + end) // 2
            sum2 = start * (1 + start) // 2
            return sum1 - sum2

        maxSum -= n
        l, r = 0, maxSum
        while l <= r:
            mid = (l + r) // 2
            left_sum = calc_sum(index + 1, mid)
            right_sum = calc_sum(n - index - 1, mid - 1)
            if left_sum + right_sum <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
# intuition:
# 1. Binary search approach will be followed to find the maximum value which satisfies the given conditions.
# 2. Start with mid and check if the sum of left and right side of the array is less than or equal to maxSum.
# 3. Also making sure, the difference between consecutive elements is not greater than 1.

# solution:
# 1. Define a function to calc_sum which takes count and end as parameters. If count is 0, return 0. Else, initialize start as max(end - count, 0). Calculate sum1 as end * (1 + end) // 2 and sum2 as start * (1 + start) // 2. Return sum1 - sum2.
# 2. Subtract n from maxSum. Initialize l as 0 and r as maxSum.
# 3. Iterate until l <= r. Initialize mid as (l + r) // 2. Calculate left_sum as calc_sum(index + 1, mid) and right_sum as calc_sum(n - index - 1, mid - 1).
# 4. If left_sum + right_sum <= maxSum, update l as mid + 1. Else, update r as mid - 1.
# 5. Return l.

# Time Complexity: O(log(maxSum))
# Space Complexity: O(1)