class Solution:
    def largestDivisibleSubset(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr.sort()
        dp = [1]*n
        hash = [i for i in range(n)]
        for i in range(1, n):
            for j in range(i):
                if arr[i]%arr[j] == 0 and dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
                    hash[i] = j
        maxLen = max(dp)
        index = dp.index(maxLen)
        res = []
        while index != hash[index]:
            res.append(arr[index])
            index = hash[index]
        res.append(arr[index])
        return res[::-1]