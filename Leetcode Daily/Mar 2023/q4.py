class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        x = nums
        n = len(nums)
        for i in range(n):
            if maxK < x[i] or x[i] < minK:
                x[i] = -1
        minK_found = 0
        maxK_found = 0
        wind_left = 0
        wind_right = 0
        last_minK_idx = -1
        last_maxK_idx = -1
        ans = 0
        while wind_right < n:
            if x[wind_right] == -1:
                minK_found = 0
                maxK_found = 0
                last_minK_idx = -1
                last_maxK_idx = -1
                wind_left = wind_right + 1
            if minK <= x[wind_right] <= maxK:
                if x[wind_right] == minK:
                    minK_found = 1
                    last_minK_idx = wind_right
                if x[wind_right] == maxK:
                    maxK_found = 1
                    last_maxK_idx = wind_right
            if minK_found == 1 and maxK_found == 1:
                ans += (min(last_minK_idx,last_maxK_idx) - wind_left + 1)
            wind_right += 1

        return ans

