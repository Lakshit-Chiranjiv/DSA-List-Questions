class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return

        n = len(nums)
        k = k % n
        x = nums[n-k:]
        y = nums[:n-k]
        nums[:k] = x
        nums[k:] = y