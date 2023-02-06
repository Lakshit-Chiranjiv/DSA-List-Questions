def shuffle(self, nums: List[int], n: int) -> List[int]:
    x = 0
    y = len(nums)//2
    ans = []
    for i in range(len(nums)//2):
        ans.append(nums[x])
        ans.append(nums[y])
        x += 1
        y += 1
    
    return ans