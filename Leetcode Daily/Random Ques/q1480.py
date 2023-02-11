def runningSum(self, nums: List[int]) -> List[int]:
    rs = []
    rs.append(nums[0])

    for i in range(1,len(nums)):
        rs.append(rs[i-1]+nums[i])

    return rs  