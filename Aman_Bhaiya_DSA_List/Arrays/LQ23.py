class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        out.append(nums[0])
        n = len(nums)
        for i in range(1,n):
            out.append(out[i-1] * nums[i])

        rp = 1
        for i in range(n-1,0,-1):
            out[i] = out[i-1] * rp
            rp = rp * nums[i]
        
        out[0] = rp
        return out

