class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        out.append(nums[0])
        n = len(nums)
        for i in range(1,n):
            out.append(out[i-1] * nums[i])

        rp = 1
        for i in range(n-1,0,-1):
            out[i] = out[i-1] * rp
            rp = rp * nums[i]
        
        out[0] = rp
        return out

# 238. Product of Array Except Self
# Time Complexity: O(n)
# Space Complexity: O(1)

# We create an array to store the product of the elements to the left of the current element. We then iterate from the end of the array and keep updating the current element with the product of the elements to the left of the current element and the product of the elements to the right of the current element. All this time we maintain a variable to store the product of the elements to the right of the current element. At the end, we update the first element of the array with the product of the elements to the right of the first element and return the array.