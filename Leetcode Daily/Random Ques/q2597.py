class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        def solve(nums,idx,res,k,sub):
            if idx == len(nums):
                if len(sub) > 0:
                    res.append(sub)
                return
            if not (nums[idx]-k) in sub:
                sub.append(nums[idx])
                solve(nums,idx+1,res,k,sub)
                sub.pop()
                
            solve(nums,idx+1,res,k,sub)
        
        nums.sort()
        res = []
        solve(nums,0,res,k,[])
        
        return len(res)