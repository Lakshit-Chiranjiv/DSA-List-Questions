class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left = 0
        right = max(nums)

        def check(k):
            have = 0
            for i in nums:
                if i <= k:
                    have += (k - i)
                else:
                    if have < (i - k):
                        return False
                    else:
                        have -= (i - k)

            return True

        while left < right:
            mid = (left + right)//2
            if check(mid):
                right = mid
            else:
                left = mid+1

        return left


# intution:
# 1. Binary search can be used to find the minimum value of the array.
# 2. We can use the check if mid can be achieved by the given set of operations.
# 3. To check if mid can be achieved, we can use the following algorithm:
# 4. For each element in the array, if the element is less than or equal to mid, then we need to add (mid - element) to achieve mid and for that the next element should be greater than mid by (mid - element). If it is not greater than mid by (mid - element), then we cannot achieve mid and we return False.

# solution:
# 1. Initialize left to 0 and right to the maximum element in the array.
# 2. While left is less than right, do the following:
# 3. Initialize mid to (left + right)//2.
# 4. If check(mid) returns True, then we can achieve mid. So, we set right to mid.
# 5. Else, we set left to mid + 1.
# 6. In check, we initialize a variable have to 0.
# 7. Iterate over the array and check if the element is less than or equal to mid. If it is, then we add (mid - element) to have. If it is not, then we check if have is less than (element - mid). If it is, then we cannot achieve mid and we return False. Else, we subtract (element - mid) from have.
# 8. If we have not returned False, then we can achieve mid and we return True.
# 9. Return left at the end.