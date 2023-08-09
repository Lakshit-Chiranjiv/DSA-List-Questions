class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        def check(mid):
            count = 0
            usedPrev = False
            for d in dif:
                if d<=mid:
                    if usedPrev==False:
                        count += 1
                        usedPrev = True
                    else:
                        usedPrev = False
                else:
                    usedPrev = False
            return count >= p
        
        nums.sort()
        dif = [nums[i]-nums[i-1] for i in range(1,len(nums))]
        s = min(dif)-1
        e = nums[-1] - nums[0]
        while s<e:
            mid = (s+e)//2
            if check(mid):
                e = mid
            else:
                s = mid+1
        return s