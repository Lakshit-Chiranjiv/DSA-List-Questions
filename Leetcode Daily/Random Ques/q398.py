class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        mp = {}
        for i in range(len(nums)):
            if mp.get(nums[i],-1) == -1:
                mp[nums[i]] = [i]
            else:
                mp[nums[i]].append(i)
        self.mp = mp

    def pick(self, target: int) -> int:
        return random.choice(self.mp[target])