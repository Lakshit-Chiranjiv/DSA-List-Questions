class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1 for _ in range(n)]
        cnt = [1 for _ in range(n)]
        for ind in range(1,n):
            for prev_ind in range(ind):
                if arr[ind] > arr[prev_ind] and dp[ind] < dp[prev_ind] + 1:
                    dp[ind] = dp[prev_ind] + 1
                    cnt[ind] = cnt[prev_ind]
                elif arr[ind] > arr[prev_ind] and dp[ind] == dp[prev_ind] + 1:
                    cnt[ind] += cnt[prev_ind]
            
        mx = max(dp)
        count = 0
        for i in range(n):
            if dp[i] == mx:
                count += cnt[i]
        return count