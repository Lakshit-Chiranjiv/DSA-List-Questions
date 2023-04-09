class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        num = nums[0][0]
        for i in nums:
            for j in i:
                num = max(num,j)
        prime = [True for i in range(num+1)]
        p = 2
        while (p * p <= num):
            if (prime[p] == True):
                for i in range(p * 2, num+1, p):
                    prime[i] = False
            p += 1
            
        prime[1] = False
        mx = 0
        for i in range(len(nums)):
            if prime[nums[i][i]] and nums[i][i] > mx:
                mx = nums[i][i]
            if prime[nums[i][len(nums) - i - 1]] and nums[i][len(nums) - i - 1] > mx:
                mx = nums[i][len(nums) - i - 1]
        
        return mx