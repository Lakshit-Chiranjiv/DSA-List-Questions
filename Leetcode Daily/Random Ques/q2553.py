class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            x = str(i)
            if len(x) > 1:
                z = list(map(int,list(x)))
                ans = ans + z
            else:
                ans.append(i)
                
        return ans
        