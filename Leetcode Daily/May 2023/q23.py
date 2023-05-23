class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse = True)
        return self.nums[self.k-1]
    
# intuition:
# 1. Simply add the new element to the array and sort it in descending order. Then return the kth largest element.

# solution:
# 1. In the constructor, we initialize the array and the value of k.
# 2. In the add function, we append the new element to the array and sort it in descending order. Then we return the kth element from the array.