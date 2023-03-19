class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums.copy()
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums