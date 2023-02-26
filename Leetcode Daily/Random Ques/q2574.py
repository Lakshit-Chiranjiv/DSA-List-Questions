class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        lf = [0]
        rt = [0]
        for i in range(len(nums)-1):
            lf.append(lf[len(lf)-1]+nums[i])
        
        for i in range(len(nums)-1,0,-1):
            rt.insert(0,rt[0]+nums[i])
        
        ans = []
        for i in range(len(nums)):
            ans.append(abs(lf[i] - rt[i]))
            
        return ans